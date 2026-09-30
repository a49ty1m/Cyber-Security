# 🔧 Tools Directory

> **88 tool mastery checklists** organized by tier and roadmap stage/module.
> Each file follows a structured curriculum with checkbox tasks, competency matrix, and interview questions.

---

## 🧭 Navigation
> [[Roadmap/README|🏠 Master Roadmap]] · [[Roadmap/Stage-1_Foundation|Stage 1: Foundation]] · [[Roadmap/Stage-2_Offense-I|Stage 2: Offense I]] · [[Roadmap/Stage-3_Web-and-App-Sec|Stage 3: Web & App Sec]] · [[Roadmap/Stage-4_Enterprise|Stage 4: Enterprise]] · [[Roadmap/Stage-5_Specialized|Stage 5: Specialized]] · [[Roadmap/Shelf_Post-Hire|📦 Shelf]]

---

## Tier System

| Tier | Label | Meaning | Depth |
|:----:|:------|:--------|:------|
| 1 | **Core** | Used on every engagement. Must be mastered before advancing. | Full checklists · 38–50 tasks · 33–58 hrs |
| 2 | **Frequent** | Used regularly in specific attack chains or modules. | Targeted checklists · 25–40 tasks · 25–45 hrs |
| 3 | **Situational** | Used for specific target types, environments, or scenarios. | Focused checklists · 16–24 tasks · 12–22 hrs |
| 4 | **Niche / Reference** | Specialized use, post-hire depth, or legacy context. Know when to reach for it. | Reference checklists · 12–18 tasks · 6–14 hrs |

---

## Tier 1 — Core Tools

| Tool | Description | Stage / Module |
|:-----|:------------|:---------------|
| [[Netcat\|🔌 Netcat]] | TCP/UDP swiss-army knife — port scanning, file transfer, reverse/bind shells | Stage 1: Module 04 & Stage 2: Module 13 |
| [[Wireshark\|🦈 Wireshark]] | Packet capture and deep protocol analysis — live capture and PCAP forensics | Stage 1: Module 04 |
| [[Nmap\|🗺️ Nmap]] | Network discovery, port scanning, service/OS detection, NSE scripting | Stage 2: Module 08 & 09 |
| [[Hashcat\|🔥 Hashcat]] | GPU-accelerated offline password cracking — all hash types and attack modes | Stage 2: Module 12 |
| [[Hydra\|🔓 Hydra]] | Online password brute-force — SSH, FTP, HTTP, SMB, RDP and more | Stage 2: Module 12 & 13 |
| [[LinPEAS\|🐉 LinPEAS]] | Linux privilege escalation enumeration script | Stage 2: Module 13 |
| [[Metasploit_Framework\|💀 Metasploit Framework]] | Exploitation framework — exploits, payloads, post-exploitation, pivoting | Stage 2: Module 13 |
| [[Burp_Suite\|🕷️ Burp Suite]] | Web application security testing platform — proxy, scanner, intruder, repeater | Stage 3: Module 14 |
| [[BloodHound\|🩸 BloodHound]] | AD graph-based attack path analysis — CE (Docker) and Legacy (Neo4j) | Stage 4: Module 19 |
| [[Impacket\|🐍 Impacket]] | Python AD attack suite — secretsdump, Kerberoast, AS-REP, DCSync, relay | Stage 4: Module 19 |

---

## Tier 2 — Frequent Tools

| Tool | Description | Stage / Module |
|:-----|:------------|:---------------|
| [[Scapy\|📦 Scapy]] | Python packet crafting and network manipulation library | Stage 1: Module 04 & Stage 4: Module 23 |
| [[tcpdump\|📻 tcpdump]] | CLI packet capture — remote collection, filter syntax, PCAP production | Stage 1: Module 04 |
| [[Amass\|🌐 Amass]] | OWASP subdomain enumeration — passive, active, API-enriched | Stage 2: Module 08 |
| [[Maltego\|🕵️ Maltego]] | Visual link analysis and OSINT graph mapping | Stage 2: Module 08 |
| [[Recon-ng\|🔭 Recon-ng]] | Modular OSINT reconnaissance framework | Stage 2: Module 08 |
| [[SpiderFoot\|🕸️ SpiderFoot]] | Automated OSINT intelligence gathering — 200+ modules | Stage 2: Module 08 |
| [[theHarvester\|🌾 theHarvester]] | OSINT email, subdomain, and hostname harvesting | Stage 2: Module 08 |
| [[Gobuster\|📂 Gobuster]] | Directory, DNS, and virtual host brute-forcing | Stage 2: Module 10 & Stage 3: Module 14 |
| [[John_the_Ripper\|🔑 John the Ripper]] | CPU-focused password cracking — exotic formats and incremental modes | Stage 2: Module 12 |
| [[Chisel\|🔀 Chisel]] | HTTP/HTTPS TCP tunneling and SOCKS5 proxy — firewall-friendly pivoting | Stage 2: Module 13 & Stage 4: Module 19 |
| [[Ligolo-ng\|🔀 Ligolo-ng]] | Agent-based network pivoting and tunneling via TUN interface | Stage 2: Module 13 & Stage 4: Module 19 |
| [[WinPEAS\|🪟 WinPEAS]] | Windows privilege escalation enumeration script | Stage 2: Module 13 |
| [[ffuf\|🌀 ffuf]] | Fast web fuzzer — directory, parameter, virtual host, and content discovery | Stage 3: Module 14 & Stage 2: Module 10 |
| [[Nuclei\|⚡ Nuclei]] | Template-based vulnerability scanner — 9,000+ community templates | Stage 3: Module 14 & 16 |
| [[sqlmap\|💉 sqlmap]] | Automated SQL injection detection and exploitation | Stage 3: Module 14 |
| [[jwt-tool\|🔐 jwt-tool]] | JWT security testing — algorithm confusion, secret cracking, claim manipulation | Stage 3: Module 15 |
| [[Nikto\|🔍 Nikto]] | Web server vulnerability scanner — misconfigurations and known CVEs | Stage 3: Module 16 |
| [[wpscan\|🔌 WPScan]] | WordPress security scanner — plugins, themes, users, vulnerabilities | Stage 3: Module 16 |
| [[Certipy\|🎫 Certipy]] | Active Directory Certificate Services (ADCS) enumeration and abuse | Stage 4: Module 19 |
| [[Evil-WinRM\|🪟 Evil-WinRM]] | WinRM post-exploitation shell — PTH, AMSI bypass, in-memory execution | Stage 4: Module 19 & Stage 2: Module 13 |
| [[Kerbrute\|🔑 Kerbrute]] | AD username enumeration and password spraying via Kerberos pre-auth | Stage 4: Module 19 |
| [[Mimikatz\|🐱 Mimikatz]] | Windows in-memory credential dumping — logonpasswords, DCSync, Golden Ticket | Stage 4: Module 19 |
| [[NetExec\|🌐 NetExec]] | AD credential testing and lateral movement — successor to CrackMapExec (`nxc`) | Stage 4: Module 19 |
| [[Responder\|📡 Responder]] | LLMNR/NBT-NS/mDNS poisoning — NetNTLMv2 credential capture and relay | Stage 4: Module 19 & 23 |
| [[Rubeus\|🎫 Rubeus]] | Windows-native Kerberos attack toolkit — roasting, PTT, delegation abuse | Stage 4: Module 19 |
| [[Pacu\|☁️ Pacu]] | AWS penetration testing framework — privilege escalation and data exfiltration | Stage 4: Module 20 |
| [[Prowler\|☁️ Prowler]] | Multi-cloud security assessment, auditing, and hardening tool | Stage 4: Module 20 |
| [[Bettercap\|🕵️ Bettercap]] | Active network MitM framework — ARP, DNS, HTTPS, BLE, Wi-Fi | Stage 4: Module 23 |
| [[GoPhish\|🎣 GoPhish]] | Phishing simulation platform — campaigns, tracking, reporting | Stage 4: Module 24 |
| [[SET\|🎭 SET]] | Social Engineering Toolkit — credential harvesting, payload delivery | Stage 4: Module 24 |
| [[Sliver\|🐍 Sliver]] | Modern open-source C2 framework — implants, pivoting, armory | Stage 5: Module 27 & 29 |
| [[Garak\|🤖 Garak]] | LLM vulnerability scanner and red teaming automation framework | Stage 5: Module 28 |
| [[Ollama\|🤖 Ollama]] | Local LLM execution framework for offensive & security model testing | Stage 5: Module 28 |
| [[PyRIT\|🛡️ PyRIT]] | Python Risk Identification Tool for generative AI red teaming | Stage 5: Module 28 |
| [[Python_AI_SDKs\|🧠 Python AI SDKs]] | Programmatic attack surfaces for LLM APIs, LangChain, and agentic workflows | Stage 5: Module 28 |
| [[Havoc\|⚔️ Havoc]] | Modern post-exploitation command and control framework | Stage 5: Module 29 |
| [[Mythic\|🏛️ Mythic]] | Multi-agent collaborative C2 framework | Stage 5: Module 29 |
| [[Aircrack-ng\|📡 Aircrack-ng]] | Wi-Fi security toolkit — monitor mode, handshake capture, WPA cracking | Shelf: Module S01 |
| [[Autopsy\|🔍 Autopsy]] | Digital forensics platform — disk image analysis, file recovery, timeline | Shelf: Module S04 |
| [[FTK_Imager\|💾 FTK Imager]] | Forensic evidence acquisition — disk and memory imaging | Shelf: Module S04 |
| [[Plaso\|📅 Plaso]] | Super-timeline generation from forensic artifacts — log2timeline | Shelf: Module S04 |
| [[Volatility\|🧠 Volatility]] | Memory forensics framework — process analysis, network artifacts, malware detection | Shelf: Module S04 |
| [[Ghidra\|🔬 Ghidra]] | NSA reverse engineering framework — binary analysis, decompilation | Shelf: Module S05 |
| [[x64dbg\|🐛 x64dbg]] | Windows userland debugger for dynamic malware analysis | Shelf: Module S05 |

---

## Tier 3 — Situational Tools

| Tool | Description | Stage / Module |
|:-----|:------------|:---------------|
| [[Procmon\|🔍 Procmon]] | Windows process monitor — file system, registry, network, process activity | Stage 1: Module 03 & Shelf: S05 |
| [[OpenSSL\|🔒 OpenSSL]] | TLS handshake inspection, key generation, and certificate verification | Stage 1: Module 05 |
| [[socat\|🔄 socat]] | Multipurpose bidirectional relay — reverse shells, encrypted tunnels, port forwards | Stage 2: Module 13 |
| [[OWASP_ZAP\|🛡️ OWASP ZAP]] | Free web application scanner — active scan, spider, fuzzer | Stage 3: Module 14 |
| [[Postman\|📬 Postman]] | API development and security testing platform | Stage 3: Module 17 |
| [[SoapUI\|🧼 SoapUI]] | SOAP and REST web services security testing | Stage 3: Module 17 |
| [[ELK\|🦌 ELK]] | Elasticsearch, Logstash, Kibana open telemetry security data pipeline | Stage 3: Side-Track A |
| [[Sigma\|📜 Sigma]] | Generic signature format for SIEM detection rules | Stage 3: Side-Track A |
| [[Splunk\|🔎 Splunk]] | Enterprise SIEM log ingestion, search processing, and alert creation | Stage 3: Side-Track A |
| [[Sysmon\|📊 Sysmon]] | Advanced Windows event telemetry for process creation and network connections | Stage 3: Side-Track A |
| [[Wazuh\|🛡️ Wazuh]] | Open-source XDR and SIEM host-based monitoring platform | Stage 3: Side-Track A |
| [[YARA\|🔍 YARA]] | Pattern matching swiss knife for malware identification and classification | Stage 3: Side-Track A & Shelf: S05 |
| [[GDB\|🐞 GDB]] | GNU Debugger with GEF/pwndbg extensions for Linux binary exploitation | Stage 5: Module 27 & Shelf: S06 |
| [[pwntools\|⚡ pwntools]] | CTF framework and exploit development library | Stage 5: Module 27 & Shelf: S06 |
| [[APKTool\|📦 APKTool]] | Reverse engineering Android APK files — decoding and rebuilding resources | Shelf: Module S02 |
| [[Frida\|💉 Frida]] | Dynamic instrumentation toolkit for mobile app runtime analysis | Shelf: Module S02 |
| [[jadx\|🔍 jadx]] | Dex to Java decompiler with GUI for Android APK analysis | Shelf: Module S02 |
| [[Objection\|📱 Objection]] | Runtime mobile security assessment framework powered by Frida | Shelf: Module S02 |
| [[Detect_It_Easy\|🔎 Detect It Easy]] | File type, packer, compiler, and protector identification | Shelf: Module S05 |
| [[PEStudio\|🔬 PEStudio]] | Windows PE file static analysis — imports, strings, entropy, indicators | Shelf: Module S05 |
| [[strings\|📝 strings]] | Static string extraction from binaries and memory dumps | Shelf: Module S05 |
| [[Gitleaks\|🔑 Gitleaks]] | Fast secret scanner for Git repositories and files | Shelf: Module S12 & S13 |
| [[TruffleHog\|🐽 TruffleHog]] | Deep secret scanner searching high-entropy strings and credentials in Git | Shelf: Module S12 & S13 |
| [[Checkov\|🛡️ Checkov]] | Static code analysis tool for infrastructure-as-code (Terraform, K8s) | Shelf: Module S13 |
| [[Semgrep\|🛡️ Semgrep]] | Fast static analysis engine for finding bugs and enforcing code standards | Shelf: Module S13 & S14 |
| [[tfsec\|⚙️ tfsec]] | Security scanner for Terraform code | Shelf: Module S13 |

---

## Tier 4 — Niche / Reference Tools

| Tool | Description | Stage / Module |
|:-----|:------------|:---------------|
| [[hping3\|🔨 hping3]] | TCP/IP packet crafting — SYN floods, traceroute, firewall testing | Stage 1: Module 04 & Shelf: S17 |
| [[iperf3\|📶 iperf3]] | Network bandwidth and throughput testing | Stage 1: Module 04 |
| [[Cookie-Editor\|🍪 Cookie-Editor]] | Browser cookie inspection and manipulation extension | Stage 3: Module 15 |
| [[Ettercap\|🐛 Ettercap]] | ⚠️ Legacy MitM tool — preserved for protocol fundamentals | Stage 4: Module 23 (Legacy) |
| [[ApacheBench\|📊 ApacheBench]] | HTTP load testing and benchmarking tool (`ab`) | Shelf: Module S17 |
| [[GoldenEye\|💣 GoldenEye]] | HTTP DoS simulation tool — educational use only | Shelf: Module S17 |
| [[Slowloris\|🐌 Slowloris]] | Slow HTTP DoS tool — connection exhaustion simulation | Shelf: Module S17 |
| [[wrk\|⚡ wrk]] | Modern HTTP benchmarking with Lua scripting | Shelf: Module S17 |

---

## Navigation by Stage

| Stage | Relevant Tools |
|:------|:--------------|
| **Stage 1 — Foundation** | Wireshark, tcpdump, Netcat, OpenSSL, Scapy, iperf3, Procmon |
| **Stage 2 — Offense I** | Nmap, Netcat, Gobuster, theHarvester, Recon-ng, SpiderFoot, Maltego, Amass, Metasploit, Hydra, Hashcat, John the Ripper, LinPEAS, WinPEAS, socat, Ligolo-ng, Chisel |
| **Stage 3 — Web & App Sec** | Burp Suite, sqlmap, ffuf, Gobuster, Nikto, Nuclei, OWASP ZAP, Postman, SoapUI, jwt-tool, WPScan, Cookie-Editor · *(Side-Track: Splunk, ELK, Wazuh, Sysmon, Sigma, YARA)* |
| **Stage 4 — Enterprise** | BloodHound, Impacket, NetExec, Responder, Evil-WinRM, Kerbrute, Certipy, Mimikatz, Rubeus, Pacu, Prowler, Bettercap, Ettercap, Scapy, GoPhish, SET, Ligolo-ng, Chisel |
| **Stage 5 — Specialized** | Sliver, Havoc, Mythic, pwntools, GDB, Ollama, Python AI SDKs, Garak, PyRIT |
| **Shelf — Post-Hire** | Aircrack-ng (S01), Frida, Objection, jadx, APKTool (S02), Volatility, Autopsy, FTK Imager, Plaso (S04), Ghidra, x64dbg, PEStudio, Detect It Easy, strings (S05), Semgrep, Gitleaks, TruffleHog, Checkov, tfsec (S12–S14), ApacheBench, wrk, GoldenEye, Slowloris, hping3 (S17) |
