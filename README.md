# 👻 Ghost Writer CI

**Ghost Writer** is an end-to-end automated testing pipeline powered by **Grok 3** (via GitHub Models). It monitors your active feature branches, automatically writes your test suites for you, and securely auto-merges your code to `master` after validating it in an isolated Docker environment.

---

## 🚀 How it Works



<img width="1024" height="559" alt="image" src="https://github.com/user-attachments/assets/e9dfcd14-dae2-481e-af15-d2ab17391124" />



The pipeline operates in two distinct phases:

### Phase 1: AI Test Generation (Feature Branch)
1. **Push Code:** A developer pushes new source code (e.g., `.js`, `.py`) to their working branch.
2. **CI Trigger:** GitHub Actions identifies the newly changed files.
3. **AI Generation:** The "Ghost" script sends the new code to Grok 3 to generate the corresponding unit tests.
4. **Pull Request:** A temporary branch (`ghost/tests-...`) is created, and a PR is opened targeting the **original working branch**.
5. **Clean Up:** Once the developer reviews and merges the generated tests into their working branch, the temporary ghost branch is automatically deleted.

### Phase 2: Docker Validation & Auto-Merge (Master Branch)
1. **Target Master:** The developer opens a PR from their feature branch (now containing the code + generated tests) into the `master` branch.
2. **Docker Build:** The `PR Test Validator` workflow triggers, building a fresh Docker image (`pr-tests`) to ensure an isolated testing environment.
3. **Automated Execution:** The tests are executed inside the Docker container.
4. **Outcome Action:**  ✅ **Success:** The bot comments "All tests passed. Auto-merging." and automatically merges the PR into `master`.
    ❌ **Failure:** The bot comments with the exact terminal error output and instantly closes the PR, preventing broken code from reaching production.

---

## 📁 Project Structure

* `src/ghost_writer.py` - The AI logic (GitHub Models integration).
* `src/run_ghost.sh` - The Git orchestrator (Diffing, Branching, PR creation).
* `.github/workflows/ghost.yml` - The AI test generation trigger for feature branches.
* `.github/workflows/valid.yml` - The Docker validation and auto-merge trigger for the master branch.
* `Dockerfile` - The container configuration for running the test suite.

---

## 🛠 Setup & Requirements

### 1. Secrets Configuration
Ensure the following secrets are added to your GitHub Repository (**Settings > Secrets and variables > Actions**):
* `GH_MODELS_TOKEN`: A Personal Access Token (PAT) with `models:read` permissions.
* `GITHUB_TOKEN`: Automatically handled by GitHub Actions (used by the GitHub CLI `gh` to create, comment, and merge PRs).

### 2. Workflow Permissions
Go to **Settings > Actions > General** and set **Workflow permissions** to:
* `Read and write permissions`
* Check `Allow GitHub Actions to create and approve pull requests`.

### 3. Repository Settings for Auto-Merge & Cleanup
To ensure smooth operation of the workflows:
* Go to **Settings > General**.
* Scroll down to the **Pull Requests** section.
* Check **Allow auto-merge** (Required for the bot to run `gh pr merge`).
* Check **Automatically delete head branches** (Keeps the repo clean after Ghost branches and feature branches are merged).

---

## 🧪 Triggering the Pipeline
To see the full pipeline in action:

```bash
# 1. Create a feature branch and push code
git checkout -b feature/new-logic
git add src/logic.js
git commit -m "feat: add business logic"
git push origin feature/new-logic

# -> Ghost Writer opens a PR with logic.test.js. Merge it into your feature branch.

# 2. Open a PR from your feature branch to master
gh pr create --base master --head feature/new-logic --title "Merge new logic to master" --body "Testing auto-merge pipeline."

# -> PR Test Validator builds Docker, runs the tests, and auto-merges if successful!
