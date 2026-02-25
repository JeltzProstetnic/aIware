#!/bin/bash
# push.sh — Dual push: private (all) + public (filtered)
# Private gets everything. Public excludes: tmp/, scripts/, session-context.md, docs/
set -e

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

# Pull from private before pushing to prevent multi-machine divergence
echo "=== Syncing with private remote ==="
git fetch private
LOCAL=$(git rev-parse main)
REMOTE=$(git rev-parse private/main 2>/dev/null || echo "none")
BASE=$(git merge-base main private/main 2>/dev/null || echo "none")

if [ "$REMOTE" != "none" ] && [ "$LOCAL" != "$REMOTE" ] && [ "$BASE" = "$LOCAL" ]; then
  # Remote is ahead — fast-forward
  echo "Fast-forwarding to private/main..."
  git merge --ff-only private/main
elif [ "$REMOTE" != "none" ] && [ "$LOCAL" != "$REMOTE" ] && [ "$BASE" != "$LOCAL" ]; then
  # Diverged — abort and let user resolve
  echo "ERROR: Local and private/main have diverged!"
  echo "  Local:  $LOCAL"
  echo "  Remote: $REMOTE"
  echo "  Base:   $BASE"
  echo "Run 'git pull --rebase private main' to resolve, then retry."
  exit 1
fi

# Paths excluded from public repo
PRIVATE_PATHS=(tmp scripts session-context.md docs pop-sci/video-script.md pop-sci/podcast-script.md pop-sci/linkedin-post.md pop-sci/magazine-article.md pop-sci/magazine-article.html pop-sci/book-outline-expanded.md pop-sci/perplexity-review.md)

# Glob patterns excluded from public repo (book manuscript & build artifacts)
PRIVATE_GLOBS=("pop-sci/book-manuscript*" "pop-sci/isbn-barcode*")

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

# Remove glob patterns from the temp index
for glob in "${PRIVATE_GLOBS[@]}"; do
  git rm -r --cached --quiet -- $glob 2>/dev/null || true
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
