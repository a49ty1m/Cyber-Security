# ⚡ Nuclei: Complete Mastery Checklist

> **What is Nuclei?** Nuclei is ProjectDiscovery's open-source, template-based vulnerability scanner. Instead of running fixed checks, it uses community-maintained YAML templates to test for specific vulnerabilities, misconfigurations, and exposures. With 9,000+ templates covering CVEs, misconfigured services, exposed panels, and web application vulnerabilities, it has become the go-to scanner for modern bug bounty and external attack surface assessments.
>
> **Why does it exist?** Traditional scanners like Nikto use a static, hardcoded check list that is slow to update and generates excessive false positives. Nuclei's template engine lets security researchers write precise, targeted checks that are reviewed by the community and updated continuously — making it dramatically more accurate and up-to-date.
>
> **When to use it:** After subdomain enumeration (Amass/Subfinder) and HTTP probing (httpx), as the automated vulnerability detection layer. For bug bounty continuous scanning. For CVE validation on known-vulnerable software versions. For technology fingerprinting and misconfiguration detection at scale.
>
> **When to avoid it:** When you need deep manual web app testing (use Burp Suite instead). When you only have a single target and are doing thorough manual testing (Nuclei complements manual testing, it does not replace it). When you are not authorized (Nuclei runs real HTTP requests against targets).
>
> **What mastering Nuclei unlocks:** Automated vulnerability detection across large attack surfaces. CVE validation. Bug bounty automation pipeline. Custom template writing for proprietary targets. Modern replacement for Nikto in professional workflows.
>
> **Roadmap Phase:** Phase 2–3 (Scanning & Enumeration, Web Vulnerability Detection)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

| Recon | Scanning | Web Attacks | Automation |
|:------|:---------|:-----------|:-----------|
| [🌐 Amass](Amass.md) | [🗺️ Nmap](Nmap.md) | [🕷️ Burp Suite](Burp_Suite.md) | [🌀 ffuf](ffuf.md) |
| [🌾 theHarvester](theHarvester.md) | [🔍 Nikto](Nikto.md) | [💉 sqlmap](sqlmap.md) | [📂 Gobuster](Gobuster.md) |
| [🔭 Recon-ng](Recon-ng.md) | **⚡ Nuclei** (you are here) | [🕷️ Burp Suite](Burp_Suite.md) | [🌐 Amass](Amass.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & Template Engine | 5 | 2–3 hours |
| 2 | Core Usage — Running Templates | 6 | 4–6 hours |
| 3 | Intermediate — Custom Templates | 5 | 5–7 hours |
| 4 | Advanced — Automation Pipelines | 4 | 3–5 hours |
| 5 | Tool Integration | 4 | 2–3 hours |
| 6 | Practical Labs | 4 | 4–7 hours |
| 7 | Methodology & Responsible Use | 3 | 2–3 hours |
| 8 | Mastery Challenges | 3 | 3–5 hours |
| | **Total** | **34** | **~25–39 hours** |

**Prerequisites:** Basic HTTP knowledge. Familiarity with YAML syntax (for template writing). Understanding of common web vulnerabilities (OWASP Top 10). A legal target for testing.

**Comparison with Nikto:** Nikto uses a static hardcoded check database. Nuclei uses community-maintained YAML templates — far more up-to-date, lower false positive rate, faster, and better integrated into modern pipelines. For new projects, use Nuclei as the primary scanner; Nikto is useful for quick legacy checks.

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Template Engine Architecture

- [ ] **Completed** · ⭐ Beginner · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand how Nuclei's YAML template engine works and why it is better than static scanners. |
| **Skills Learned** | Template structure (info block, requests, matchers, extractors), how matchers define what constitutes a finding, community template repository (`nuclei-templates` GitHub), why template-based scanning has lower false positives. |
| **Practical Exercise** | Open any Nuclei template from `~/nuclei-templates/` in a text editor. Read the `info:` block (name, severity, tags). Read the `requests:` block (method, path, matchers). Understand: this template sends a specific HTTP request and flags a finding ONLY when a specific pattern matches the response. |
| **Expected Output** | Understanding of template anatomy. Ability to predict what a template does by reading it. |

### Task 1.2 — Installation & Template Update

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Install Nuclei and download/update the community template library. |
| **Practical Exercise** | `go install -v github.com/projectdiscovery/nuclei/v3/cmd/nuclei@latest` OR `sudo apt install nuclei`. Update templates: `nuclei -update-templates`. Check: `nuclei -version`. Count templates: `ls ~/nuclei-templates/**/*.yaml \| wc -l`. |
| **Expected Output** | Nuclei installed. Templates updated (9,000+ templates). Version confirmed. |

### Task 1.3 — Template Categories

- [ ] **Completed** · ⭐ Beginner · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Know the template category structure so you can target relevant checks. |
| **Skills Learned** | Template directories: `cves/` (CVE-specific), `exposures/` (sensitive file/config exposure), `misconfigurations/` (security misconfigs), `takeovers/` (subdomain takeover), `technologies/` (tech fingerprinting), `vulnerabilities/` (generic vulns), `default-logins/` (default credentials). |
| **Practical Exercise** | `ls ~/nuclei-templates/` → explore each directory. `ls ~/nuclei-templates/cves/ \| wc -l` → count CVE templates. `cat ~/nuclei-templates/exposures/configs/git-config.yaml` → read a simple exposure template. |
| **Expected Output** | Template category map. Understanding of which category to target for which assessment type. |

### Task 1.4 — Severity Levels

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand Nuclei severity levels and when to filter by them. |
| **Practical Exercise** | Nuclei severities: `critical`, `high`, `medium`, `low`, `info`. `-severity critical,high` runs only critical and high templates (faster, focused on P1/P2 findings). `-severity info` runs tech fingerprinting and exposure checks. For a first pass on a new target: `-severity critical,high,medium`. |

### Task 1.5 — Basic Target Formats

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand how to specify single targets, lists, and piped input. |
| **Practical Exercise** | Single URL: `nuclei -u https://target.com`. URL list: `nuclei -l urls.txt`. Piped from httpx: `cat subs.txt \| httpx -silent \| nuclei -t ~/nuclei-templates/`. CIDR: `nuclei -u 192.168.1.0/24`. |

---

# PHASE 2: CORE USAGE

---

### Task 2.1 — First Scan: Tech Detection

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Run Nuclei's technology detection templates to fingerprint the target stack. |
| **Practical Exercise** | `nuclei -u https://target.com -t ~/nuclei-templates/technologies/ -o tech_results.txt`. Review output: web server, CMS, framework, CDN, analytics — all detected from HTTP headers, response content, and JavaScript. |
| **Expected Output** | Technology fingerprint of the target. WordPress version, Apache/Nginx version, PHP version, JavaScript frameworks — all relevant for targeted CVE scanning next. |

### Task 2.2 — CVE Scanning

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Scan for known CVEs based on the fingerprinted technology stack. |
| **Skills Learned** | `-t cves/` directory, filtering by year (`-t cves/2023/`), filtering by technology tag (`-tags wordpress`), understanding false positive rate (CVE templates require version detection or PoC confirmation). |
| **Practical Exercise** | After identifying WordPress: `nuclei -u https://target.com -tags wordpress -severity critical,high`. After identifying Apache: `nuclei -u https://target.com -tags apache -severity critical,high`. Review findings — each should include PoC evidence (response content, version string, etc.). |
| **Expected Output** | CVE findings with evidence. Each finding includes template name, severity, matched URL, and response snippet. |

### Task 2.3 — Misconfiguration Detection

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Detect common security misconfigurations: open redirects, CORS misconfig, HTTP security headers, directory listing, exposed sensitive files. |
| **Practical Exercise** | `nuclei -u https://target.com -t ~/nuclei-templates/misconfigurations/ -o misconfigs.txt`. Common findings: missing security headers (`X-Frame-Options`, `Content-Security-Policy`), open redirect, CORS wildcard, exposed `.git`, exposed `.env`. |
| **Expected Output** | List of misconfigurations with evidence. Security headers audit results. |

### Task 2.4 — Exposure Detection (Sensitive Files)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Detect exposed configuration files, backup files, and sensitive paths. |
| **Practical Exercise** | `nuclei -u https://target.com -t ~/nuclei-templates/exposures/ -o exposures.txt`. High-value findings: `.env` (API keys, DB passwords), `.git/config` (source code), `wp-config.php.bak` (WordPress creds), `phpinfo.php` (server info), exposed admin panels. |
| **Expected Output** | Any exposed sensitive files. `.env` or config exposures are immediate Critical findings. |

### Task 2.5 — Default Credentials Scan

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Check for default login credentials on admin panels, IoT devices, and network services. |
| **Practical Exercise** | `nuclei -u https://target.com -t ~/nuclei-templates/default-logins/ -o default_creds.txt`. Common hits: Grafana `admin:admin`, Jenkins anonymous, Router `admin:admin`, Tomcat `tomcat:s3cret`, Kibana open. |
| **Expected Output** | Any services accepting default credentials. Immediate Critical finding in any pentest report. |

### Task 2.6 — Output Formats and Reporting

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Capture Nuclei results in formats useful for reporting and downstream tooling. |
| **Practical Exercise** | Plain text: `-o results.txt`. JSON: `-json -o results.json`. Markdown: `-markdown-export reports/`. Silent mode (findings only): `-silent`. Stats: `-stats`. Verbose: `-v` (show all requests). `jq '.info.severity' results.json \| sort \| uniq -c` to summarize by severity. |
| **Expected Output** | JSON output parsed with jq. Markdown report generated for inclusion in pentest report. |

---

# PHASE 3: CUSTOM TEMPLATES

---

### Task 3.1 — Template YAML Structure

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the full YAML structure of a Nuclei template. |
| **Skills Learned** | `id`, `info` block (name, author, severity, description, tags), `requests` block (method, path, headers, body), `matchers` (word, regex, status, binary, dsl), `extractors` (regex, xpath, json), matcher conditions (`and`/`or`). |
| **Practical Exercise** | Write a template that detects a `/debug` endpoint returning HTTP 200 with the word "DEBUG" in the response body. Test it against a local test server. |
| **Expected Output** | Working custom template. Understanding of matchers and how to tune them to reduce false positives. |

### Task 3.2 — Writing a Simple Exposure Template

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Write a template that detects an exposed `.env` file. |
| **Practical Exercise** | Template: GET `/.env` → matcher: status 200 AND body contains `APP_KEY` or `DB_PASSWORD`. Test against a local Flask app with a `.env` file. Refine to reduce false positives (add `part: body` to matcher). |
| **Expected Output** | Working `.env` exposure template. Understanding of how to avoid false positives with multi-condition matchers. |

### Task 3.3 — Writing a CVE PoC Template

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 50 min

| Field | Detail |
|:---|:---|
| **Objective** | Write a template that validates a specific CVE with a proof-of-concept request. |
| **Practical Exercise** | Pick a simple CVE with a known PoC HTTP request (e.g., CVE-2021-41773 Apache path traversal). Write a Nuclei template: send the PoC request → match on the response that confirms exploitation. Test against a vulnerable Docker container. |
| **Expected Output** | Working CVE PoC template. Confirmed true positive on vulnerable target, confirmed no false positive on patched target. |

### Task 3.4 — Template Variables and Dynamic Values

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Nuclei's built-in variables and DSL expressions for dynamic template logic. |
| **Skills Learned** | Variables: `{{BaseURL}}`, `{{Hostname}}`, `{{RandStr}}`, `{{unix_time}}`. DSL matchers: `contains(body, "error")`, `status_code == 200`, `len(body) > 0`. Extractors for capturing dynamic values (API keys, tokens, version strings). |
| **Practical Exercise** | Write a template that generates a unique random string in the request and confirms it is reflected in the response body — basic reflected XSS detection pattern. |

### Task 3.5 — Contributing Templates to the Community

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the process for contributing quality templates to the nuclei-templates repository. |
| **Practical Exercise** | Fork `projectdiscovery/nuclei-templates`. Write a new template following the contribution guide (proper `info` block, tested against a real vulnerable instance, no false positives on patched version). Submit a PR. |

---

# PHASE 4: AUTOMATION PIPELINES

---

### Task 4.1 — Amass → httpx → Nuclei Pipeline

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Build the standard recon-to-vuln pipeline used in professional bug bounty. |
| **Practical Exercise** | `amass enum -passive -d target.com -o subs.txt` → `cat subs.txt \| httpx -silent -o live.txt` → `nuclei -l live.txt -t ~/nuclei-templates/ -severity critical,high -o vulns.txt`. |
| **Expected Output** | Automated pipeline from domain → live subdomains → vulnerabilities in one script. |

### Task 4.2 — Rate Limiting and Concurrency Tuning

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Tune Nuclei's concurrency and rate limiting for responsible scanning. |
| **Practical Exercise** | `-c 25` (25 concurrent templates). `-rate-limit 100` (max 100 requests/second). `-timeout 10` (10s timeout per request). For slow targets or WAF-protected: `-rate-limit 10 -c 5`. For fast internal networks: `-c 50 -rate-limit 500`. |

### Task 4.3 — Nuclei in CI/CD (Continuous Scanning)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Integrate Nuclei into an automated continuous scanning workflow that alerts on new findings. |
| **Practical Exercise** | Create a bash script: run Nuclei daily → compare JSON output with previous run → alert on new findings via Slack webhook or email. Use `anew` for diff: `nuclei -l live.txt -json \| anew new_findings.json`. |

### Task 4.4 — PDCP / Nuclei Cloud

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand ProjectDiscovery's cloud platform (PDCP) for managed Nuclei scanning. |
| **Practical Exercise** | Sign up for PDCP free tier → create a scan target → run a cloud-based Nuclei scan → compare results with local run. Understand when cloud scanning is appropriate (continuous monitoring for large programs). |

---

# PHASE 5: TOOL INTEGRATION

---

### Task 5.1 — Nuclei + Burp Suite (Manual + Auto)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min
| Field | Detail |
|:---|:---|
| **Objective** | Use Nuclei for automated detection while Burp Suite handles manual deep-dive testing. |
| **Practical Exercise** | Run Nuclei first to identify all quick wins and tech stack. Then open confirmed interesting endpoints in Burp for manual testing. Nuclei identifies the attack surface; Burp exploits it. |

### Task 5.2 — Nuclei + Amass + httpx (Full Attack Surface Pipeline)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min
| Field | Detail |
|:---|:---|
| **Practical Exercise** | Full bash pipeline: `amass enum -passive -d $DOMAIN -o subs.txt && cat subs.txt \| httpx -silent -title -tech-detect -o live.txt && nuclei -l live.txt -t nuclei-templates/ -o findings.txt`. |

### Task 5.3 — Nuclei + Nmap (Port to Web)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min
| Field | Detail |
|:---|:---|
| **Practical Exercise** | Nmap finds non-standard web ports (8080, 8443, 9090) → extract those URLs → pipe into Nuclei for service-specific templates. |

### Task 5.4 — Nuclei for API Testing

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min
| Field | Detail |
|:---|:---|
| **Practical Exercise** | `nuclei -u https://api.target.com -t ~/nuclei-templates/ -tags api -o api_findings.txt`. Combine with `-H "Authorization: Bearer <token>"` for authenticated API scanning. |

---

# PHASE 6: PRACTICAL LABS

---

### Lab 6.1 — DVWA Full Nuclei Scan

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 2 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Run Nuclei against DVWA (locally hosted). Identify all findings. Compare with Nikto results. Document which tool found what. |
| **Success Criteria** | Nuclei finds at least 5 unique findings. Results compared with Nikto — note what each missed. |

### Lab 6.2 — Bug Bounty: First Pass Scan

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 3–4 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Pick a bug bounty program. Run full pipeline: Amass → httpx → Nuclei critical/high. Document all findings. |
| **Success Criteria** | At least one valid Medium+ finding identified. Full pipeline automated in a single script. |

### Lab 6.3 — Custom Template for a Known CVE

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 2–3 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Pick a CVE with a public PoC. Write a Nuclei template. Test against a vulnerable Docker container (Vulhub). Confirm true positive and no false positive on patched version. |
| **Success Criteria** | Working template that correctly identifies vulnerable vs patched instances. |

### Lab 6.4 — Continuous Monitoring Setup

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 2 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Cron job running Nuclei + Amass daily against a bug bounty target. New findings trigger a notification. |
| **Success Criteria** | Automated daily scan running. New finding notification demonstrated. |

---

# PHASE 7: METHODOLOGY & RESPONSIBLE USE

---

### Task 7.1 — Nuclei in the Recon Methodology

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min
| Field | Detail |
|:---|:---|
| **Objective** | Position Nuclei correctly: after asset discovery, before manual testing. |
| **Expected Output** | Methodology flow: Amass → httpx (live hosts) → **Nuclei** (automated vuln detection) → Burp Suite (manual testing of interesting findings) → Report. |

### Task 7.2 — Avoiding Noise and False Positives

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min
| Field | Detail |
|:---|:---|
| **Objective** | Tune Nuclei scans to minimize false positives and avoid noisy/unreliable templates. |
| **Skills Learned** | `-exclude-tags dos,fuzz,brute-force` (skip intrusive checks), template quality ratings, verifying each finding manually before reporting, using `-validate` to check template correctness before running. |

### Task 7.3 — Responsible Disclosure via Nuclei Findings

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min
| Field | Detail |
|:---|:---|
| **Objective** | Understand how to responsibly handle Nuclei findings in bug bounty and pentest contexts. |
| **Skills Learned** | Verifying findings before submitting (no raw scanner output submissions — all findings require manual verification), severity classification, writing clear PoC for each finding, understanding scope boundaries. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Custom Template Portfolio

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 4–6 hours
Write 5 original Nuclei templates: 2 CVE PoCs, 2 exposure checks, 1 misconfiguration. Test all against lab targets. Publish to your GitHub. This is an excellent portfolio piece for security engineering roles.

### Challenge 8.2 — Full Bug Bounty Pipeline in a Script

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 4 hours
Automate: domain input → Amass + Subfinder → httpx → Nuclei → output report. Single bash script, handles rate limiting, deduplication, and severity filtering. Run against a bug bounty program.

### Challenge 8.3 — Valid Bug Bounty Submission

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ Variable
Find and responsibly disclose a valid vulnerability via Nuclei discovery (manually verified) on a bug bounty program. Document methodology for portfolio.

---

## 🎓 Competency Matrix

| Skill | Beginner | Intermediate | Advanced |
|:------|:--------:|:------------:|:--------:|
| Run basic scan with severity filter | [ ] | | |
| Technology fingerprinting | [ ] | | |
| CVE scanning with tag filter | | [ ] | |
| Misconfiguration and exposure detection | | [ ] | |
| Full Amass → httpx → Nuclei pipeline | | [ ] | |
| Output parsing with jq | | [ ] | |
| Write simple exposure template | | [ ] | |
| Write CVE PoC template | | | [ ] |
| Continuous monitoring automation | | | [ ] |
| Template contribution to community | | | [ ] |

---

## 💬 Interview Questions

1. How does Nuclei's template engine differ from Nikto's scanning approach?
2. What is the nuclei-templates repository and how do you keep it updated?
3. What severity levels does Nuclei use and when would you filter to only `critical,high`?
4. Describe the full pipeline from domain name to Nuclei vulnerability findings.
5. How would you write a Nuclei template to detect an exposed `.git` directory?
6. What are matchers and extractors in a Nuclei template? Give an example of each.
7. How do you prevent Nuclei from running intrusive/DoS templates during a bug bounty?
8. What is the difference between tags `-tags wordpress` and `-t cves/`?
9. How would you integrate Nuclei into a CI/CD pipeline for continuous security monitoring?
10. What are the limitations of automated scanners like Nuclei compared to manual testing with Burp Suite?
