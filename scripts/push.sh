#!/bin/bash
# push.sh — Dual push: private (all) + public (filtered)
# Private gets everything. Public excludes: tmp/, scripts/, session-context.md, docs/
set -e

REPO_ROOT="$(git rev-parse --show-toplevel)"
cd "$REPO_ROOT"

# Paths excluded from public repo
PRIVATE_PATHS=(tmp scripts session-context.md docs)

echo "=== Pushing to private (full content) ==="
git push private main

echo ""
echo "=== Preparing public push ==="

# Create a temporary index to build a filtered tree
TEMP_INDEX=$(mktemp)
trap "rm -f $TEMP_INDEX" EXIT
export GIT_INDEX_FILE="$TEMP_INDEX"

# Read main's tree into the temp index
git read-tree main

# Remove private paths from the temp index
for path in "${PRIVATE_PATHS[@]}"; do
  git rm -r --cached --quiet "$path" 2>/dev/null || true
done

# Write the filtered tree
TREE=$(git write-tree)

# Restore normal index
unset GIT_INDEX_FILE

# Determine parent for the public commit
PARENT_ARG=""
if git rev-parse --verify refs/remotes/origin/main &>/dev/null; then
  PARENT_ARG="-p $(git rev-parse refs/remotes/origin/main)"
fi

# Use main's commit message for the public commit
MAIN_MSG=$(git log -1 --format=%B main)
COMMIT=$(echo "$MAIN_MSG" | git commit-tree "$TREE" $PARENT_ARG)

# Check if this is actually a new commit (tree differs from current public HEAD)
if git rev-parse --verify refs/remotes/origin/main &>/dev/null; then
  CURRENT_PUBLIC_TREE=$(git rev-parse refs/remotes/origin/main^{tree} 2>/dev/null || echo "none")
  if [ "$TREE" = "$CURRENT_PUBLIC_TREE" ]; then
    echo "Public repo already up to date."
    exit 0
  fi
fi

echo "=== Pushing to public (filtered) ==="
git push origin "$COMMIT:refs/heads/main"

echo ""
echo "Done. Private: full push. Public: filtered (excluded: ${PRIVATE_PATHS[*]})"
