# 🛡️ OWASP ZAP: Complete Mastery Checklist

> **What is OWASP ZAP?** OWASP Zed Attack Proxy (ZAP) is a free, open-source web application security scanner and intercepting proxy. It sits between your browser and the target application, capturing and allowing you to modify all HTTP/HTTPS traffic. It includes an automated active scanner that tests for OWASP Top 10 vulnerabilities, a spider to crawl application content, a fuzzer, and a suite of passive scan rules that flag issues without sending attack traffic.
>
> **Why does it exist?** Burp Suite Community is free but has significant limitations (no active scanner, no automated testing). ZAP fills that gap — it's the most feature-complete free web application security testing tool available. It's widely used in DAST (Dynamic Application Security Testing) pipelines, in CTFs, and in security assessments where Burp Pro's license cost isn't justified.
>
> **When to use it:** When Burp Suite Pro isn't available. Automated scanning for OWASP Top 10. CI/CD pipeline integration for automated security testing. API scanning. CTFs and HTB/THM web machines.
>
> **When to use Burp Suite instead:** When you need the most powerful, extensible, commercial-grade proxy and scanner with the richest extension ecosystem.
>
> **What mastering OWASP ZAP unlocks:** Free automated web application scanning. Complete OWASP Top 10 coverage. API security testing. CI/CD integration capability. The ability to perform professional web assessments without a commercial license.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | Manual Testing | 5 | 3–4 hours |
| 3 | Active Scanning | 4 | 2–3 hours |
| 4 | API Testing | 4 | 2–3 hours |
| 5 | Automation | 4 | 3–4 hours |
| 6 | Advanced | 3 | 2–3 hours |
| 7 | Practical Labs | 3 | 3–5 hours |
| 8 | Mastery Challenges | 2 | 2–3 hours |
| | **Total** | **29** | **~18–27 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — ZAP Architecture

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Intercepting Proxy** | Browser → ZAP proxy (default: `127.0.0.1:8080`) → target. All traffic captured. |
| **Sites Tree** | Left panel: shows all discovered URLs organized by domain. |
| **Active Scan** | ZAP sends attack payloads to discovered URLs. Tests for XSS, SQLi, path traversal, etc. |
| **Passive Scan** | Analyzes traffic passing through the proxy for issues — no attack traffic. |
| **Spider** | Crawls the application by following all links. Discovers URLs before active scanning. |
| **Ajax Spider** | Uses a browser to spider JavaScript-heavy applications. |

---

### Task 1.2 — Installation and Setup

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Download** | `zaproxy.org` — cross-platform Java application. |
| **Kali** | `apt install zaproxy`. |
| **Java** | Requires Java 11+. |
| **Browser Config** | Configure browser to proxy through `127.0.0.1:8080`. Install ZAP's CA cert: ZAP → Options → Network → Server Certificates → Save → import into browser. |
| **HUD** | ZAP HUD: overlay on target website in browser. Enable for guided testing. |

---

### Task 1.3 — ZAP vs. Burp Suite

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **ZAP Free** | Active scanner (free). Good automation/CI/CD integration. Open source — extensible via scripts. Python/JS/Groovy scripting. |
| **Burp Community** | No active scanner. Excellent manual testing tools (Repeater, Intruder limited). More polished UI. Better extension ecosystem (BAppStore). |
| **Burp Pro** | Best-in-class scanner, Collaborator, all Intruder attack types. Industry standard for commercial engagements. |
| **Verdict** | ZAP = free Burp Pro for scanning. Burp = better for manual, interactive testing. Many professionals use both. |

---

### Task 1.4 — Core Concepts: Passive vs. Active

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Passive** | Automatically analyzes traffic as it passes through ZAP. No attack requests sent. Flags: missing headers, information disclosure, cookie issues, insecure content. Always running when proxy is active. |
| **Active** | Must be explicitly triggered. Sends malicious payloads to each discovered URL. Finds: XSS, SQLi, SSRF, path traversal, command injection. Can break application state — only on authorized targets. |

---

# PHASE 2: MANUAL TESTING

---

### Task 2.1 — Intercepting and Modifying Requests

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Break Points** | Set a breakpoint: ZAP toolbar → Break button (red circle). Intercepts all requests. Edit request → Forward. |
| **Request Editor** | Right-click any request in history → Open/Resend with Request Editor. Modify and resend. ZAP's equivalent of Burp Repeater. |
| **History** | All proxied requests in the History tab. Filter by URL, method, code. |

---

### Task 2.2 — Spider

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Start** | Right-click a URL in Sites Tree → Spider. Or: Tools → Spider. Set scope. Start Scan. |
| **Output** | Sites tree fills with discovered URLs. Spider finds links in HTML, forms, comments. |
| **Ajax Spider** | For JavaScript-heavy apps: Tools → Ajax Spider. Uses Firefox/Chrome headless. Much slower but finds dynamic content. |

---

### Task 2.3 — Forced Browse

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Concept** | Like Gobuster/ffuf but integrated in ZAP. Tests wordlist of directory/file names against the target. |
| **Start** | Right-click URL → Forced Browse Site. Select wordlist. Start. |
| **Wordlists** | ZAP ships with built-in wordlists. Custom: specify path. |

---

### Task 2.4 — Fuzzer

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Start** | Right-click a parameter in a request → Fuzz. Select the string to fuzz → Add → select payload type. |
| **Payloads** | Files: load wordlist. Numberzz: integer range. String: static list. Script: generate via script. |
| **Processors** | Apply transformations to payloads: URL encode, base64 encode, MD5 hash. |
| **vs. Burp Intruder** | ZAP Fuzzer is free and unlimited. Burp Intruder Community is rate-limited. ZAP is preferred for free fuzzing. |

---

### Task 2.5 — Manual Parameter Testing

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Workflow** | Browse application → identify parameters in History → right-click → Open in Request Editor → modify parameter → send → analyze response for SQLi/XSS/SSRF etc. |
| **Encode/Decode** | Right-click → Encode/Decode → URL encode, base64, SHA1 etc. Useful for testing encoded parameters. |

---

# PHASE 3: ACTIVE SCANNING

---

### Task 3.1 — Running the Active Scanner

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Start** | Right-click target URL in Sites Tree → Active Scan. Or: toolbar → Active Scan button. |
| **Policy** | Scan policy defines which tests to run. Default: all. Custom policy: disable unnecessary tests (reduces time/noise). |
| **Authenticated** | Configure authentication before scanning (Task 3.3) to scan authenticated pages. |

---

### Task 3.2 — Scan Policy Configuration

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Edit Policy** | Analyze → Scan Policy Manager → Add/Edit. |
| **Categories** | Enable/disable specific test categories: SQL Injection, XSS, Path Traversal, SSRF, etc. |
| **Strength/Threshold** | Strength: how many payloads per test. Threshold: sensitivity of alerts (Low/Medium/High). |
| **Targeted** | For a quick scan: enable only SQLi and XSS. For comprehensive: enable all. |

---

### Task 3.3 — Authenticated Scanning

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Context** | ZAP uses "Contexts" to define scope and authentication. Right-click target → Include in Context → New Context. |
| **Authentication** | Context → Authentication → Form-based authentication. Set login URL, username/password parameters, logged-in indicator string. |
| **Session** | Context → Session Management. Set how ZAP maintains session (cookies, HTTP Auth). |
| **User** | Context → Users → add user (username + password). Scanner authenticates as this user. |

---

### Task 3.4 — Alert Analysis

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Alerts Tab** | Bottom panel → Alerts. All findings categorized by risk: High, Medium, Low, Informational, False Positive. |
| **Details** | Click alert → see: description, solution, evidence (the exact request/response that triggered it), references (CWE, WASC). |
| **False Positives** | Mark as False Positive (right-click). Excluded from report. |
| **Priority** | High risk alerts first → verify manually → confirm before reporting. |

---

# PHASE 4: API TESTING

---

### Task 4.1 — Import OpenAPI/Swagger

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Import** | Import → OpenAPI Definition. Paste Swagger JSON/YAML URL or file. ZAP parses all endpoints and parameters → adds to Sites Tree. |
| **Value** | Discover all API endpoints automatically. No need to manually browse. |
| **Then** | Run Active Scan on imported API endpoints. ZAP tests each endpoint with appropriate payloads. |

---

### Task 4.2 — Import Postman Collection

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Import** | Import → Postman Collection. Import `.json` collection file. |
| **Result** | All Postman requests added to ZAP Sites Tree. Replay them, add authentication, run active scanner. |

---

### Task 4.3 — API Key and Bearer Token Auth

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Header Replacement** | Options → Replacer → add rule: Replace `Authorization: Bearer PLACEHOLDER` with `Authorization: Bearer <actual_token>`. Applied to all matching requests automatically. |
| **Use** | ZAP sends authenticated API requests with the real token. Active scanner tests authenticated endpoints. |

---

### Task 4.4 — GraphQL Testing

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Addon** | Install "GraphQL Support" addon from ZAP Marketplace. |
| **Import** | Import GraphQL schema. ZAP generates all possible queries. |
| **Test** | Active scan on GraphQL endpoint — tests for injection in query parameters. |

---

# PHASE 5: AUTOMATION

---

### Task 5.1 — ZAP CLI (Command Line)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Baseline Scan** | `docker run -t zaproxy/zap-stable zap-baseline.py -t http://target.com -r report.html`. |
| **Full Scan** | `docker run -t zaproxy/zap-stable zap-full-scan.py -t http://target.com -r report.html`. |
| **API Scan** | `docker run -t zaproxy/zap-stable zap-api-scan.py -t http://target.com/openapi.json -f openapi -r report.html`. |

---

### Task 5.2 — CI/CD Integration

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **GitHub Actions** | `.github/workflows/zap_scan.yml`: `zaproxy/action-baseline@v0.7.0` action. Runs baseline scan on every PR. Fails if high-risk alerts found. |
| **Jenkins** | ZAP Jenkins plugin. Trigger scan as build step. Parse results, fail build on alerts. |
| **Baseline vs. Full** | CI/CD: baseline scan (fast, passive + limited active). Pre-release: full scan (complete active testing). |

---

### Task 5.3 — ZAP API

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Enable** | ZAP Tools → Options → API → Enable API. API key required for non-localhost. |
| **Endpoints** | `http://localhost:8080/JSON/core/view/sites/` — list sites. `http://localhost:8080/JSON/ascan/action/scan/?url=TARGET` — start active scan. |
| **Python** | `pip install zapcli python-owasp-zap-v2.4`. `from zapv2 import ZAPv2; zap = ZAPv2(apikey='key'); zap.spider.scan(url)`. |

---

### Task 5.4 — Automation Framework

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **ZAP Automation Framework** | YAML-based pipeline definition for ZAP. Define: environments, authentication, contexts, jobs (spider, active scan, passive scan, report). |
| **File** | `af.yaml` — specifies the complete test plan. `./zap.sh -autorun af.yaml`. |
| **Powerful** | Full control over scan lifecycle in a repeatable, version-controlled format. |

---

# PHASE 6: ADVANCED

---

### Task 6.1 — Add-ons / Marketplace

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Marketplace** | Help → Check for Updates → Marketplace tab. Install: Active Scanner Rules (Beta), Retire.js (outdated JS libraries), JWT Support, DOM XSS Scanner, Custom Payloads. |
| **Beta Rules** | Many additional checks are in the "beta" addon — install for more thorough scanning. |

---

### Task 6.2 — Scripts

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Languages** | Python, JavaScript, Groovy, Ruby. |
| **Types** | Targeted Rules (run on specific requests). Proxy Scripts (modify all traffic). Authentication Scripts (custom auth flows). Fuzzer Payload Processors. |
| **Use** | Write a Python script to extract all API tokens from traffic and log them. Or: custom authentication flow for OAuth2. |

---

### Task 6.3 — Reporting

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Report** | Report → Generate Report. Formats: HTML, PDF, XML, JSON, Markdown. |
| **Contents** | Alert list, risk categorization, full request/response evidence, CWE references, remediation advice. |
| **Customize** | Custom report templates. Exclude false positives before generating. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — DVWA Automated Scan

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Configure browser proxy → authenticate to DVWA → spider → active scan. Analyze all alerts. Verify High alerts manually. Generate HTML report. |
| **Success Criteria** | At least 5 unique findings. High alerts verified manually. HTML report generated. |

---

### Lab 7.2 — API Security Test

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Find a target with an OpenAPI spec (OWASP Juice Shop, vulnerable APIs). Import spec into ZAP. Configure bearer token auth. Run API active scan. Document findings. |
| **Success Criteria** | API scan completed. At least 1 API-specific vulnerability found. |

---

### Lab 7.3 — CI/CD Integration

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Set up a GitHub Actions workflow that runs ZAP baseline scan on a containerized web app. Configure it to fail the pipeline on High alerts. Verify the pipeline fails when a known vulnerability exists. |
| **Success Criteria** | Pipeline fails on high alert. Passes on clean app. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Full Web Assessment Report

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Full ZAP assessment of OWASP Juice Shop or DVWA. Spider → authenticated scan → active scan → alert review → false positive removal → professional report. |
| **Success Criteria** | Professional report written. False positives removed. All High findings verified. |

---

### Challenge 8.2 — ZAP API Automation Script

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Write a Python script using the ZAP API that: starts ZAP, runs a spider, runs an active scan, retrieves alerts, and writes a JSON report — all without the GUI. |
| **Success Criteria** | Fully automated scan via Python API. JSON report generated. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can configure browser proxy and ZAP CA certificate | ☐ |
| Can run spider, Ajax spider, and forced browse | ☐ |
| Can run an authenticated active scan | ☐ |
| Can import OpenAPI/Swagger for API testing | ☐ |
| Can use the fuzzer for parameter testing | ☐ |
| Can analyze, verify, and mark false-positive alerts | ☐ |
| Can generate HTML/JSON reports | ☐ |
| Can run ZAP via CLI for CI/CD integration | ☐ |
| Knows when to use ZAP vs. Burp Suite | ☐ |
| Can write a Python script using the ZAP REST API | ☐ |

---

## 🎯 Interview Questions

1. What is the difference between ZAP's passive scan and active scan?
2. How do you configure authenticated scanning in ZAP?
3. How do you import an OpenAPI specification for API testing?
4. How do you integrate ZAP into a CI/CD pipeline?
5. What is the ZAP Automation Framework and how does it work?
6. How does ZAP's fuzzer compare to Burp Intruder?
7. What add-ons would you install for a more thorough ZAP assessment?
8. How do you use the ZAP API to automate scans programmatically?
