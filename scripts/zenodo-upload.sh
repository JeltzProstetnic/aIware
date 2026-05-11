#!/usr/bin/env bash
set -euo pipefail

# Zenodo v5+ upload script for FMT paper
# Usage: bash scripts/zenodo-upload.sh <pdf-path> [--dry-run]
#
# Reads ZENODO_TOKEN from .env.zenodo (gitignored).
# Creates a new version of the existing Zenodo deposit,
# uploads the PDF, updates metadata, and publishes.

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
PROJECT_DIR="$(dirname "$SCRIPT_DIR")"
ENV_FILE="$PROJECT_DIR/.env.zenodo"
API="https://zenodo.org/api"
CONCEPT_DOI="10.5281/zenodo.18669891"

# Load token
if [[ ! -f "$ENV_FILE" ]]; then
    echo "ERROR: $ENV_FILE not found. Create it with ZENODO_TOKEN=<your-token>"
    exit 1
fi
source "$ENV_FILE"
if [[ -z "${ZENODO_TOKEN:-}" ]]; then
    echo "ERROR: ZENODO_TOKEN not set in $ENV_FILE"
    exit 1
fi

# Args
PDF_PATH="${1:-}"
DRY_RUN=false
if [[ "${2:-}" == "--dry-run" ]] || [[ "${1:-}" == "--dry-run" ]]; then
    DRY_RUN=true
    if [[ "${1:-}" == "--dry-run" ]]; then
        PDF_PATH="${2:-}"
    fi
fi

if [[ -z "$PDF_PATH" ]]; then
    echo "Usage: bash scripts/zenodo-upload.sh <pdf-path> [--dry-run]"
    echo "       bash scripts/zenodo-upload.sh --dry-run  (metadata check only)"
    exit 1
fi

if [[ "$PDF_PATH" != "--dry-run" ]] && [[ ! -f "$PDF_PATH" ]]; then
    echo "ERROR: PDF not found: $PDF_PATH"
    exit 1
fi

AUTH="Authorization: Bearer $ZENODO_TOKEN"

echo "=== Zenodo Upload Script ==="
echo "PDF: $PDF_PATH"
echo "Concept DOI: $CONCEPT_DOI"
echo ""

# Step 1: Find the latest version's record ID via concept DOI
echo "[1/5] Resolving latest version..."
CONCEPT_ID="${CONCEPT_DOI##*.}"
LATEST=$(curl -sL -H "$AUTH" "$API/records/$CONCEPT_ID")
LATEST_ID=$(echo "$LATEST" | python3 -c "import sys,json; print(json.load(sys.stdin)['id'])")
LATEST_VERSION=$(echo "$LATEST" | python3 -c "import sys,json; m=json.load(sys.stdin)['metadata']; print(m.get('version','unknown'))")
echo "  Latest record: $LATEST_ID (version: $LATEST_VERSION)"

if $DRY_RUN; then
    echo ""
    echo "[DRY RUN] Would create new version from record $LATEST_ID"
    echo "[DRY RUN] Would upload: $PDF_PATH"
    echo "[DRY RUN] Would publish as next version"
    exit 0
fi

# Step 2: Create new version
echo "[2/5] Creating new version draft..."
NEW_VERSION=$(curl -sL -H "$AUTH" -X POST "$API/deposit/depositions/$LATEST_ID/actions/newversion")
DRAFT_URL=$(echo "$NEW_VERSION" | python3 -c "import sys,json; print(json.load(sys.stdin)['links']['latest_draft'])")
DRAFT_ID=$(echo "$DRAFT_URL" | grep -oP '\d+$')
echo "  Draft created: $DRAFT_ID"

# Step 3: Get the draft details (need bucket URL and existing files)
echo "[3/5] Preparing file upload..."
DRAFT=$(curl -sL -H "$AUTH" "$API/deposit/depositions/$DRAFT_ID")
BUCKET=$(echo "$DRAFT" | python3 -c "import sys,json; print(json.load(sys.stdin)['links']['bucket'])")

# Delete old files from the draft
OLD_FILES=$(echo "$DRAFT" | python3 -c "
import sys, json
d = json.load(sys.stdin)
for f in d.get('files', []):
    print(f['id'])
")
for fid in $OLD_FILES; do
    echo "  Removing old file: $fid"
    curl -sL -H "$AUTH" -X DELETE "$API/deposit/depositions/$DRAFT_ID/files/$fid" > /dev/null
done

# Upload new PDF
FILENAME=$(basename "$PDF_PATH")
echo "  Uploading: $FILENAME"
curl -sL -H "$AUTH" \
    -H "Content-Type: application/octet-stream" \
    --data-binary @"$PDF_PATH" \
    "$BUCKET/$FILENAME" > /dev/null
echo "  Upload complete."

# Step 4: Update metadata (bump version, add changelog)
echo "[4/5] Updating metadata..."
CURRENT_META=$(echo "$DRAFT" | python3 -c "
import sys, json
d = json.load(sys.stdin)
m = d['metadata']
# Print current version for incrementing
print(m.get('version', 'v4'))
")
echo "  Current version: $CURRENT_META"

# Read changelog from stdin or use default
CHANGELOG_FILE="$PROJECT_DIR/tmp/zenodo-changelog.md"
if [[ -f "$CHANGELOG_FILE" ]]; then
    CHANGELOG=$(cat "$CHANGELOG_FILE")
    echo "  Changelog loaded from $CHANGELOG_FILE"
else
    echo "  WARNING: No changelog file at $CHANGELOG_FILE"
    echo "  Create it before publishing, or the version notes will be empty."
    CHANGELOG="Version update."
fi

# Update version number and description
python3 -c "
import json, sys, os

# Read current draft metadata
draft_json = '''$(echo "$DRAFT" | python3 -c "import sys,json; json.dump(json.load(sys.stdin)['metadata'], sys.stdout)")'''
meta = json.loads(draft_json)

# Bump version
old_ver = meta.get('version', 'v4')
if old_ver.startswith('v'):
    new_num = int(old_ver[1:]) + 1
    meta['version'] = f'v{new_num}'
else:
    meta['version'] = 'v5'

# Update publication date
from datetime import date
meta['publication_date'] = date.today().isoformat()

# Append changelog to description
changelog = open('$CHANGELOG_FILE').read() if os.path.exists('$CHANGELOG_FILE') else 'Version update.'
if meta.get('description'):
    meta['description'] = meta['description'].rstrip()
    # Remove old changelog if present
    if '<h3>Changelog' in meta['description']:
        idx = meta['description'].index('<h3>Changelog')
        meta['description'] = meta['description'][:idx].rstrip()
    meta['description'] += f'\n\n<h3>Changelog {meta[\"version\"]}</h3>\n{changelog}'

print(json.dumps({'metadata': meta}))
" > /tmp/zenodo-meta-update.json

curl -sL -H "$AUTH" \
    -H "Content-Type: application/json" \
    -X PUT \
    --data-binary @/tmp/zenodo-meta-update.json \
    "$API/deposit/depositions/$DRAFT_ID" > /dev/null
echo "  Metadata updated."

# Step 5: Publish
echo "[5/5] Publishing..."
RESULT=$(curl -sL -H "$AUTH" -X POST "$API/deposit/depositions/$DRAFT_ID/actions/publish")
NEW_DOI=$(echo "$RESULT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('doi', 'UNKNOWN'))")
NEW_URL=$(echo "$RESULT" | python3 -c "import sys,json; print(json.load(sys.stdin).get('links', {}).get('record_html', 'UNKNOWN'))")

echo ""
echo "=== Published ==="
echo "  Version DOI: $NEW_DOI"
echo "  URL: $NEW_URL"
echo "  Concept DOI: $CONCEPT_DOI (auto-resolves to latest)"
echo ""
echo "No downstream link updates needed — concept DOI covers everything."
