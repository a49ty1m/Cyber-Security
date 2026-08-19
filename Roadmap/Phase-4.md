# Phase 4: Web & Application Security

---

### 🧭 Navigation
◀ [Phase 3](Phase-3.md) | 🏠 [Master Roadmap](README.md) | [Phase 5](Phase-5.md) ➔

---

> [!NOTE]
> **Phase Overview**
> - **⏱️ Time Commitment (Full-Time):** 3–4 months
> - **⏱️ Time Commitment (Part-Time):** 4–7 months
> - **🎯 Primary Focus:** Web application hacking, web server exploitation, API security (OWASP API Top 10), and professional bug bounty methodology.

---

> [!NOTE]
> ### 📝 Phase 4 Documentation Requirements
> Every vulnerability you discover must be documented to professional reporting standards. Required artifacts:
> - **Bug reports** in standard format (title, severity, description, steps to reproduce, impact, remediation)
> - **Burp request/response pairs** — saved HTTP interactions proving each vulnerability
> - **PortSwigger lab solutions** — writeups for each completed lab explaining the vulnerability class
> - **PoC screenshots and videos** — visual evidence for every finding
> - **Git commits** — all reports and evidence committed to your repository
>
> _By the end of Phase 4, you should have a library of vulnerability reports ready for your portfolio._

---

### 🗂️ Table of Contents
- [Part 17: Web Application Hacking](#part-17-web-application-hacking)
  - [Stage 1: Reconnaissance & Mapping](#stage-1-reconnaissance-mapping)
  - [Stage 2: Vulnerability Analysis & Probing](#stage-2-vulnerability-analysis-probing)
  - [Stage 3: Exploitation (The OWASP Top 10)](#stage-3-exploitation-the-owasp-top-10)
  - [Stage 4: Post-Exploitation & Persistence](#stage-4-post-exploitation-persistence)
  - [Stage 5: Defense & Mitigation (The Shield)](#stage-5-defense-mitigation-the-shield)
  - [Lab Progression (Part 17: Web Application Hacking)](#lab-progression-part-17-web-application-hacking)
- [Part 18: Web Server Hacking](#part-18-web-server-hacking)
  - [Stage 1: Target Acquisition & Reconnaissance](#stage-1-target-acquisition-reconnaissance)
  - [Stage 2: Scanning & Service Enumeration](#stage-2-scanning-service-enumeration)
  - [Stage 3: Vulnerability Assessment & Exploitation](#stage-3-vulnerability-assessment-exploitation)
  - [Stage 4: Post-Exploitation & Persistence](#stage-4-post-exploitation-persistence)
  - [Lab Progression (Part 18: Web Server Hacking)](#lab-progression-part-18-web-server-hacking)
- [Part 19: API Security](#part-19-api-security)
  - [Stage 1: API Reconnaissance & Mapping](#stage-1-api-reconnaissance-mapping)
  - [Stage 2: OWASP API Security Top 10](#stage-2-owasp-api-security-top-10)
  - [Stage 3: Protocol-Specific API Attacks](#stage-3-protocol-specific-api-attacks)
  - [Stage 4: API Authentication & Token Attacks](#stage-4-api-authentication-token-attacks)
  - [Stage 5: Defense & Hardening](#stage-5-defense-hardening)
  - [Lab Progression (Part 19: API Security)](#lab-progression-part-19-api-security)
- [Part 20: Bug Bounty and Penetration Testing](#part-20-bug-bounty-and-penetration-testing)
  - [Stage 1: Preparation & Scoping](#stage-1-preparation-scoping)
  - [Stage 2: Reconnaissance (The Wide Net)](#stage-2-reconnaissance-the-wide-net)
  - [Stage 3: Vulnerability Assessment (The Deep Dive)](#stage-3-vulnerability-assessment-the-deep-dive)
  - [Stage 4: Exploitation & Validation](#stage-4-exploitation-validation)
  - [Stage 5: Reporting & Triage](#stage-5-reporting-triage)
  - [Stage 6: Professional Development](#stage-6-professional-development)

---

<a id="part-17-web-application-hacking"></a>

## Part 17: Web Application Hacking

> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `The Web Application Hacker's Handbook` — Primary companion — read the chapter matching your current PortSwigger module
> - 🔴 `SQL Injection Attacks and Defense` — Deepest SQLi reference; read alongside PortSwigger SQLi Modules 6–18
> - 🔴 `Burp Suite Compendium` / `The Power of Burp Suite` — Reference — deep Burp feature coverage
> - 🟡 `Web Application Security - Andrew Hoffman` — Full — developer-code-level explanation of WHY each vulnerability exists
> - 🟡 `Web penetration testing with kali linux` — Targeted chapters — Burp, sqlmap, Nikto, ZAP in practice
> - 🟡 `Bypassing Web Application Firewall Workshop` — Full — WAF bypass techniques for filter evasion labs
> - 🟡 `XSS CheatSheet` — Keep open during all PortSwigger XSS modules
> - 🟢 `White Hat Hacking complete guide to XSS Attacks` — Full (short) — structured XSS coverage
> - 🟢 `SQL Injection Attacks` / `SQL Injection Strategies` / `SQL injection CyberSecurity` — Quick reference PDFs
> - 🟢 `Web Application Hacking Advanced SQL Injection and Data Store Attacks` — Advanced DB-level exploitation post-PortSwigger SQLi


> [!IMPORTANT]
> **Phase 4 Resource Alignment**
>
> | Resource | Role |
> |----------|------|
> | **This roadmap (Phase 4)** | Curriculum — what to learn and in what order |
> | **PortSwigger Web Security Academy** | Primary lab environment — do labs that match the current topic |
> | **Burp Suite** | Primary tool for all web testing work |
> | **OWASP Juice Shop / DVWA** | Secondary lab environments for free-form practice |
> | **Web pentesting books/courses** | Reference only — use for a second explanation, not as a competing roadmap |

> [!NOTE]
> **Part 17 Vulnerability Learning Sequence** — work through topics in this order within Stage 3:
>
> ```text
> HTTP/Web fundamentals (already in Phase 1 Part 3C — review if needed)
>         ↓
> Recon & attack-surface mapping → Burp Suite setup
>         ↓
> Content discovery (directories, endpoints, backup files)
>         ↓
> Authentication attacks (broken auth, credential stuffing, password reset flaws)
>         ↓
> Authorization & IDOR (access control bypass, object reference manipulation)
>         ↓
> XSS — Reflected → Stored → DOM-based
>         ↓
> SQL Injection — Error-based → Boolean blind → Time-based blind
>         ↓
> CSRF
>         ↓
> SSRF
>         ↓
> Command Injection
>         ↓
> Path Traversal / LFI / RFI
>         ↓
> XXE (XML External Entity)
>         ↓
> SSTI (Server-Side Template Injection)
>         ↓
> File Upload vulnerabilities
>         ↓
> Business logic flaws
>         ↓
> Web cache poisoning / advanced web attacks
> ```
>
> PortSwigger has labs for every one of these. Do the labs as you reach each topic — not all upfront.


<a id="stage-1-reconnaissance-mapping"></a>
### **Stage 1: Reconnaissance & Mapping**

> [!TIP]
> **Goal:** Understand the target application's structure and technologies.

- [ ] **OSINT & Discovery:** Perform **Reconnaissance** using **Google Dorks, Shodan, Certificate Transparency** to find subdomains, exposed admin panels, and developer info.

- [ ] **Service Enumeration:** Use `[nmap](../Tools/Nmap.md) -sV -sC` to identify web servers, versions, and common vulnerabilities.

- [ ] **Technology Fingerprinting:** Use **Wappalyzer, BuiltWith, WhatWeb** to identify frameworks, CMS, WAF, CDN, and backend technologies.

- [ ] **Content Discovery:** Run **[Gobuster](../Tools/Gobuster.md), [ffuf](../Tools/ffuf.md), dirsearch** to find hidden directories, backup files, API endpoints, and admin panels.

- [ ] **Sitemap & Robots Analysis:** Parse **robots.txt, sitemap.xml, security.txt** for disallowed paths and contact info.

---

<a id="stage-2-vulnerability-analysis-probing"></a>
### **Stage 2: Vulnerability Analysis & Probing**

> [!TIP]
> **Goal:** Find potential entry points and weaknesses.

- [ ] **Input Validation Testing:** Test every input field for **SQL Injection, NoSQL Injection, Command Injection, LDAP Injection**.

- [ ] **Path Manipulation:** Probe for **Directory/Path Traversal** using `../../../etc/passwd` and **LFI/RFI** vulnerabilities.

- [ ] **Logic Testing:** Analyze **authentication/authorization** mechanisms; test for **IDOR, broken access controls, privilege escalation**.

- [ ] **Protocol & Crypto Analysis:** Check **TLS configuration** with **sslyze/testssl.sh**; test for **weak ciphers, certificate issues, HTTPS downgrade**.

- [ ] **API Testing:** Enumerate **REST/GraphQL/SOAP** endpoints; test for **lack of rate limiting, exposed documentation, mass assignment**.

---

<a id="stage-3-exploitation-the-owasp-top-10"></a>
### **Stage 3: Exploitation (The OWASP Top 10)**

> [!TIP]
> **Goal:** Prove the vulnerability and gain access.

- [ ] **Injection Attacks:** Execute **SQL injection** for data extraction; **command injection** for RCE; **LDAP/XPath** injection.

- [ ] **Cross-Site Scripting (XSS):** Deliver **reflected, stored, DOM-based** XSS to steal cookies, hijack sessions, or deface pages.

- [ ] **CSRF & Request Forgery:** Construct **CSRF attacks** to perform state-changing actions; test **SSRF** for internal network access.

- [ ] **Authentication Bypass:** Exploit **logic flaws, password reset**, **JWT manipulation, OAuth misconfigs** to gain unauthorized access.

- [ ] **File Upload Exploitation:** Bypass **filters** to upload **web shells** via **null bytes, double extensions, MIME confusion**.

- [ ] **Deserialization Attacks:** Exploit **unsafe deserialization** in Java/Python/PHP for RCE.

- [ ] **XXE & SSTI:** Parse **malicious XML** for file read; exploit **template engines** (Jinja2, Twig) for code execution.

---

<a id="stage-4-post-exploitation-persistence"></a>
### **Stage 4: Post-Exploitation & Persistence**

> [!TIP]
> **Goal:** Maintain access and pivot deeper.

- [ ] **Web Shell Management:** Deploy **persistent web shells** (PHP, ASPX, JSP) in writable directories.

- [ ] **Database Enumeration:** Extract **credentials, PII, business data** via SQL injection or direct access.

- [ ] **Lateral Movement:** Use compromised web app to **pivot to internal network, access cloud metadata (IMDS), enumerate AWS/Azure resources**.

- [ ] **Data Exfiltration:** Exfil via **DNS, HTTPS covert channels, cloud storage APIs**.

---

<a id="stage-5-defense-mitigation-the-shield"></a>
### **Stage 5: Defense & Mitigation (The Shield)**

> [!TIP]
> **Goal:** Prevent and detect these attacks.

- [ ] **WAF Deployment:** Implement **Web Application Firewall** (ModSecurity, CloudFlare WAF, AWS WAF) with custom rules.

- [ ] **Secure Coding:** Use **parameterized queries, input validation, output encoding, CSP headers** to prevent injections.

- [ ] **Strong Authentication:** Require **MFA/2FA, strong password policies, account lockout, CAPTCHA** after failed attempts.

- [ ] **Security Headers:** Implement **CSP, X-Frame-Options, HSTS, X-Content-Type-Options** to mitigate client-side attacks.

- [ ] **Continuous Monitoring:** Deploy **SIEM, web server logging, intrusion detection** to identify attack patterns.

---

<a id="lab-progression-part-17-web-application-hacking"></a>
### **Lab Progression (Part 17: Web Application Hacking)**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Complete all OWASP Top 10 labs on PortSwigger Web Security Academy | Badge/completion screenshots |
| 2 | Exploit SQLi + XSS + SSRF on DVWA or OWASP Juice Shop | Attack chain documentation with request/response evidence |
| 3 | Perform an authenticated web app assessment on WebGoat (all modules) | Structured vulnerability report |
| 4 | Chain 3+ vulnerabilities for maximum impact on a single lab target (e.g., XSS→session theft→admin access→RCE) | Kill chain diagram + technical report |
| 5 | Write a custom [Burp Suite](../Tools/Burp_Suite.md) extension or automated scanner script | Working extension/script + README |
| 6 | Complete 10 PentesterLab exercises (source-code-level web vulnerability analysis) | Exercise certificates + code review notes |
| 7 | Solve 5 Root-Me web application challenges at intermediate difficulty | Challenge completion screenshots + methodology notes |

**Platform Guide for Phase 4:**

| Platform | Best For | Cost |
|----------|----------|------|
| [PortSwigger Web Security Academy](https://portswigger.net/web-security) | OWASP Top 10 labs, JWT attacks, SSRF, OAuth, deserialization — industry gold standard | Free |
| [PentesterLab](https://pentesterlab.com) | Source-code-based vulnerability training, PHP/Ruby/Python code review, white-box web testing | Free + Pro |
| [Root-Me](https://root-me.org) | 400+ realistic web challenges organized by category and difficulty — excellent for breadth coverage | Free |
| [DVWA / OWASP Juice Shop / WebGoat](https://owasp.org) | Self-hosted intentionally vulnerable apps for manual exploitation practice | Free (self-hosted) |
| [Hack The Box](https://hackthebox.com) | Web-focused machines + Pro Lab environments for realistic enterprise web app testing | Free + VIP |
| [TryHackMe](https://tryhackme.com) | Guided web hacking learning paths — good for structured beginners before PortSwigger | Free + Premium |

> [!IMPORTANT]
> **Move-On Gate:** You can perform a complete web application assessment covering OWASP Top 10, chain vulnerabilities for maximum impact, use Burp Suite professionally, and produce a client-ready web app pentest report.

---

<a id="toc-part-18-web-server-hacking"></a>
<a id="part-18-web-server-hacking"></a>
## Part 18: Web Server Hacking

> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🟡 `Web Application Attacks` — Broad web attack catalog — covers server-side attack vectors beyond SQLi and XSS
> - 🟢 `Web security exposed` — Reference — supplementary web server attack coverage
> - 🟢 `WordPress Hacking and Security` — Reference — CMS-specific attack methodology for real-world scope targets


<a id="stage-1-target-acquisition-reconnaissance"></a>
### **Stage 1: Target Acquisition & Reconnaissance**

> [!TIP]
> **Goal:** Identify the target server and gather intelligence.

- [ ] **OSINT Gathering:** Conduct **Reconnaissance** using **WHOIS, DNS enumeration, Certificate Transparency** to identify IP ranges and domain information.

- [ ] **Network Mapping:** Determine the server's network position via **traceroute, OSINT**; identify if it's in **Perimeter, DMZ, or internal** segments.

- [ ] **Historical Analysis:** Use **Wayback Machine, Shodan history** to identify previous exposures and configuration changes.

---

<a id="stage-2-scanning-service-enumeration"></a>
### **Stage 2: Scanning & Service Enumeration**

> [!TIP]
> **Goal:** Map out the server's attack surface.

- [ ] **Port Scanning:** Use `nmap -sS -sV -sC -p-` to discover **all open ports** and identify services (Apache, Nginx, IIS, Tomcat, SSH, FTP, DB).

- [ ] **Banner Grabbing:** Use **curl, nc, telnet** to grab service banners and identify **software versions, OS fingerprints**.

- [ ] **HTTP Method Enumeration:** Test for **PUT, DELETE, TRACE, OPTIONS** enabled; check **WebDAV** misconfiguration.

- [ ] **Protocol Audit:** Check for **insecure protocols (HTTP, FTP, Telnet)**; analyze **TLS** config with **testssl.sh** for weak ciphers.

- [ ] **Virtual Host Discovery:** Enumerate **vhosts** via **Host header manipulation, DNS brute-forcing** to find hidden services.

---

<a id="stage-3-vulnerability-assessment-exploitation"></a>
### **Stage 3: Vulnerability Assessment & Exploitation**

> [!TIP]
> **Goal:** Find and exploit flaws to gain initial access.

- [ ] **Patch Audit:** Check for **outdated software versions** against CVE databases; test for **known exploits** (Apache Struts, IIS 6.0, etc.).

- [ ] **Web Application Attacks:** Attempt **SQL injection, XSS, file upload** against hosted applications to compromise the web server.

- [ ] **File System Attacks:** Test for **directory traversal** (`../../../etc/passwd`), **LFI/RFI**, **arbitrary file read**.

- [ ] **Service Exploitation:** Look for **buffer overflow, format string, RCE** exploits for specific service versions (Apache mod_ssl, ProFTPd, vsftpd).

- [ ] **Credential Attacks:** Launch **brute force, password spray, dictionary attacks** against **SSH, FTP, admin panels** with [Hydra](../Tools/Hydra.md)/Medusa.

- [ ] **Default Credentials:** Test **default admin passwords** for web servers (tomcat/tomcat, admin/admin) and management interfaces.

---

<a id="stage-4-post-exploitation-persistence"></a>
### **Stage 4: Post-Exploitation & Persistence**

> [!TIP]
> **Goal:** Escalate privileges and maintain control.

- [ ] **Privilege Escalation:** After gaining low-privilege shell, use **kernel exploits, SUID binaries, sudo misconfigs, service misconfigurations** for root/SYSTEM.

- [ ] **Web Shell Deployment:** Upload **persistent web shells** (b374k, c99, webacoo) to writable web directories for backdoor access.

- [ ] **Living off the Land:** Use **LOLBAS/GTFOBins** for post-exploitation execution and persistence. 📌 _See Part 7 Stage 2 for full LOLBAS/GTFOBins coverage._

- [ ] **Credential Harvesting:** Dump **database credentials, config files** (`web.config`, `wp-config.php`), **SSH keys** for lateral movement.

- [ ] **Covering Tracks:** Clear **access logs, error logs, auth logs**; use **timestomping** to hide file modifications.

---

<a id="lab-progression-part-18-web-server-hacking"></a>
### **Lab Progression (Part 18: Web Server Hacking)**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Enumerate and exploit a vulnerable web server (Metasploitable 2/3) | Exploitation walkthrough |
| 2 | Gain shell via file upload or RCE on a lab web server | Web shell deployment report |
| 3 | Escalate from web shell to root/SYSTEM on the host | Full attack chain document |
| 4 | Exploit a misconfigured web server (default creds, PUT method, WebDAV) | Misconfiguration exploitation report |
| 5 | Harden a web server against all attacks you performed | Hardening checklist + before/after comparison |

> [!IMPORTANT]
> **Move-On Gate:** You can identify web server technologies, exploit known service vulnerabilities, escalate privileges from web shell to root/SYSTEM, and produce hardening recommendations based on your findings.

---

<a id="toc-part-19-api-security"></a>
<a id="part-19-api-security"></a>
## Part 19: API Security

> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Hacking APIs Breaking Web Application Programming Interfaces - Corey` — Full book — the best dedicated API security resource; maps directly to this Part
> - 🟡 `Web security testing guide` — Reference — OWASP WSTG API test cases; use IDs when writing reports


<a id="stage-1-api-reconnaissance-mapping"></a>
### **Stage 1: API Reconnaissance & Mapping**

> [!TIP]
> **Goal:** Discover and map API attack surface.

- [ ] **API Discovery:** Find undocumented endpoints via **JS file analysis, Wayback Machine, Google Dorks (`site:target.com api`), Shodan**, and **Burp Suite passive crawling**.

- [ ] **Spec File Harvesting:** Locate exposed **OpenAPI/Swagger (`/swagger.json`, `/api-docs`), WSDL, GraphQL introspection** schemas that reveal all routes, parameters, and data models.

- [ ] **Endpoint Enumeration:** Fuzz **API paths and versions** (`/api/v1/`, `/api/v2/`, `/v3/`) using **ffuf, kiterunner, Arjun** with API-specific wordlists.

- [ ] **Technology Fingerprinting:** Identify **framework, auth scheme, rate limiting, versioning strategy** from headers, response patterns, and error messages.

---

<a id="stage-2-owasp-api-security-top-10"></a>
### **Stage 2: OWASP API Security Top 10**

> [!TIP]
> **Goal:** Methodically test each API-specific vulnerability class.

- [ ] **API1 — Broken Object Level Authorization (BOLA/IDOR):** Substitute **object IDs** (user, order, account) in requests to access **other users' resources** without authorization check.

- [ ] **API2 — Broken Authentication:** Test **weak tokens, missing expiry, no rate limiting on login, JWT algorithm confusion (`alg:none`), token reuse after logout**.

- [ ] **API3 — Broken Object Property Level Authorization (BOPLA):** Send **extra fields** in PUT/PATCH requests to modify properties the user shouldn't control (e.g., `"role":"admin"`, `"is_verified":true`).

- [ ] **API4 — Unrestricted Resource Consumption:** Test **missing rate limits, no pagination caps, large payload DoS, CPU-exhausting regex/query parameters**.

- [ ] **API5 — Broken Function Level Authorization (BFLA):** Access **admin-only endpoints** (`/api/admin/users`, `/api/internal/`) using **regular user tokens**; test HTTP method switching (GET → DELETE).

- [ ] **API6 — Unrestricted Access to Sensitive Business Flows:** Abuse **checkout flows, invite systems, voting, coupon redemption** without rate limiting or workflow enforcement.

- [ ] **API7 — Server-Side Request Forgery (SSRF):** Supply **internal URLs, cloud metadata endpoints** (`169.254.169.254`) as API parameters for internal network pivoting.

- [ ] **API8 — Security Misconfiguration:** Find **exposed debug endpoints, verbose errors, missing CORS restrictions, HTTP instead of HTTPS, default API keys**.

- [ ] **API9 — Improper Inventory Management:** Target **deprecated API versions, shadow APIs, staging/dev endpoints** still accessible in production.

- [ ] **API10 — Unsafe Consumption of APIs:** Exploit **third-party API data** that is trusted and processed without validation, causing **injection or SSRF** on the consuming server.

---

<a id="stage-3-protocol-specific-api-attacks"></a>
### **Stage 3: Protocol-Specific API Attacks**

> [!TIP]
> **Goal:** Attack REST, GraphQL, gRPC, and SOAP distinctly.

- [ ] **REST API Testing:** Chain **BOLA + privilege escalation**, test **HTTP verb tampering**, exploit **mass assignment** via undocumented writable fields.

- [ ] **GraphQL Attacks:** Run **introspection queries** to dump full schema; exploit **batching/aliasing for DoS**, **nested query depth abuse**, **IDOR via node IDs**, and **mutations without auth checks**.

- [ ] **gRPC Security:** Use **grpcurl, Evans** to enumerate services; test for **missing auth interceptors, reflection enabled in prod, proto injection**.

- [ ] **SOAP/XML APIs:** Exploit **XXE via SOAP body**, test **WS-Security header bypass**, abuse **type confusion in XML parsing**.

---

<a id="stage-4-api-authentication-token-attacks"></a>
### **Stage 4: API Authentication & Token Attacks**

> [!TIP]
> **Goal:** Break API authentication mechanisms.

- [ ] **JWT Attacks:** Test **`alg:none` bypass, RS256→HS256 confusion, weak secret brute-force (hashcat mode 16500), kid injection, jku/x5u header injection** to forge arbitrary tokens.

- [ ] **OAuth 2.0 Attacks:** Exploit **CSRF on authorization endpoint, open redirect in redirect_uri, state parameter bypass, token leakage via Referer header**.

- [ ] **API Key Attacks:** Find **keys in JS bundles, git history, response headers, error messages**; test **key rotation absence, missing key scoping**.

- [ ] **mTLS Bypass:** Identify **endpoints that skip client certificate validation**, abuse **certificate pinning gaps**, exploit **proxy stripping of client certs**.

---

<a id="stage-5-defense-hardening"></a>
### **Stage 5: Defense & Hardening**

> [!TIP]
> **Goal:** Know what defenders implement so you can test it properly.

- [ ] **API Gateway Controls:** Understand **rate limiting, quota enforcement, request validation, JWT verification, IP allowlisting** at the gateway layer.

- [ ] **Input Validation:** Test that **schema validation, type enforcement, max length, allowed values** are enforced server-side not just client-side.

- [ ] **Logging & Monitoring:** Verify **all API calls are logged** with enough context (user, IP, endpoint, response code) for anomaly detection.

---

<a id="lab-progression-part-19-api-security"></a>
### **Lab Progression (Part 19: API Security)**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Complete crAPI (completely ridiculous API) lab — all OWASP API Top 10 challenges | Challenge completion documentation |
| 2 | Test BOLA, broken auth, and mass assignment against vAPI or Juice Shop API | OWASP API assessment report |
| 3 | Exploit JWT algorithm confusion (`alg:none`, RS256→HS256) and forge tokens in a lab API | JWT attack PoC + writeup |
| 4 | Write automated API security tests using [Postman](../Tools/Postman.md) collections or Burp macros | Test suite + results |
| 5 | Audit a GraphQL API (introspection dump, batching abuse, nested query DoS, IDOR via node IDs) | GraphQL security assessment report |

> [!IMPORTANT]
> **Move-On Gate:** You can discover undocumented API endpoints, test all OWASP API Top 10 categories, exploit JWT/OAuth flaws, attack REST/GraphQL/gRPC APIs, and produce a professional API security assessment report.

---

<a id="toc-part-20-bug-bounty-and-penetration-testing"></a>
<a id="part-20-bug-bounty-and-penetration-testing"></a>
## Part 20: Bug Bounty and Penetration Testing

> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `zseano's methodology` — Full (short) — practical bug bounty workflow from an experienced hunter
> - 🔴 `From Hacking to Report Writing` — Full — bridges exploitation to professional report writing; read before Part 39
> - 🟡 `Bug Bounty Hunting For Web Security` — Full — platform-specific methodology for HackerOne, Bugcrowd etc.
> - 🟡 `Web security testing guide` — Reference — OWASP WSTG test case IDs for reporting (e.g. WSTG-INPV-05)
> - 🟢 `Web Application Pentest Methodology` — Reference — structured methodology doc to use during assessments


<a id="stage-1-preparation-scoping"></a>
### **Stage 1: Preparation & Scoping**

> [!TIP]
> **Goal:** Stay legal and define the target.

- [ ] **Legal Check:** Read and sign the `Penetration Testing Rules of Engagement` or the Bug Bounty Policy (Safe Harbor).

- [ ] **Scope Validation:** Confirm IP ranges and domains. Ensure you are not attacking "Out of Scope" assets.

- [ ] **Framework Selection:** Decide which **testing methodology** governs the engagement:
  - **OWASP WSTG (Web Security Testing Guide)** — the methodology for *how to test* web applications; test cases are referenced by ID (e.g., WSTG-INPV-01 for SQL injection)
  - **NIST SP 800-115** — federal/regulated-industry methodology
  - **PTES** — comprehensive red team engagement framework

  > [!WARNING]
  > **Critical Distinction:** The **OWASP Top 10** is a *vulnerability classification list* used to categorize and report findings — it is NOT a testing methodology. Saying you "test against OWASP Top 10" is a common red flag in interviews and client engagements. You *test using OWASP WSTG* and *report findings mapped to OWASP Top 10 categories*. These are different documents serving different purposes.

---

<a id="stage-2-reconnaissance-the-wide-net"></a>
### **Stage 2: Reconnaissance (The Wide Net)**

> [!TIP]
> **Goal:** Find what others missed.

- [ ] **Subdomain Enumeration:** Use **OSINT** tools to find `dev`, `stage`, or `test` subdomains.

- [ ] **Port Scanning:** Run `nmap` to identify non-standard ports (e.g., 8080, 8443) and running services.

- [ ] **Tech Stack Analysis:** Use `curl` or browser extensions to identify the server, framework (React, Angular), and backend (PHP, Python).

---

<a id="stage-3-vulnerability-assessment-the-deep-dive"></a>
### **Stage 3: Vulnerability Assessment (The Deep Dive)**

> [!TIP]
> **Goal:** Find the flaw.

- [ ] **Input Fuzzing:** Test all input fields for `SQL Injection` (WSTG-INPV-05), `Cross-Site Scripting` (WSTG-CLNT-01), `Command Injection` (WSTG-INPV-12), `Server-Side Template Injection` (WSTG-INPV-18), `HTTP Parameter Pollution`, and `Mass Assignment` vulnerabilities.

  > [!NOTE]
  > **Do NOT test for Buffer Overflow in web application input fields.** Web applications run on managed-memory, interpreted runtimes (PHP, Python, Ruby, Node.js, Java). Buffer overflows are memory-corruption vulnerabilities in compiled binary applications — testing a PHP login form for buffer overflows is technically incorrect and will waste time. Buffer overflows belong in Phase 7 (Binary Exploitation). In web app testing, focus on injection and logic flaws.

- [ ] **Access Control:** Test for `IDOR` (Insecure Direct Object Reference) and verify `Authentication vs Authorization` logic.

- [ ] **Configuration Check:** Look for `Directory Traversal`, exposed `.git` folders, or default credentials (`admin/admin`).

---

<a id="stage-4-exploitation-validation"></a>
### **Stage 4: Exploitation & Validation**

> [!TIP]
> **Goal:** Prove the risk without breaking the system.

- [ ] **PoC Development:** Create a non-destructive Proof of Concept. (e.g., `alert(1)` for XSS, `whoami` for RCE).

- [ ] **False Positive Check:** Verify the finding is a `True Positive` before reporting.

- [ ] **Lateral Movement:** (Pentest only) Attempt `Privilege Escalation` or `Pass the Hash` if internal access is achieved.

---

<a id="stage-5-reporting-triage"></a>
### **Stage 5: Reporting & Triage**

> [!TIP]
> **Goal:** Get paid and drive remediation.

- [ ] **Impact Assessment:** Clearly explain **business risk** (data breach, financial loss, compliance violation) to management.

- [ ] **Proof of Concept:** Provide **detailed steps, screenshots, videos, request/response** to reproduce the vulnerability.

- [ ] **Remediation Guidance:** Offer **specific technical fixes** (parameterized queries, input validation, patching) with code examples.

- [ ] **CVSS Scoring:** Calculate **CVSS score** to quantify severity and prioritize remediation.

---

<a id="stage-6-professional-development"></a>
### **Stage 6: Professional Development**

> [!TIP]
> **Goal:** Build skills and reputation.

- [ ] **Platform Selection:** Focus on **HackerOne, Bugcrowd, Synack, Intigriti** platforms with active programs.

- [ ] **Specialization:** Develop expertise in **specific areas** (API security, mobile, cloud, blockchain).

- [ ] **Documentation:** Maintain **personal writeups, CVEs, Hall of Fame entries** for portfolio building.

- [ ] **Community Engagement:** Participate in **CTFs, conferences, Twitter/Discord security communities** for networking.

- [ ] **Continuous Learning:** Stay updated on **latest vulnerabilities, techniques, tools** through blogs, research papers, trainings.

---

### 🏆 Phase 4 Capstone Project

**Find and Document 5 Web Vulnerabilities Across Multiple Targets**

- [ ] **Identify 5 distinct vulnerability types** across 2+ targets (PortSwigger labs, DVWA, Juice Shop, or bug bounty programs)
- [ ] **Write a professional report** for each finding with CVSS scoring
- [ ] **Create PoC demonstrations** (non-destructive) for each vulnerability
- [ ] **Propose remediation** for each finding with code-level fixes where applicable

**Deliverables:**
- [ ] 5 vulnerability reports following responsible disclosure format
- [ ] PoC evidence (Burp exports, screenshots, curl commands)
- [ ] Remediation guide with before/after code examples
- [ ] All reports committed to your Git repository

> [!IMPORTANT]
> **Capstone Gate:** Your 5 reports must each contain reproducible steps, accurate CVSS scores, and actionable remediation guidance.

---

### 🧭 Phase 4 Reflection & Competency Check

- [ ] **Reflection:** Which vulnerability class was easiest to find but hardest to explain clearly?

- [ ] **Reflection:** Where did your first proof of concept need restraint to stay non-destructive?
- [ ] **Competency:** Can you map web and API findings to root cause, impact, and remediation?
- [ ] **Competency:** Can you reproduce each finding from a clean browser/session using only your report?
- [ ] **Competency:** Can you write reports that developers can fix without asking for missing steps?

> [!IMPORTANT]
> **Phase Completion Gate:** Move on only when your web findings are reproducible, responsibly scoped, accurately scored, and paired with concrete fixes.

---

<a id="toc-part-21-wireless-pentesting"></a>

---

<a id="phase-4-mini-projects"></a>

## 🛠️ Phase 4 Mini Projects

> [!TIP]
> **Why these projects are here:** Phase 4 covers web application hacking, web server exploitation, API security, and bug bounty methodology. All 9 projects below map directly to Parts 17–20 of this phase. They are not shortcuts — build each one *after* completing its corresponding Part, so you understand the vulnerability class before you write a tool to detect it.

> [!NOTE]
> **How to use this section:** Projects 15–22 are individual vulnerability checkers. Project 23 (Web Vulnerability Scanner) is the capstone — it integrates all the others into a single tool. Do not start Project 23 until all preceding projects are complete and working. All code must be committed to Git with proper READMEs that include: what vulnerability it targets, how it works, what it *cannot* detect, and ethical usage requirements.

---

### Project 15 — Website Security Header Checker

**Maps to:** Part 17 (Web Application Hacking) → Stage 1: Reconnaissance & Mapping + Stage 5: Defense & Mitigation

**What it is:** A tool that sends an HTTP(S) request to a target URL and analyzes the response headers for the presence and correctness of security headers: `Content-Security-Policy`, `Strict-Transport-Security`, `X-Content-Type-Options`, `X-Frame-Options`, `Referrer-Policy`, `Permissions-Policy`, `Cross-Origin-Opener-Policy`, and `Cross-Origin-Resource-Policy`. Grades each header (present/misconfigured/missing) and outputs an overall security score.

**What you need before building it:**
- HTTP request-response cycle: headers are sent by the server, parsed by the browser
- What each header does and what its *absence* enables:
  - Missing `CSP` → XSS can execute arbitrary scripts
  - Missing `HSTS` → SSL stripping attacks are possible
  - Missing `X-Frame-Options` or `CSP frame-ancestors` → clickjacking is possible
  - Missing `X-Content-Type-Options: nosniff` → MIME-sniffing attacks possible
- `requests` library (Python) for HTTP
- OWASP Secure Headers Project as your reference for correct values

**Why build it:**
Security headers are the first passive defense layer of any web application, and the majority of real-world sites fail basic header audits. Building this checker forces you to internalize what each header *prevents* — not just memorize their names. This knowledge transfers directly to code review, penetration testing, and secure development. It also gives you a tool that produces immediate, demonstrable value on any website — useful for bug bounty first steps.

**Deliverable:** Python CLI — `check <url>`. Output: table of headers, presence status, and what each missing header risks. Include an overall letter grade (A–F). README must explain what clickjacking is and which header prevents it.

---

### Project 16 — SSL/TLS Certificate Checker

**Maps to:** Part 17 (Web Application Hacking) → Stage 1: Reconnaissance & Mapping + Part 18 (Web Server Hacking) → Stage 2: Scanning & Service Enumeration

**What it is:** A tool that connects to a target hostname, retrieves the TLS certificate chain, and checks: certificate expiry date and validity window, hostname match (CN/SAN verification), certificate chain completeness, issuer and signature algorithm (flag SHA-1 signatures), TLS protocol version (flag TLS 1.0/1.1 and SSLv3), and cipher suite strength (flag export ciphers, RC4, DES).

**What you need before building it:**
- TLS handshake mechanics: ClientHello → ServerHello → Certificate → Key Exchange → Finished
- Certificate structure: Subject, Issuer, SAN (Subject Alternative Names), validity period, signature algorithm
- Python `ssl` module: `ssl.create_default_context()`, `ssl.SSLSocket.getpeercert()`
- `pyOpenSSL` for more detailed certificate chain inspection
- Know what `ssl.PROTOCOL_TLS_CLIENT` does vs constructing a context manually

**Why build it:**
Certificate misconfiguration is a frequent finding in professional audits and bug bounty programs. Expired certificates cause service outages. Weak cipher suites are exploitable. TLS 1.0/1.1 vulnerabilities (BEAST, POODLE) are well-documented. Building this tool means you understand TLS not just as "the green padlock" but as a protocol with version numbers, cipher negotiation, and a chain of trust that must be validated properly. This directly prepares you for understanding certificate-based authentication, MTLS, and PKI in Phase 6.

**Deliverable:** Python CLI — `check <hostname>`. Output: certificate details table with expiry, issuer, SAN list, protocol version, cipher suite, and flagged issues. README must explain what an expired certificate means for a production service and why SHA-1 signatures are deprecated.

---

### Project 17 — SQL Injection Detection Tool

**Maps to:** Part 17 (Web Application Hacking) → Stage 3: Exploitation (OWASP Top 10) — specifically A03:2021 Injection

**What it is:** An automated SQL injection tester for authorized web applications. Identifies injectable parameters (URL query strings, POST body fields), tests each parameter with error-based, boolean-based, and time-based payloads, analyzes responses for SQL error messages or behavioral anomalies, and generates a finding report with reproduction steps.

**What you need before building it:**
- SQL syntax basics: `SELECT`, `WHERE`, `UNION`, `--` (comment), `'` (string delimiter)
- The 3 main SQLi types:
  - **Error-based:** inject `'` → server returns a database error message containing SQL syntax
  - **Boolean-based blind:** inject `' AND 1=1--` (true) vs `' AND 1=2--` (false) → compare response differences
  - **Time-based blind:** inject `'; WAITFOR DELAY '0:0:5'--` (MSSQL) or `'; SELECT SLEEP(5)--` (MySQL) → measure response time
- HTTP parameter extraction with `BeautifulSoup` (parse HTML forms) and `requests`
- Database-specific error signatures: MySQL, PostgreSQL, MSSQL, SQLite each have distinct error strings

**Why build it:**
SQL injection has been in the OWASP Top 10 every year since its inception. It caused the Adobe breach (153M records), LinkedIn breach (117M), and hundreds of others. Building a detector forces you to think like an attacker — what does putting `'` in an input field actually do to a SQL query? What does a time delay reveal when there's no visible output? The understanding you gain here is what separates a developer who knows SQLi exists from one who can identify and fix it in production code.

**Deliverable:** Python CLI — `scan <url> --params auto`. Inject payloads into detected parameters, output findings as a structured report with: parameter name, injection type, payload used, evidence. README must include a lab setup section using DVWA or Juice Shop (never test on live sites without permission).

---

### Project 18 — XSS Scanner

**Maps to:** Part 17 (Web Application Hacking) → Stage 3: Exploitation (OWASP Top 10) — A03:2021 Injection (client-side)

**What it is:** A reflected XSS detection tool that: extracts injectable parameters from a target URL (query strings, form inputs), injects a set of XSS probe payloads, analyzes the HTML response to check if the payload appears unescaped in the output, and reports confirmed findings. Optionally uses a headless browser (Playwright) to detect DOM-based XSS.

**What you need before building it:**
- How browsers parse HTML and when script tags execute
- The 3 XSS types:
  - **Reflected:** payload in URL → reflected in immediate response → executes in victim's browser
  - **Stored:** payload saved to database → executes every time the page loads (not testable with this tool alone)
  - **DOM-based:** payload processed by client-side JavaScript — requires a headless browser to detect
- XSS payload variants: `<script>alert(1)</script>`, `"><img src=x onerror=alert(1)>`, `javascript:alert(1)`, attribute injection
- Why `<script>alert(1)</script>` doesn't always work: HTML encoding, Content-Security-Policy, modern browser mitigations
- `BeautifulSoup` for HTML response parsing

**Why build it:**
XSS enables session hijacking (steal `document.cookie`), credential phishing (inject fake login forms), defacement, and malware distribution. Detecting it requires understanding how browsers interpret HTML differently depending on context (HTML body vs attribute vs JavaScript string). Building this scanner forces you to internalize exactly why output encoding — not input filtering — is the correct defense. Every output in a web app has a context, and that context determines the correct encoding function.

**Deliverable:** Python CLI — `scan <url>`. Output: list of reflected parameters with payload evidence. README must explain the difference between reflected and stored XSS and why your tool can only detect reflected.

---

### Project 19 — Phishing URL Detector

**Maps to:** Part 10 (Social Engineering) → Stage 2: The Digital Assault (Remote Vectors) + Part 17 Stage 3: OWASP A09 Security Logging and Monitoring Failures

**What it is:** A URL analysis tool that scores a given URL's likelihood of being a phishing link based on: lexical features (URL length, number of dots, presence of IP address, suspicious keywords like `paypal-secure`, `login-verify`), homoglyph detection (lookalike characters: `рaypal.com` using Cyrillic `р`), domain age via WHOIS (newly registered domains are high risk), entropy of the subdomain, and reputation check via VirusTotal API and Google Safe Browsing API.

**What you need before building it:**
- URL structure: scheme, subdomain, domain, TLD, path, query, fragment — know what each part is
- Unicode homoglyphs: `а` (Cyrillic) looks identical to `a` (Latin) — phishers exploit this
- Levenshtein distance for typosquatting detection (e.g., `gooogle.com` vs `google.com`)
- WHOIS domain age: `python-whois` library
- VirusTotal API (free tier: 4 requests/minute) — requires an API key
- Google Safe Browsing API (free) — requires a Google Cloud API key
- Shannon entropy calculation for detecting algorithmically generated subdomains (DGA)

**Why build it:**
Phishing is the #1 initial access vector in real-world attacks — responsible for over 80% of reported security incidents according to Verizon DBIR. This is also where security meets machine learning: production phishing detectors at Google, Microsoft, and Cloudflare use ML models trained on millions of URLs. Building the feature-extraction and rule-based version teaches you what features matter and *why*, which is the foundation for building or evaluating ML-based versions later. It also gives you hands-on experience with real threat intelligence APIs.

**Deliverable:** Python CLI — `analyze <url>`. Output: feature breakdown table with scores, overall risk verdict (Likely Phishing / Suspicious / Likely Safe), and evidence. README must explain what a homoglyph attack is with a real example.

---

### Project 20 — Command Injection Detector

**Maps to:** Part 17 (Web Application Hacking) → Stage 3: Exploitation (OWASP Top 10) — A03:2021 Injection (OS command)

**What it is:** A tool that tests authorized web application endpoints for OS command injection by injecting shell metacharacters and command chaining operators into parameters, analyzing responses for command output or timing anomalies, and reporting confirmed injection points with payload evidence.

**What you need before building it:**
- Linux/Unix shell operators: `;` (sequential execution), `|` (pipe), `&&` (AND), `||` (OR), `` ` `` (backtick subshell), `$()` (subshell)
- Windows command chaining: `&`, `&&`, `|`, `||`, `%0A` (URL-encoded newline)
- Blind command injection: when there's no visible output, use time-based payloads (`; sleep 5`) or out-of-band (DNS/HTTP callback to a server you control)
- Why command injection happens: web apps that call `os.system()`, `subprocess.call()`, `exec()`, or shell=True with unsanitized user input
- Payloads: `; id`, `| whoami`, `&& cat /etc/passwd`, `$(id)`, backtick variants

**Why build it:**
Command injection is the highest-severity web vulnerability class — successful exploitation gives an attacker direct shell access to the server. Unlike SQLi (database) or XSS (browser), command injection compromises the entire operating system. Understanding how to detect it requires knowing how web applications interact with the underlying OS, why `shell=True` in Python's `subprocess` is dangerous, and what a WAF can and cannot block. This knowledge directly informs secure code review.

**Deliverable:** Python CLI — `scan <url> --params <param1,param2>`. Inject payloads, detect command output or timing anomalies, output findings. README must include a vulnerable test case setup using DVWA and explain why `shell=False` with explicit argument lists prevents injection.

---

### Project 21 — SSRF Detection Tool

**Maps to:** Part 17 (Web Application Hacking) → Stage 3: Exploitation (OWASP Top 10) — A10:2021 Server-Side Request Forgery

**What it is:** A tool that tests authorized web applications for Server-Side Request Forgery by submitting internal network addresses and cloud metadata endpoints as URL parameters, detecting whether the server fetches those URLs (via response content analysis or out-of-band callback), and reporting confirmed SSRF with potential impact analysis.

**What you need before building it:**
- What SSRF is: an attacker controls a URL that the *server* fetches — the server becomes a proxy for attacking internal resources
- Internal network targets: `http://127.0.0.1/`, `http://localhost/`, `http://169.254.169.254/` (AWS EC2 metadata), `http://192.168.x.x/`, `http://[::1]/`
- Cloud metadata endpoints:
  - AWS: `http://169.254.169.254/latest/meta-data/iam/security-credentials/`
  - GCP: `http://metadata.internal/computeMetadata/v1/`
  - Azure: `http://169.254.169.254/metadata/instance`
- Out-of-band detection: set up a webhook (Webhook.site, Interactsh, or self-hosted) and use your webhook URL as the payload — if the server calls your webhook, SSRF is confirmed
- URL parser bypass techniques: `http://evil.com@127.0.0.1/`, DNS rebinding concepts

**Why build it:**
SSRF became a critical vulnerability class with cloud adoption. The 2019 Capital One breach — 100 million records stolen — was executed via SSRF against the AWS EC2 metadata service to steal IAM credentials. Understanding SSRF requires understanding cloud architecture, internal service communication, and why "the server can reach internal services" is a dangerous design assumption. This project also introduces you to out-of-band detection, a technique used throughout professional penetration testing for blind vulnerabilities.

**Deliverable:** Python CLI — `scan <url> --param <url-parameter>`. Test with internal IP payloads and cloud metadata endpoints. Set up Interactsh for OOB detection. Output: confirmed SSRF findings with impact analysis. README must explain the Capital One breach at a high level and which SSRF mitigation (allowlist vs blocklist) is more reliable.

---

### Project 22 — Directory Brute-Force Tool

**Maps to:** Part 17 (Web Application Hacking) → Stage 1: Reconnaissance & Mapping — specifically content discovery

**What it is:** A web directory and file enumeration tool that sends HTTP requests for each entry in a wordlist, analyzes response codes and content lengths to identify valid paths, filters false positives (servers that return 200 for all requests), and reports discovered directories and files with their HTTP status and size.

**What you need before building it:**
- HTTP status codes: 200 (found), 301/302 (redirect — still interesting), 403 (forbidden — path exists, just restricted), 404 (not found), 500 (server error — may indicate the path processes something)
- False positive filtering: some servers return 200 for every path (catch-all) — detect this by comparing content-length variance across responses
- Wordlists: SecLists `Discovery/Web-Content/` — `common.txt` for quick sweeps, `raft-large-files.txt` for thorough enumeration
- Async HTTP (`asyncio` + `aiohttp`) — sending 10,000 requests sequentially is unusably slow; concurrent async requests make it practical
- Rate limiting and backoff: don't DoS the target or trigger WAF rate limits

**Why build it:**
Exposed `.git` directories (leaking full source code), `/admin` panels, `/backup.zip` files, `/phpMyAdmin`, and `/wp-login.php` endpoints are found through directory brute-forcing. These are consistently among the most impactful bug bounty findings and real breach vectors. Building the tool teaches you *why* wordlist composition matters (what paths to test), how HTTP response analysis distinguishes existing paths from non-existent ones, and why false-positive filtering is non-trivial. It combines Phase 3 recon techniques with Phase 4 HTTP knowledge.

**Deliverable:** Python CLI — `scan <url> --wordlist <path> --threads <n> --extensions php,html,txt`. Output: table of discovered paths with status codes and content lengths, false-positive-filtered. README must explain what finding an exposed `.git` directory means for a target's security.

---

### Project 23 — Web Vulnerability Scanner (Capstone)

**Maps to:** Part 20 (Bug Bounty & Penetration Testing) → Stage 3: Vulnerability Assessment (The Deep Dive) — entire Phase 4 capstone

**What it is:** An automated web security assessment tool that orchestrates all preceding Phase 4 projects as modules in a single unified workflow. Given a target URL and authorization, it: runs security header checks (Project 15), TLS certificate inspection (Project 16), SQL injection testing (Project 17), XSS scanning (Project 18), command injection testing (Project 20), SSRF testing (Project 21), and directory brute-forcing (Project 22) — then aggregates all findings into a single structured report with severity ratings, reproduction steps, and remediation guidance.

**What you need before building it:**
- All Projects 15–22 must be complete and working as standalone tools
- Plugin/module architecture: each project becomes an importable module with a consistent interface — `run(target, options) → [Finding]`
- Unified finding schema: `{module, severity, title, url, parameter, payload, evidence, remediation}`
- Severity scoring: Critical / High / Medium / Low / Info — apply CVSS-inspired logic
- Async orchestration: run all modules concurrently (not sequentially) to reduce total scan time
- HTML report generation: use `jinja2` templates to produce a clean, shareable HTML report
- Scope enforcement: the tool must accept a scope definition and refuse to scan out-of-scope targets

**Why build it:**
This is the project you show to employers. It doesn't introduce new vulnerability concepts — it demonstrates you can *architect systems*, think about software design (plugin interfaces, unified schemas, concurrent execution), and deliver a professional output (structured report). Recruiters and interviewers don't just see a web scanner — they see evidence that you can integrate multiple domains of knowledge into a cohesive product. A polished version of this with a sample report is your Phase 4 portfolio centerpiece.

It also teaches a critical professional lesson: automated scanners miss things. Your README must document what this scanner *cannot* detect (stored XSS, CSRF, business logic flaws, authentication bypass, insecure direct object references) and why manual testing is still required. That intellectual honesty is what makes a security engineer trustworthy.

**Deliverable:**
- Python package with a CLI entry point: `webscan <url> --scope <domain> --output <report.html>`
- Each vulnerability module importable independently
- HTML report with: executive summary, finding table sorted by severity, per-finding detail pages with PoC steps and remediation
- README with: architecture diagram showing module integration, limitations section, ethical usage requirements, and sample report screenshot

---

> [!IMPORTANT]
> **Phase 4 Project Completion Gate:** Project 23 (the capstone) must produce a report that a security professional could read and act on without asking follow-up questions. If your findings lack reproduction steps, payload evidence, or remediation guidance — the project is not done. Polish the report before moving to Phase 5.
