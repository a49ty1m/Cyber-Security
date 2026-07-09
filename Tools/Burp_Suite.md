# 🕷️ Burp Suite: Complete Mastery Checklist

> **What is Burp Suite?** Burp Suite is the industry-standard web application security testing platform. It acts as an intercepting proxy between your browser and the target web application, allowing you to inspect, modify, and replay every HTTP/HTTPS request and response. It includes tools for scanning, fuzzing, brute-forcing, and encoding.
>
> **Why does it exist?** Web applications are the largest attack surface in modern IT. Browsers hide the HTTP mechanics from users. Burp Suite makes every HTTP request and response visible and modifiable, turning the browser into a security testing instrument.
>
> **When to use it:** Every web application penetration test, bug bounty engagement, API security assessment, and web-focused CTF. Burp Suite is THE tool for web application security.
>
> **When to avoid it:** Network-level scanning (use Nmap). Binary exploitation (use GDB/Ghidra). Infrastructure testing without web components. Automated large-scale scanning of thousands of hosts (use Nuclei or custom scripts).
>
> **What mastering Burp Suite unlocks:** The ability to test any web application for security vulnerabilities. Web application pentesting (OSCP, OSWE, eWPT). Bug bounty hunting. Understanding of web security at the HTTP level. Career opportunities in application security.

---

## 🧭 Navigation

- 📋 [Master Roadmap](../Roadmap/README.md)
- 🌐 [OWASP BWA Lab](../Lab/OWASP_Broken_WebApps/TASK_LIST.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & Proxy Setup | 6 | 3–4 hours |
| 2 | Core Tools (Proxy, Repeater, Intruder) | 9 | 6–8 hours |
| 3 | Intermediate (Scanner, Extensions, Macros) | 6 | 5–7 hours |
| 4 | Advanced (Automation, Collaborator, SSRF) | 5 | 5–7 hours |
| 5 | Tool Integration | 4 | 3–4 hours |
| 6 | Practical Labs | 5 | 8–12 hours |
| 7 | Methodology & Bug Bounty | 4 | 3–4 hours |
| 8 | Mastery Challenges | 4 | 6–10 hours |
| | **Total** | **43** | **~39–56 hours** |

**Prerequisites:** HTTP fundamentals (methods, headers, cookies, status codes). Basic understanding of web technologies (HTML, JavaScript, SQL). A browser configured with a proxy extension (FoxyProxy).

**Editions:** Community (free — no scanner, throttled Intruder), Professional ($449/year — full scanner, fast Intruder, Collaborator), Enterprise (automated CI/CD scanning). This checklist works with Community but notes where Pro is needed.

**Alternatives:** OWASP ZAP (free, open-source alternative), mitmproxy (CLI-based, Python-scriptable), Caido (modern Rust-based alternative), Fiddler (Windows-focused), Charles Proxy (macOS-focused).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Understand the Intercepting Proxy Concept

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand how Burp Suite sits between your browser and the target: Browser → Burp Proxy (port 8080) → Target Server. Every HTTP/HTTPS request passes through Burp, making it visible and modifiable. |
| **Skills Learned** | MITM proxy architecture, why proxies can see HTTPS (CA certificate installation), the difference between passive observation (HTTP History) and active interception (Intercept tab), why this is the foundation of web app testing. |
| **Practical Exercise** | Draw a diagram: Browser → Proxy (localhost:8080) → Internet → Target Server. Label where HTTPS is terminated and re-encrypted. Explain how this is technically a "man-in-the-middle" for analysis purposes. |
| **Expected Output** | Understanding that Burp is a controlled MITM. Explanation of why CA certificate installation is required for HTTPS. |
| **Common Mistakes** | Not understanding the proxy chain (browser → Burp → server). Thinking Burp "hacks" websites (it's a testing tool, not an exploit). Not realizing that without the CA cert, HTTPS sites show certificate errors. |

---

### Task 1.2 — Configure Browser Proxy & CA Certificate

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Configure your browser to route all traffic through Burp Suite's proxy listener. Install Burp's CA certificate so HTTPS interception works without errors. |
| **Skills Learned** | FoxyProxy extension setup, proxy toggle workflow, CA certificate installation in browser/OS certificate stores, verifying proxy connectivity. |
| **Practical Exercise** | Install FoxyProxy in Firefox/Chrome → add proxy: 127.0.0.1:8080 → activate. Navigate to `http://burpsuite` → download CA certificate → install in browser (Firefox: Settings → Certificates → Import → trust for websites). Verify: browse to any HTTPS site — no certificate warnings and requests appear in Burp's HTTP History. |
| **Expected Output** | All browser traffic flowing through Burp. HTTPS sites loading without certificate warnings. HTTP History showing captured requests. |
| **Common Mistakes** | Not installing the CA certificate (HTTPS sites error out or don't load). Setting the wrong proxy port (Burp defaults to 8080). Not using FoxyProxy (manual proxy settings are painful to toggle). Leaving the proxy enabled after closing Burp (no internet access). |

---

### Task 1.3 — Burp Interface Walkthrough

- [ ] **Completed** · ⭐ Beginner · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Navigate every major tab in Burp Suite: Dashboard, Target, Proxy (HTTP History, Intercept, WebSockets), Intruder, Repeater, Sequencer, Decoder, Comparer, Logger, Extender. |
| **Skills Learned** | UI fluency, understanding each tool's purpose, the workflow (Proxy captures → send to Repeater/Intruder for testing), where to find settings, project file management. |
| **Practical Exercise** | Open Burp → browse the OWASP BWA landing page → check HTTP History (Proxy tab). Right-click a request → Send to Repeater → Send to Intruder. Visit each tab and read the tool description. |
| **Expected Output** | Comfortable navigation of all tabs. Understanding of the Proxy → Repeater/Intruder workflow. |
| **Common Mistakes** | Only using the Proxy tab (Repeater and Intruder are where the real testing happens). Not exploring the Target → Site map (visual representation of the application). Not saving projects (Burp can save and restore your entire session — Pro only). |

---

### Task 1.4 — Scope Configuration

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Define the target scope in Burp to filter out irrelevant traffic. Only in-scope targets appear in your Site Map and are processed by the scanner. |
| **Skills Learned** | Scope management, why scope matters (legal and practical), including/excluding URLs, protocol-specific scope (HTTP vs HTTPS), keeping your project clean and focused. |
| **Practical Exercise** | Target → Scope Settings → Add → enter target URL (e.g., `http://192.168.1.100`). Enable "Use advanced scope control" for regex patterns. Proxy → Options → check "Only show in-scope items in HTTP history." |
| **Expected Output** | HTTP History showing only target traffic. Site map containing only in-scope application. |
| **Common Mistakes** | Not setting scope (your HTTP History fills with hundreds of requests to google.com, browser extensions, analytics, etc.). Setting scope too narrowly (missing subdomains or alternate ports). Not filtering HTTP History by scope (drowning in noise). |

---

### Task 1.5 — Project Management & Saving State

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Save and manage Burp Suite projects (Pro: full project files; Community: use project options for temporary state). Understand how to export and import specific items. |
| **Skills Learned** | Project file management, exporting specific requests/responses, saving scan results, organizing findings by engagement, resuming work across sessions. |
| **Practical Exercise** | Pro: Create a named project file on disk. Community: Export selected requests (right-click → Save items). Save Burp state: Project → Project options → Save → export configuration. |
| **Expected Output** | Saved project that can be resumed later. Exported request/response items for documentation. |
| **Common Mistakes** | Using temporary projects and losing all work when Burp closes (Community limitation). Not exporting important findings before closing. Not organizing separate projects for separate engagements. |

---

### Task 1.6 — Burp's Built-In Browser

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Burp's built-in Chromium browser (pre-configured with proxy settings and CA certificate). Understand when to use it vs your regular browser. |
| **Skills Learned** | Built-in browser usage, zero-configuration proxying, when it's convenient (quick testing) vs when your own browser is better (extensions, saved sessions, multiple profiles). |
| **Practical Exercise** | Proxy → Intercept → Open Browser. Browse the target. Verify requests appear in HTTP History without any proxy configuration. |
| **Expected Output** | Built-in browser working with automatic proxy configuration. |
| **Common Mistakes** | Not knowing this feature exists (saves time for quick testing). Relying only on the built-in browser (your regular browser has extensions, bookmarks, and persistent sessions). |

---

# PHASE 2: CORE TOOLS

---

### Task 2.1 — HTTP History: Passive Observation

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Use the HTTP History tab as your primary reconnaissance tool. Browse the application normally while Burp captures every request and response. Learn to filter, sort, search, and annotate entries. |
| **Skills Learned** | Passive traffic collection, request/response inspection, filtering by URL/method/status/MIME type, highlighting interesting requests, annotation (comments and color coding), identifying attack surface from captured traffic. |
| **Practical Exercise** | Browse the entire target application (every link, every form, every page). Review HTTP History. Filter: show only POST requests (these contain user input). Filter: show only 302 redirects (these reveal authentication flows). Highlight interesting requests with colors. |
| **Expected Output** | Complete HTTP History of the application with annotated interesting endpoints. Understanding of the application's authentication flow, form submissions, and API calls. |
| **Common Mistakes** | Intercepting everything (leave Intercept OFF for passive browsing — use HTTP History to review). Not using filters (hundreds of requests are unmanageable without filtering). Not annotating (you'll forget which request was interesting). |

---

### Task 2.2 — Intercept: Modifying Requests In-Flight

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Enable Intercept to pause HTTP requests between the browser and server. Modify parameters, headers, or body content before forwarding. This is how you bypass client-side validation and test server-side logic. |
| **Skills Learned** | Request interception workflow (Intercept ON → browse → request paused → modify → Forward), modifying parameters/headers/cookies in-flight, the critical concept that client-side controls are a UI feature not a security feature. |
| **Practical Exercise** | Enable Intercept → submit a form with a `maxlength="10"` field → intercept the request → change the value to 10000 characters → Forward → observe server response. Intercept a request with a hidden field (e.g., `price=9.99`) → change the value → Forward. |
| **Expected Output** | Modified requests accepted by the server (proving lack of server-side validation). Understanding that Intercept is for surgical modifications, not general browsing. |
| **Common Mistakes** | Leaving Intercept ON during normal browsing (every request pauses, pages never load — the #1 beginner confusion). Modifying the wrong request (Burp intercepts ALL requests, including images and CSS — use the "Drop" button or scope filtering). Not clicking "Forward" after modification (request hangs). |

---

### Task 2.3 — Repeater: The Testing Workbench

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Master Burp Repeater — the tool where you spend 70% of your testing time. Send a request to Repeater, modify it, send it, analyze the response, modify again, repeat. It's your experiment bench. |
| **Skills Learned** | Request/response side-by-side analysis, iterative modification, comparing responses to understand server behavior, identifying which parameters the server validates, using Repeater tabs to organize tests by vulnerability class. |
| **Practical Exercise** | Right-click a request in HTTP History → Send to Repeater. In Repeater: modify a parameter → click Send → analyze response. Create multiple Repeater tabs for different tests: rename them (SQLi, XSS, IDOR). Compare response lengths for true/false conditions. |
| **Expected Output** | Multiple Repeater tabs organized by test type. Understanding of how modifying parameters changes server behavior. At least one finding where the server accepted unexpected input. |
| **Common Mistakes** | Not using Repeater (testing in the browser is slower and less controlled). Not renaming Repeater tabs (you end up with 20 unnamed tabs). Not comparing response lengths (a different response length often indicates different behavior — key for blind injection). Not using "Send" repeatedly with small changes (iterative testing is the methodology). |

---

### Task 2.4 — Intruder: Automated Fuzzing

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 45 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Burp Intruder for automated parameter fuzzing, brute-force attacks, directory enumeration, and IDOR testing. Understand the four attack types and when to use each. |
| **Skills Learned** | Payload position marking, attack type selection (Sniper, Battering Ram, Pitchfork, Cluster Bomb), payload set configuration (wordlists, number ranges, custom lists), result analysis (response length, status code, grep extraction). |
| **Attack Types** | **Sniper:** One position, one payload set, tests each position independently. Use for single-parameter testing. **Battering Ram:** All positions, same payload simultaneously. Use when all parameters need the same value. **Pitchfork:** Multiple positions, one payload set per position, iterated in parallel (row 1 with row 1). Use for username:password pairs from a credential list. **Cluster Bomb:** All combinations of all payload sets. Use for brute-forcing (every username with every password). |
| **Practical Exercise** | Send a login request to Intruder → mark username and password as positions → choose Cluster Bomb → set username list and password list → Start → sort by response length to find successful logins. Then: send an IDOR request → mark the ID parameter → Sniper with a number range (1-100) → identify different responses. |
| **Expected Output** | Intruder results showing differentiated responses. Valid credentials discovered (different response length). IDOR resources discovered (different response content). |
| **Common Mistakes** | Using Cluster Bomb when Pitchfork is appropriate (Cluster Bomb tries ALL combinations — exponentially more requests). Not sorting by response length (the key differentiator in results). Community Edition Intruder is throttled to ~1 request/second (use Turbo Intruder extension or Ffuf for speed). Not using payload processing (URL-encoding, hashing, etc.). |

---

### Task 2.5 — Decoder: Encoding & Decoding

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Burp Decoder to encode, decode, and hash data. Essential for understanding tokens, cookies, parameters, and crafting payloads that bypass filters. |
| **Skills Learned** | URL encoding/decoding, Base64, HTML entities, hex, ASCII hex, gzip decompression, hashing (MD5, SHA-1, SHA-256), recognizing encoding types by visual pattern, "Smart decode" feature. |
| **Practical Exercise** | Decode a Base64 session cookie. URL-encode an XSS payload: `<script>alert(1)</script>`. Double-URL-encode for filter bypass. Hash a password to compare with a captured hash. Use "Smart Decode" on unknown encoded data. |
| **Expected Output** | Fluency in encoding/decoding common formats. Understanding that encoding is NOT encryption. A reference of visual patterns: Base64 (`=` padding), URL (`%XX`), HTML entities (`&#XX;`). |
| **Common Mistakes** | Confusing encoding with encryption (encoding is reversible without a key). Not using Smart Decode (it auto-detects the encoding). Not recognizing Base64 in the wild (cookies, tokens, JWT payloads). |

---

### Task 2.6 — Comparer: Spotting Differences

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Burp Comparer to identify exact differences between two requests or responses. Critical for understanding what changes between valid/invalid inputs, different users, or before/after modifications. |
| **Skills Learned** | Response diffing, identifying subtle differences (a single character, a different header, a missing field), word-level vs byte-level comparison, using Comparer to understand application behavior. |
| **Practical Exercise** | Send two login attempts to Comparer: one with a valid username (wrong password) and one with an invalid username. Compare the responses — find the exact difference that enables username enumeration. |
| **Expected Output** | Highlighted differences between responses. Evidence of username enumeration (different error message or response length). |
| **Common Mistakes** | Not using Comparer (manually reading two responses side-by-side is error-prone). Using word-level comparison when byte-level is needed (some differences are whitespace-only). Not right-clicking → "Send to Comparer" (it's two clicks from any request/response). |

---

### Task 2.7 — Sequencer: Token Randomness Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Burp Sequencer to analyze the randomness (entropy) of session tokens, CSRF tokens, or any other security-critical values. Weak randomness = predictable tokens = session hijacking. |
| **Skills Learned** | Token entropy analysis, FIPS statistical tests, what makes a token "sufficiently random," practical impact of weak randomness, how Sequencer collects and analyzes samples. |
| **Practical Exercise** | Send a login response (containing a Set-Cookie with a session ID) to Sequencer. Configure it to extract the session cookie value. Run live capture → collect 10,000+ tokens. Analyze: check the overall entropy score and individual test results. |
| **Expected Output** | Entropy analysis report showing whether tokens pass randomness tests. Understanding that tokens need >100 bits of effective entropy. Any tokens failing tests are a finding. |
| **Common Mistakes** | Not collecting enough samples (need thousands for statistically significant results). Analyzing the wrong token (make sure you're extracting just the token value, not the entire cookie header). Not understanding the results (look at the "Overall result" summary first). |

---

### Task 2.8 — Target Site Map & Discovery

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Burp's Site Map for visual application mapping. Understand how passive spidering (from browsing) and active spidering (crawler) build the map. Discover hidden endpoints, parameters, and attack surface. |
| **Skills Learned** | Application mapping, passive vs active spidering, discovering unlinked pages, identifying API endpoints from JavaScript, parameter discovery, form analysis. |
| **Practical Exercise** | Browse the target thoroughly → check Target → Site Map for the discovered structure. Right-click the target → Engagement tools → Find comments, Find scripts, Find references. Review discovered but not-yet-visited URLs (gray in the site map). |
| **Expected Output** | Complete site map showing the application structure. List of discovered parameters and forms. Hidden endpoints found through JavaScript analysis. |
| **Common Mistakes** | Not browsing the application thoroughly before testing (Burp only maps what it sees — automated crawling misses JavaScript-rendered content). Not checking "Engagement tools" (Find comments often reveals developer notes, debug flags, and internal URLs). |

---

### Task 2.9 — Logger & HTTP History Export

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Use the Logger tab for detailed request/response logging across all Burp tools. Export HTTP history and specific requests for documentation and reporting. |
| **Skills Learned** | Cross-tool logging, exporting requests as cURL commands, saving items as XML, copying requests for report evidence, building documentation as you test. |
| **Practical Exercise** | Enable Logger → perform some tests → review the unified log. Right-click a request → Copy as cURL command (for reproduction in reports). Right-click → Save selected items (for archival). |
| **Expected Output** | Logger entries showing requests from Proxy, Repeater, and Intruder in one view. Exported cURL commands for report reproduction. |
| **Common Mistakes** | Not enabling Logger (miss the cross-tool unified view). Not exporting evidence as you find it (reconstructing evidence after the fact is difficult). |

---

# PHASE 3: INTERMEDIATE TECHNIQUES

---

### Task 3.1 — Active Scanner (Pro Only)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Burp's active scanner to automatically test for vulnerabilities: SQL injection, XSS, command injection, path traversal, and more. Understand scan configurations, audit items, and false positive handling. |
| **Skills Learned** | Active scanning methodology, scan configuration (crawl and audit, audit only, specific insertion points), interpreting scan results (confidence levels, severity ratings), false positive identification, scan queue management. |
| **Practical Exercise** | Right-click a request → "Scan" (or "Do active scan" in older versions). Configure: Audit only (not crawl) → select specific insertion points → Start. Review results in Dashboard → Issue activity. Click each finding → examine the evidence (request/response with the payload highlighted). |
| **Expected Output** | Scanner findings with confidence and severity ratings. Manually verified findings (confirm each scanner result by reproducing in Repeater). |
| **Common Mistakes** | Trusting scanner results blindly (always verify manually — scanners produce false positives AND false negatives). Running a full crawl-and-audit without understanding the application first (may trigger destructive actions). Not understanding insertion points (the scanner needs to know WHERE to inject payloads). Community Edition doesn't include the scanner. |

---

### Task 3.2 — Session Handling Rules & Macros

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Configure session handling rules to maintain authenticated sessions during testing. Create macros that automatically re-authenticate when the session expires. Handle CSRF tokens that change on every request. |
| **Skills Learned** | Session management in Burp, macro creation (recorded sequences of requests), CSRF token extraction and injection, cookie jar management, why session handling is essential for authenticated testing. |
| **Practical Exercise** | Settings → Sessions → Session handling rules → Add. Create a macro that: (1) requests the login page, (2) extracts the CSRF token, (3) submits login credentials with the token, (4) updates the session cookie. Attach the rule to Repeater and Intruder tools. |
| **Expected Output** | Automated re-authentication when sessions expire. CSRF tokens automatically refreshed in Intruder attacks. Uninterrupted testing without manual re-login. |
| **Common Mistakes** | Not setting up session handling (tests fail silently when the session expires — responses show login pages instead of application pages). Not handling CSRF tokens (Intruder attacks fail because every request needs a fresh token). Overly complex macro chains when a simple cookie jar rule suffices. |

---

### Task 3.3 — Burp Extensions (BApp Store)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Install and configure essential Burp extensions from the BApp Store to extend functionality: authentication testing, content discovery, vulnerability detection, and workflow enhancement. |
| **Skills Learned** | Extension management, Jython/JRuby setup for Python/Ruby extensions, essential extension selection, extension configuration. |
| **Essential Extensions** | **Autorize** (automatic authorization testing — replays requests as a different user). **Logger++** (advanced logging with regex search). **Turbo Intruder** (Python-scripted Intruder at thousands of requests/sec). **Param Miner** (hidden parameter discovery). **Active Scan++** (additional scanner checks). **Retire.js** (JavaScript library vulnerability detection). **JSON Beautifier** (readable JSON responses). **Hackvertor** (encoding/decoding tags in requests). |
| **Expected Output** | Essential extensions installed and functional. Understanding of when to use each extension. |
| **Common Mistakes** | Installing too many extensions (slows Burp significantly). Not installing Jython (required for Python-based extensions). Not configuring Autorize correctly (it needs a low-privilege session cookie to compare against). |

---

### Task 3.4 — Turbo Intruder: High-Speed Fuzzing

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Turbo Intruder for high-speed automated testing. It's a Python-scriptable extension that bypasses Community Edition's Intruder throttling and enables thousands of requests per second. |
| **Skills Learned** | Turbo Intruder Python scripting, pipeline HTTP/2 support, race condition testing, large wordlist processing, callback-based result filtering. |
| **Practical Exercise** | Right-click a request → Extensions → Turbo Intruder → Send to Turbo Intruder. Modify the Python template to: load a wordlist, send requests in parallel, filter results by response code or length. |
| **Expected Output** | High-speed fuzzing results (thousands of requests in seconds). Filtered results showing only interesting responses. |
| **Common Mistakes** | Not modifying the Python template (the default may not match your needs). Setting concurrency too high (overwhelming the target or getting rate-limited). Not filtering results (thousands of responses are unreadable without filtering). |

---

### Task 3.5 — Match & Replace Rules

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Configure Proxy → Options → Match and Replace rules to automatically modify requests or responses passing through Burp. Use cases: remove security headers, inject custom headers, change User-Agent, disable CSP. |
| **Skills Learned** | Automatic request/response modification, removing defensive headers for testing (CSP, X-Frame-Options), injecting authorization headers, modifying cookies automatically, testing with different User-Agents. |
| **Practical Exercise** | Add a rule to remove `Content-Security-Policy` headers from responses (makes XSS testing easier). Add a rule to replace `User-Agent` with a mobile user agent (tests mobile-specific behavior). Add a rule to inject `X-Forwarded-For: 127.0.0.1` into requests (tests IP-based access controls). |
| **Expected Output** | Automatic modifications applied to all proxied traffic. CSP headers removed for XSS testing. Custom headers injected without manual modification. |
| **Common Mistakes** | Not removing CSP headers during testing (CSP blocks XSS payloads from executing — great for defense, but makes testing harder). Forgetting to disable rules after testing (modifications affect all traffic). Not using regex in match rules when needed (simple string matching may not catch all variations). |

---

### Task 3.6 — WebSocket Testing

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Intercept, view, and modify WebSocket messages in Burp. Many modern applications use WebSockets for real-time communication — these messages need testing too. |
| **Skills Learned** | WebSocket protocol in Burp, viewing WebSocket history (Proxy → WebSockets history), intercepting WS messages, sending WS messages to Repeater, testing for injection in WebSocket frames. |
| **Practical Exercise** | Browse a WebSocket-using application → check Proxy → WebSockets history. Intercept a WS message → modify it → forward. Send a WS message to Repeater → test for XSS or SQLi in WebSocket parameters. |
| **Expected Output** | WebSocket messages captured, modified, and replayed. Understanding that WebSocket testing follows the same methodology as HTTP testing. |
| **Common Mistakes** | Ignoring WebSocket traffic (modern apps use it for chat, notifications, real-time updates — it's all attack surface). Not realizing WebSockets bypass some traditional security controls (WAFs may not inspect WS frames). |

---

# PHASE 4: ADVANCED USAGE

---

### Task 4.1 — Burp Collaborator (Out-of-Band Testing)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Burp Collaborator for out-of-band (OOB) vulnerability detection: SSRF, blind XXE, blind SQLi via DNS, blind command injection, email header injection. |
| **Skills Learned** | Out-of-band testing concept (inject a Collaborator URL → if the server makes a request to it, the vulnerability is confirmed), Collaborator client usage, DNS vs HTTP vs SMTP interactions, using Collaborator payloads in injection tests. |
| **Practical Exercise** | Burp → Collaborator client → Copy to clipboard (get a unique Collaborator URL). Inject the URL into a parameter: `http://xxxx.burpcollaborator.net/`. If the server fetches it, the Collaborator client shows the DNS/HTTP interaction. Test SSRF: inject Collaborator URL in URL parameters. Test blind XXE: inject Collaborator URL in XML external entity. |
| **Expected Output** | Collaborator interactions received, confirming out-of-band vulnerability. Understanding that blind vulnerabilities (no visible response) can be confirmed through OOB channels. |
| **Common Mistakes** | Not using Collaborator for blind vulnerabilities (it's the only way to confirm many blind injection types). Community Edition has limited Collaborator access. Not checking Collaborator results after testing (interactions may arrive with a delay). |

---

### Task 4.2 — Autorize: Automated Authorization Testing

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Configure the Autorize extension to automatically test every request for authorization bypass: does the same request work with a lower-privileged session? Without any session? |
| **Skills Learned** | Horizontal and vertical privilege escalation testing at scale, automated IDOR detection, three-state comparison (admin request vs normal user vs unauthenticated), understanding authorization bypass as the most common web vulnerability class. |
| **Practical Exercise** | Install Autorize extension. Configure with a low-privilege user's session cookie. Browse the application as admin → Autorize automatically replays every request with the low-privilege cookie and with no cookie. Review results: green = properly enforced, red = authorization bypassed, orange = unclear. |
| **Expected Output** | Authorization bypass findings showing which admin endpoints are accessible to normal users. Color-coded results for every tested endpoint. |
| **Common Mistakes** | Not providing the correct low-privilege cookie (results are meaningless if the comparison cookie is wrong). Not understanding the three-column results (original, modified cookie, no cookie). Not manually verifying red results (some may be false positives). |

---

### Task 4.3 — Burp REST API & Automation

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use Burp's REST API (Pro) to automate scan initiation, result retrieval, and integration with CI/CD pipelines. |
| **Skills Learned** | Burp API endpoints, programmatic scan launching, scan status polling, result export, CI/CD integration, headless scanning. |
| **Practical Exercise** | Enable API: User options → Misc → REST API → Enable. Start scan via API: `curl -X POST http://127.0.0.1:1337/v0.1/scan -d '{"urls":["http://target"]}'`. Check status: `curl http://127.0.0.1:1337/v0.1/scan/<task_id>`. |
| **Expected Output** | Programmatic scan launch and result retrieval. Understanding of how Burp integrates into automated security pipelines. |
| **Common Mistakes** | Not enabling the API before trying to use it. Trying to use the API with Community Edition (Pro only). Not authenticating API requests (API key required in some configurations). |

---

### Task 4.4 — Custom Intruder Payloads & Processing

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Create custom payload lists and use payload processing rules: encoding, hashing, prefix/suffix addition, case modification, and payload generation for specific vulnerability classes. |
| **Skills Learned** | Custom wordlist creation for specific applications, payload processing chains (e.g., add prefix → Base64 encode → URL encode), using runtime file loading, character substitution for WAF bypass, generating payloads programmatically. |
| **Practical Exercise** | Create a custom SQLi payload list targeting specific database errors. Configure payload processing: URL-encode each payload → add a prefix. Create a number-range payload for IDOR testing with padding (001-999). |
| **Expected Output** | Custom payload lists targeting specific vulnerability classes. Payload processing chains producing correctly formatted payloads. |
| **Common Mistakes** | Using generic wordlists when application-specific payloads would be more effective. Not URL-encoding payloads (special characters break the request). Not using payload processing chains (manual encoding of hundreds of payloads is impractical). |

---

### Task 4.5 — Race Condition Testing

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Test for race conditions using Burp's "Send group in parallel" feature (or Turbo Intruder's race condition template). Race conditions occur when multiple requests processed simultaneously produce unintended behavior (double spending, bypassing rate limits, creating duplicate resources). |
| **Skills Learned** | Race condition theory (TOCTOU — Time of Check to Time of Use), parallel request sending, "last-byte sync" technique in Turbo Intruder, identifying race-condition-prone functionality (payments, voting, coupon redemption). |
| **Practical Exercise** | Select multiple identical requests in Repeater → right-click → "Send group in parallel (last-byte sync)." Or use Turbo Intruder's `race.py` template. Target: a coupon redemption endpoint, a balance transfer, or a vote button. |
| **Expected Output** | Multiple successful applications of a single-use action (proving the race condition). Documentation of the timing window. |
| **Common Mistakes** | Not using last-byte sync (requests need to arrive at the server simultaneously — regular parallel sending has too much jitter). Not targeting race-prone functionality (race conditions only matter for state-changing, one-time operations). |

---

# PHASE 5: TOOL INTEGRATION

---

### Task 5.1 — Nmap → Burp: Web Target Discovery Pipeline

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| **Workflow** | Nmap discovers web servers (`grep "80/open\|443/open" scan.gnmap`) → extract URLs → add to Burp's target scope → spider and scan. |

---

### Task 5.2 — Burp + SQLMap: SQL Injection Exploitation

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| **Workflow** | Identify SQLi in Burp Repeater → right-click → Copy as cURL → convert to SQLMap: `sqlmap -u "URL" --cookie "cookie" --data "POST-body" -p "parameter"`. Or: Save request to file → `sqlmap -r request.txt`. |

---

### Task 5.3 — Burp + Ffuf/Gobuster: Directory Discovery

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| **Workflow** | Use Burp for initial browsing and mapping → Ffuf for fast directory brute-forcing → import discovered URLs back into Burp for analysis. `ffuf -u http://target/FUZZ -w wordlist.txt -x http://127.0.0.1:8080` (proxies ffuf through Burp). |

---

### Task 5.4 — Burp + Wireshark: Protocol-Level Analysis

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| **Workflow** | Capture traffic in Wireshark while testing in Burp → compare what Burp shows (HTTP-level) with what Wireshark shows (packet-level) → understand the complete request lifecycle including DNS resolution, TCP handshake, TLS negotiation, and HTTP exchange. |

---

# PHASE 6: PRACTICAL LABS

---

### Lab 6.1 — Beginner: DVWA Full Walkthrough via Burp

- [ ] **Completed** · ⭐⭐ Beginner · ⏱️ 90 min

| **Scenario** | Use Burp Suite to test every DVWA module at Low security. Use Repeater for manual testing and document every finding. |
| **Success Criteria** | Each DVWA module tested through Burp (not just the browser). Findings documented with request/response evidence from Repeater. |

---

### Lab 6.2 — Intermediate: Authentication Bypass Testing

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 60 min

| **Scenario** | Test a BWA application for: default credentials (Intruder), username enumeration (response comparison), brute force (Intruder with wordlists), session fixation (cookie analysis), and weak session tokens (Sequencer). |
| **Success Criteria** | At least three authentication-related findings with evidence. |

---

### Lab 6.3 — Advanced: Full Web Application Assessment

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 120 min

| **Scenario** | Perform a complete web application assessment against WackoPicko or BodgeIt Store. Map the application, test all input points, chain vulnerabilities, and produce a findings summary. |
| **Success Criteria** | Application fully mapped in Site Map. At least 5 findings across different vulnerability classes. One vulnerability chain demonstrated. |

---

### Lab 6.4 — Advanced: Authorization Testing with Autorize

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Configure Autorize and test an application with multiple user roles. Identify all endpoints where authorization is missing or improperly enforced. |
| **Success Criteria** | Autorize configured with two different privilege levels. Authorization bypass findings documented. Remediation recommendations provided. |

---

### Lab 6.5 — Expert: Bug Bounty Simulation

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 180 min

| **Scenario** | Treat a BWA application as a bug bounty target. Map the attack surface, test systematically using Burp's full toolkit, and write a professional vulnerability report with reproduction steps. |
| **Success Criteria** | Professional report with: title, severity, description, reproduction steps (cURL commands), impact, remediation. At least 3 findings. |

---

# PHASE 7: METHODOLOGY & BUG BOUNTY

---

### Task 7.1 — Burp in the Web Application Testing Methodology

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| **Objective** | Map Burp Suite usage to the OWASP Testing Guide methodology: Configuration Management → Authentication → Session Management → Authorization → Input Validation → Error Handling → Cryptography → Business Logic. |

---

### Task 7.2 — Bug Bounty Workflow with Burp

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Objective** | Build a systematic bug bounty workflow: scope review → subdomain enumeration → Burp spider → manual crawling → automated scanning → manual testing → report writing. Understand Burp's role at each step. |

---

### Task 7.3 — Burp Suite Limitations

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Key Limitations** | Only tests HTTP/HTTPS (not binary protocols, network services, or OS-level vulns). Scanner misses logic vulnerabilities (requires human understanding). Community Edition lacks the scanner and has throttled Intruder. Cannot test mobile app backends without additional proxy configuration. Not designed for DDoS testing or high-volume performance testing. |

---

### Task 7.4 — Professional Report Writing from Burp Findings

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Objective** | Transform Burp findings into professional penetration test report format: finding title, CVSS score, description, affected URL/parameter, request/response evidence (from Repeater), business impact, and remediation recommendation with code examples. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Zero-to-Findings in 60 Minutes

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Choose a BWA application you haven't tested before. Set a 60-minute timer. Configure Burp, map the application, find as many vulnerabilities as possible, and document everything — all within the time limit. |

---

### Challenge 8.2 — Automated Pipeline Project

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 120 min

| **Scenario** | Build a web application security pipeline: Nmap discovers web ports → URLs fed to Burp via API → Burp scans → results exported → findings formatted into a markdown report. Automate the entire chain. |

---

### Challenge 8.3 — Write a Custom Burp Extension

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 180 min

| **Scenario** | Write a custom Burp extension in Python (Jython) that: monitors HTTP responses for sensitive data (API keys, credentials, PII), highlights matches in the UI, and generates a summary report. |

---

### Challenge 8.4 — Teach Burp Suite

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Prepare a 30-minute workshop: proxy setup, Repeater workflow, Intruder basics, one complete vulnerability discovery live demo. Deliver to a junior colleague or record as a video. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can configure proxy and intercept all browser traffic | ☐ |
| Can use Repeater for manual vulnerability testing | ☐ |
| Can configure and run Intruder attacks | ☐ |
| Can use Decoder for encoding/decoding operations | ☐ |
| Can analyze session token randomness with Sequencer | ☐ |
| Can set up session handling rules and macros | ☐ |
| Can install and configure essential extensions | ☐ |
| Can test for authorization bypass with Autorize | ☐ |
| Can use Collaborator for out-of-band testing | ☐ |
| Can produce professional reports from Burp findings | ☐ |
| Can automate testing workflows | ☐ |
| Can teach Burp Suite to another person | ☐ |

---

## 🎯 Interview Questions

1. What is the difference between Burp's Proxy, Repeater, and Intruder?
2. Explain the four Intruder attack types and when to use each.
3. How do you handle CSRF tokens in automated Intruder attacks?
4. What is Burp Collaborator and when do you use it?
5. How do you configure Burp for testing authenticated applications?
6. What are the key differences between Burp Community and Professional editions?
7. How would you test for authorization bypass at scale?
8. What extensions do you consider essential and why?
9. How do you integrate Burp with SQLMap?
10. What are Burp Suite's limitations and when would you use other tools?
