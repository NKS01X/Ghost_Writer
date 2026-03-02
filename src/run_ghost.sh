#!/bin/bash
set -e

CHANGED_FILES=$(git diff --name-only HEAD~1 | grep -E '\.(js|ts|py|java|go|rb|php|rs|cs|cpp|c)$' | grep -v '\.test\.' || true)

if [ -z "$CHANGED_FILES" ]; then
  echo "No relevant files changed. Exiting."
  exit 0
fi

git config --global user.name "github-actions[bot]"
git config --global user.email "github-actions[bot]@users.noreply.github.com"

ORIGINAL_BRANCH=$(git rev-parse --abbrev-ref HEAD)
GHOST_BRANCH="ghost-tests-$(date +%s)"
git checkout -b "$GHOST_BRANCH"

for file in $CHANGED_FILES; do
  python3 src/ghost_writer.py "$file"
done

git add .
git commit -m "chore: automated tests via Grok 3 [skip ci]"
git push origin "$GHOST_BRANCH"

gh pr create --title "Ghost Writer: Unit Tests" --body "Tests generated for: $CHANGED_FILES" --base "$ORIGINAL_BRANCH" --head "$GHOST_BRANCH"