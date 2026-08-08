# 🔧 wrk: Complete Reference

> **What is wrk?** wrk is a modern, high-performance HTTP benchmarking tool. It uses a multi-threaded design and event-driven I/O to generate far more HTTP load than ApacheBench from a single machine. It supports Lua scripting for custom request generation (dynamic URLs, different methods, request bodies, response validation). wrk is the standard HTTP load testing tool when you need accurate, sustained, high-concurrency results.
>
> **When to use it:** Serious HTTP/HTTPS performance benchmarking. Finding a server's maximum sustained throughput. Testing API performance under realistic load. Comparing server configurations. When ab runs out of capacity before the server does (very common with high-performance servers or APIs).
>
> **Tier 4 Reminder:** Know the command syntax, understand the output, and know when wrk is appropriate over ab.
>
> **Roadmap Phase:** Phase 10 (DoS Awareness and HTTP Performance Testing)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 3 | 45 min |
| 2 | Core Usage | 4 | 1–2 hours |
| 3 | Lua Scripting | 4 | 2–3 hours |
| 4 | Interpreting Results | 3 | 1 hour |
| 5 | Mastery Check | 2 | 20 min |
| | **Total** | **16** | **~5–7 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — What Makes wrk Different

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Multi-threaded** | Uses multiple OS threads, each running an event loop. Can saturate high-performance servers that ab cannot. |
| **Event-driven I/O** | Uses `epoll`/`kqueue` — same architecture as Nginx. Handles thousands of concurrent connections efficiently from one machine. |
| **Lua Scripting** | Embedded Lua interpreter allows custom request logic: different URLs per request, dynamic headers, request body generation, response validation. |
| **vs. ab** | ab: simple, single-threaded, limited to one URL, easy to use. wrk: multi-threaded, Lua scripting, sustainable at very high concurrency, more accurate. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Linux** | `apt install wrk`. Or compile: `git clone https://github.com/wg/wrk; cd wrk; make`. |
| **macOS** | `brew install wrk`. |
| **Verify** | `wrk --version`. |
| **Note** | wrk does not have a Windows build — use Linux/macOS or WSL. |

---

### Task 1.3 — Basic Syntax

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Format** | `wrk [options] <URL>`. |
| **Key Options** | `-t 4` — threads (typically 2x CPU cores). `-c 100` — concurrent connections. `-d 30s` — duration (30 seconds). `-H "Header: value"` — add header. `--script script.lua` — Lua script. `--latency` — print latency statistics. `-T 5s` — timeout per request. |

---

# PHASE 2: CORE USAGE

---

### Task 2.1 — Basic Benchmark

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `wrk -t 4 -c 100 -d 30s http://target.com/`. |
| **Explanation** | 4 threads, 100 concurrent connections, run for 30 seconds. Each thread handles 25 connections. |
| **Thread Count** | Rule of thumb: 2x physical CPU cores. More threads beyond that don't help (context switching overhead). On a 2-core machine: `-t 4`. On a 4-core: `-t 8`. |

---

### Task 2.2 — Authenticated Endpoint

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Cookie** | `wrk -t 4 -c 100 -d 30s -H "Cookie: session=abc123" http://target.com/api`. |
| **Bearer Token** | `wrk -t 4 -c 100 -d 30s -H "Authorization: Bearer eyJ..." http://target.com/api/data`. |
| **Multiple Headers** | Chain multiple `-H` flags: `wrk -t 4 -c 100 -H "Auth: bearer token" -H "Accept: application/json" -d 30s http://target.com/`. |

---

### Task 2.3 — High Concurrency Test

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Find the concurrency level at which the server's performance degrades. |
| **Method** | `wrk -t 4 -c 50 -d 30s --latency http://target.com/` → record req/sec and 99th percentile. Increase: `-c 100`, `-c 200`, `-c 500`, `-c 1000`. Plot: as concurrency increases, at what point do req/sec plateau or drop and latency spike? That's the saturation point. |

---

### Task 2.4 — Sustained Load Test

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Verify server performance is stable over time, not just for a quick burst. |
| **Command** | `wrk -t 4 -c 100 -d 600s --latency http://target.com/`. (10 minute run). |
| **Watch For** | Memory leaks: does req/sec decrease over time while memory grows? Connection pool exhaustion: do errors appear after N minutes? GC pressure: does latency spike periodically (garbage collection pauses)? |

---

# PHASE 3: LUA SCRIPTING

---

### Task 3.1 — POST Request Script

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Script** | `-- post.lua`<br>`wrk.method = "POST"`<br>`wrk.body = '{"user":"test","action":"ping"}'`<br>`wrk.headers["Content-Type"] = "application/json"` |
| **Run** | `wrk -t 4 -c 100 -d 30s --script post.lua http://target.com/api`. |
| **Use Case** | Benchmark a POST API endpoint. Measure throughput for write-heavy workloads. |

---

### Task 3.2 — Dynamic URLs

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Script** | `-- dynamic.lua`<br>`math.randomseed(os.time())`<br>`local ids = {1, 2, 3, 4, 5, 100, 200}`<br>`function request()`<br>`  local id = ids[math.random(#ids)]`<br>`  return wrk.format("GET", "/api/users/" .. id)`<br>`end` |
| **Use Case** | Benchmark an endpoint with different resource IDs. More realistic than always hitting the same URL (avoids server-side caching of a single object). |

---

### Task 3.3 — Response Validation

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Script** | `-- validate.lua`<br>`local errors = 0`<br>`function response(status, headers, body)`<br>`  if status ~= 200 then`<br>`    errors = errors + 1`<br>`  end`<br>`end`<br>`function done(summary, latency, requests)`<br>`  io.write("Custom errors: " .. errors .. "\n")`<br>`end` |
| **Use Case** | Count non-200 responses during load test. Identify at what concurrency errors start appearing. |

---

### Task 3.4 — Rate-Limited Test

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Script** | `-- ratelimit.lua`<br>`local delay = 100 -- ms between requests per connection`<br>`function delay()`<br>`  return delay`<br>`end` |
| **Use Case** | Simulate realistic user think time. Instead of hammering as fast as possible, each connection waits 100ms between requests — simulating real user behavior. More accurate for per-user throughput testing. |

---

# PHASE 4: INTERPRETING RESULTS

---

### Task 4.1 — Output Metrics

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Output** | `Running 30s test @ http://target.com/`. `  4 threads and 100 connections`. `  Thread Stats   Avg      Stdev     Max   +/- Stdev`. `    Latency    23.45ms   5.12ms  89.34ms   85.23%`. `    Req/Sec     1.07k    98.34     1.32k    67.12%`. `  128340 requests in 30.08s, 23.45MB read`. `Requests/sec:   4266.23`. `Transfer/sec:    798.23KB`. |
| **Req/Sec** | The headline metric. 4266 requests/second = server throughput under this load. |
| **Latency** | Avg=23ms is the mean. Max=89ms is the worst. Stdev=5ms — low stdev = consistent; high stdev = unpredictable. |

---

### Task 4.2 — Latency Distribution (`--latency`)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Flag** | Add `--latency` to get percentile breakdown. |
| **Output** | `Latency Distribution`. `  50%   21.34ms`. `  75%   28.12ms`. `  90%   45.23ms`. `  99%   67.89ms`. `  99.9%   89.34ms`. |
| **P99** | The 99th percentile response time. 1% of requests take longer than this. If your SLA is "99th percentile < 100ms", you can verify compliance under load. |
| **Tail Latency** | Large gap between P90 and P99 = unpredictable tail. GC pauses, lock contention, or resource exhaustion at peak. |

---

### Task 4.3 — Errors in Output

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Socket Errors** | `Socket errors: connect 0, read 12, write 0, timeout 3`. Read errors = server closed connection before sending full response. Timeout = server too slow. Connect errors = can't open new connections. |
| **Non-2xx** | `Non-2xx or 3xx responses: 245`. Server returned errors (400, 500) for some requests. Always investigate — usually indicates server overload or rate limiting. |
| **Clean Run** | A proper benchmark: 0 socket errors, 0 non-2xx. Any errors = the server is struggling. |

---

# PHASE 5: MASTERY CHECK

---

### Task 5.1 — Competency Self-Assessment

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Competency | Self-Assessment |
|:---|:---:|
| Can run a basic wrk benchmark with threads, connections, and duration | ☐ |
| Can add custom headers for authenticated endpoint testing | ☐ |
| Can interpret req/sec, mean latency, and P99 latency | ☐ |
| Can write a basic Lua script for POST requests | ☐ |
| Can identify the saturation point by varying concurrency | ☐ |
| Knows when to use wrk vs. ab | ☐ |

---

### Task 5.2 — Interview Questions

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

1. How does wrk differ architecturally from ApacheBench?
2. What does the P99 latency metric represent and why does it matter?
3. What does a high standard deviation in wrk latency indicate?
4. How do you write a Lua script to benchmark a POST API endpoint?
5. What does a non-zero "socket errors" count mean in wrk output?
6. When would you use wrk over ab?
