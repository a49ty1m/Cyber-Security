# 🕵️ Gitleaks: Complete Mastery Checklist

> **What is Gitleaks?** Gitleaks is an open-source SAST tool specifically designed to detect hardcoded secrets — API keys, tokens, passwords, SSH private keys, connection strings, and other credentials — in Git repositories. It scans the entire Git history (not just the current state of the code), meaning a secret committed and then deleted a year ago is still detected. Gitleaks includes 200+ built-in detection rules for common secret patterns (AWS keys, GitHub tokens, Stripe keys, Slack tokens, etc.).
>
> **Why does it exist?** Developers accidentally commit secrets constantly. A quick `git log` reveals that secrets often get committed, then deleted in a follow-up commit — but they're still in the Git history forever (unless the history is explicitly purged). Attackers who clone a public repo or gain access to a private one immediately run secret scanning tools. Gitleaks makes it easy to catch these secrets before — or after — they're exposed.
>
> **When to use it:** Pre-commit hook (prevent secrets from ever being committed), CI/CD pipeline (fail builds when secrets are detected), auditing existing repositories for historical secrets, and security assessments of client source code repositories.
>
> **When to avoid it:** Gitleaks produces false positives on high-entropy strings that aren't secrets (UUIDs, test certificates, base64-encoded data). Tune rules and use `.gitleaksignore` for known safe patterns. Don't use Gitleaks as your only secret scanning tool — pair with TruffleHog for comprehensive coverage.
>
> **What mastering Gitleaks unlocks:** The ability to find leaked credentials in any repository (offensive capability), implement preventive secret scanning in development workflows (defensive capability), and achieve the Phase 8 exit gate of a CI/CD security pipeline with secret scanning.
>
> **Roadmap Stage / Module:** Shelf: Module S12 & S13 (Supply Chain & DevSecOps)

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| Secrets Scanning | SAST | IaC Security |
|:----------------|:-----|:-------------|
| **🕵️ Gitleaks** (you are here) | [🔍 Semgrep](Semgrep.md) | [✅ Checkov](Checkov.md) |
| [🔎 TruffleHog](TruffleHog.md) | | [🛡️ tfsec](tfsec.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & First Scan | 4 | 1 hour |
| 2 | Git History & Commit Scanning | 6 | 2–3 hours |
| 3 | Custom Rules & Tuning | 7 | 3–4 hours |
| 4 | Pre-Commit Hooks | 4 | 1–2 hours |
| 5 | CI/CD Integration (GitHub Actions) | 5 | 2–3 hours |
| 6 | Offensive Use — Repo Auditing | 5 | 2–3 hours |
| 7 | Practical Labs | 4 | 3–5 hours |
| | **Total** | **35** | **~14–21 hours** |

**Prerequisites:** Phase 1 complete. Git basics (clone, commit, log, history). Phase 8 DevSecOps fundamentals.

---

# PHASE 1: INSTALLATION & FIRST SCAN

---

## 1.1 Installation

```bash
# Option 1: Download binary (recommended — no Python dependency)
# Go to https://github.com/gitleaks/gitleaks/releases
wget https://github.com/gitleaks/gitleaks/releases/latest/download/gitleaks_8.18.0_linux_x64.tar.gz
tar xvf gitleaks_8.18.0_linux_x64.tar.gz
sudo mv gitleaks /usr/local/bin/
gitleaks version

# Option 2: Go install
go install github.com/gitleaks/gitleaks/v8@latest

# Option 3: Docker
docker run --rm -v "${PWD}:/path" zricethezav/gitleaks:latest dir /path

# Option 4: Package manager
brew install gitleaks    # macOS
```

## 1.2 First Scan

```bash
# Scan a local repository (entire git history)
gitleaks detect --source /path/to/repo

# Scan a local directory (not a git repo — just files)
gitleaks detect --source /path/to/dir --no-git

# Scan the current directory
cd /my/project && gitleaks detect

# Output: shows findings inline + summary
# Example output:
# ○
# ○
# ○
#     ○○○
# ...
# Finding:     ⚠️  secret=AIzaSy...
# Secret:      AIzaSyExample...
# RuleID:      google-api-key
# Entropy:     4.71
# File:        config/settings.py
# Line:        42
# Commit:      a1b2c3d4
# Author:      developer@example.com
# Date:        2023-10-15

# Exit codes:
# 0 = no leaks found
# 1 = leaks found
# 126 = error
```

---

# PHASE 2: GIT HISTORY & COMMIT SCANNING

---

## 2.1 Scanning Modes

```bash
# Scan entire git history (default — most thorough)
gitleaks detect --source /path/to/repo --log-level debug

# Scan only current working tree (faster, misses historical secrets)
gitleaks detect --source /path/to/repo --no-git

# Scan a specific commit range (for CI/CD — only scan new commits)
gitleaks detect --log-opts "HEAD~5..HEAD"    # Last 5 commits
gitleaks detect --log-opts "origin/main..HEAD"  # New commits since main

# Scan a specific branch
gitleaks detect --log-opts "feature-branch"

# Scan a specific commit
gitleaks detect --log-opts "abc123..abc124"
```

## 2.2 Output Formats

```bash
# Default: console output
gitleaks detect --source .

# JSON output (machine-readable, for tooling)
gitleaks detect --source . --report-format json --report-path gitleaks-report.json

# SARIF output (for GitHub Security tab)
gitleaks detect --source . --report-format sarif --report-path results.sarif

# CSV output
gitleaks detect --source . --report-format csv --report-path report.csv

# Review JSON output
cat gitleaks-report.json | jq '.[] | {RuleID, File, Commit, Secret}'
```

## 2.3 Understanding Findings

```json
{
  "RuleID": "aws-access-key-id",
  "Description": "AWS Access Key ID",
  "StartLine": 42,
  "EndLine": 42,
  "StartColumn": 1,
  "EndColumn": 60,
  "Match": "AKIAIOSFODNN7EXAMPLE",
  "Secret": "AKIAIOSFODNN7EXAMPLE",
  "File": "config/aws.py",
  "Commit": "a1b2c3d4e5f6",
  "Entropy": 3.72,
  "Author": "dev@company.com",
  "Email": "dev@company.com",
  "Date": "2023-10-15T12:00:00Z",
  "Message": "Add AWS configuration"
}
```

---

# PHASE 3: CUSTOM RULES & TUNING

---

## 3.1 Custom Gitleaks Configuration

```toml
# .gitleaks.toml (place in repo root)
title = "My Company Gitleaks Config"

[extend]
useDefault = true    # Use all default rules + add custom ones

# Custom rule
[[rules]]
id = "internal-api-key"
description = "Company internal API key pattern"
regex = '''company_[a-z0-9]{32}'''
entropy = 3.5
keywords = ["company_"]

[[rules]]
id = "db-connection-string"
description = "Database connection string with credentials"
regex = '''(mysql|postgres|mongodb|redis):\/\/[^:]+:[^@]+@'''
keywords = ["mysql://", "postgres://", "mongodb://", "redis://"]

[[rules]]
id = "private-key"
description = "Private key material"
regex = '''-----BEGIN (RSA |EC |DSA |OPENSSH )?PRIVATE KEY-----'''
keywords = ["PRIVATE KEY"]
```

## 3.2 Allowlist / Ignore Patterns

```toml
# .gitleaks.toml — suppress false positives

[allowlist]
description = "Global allowlist"
# Ignore specific commits (e.g., test data commits)
commits = ["a1b2c3d4", "e5f6g7h8"]

# Ignore files/paths
paths = [
    '''tests/.*''',
    '''.*_test\.py''',
    '''docs/.*'''
]

# Ignore specific regex patterns globally
regexes = [
    '''example_api_key_.*''',        # Clearly labeled example keys
    '''AKIA[A-Z]{16}EXAMPLE''',      # AWS example key pattern
    '''fake_secret_for_testing'''
]

# Per-rule allowlist
[[rules]]
id = "aws-access-key-id"
[[rules.allowlist]]
description = "Ignore test fixtures"
paths = ['''tests/fixtures/.*''']
regexes = ['''AKIAEXAMPLE.*''']
```

## 3.3 `.gitleaksignore` File

```bash
# Similar to .gitignore — Gitleaks respects this file
# Format: sha256_fingerprint_of_secret

# Generate fingerprint for a known-safe finding
gitleaks detect --source . --report-format json | \
  jq -r '.[] | .Fingerprint' | head -5

# Add to .gitleaksignore:
echo "6971eca6b2e9e8e8f39fd3a2e30b7f29abcd1234..." >> .gitleaksignore
```

---

# PHASE 4: PRE-COMMIT HOOKS

---

```bash
# Method 1: Direct pre-commit hook
cat > .git/hooks/pre-commit << 'EOF'
#!/bin/bash
gitleaks protect --staged --source . --verbose
if [ $? -eq 1 ]; then
    echo "❌ Gitleaks found secrets in staged changes. Commit blocked."
    echo "   Review findings above and remove secrets before committing."
    exit 1
fi
EOF
chmod +x .git/hooks/pre-commit

# Method 2: Using pre-commit framework (recommended for teams)
# .pre-commit-config.yaml
cat > .pre-commit-config.yaml << 'EOF'
repos:
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.18.0
    hooks:
      - id: gitleaks
        name: Gitleaks — Detect Secrets
EOF

# Install pre-commit hooks
pip3 install pre-commit
pre-commit install
```

- [ ] **`protect` vs `detect` mode:**
  - `gitleaks detect` — scans the entire git history for secrets
  - `gitleaks protect --staged` — scans only staged (uncommitted) changes — for pre-commit use

---

# PHASE 5: CI/CD INTEGRATION (GITHUB ACTIONS)

---

```yaml
# .github/workflows/gitleaks.yml
name: Gitleaks Secret Scanning

on:
  push:
    branches: ["*"]
  pull_request:

jobs:
  gitleaks:
    name: Detect Secrets
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0     # CRITICAL: fetch full history, not just last commit

      - name: Run Gitleaks
        uses: gitleaks/gitleaks-action@v2
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
          GITLEAKS_LICENSE: ${{ secrets.GITLEAKS_LICENSE }}  # Optional: Enterprise

      # Alternative: run binary directly
      - name: Run Gitleaks (Binary)
        run: |
          wget -q https://github.com/gitleaks/gitleaks/releases/latest/download/gitleaks_8.18.0_linux_x64.tar.gz
          tar xf gitleaks_*.tar.gz
          ./gitleaks detect \
            --log-opts "origin/${{ github.base_ref }}..HEAD" \
            --report-format sarif \
            --report-path gitleaks.sarif \
            --exit-code 1

      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@v3
        if: always()
        with:
          sarif_file: gitleaks.sarif
```

> [!IMPORTANT]
> `fetch-depth: 0` is **mandatory** for full history scanning. Without it, `actions/checkout` only fetches the last commit, and Gitleaks will miss secrets in older commits.

---

# PHASE 6: OFFENSIVE USE — REPO AUDITING

---

```bash
# Audit a public GitHub repository for leaked secrets
git clone https://github.com/target/repo.git
gitleaks detect --source ./repo --report-format json --report-path findings.json

# Audit an organization's repos (if you have access)
# Clone all repos:
gh repo list ORG --limit 100 --json nameWithOwner -q '.[].nameWithOwner' | \
  xargs -I {} git clone https://github.com/{}.git

# Scan all cloned repos
for dir in */; do
  echo "=== Scanning $dir ==="
  gitleaks detect --source "$dir" --report-format json --report-path "${dir%/}.json"
done

# Review all findings
jq -s 'flatten' *.json | jq '.[] | {RuleID, File, Secret, Commit, Author}'
```

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — Historical Secret Discovery:** Take any open-source repository with a long git history (or your own projects). Run a full history scan. Document: how many findings, what types of secrets, oldest commit date with a secret. Practice triaging: classify each as true positive, false positive, or requires investigation.

- [ ] **Lab 2 — Pre-Commit Hook:** Install Gitleaks as a pre-commit hook in a test repository. Try to commit a file containing a fake AWS key (`AKIAIOSFODNN7EXAMPLE`). Verify the commit is blocked. Add it to `.gitleaksignore` and verify the commit succeeds. Document the workflow.

- [ ] **Lab 3 — CI/CD Security Gate (Phase 8 Exit Gate):** Create a GitHub repository. Add a GitHub Actions workflow that runs Gitleaks on every push. Commit a file with a hardcoded API key pattern. Confirm the CI/CD pipeline fails. Remove the secret, commit, confirm the pipeline passes.

- [ ] **Lab 4 — Custom Rule:** Write a custom Gitleaks rule for a fake company-internal credential pattern (e.g., `corp_token_[a-z0-9]{40}`). Add it to `.gitleaks.toml`. Create test cases (one match, one non-match, one allowlisted). Verify the rule behaves correctly.

---

## 📝 Operational Notes

- **Gitleaks vs TruffleHog:** Gitleaks is faster (Go binary) and has simpler configuration. TruffleHog has more detection methods (entropy analysis, regex, rule engine) and native GitHub/GitLab/Bitbucket integration. Use both — they catch different things.
- **False positive rate:** The default Gitleaks ruleset prioritizes low false positives but will still flag test fixtures, example code, and high-entropy random strings. Budget time for triage. A finding rate >10% false positives means your allowlist needs tuning.
- **Secret rotation after discovery:** When Gitleaks finds a real secret that's been committed, the secret MUST be rotated (revoked and replaced) immediately — even if the repository is private. Git history is easily shared and copied. Rotation is non-negotiable.
- **`--log-opts "origin/main..HEAD"`:** The most efficient mode for CI/CD — only scans commits added in the current PR/push, not the entire history on every run. This dramatically reduces scan time while still catching new secrets.
- **GitHub native secret scanning:** GitHub has built-in secret scanning for public repos (and optionally private repos) that covers 200+ token patterns from providers. Gitleaks is complementary — use both. Gitleaks catches custom patterns that GitHub's scanner doesn't know about.
