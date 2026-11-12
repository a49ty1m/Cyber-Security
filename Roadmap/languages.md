### Topic 7A: Programming & Scripting Fundamentals — 🔬 Practical
[[Topic-7A_Programming-and-Scripting-Fundamentals|📁]]

> [!TIP]
> **Goal (Stage 7A):** Build a strong programming foundation for cybersecurity by learning to automate tasks, understand software internals, interact with operating systems and networks, and create custom security tooling. This stage covers Python, Bash, PowerShell, and JavaScript — the four languages with immediate utility from Stage 1. **C and C++ are deferred to Stage 5 (Module 27)**, where binary analysis context makes them immediately applicable.
> **C & C++ programming lives in Stage 5 (Module 27) and Shelf 05.** Do not attempt C or C++ now. They require debugger experience and binary analysis context to learn meaningfully.

> [!NOTE]
> ⏱️ **Topic 7A Total Time: 3–5 weeks (daily) or 6–8 weeks (weekends-only)**
> Broken down by language:
> - **Python:** ~6 months total — 2 weeks fundamentals → 1 month beginner projects → 2–3 months intermediate → advanced by month 6
> - **JavaScript:** 1.5–2 weeks — Core JS + browser internals + security context (DOM XSS, CORS, JWT). Budget the upper end: the scope consistently runs longer than 1 week.
> - **Bash:** 1 week — Shell fundamentals + CLI tool mastery + automation scripts
> - **PowerShell:** 1 week — Language + Windows admin + AD automation + 2 projects
>
> Build foundation **competency**, not mastery. You need to be able to write scripts and read others’ code — not build production frameworks. Mastery comes during use in later stages.

---

#### Python (Automation, Networking & Security Scripting)
[[Module-01_Fundamentals/Topic-7A_Programming-and-Scripting-Fundamentals/PYTHON|📄]]

> [!NOTE]
> ⏱️ **Python Time Bracket: ~6 months total**
> **Phase 1 — Fundamentals (2 weeks):** Variables, loops, functions, lists, dictionaries, file handling, modules. Learn just enough to be dangerous — stop studying and start building immediately after.
> **Phase 2 — Beginner Projects (1 month):** Build 3 beginner projects. Each one teaches a specific skill cluster.
> **Phase 3 — Intermediate Projects (2–3 months):** Build projects that each open a new door and stop you feeling like a beginner.
> **Phase 4 — Advanced Projects (by month 6):** Build these not because you need them, but because building them forces you to understand exactly how they work.
> Milestone: Write a Python port scanner from scratch with banner grabbing — no tutorial, no copying.

> [!TIP]
> **Mindset:** Your first project is supposed to be terrible, messy, break, and crash — that is programming, not failure. Every good developer has a graveyard of terrible projects. Build, make mistakes, learn, and never stop building. You will never feel "ready" — the real skill is knowing how to figure things out, not memorizing syntax. Python rewards **action**, not perfection.
> 📚 Recommended books: *Python Crash Course* · *Automate the Boring Stuff with Python*

##### 1. Core Fundamentals
- [ ] **Core Language Fundamentals:** Master variables, data types, operators, strings, collections (lists, tuples, dictionaries, sets), control flow, loops, functions, modules, packages, decorators, generators, context managers, object-oriented programming (OOP), file handling, exception handling, virtual environments (venv), pip, and project structure.
- [ ] **Secure Coding Practices:** Learn input validation, error handling, logging, configuration management, secrets handling, dependency management, and code documentation.
- [ ] **Code Quality:** Understand debugging, profiling, testing (pytest), linting, formatting, and version control using Git.

##### 2. Project-Driven Learning

###### 🟢 Phase 2 — Beginner Projects (1 Month)

- [ ] **Project: Password Strength Checker**
  - **Prerequisites:** variables, strings, control flow *(from Core Fundamentals)*
  - **Topics to Learn:**
    - [ ] User input handling (`input()`)
    - [ ] Conditions, logic, and software decision-making
    - [ ] String analysis and strength scoring

- [ ] **Project: Port Scanner & Banner Grabber**
  - **Prerequisites:** functions, error handling *(from Core Fundamentals)*
  - **Topics to Learn:**
    - [ ] `socket` – TCP/UDP networking, client-server communication
    - [ ] Threading, multiprocessing, and `asyncio` – concurrent networking
    - [ ] Connection timeouts and banner grabbing logic

- [ ] **Project: Simple Website Scraper**
  - **Prerequisites:** file handling, loops *(from Core Fundamentals)*
  - **Topics to Learn:**
    - [ ] `requests` – HTTP requests and sessions
    - [ ] `BeautifulSoup (bs4)` – HTML parsing and web scraping
    - [ ] Storing scraped data to file; foundation for OSINT automation

- [ ] **Project: System Info & Geolocation Extractor**
  - **Prerequisites:** `requests` *(Port Scanner / Website Scraper)*
  - **Topics to Learn:**
    - [ ] `platform` – OS version and system info
    - [ ] `uuid`, `getmac` – MAC address and unique identifiers
    - [ ] System fingerprinting and footprinting basics

###### 🟡 Phase 3 — Intermediate Projects (2–3 Months)

- [ ] **Project: Subdomain Enumerator**
  - **Prerequisites:** threading/asyncio *(Port Scanner)*, `requests` *(Website Scraper)*
  - **Topics to Learn:**
    - [ ] `dnspython` – DNS enumeration and record analysis
    - [ ] Wordlist-based brute forcing and DNS resolution logic

- [ ] **Project: Log Analyzer & IOC Extractor**
  - **Prerequisites:** file handling *(Core Fundamentals)*
  - **Topics to Learn:**
    - [ ] `re` – Regular expressions for pattern matching
    - [ ] Stream processing large files line-by-line
    - [ ] `csv` – CSV file processing
    - [ ] `json` – JSON parsing and manipulation
    - [ ] `xml.etree.ElementTree / lxml` – XML parsing
    - [ ] `PyYAML` – YAML parsing and configuration handling

- [ ] **Project: API Automation Tool & Vulnerability Checker**
  - **Prerequisites:** `requests` *(Website Scraper)*, `json` *(Log Analyzer)*
  - **Topics to Learn:**
    - [ ] REST API authentication — headers, sessions, status verification
    - [ ] Input validation, secrets handling, and configuration management

- [ ] **Project: Packet Analyzer**
  - **Prerequisites:** `socket`, threading *(Port Scanner)*
  - **Topics to Learn:**
    - [ ] `scapy` – Packet crafting, sniffing, and network protocol analysis
    - [ ] `pyshark` – Packet capture (PCAP) analysis using Wireshark/TShark
    - [ ] Network protocol analysis and raw packet inspection

- [ ] **Project: Discord Bot**
  - **Prerequisites:** `asyncio` *(Port Scanner)*, API integration *(API Automation Tool)*
  - **Topics to Learn:**
    - [ ] `discord.py` – Bot creation, event handling, commands
    - [ ] Event-driven design and webhook usage

- [ ] **Project: Simple Malware Analysis Tool**
  - **Prerequisites:** `re` *(Log Analyzer)*, file I/O *(Core Fundamentals)*
  - **Topics to Learn:**
    - [ ] Binary file reading and string extraction from suspicious files
    - [ ] Identifying indicators of compromise (IOCs) in file contents

- [ ] **Project: Web Crawler & Directory Brute Forcer**
  - **Prerequisites:** `requests`, `BeautifulSoup` *(Website Scraper)*, threading *(Port Scanner)*
  - **Topics to Learn:**
    - [ ] `Selenium` – Browser automation and dynamic web app testing
    - [ ] `urllib.parse` – URL parsing and encoding/decoding
    - [ ] SSL/TLS basics and concurrent request handling for fuzzing

- [ ] **Project: Report Generator**
  - **Prerequisites:** `csv`, `json` *(Log Analyzer)*, file writing *(Core Fundamentals)*
  - **Topics to Learn:**
    - [ ] Structured data export formatting (CSV, JSON, formatted text)
    - [ ] Data processing pipeline design and logging

- [ ] **Project: Remote Automation & Secure Communication Tool**
  - **Prerequisites:** SSL/TLS basics *(Web Crawler)*
  - **Topics to Learn:**
    - [ ] `paramiko` – SSH automation, remote command execution, SFTP
    - [ ] `cryptography` – Encryption, hashing, digital signatures, certificates

- [ ] **Project: Educational Keylogger PoC**
  - **Prerequisites:** `getmac` *(System Info Extractor)*, `requests` *(Website Scraper)*
  - **Topics to Learn:**
    - [ ] `pynput` – Low-level keyboard and mouse input monitoring
    - [ ] `win32gui` – Active window detection (Windows)
    - [ ] `smtplib` – Email logs to self
    - [ ] ⚠️ *Ethical use only — test systems, always disclose*

- [ ] **Project: Browser Autofill Attack Simulation**
  - **Prerequisites:** HTML basics *(Web Crawler / general)*
  - **Topics to Learn:**
    - [ ] `Flask` – Local web server and routing
    - [ ] HTML form design and autofill behavior exploitation for security awareness

- [ ] **Project: Phishing Page PoC (Offline Awareness)**
  - **Prerequisites:** `Flask` *(Browser Autofill Simulation)*
  - **Topics to Learn:**
    - [ ] `Jinja2` – Templating for simulated credential capture pages
    - [ ] Static page cloning and local log capture
    - [ ] ⚠️ *Offline/local only — for security awareness training*

- [ ] **Project: Python .exe Binder with Image**
  - **Prerequisites:** `os`, file handling *(Core Fundamentals)*
  - **Topics to Learn:**
    - [ ] `pyinstaller` – Compile Python scripts to executables
    - [ ] `zipfile` – Archive manipulation and file bundling
    - [ ] Steganography simulation — hiding payloads in plain sight
    - [ ] ⚠️ *Ethical use only — steganography education, not exploitation*

###### 🔴 Phase 4 — Advanced Projects (By Month 6)

- [ ] **Project: Web Crawler (Advanced)**
  - **Prerequisites:** `requests`, `BeautifulSoup`, `Selenium`, `urllib.parse` *(Web Crawler & Directory Brute Forcer)*
- [ ] **Project: OSINT Framework**
  - **Prerequisites:** `requests`, `dnspython`, `BeautifulSoup`, `getmac` *(all earlier projects)*
- [ ] **Project: Network Monitoring Dashboard**
  - **Prerequisites:** `scapy`, `pyshark` *(Packet Analyzer)*, `Flask` *(Browser Autofill Simulation)*
- [ ] **Project: Phishing Detection Tool**
  - **Prerequisites:** `re`, `requests`, `BeautifulSoup` *(Log Analyzer, Website Scraper)*
- [ ] **Project: AI-Powered Security Assistant**
  - **Prerequisites:** `requests`, REST APIs *(API Automation Tool)*, `Flask` *(Browser Autofill Simulation)*
- [ ] **Project: Malware Sandbox**
  - **Prerequisites:** binary reading, IOC extraction *(Simple Malware Analysis Tool)*, `subprocess`
- [ ] **Project: Custom Vulnerability Scanner**
  - **Prerequisites:** `socket` *(Port Scanner)*, `requests` *(API Automation Tool)*, `dnspython` *(Subdomain Enumerator)*
- [ ] **Project: Packet Inspection Tool**
  - **Prerequisites:** `scapy`, `pyshark` *(Packet Analyzer)*

- [ ] **Project: Firewall Evasion Script (Outbound Tester)**
  - **Prerequisites:** `socket`, threading *(Port Scanner)*
  - **Topics to Learn:**
    - [ ] `subprocess` – Spawning system processes and reading output
    - [ ] Testing outbound connections across ports and understanding filter bypass

###### 🏆 Phase 5 — Portfolio & Hosting Projects

- [ ] **Project: Flask-Based Security Tools Dashboard**
  - **Prerequisites:** `Flask`, `Jinja2` *(Phishing Page PoC)*, all previous PoC tools
  - **Topics to Learn:**
    - [ ] Bootstrap – Frontend styling and responsive layout
    - [ ] Integrating multiple tools into a single locally-hosted GUI

- [ ] **Project: Personal Website for Tools & Reports**
  - **Prerequisites:** Markdown, HTML *(general/fundamentals)*
  - **Topics to Learn:**
    - [ ] GitHub Pages / Netlify – Static site hosting and deployment
    - [ ] Publishing tool docs, blog posts, and downloadable project ZIPs

- [ ] **Project: Markdown to Medium Sync Pipeline**
  - **Prerequisites:** Markdown *(general)*, HTML *(Web Crawler / Phishing PoC)*
  - **Topics to Learn:**
    - [ ] `markdown`, `html2text` – Convert between Markdown and HTML formats
    - [ ] GitHub Actions *(optional)* – Automate sync on push

- [ ] **Project: Email Notification Bot**
  - **Prerequisites:** `smtplib` *(Educational Keylogger PoC)*
  - **Topics to Learn:**
    - [ ] `email`, `ssl` – Structured email composition and secure sending
    - [ ] Pattern-based alerting from logs or input events

- [ ] **Project: Proof of Concept Index Page**
  - **Prerequisites:** HTML *(Browser Autofill Simulation)*, `markdown` *(Markdown Sync Pipeline)*
  - **Topics to Learn:**
    - [ ] Building a clickable HTML table of contents linking all PoC projects
    - [ ] Python Markdown-to-HTML generation for interview/client demos

##### 3. Advanced / Exploit Development
- [ ] **pwntools** _(learn later)_ – Binary exploitation, CTFs, exploit development, ROP, shellcode

- [ ] **Learning Outcome:** Be capable of writing professional automation scripts and custom security tools without relying entirely on third-party utilities.

---

#### JavaScript & Node.js (Web, Browser & API Security)
[[Module-01_Fundamentals/Topic-7A_Programming-and-Scripting-Fundamentals/JAVA_SCRIPT|📄]]

> [!NOTE]
> ⏱️ **JavaScript Time Bracket: 1.5–2 weeks**
> Day 1–2: Core language (closures, prototypes, async/await, event loop).
> Day 3–4: Browser internals — cookies, localStorage, fetch, XHR, WebSockets, Service Workers, DevTools.
> Day 5–6: Security context — DOM XSS, prototype pollution, CORS misconfiguration, CSP bypasses, JWT misuse. These items are not optional.
> Day 7–10: Node.js basics + build 2 automation projects (web crawler + JWT analyzer).
> Day 11–14: Review security context gaps, finish any incomplete automation projects, consolidate notes.
> Scope note: Do NOT try to master React/Angular/Vue frameworks now. Awareness-level only.

> [!NOTE]
> **JavaScript Scope in Stage 1:** The functional minimum for Stage 1 is: core language syntax, browser APIs, DOM basics, the fetch/axios communication layer, and the Security Context section (XSS, prototype pollution, CSRF, CORS misconfig). The Node.js/Express, Service Worker, SSE, and modern framework awareness content is intentionally brief and awareness-level — revisit it in Stage 3 with web application testing context where it becomes immediately applicable. Do not stall Stage 1 attempting to master React, Angular, or Express.js depth before moving forward.

- [ ] **Core JavaScript:** Master variables, data types, operators, scope, hoisting, closures, prototypes, prototype chain, objects, arrays, functions, asynchronous programming, callbacks, Promises, async/await, ES6+ features, modules, classes, the event loop, memory model, DOM manipulation, BOM, and browser APIs.

- [ ] **Node.js Fundamentals:** Learn npm, package management, Express.js, middleware, routing, filesystem APIs, child processes, streams, buffers, environment variables, authentication, session management, JWT handling, server-side JavaScript, and REST API development.

- [ ] **Browser Internals:** Understand:
  - [ ] Cookies (attributes: `HttpOnly`, `Secure`, `SameSite`) — _security reasoning for each attribute is covered in full in **Module 07 (Web Technology Fundamentals): Cookies, Sessions & Tokens**_
  - [ ] localStorage
  - [ ] sessionStorage
  - [ ] IndexedDB
  - [ ] Cache Storage API
  - [ ] Service Workers
  - [ ] Fetch API
  - [ ] XMLHttpRequest (XHR)
  - [ ] WebSockets
  - [ ] Server-Sent Events (SSE)
  - [ ] Cross-Origin Resource Sharing (CORS) _(canonical full treatment in Module 07 (Web Technology Fundamentals): Same-Origin Policy, CORS & Web Security Headers)_
  - [ ] Content Security Policy (CSP)
  - [ ] Same-Origin Policy (SOP)
  - [ ] postMessage API
  - [ ] Browser rendering pipeline
  - [ ] DevTools for debugging and network analysis

- [ ] **JavaScript Security APIs & Libraries:** Gain practical experience with:

  **🌐 HTTP & API Communication**
  - [ ] **fetch** – Modern HTTP requests
  - [ ] **axios** – API requests and interceptors
  - [ ] **WebSocket API** – Real-time communication
  - [ ] **EventSource (SSE)** – Server-Sent Events

  **🧩 DOM Manipulation**
  - [ ] **DOM API** – querySelector, events, element manipulation
  - [ ] **DOMParser** – HTML/XML parsing
  - [ ] **MutationObserver** – Detecting DOM changes

  **🔍 Parsing & Data Handling**
  - [ ] **JSON** – Serialization and parsing
  - [ ] **URL & URLSearchParams** – URL parsing and manipulation
  - [ ] **FormData** – Multipart form handling
  - [ ] **TextEncoder / TextDecoder** – Encoding and decoding

  **🔐 Security & Cryptography**
  - [ ] **Web Crypto API** – Hashing, encryption, key generation
  - [ ] **jsonwebtoken** – JWT creation and verification
  - [ ] **crypto (Node.js)** – Server-side cryptography

  **⚙️ Automation & Testing**
  - [ ] **Puppeteer** – Chrome automation
  - [ ] **Playwright** – Cross-browser automation
  - [ ] **jsdom** – DOM emulation for testing

- [ ] **Security Context:** Study:
  - [ ] DOM XSS
  - [ ] Reflected, Stored & DOM-based XSS
  - [ ] Prototype Pollution
  - [ ] Client-side Injection
  - [ ] Open Redirects
  - [ ] CSRF
  - [ ] CORS Misconfiguration
  - [ ] postMessage abuse
  - [ ] Clickjacking
  - [ ] JWT misuse
  - [ ] WebSocket security
  - [ ] CSP bypasses
  - [ ] Cookie security
  - [ ] LocalStorage & SessionStorage abuse
  - [ ] Service Worker abuse
  - [ ] Client-side request smuggling (awareness)

- [ ] **Automation Projects:** Build custom:
  - [ ] Web crawlers
  - [ ] API fuzzers
  - [ ] Endpoint enumerators
  - [ ] JavaScript endpoint extractors
  - [ ] Secret/API key finders
  - [ ] Link and route discovery tools
  - [ ] JWT analyzers
  - [ ] CORS testing tools
  - [ ] CSP analyzers
  - [ ] Browser automation scripts

- [ ] **Modern Framework Awareness:** Learn how React, Angular, Vue, Svelte, Next.js, Nuxt.js, and Electron influence modern attack surfaces without becoming a frontend developer.

- [ ] **AI Web Applications:** Understand how AI platforms such as ChatGPT, Claude, Gemini, Microsoft Copilot, and similar LLM applications operate as JavaScript frontends communicating with backend APIs, including streaming responses, authentication flows, and browser-based security considerations.

- [ ] **Code Quality:** Learn debugging with Chrome DevTools, Node.js Inspector, ESLint, Prettier, testing (Jest/Vitest), dependency auditing (npm audit), package security, and version control using Git.

- [ ] **Learning Outcome:** Confidently inspect, analyse, automate, and test modern JavaScript applications, SPAs, APIs, browser behaviour, and client-side security during professional web application penetration testing.

---

#### Bash (Linux Automation & Operations)
[[Module-01_Fundamentals/Topic-7A_Programming-and-Scripting-Fundamentals/BASH|📄]]

> [!NOTE]
> ⏱️ **Bash Time Bracket: 1 week**
> Day 1–2: Shell fundamentals — variables, quoting, loops, conditionals, functions, pipes, redirects.
> Day 3–4: CLI tool mastery — work through the File Processing, Filesystem, and Networking command lists. Run every command at least once in your lab.
> Day 5–6: Write 3 automation scripts: a host enumeration script, a log analyzer, and a network recon wrapper for Nmap.
> Day 7: Security automation — automate DNS enumeration, SSL cert inspection, and parsing recon results.
> Milestone: You should be able to write a working bash script from scratch for any listed automation use case without looking up basic syntax.

- [ ] **Shell Fundamentals:** Master variables, data types, quoting, command substitution, arithmetic operations, loops, conditionals, functions, arrays, pipes, redirection, file descriptors, environment variables, aliases, shell expansion, permissions, process management, exit codes, and shell scripting best practices.

- [ ] **Linux Command-Line Mastery:** Gain proficiency with:

  **📂 File & Text Processing**
  - [ ] grep
  - [ ] awk
  - [ ] sed
  - [ ] cut
  - [ ] tr
  - [ ] sort
  - [ ] uniq
  - [ ] xargs
  - [ ] tee
  - [ ] split
  - [ ] paste
  - [ ] wc
  - [ ] strings
  - [ ] file

  **📁 Filesystem Operations**
  - [ ] find
  - [ ] locate
  - [ ] ls
  - [ ] stat
  - [ ] chmod
  - [ ] chown
  - [ ] ln
  - [ ] tar
  - [ ] gzip
  - [ ] zip
  - [ ] rsync

  **🌐 Networking**
  - [ ] curl
  - [ ] wget
  - [ ] ssh
  - [ ] scp
  - [ ] nc (netcat)
  - [ ] socat
  - [ ] dig
  - [ ] host
  - [ ] nslookup
  - [ ] ping
  - [ ] traceroute
  - [ ] ss
  - [ ] netstat _(legacy awareness)_
  - [ ] tcpdump

  **⚙️ System Administration**
  - [ ] ps
  - [ ] top / htop
  - [ ] kill
  - [ ] systemctl
  - [ ] service
  - [ ] journalctl
  - [ ] crontab
  - [ ] env
  - [ ] export
  - [ ] history
  - [ ] sudo
  - [ ] tmux

  **📊 Data Processing**
  - [ ] jq (JSON)
  - [ ] yq (YAML)
  - [ ] base64
  - [ ] md5sum
  - [ ] sha256sum

- [ ] **Linux System Programming Basics:** Understand:
  - [ ] Processes
  - [ ] Background & foreground jobs
  - [ ] Signals
  - [ ] Environment variables
  - [ ] Permissions & ownership
  - [ ] File descriptors
  - [ ] Pipes & named pipes
  - [ ] Cron jobs
  - [ ] System logging
  - [ ] Package management
  - [ ] Bash startup files (.bashrc, .profile)

- [ ] **Automation Projects:** Build scripts for:
  - [ ] Host enumeration
  - [ ] Network reconnaissance
  - [ ] Subdomain enumeration
  - [ ] Log analysis
  - [ ] File processing
  - [ ] Backup automation
  - [ ] System monitoring
  - [ ] Cron job automation
  - [ ] SSH automation
  - [ ] Firewall management
  - [ ] Service monitoring
  - [ ] Package update automation
  - [ ] IOC extraction
  - [ ] Report generation

- [ ] **Security & Pentesting Automation:** Learn to automate:
  - [ ] Nmap scanning
  - [ ] HTTP requests using curl
  - [ ] DNS enumeration
  - [ ] SSL/TLS certificate inspection
  - [ ] Whois lookups
  - [ ] Log parsing
  - [ ] Directory brute-forcing workflows
  - [ ] Batch vulnerability scanning
  - [ ] Parsing reconnaissance results
  - [ ] Linux privilege enumeration

- [ ] **Debugging & Best Practices:** Learn:
  - [ ] ShellCheck
  - [ ] Bash debugging (`set -x`, `set -e`, `set -u`)
  - [ ] Error handling
  - [ ] Logging
  - [ ] Input validation
  - [ ] Portable shell scripting
  - [ ] Modular script design
  - [ ] Git for script version control

- [ ] **Learning Outcome:** Automate Linux administration, reconnaissance, enumeration, log processing, system operations, and penetration testing workflows efficiently using professional, reusable, and maintainable Bash scripts.

---

#### PowerShell (Windows Automation & Enterprise Administration)
[[Module-01_Fundamentals/Topic-7A_Programming-and-Scripting-Fundamentals/POWERSHELL|📄]]

> [!NOTE]
> ⏱️ **PowerShell Time Bracket: 1 week**
> Day 1–2: Language fundamentals — cmdlets, pipeline, objects vs text, error handling, execution policies.
> Day 3–4: Windows administration automation — process, service, event log, registry, scheduled tasks. Run every cmdlet group in a lab VM.
> Day 5–6: Active Directory module — enumerate users, groups, computers, GPOs, ACLs. Write an AD inventory script.
> Day 7: Enterprise automation — PowerShell Remoting (WinRM), Invoke-Command, remote event log collection.
> Milestone: Write a PowerShell script that: lists all local admins, finds stale AD accounts (no login > 90 days), and exports the result to CSV.

- [ ] **Language Fundamentals:** Master variables, data types, objects, pipelines, cmdlets, aliases, functions, modules, providers, scripting, execution policies, remoting, error handling, classes, background jobs, and PowerShell best practices.

- [ ] **PowerShell Core Concepts:** Understand:
  - [ ] Objects vs Text
  - [ ] Pipeline Processing
  - [ ] Get-Member
  - [ ] Select-Object
  - [ ] Where-Object
  - [ ] ForEach-Object
  - [ ] Sort-Object
  - [ ] Group-Object
  - [ ] Measure-Object
  - [ ] Out-File
  - [ ] Export-Csv
  - [ ] ConvertTo-Json / ConvertFrom-Json
  - [ ] XML Processing

- [ ] **Windows Administration:** Automate:
  - [ ] Active Directory enumeration
  - [ ] User & Group management
  - [ ] Registry operations
  - [ ] Service management
  - [ ] Process management
  - [ ] Event log collection
  - [ ] WMI queries
  - [ ] CIM
  - [ ] Scheduled Tasks
  - [ ] Windows Services
  - [ ] File & Directory management
  - [ ] SMB share management
  - [ ] Firewall configuration
  - [ ] Windows Defender management
  - [ ] Certificate management

- [ ] **Enterprise Automation:** Learn:
  - [ ] WinRM
  - [ ] PowerShell Remoting
  - [ ] Invoke-Command
  - [ ] Enter-PSSession
  - [ ] New-PSSession
  - [ ] CIM Sessions
  - [ ] Remote Event Log collection
  - [ ] Group Policy automation _(awareness)_
  - [ ] Desired State Configuration (DSC) _(awareness)_

- [ ] **Active Directory Automation:** Learn:
  - [ ] ActiveDirectory PowerShell Module
  - [ ] User enumeration
  - [ ] Group enumeration
  - [ ] Computer enumeration
  - [ ] OU management
  - [ ] GPO enumeration
  - [ ] ACL inspection
  - [ ] Trust enumeration
  - [ ] Domain information gathering

- [ ] **Essential Modules & APIs:** Gain practical experience with:
  - [ ] Microsoft.PowerShell.Management
  - [ ] Microsoft.PowerShell.Utility
  - [ ] ActiveDirectory Module
  - [ ] NetTCPIP
  - [ ] ScheduledTasks
  - [ ] CimCmdlets
  - [ ] PSReadLine
  - [ ] PowerShellGet

- [ ] **Automation Projects:** Build:
  - [ ] Active Directory inventory
  - [ ] User audit reports
  - [ ] Event log collector
  - [ ] Service monitoring scripts
  - [ ] Registry auditing tools
  - [ ] Windows asset inventory
  - [ ] Remote administration toolkit
  - [ ] File integrity checker
  - [ ] Windows health monitoring scripts
  - [ ] Enterprise reporting dashboards

- [ ] **Security & Defensive Automation:** Learn to automate:
  - [ ] Windows system enumeration
  - [ ] Active Directory auditing
  - [ ] Windows Defender status checks
  - [ ] Event log analysis
  - [ ] IOC hunting
  - [ ] Security baseline verification
  - [ ] Windows update auditing
  - [ ] Local administrator auditing
  - [ ] Scheduled Task auditing
  - [ ] Service permission auditing

- [ ] **Debugging & Best Practices:** Learn:
  - [ ] PowerShell ISE / VS Code
  - [ ] PowerShell Debugger
  - [ ] Error handling
  - [ ] Logging
  - [ ] Script signing
  - [ ] Secure credential handling
  - [ ] SecretManagement module _(awareness)_
  - [ ] PSScriptAnalyzer
  - [ ] Git for version control

- [ ] **Learning Outcome:** Confidently automate Windows administration, Active Directory management, enterprise enumeration, system auditing, incident response, and security operations using professional, reusable, and maintainable PowerShell scripts.

---

#### Cross-Platform Development

- [ ] Choose the appropriate language for each task:
  - [ ] Python → Automation, APIs, cross-platform tooling
  - [ ] Bash → Linux administration and automation
  - [ ] PowerShell → Windows administration and Active Directory
  - [ ] C → Low-level programming and exploit foundations
  - [ ] C++ → Reverse engineering and malware analysis
  - [ ] JavaScript → Web application and browser security

- [ ] **Additional Languages — Security Awareness:**

  **Java:** Java is the dominant language in enterprise backends (Spring Boot, Jakarta EE), Android development, and many legacy security tools (Burp Suite extensions, Metasploit auxiliary modules, OWASP tooling). Security relevance: **Java deserialization** (`ObjectInputStream.readObject()`) is one of the most exploited vulnerability classes — `ysoserial` generates gadget chains that achieve RCE by exploiting unsafe deserialization of attacker-controlled bytes. **SSRF** via `java.net.URL` fetches any URI including `file://`, `jar://`, `ftp://`. Know how Java class loading works (ClassLoader hierarchy, classpath, JAR files) — relevant for understanding exploitation and for writing Burp extensions. Tools: `jd-gui` (decompiler), `jadx` (Android RE). I do not need to master Java — I need to read it, understand deserialization gadget chains, and write basic Burp Suite extensions (`IBurpExtender` interface).

  **PHP:** PHP powers a significant portion of the web (WordPress, Drupal, Laravel, Magento, legacy custom apps). Security relevance: PHP's loose type comparison (`==` vs `===`) enables **type juggling** attacks — `"0e12345" == "0e67890"` evaluates to `true` because both are treated as scientific notation zero. **PHP deserialization** via `unserialize()` with magic methods (`__wakeup`, `__destruct`, `__toString`) enables RCE gadget chains. **File inclusion**: `include $_GET['page']` with no sanitisation → LFI/RFI. **`eval()` and `system()` injection**. Know how to read PHP source for these patterns during whitebox assessments and CTFs. Tools: `phpggc` (PHP deserialization gadget chain generator, equivalent of ysoserial for PHP).

- [ ] Learn to combine multiple languages into complete security workflows rather than treating each language in isolation.

---

### Stage Completion Criteria

Before moving to the next stage, I should be able to:

- [ ] Write custom automation tools from scratch.
- [ ] Read and modify existing security scripts.
- [ ] Debug programs in multiple languages.
- [ ] Interact directly with networks and operating systems using code.
- [ ] Build complete command-line utilities.
- [ ] Parse logs, APIs, packets, and structured data automatically.
- [ ] Select the most appropriate programming language for a given security task.
- [ ] Understand how programming knowledge supports penetration testing, malware analysis, reverse engineering, digital forensics, and detection engineering.

> **📌 Cross-Reference:** Offensive programming is covered in dedicated Parts:
> - **Module 27: Offensive Development & Tooling** (Stage 5) — Exploit prototyping with pwntools, custom C2 implant logic, buffer overflow exploits, shellcode writing, Win32 API process injection, DLL loading, token manipulation, .NET offensive tooling (P/Invoke, D/Invoke, SharpHound, Rubeus), AMSI/ETW bypass, in-memory execution, offensive PowerShell (download cradles, constrained language mode escape).
> - **Shelf 06: Modern Exploitation** — Advanced memory exploitation, kernel exploits, browser exploitation.
> - **Module 25: Malware & Weaponization** (Stage 4) — Document weaponization (VBA macros, DDE template abuse, OneNote/PDF weaponization), email client abuse, OAuth consent phishing, cloud persistence, data exfiltration, and covert channels.

---

### Topic 7B: C & C++ Programming ← Deferred to Stage 5 (Module 27) — 🔬 Practical
[[Topic-7B_C-and-Cpp_Deferred-to-Stage-5|📁]]

> [!IMPORTANT]
> **Do not start Stage 7B now.** This stage is placed here as a structural marker only. C and C++ are the languages of OS internals, exploit primitives, shellcode, and reverse engineering targets — but they require meaningful context to learn effectively:
> - I need to have seen a stack frame in a debugger before C memory layout makes sense.
> - I need to have read disassembly before C++ vtables mean anything.
> - I need to have written at least one exploit before custom shellcode has purpose.
> **Return here when reaching Stage 5, before starting Module 27 (Offensive Development) and Shelf 05 (Reverse Engineering).** At that point, C and C++ become immediately applicable rather than abstract theory.
> **Stage 5 location:** Stage-5_Specialized.md — C/C++ Foundation before Module 27.

_The full curriculum below is what I will complete when I return. Read it now for scope awareness, then close this section and proceed to Module 02._

---

#### C (Operating Systems & Memory Fundamentals)

- [ ] **Language Fundamentals:** Master variables, data types, operators, pointers, pointer arithmetic, arrays, strings, structs, unions, enums, typedefs, functions, recursion, bitwise operations, macros, preprocessing, header files, static vs dynamic variables, dynamic memory allocation, compilation, linking, and debugging.

- [ ] **Memory Management:** Understand:
  - [ ] Stack
  - [ ] Heap
  - [ ] Text Segment (.text)
  - [ ] Data Segment (.data)
  - [ ] BSS (.bss)
  - [ ] Memory Alignment
  - [ ] Padding
  - [ ] Stack Frames
  - [ ] Calling Conventions (cdecl, stdcall, fastcall, System V ABI)
  - [ ] Process Memory Layout
  - [ ] Buffer Boundaries
  - [ ] Memory Allocation (malloc, calloc, realloc, free)

- [ ] **System Programming:** Learn:
  - [ ] File descriptors
  - [ ] Processes
  - [ ] Threads (POSIX Threads)
  - [ ] Signals
  - [ ] Pipes
  - [ ] Named Pipes (FIFO)
  - [ ] TCP/UDP Sockets
  - [ ] Shared Memory
  - [ ] Semaphores
  - [ ] Message Queues
  - [ ] IPC mechanisms
  - [ ] fork()
  - [ ] exec() family
  - [ ] wait()/waitpid()
  - [ ] system() and execve()
  - [ ] Linux system calls
  - [ ] File permissions
  - [ ] Linux APIs (unistd, fcntl, syscalls)

- [ ] **Compiler & Binary Fundamentals:** Understand:
  - [ ] GCC
  - [ ] Clang
  - [ ] Makefiles
  - [ ] Static vs Dynamic Linking
  - [ ] Object Files (.o)
  - [ ] ELF Binary Format
  - [ ] Symbols
  - [ ] Libraries (.a / .so)
  - [ ] Compiler Optimisations
  - [ ] Debugging with GDB
  - [ ] objdump
  - [ ] readelf
  - [ ] nm
  - [ ] strings
  - [ ] ldd

- [ ] **Memory Exploitation Fundamentals:** Learn:
  - [ ] Buffer Overflows (Stack & Heap)
  - [ ] Integer Overflows
  - [ ] Format String Vulnerabilities
  - [ ] Use-After-Free (UAF)
  - [ ] Double Free
  - [ ] Heap Corruption
  - [ ] Null Pointer Dereference
  - [ ] Race Conditions
  - [ ] TOCTOU (Time-of-Check to Time-of-Use)
  - [ ] Off-by-One Errors
  - [ ] Stack Canaries
  - [ ] DEP / NX
  - [ ] ASLR
  - [ ] PIE
  - [ ] RELRO
  - [ ] Safe Memory Management Practices

- [ ] **Essential Tools:** Gain practical experience with:
  - [ ] GDB
  - [ ] GEF or pwndbg
  - [ ] Valgrind
  - [ ] AddressSanitizer (ASan)
  - [ ] objdump
  - [ ] readelf
  - [ ] strings
  - [ ] nm
  - [ ] ltrace
  - [ ] strace
  - [ ] checksec

- [ ] **Automation & Mini Projects:** Build:
  - [ ] TCP client/server
  - [ ] Simple shell
  - [ ] Mini HTTP server
  - [ ] File parser
  - [ ] Process monitor
  - [ ] Memory allocator (mini malloc)
  - [ ] ELF parser
  - [ ] Simple debugger
  - [ ] Binary file analyser

- [ ] **Learning Outcome:** Develop a deep understanding of C programming, Linux internals, process execution, memory management, binary structure, and how memory corruption vulnerabilities occur—forming the foundation for reverse engineering, exploit development, binary exploitation, and operating system security.

---

#### C++ (Reverse Engineering & Software Analysis)

- [ ] **Core Language:** Master classes, objects, inheritance, polymorphism, encapsulation, abstraction, constructors, destructors, namespaces, templates, the Standard Template Library (STL), operator overloading, exception handling, smart pointers, RAII, move semantics, object lifecycles, and modern C++ (C++11/14/17) features.

- [ ] **Object-Oriented Internals:** Understand:
  - [ ] Classes & Objects
  - [ ] Constructors
  - [ ] Destructors
  - [ ] Inheritance
  - [ ] Multiple Inheritance
  - [ ] Virtual Functions
  - [ ] Pure Virtual Functions
  - [ ] VTables
  - [ ] VPointers (vptr)
  - [ ] Runtime Type Information (RTTI)
  - [ ] Dynamic Casting
  - [ ] Object Memory Layout
  - [ ] Name Mangling
  - [ ] Template Expansion
  - [ ] Inline Functions

- [ ] **Compiler & Binary Fundamentals:** Learn:
  - [ ] C++ Compilation Process
  - [ ] Name Demangling
  - [ ] Symbol Tables
  - [ ] Static vs Dynamic Linking
  - [ ] ELF (Linux)
  - [ ] PE (Windows)
  - [ ] Shared Libraries (.so / DLL)
  - [ ] Import & Export Tables
  - [ ] Exception Handling Internals
  - [ ] Debug Symbols

- [ ] **Reverse Engineering:** Learn how C++ applications appear inside:
  - [ ] Ghidra
  - [ ] IDA Pro
  - [ ] Binary Ninja
  - [ ] Radare2 / Cutter
  - [ ] x64dbg
  - [ ] WinDbg
  - [ ] GDB

- [ ] **Reverse Engineering Concepts:** Study:
  - [ ] Function Identification
  - [ ] Class Reconstruction
  - [ ] VTable Recovery
  - [ ] RTTI Analysis
  - [ ] Object Reconstruction
  - [ ] Constructor & Destructor Identification
  - [ ] Virtual Function Resolution
  - [ ] Control Flow Graphs (CFG)
  - [ ] Cross References (XREFs)
  - [ ] Strings Analysis
  - [ ] Import/Export Analysis
  - [ ] Symbol Recovery
  - [ ] Manual Decompilation

- [ ] **Malware Analysis Context:** Understand how C++ is commonly used in:
  - [ ] Malware loaders
  - [ ] Packers
  - [ ] Ransomware
  - [ ] Trojans
  - [ ] Remote Access Trojans (RATs)
  - [ ] Command & Control (C2) clients
  - [ ] Windows API-heavy applications

- [ ] **Essential Libraries & APIs:** Gain familiarity with:
  - [ ] Standard Template Library (STL)
  - [ ] Windows API (Win32)
  - [ ] C Runtime Library (CRT)
  - [ ] Boost _(awareness)_
  - [ ] COM (Component Object Model) — understand COM as the Windows binary interface standard for inter-process communication and component reuse. Every COM object has a **CLSID** (Class ID, a GUID) registered in `HKCR\CLSID\`. Clients instantiate objects via `CoCreateInstance()`. COM objects run **in-process** (DLL loaded into caller), **out-of-process** (separate EXE via DCOM), or in a **surrogate process**. Security relevance for RE: COM is ubiquitous in Windows — shell extensions, Office automation, WMI providers, and security products all use COM. When reversing a Windows binary, COM call patterns (`QueryInterface`, `AddRef`, `Release`, vtable dispatch) are a key pattern to recognise. **COM hijacking** (a persistence/privilege escalation technique) works by placing a malicious DLL at a HKCU registry path that Windows searches before HKLM — no admin rights required; the malicious COM object loads whenever a privileged process instantiates the targeted CLSID. Detect via Procmon (`RegQueryValue` on CLSID paths returning `NAME NOT FOUND`) and Sysmon Event ID 7.

- [ ] **Practical Projects:**
  - [ ] PE parser
  - [ ] ELF parser
  - [ ] Mini disassembler
  - [ ] Binary string extractor
  - [ ] Symbol demangler
  - [ ] Windows API monitoring tool
  - [ ] Simple DLL loader
  - [ ] Basic binary patcher

- [ ] **Learning Outcome:** Read, analyse, reconstruct, and understand modern C++ binaries by recognising compiler-generated patterns, object-oriented structures, Windows/Linux APIs, and binary internals during malware analysis, reverse engineering, exploit research, and advanced penetration testing.

---

---
