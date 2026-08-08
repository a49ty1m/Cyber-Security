# 🔧 Tools Directory

> **52 tool mastery checklists** organized by tier and roadmap phase.
> Each file follows a structured 8-phase curriculum with checkbox tasks, competency matrix, and interview questions.

---

## Tier System

| Tier | Label | Meaning | Depth |
|:----:|:------|:--------|:------|
| 1 | **Core** | Used on every engagement. Must be mastered before advancing. | 8 phases · 38–50 tasks · 33–58 hrs |
| 2 | **Frequent** | Used regularly in specific attack chains or phases. | 8 phases · 25–40 tasks · 25–45 hrs |
| 3 | **Situational** | Used for specific target types or scenarios. | 4–6 phases · 16–24 tasks · 12–22 hrs |
| 4 | **Niche / Reference** | Specialized use. Know when to reach for it. | 4–5 phases · 12–18 tasks · 6–14 hrs |

---

## Tier 1 — Core Tools

| Tool | Description | Roadmap Phase |
|:-----|:------------|:-------------|
| [🗺️ Nmap](Nmap.md) | Network discovery, port scanning, service/OS detection, NSE scripting | Phase 1–2 |
| [🕷️ Burp Suite](Burp_Suite.md) | Web application security testing platform — proxy, scanner, intruder, repeater | Phase 3 |
| [💀 Metasploit Framework](Metasploit_Framework.md) | Exploitation framework — exploits, payloads, post-exploitation, pivoting | Phase 4 |
| [🔥 Hashcat](Hashcat.md) | GPU-accelerated offline password cracking — all hash types and attack modes | Phase 4–5 |
| [🦈 Wireshark](Wireshark.md) | Packet capture and deep protocol analysis — live capture and PCAP forensics | Phase 2–7 |
| [🔌 Netcat](Netcat.md) | TCP/UDP swiss-army knife — port scanning, file transfer, reverse/bind shells | Phase 2–5 |
| [🩸 BloodHound](BloodHound.md) | AD graph-based attack path analysis — CE (Docker) and Legacy (Neo4j) | Phase 5 |
| [🐍 Impacket](Impacket.md) | Python AD attack suite — secretsdump, Kerberoast, AS-REP, DCSync, relay | Phase 4–5 |
| [🐉 LinPEAS](LinPEAS.md) | Linux privilege escalation enumeration script | Phase 4–5 |
| [🔓 Hydra](Hydra.md) | Online password brute-force — SSH, FTP, HTTP, SMB, RDP and more | Phase 3–4 |

---

## Tier 2 — Frequent Tools

| Tool | Description | Roadmap Phase |
|:-----|:------------|:-------------|
| [🌐 NetExec](NetExec.md) | AD credential testing and lateral movement — successor to CrackMapExec (`nxc`) | Phase 4–5 |
| [📡 Responder](Responder.md) | LLMNR/NBT-NS/mDNS poisoning — NetNTLMv2 credential capture and relay | Phase 4–5 |
| [🔑 John the Ripper](John_the_Ripper.md) | CPU-focused password cracking — exotic formats and incremental modes | Phase 4–5 |
| [💉 sqlmap](sqlmap.md) | Automated SQL injection detection and exploitation | Phase 3 |
| [🌀 ffuf](ffuf.md) | Fast web fuzzer — directory, parameter, virtual host, and content discovery | Phase 3 |
| [📂 Gobuster](Gobuster.md) | Directory, DNS, and virtual host brute-forcing | Phase 2–3 |
| [🔍 Nikto](Nikto.md) | Web server vulnerability scanner — misconfigurations and known CVEs | Phase 2–3 |
| [⚡ Nuclei](Nuclei.md) | Template-based vulnerability scanner — 9,000+ community templates, modern Nikto replacement | Phase 2–3 |
| [🪟 WinPEAS](WinPEAS.md) | Windows privilege escalation enumeration script | Phase 4–5 |
| [🔬 Ghidra](Ghidra.md) | NSA reverse engineering framework — binary analysis, decompilation | Phase 7 |
| [🐛 x64dbg](x64dbg.md) | Windows userland debugger for dynamic malware analysis | Phase 7 |
| [🐍 Sliver](Sliver.md) | Modern open-source C2 framework — implants, pivoting, armory | Phase 5–6 |
| [🔀 Ligolo-ng](Ligolo-ng.md) | Agent-based network pivoting and tunneling via TUN interface | Phase 5 |
| [🔀 Chisel](Chisel.md) | HTTP/HTTPS TCP tunneling and SOCKS5 proxy — firewall-friendly pivoting | Phase 5 |
| [🌾 theHarvester](theHarvester.md) | OSINT email, subdomain, and hostname harvesting | Phase 1 |
| [🔭 Recon-ng](Recon-ng.md) | Modular OSINT reconnaissance framework | Phase 1 |
| [🕸️ SpiderFoot](SpiderFoot.md) | Automated OSINT intelligence gathering — 200+ modules | Phase 1 |
| [🕵️ Maltego](Maltego.md) | Visual link analysis and OSINT graph mapping | Phase 1 |
| [🌐 Amass](Amass.md) | OWASP subdomain enumeration — passive, active, API-enriched | Phase 1 |
| [🎣 GoPhish](GoPhish.md) | Phishing simulation platform — campaigns, tracking, reporting | Phase 6 |
| [🎭 SET](SET.md) | Social Engineering Toolkit — credential harvesting, payload delivery | Phase 6 |
| [🕵️ Bettercap](Bettercap.md) | Active network MitM framework — ARP, DNS, HTTPS, BLE, Wi-Fi | Phase 3–4 |
| [🐛 Ettercap](Ettercap.md) | ⚠️ Legacy MitM tool — use Bettercap for active work. Preserved for protocol fundamentals | Phase 3 |
| [📦 Scapy](Scapy.md) | Python packet crafting and network manipulation library | Phase 2–3 |
| [📻 tcpdump](tcpdump.md) | CLI packet capture — remote collection, filter syntax, PCAP production | Phase 2–7 |
| [🔐 jwt-tool](jwt-tool.md) | JWT security testing — algorithm confusion, secret cracking, claim manipulation | Phase 3 |
| [🔌 WPScan](wpscan.md) | WordPress security scanner — plugins, themes, users, vulnerabilities | Phase 3 |
| [🪟 Evil-WinRM](Evil-WinRM.md) | WinRM post-exploitation shell — PTH, AMSI bypass, in-memory execution | Phase 4–5 |
| [🔑 Kerbrute](Kerbrute.md) | AD username enumeration and password spraying via Kerberos pre-auth | Phase 2–3 |
| [🐱 Mimikatz](Mimikatz.md) | Windows in-memory credential dumping — logonpasswords, DCSync, Golden Ticket | Phase 4–5 |
| [🎫 Rubeus](Rubeus.md) | Windows-native Kerberos attack toolkit — roasting, PTT, delegation abuse | Phase 4–5 |
| [📡 Aircrack-ng](Aircrack-ng.md) | Wi-Fi security toolkit — monitor mode, handshake capture, WPA cracking | Phase 3 |
| [🧠 Volatility](Volatility.md) | Memory forensics framework — process analysis, network artifacts, malware detection | Phase 7 |
| [🔍 Autopsy](Autopsy.md) | Digital forensics platform — disk image analysis, file recovery, timeline | Phase 7 |
| [💾 FTK Imager](FTK_Imager.md) | Forensic evidence acquisition — disk and memory imaging | Phase 7 |
| [📅 Plaso](Plaso.md) | Super-timeline generation from forensic artifacts — log2timeline | Phase 7 |

---

## Tier 3 — Situational Tools

| Tool | Description | Roadmap Phase |
|:-----|:------------|:-------------|
| [🛡️ OWASP ZAP](OWASP_ZAP.md) | Free web application scanner — active scan, spider, fuzzer | Phase 3 |
| [📬 Postman](Postman.md) | API development and security testing platform | Phase 3 |
| [🧼 SoapUI](SoapUI.md) | SOAP and REST web services security testing | Phase 3 |
| [🔬 PEStudio](PEStudio.md) | Windows PE file static analysis — imports, strings, entropy, indicators | Phase 7 |
| [🔎 Detect It Easy](Detect_It_Easy.md) | File type, packer, compiler, and protector identification | Phase 7 |
| [📝 strings](strings.md) | Static string extraction from binaries and memory dumps | Phase 7 |
| [🔍 Procmon](Procmon.md) | Windows process monitor — file system, registry, network, process activity | Phase 7 |

---

## Tier 4 — Niche / Reference Tools

| Tool | Description | Roadmap Phase |
|:-----|:------------|:-------------|
| [🍪 Cookie-Editor](Cookie-Editor.md) | Browser cookie inspection and manipulation extension | Phase 3 |
| [📊 ApacheBench](ApacheBench.md) | HTTP load testing and benchmarking tool (`ab`) | Phase 10 |
| [⚡ wrk](wrk.md) | Modern HTTP benchmarking with Lua scripting | Phase 10 |
| [💣 GoldenEye](GoldenEye.md) | HTTP DoS simulation tool — educational use only | Phase 10 |
| [🐌 Slowloris](Slowloris.md) | Slow HTTP DoS tool — connection exhaustion simulation | Phase 10 |
| [🔨 hping3](hping3.md) | TCP/IP packet crafting — SYN floods, traceroute, firewall testing | Phase 10 |
| [📶 iperf3](iperf3.md) | Network bandwidth and throughput testing | Phase 10 |

---

## Navigation by Phase

| Phase | Relevant Tools |
|:------|:--------------|
| **Phase 1 — Reconnaissance** | theHarvester, Recon-ng, SpiderFoot, Maltego |
| **Phase 2 — Scanning & Enumeration** | Nmap, Netcat, Gobuster, Nikto, Scapy, tcpdump, Wireshark |
| **Phase 3 — Web & Service Attacks** | Burp Suite, sqlmap, ffuf, Gobuster, Nikto, OWASP ZAP, Postman, SoapUI, jwt-tool, WPScan, Bettercap, Ettercap, Scapy |
| **Phase 4 — Exploitation** | Metasploit, Hydra, Hashcat, Impacket, NetExec, Responder |
| **Phase 5 — Post-Exploitation & Lateral Movement** | LinPEAS, WinPEAS, BloodHound, Impacket, NetExec, Responder, Hashcat, John the Ripper, Sliver, Ligolo-ng, Netcat |
| **Phase 6 — Social Engineering & Red Team** | GoPhish, SET, Sliver |
| **Phase 7 — DFIR & Reverse Engineering** | Volatility, Autopsy, FTK Imager, Plaso, Ghidra, x64dbg, PEStudio, Detect It Easy, strings, Procmon, Wireshark, tcpdump |
| **Phase 10 — DoS Awareness** | ApacheBench, wrk, GoldenEye, Slowloris, hping3, iperf3 |

---

## Planned Files (from TOOLS_AUDIT.md)

These tools were added as part of the TOOLS_AUDIT.md recommendations. All planned files have now been created:

| Tool | Status | File |
|:-----|:------:|:-----|
| Evil-WinRM | ✅ Created | [Evil-WinRM.md](Evil-WinRM.md) |
| Kerbrute | ✅ Created | [Kerbrute.md](Kerbrute.md) |
| Mimikatz | ✅ Created | [Mimikatz.md](Mimikatz.md) |
| Amass | ✅ Created | [Amass.md](Amass.md) |
| Rubeus | ✅ Created | [Rubeus.md](Rubeus.md) |
| Nuclei | ✅ Created | [Nuclei.md](Nuclei.md) |
| Aircrack-ng | ✅ Created | [Aircrack-ng.md](Aircrack-ng.md) |
| Chisel | ✅ Created | [Chisel.md](Chisel.md) |

> See [TOOLS_AUDIT.md](../TOOLS_AUDIT.md) for the full audit report.
