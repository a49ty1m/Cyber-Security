# 🔍 Semgrep: Complete Mastery Checklist

> **What is Semgrep?** Semgrep (Semantic Grep) is a fast, open-source static analysis engine that finds bugs, security vulnerabilities, and code quality issues using pattern-matching rules that understand code syntax and semantics. Unlike `grep` (which matches strings), Semgrep understands code structure — it can match across multiple lines, understand that `x + y` and `y + x` are equivalent, and respect language-specific semantics. It supports 30+ languages and has thousands of pre-written security rules.
>
> **Why does it exist?** SAST (Static Application Security Testing) tools are either expensive (Fortify, Checkmarx) or inaccurate (lots of false positives). Semgrep bridges the gap: free, fast (runs in seconds on large codebases), accurate, and developer-friendly (rules are written in the same language as the code they scan). It's the SAST tool that developers will actually use without resisting.
>
> **When to use it:** Code review automation (CI/CD pipeline security gates), finding hardcoded secrets and insecure patterns in source code, writing custom rules for organization-specific vulnerability classes, auditing third-party code before adoption, and the Phase 8 exit gate (build-failing SAST rules in GitHub Actions).
>
> **When to avoid it:** Semgrep doesn't run code — it can't find runtime vulnerabilities (SQL injection via complex data flows, auth bypasses from logic errors), only syntactic/structural patterns. For deep taint analysis, use commercial tools or CodeQL. For compiled binaries without source, use Ghidra.
>
> **What mastering Semgrep unlocks:** Automated security code review at scale, ability to enforce security standards across a codebase via CI/CD, the Phase 8 exit gate skill (custom SAST rule that fails CI/CD builds), and the foundation for application security engineering roles (AppSec).
>
> **Roadmap Stage / Module:** Shelf: Module S13 (DevSecOps) & Module S14 (Secure Code Review)

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| SAST/DevSecOps | Secrets Scanning | IaC Security |
|:--------------|:----------------|:-------------|
| **🔍 Semgrep** (you are here) | [🕵️ Gitleaks](Gitleaks.md) | [✅ Checkov](Checkov.md) |
| | [🔎 TruffleHog](TruffleHog.md) | [🛡️ tfsec](tfsec.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & First Scan | 4 | 1 hour |
| 2 | Using Pre-Built Rules | 6 | 2–3 hours |
| 3 | Rule Syntax — Writing Custom Rules | 9 | 4–6 hours |
| 4 | Advanced Pattern Matching | 7 | 3–4 hours |
| 5 | CI/CD Integration (GitHub Actions) | 5 | 2–3 hours |
| 6 | Taint Analysis & Data Flow | 5 | 3–4 hours |
| 7 | Practical Labs | 4 | 4–6 hours |
| | **Total** | **40** | **~19–27 hours** |

**Prerequisites:** Phase 1 complete. Basic familiarity with at least one programming language (Python, JavaScript, Java). Understanding of common web vulnerabilities (SQL injection, XSS, path traversal) from Phase 4.

---

# PHASE 1: INSTALLATION & FIRST SCAN

---

## 1.1 Installation

```bash
# Install via pip (recommended)
pip3 install semgrep

# Verify
semgrep --version

# Alternative: Docker
docker run --rm -v "${PWD}:/src" semgrep/semgrep semgrep --config=auto /src

# Alternative: Homebrew (macOS)
brew install semgrep
```

## 1.2 First Scan

```bash
# Scan the current directory with auto-selected rules (Semgrep registry)
semgrep --config=auto .

# Scan with a specific ruleset
semgrep --config p/python-security .          # Python security rules
semgrep --config p/javascript .               # JavaScript rules
semgrep --config p/owasp-top-ten .            # OWASP Top 10 rules

# Scan a single file
semgrep --config=auto app.py

# Quiet output (only findings)
semgrep --config=auto . --quiet

# JSON output (for tooling integration)
semgrep --config=auto . --json > results.json

# SARIF output (for GitHub/GitLab security dashboards)
semgrep --config=auto . --sarif > results.sarif
```

---

# PHASE 2: USING PRE-BUILT RULES

---

## 2.1 Semgrep Registry Rulesets

```bash
# List of key public rulesets (from semgrep.dev/r):
semgrep --config p/python-security        # Python vulnerabilities
semgrep --config p/javascript-security    # JavaScript/Node.js vulnerabilities
semgrep --config p/java-security          # Java vulnerabilities
semgrep --config p/go-security            # Go vulnerabilities
semgrep --config p/ruby-security          # Ruby vulnerabilities
semgrep --config p/owasp-top-ten          # OWASP Top 10 across languages
semgrep --config p/cwe-top-25             # CWE Top 25 most dangerous weaknesses
semgrep --config p/sql-injection          # SQL injection patterns
semgrep --config p/xss                    # Cross-Site Scripting patterns
semgrep --config p/command-injection      # Command injection
semgrep --config p/secrets               # Hardcoded secrets (API keys, passwords)
semgrep --config p/jwt                    # JWT misconfigurations
semgrep --config p/crypto                 # Cryptographic weaknesses

# Scan with multiple rulesets
semgrep --config p/python-security --config p/secrets .

# Use all rules (broad, more false positives)
semgrep --config p/default .
```

## 2.2 Understanding Semgrep Output

```
Finding #1:
  Rule: python.django.security.injection.tainted-sql-string.tainted-sql-string
  Severity: ERROR
  File: app/views.py
  Lines: 42-43
  Message: Detected user-controlled data passed to SQL query without parameterization.
           This could result in SQL injection.
  
  42: query = "SELECT * FROM users WHERE name = '" + request.GET['name'] + "'"
  43: cursor.execute(query)
  
  Fix: Use parameterized queries: cursor.execute("SELECT * FROM users WHERE name = %s", [name])
  Reference: https://semgrep.dev/r/python.django.security.injection.tainted-sql-string
```

---

# PHASE 3: RULE SYNTAX — WRITING CUSTOM RULES

---

## 3.1 Semgrep Rule Structure (YAML)

```yaml
rules:
  - id: unparameterized-sql-query        # Unique rule ID
    message: >
      Detected SQL query built with string concatenation.
      This is vulnerable to SQL injection.
      Use parameterized queries instead: cursor.execute(query, [params])
    severity: ERROR                       # INFO | WARNING | ERROR
    languages: [python]                   # Which languages this rule applies to
    metadata:
      cwe: "CWE-89: Improper Neutralization of Special Elements used in SQL Commands"
      owasp: "A03:2021 — Injection"
      confidence: HIGH
    patterns:
      - pattern: |
          $CURSOR.execute($QUERY + ...)
      - pattern: |
          $CURSOR.execute(f"... {$VAR} ...")
      - pattern: |
          $CURSOR.execute("..." % $VAR)
```

## 3.2 Pattern Syntax

```yaml
# Metavariables: $NAME matches any expression
pattern: |
  $FUNC($USER_INPUT)

# Ellipsis ...: matches any sequence of statements/arguments
pattern: |
  eval(...)            # matches eval with any arguments
pattern: |
  os.system($CMD)

# Typed metavariables (language-specific)
pattern: |
  (str $X) + $Y       # $X must be of type str

# Regex patterns for string literals
pattern: |
  $KEY = "..."
pattern-regex: (?i)password\s*=\s*"[^"]+"

# Inside patterns — match in specific code contexts
pattern-inside: |
  def $FUNC(...):
      ...
```

## 3.3 Pattern Combinators

```yaml
# ALL patterns must match
patterns:
  - pattern: |
      subprocess.call($CMD, shell=True)
  - pattern-not: |
      subprocess.call("...", shell=True)   # Exclude hardcoded strings (less risky)

# ANY pattern matches (OR logic)
pattern-either:
  - pattern: os.system($CMD)
  - pattern: subprocess.call($CMD, shell=True)
  - pattern: subprocess.Popen($CMD, shell=True)

# Match UNLESS pattern is also present
pattern-not: |
  hashlib.md5(...)     # Would exclude MD5 usage from a "weak hash" rule

# Match INSIDE this context only
pattern-inside: |
  @app.route(...)
  def $FUNC(...):
      ...

# Match NOT inside this context
pattern-not-inside: |
  # type: ignore
  ...
```

## 3.4 Complete Custom Rule Examples

```yaml
rules:
  # Rule 1: SQL injection via string formatting
  - id: sql-injection-string-format
    message: SQL injection via string formatting. Use parameterized queries.
    severity: ERROR
    languages: [python]
    patterns:
      - pattern-either:
          - pattern: cursor.execute($QUERY % ...)
          - pattern: cursor.execute($QUERY.format(...))
          - pattern: cursor.execute(f"... {$VAR} ...")
          - pattern: cursor.execute($A + $B)
    metadata:
      cwe: "CWE-89"

  # Rule 2: Hardcoded JWT secret
  - id: hardcoded-jwt-secret
    message: JWT secret key is hardcoded. Use environment variables.
    severity: ERROR
    languages: [python, javascript]
    pattern-either:
      - pattern: jwt.encode($PAYLOAD, "...")
      - pattern: jwt.sign($PAYLOAD, "...")
    pattern-not:
      - pattern: jwt.encode($PAYLOAD, os.environ[...])
      - pattern: jwt.encode($PAYLOAD, os.getenv(...))

  # Rule 3: Insecure deserialization
  - id: insecure-pickle-deserialize
    message: >
      pickle.loads() on untrusted data allows arbitrary code execution.
      Use JSON or another safe serialization format.
    severity: ERROR
    languages: [python]
    patterns:
      - pattern: pickle.loads($DATA)
      - pattern-not: pickle.loads(b"...")  # Hardcoded bytes are not user-controlled

  # Rule 4: Command injection
  - id: command-injection
    message: User-controlled input passed to shell command. Risk of command injection.
    severity: ERROR
    languages: [python]
    pattern-either:
      - pattern: os.system($USER_INPUT)
      - pattern: subprocess.call($USER_INPUT, shell=True)
      - pattern: subprocess.run($USER_INPUT, shell=True)
```

---

# PHASE 4: ADVANCED PATTERN MATCHING

---

## 4.1 Taint Mode (Pro Feature / OSS Experimental)

```yaml
# Taint analysis tracks data flow from source to sink
- id: sql-taint-analysis
  mode: taint                    # Enable taint tracking
  message: User data flows into SQL query without sanitization
  severity: ERROR
  languages: [python]
  pattern-sources:
    - pattern: request.args[...]      # Data sources (user-controlled)
    - pattern: request.form[...]
    - pattern: request.get_json()[...]
  pattern-sinks:
    - pattern: cursor.execute(...)    # Dangerous sinks
    - pattern: db.query(...)
  pattern-sanitizers:
    - pattern: parameterize($X)       # Known sanitization functions
    - pattern: escape($X)
```

## 4.2 Autofix Rules

```yaml
# Semgrep can automatically fix issues with --autofix flag
- id: use-secrets-not-hardcoded
  message: Hardcoded API key detected
  severity: WARNING
  languages: [python]
  pattern: |
    $KEY = "$VALUE"
  fix: |
    $KEY = os.environ.get("$KEY")
  # Run with: semgrep --autofix --config myrule.yml .
```

---

# PHASE 5: CI/CD INTEGRATION (GITHUB ACTIONS)

---

## 5.1 GitHub Actions Workflow

```yaml
# .github/workflows/semgrep.yml
name: Semgrep Security Scan

on:
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  semgrep:
    name: SAST Security Scan
    runs-on: ubuntu-latest
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Run Semgrep
        uses: semgrep/semgrep-action@v1
        with:
          config: >-
            p/python-security
            p/owasp-top-ten
            ./security/custom-rules.yml     # Your custom rules
          fail_open: false                  # Fail build if Semgrep errors occur
          
        env:
          SEMGREP_APP_TOKEN: ${{ secrets.SEMGREP_APP_TOKEN }}  # Optional: Semgrep Cloud

      # Alternative: Run directly without the action
      - name: Install and Run Semgrep
        run: |
          pip install semgrep
          semgrep --config p/python-security \
                  --config ./security/custom-rules.yml \
                  --error \                  # Exit code 1 if findings (fails the build)
                  --sarif-output results.sarif \
                  .
          
      - name: Upload SARIF Results
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: results.sarif         # Shows in GitHub Security tab
        if: always()                        # Upload even if scan failed
```

## 5.2 The Phase 8 Exit Gate — SQL Injection CI/CD Rule

```yaml
# security/no-sql-injection.yml
# This rule FAILS the CI/CD build if any unparameterized SQL is found

rules:
  - id: no-unparameterized-sql
    message: >
      [SECURITY GATE FAILURE] Unparameterized SQL query detected.
      This violates our secure coding standard.
      Use parameterized queries: cursor.execute(query, [params])
      Build will fail until this is fixed.
    severity: ERROR
    languages: [python, javascript, java, go]
    pattern-either:
      - pattern: cursor.execute($Q + ...)
      - pattern: cursor.execute(f"...{$V}...")
      - pattern: cursor.execute($Q % ...)
      - pattern: db.query($Q + ...)
    metadata:
      category: security
      cwe: "CWE-89"
```

---

# PHASE 6: TAINT ANALYSIS & DATA FLOW

---

```bash
# Run taint analysis (experimental in OSS, full in Pro)
semgrep --config=auto --experimental .

# The Pro version has full inter-procedural taint tracking
# (follows data through function calls)
# For free/OSS: taint analysis works within a single function scope
```

```python
# Example of what taint analysis detects vs doesn't detect:

# DETECTED (single function, direct flow):
def login(request):
    username = request.GET['username']   # Source: user input
    cursor.execute("SELECT * FROM users WHERE name = '" + username + "'")  # Sink

# NOT DETECTED by OSS taint (crosses function boundaries):
def get_username(request):
    return request.GET['username']   # Source: in a different function

def login(request):
    username = get_username(request)  # OSS taint can't follow this
    cursor.execute("SELECT * FROM users WHERE name = '" + username + "'")  # Sink
```

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — Scan a Real Project:** Clone a popular open-source web application (e.g., a Django or Flask app from GitHub). Run `semgrep --config p/python-security .`. Document all findings by severity. Pick 3 findings and verify whether they are true positives or false positives by reading the surrounding code.

- [ ] **Lab 2 — Custom Rule Sprint:** Write 5 custom Semgrep rules for your organization's tech stack (pick Python, JavaScript, or Java). Required: one SQL injection rule, one hardcoded secret rule, one insecure crypto rule, one command injection rule, one deserialization rule. Test each against a sample of intentionally vulnerable code.

- [ ] **Lab 3 — CI/CD Security Gate (Phase 8 Exit Gate):** Create a GitHub repository with a vulnerable Python Flask app containing at least one SQL injection. Build a GitHub Actions workflow that runs your custom `no-unparameterized-sql` Semgrep rule. Verify the CI/CD build fails due to the finding. Fix the SQL injection, commit, and verify the build passes.

- [ ] **Lab 4 — False Positive Tuning:** Take the output from Lab 1. Identify 3 false positives. Write `pattern-not` conditions to exclude them from the rule. Verify the exclusions don't affect true positive detection on your intentionally vulnerable code.

---

## 📝 Operational Notes

- **`--error` flag:** This is what makes Semgrep a security gate — it exits with code 1 when findings are present, causing CI/CD to fail. Without `--error`, Semgrep exits 0 regardless of findings (advisory mode only).
- **Semgrep OSS vs Pro vs Cloud:** OSS (what you install via pip) is free, open-source, and fully functional for custom rules. Pro adds inter-procedural taint analysis. Cloud adds a dashboard, team management, and CI/CD integrations. You only need OSS for Phase 8.
- **Rule registry at semgrep.dev:** Browse all public rules at `semgrep.dev/r`. Filter by language, category (security, best-practices), and severity. This is your starting point for learning rule syntax by example.
- **Performance:** Semgrep scans Python at ~100K lines/second. For very large codebases, use `--include` and `--exclude` to target specific directories, or split into multiple jobs.
- **`# nosemgrep`:** Add `# nosemgrep: rule-id` as a comment on a line to suppress that specific finding. Use sparingly — document why the exception is safe.
