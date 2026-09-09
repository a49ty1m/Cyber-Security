# 🔎 TruffleHog: Complete Mastery Checklist

> **What is TruffleHog?** TruffleHog is an open-source secret scanning tool that searches for high-entropy strings and credential patterns across Git repositories, S3 buckets, file systems, GitHub/GitLab organizations, Jira, Confluence, and more. Its key differentiator is **secret verification** — TruffleHog doesn't just detect potential secrets, it actively tests them against APIs (AWS STS, GitHub, Stripe, Slack, etc.) to confirm whether the detected credential is still valid and live.
>
> **Why does it exist?** Finding a credential in code is only half the battle. Knowing whether it's still active determines urgency. TruffleHog's verification capability transforms a "potential finding" into a confirmed "live credential compromise" — dramatically changing the priority of the response. It also scans more sources than most tools (not just Git — S3, CI/CD systems, collaboration tools).
>
> **When to use it:** Comprehensive secret scanning across diverse sources, confirming whether discovered credentials are still live (verification), security assessments of client codebases, scanning cloud storage for accidentally uploaded secrets, and pairing with Gitleaks for complete secret scanning coverage.
>
> **When to avoid it:** TruffleHog's active verification makes API calls against cloud providers — this is visible in logs and may trigger security alerts if scanning someone else's credentials. Only verify secrets in authorized engagements. For simple, fast local scanning, Gitleaks may be more appropriate.
>
> **What mastering TruffleHog unlocks:** Comprehensive multi-source secret scanning capability, credential verification (knowing if a found secret is live), broader attack surface coverage beyond Git (S3, CI/CD, collaboration tools), and complementary coverage alongside Gitleaks for Phase 8 DevSecOps pipelines.
>
> **Roadmap Stage / Module:** Shelf: Module S12 & S13 (Supply Chain & DevSecOps)

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| Secrets Scanning | SAST | IaC Security |
|:----------------|:-----|:-------------|
| [🕵️ Gitleaks](Gitleaks.md) | [🔍 Semgrep](Semgrep.md) | [✅ Checkov](Checkov.md) |
| **🔎 TruffleHog** (you are here) | | [🛡️ tfsec](tfsec.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & First Scan | 4 | 1 hour |
| 2 | Git Repository Scanning | 6 | 2–3 hours |
| 3 | Secret Verification | 5 | 2–3 hours |
| 4 | Multi-Source Scanning | 6 | 3–4 hours |
| 5 | CI/CD Integration | 4 | 1–2 hours |
| 6 | Detectors & Custom Rules | 5 | 2–3 hours |
| 7 | Practical Labs | 4 | 3–5 hours |
| | **Total** | **34** | **~14–21 hours** |

**Prerequisites:** Phase 1 complete. Git basics. Understanding of API keys and credentials from Phase 4/5 context. Phase 8 DevSecOps fundamentals.

---

# PHASE 1: INSTALLATION & FIRST SCAN

---

## 1.1 Installation

```bash
# Option 1: Download binary (recommended)
curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh -s -- -b /usr/local/bin
trufflehog --version

# Option 2: Docker
docker run --rm -it -v "$PWD:/pwd" trufflesecurity/trufflehog:latest git file:///pwd

# Option 3: Go install
go install github.com/trufflesecurity/trufflehog/v3@latest

# Option 4: Package manager (limited)
brew install trufflehog    # macOS
```

## 1.2 First Scan

```bash
# Scan a local git repository
trufflehog git file:///path/to/repo

# Scan a remote GitHub repository
trufflehog github --repo https://github.com/target/repo.git

# Scan current directory as a git repo
cd /my/project && trufflehog git file://.

# Only include verified secrets (confirmed live credentials)
trufflehog git file:///path/to/repo --only-verified

# Exit code 183 if verified secrets found, 0 if not
echo $?
```

## 1.3 Output Formats

```bash
# Default: colored console output with finding details
trufflehog git file:///path/to/repo

# JSON output (machine-readable)
trufflehog git file:///path/to/repo --json

# Pipe JSON to jq for filtering
trufflehog git file:///path/to/repo --json | jq '{
  Detector: .DetectorName,
  File: .SourceMetadata.Data.Git.file,
  Commit: .SourceMetadata.Data.Git.commit,
  Verified: .Verified,
  Raw: .Raw
}'
```

---

# PHASE 2: GIT REPOSITORY SCANNING

---

## 2.1 Scan Modes

```bash
# Full git history scan (most thorough)
trufflehog git file:///path/to/repo

# Scan a specific branch
trufflehog git file:///path/to/repo --branch feature-branch

# Scan since a specific commit (for CI/CD — only new commits)
trufflehog git file:///path/to/repo --since-commit HEAD~5

# Scan a specific commit range
trufflehog git file:///path/to/repo --since-commit abc123 --head def456

# Scan without verification (faster, no API calls)
trufflehog git file:///path/to/repo --no-verification

# Increase concurrency (faster on large repos)
trufflehog git file:///path/to/repo --concurrency 8
```

## 2.2 GitHub Source (Scan Remote Repos)

```bash
# Scan a single GitHub repo
trufflehog github --repo https://github.com/owner/repo

# Scan all repos in a GitHub organization
trufflehog github --org ORGNAME --token $GITHUB_TOKEN

# Scan all repos a user has access to
trufflehog github --token $GITHUB_TOKEN

# Include scan of issues and pull request comments
trufflehog github --repo https://github.com/owner/repo --include-members

# Scan only specific repos in an org
trufflehog github --org ORGNAME --repo repo1 --repo repo2 --token $GITHUB_TOKEN
```

---

# PHASE 3: SECRET VERIFICATION

---

## 3.1 How Verification Works

TruffleHog has "detectors" for 700+ credential types. Each detector knows how to:
1. **Identify** the credential pattern (regex + entropy analysis)
2. **Verify** it by making an API call to the provider

```bash
# Example verification for an AWS access key:
# 1. TruffleHog detects pattern: AKIA[0-9A-Z]{16}
# 2. TruffleHog calls: aws sts get-caller-identity using the detected key
# 3. If the API returns 200: credential is VERIFIED (live, confirmed valid)
# 4. If the API returns 403/401: credential is UNVERIFIED (may be revoked)

# Verified secret in output:
# ✅ Verified!
# Detector Type: AWS
# Decoder Type: PLAIN
# Raw: AKIAIOSFODNN7EXAMPLE

# Unverified secret:
# ❌ Not verified!
# (still reported — may be valid on a different environment)
```

## 3.2 Only Showing Verified Secrets

```bash
# Filter to only show actively verified (live) credentials
trufflehog git file:///path/to/repo --only-verified

# This is the most actionable output — confirmed live credentials
# Use this mode when you need to triage quickly in an incident

# Combine with GitHub org scan for incident response:
trufflehog github --org ORGNAME --token $GITHUB_TOKEN --only-verified
```

## 3.3 Verification Safety Note

> [!WARNING]
> TruffleHog's verification makes real API calls using discovered credentials. On authorized pentests, this confirms the finding. In bug bounty work, verify you're allowed to test live credentials before running `--only-verified` mode. For internal audits, verification is safe on your own organization's credentials.

---

# PHASE 4: MULTI-SOURCE SCANNING

---

## 4.1 Filesystem Scan

```bash
# Scan any directory (non-git)
trufflehog filesystem /path/to/scan

# Scan specific file types
trufflehog filesystem /path/to/scan --include-paths '*.env,*.config,*.json,*.yaml'

# Scan compressed archives (zip, tar, etc.)
trufflehog filesystem /path/to/archives --include-archives
```

## 4.2 S3 Bucket Scan

```bash
# Scan an entire S3 bucket
trufflehog s3 --bucket my-company-bucket

# Scan multiple buckets
trufflehog s3 --bucket bucket1 --bucket bucket2

# Scan with specific AWS credentials
AWS_ACCESS_KEY_ID=... AWS_SECRET_ACCESS_KEY=... trufflehog s3 --bucket bucket-name

# Scan all accessible S3 buckets
trufflehog s3 --scan-all-buckets

# Only show verified findings in S3
trufflehog s3 --bucket my-bucket --only-verified
```

## 4.3 CI/CD Systems

```bash
# Scan CircleCI
trufflehog circleci --token $CIRCLECI_TOKEN

# Scan Travis CI
trufflehog travis --token $TRAVIS_TOKEN

# Scan Jenkins
trufflehog jenkins --url https://jenkins.company.com --username admin --password pass

# Scan Drone CI
trufflehog drone --token $DRONE_TOKEN --server https://drone.company.com
```

## 4.4 Collaboration Tools

```bash
# Scan a Slack workspace (via export)
trufflehog slack --token $SLACK_TOKEN

# Scan a Jira instance
trufflehog jira --url https://company.atlassian.net \
  --username user@company.com --password $JIRA_API_TOKEN

# Scan a Confluence space
trufflehog confluence --url https://company.atlassian.net/wiki \
  --username user@company.com --password $CONFLUENCE_API_TOKEN
```

---

# PHASE 5: CI/CD INTEGRATION

---

```yaml
# .github/workflows/trufflehog.yml
name: TruffleHog Secret Scanning

on:
  push:
  pull_request:

jobs:
  trufflehog:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0     # Full history required

      - name: TruffleHog Secret Scan
        uses: trufflesecurity/trufflehog@main
        with:
          path: ./                              # Repository path
          base: ${{ github.event.repository.default_branch }}  # Base branch
          head: HEAD                            # Current branch tip
          extra_args: --only-verified           # Only report confirmed live secrets
```

```bash
# GitHub Actions with binary
- name: TruffleHog Scan (Binary)
  run: |
    curl -sSfL https://raw.githubusercontent.com/trufflesecurity/trufflehog/main/scripts/install.sh | sh
    ./trufflehog git file://. \
      --since-commit origin/${{ github.base_ref }} \
      --only-verified \
      --json > trufflehog-results.json
    if [ -s trufflehog-results.json ]; then
      echo "❌ Verified secrets detected! Check trufflehog-results.json"
      cat trufflehog-results.json | jq .
      exit 1
    fi
```

---

# PHASE 6: DETECTORS & CUSTOM RULES

---

## 6.1 Built-in Detectors (700+)

Key detectors TruffleHog includes:
```
AWS: Access Key ID + Secret Key (verified via STS)
GitHub: PATs, OAuth tokens, App tokens (verified via API)
Stripe: API keys (verified via Stripe API)
Slack: Bot tokens, OAuth tokens (verified via Slack API)
Google: API keys, Service account JSON (verified via Google APIs)
Azure: Storage account keys, SAS tokens
JWT: Secret detection (not verified — can't call anything without knowing the alg/secret)
SSH: Private keys (RSA, EC, DSA, ECDSA, Ed25519)
Postgres/MySQL: Connection strings with credentials
Sendgrid/Mailgun/Twilio: API keys
Datadog/PagerDuty/New Relic: API tokens
Heroku: API keys
Shopify: Access tokens
Docker Hub: Credentials
NPM: Auth tokens
PyPI: Upload tokens
```

## 6.2 List Available Detectors

```bash
# List all detector types
trufflehog --list-detectors

# Run only specific detectors
trufflehog git file:///path/to/repo --detector aws --detector github

# Skip specific detectors
trufflehog git file:///path/to/repo --filter-detectors '!slack,!stripe'
```

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — Compared Coverage:** Take a repository with intentionally embedded secrets (create one: add an AWS key pattern, a GitHub token pattern, and a Stripe key pattern to different files and commits). Run both Gitleaks and TruffleHog. Compare which detects which. Document the difference in detection coverage.

- [ ] **Lab 2 — Verification in Action:** In a lab AWS environment, create an IAM user with an access key. Commit the access key to a test repository. Run TruffleHog with `--only-verified`. Confirm it detects and verifies the key as live. Immediately deactivate the key and re-run. Confirm TruffleHog now reports it as unverified.

- [ ] **Lab 3 — S3 Scan:** Create an S3 bucket and upload a file containing a fake API key pattern. Run `trufflehog s3 --bucket your-bucket`. Confirm detection. Document the workflow for including S3 scanning in an incident response playbook.

- [ ] **Lab 4 — CI/CD Pipeline:** Set up a GitHub repository with a GitHub Actions workflow using TruffleHog. Commit a file with a GitHub PAT (use a valid token you control). Confirm the CI/CD pipeline fails and reports the verified credential. Revoke the token, remove from the file, and confirm the pipeline passes.

---

## 📝 Operational Notes

- **TruffleHog vs Gitleaks:** TruffleHog excels at verification (is the secret still live?) and multi-source scanning (S3, Jira, Slack). Gitleaks excels at speed, custom rule simplicity, and pre-commit integration. Use both together — they are complementary.
- **Exit code 183:** TruffleHog uses exit code 183 (not 1) to indicate verified secrets found. CI/CD systems need to check for this specific code: `if [ $? -eq 183 ]`. Many pipeline templates get this wrong.
- **Rate limiting:** TruffleHog makes real API calls for verification. AWS, GitHub, and other providers rate-limit API calls. On very large codebases with many secrets, verification may slow significantly or get throttled. Use `--no-verification` for initial fast scans, then verify selectively.
- **False positives in verification:** A credential may be unverified because the API is down, rate-limited, or the verification endpoint changed. `Unverified` doesn't mean the credential is invalid — it means TruffleHog couldn't confirm it. Always review unverified high-confidence findings manually.
- **Entropy analysis:** TruffleHog (and Gitleaks) use Shannon entropy to detect high-randomness strings that are likely to be credentials. High entropy + pattern match = strong confidence. Low entropy strings that match a pattern = lower confidence. Know that entropy alone is not a reliable signal (UUIDs and test data are also high-entropy).
