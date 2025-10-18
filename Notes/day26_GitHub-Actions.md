# GitHub Actions

## 1. Overview
**GitHub Actions** is a **CI/CD (Continuous Integration and Continuous Deployment)** tool built into GitHub.  
It automates workflows such as building, testing, and deploying code directly from your GitHub repository.  
Workflows are triggered by **events** like pushes, pull requests, or issues.

---

## 2. Key Concepts

### a. Workflow
- A **workflow** is an automated process defined in a **YAML file** inside `.github/workflows/`.
- Example: `.github/workflows/ci.yml`
- Can contain multiple **jobs** that run sequentially or in parallel.

### b. Event
- Triggers that start workflows.
- Common events:
  - `push`
  - `pull_request`
  - `schedule`
  - `workflow_dispatch`

### c. Job
- A **job** is a group of steps that run in the same **runner**.
- Jobs can depend on other jobs.
- Each job runs in a **fresh virtual environment**.

### d. Step
- Individual tasks in a job.
- Can be:
  - **Shell commands**
  - **Actions** (pre-built reusable components)

### e. Runner
- A **server (virtual machine)** that runs your workflow.
- Types:
  - **GitHub-hosted runners** (Ubuntu, Windows, macOS)
  - **Self-hosted runners** (your own servers)

---

## 3. Workflow File Structure (YAML)

```yaml
name: CI Pipeline

on:
  push:
    branches: [ main ]

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Setup Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 18

      - name: Install dependencies
        run: npm install

      - name: Run tests
        run: npm test
```

---

## 4. Built-in Actions
- `actions/checkout` → Clones your repository
- `actions/setup-node` → Installs Node.js
- `actions/upload-artifact` → Saves build artifacts
- `actions/download-artifact` → Retrieves saved artifacts
- `actions/cache` → Caches dependencies for faster builds

---

## 5. Workflow Triggers (Events)

| Event | Description |
|--------|--------------|
| `push` | Triggered when code is pushed |
| `pull_request` | Triggered when a PR is created/updated |
| `schedule` | Triggered on a defined time interval (CRON) |
| `workflow_dispatch` | Manual trigger from GitHub UI |
| `release` | Triggered when a release is published |
| `issue_comment` | Triggered on issue comment events |

---

## 6. Workflow Syntax

- **`runs-on`** → Specifies OS runner  
- **`needs`** → Specifies job dependencies  
- **`if`** → Conditional execution  
- **`env`** → Defines environment variables  
- **`with`** → Passes input parameters to actions  

Example:
```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    needs: build
    if: github.ref == 'refs/heads/main'
    env:
      DEPLOY_ENV: production
```

---

## 7. Secrets and Environment Variables
- **Secrets**: Encrypted variables (API keys, tokens)
  - Set in: `Settings → Secrets and variables → Actions`
  - Access with: `${{ secrets.MY_SECRET }}`
- **Environment variables**: Temporary variables for workflow.

---

## 8. Matrix Builds

Run jobs with multiple versions or configurations:
```yaml
strategy:
  matrix:
    node: [14, 16, 18]

steps:
  - uses: actions/setup-node@v4
    with:
      node-version: ${{ matrix.node }}
```

---

## 9. Artifacts & Caching

- **Artifacts**: Save build/test outputs.  
- **Caching**: Store dependencies to speed up builds.

```yaml
- uses: actions/cache@v4
  with:
    path: ~/.npm
    key: ${{ runner.os }}-node-${{ hashFiles('package-lock.json') }}
```

---

## 10. Reusable Workflows

You can reuse workflows across repositories:
```yaml
jobs:
  call-workflow:
    uses: org/repo/.github/workflows/deploy.yml@main
```

---

## 11. Continuous Deployment Example

```yaml
on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to Server
        run: |
          ssh user@server "cd /app && git pull && npm install && systemctl restart app"
```

---

## 12. Advantages
- Integrated directly with GitHub  
- Easy YAML configuration  
- Supports Linux, macOS, and Windows  
- Free minutes for public repositories  
- Scalable and reusable

---

## 13. Common Use Cases
- Automated testing  
- Code linting & formatting  
- Deployment to cloud (AWS, Azure, GCP)  
- Docker image builds  
- Documentation generation  
- Notifications (Slack, Discord)

---
