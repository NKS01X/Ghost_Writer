#!/bin/bash

CHANGED_FILES=$(git diff --name-only origin/main | grep '\.js$' | grep -v '\.test\.js$')

if [ -z "$CHANGED_FILES" ]; then
  exit 0
fi

git config --global user.name "github-actions[bot]"
git config --global user.email "github-actions[bot]@users.noreply.github.com"

BRANCH_NAME="ghost/tests-$(date +%s)"
git checkout -b "$BRANCH_NAME"

for file in "$CHANGED_FILES"; do
  python3 ghost_writer.py "$file"
done

git add .
git commit -m "chore: automated tests via GitHub Models (Grok)"
git push origin "$BRANCH_NAME"

GH_TOKEN=$GITHUB_TOKEN gh pr create --title "Ghost Writer: Grok-Generated Tests" --body "Tests created for: $CHANGED_FILES"