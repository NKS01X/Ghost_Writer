#!/bin/bash

CHANGED_FILES=$(git diff --name-only origin/master | grep '\.js$' | grep -v '\.test\.js$')

if [ -z "$CHANGED_FILES" ]; then
  exit 0
fi

git config --global user.name "github-actions[bot]"
git config --global user.email "github-actions[bot]@users.noreply.github.com"

BRANCH_NAME="ghost/tests-$(date +%s)"
git checkout -b "$BRANCH_NAME"

for file in $CHANGED_FILES; do
  # Points to the new location in src/
  python3 src/ghost_writer.py "$file"
done

git add .
git commit -m "chore: automated tests via Grok 3"
git push origin "$BRANCH_NAME"

gh pr create --title "Ghost Writer: Unit Tests" --body "Tests generated for: $CHANGED_FILES"