# 💛 GoldenEye: Complete Reference

> **What is GoldenEye?** GoldenEye is a Python-based HTTP Layer 7 DoS testing tool. Unlike Slowloris (which holds connections open slowly), GoldenEye sends legitimate-looking but rapidly-generated HTTP GET/POST requests with randomized User-Agent headers, randomized referers, and cache-bypass parameters — flooding the web server with requests it must actually process. It aims to exhaust server CPU and memory by forcing real HTTP processing, not just connection slot exhaustion.
>
> **When to use it:** Lab environments for stress testing web servers. Understanding HTTP-level DoS attack patterns for defensive configuration. DDoS resilience testing where the threat model includes HTTP flood attacks. Understanding the difference between connection-level (Slowloris) and request-level (GoldenEye) DoS.
>
> **Tier 4 Reminder:** This is a conceptual and lab tool. Real HTTP flood attacks at scale require botnets — not single-machine tools. Understand the mechanism and the defenses.
>
> **Roadmap Phase:** Phase 10 (DoS Awareness — HTTP Layer 7 Flood Testing)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | How GoldenEye Works | 4 | 1–2 hours |
| 2 | Using GoldenEye | 3 | 1–2 hours |
| 3 | Defense | 3 | 1–2 hours |
| 4 | Comparison | 2 | 30 min |
| 5 | Mastery Check | 2 | 20 min |
| | **Total** | **14** | **~4–7 hours** |

---

# PHASE 1: HOW GOLDENEYE WORKS

---

### Task 1.1 — Attack Mechanism

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **What It Does** | Opens many concurrent HTTP/HTTPS connections (like a real browser would). Sends complete HTTP GET or POST requests — not partial like Slowloris. Randomizes User-Agent (browser spoofing), Referer, and Cache-Control headers. Appends random parameters to URLs to bypass caches (`?r=1234567`). Each request forces the web server to process a "real" request. |
| **Why This Works** | Server must: parse HTTP headers, route the request, query a database (for dynamic pages), render a response, and send it. At 500 requests/second from multiple threads, this exhausts CPU, memory, or database connections. |
| **vs. Slowloris** | Slowloris: exhausts connection slots. GoldenEye: exhausts processing capacity (CPU/RAM/DB). |

---

### Task 1.2 — Cache Bypass

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Problem with Cache** | CDNs and reverse proxies cache responses. An HTTP flood to a cached URL hits the cache, not the server — server is protected. |
| **GoldenEye Solution** | Appends random query parameters: `/?r=8472910`. Cache sees each URL as unique → cache miss → request forwarded to origin server → server must process each. Also sends: `Cache-Control: no-cache` and `Pragma: no-cache` headers to explicitly request uncached content. |

---

### Task 1.3 — Header Randomization

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **User-Agent** | Randomized from a list of real browser User-Agents. Each connection appears to come from a different browser. Evades simple User-Agent-based blocking. |
| **Referer** | Randomized HTTP Referer headers. |
| **Cookies** | Can include session-like cookies to bypass authentication-required pages (if a valid session cookie is provided). |
| **Accept** | Randomized Accept headers to further mimic real browsers. |

---

### Task 1.4 — Effectiveness Limits

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Single Machine Limit** | One machine generates ~a few thousand requests/second. Modern web servers handle tens of thousands. GoldenEye from a single host is effective against small/unprotected servers only. |
| **Real DDoS** | Requires a botnet — thousands of source IPs. GoldenEye is a proof-of-concept tool, not a real attack tool at scale. |
| **CDN/WAF** | Cloudflare, AWS WAF, etc. absorb HTTP floods trivially at their scale. |

---

# PHASE 2: USING GOLDENEYE

---

### Task 2.1 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Install** | `git clone https://github.com/jseidl/GoldenEye; cd GoldenEye; pip3 install -r requirements.txt`. |
| **Run** | `python3 goldeneye.py http://target.com`. |

---

### Task 2.2 — Basic Usage (Lab Only)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

> [!CAUTION]
> Lab only. Never use against systems you don't own.

| Field | Detail |
|:---|:---|
| **Basic** | `python3 goldeneye.py http://192.168.1.10`. Defaults: 500 workers, GET method. |
| **Workers** | `-w 200` — 200 concurrent connections (lower for slow networks). Default 500 may overwhelm your own network. |
| **Method** | `-m GET` or `-m POST`. POST is more resource-intensive for the server (body parsing). |
| **sockets** | `-s 50` — sockets per worker. |
| **Randomize** | `-n` — randomize User-Agent per connection. `-d` — debug output. |

---

### Task 2.3 — Measuring Impact

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Server Monitoring** | On target: `top` or `htop` — watch CPU usage. `vmstat 1` — watch memory. Apache: `apache2ctl status` — active workers. `tail -f /var/log/apache2/access.log` — incoming requests per second. |
| **Response Time** | From a third machine: `curl -o /dev/null -s -w "%{time_total}\n" http://target.com` — measure response time during attack. |
| **Threshold** | Note at what worker count CPU hits 90%+ or response time exceeds 5 seconds. Document as the server's effective request capacity. |

---

# PHASE 3: DEFENSE

---

### Task 3.1 — Rate Limiting

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Nginx Rate Limit** | `limit_req_zone $binary_remote_addr zone=one:10m rate=10r/s; limit_req zone=one burst=20 nodelay;`. Limits each IP to 10 requests/second. GoldenEye from one IP = blocked after 10 req/s. |
| **ModSecurity (Apache)** | WAF rules to detect and block HTTP flood patterns. |
| **iptables** | `iptables -A INPUT -p tcp --dport 80 -m limit --limit 25/minute --limit-burst 100 -j ACCEPT`. |

---

### Task 3.2 — WAF and CDN

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **CDN Caching** | Serve static content from CDN cache — GoldenEye's random params bypass client-side caching but CDN's own cache logic may still serve cached responses. |
| **WAF Challenge** | Cloudflare and AWS WAF present browser challenges (JavaScript, CAPTCHA) to suspected bots. GoldenEye doesn't execute JavaScript → fails challenge → blocked. |
| **Bot Detection** | Behavioral analysis: too many requests too fast from one IP, no normal browser activity pattern → block. |

---

### Task 3.3 — CAPTCHA for Dynamic Content

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Protected Pages** | High-cost dynamic pages (search, product listing, complex forms) → protect with CAPTCHA or JS challenge. Bots can't solve → never reach expensive server-side processing. |
| **Login Protection** | Rate limit + CAPTCHA on login endpoints — critical DoS targets for account lockout and credential stuffing. |

---

# PHASE 4: COMPARISON

---

### Task 4.1 — GoldenEye vs. Other DoS Tools

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **hping3** | Layer 3/4. SYN flood. High packet rate required. Targets connection table. |
| **Slowloris** | Layer 7. Holds connections open, never completing requests. Targets connection slots. Low bandwidth. |
| **GoldenEye** | Layer 7. Sends complete requests very fast. Targets processing capacity (CPU/DB). More bandwidth required than Slowloris. |
| **ApacheBench/wrk** | Performance testing tools, not DoS tools. Show throughput capacity. Can be misused for DoS but that's not their purpose. |

---

### Task 4.2 — When Each Fails

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **GoldenEye Fails When** | CDN absorbs requests at edge. Per-IP rate limiting is active. WAF bot detection is active. Server has abundant CPU/memory capacity (enterprise hardware). |
| **Slowloris Fails When** | Nginx (event-driven) is the target. Short timeout windows are configured. Connection limits per IP are in place. |

---

# PHASE 5: MASTERY CHECK

---

### Task 5.1 — Competency Self-Assessment

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Competency | Self-Assessment |
|:---|:---:|
| Can explain how GoldenEye differs from Slowloris | ☐ |
| Understands why cache bypass via random query parameters matters | ☐ |
| Can run a basic GoldenEye test in a lab | ☐ |
| Can apply Nginx rate limiting to defend against HTTP floods | ☐ |
| Understands the effectiveness limits of single-machine HTTP flood tools | ☐ |
| Knows why CDN/WAF protection defeats GoldenEye-style attacks | ☐ |

---

### Task 5.2 — Interview Questions

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

1. How does GoldenEye differ from Slowloris as a DoS tool?
2. Why does GoldenEye add random parameters to URLs?
3. What server resources does a GoldenEye attack exhaust?
4. How does a CDN protect against HTTP flood attacks?
5. What is the limitation of single-machine HTTP flood tools like GoldenEye?
6. How does Nginx rate limiting defend against HTTP floods?
