# 👻 Ghost Writer CI

**Ghost Writer** is an automated unit test generation engine powered by **Grok 3** (via GitHub Models). It monitors your feature branches and automatically writes your test suites for you.

---

## 🚀 How it Works

1. **Push Code:** Developer pushes a new `.js` file to any branch starting with `feature/`.
2. **CI Trigger:** GitHub Actions identifies the changes by comparing the branch against `master`.
3. **AI Generation:** The "Ghost" sends the new code to Grok 3.
4. **Pull Request:** A new branch is created, and a PR is opened containing the generated `.test.js` files.



---

## 📁 Project Structure

* `src/ghost_writer.py` - The AI logic (GitHub Models integration).
* `src/run_ghost.sh` - The Git orchestrator (Diffing, Branching, PR creation).
* `.github/workflows/ghost.yml` - The automation trigger.

---

## 🛠 Setup & Requirements

### 1. Secrets Configuration
Ensure the following secrets are added to your GitHub Repository (**Settings > Secrets and variables > Actions**):
* `GH_MODELS_TOKEN`: A Personal Access Token (PAT) with `models:read` permissions.
* `GITHUB_TOKEN`: Automatically handled by GitHub Actions (ensure "Allow GitHub Actions to create PRs" is enabled in Settings).

### 2. Workflow Permissions
Go to **Settings > Actions > General** and set **Workflow permissions** to:
* `Read and write permissions`
* Check `Allow GitHub Actions to create and approve pull requests`.

---

## 🧪 Triggering a Test
To see the Ghost in action, simply create a new feature branch and push a JavaScript file:

```bash
git checkout -b feature/new-logic
# Create a .js file in src/
git add .
git commit -m "feat: add business logic"
git push origin feature/new-logic
