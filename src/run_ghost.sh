#!/bin/bash
set -e

CHANGED_FILES=$(git diff --name-only HEAD~1 | grep -E '\.(js|ts|py|java|go|rb|php|rs|cs|cpp|c)$' | grep -v '\.test\.' || true)

if [ -z "$CHANGED_FILES" ]; then
  echo "No relevant files changed. Exiting."
  exit 0
fi

git config --global user.name "github-actions[bot]"
git config --global user.email "github-actions[bot]@users.noreply.github.com"

BRANCH_NAME="feature/ghost-tests-$(date +%s)"
git checkout -b "$BRANCH_NAME"

for file in $CHANGED_FILES; do
  python3 src/ghost_writer.py "$file"
done

git add .
git commit -m "chore: automated tests via Grok 3"
git push origin "$BRANCH_NAME"

gh pr create --title "Ghost Writer: Unit Tests" --body "Tests generated for: $CHANGED_FILES" --base main