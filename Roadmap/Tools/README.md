# 🔧 Tools Hub

> **88 tool mastery checklists** — each tool has its own folder with a structured checklist (`<Tool>.md`) and a personal notes file (`<Tool>_Notes.md`).
> Checklists contain checkbox tasks, a competency matrix, and interview questions. Notes files are yours — never regenerated.

---

## 🧭 Navigation

> [[Cyber-Security/Roadmap/README|MASTER_README]] · [[Cyber-Security/Roadmap/Stage-1_Foundation|Stage 1: Foundation]] · [[Cyber-Security/Roadmap/Stage-2_Offense-I|Stage 2: Offense I]] · [[Cyber-Security/Roadmap/Stage-3_Web-and-App-Sec|Stage 3: Web & App Sec]] · [[Cyber-Security/Roadmap/Stage-4_Enterprise|Stage 4: Enterprise]] · [[Cyber-Security/Roadmap/Stage-5_Specialized|Stage 5: Specialized]] · [[Cyber-Security/Roadmap/Shelf_Post-Hire|📦 Shelf]]

---

## 🏷️ Tier System

| Tier | Label | When you use it | Checklist depth |
| :----: | :------ | :---------------- | :---------------- |
| **1** | **Core** | Every single engagement — master these first | 38–50 tasks · 33–58 hrs |
| **2** | **Frequent** | Regularly, in specific attack chains or modules | 25–40 tasks · 25–45 hrs |
| **3** | **Situational** | For specific target types, environments, or scenarios | 16–24 tasks · 12–22 hrs |
| **4** | **Niche / Reference** | Specialized, post-hire depth, or legacy context | 12–18 tasks · 6–14 hrs |

---

## 🥇 Tier 1 — Core Tools *(10 tools)*

> Must be mastered before advancing. Used on every engagement.

| Tool | What it does | Stage / Module |
| :----- | :------------- | :--------------- |
| [[Netcat\|🔌 Netcat]] | TCP/UDP swiss-army knife — port scanning, file transfer, reverse/bind shells | S1: M04 · S2: M13 |
| [[Wireshark\|🦈 Wireshark]] | Packet capture and deep protocol analysis — live capture and PCAP forensics | S1: M04 |
| [[Nmap\|🗺️ Nmap]] | Network discovery, port scanning, service/OS detection, NSE scripting | S2: M08–09 |
| [[Hashcat\|🔥 Hashcat]] | GPU-accelerated offline password cracking — all hash types and attack modes | S2: M12 |
| [[Hydra\|🔓 Hydra]] | Online password brute-force — SSH, FTP, HTTP, SMB, RDP and more | S2: M12–13 |
| [[LinPEAS\|🐉 LinPEAS]] | Linux privilege escalation enumeration script | S2: M13 |
| [[Metasploit_Framework\|💀 Metasploit Framework]] | Exploitation framework — exploits, payloads, post-exploitation, pivoting | S2: M13 |
| [[Burp_Suite\|🕷️ Burp Suite]] | Web application security testing platform — proxy, scanner, intruder, repeater | S3: M14 |
| [[BloodHound\|🩸 BloodHound]] | AD graph-based attack path analysis — CE (Docker) and Legacy (Neo4j) | S4: M19 |
| [[Impacket\|🐍 Impacket]] | Python AD attack suite — secretsdump, Kerberoast, AS-REP, DCSync, relay | S4: M19 |

---

## 🥈 Tier 2 — Frequent Tools *(43 tools)*

> Used regularly across specific attack chains, modules, or lab setups.

| Tool | What it does | Stage / Module |
| :----- | :------------- | :--------------- |
| [[Scapy\|📦 Scapy]] | Python packet crafting and network manipulation library | S1: M04 · S4: M23 |
| [[tcpdump\|📻 tcpdump]] | CLI packet capture — remote collection, filter syntax, PCAP production | S1: M04 |
| [[Amass\|🌐 Amass]] | OWASP subdomain enumeration — passive, active, API-enriched | S2: M08 |
| [[Maltego\|🕵️ Maltego]] | Visual link analysis and OSINT graph mapping | S2: M08 |
| [[Recon-ng\|🔭 Recon-ng]] | Modular OSINT reconnaissance framework | S2: M08 |
| [[SpiderFoot\|🕸️ SpiderFoot]] | Automated OSINT intelligence gathering — 200+ modules | S2: M08 |
| [[theHarvester\|🌾 theHarvester]] | OSINT email, subdomain, and hostname harvesting | S2: M08 |
| [[Gobuster\|📂 Gobuster]] | Directory, DNS, and virtual host brute-forcing | S2: M10 · S3: M14 |
| [[John_the_Ripper\|🔑 John the Ripper]] | CPU-focused password cracking — exotic formats and incremental modes | S2: M12 |
| [[Chisel\|🔀 Chisel]] | HTTP/HTTPS TCP tunneling and SOCKS5 proxy — firewall-friendly pivoting | S2: M13 · S4: M19 |
| [[Ligolo-ng\|🔀 Ligolo-ng]] | Agent-based network pivoting and tunneling via TUN interface | S2: M13 · S4: M19 |
| [[WinPEAS\|🪟 WinPEAS]] | Windows privilege escalation enumeration script | S2: M13 |
| [[ffuf\|🌀 ffuf]] | Fast web fuzzer — directory, parameter, virtual host, and content discovery | S2: M10 · S3: M14 |
| [[Nuclei\|⚡ Nuclei]] | Template-based vulnerability scanner — 9,000+ community templates | S3: M14–16 |
| [[sqlmap\|💉 sqlmap]] | Automated SQL injection detection and exploitation | S3: M14 |
| [[jwt-tool\|🔐 jwt-tool]] | JWT security testing — algorithm confusion, secret cracking, claim manipulation | S3: M15 |
| [[Nikto\|🔍 Nikto]] | Web server vulnerability scanner — misconfigurations and known CVEs | S3: M16 |
| [[wpscan\|🔌 WPScan]] | WordPress security scanner — plugins, themes, users, vulnerabilities | S3: M16 |
| [[Certipy\|🎫 Certipy]] | Active Directory Certificate Services (ADCS) enumeration and abuse | S4: M19 |
| [[Evil-WinRM\|🪟 Evil-WinRM]] | WinRM post-exploitation shell — PTH, AMSI bypass, in-memory execution | S2: M13 · S4: M19 |
| [[Kerbrute\|🔑 Kerbrute]] | AD username enumeration and password spraying via Kerberos pre-auth | S4: M19 |
| [[Mimikatz\|🐱 Mimikatz]] | Windows in-memory credential dumping — logonpasswords, DCSync, Golden Ticket | S4: M19 |
| [[NetExec\|🌐 NetExec]] | AD credential testing and lateral movement — successor to CrackMapExec (`nxc`) | S4: M19 |
| [[Responder\|📡 Responder]] | LLMNR/NBT-NS/mDNS poisoning — NetNTLMv2 credential capture and relay | S4: M19·23 |
| [[Rubeus\|🎫 Rubeus]] | Windows-native Kerberos attack toolkit — roasting, PTT, delegation abuse | S4: M19 |
| [[Pacu\|☁️ Pacu]] | AWS penetration testing framework — privilege escalation and data exfiltration | S4: M20 |
| [[Prowler\|☁️ Prowler]] | Multi-cloud security assessment, auditing, and hardening tool | S4: M20 |
| [[Bettercap\|🕵️ Bettercap]] | Active network MitM framework — ARP, DNS, HTTPS, BLE, Wi-Fi | S4: M23 |
| [[GoPhish\|🎣 GoPhish]] | Phishing simulation platform — campaigns, tracking, reporting | S4: M24 |
| [[SET\|🎭 SET]] | Social Engineering Toolkit — credential harvesting, payload delivery | S4: M24 |
| [[Sliver\|🐍 Sliver]] | Modern open-source C2 framework — implants, pivoting, armory | S5: M27·29 |
| [[Garak\|🤖 Garak]] | LLM vulnerability scanner and red teaming automation framework | S5: M28 |
| [[Ollama\|🤖 Ollama]] | Local LLM execution framework for offensive & security model testing | S5: M28 |
| [[PyRIT\|🛡️ PyRIT]] | Python Risk Identification Tool for generative AI red teaming | S5: M28 |
| [[Python_AI_SDKs\|🧠 Python AI SDKs]] | Programmatic attack surfaces for LLM APIs, LangChain, and agentic workflows | S5: M28 |
| [[Havoc\|⚔️ Havoc]] | Modern post-exploitation command and control framework | S5: M29 |
| [[Mythic\|🏛️ Mythic]] | Multi-agent collaborative C2 framework | S5: M29 |
| [[Aircrack-ng\|📡 Aircrack-ng]] | Wi-Fi security toolkit — monitor mode, handshake capture, WPA cracking | Shelf: S01 |
| [[Autopsy\|🔍 Autopsy]] | Digital forensics platform — disk image analysis, file recovery, timeline | Shelf: S04 |
| [[FTK_Imager\|💾 FTK Imager]] | Forensic evidence acquisition — disk and memory imaging | Shelf: S04 |
| [[Plaso\|📅 Plaso]] | Super-timeline generation from forensic artifacts — log2timeline | Shelf: S04 |
| [[Volatility\|🧠 Volatility]] | Memory forensics framework — process analysis, network artifacts, malware detection | Shelf: S04 |
| [[Ghidra\|🔬 Ghidra]] | NSA reverse engineering framework — binary analysis, decompilation | Shelf: S05 |
| [[x64dbg\|🐛 x64dbg]] | Windows userland debugger for dynamic malware analysis | Shelf: S05 |

---

## 🥉 Tier 3 — Situational Tools *(27 tools)*

> Reach for these when the target type or scenario demands it.

| Tool | What it does | Stage / Module |
| :----- | :------------- | :--------------- |
| [[Procmon\|🔍 Procmon]] | Windows process monitor — file system, registry, network, process activity | S1: M03 · Shelf: S05 |
| [[OpenSSL\|🔒 OpenSSL]] | TLS handshake inspection, key generation, and certificate verification | S1: M05 |
| [[socat\|🔄 socat]] | Multipurpose bidirectional relay — reverse shells, encrypted tunnels, port forwards | S2: M13 |
| [[OWASP_ZAP\|🛡️ OWASP ZAP]] | Free web application scanner — active scan, spider, fuzzer | S3: M14 |
| [[Postman\|📬 Postman]] | API development and security testing platform | S3: M17 |
| [[SoapUI\|🧼 SoapUI]] | SOAP and REST web services security testing | S3: M17 |
| [[ELK\|🦌 ELK]] | Elasticsearch, Logstash, Kibana open telemetry security data pipeline | S3: Side-Track A |
| [[Sigma\|📜 Sigma]] | Generic signature format for SIEM detection rules | S3: Side-Track A |
| [[Splunk\|🔎 Splunk]] | Enterprise SIEM log ingestion, search processing, and alert creation | S3: Side-Track A |
| [[Sysmon\|📊 Sysmon]] | Advanced Windows event telemetry for process creation and network connections | S3: Side-Track A |
| [[Wazuh\|🛡️ Wazuh]] | Open-source XDR and SIEM host-based monitoring platform | S3: Side-Track A |
| [[YARA\|🔍 YARA]] | Pattern matching swiss knife for malware identification and classification | S3: Side-Track A · Shelf: S05 |
| [[GDB\|🐞 GDB]] | GNU Debugger with GEF/pwndbg extensions for Linux binary exploitation | S5: M27 · Shelf: S06 |
| [[pwntools\|⚡ pwntools]] | CTF framework and exploit development library | S5: M27 · Shelf: S06 |
| [[APKTool\|📦 APKTool]] | Reverse engineering Android APK files — decoding and rebuilding resources | Shelf: S02 |
| [[Frida\|💉 Frida]] | Dynamic instrumentation toolkit for mobile app runtime analysis | Shelf: S02 |
| [[jadx\|🔍 jadx]] | Dex to Java decompiler with GUI for Android APK analysis | Shelf: S02 |
| [[Objection\|📱 Objection]] | Runtime mobile security assessment framework powered by Frida | Shelf: S02 |
| [[Detect_It_Easy\|🔎 Detect It Easy]] | File type, packer, compiler, and protector identification | Shelf: S05 |
| [[PEStudio\|🔬 PEStudio]] | Windows PE file static analysis — imports, strings, entropy, indicators | Shelf: S05 |
| [[strings\|📝 strings]] | Static string extraction from binaries and memory dumps | Shelf: S05 |
| [[Gitleaks\|🔑 Gitleaks]] | Fast secret scanner for Git repositories and files | Shelf: S12–13 |
| [[TruffleHog\|🐽 TruffleHog]] | Deep secret scanner — high-entropy strings and credentials in Git history | Shelf: S12–13 |
| [[Checkov\|🛡️ Checkov]] | Static analysis for infrastructure-as-code (Terraform, Kubernetes) | Shelf: S13 |
| [[Semgrep\|🛡️ Semgrep]] | Fast static analysis engine for bugs and code standard enforcement | Shelf: S13–14 |
| [[tfsec\|⚙️ tfsec]] | Security scanner for Terraform code | Shelf: S13 |

---

## 🏅 Tier 4 — Niche / Reference Tools *(8 tools)*

> Specialized, legacy, or post-hire depth. Know when to reach for them.

| Tool | What it does | Stage / Module |
| :----- | :------------- | :--------------- |
| [[hping3\|🔨 hping3]] | TCP/IP packet crafting — SYN floods, traceroute, firewall testing | S1: M04 · Shelf: S17 |
| [[iperf3\|📶 iperf3]] | Network bandwidth and throughput testing | S1: M04 |
| [[Cookie-Editor\|🍪 Cookie-Editor]] | Browser cookie inspection and manipulation extension | S3: M15 |
| [[Ettercap\|🐛 Ettercap]] | ⚠️ Legacy MitM tool — preserved for protocol fundamentals only | S4: M23 (Legacy) |
| [[ApacheBench\|📊 ApacheBench]] | HTTP load testing and benchmarking tool (`ab`) | Shelf: S17 |
| [[GoldenEye\|💣 GoldenEye]] | HTTP DoS simulation tool — educational use only | Shelf: S17 |
| [[Slowloris\|🐌 Slowloris]] | Slow HTTP DoS tool — connection exhaustion simulation | Shelf: S17 |
| [[wrk\|⚡ wrk]] | Modern HTTP benchmarking with Lua scripting | Shelf: S17 |

---

## 🗺️ Tools by Roadmap Stage

| Stage | Tools |
| :------ | :------ |
| **S1 — Foundation** | [[Wireshark\|Wireshark]] · [[tcpdump\|tcpdump]] · [[Netcat\|Netcat]] · [[OpenSSL\|OpenSSL]] · [[Scapy\|Scapy]] · [[iperf3\|iperf3]] · [[Procmon\|Procmon]] · [[hping3\|hping3]] |
| **S2 — Offense I** | [[Nmap\|Nmap]] · [[Amass\|Amass]] · [[theHarvester\|theHarvester]] · [[Recon-ng\|Recon-ng]] · [[SpiderFoot\|SpiderFoot]] · [[Maltego\|Maltego]] · [[Gobuster\|Gobuster]] · [[Hashcat\|Hashcat]] · [[Hydra\|Hydra]] · [[John_the_Ripper\|John the Ripper]] · [[Metasploit_Framework\|Metasploit]] · [[LinPEAS\|LinPEAS]] · [[WinPEAS\|WinPEAS]] · [[socat\|socat]] · [[Ligolo-ng\|Ligolo-ng]] · [[Chisel\|Chisel]] · [[Evil-WinRM\|Evil-WinRM]] |
| **S3 — Web & App Sec** | [[Burp_Suite\|Burp Suite]] · [[sqlmap\|sqlmap]] · [[ffuf\|ffuf]] · [[Gobuster\|Gobuster]] · [[Nikto\|Nikto]] · [[Nuclei\|Nuclei]] · [[OWASP_ZAP\|OWASP ZAP]] · [[Postman\|Postman]] · [[SoapUI\|SoapUI]] · [[jwt-tool\|jwt-tool]] · [[wpscan\|WPScan]] · [[Cookie-Editor\|Cookie-Editor]] · *Side-Track: [[Splunk\|Splunk]] · [[ELK\|ELK]] · [[Wazuh\|Wazuh]] · [[Sysmon\|Sysmon]] · [[Sigma\|Sigma]] · [[YARA\|YARA]]* |
| **S4 — Enterprise** | [[BloodHound\|BloodHound]] · [[Impacket\|Impacket]] · [[NetExec\|NetExec]] · [[Responder\|Responder]] · [[Evil-WinRM\|Evil-WinRM]] · [[Kerbrute\|Kerbrute]] · [[Certipy\|Certipy]] · [[Mimikatz\|Mimikatz]] · [[Rubeus\|Rubeus]] · [[Pacu\|Pacu]] · [[Prowler\|Prowler]] · [[Bettercap\|Bettercap]] · [[Scapy\|Scapy]] · [[GoPhish\|GoPhish]] · [[SET\|SET]] · [[Ligolo-ng\|Ligolo-ng]] · [[Chisel\|Chisel]] · [[Ettercap\|Ettercap]] |
| **S5 — Specialized** | [[Sliver\|Sliver]] · [[Havoc\|Havoc]] · [[Mythic\|Mythic]] · [[pwntools\|pwntools]] · [[GDB\|GDB]] · [[Ollama\|Ollama]] · [[Python_AI_SDKs\|Python AI SDKs]] · [[Garak\|Garak]] · [[PyRIT\|PyRIT]] |
| **Shelf — Post-Hire** | [[Aircrack-ng\|Aircrack-ng]] (S01) · [[Frida\|Frida]] · [[Objection\|Objection]] · [[jadx\|jadx]] · [[APKTool\|APKTool]] (S02) · [[Volatility\|Volatility]] · [[Autopsy\|Autopsy]] · [[FTK_Imager\|FTK Imager]] · [[Plaso\|Plaso]] (S04) · [[Ghidra\|Ghidra]] · [[x64dbg\|x64dbg]] · [[PEStudio\|PEStudio]] · [[Detect_It_Easy\|Detect It Easy]] · [[strings\|strings]] · [[YARA\|YARA]] (S05) · [[Semgrep\|Semgrep]] · [[Gitleaks\|Gitleaks]] · [[TruffleHog\|TruffleHog]] · [[Checkov\|Checkov]] · [[tfsec\|tfsec]] (S12–14) · [[ApacheBench\|ApacheBench]] · [[wrk\|wrk]] · [[GoldenEye\|GoldenEye]] · [[Slowloris\|Slowloris]] · [[hping3\|hping3]] (S17) |

---

## 📁 Folder Structure

```
Tools/
├── README.md                  ← this file
├── Tier-1_Core/               ← 10 tools
│   └── <Tool>/
│       ├── <Tool>.md          ← structured checklist (do not manually edit curriculum)
│       └── <Tool>_Notes.md    ← your notes (never regenerated or overwritten)
├── Tier-2_Frequent/           ← 43 tools
├── Tier-3_Situational/        ← 27 tools
└── Tier-4_Niche/              ←  8 tools
```

Obsidian resolves wikilinks by unique filename — `[[Nmap]]` always finds `Tier-1_Core/Nmap/Nmap.md` regardless of folder depth. No links break when tools move between tiers.
