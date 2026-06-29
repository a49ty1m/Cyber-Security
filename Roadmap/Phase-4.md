# Phase 4: Web & Application Security

---

### 🧭 Navigation
◀ [Phase 3](Phase-3.md) | 🏠 [Master Roadmap](README.md) | [Phase 5](Phase-5.md) ➔

---

> [!NOTE]
> **Phase Overview**
> - **⏱️ Time Commitment (Full-Time):** 2–3 months
> - **⏱️ Time Commitment (Part-Time):** 4–6 months
> - **🎯 Primary Focus:** Web application hacking, web server exploitation, API security (OWASP API Top 10), and professional bug bounty methodology.

---

### 🗂️ Table of Contents
- [Part 17: Web Application Hacking](#part-17-web-application-hacking)
  - [Stage 1: Reconnaissance & Mapping](#stage-1-reconnaissance-mapping)
  - [Stage 2: Vulnerability Analysis & Probing](#stage-2-vulnerability-analysis-probing)
  - [Stage 3: Exploitation (The OWASP Top 10)](#stage-3-exploitation-the-owasp-top-10)
  - [Stage 4: Post-Exploitation & Persistence](#stage-4-post-exploitation-persistence)
  - [Stage 5: Defense & Mitigation (The Shield)](#stage-5-defense-mitigation-the-shield)
  - [Lab Progression](#lab-progression)
- [Part 18: Web Server Hacking](#part-18-web-server-hacking)
  - [Stage 1: Target Acquisition & Reconnaissance](#stage-1-target-acquisition-reconnaissance)
  - [Stage 2: Scanning & Service Enumeration](#stage-2-scanning-service-enumeration)
  - [Stage 3: Vulnerability Assessment & Exploitation](#stage-3-vulnerability-assessment-exploitation)
  - [Stage 4: Post-Exploitation & Persistence](#stage-4-post-exploitation-persistence)
  - [Lab Progression](#lab-progression)
- [Part 19: API Security](#part-19-api-security)
  - [Stage 1: API Reconnaissance & Mapping](#stage-1-api-reconnaissance-mapping)
  - [Stage 2: OWASP API Security Top 10](#stage-2-owasp-api-security-top-10)
  - [Stage 3: Protocol-Specific API Attacks](#stage-3-protocol-specific-api-attacks)
  - [Stage 4: API Authentication & Token Attacks](#stage-4-api-authentication-token-attacks)
  - [Stage 5: Defense & Hardening](#stage-5-defense-hardening)
  - [Lab Progression](#lab-progression)
- [Part 20: Bug Bounty and Penetration Testing](#part-20-bug-bounty-and-penetration-testing)
  - [Stage 1: Preparation & Scoping](#stage-1-preparation-scoping)
  - [Stage 2: Reconnaissance (The Wide Net)](#stage-2-reconnaissance-the-wide-net)
  - [Stage 3: Vulnerability Assessment (The Deep Dive)](#stage-3-vulnerability-assessment-the-deep-dive)
  - [Stage 4: Exploitation & Validation](#stage-4-exploitation-validation)
  - [Stage 5: Reporting & Triage](#stage-5-reporting-triage)
  - [Stage 6: Professional Development](#stage-6-professional-development)

---

## Part 17: Web Application Hacking

### **Stage 1: Reconnaissance & Mapping**

> [!TIP]
> **Goal:** : Understand the target application's structure and technologies.

- [ ] **OSINT & Discovery:** Perform **Reconnaissance** using **Google Dorks, Shodan, Certificate Transparency** to find subdomains, exposed admin panels, and developer info.

- [ ] **Service Enumeration:** Use `nmap -sV -sC` to identify web servers, versions, and common vulnerabilities.

- [ ] **Technology Fingerprinting:** Use **Wappalyzer, BuiltWith, WhatWeb** to identify frameworks, CMS, WAF, CDN, and backend technologies.

- [ ] **Content Discovery:** Run **Gobuster, ffuf, dirsearch** to find hidden directories, backup files, API endpoints, and admin panels.

- [ ] **Sitemap & Robots Analysis:** Parse **robots.txt, sitemap.xml, security.txt** for disallowed paths and contact info.

---

### **Stage 2: Vulnerability Analysis & Probing**

> [!TIP]
> **Goal:** : Find potential entry points and weaknesses.

- [ ] **Input Validation Testing:** Test every input field for **SQL Injection, NoSQL Injection, Command Injection, LDAP Injection**.

- [ ] **Path Manipulation:** Probe for **Directory/Path Traversal** using `../../../etc/passwd` and **LFI/RFI** vulnerabilities.

- [ ] **Logic Testing:** Analyze **authentication/authorization** mechanisms; test for **IDOR, broken access controls, privilege escalation**.

- [ ] **Protocol & Crypto Analysis:** Check **TLS configuration** with **sslyze/testssl.sh**; test for **weak ciphers, certificate issues, HTTPS downgrade**.

- [ ] **API Testing:** Enumerate **REST/GraphQL/SOAP** endpoints; test for **lack of rate limiting, exposed documentation, mass assignment**.

---

### **Stage 3: Exploitation (The OWASP Top 10)**

> [!TIP]
> **Goal:** : Prove the vulnerability and gain access.

- [ ] **Injection Attacks:** Execute **SQL injection** for data extraction; **command injection** for RCE; **LDAP/XPath** injection.

- [ ] **Cross-Site Scripting (XSS):** Deliver **reflected, stored, DOM-based** XSS to steal cookies, hijack sessions, or deface pages.

- [ ] **CSRF & Request Forgery:** Construct **CSRF attacks** to perform state-changing actions; test **SSRF** for internal network access.

- [ ] **Authentication Bypass:** Exploit **logic flaws, password reset**, **JWT manipulation, OAuth misconfigs** to gain unauthorized access.

- [ ] **File Upload Exploitation:** Bypass **filters** to upload **web shells** via **null bytes, double extensions, MIME confusion**.

- [ ] **Deserialization Attacks:** Exploit **unsafe deserialization** in Java/Python/PHP for RCE.

- [ ] **XXE & SSTI:** Parse **malicious XML** for file read; exploit **template engines** (Jinja2, Twig) for code execution.

---

### **Stage 4: Post-Exploitation & Persistence**

> [!TIP]
> **Goal:** : Maintain access and pivot deeper.

- [ ] **Web Shell Management:** Deploy **persistent web shells** (PHP, ASPX, JSP) in writable directories.

- [ ] **Database Enumeration:** Extract **credentials, PII, business data** via SQL injection or direct access.

- [ ] **Lateral Movement:** Use compromised web app to **pivot to internal network, access cloud metadata (IMDS), enumerate AWS/Azure resources**.

- [ ] **Data Exfiltration:** Exfil via **DNS, HTTPS covert channels, cloud storage APIs**.

---

### **Stage 5: Defense & Mitigation (The Shield)**

> [!TIP]
> **Goal:** : Prevent and detect these attacks.

- [ ] **WAF Deployment:** Implement **Web Application Firewall** (ModSecurity, CloudFlare WAF, AWS WAF) with custom rules.

- [ ] **Secure Coding:** Use **parameterized queries, input validation, output encoding, CSP headers** to prevent injections.

- [ ] **Strong Authentication:** Require **MFA/2FA, strong password policies, account lockout, CAPTCHA** after failed attempts.

- [ ] **Security Headers:** Implement **CSP, X-Frame-Options, HSTS, X-Content-Type-Options** to mitigate client-side attacks.

- [ ] **Continuous Monitoring:** Deploy **SIEM, web server logging, intrusion detection** to identify attack patterns.

---

### **Lab Progression**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Complete all OWASP Top 10 labs on PortSwigger Web Security Academy | Badge/completion screenshots |
| 2 | Exploit SQLi + XSS + SSRF on DVWA or OWASP Juice Shop | Attack chain documentation with request/response evidence |
| 3 | Perform an authenticated web app assessment on WebGoat (all modules) | Structured vulnerability report |
| 4 | Chain 3+ vulnerabilities for maximum impact on a single lab target (e.g., XSS→session theft→admin access→RCE) | Kill chain diagram + technical report |
| 5 | Write a custom Burp Suite extension or automated scanner script | Working extension/script + README |

> [!IMPORTANT]
> **Move-On Gate:** You can perform a complete web application assessment covering OWASP Top 10, chain vulnerabilities for maximum impact, use Burp Suite professionally, and produce a client-ready web app pentest report.

---

<a id="toc-part-18-web-server-hacking"></a>
## Part 18: Web Server Hacking

### **Stage 1: Target Acquisition & Reconnaissance**

> [!TIP]
> **Goal:** : Identify the target server and gather intelligence.

- [ ] **OSINT Gathering:** Conduct **Reconnaissance** using **WHOIS, DNS enumeration, Certificate Transparency** to identify IP ranges and domain information.

- [ ] **Network Mapping:** Determine the server's network position via **traceroute, OSINT**; identify if it's in **Perimeter, DMZ, or internal** segments.

- [ ] **Historical Analysis:** Use **Wayback Machine, Shodan history** to identify previous exposures and configuration changes.

---

### **Stage 2: Scanning & Service Enumeration**

> [!TIP]
> **Goal:** : Map out the server's attack surface.

- [ ] **Port Scanning:** Use `nmap -sS -sV -sC -p-` to discover **all open ports** and identify services (Apache, Nginx, IIS, Tomcat, SSH, FTP, DB).

- [ ] **Banner Grabbing:** Use **curl, nc, telnet** to grab service banners and identify **software versions, OS fingerprints**.

- [ ] **HTTP Method Enumeration:** Test for **PUT, DELETE, TRACE, OPTIONS** enabled; check **WebDAV** misconfiguration.

- [ ] **Protocol Audit:** Check for **insecure protocols (HTTP, FTP, Telnet)**; analyze **TLS** config with **testssl.sh** for weak ciphers.

- [ ] **Virtual Host Discovery:** Enumerate **vhosts** via **Host header manipulation, DNS brute-forcing** to find hidden services.

---

### **Stage 3: Vulnerability Assessment & Exploitation**

> [!TIP]
> **Goal:** : Find and exploit flaws to gain initial access.

- [ ] **Patch Audit:** Check for **outdated software versions** against CVE databases; test for **known exploits** (Apache Struts, IIS 6.0, etc.).

- [ ] **Web Application Attacks:** Attempt **SQL injection, XSS, file upload** against hosted applications to compromise the web server.

- [ ] **File System Attacks:** Test for **directory traversal** (`../../../etc/passwd`), **LFI/RFI**, **arbitrary file read**.

- [ ] **Service Exploitation:** Look for **buffer overflow, format string, RCE** exploits for specific service versions (Apache mod_ssl, ProFTPd, vsftpd).

- [ ] **Credential Attacks:** Launch **brute force, password spray, dictionary attacks** against **SSH, FTP, admin panels** with Hydra/Medusa.

- [ ] **Default Credentials:** Test **default admin passwords** for web servers (tomcat/tomcat, admin/admin) and management interfaces.

---

### **Stage 4: Post-Exploitation & Persistence**

> [!TIP]
> **Goal:** : Escalate privileges and maintain control.

- [ ] **Privilege Escalation:** After gaining low-privilege shell, use **kernel exploits, SUID binaries, sudo misconfigs, service misconfigurations** for root/SYSTEM.

- [ ] **Web Shell Deployment:** Upload **persistent web shells** (b374k, c99, webacoo) to writable web directories for backdoor access.

- [ ] **Living off the Land:** Use **LOLBAS/GTFOBins** for post-exploitation execution and persistence. 📌 _See Part 7 Stage 2 for full LOLBAS/GTFOBins coverage._

- [ ] **Credential Harvesting:** Dump **database credentials, config files** (`web.config`, `wp-config.php`), **SSH keys** for lateral movement.

- [ ] **Covering Tracks:** Clear **access logs, error logs, auth logs**; use **timestomping** to hide file modifications.

---

### **Lab Progression**

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
## Part 19: API Security

### **Stage 1: API Reconnaissance & Mapping**

> [!TIP]
> **Goal:** : Discover and map API attack surface.

- [ ] **API Discovery:** Find undocumented endpoints via **JS file analysis, Wayback Machine, Google Dorks (`site:target.com api`), Shodan**, and **Burp Suite passive crawling**.

- [ ] **Spec File Harvesting:** Locate exposed **OpenAPI/Swagger (`/swagger.json`, `/api-docs`), WSDL, GraphQL introspection** schemas that reveal all routes, parameters, and data models.

- [ ] **Endpoint Enumeration:** Fuzz **API paths and versions** (`/api/v1/`, `/api/v2/`, `/v3/`) using **ffuf, kiterunner, Arjun** with API-specific wordlists.

- [ ] **Technology Fingerprinting:** Identify **framework, auth scheme, rate limiting, versioning strategy** from headers, response patterns, and error messages.

---

### **Stage 2: OWASP API Security Top 10**

> [!TIP]
> **Goal:** : Methodically test each API-specific vulnerability class.

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

### **Stage 3: Protocol-Specific API Attacks**

> [!TIP]
> **Goal:** : Attack REST, GraphQL, gRPC, and SOAP distinctly.

- [ ] **REST API Testing:** Chain **BOLA + privilege escalation**, test **HTTP verb tampering**, exploit **mass assignment** via undocumented writable fields.

- [ ] **GraphQL Attacks:** Run **introspection queries** to dump full schema; exploit **batching/aliasing for DoS**, **nested query depth abuse**, **IDOR via node IDs**, and **mutations without auth checks**.

- [ ] **gRPC Security:** Use **grpcurl, Evans** to enumerate services; test for **missing auth interceptors, reflection enabled in prod, proto injection**.

- [ ] **SOAP/XML APIs:** Exploit **XXE via SOAP body**, test **WS-Security header bypass**, abuse **type confusion in XML parsing**.

---

### **Stage 4: API Authentication & Token Attacks**

> [!TIP]
> **Goal:** : Break API authentication mechanisms.

- [ ] **JWT Attacks:** Test **`alg:none` bypass, RS256→HS256 confusion, weak secret brute-force (hashcat mode 16500), kid injection, jku/x5u header injection** to forge arbitrary tokens.

- [ ] **OAuth 2.0 Attacks:** Exploit **CSRF on authorization endpoint, open redirect in redirect_uri, state parameter bypass, token leakage via Referer header**.

- [ ] **API Key Attacks:** Find **keys in JS bundles, git history, response headers, error messages**; test **key rotation absence, missing key scoping**.

- [ ] **mTLS Bypass:** Identify **endpoints that skip client certificate validation**, abuse **certificate pinning gaps**, exploit **proxy stripping of client certs**.

---

### **Stage 5: Defense & Hardening**

> [!TIP]
> **Goal:** : Know what defenders implement so you can test it properly.

- [ ] **API Gateway Controls:** Understand **rate limiting, quota enforcement, request validation, JWT verification, IP allowlisting** at the gateway layer.

- [ ] **Input Validation:** Test that **schema validation, type enforcement, max length, allowed values** are enforced server-side not just client-side.

- [ ] **Logging & Monitoring:** Verify **all API calls are logged** with enough context (user, IP, endpoint, response code) for anomaly detection.

---

### **Lab Progression**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Complete crAPI (completely ridiculous API) lab — all OWASP API Top 10 challenges | Challenge completion documentation |
| 2 | Test BOLA, broken auth, and mass assignment against vAPI or Juice Shop API | OWASP API assessment report |
| 3 | Exploit JWT algorithm confusion (`alg:none`, RS256→HS256) and forge tokens in a lab API | JWT attack PoC + writeup |
| 4 | Write automated API security tests using Postman collections or Burp macros | Test suite + results |
| 5 | Audit a GraphQL API (introspection dump, batching abuse, nested query DoS, IDOR via node IDs) | GraphQL security assessment report |

> [!IMPORTANT]
> **Move-On Gate:** You can discover undocumented API endpoints, test all OWASP API Top 10 categories, exploit JWT/OAuth flaws, attack REST/GraphQL/gRPC APIs, and produce a professional API security assessment report.

---

<a id="toc-part-20-bug-bounty-and-penetration-testing"></a>
## Part 20: Bug Bounty and Penetration Testing

### **Stage 1: Preparation & Scoping**

> [!TIP]
> **Goal:** : Stay legal and define the target.

- [ ] **Legal Check:** Read and sign the `Penetration Testing Rules of Engagement` or the Bug Bounty Policy (Safe Harbor).

- [ ] **Scope Validation:** Confirm IP ranges and domains. Ensure you are not attacking "Out of Scope" assets.

- [ ] **Framework Selection:** Decide if you are testing against `NIST`, `ISO`, or `OWASP10` standards.

---

### **Stage 2: Reconnaissance (The Wide Net)**

> [!TIP]
> **Goal:** : Find what others missed.

- [ ] **Subdomain Enumeration:** Use **OSINT** tools to find `dev`, `stage`, or `test` subdomains.

- [ ] **Port Scanning:** Run `nmap` to identify non-standard ports (e.g., 8080, 8443) and running services.

- [ ] **Tech Stack Analysis:** Use `curl` or browser extensions to identify the server, framework (React, Angular), and backend (PHP, Python).

---

### **Stage 3: Vulnerability Assessment (The Deep Dive)**

> [!TIP]
> **Goal:** : Find the flaw.

- [ ] **Input Fuzzing:** Test all input fields for `SQL Injection`, `XSS`, and `Buffer Overflow`.

- [ ] **Access Control:** Test for `IDOR` (Insecure Direct Object Reference) and verify `Authentication vs Authorization` logic.

- [ ] **Configuration Check:** Look for `Directory Traversal`, exposed `.git` folders, or default credentials (`admin/admin`).

---

### **Stage 4: Exploitation & Validation**

> [!TIP]
> **Goal:** : Prove the risk without breaking the system.

- [ ] **PoC Development:** Create a non-destructive Proof of Concept. (e.g., `alert(1)` for XSS, `whoami` for RCE).

- [ ] **False Positive Check:** Verify the finding is a `True Positive` before reporting.

- [ ] **Lateral Movement:** (Pentest only) Attempt `Privilege Escalation` or `Pass the Hash` if internal access is achieved.

---

### **Stage 5: Reporting & Triage**

> [!TIP]
> **Goal:** : Get paid and drive remediation.

- [ ] **Impact Assessment:** Clearly explain **business risk** (data breach, financial loss, compliance violation) to management.

- [ ] **Proof of Concept:** Provide **detailed steps, screenshots, videos, request/response** to reproduce the vulnerability.

- [ ] **Remediation Guidance:** Offer **specific technical fixes** (parameterized queries, input validation, patching) with code examples.

- [ ] **CVSS Scoring:** Calculate **CVSS score** to quantify severity and prioritize remediation.

---

### **Stage 6: Professional Development**

> [!TIP]
> **Goal:** : Build skills and reputation.

- [ ] **Platform Selection:** Focus on **HackerOne, Bugcrowd, Synack, Intigriti** platforms with active programs.

- [ ] **Specialization:** Develop expertise in **specific areas** (API security, mobile, cloud, blockchain).

- [ ] **Documentation:** Maintain **personal writeups, CVEs, Hall of Fame entries** for portfolio building.

- [ ] **Community Engagement:** Participate in **CTFs, conferences, Twitter/Discord security communities** for networking.

- [ ] **Continuous Learning:** Stay updated on **latest vulnerabilities, techniques, tools** through blogs, research papers, trainings.

---

<a id="toc-part-21-wireless-pentesting"></a>