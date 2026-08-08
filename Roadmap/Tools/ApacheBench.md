# ⚖️ ApacheBench (ab): Complete Reference

> **What is ApacheBench?** ApacheBench (`ab`) is a command-line HTTP benchmarking tool bundled with the Apache web server. It sends a specified number of HTTP requests to a URL — with a configurable concurrency level — and reports throughput metrics: requests per second, mean request time, time per request, transfer rate, and a full request time distribution. It tells you how fast a server can handle HTTP load under controlled conditions.
>
> **When to use it:** Quickly measuring a web server's baseline throughput. Comparing performance before and after configuration changes. Understanding how concurrency affects server response time. Simple load tests for small servers or APIs. When you need HTTP benchmarking results without setting up wrk or JMeter.
>
> **Tier 4 Reminder:** ab is the simplest HTTP benchmarking tool — great for quick capacity checks. For serious load testing, use wrk. Understand what the output numbers mean.
>
> **Roadmap Phase:** Phase 10 (DoS Awareness and HTTP Load Testing)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 3 | 45 min |
| 2 | Core Usage | 4 | 1–2 hours |
| 3 | Interpreting Output | 4 | 1–2 hours |
| 4 | Limitations & Alternatives | 3 | 45 min |
| 5 | Mastery Check | 2 | 20 min |
| | **Total** | **16** | **~4–6 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — What ab Does

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Mechanism** | Sends N total requests with C concurrent connections. Measures: total time, requests/second, time per request (mean and across concurrency), min/max/median response time, response size. |
| **Single URL** | ab tests only one URL per run. It does not simulate a real browsing session (no JS, no CSS fetching, no redirect following by default). |
| **Use Case** | "How many requests/second can this API endpoint handle?" "What response time should I expect under 50 concurrent users?" |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 5 min

| Field | Detail |
|:---|:---|
| **Linux** | Included with `apache2-utils`: `apt install apache2-utils`. |
| **macOS** | Bundled with macOS (Apache installed). |
| **Windows** | Install Apache for Windows — ab is included in the `bin/` directory. |
| **Verify** | `ab -V`. |

---

### Task 1.3 — Basic Syntax

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Format** | `ab [options] http://target.com/path/`. Note the trailing slash — required. |
| **Key Options** | `-n 1000` — total requests. `-c 50` — concurrent connections. `-k` — Keep-Alive. `-H "Header: value"` — add custom header. `-p post_data.txt -T content-type` — POST request. `-s 30` — timeout per request (seconds). |

---

# PHASE 2: CORE USAGE

---

### Task 2.1 — Basic GET Benchmark

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `ab -n 1000 -c 10 http://target.com/`. |
| **What This Does** | Sends 1000 total requests, 10 at a time. Reports how long it took, req/sec, mean response time. |
| **Realistic Test** | Match concurrency to expected real-world load. 10 concurrent = small site. 100 concurrent = medium traffic. |

---

### Task 2.2 — Authenticated Request

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Cookie Auth** | `ab -n 500 -c 20 -H "Cookie: session=abc123" http://target.com/dashboard`. |
| **Basic Auth** | `ab -n 500 -c 20 -A username:password http://target.com/api`. |
| **Bearer Token** | `ab -n 500 -c 20 -H "Authorization: Bearer eyJ..." http://target.com/api/data`. |

---

### Task 2.3 — POST Request Benchmark

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Create Body File** | `echo '{"user":"test","action":"query"}' > body.json`. |
| **Command** | `ab -n 500 -c 20 -p body.json -T "application/json" http://target.com/api/endpoint`. |
| **Form POST** | `echo "user=test&pass=secret" > form.txt`. `ab -n 500 -c 20 -p form.txt -T "application/x-www-form-urlencoded" http://target.com/login`. |

---

### Task 2.4 — Keep-Alive and HTTPS

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Keep-Alive** | `ab -n 1000 -c 50 -k http://target.com/` — reuses TCP connections (HTTP/1.1 keep-alive). Significantly faster — removes TCP connection setup overhead. More realistic for modern apps (browsers reuse connections). |
| **HTTPS** | `ab -n 500 -c 20 https://target.com/` — TLS overhead adds latency. Compare HTTP vs HTTPS response times to measure TLS overhead. |

---

# PHASE 3: INTERPRETING OUTPUT

---

### Task 3.1 — Key Metrics

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Requests per second** | `Requests per second: 423.19 [#/sec]` — server throughput. Higher = better. This is the headline metric. |
| **Time per request (mean)** | `Time per request: 23.634 [ms] (mean)` — average response time across all requests. Lower = better. |
| **Time per request (across all concurrent)** | `Time per request: 2.363 [ms] (mean, across all concurrent requests)` — mean time per connection including concurrency. Lower than the mean because connections are served in parallel. |
| **Transfer rate** | `Transfer rate: 1234.56 [Kbytes/sec]` — data throughput. Useful for bandwidth estimation. |
| **Failed requests** | `Failed requests: 0` — any non-zero value indicates the server is dropping or erroring on requests under load. Critical metric. |

---

### Task 3.2 — Connection Time Breakdown

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Table** | `Connection Times (ms)`: rows=Connect, Processing, Waiting, Total. Columns=min, mean, median, max, stddev. |
| **Connect** | TCP connection setup time. High connect time = network latency or server backlog. |
| **Waiting** | Time from request sent to first byte received (TTFB — Time to First Byte). High TTFB = slow server-side processing. |
| **Processing** | Time from first byte received to last byte received. High processing = large response body or slow transfer. |
| **Total** | Connect + Processing. |

---

### Task 3.3 — Percentile Distribution

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Table** | `Percentage of the requests served within a certain time (ms)`. Shows 50th, 66th, 75th, 80th, 90th, 95th, 98th, 99th, 100th percentile response times. |
| **Important** | The 99th and 100th percentile are the "tail latency" — the worst-case experience for 1% and the absolute worst request. High tail latency = unpredictable performance under load. |
| **SLA Context** | If SLA requires <500ms for 99% of requests: check if 99th percentile is below 500ms under your expected concurrency. |

---

### Task 3.4 — Interpreting Failed Requests

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Non-zero Failed** | Any failed request during a benchmark = the server cannot sustain that load level reliably. Common causes: connection refused (max connections reached), timeouts, 500 errors (server crash/exception). |
| **Find the Threshold** | Binary search: at 50 concurrent → 0 failures. At 200 concurrent → 50 failures. At 100 concurrent → 0 failures. At 150 concurrent → 5 failures. Max stable concurrency ≈ 130. |

---

# PHASE 4: LIMITATIONS & ALTERNATIVES

---

### Task 4.1 — ab Limitations

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Single URL** | Only tests one URL. Real traffic hits dozens of different URLs. |
| **No JS Execution** | Doesn't execute JavaScript, fetch CSS, or load images. Not representative of a real browser visit. |
| **HTTP/1.1 Only** | ab doesn't support HTTP/2 or HTTP/3. Modern servers are optimized for HTTP/2 — ab results may not reflect real performance. |
| **Single-threaded** | ab itself is single-threaded — at very high concurrency, ab becomes the bottleneck before the server does. |

---

### Task 4.2 — wrk as the Upgrade

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **wrk Advantages** | Multi-threaded (doesn't bottleneck on the client side). Lua scripting for complex request scenarios. Better for sustained, high-concurrency load. More accurate at high request rates. |
| **When to Use ab** | Quick sanity check. Simple scenarios. When wrk isn't available. When you need results in 30 seconds without configuration. |
| **When to Use wrk** | Serious performance benchmarking. High concurrency (>200). Complex request scenarios. |

---

### Task 4.3 — ab as a Learning Tool

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Teaching Concurrency** | Run ab with -c 1 (serial) vs. -c 50 (concurrent). Compare req/sec. See the benefit of parallelism. |
| **Teaching Caching** | Run ab against a cached endpoint vs. uncached. See 10x+ improvement from caching. |
| **Teaching Rate Limiting** | Apply Nginx rate limiting. Run ab. See failed requests appear. Remove rate limiting. See improvement. |

---

# PHASE 5: MASTERY CHECK

---

### Task 5.1 — Competency Self-Assessment

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Competency | Self-Assessment |
|:---|:---:|
| Can run a basic GET benchmark with specified concurrency | ☐ |
| Can benchmark authenticated (cookie/token) endpoints | ☐ |
| Can interpret requests/second, mean response time, and failed requests | ☐ |
| Can read the percentile distribution table | ☐ |
| Understands the limitations of ab vs. wrk | ☐ |
| Can use ab to find a server's maximum stable concurrency | ☐ |

---

### Task 5.2 — Interview Questions

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

1. What does ApacheBench measure and what is its primary output metric?
2. What is the difference between `-n` and `-c` in an ab command?
3. What does "failed requests" in ab output mean?
4. What does the 99th percentile response time tell you?
5. What are the key limitations of ab compared to wrk?
6. How do you benchmark an endpoint that requires authentication?
