# 🦥 Slowloris: Complete Reference

> **What is Slowloris?** Slowloris is a Layer 7 (application-layer) HTTP DoS tool that attacks web servers by holding many concurrent connections open as long as possible — sending HTTP headers just often enough to prevent the connection from timing out, but never completing the request. It consumes the server's connection pool with minimal bandwidth, causing legitimate requests to be dropped because the server has no connections left to serve them.
>
> **Why it's significant:** Slowloris demonstrated that a DoS attack doesn't require massive bandwidth — a single machine on a slow connection can take down a web server if that server is configured to wait indefinitely for incomplete requests. It exploits server design decisions, not a vulnerability in the traditional sense.
>
> **When to use it:** Lab environments to test server resilience to slow-client DoS. Understanding defensive countermeasures (timeouts, mod_reqtimeout, nginx configuration). Security architecture testing where DoS resilience is in scope.
>
> **Tier 4 Reminder:** Understand the attack mechanism, how servers are affected, and what defenses work against it.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | How Slowloris Works | 4 | 1–2 hours |
| 2 | Using Slowloris | 4 | 1–2 hours |
| 3 | Defense | 3 | 1–2 hours |
| 4 | Comparison | 2 | 30 min |
| 5 | Mastery Check | 2 | 20 min |
| | **Total** | **15** | **~4–7 hours** |

---

# PHASE 1: HOW SLOWLORIS WORKS

---

### Task 1.1 — The Attack Mechanism

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Normal HTTP** | Client connects → sends complete HTTP request headers → server processes → responds → connection closed or reused. |
| **Slowloris** | Client connects → sends partial HTTP headers → waits → sends one more header every ~15 seconds → never sends the terminating `\r\n\r\n`. Server waits for the request to complete. Multiplied across hundreds of connections = connection pool exhausted. |
| **Impact** | Server's `MaxConnections` (Apache: ~150 default) fills with Slowloris connections. New legitimate requests → "503 Service Unavailable" or "Connection refused". The server itself is fine — only its connection handling capacity is consumed. |
| **Bandwidth** | Requires almost zero bandwidth — just keeping connections alive with occasional bytes. One low-end machine can take down a vulnerable Apache server. |

---

### Task 1.2 — Affected vs. Non-Affected Servers

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Vulnerable** | Apache 1.x and 2.x (by default). dhttpd. GoAhead. Many other thread-per-connection servers. |
| **Resistant** | Nginx (event-driven, non-blocking I/O — incomplete requests don't block worker threads). IIS (configurable request timeouts). lighttpd. Servers with good request timeout configuration. Load balancers (terminate incomplete connections quickly). |
| **Why Nginx Resists** | Nginx uses asynchronous event-driven architecture. Incomplete connections are held in a queue without consuming a thread. The worker threads only engage when data is ready. Slowloris fills the queue but doesn't block thread capacity. |

---

### Task 1.3 — Anatomy of the Slowloris Headers

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Initial Request** | `GET / HTTP/1.1\r\nHost: target.com\r\nUser-Agent: ...\r\n`. (No terminating `\r\n\r\n` — request never completes.) |
| **Keep-Alive Headers** | Every ~15 seconds: `X-a: b\r\n` — sends a meaningless header to prevent the server's incomplete request timeout from firing. |
| **Loop** | This continues until the connection is closed by the server or the attack stops. |

---

### Task 1.4 — Historical Context

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Origin** | Created by RSnake (Robert Hansen) in 2009. Demonstrated that low-bandwidth attacks could be as devastating as high-bandwidth ones. Named after the slow loris animal (which moves very slowly). |
| **Impact** | Caused Apache to add `mod_reqtimeout`. Led to wider adoption of Nginx and event-driven architectures. Changed how server connection handling is designed. |

---

# PHASE 2: USING SLOWLORIS

---

### Task 2.1 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Python** | `pip install slowloris`. `slowloris target.com`. |
| **Original Perl** | `github.com/llaera/slowloris.pl`. |
| **CLI** | `slowloris target.com -p 80 -s 150 --sleeptime 15`. |

---

### Task 2.2 — Basic Attack (Lab Only)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

> [!CAUTION]
> Lab only. Only test against servers you own or have explicit written authorization for.

| Field | Detail |
|:---|:---|
| **Command** | `slowloris 192.168.1.10 -p 80 -s 200 --sleeptime 15`. |
| **Options** | `-p 80` — target port. `-s 200` — number of sockets (connections). `--sleeptime 15` — seconds between keep-alive header sends. `-v` — verbose (shows connection count). |
| **Observe** | Monitor the target: `ss -tn | grep :80 | wc -l` — count connections. Once the connection count hits server max, try browsing to the server — you should get connection refused or timeout. |

---

### Task 2.3 — HTTPS Mode

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `slowloris target.com -p 443 --ssl`. |
| **Note** | TLS handshake still completes — the incomplete HTTP request comes after the TLS layer. Same mechanism, but over encrypted transport. SSL termination at a load balancer may cut the connection before it reaches the web server. |

---

### Task 2.4 — Measuring Resilience

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Determine at what socket count the server becomes unresponsive. |
| **Method** | Start: `slowloris target -s 50`. Verify server still responds. Increase: `slowloris target -s 100`. Increase: `slowloris target -s 200`. Stop when server becomes unresponsive. Document: threshold socket count = server's practical connection limit. |
| **Mitigation Test** | Apply `mod_reqtimeout` on Apache → retest. Does the mitigation raise the threshold or eliminate the attack? |

---

# PHASE 3: DEFENSE

---

### Task 3.1 — Apache Mitigation

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **mod_reqtimeout** | `a2enmod reqtimeout`. Config: `RequestReadTimeout header=20-40,MinRate=500 body=20,MinRate=500`. Forces server to close connections that don't send headers fast enough. |
| **mod_limitipconn** | Limit connections per IP: `MaxConnPerIP 5`. |
| **MaxRequestWorkers** | Increase Apache's worker count (buys time but doesn't fix the root problem). |

---

### Task 3.2 — Network/Firewall Mitigation

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Rate Limiting** | `iptables -A INPUT -p tcp --dport 80 -m connlimit --connlimit-above 20 -j REJECT`. Limit connections per source IP. |
| **Load Balancer** | Put Nginx or HAProxy in front of Apache. Nginx handles connection management; Apache only sees complete requests. Nginx's event model absorbs slow connections without blocking Apache workers. |
| **CDN/WAF** | Cloudflare, AWS CloudFront — terminate connections at the edge, which has massive connection capacity and sophisticated DDoS mitigations. |

---

### Task 3.3 — Detection

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Indicators** | Many connections from the same IP(s) in ESTABLISHED state with no data transfer. `netstat -nt | grep :80 | awk '{print $5}' | cut -d: -f1 | sort | uniq -c | sort -rn`. High connection count from single IP → likely Slowloris. Server access log: many partial requests (requests logged with "408 Request Timeout" or no response logged). |

---

# PHASE 4: COMPARISON

---

### Task 4.1 — Slowloris vs. Other DoS

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **SYN Flood (hping3)** | Layer 3/4. Targets TCP connection table. Requires high packet rate. Defenses: SYN cookies. |
| **HTTP Flood (GoldenEye)** | Layer 7. Sends many complete HTTP requests very fast. Requires more bandwidth than Slowloris. |
| **Slowloris** | Layer 7. Holds connections open, never completing them. Very low bandwidth. Targets connection pool, not bandwidth. |
| **Key Insight** | Slowloris is devastating against thread-per-connection servers with large timeout windows. Modern event-driven servers (Nginx) are immune. |

---

### Task 4.2 — When Slowloris Fails

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Nginx Target** | Slowloris has negligible impact. Nginx holds queued connections without blocking threads. |
| **Short Timeouts** | If the server closes incomplete connections within seconds, Slowloris can't hold them open long enough. |
| **Rate Limiting** | Firewall blocks after N connections from source IP. |
| **CDN/WAF** | CDN absorbs connections before they reach the origin server. |

---

# PHASE 5: MASTERY CHECK

---

### Task 5.1 — Competency Self-Assessment

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Competency | Self-Assessment |
|:---|:---:|
| Can explain how Slowloris works mechanically | ☐ |
| Knows which server architectures are vulnerable and which are resistant | ☐ |
| Can run a Slowloris test in a lab environment | ☐ |
| Can apply Apache mitigations and verify they work | ☐ |
| Can detect Slowloris attacks from connection counts | ☐ |
| Knows the difference between Slowloris, SYN flood, and HTTP flood | ☐ |

---

### Task 5.2 — Interview Questions

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

1. How does Slowloris work and why does it require very little bandwidth?
2. Why is Apache vulnerable to Slowloris but Nginx is largely resistant?
3. What is `mod_reqtimeout` and how does it mitigate Slowloris?
4. How do you detect a Slowloris attack from server-side?
5. How does placing Nginx as a reverse proxy in front of Apache protect against Slowloris?
6. What is the difference between a Layer 3/4 DoS and a Layer 7 DoS?
