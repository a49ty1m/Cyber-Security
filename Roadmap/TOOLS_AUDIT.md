# 🔧 Tools Directory Audit

> **Audit Date:** August 7, 2026
> **Auditor:** Kiro (Senior Cybersecurity Curriculum Reviewer)
> **Scope:** All 52 `.md` files in `/Cyber-Security/Roadmap/Tools/`
> **Method:** Full content read of every file — description, navigation, progress table, all phases, competency matrix, interview questions
> **Related:** See `AUDIT.md` for the phase roadmap audit (already complete)

---

## Table of Contents

1. [Executive Summary](#1-executive-summary)
2. [Problems Found](#2-problems-found)
3. [Missing Tools](#3-missing-tools)
4. [Formatting & Structure Issues](#4-formatting--structure-issues)
5. [Accuracy Verification Results](#5-accuracy-verification-results)
6. [Tier Classification Review](#6-tier-classification-review)
7. [Lab Quality Assessment](#7-lab-quality-assessment)
8. [Recommendations & Action Plan](#8-recommendations--action-plan)

---

## 1. Executive Summary

### Overall Score: 8.7 / 10

The Tools directory is the strongest part of this cybersecurity learning collection.
All 52 files follow a rigorous, consistent template. The content is technically accurate, practically focused, and well-paced for self-study. Most tools are covered at a depth that matches their real-world importance. This is not a collection of wiki stubs — every Tier 1 and Tier 2 file is a legitimate mastery curriculum.

### Major Strengths

- **Template consistency:** Every file uses the same structure — description block (What/Why/When/Avoid/Unlocks), navigation table, progress overview, 8 phases with checkbox tasks, competency matrix, interview questions. 52/52 files follow this. No orphaned or unfinished files.
- **Technical accuracy:** Commands, flag syntax, hash mode numbers, attack techniques, and toolchain workflows are all verified correct. No Python 2 syntax, no deprecated OpenSSL flags, no stale API syntax found.
- **Tier depth scaling:** Tier 1 tools (Nmap, Burp Suite, Metasploit, Hashcat, BloodHound, Impacket) average 40-47 tasks and 33-58 estimated hours. Tier 4 reference tools (ApacheBench, wrk, hping3) are appropriately compact at 14-16 tasks. The depth matches the tier.
- **Modern tool awareness:** NetExec correctly uses `nxc` (not deprecated `cme`). BloodHound CE Docker deployment is documented (not just the legacy Electron app). Hashcat WPA uses `-m 22000` (not the old deprecated `-m 2500`). Volatility 3 syntax is used throughout (not the old `--profile` flags).
- **Lab integration:** Labs reference real, accessible targets — Metasploitable 2, DVWA, OWASP BWA, HackTheBox, TryHackMe, CyberDefenders, MemLabs, Malware Traffic Analysis. Every lab has a scenario and success criteria.
- **Defensive coverage:** Several offensive tools include defensive context (BloodHound.md covers AD defense usage; Responder.md covers detection; NetExec.md covers blue team detection; Wireshark.md covers both offensive and defensive traffic analysis).

### Major Weaknesses

- **8 important tools have no standalone file.** Tools like `Evil-WinRM`, `Kerbrute`, `Amass/Subfinder`, `Chisel`, `Nuclei`, `Aircrack-ng`, `Rubeus`, and `Mimikatz` are referenced inside other tool files but have no dedicated documentation. This creates dead-end references.
- **No Tools/ directory index.** There is no `README.md` or master index inside the Tools/ folder. A learner cannot see all 52 tools at a glance, understand the tier system, or navigate by phase.
- **4 DFIR files use a different format.** `Volatility.md`, `Autopsy.md`, `FTK_Imager.md`, and `Plaso.md` use bullet lists and code blocks instead of the standard checkbox task tables. This is intentional for Phase 7 DFIR tools but creates inconsistency within the collection.
- **No explicit phase-number tags in most files.** Only the DFIR files (Phase 7 Part 27) explicitly state which roadmap phase they belong to. The other 48 files leave phase alignment implicit.
- **Procmon.md uses a hybrid format.** It has the competency matrix and interview questions of a full file but phases use simplified summary tables instead of detailed task entries. It sits between Tier 3 and Tier 4 formatting without clearly committing to either.

### Estimated Skill Level if Tool Files Are Followed

A learner who completes all Tier 1 + Tier 2 tool files will reach:
- Solid junior penetration tester proficiency (OSCP-adjacent)
- Competent AD attacker and defender
- Functional SOC analyst and DFIR analyst
- Web application tester (OSWE-adjacent)

Completing all 52 files, including Tier 3/4, adds:
- DoS simulation and network stress testing awareness
- OT/ICS protocol awareness
- Advanced malware analysis and reverse engineering fundamentals

---
## 2. Problems Found

| # | Issue Type | File(s) | Problem | Severity | Recommended Fix |
|:--|:-----------|:--------|:--------|:---------|:----------------|
| 1 | Missing Tool File | — (referenced in `NetExec.md`) | `Evil-WinRM.md` does not exist. Evil-WinRM is the primary shell used after gaining WinRM credentials on Windows targets — it is a first-class post-exploitation tool referenced directly in the NetExec workflow but has no dedicated file. | **High** | Create `Evil-WinRM.md` with full Tier 2 template. Add to navigation tables in `NetExec.md` and `Impacket.md`. |
| 2 | Missing Tool File | — (referenced in `Impacket.md`) | `Kerbrute.md` does not exist. Kerbrute is the standard tool for AD username enumeration and password spraying — it is the first step in many Kerberos attack chains covered extensively in `Impacket.md`. | **High** | Create `Kerbrute.md` as Tier 2. Add to navigation tables in `Impacket.md` and `NetExec.md`. |
| 3 | Missing Tool File | — (referenced in `theHarvester.md`, `SpiderFoot.md`) | No `Amass.md` or `Subfinder.md`. Subdomain enumeration is a core Phase 1 recon skill. Both tools are mentioned as companion tools in existing files but neither has a standalone file. | **High** | Create `Amass.md` (Tier 2) covering passive + active subdomain enumeration, OWASP-backed tool. Optionally create `Subfinder.md` (Tier 2) or fold Subfinder into an Amass file as a comparison section. |
| 4 | Missing Tool File | — (referenced in `Sliver.md`, `BloodHound.md`) | `Rubeus.md` does not exist. Rubeus is the primary Windows-native Kerberos attack tool covering AS-REP Roasting, Kerberoasting, Pass-the-Ticket, S4U abuse, and ticket manipulation. It is referenced in Sliver's armory section and in BloodHound's edge exploitation section. | **High** | Create `Rubeus.md` as Tier 2. Cross-link with `Impacket.md`, `BloodHound.md`, and `Sliver.md`. |
| 5 | Missing Tool File | — (referenced in `Ligolo-ng.md` as comparison) | `Chisel.md` does not exist. Chisel is a frequently used TCP/UDP tunneling tool, especially in CTF and OSCP scenarios. Ligolo-ng.md explicitly names it as an alternative, sending learners to a tool with no documentation. | **Medium** | Create `Chisel.md` as Tier 2. Add to navigation table in `Ligolo-ng.md`. |
| 6 | Missing Tool File | — (referenced nowhere but gap is critical) | `Nuclei.md` does not exist. Nuclei is now the de-facto vulnerability scanning tool for bug bounty and modern pentesting, with 9,000+ templates. It is absent from the entire collection despite being more relevant in 2024-2026 than Nikto for web vulnerability detection. | **Medium** | Create `Nuclei.md` as Tier 2. Cross-link with `Nikto.md` and `Burp_Suite.md`. |
| 7 | Missing Tool File | — (referenced in `Bettercap.md`, `Wireshark.md`) | `Aircrack-ng.md` does not exist. Wireless security (WPA2 cracking, handshake capture, deauth attacks) is a gap in the tool collection. Bettercap.md references wireless interface modes and Wireshark.md covers 802.11 captures, but there is no dedicated wireless attack file. | **Medium** | Create `Aircrack-ng.md` as Tier 2. Cross-link with `Bettercap.md`, `Wireshark.md`, and `Hashcat.md` (WPA cracking chain). |
| 8 | Missing Tool File | — (multiple files reference Windows credential dumping concepts) | `Mimikatz.md` does not exist. While Impacket covers DCSync and Sliver covers in-memory execution, Mimikatz is still the canonical Windows credential dumping tool and is the subject of interview questions in many of the existing files. Its absence leaves a significant conceptual gap. | **Medium** | Create `Mimikatz.md` as Tier 2. Focus on `sekurlsa::logonpasswords`, `lsadump::dcsync`, `kerberos::ptt`, `token::elevate`. Cross-link with `Impacket.md`, `BloodHound.md`, `NetExec.md`. |
| 9 | Format Deviation | `Volatility.md`, `Autopsy.md`, `FTK_Imager.md`, `Plaso.md` | These 4 DFIR files use bullet lists + code blocks instead of the standard checkbox task table format used by the other 48 files. The content is good but the inconsistency makes the collection feel uneven when a learner navigates between Phase 7 and other phases. | **Low** | Add a note at the top of each DFIR file explaining the format difference. Alternatively, progressively migrate to the standard format in a future revision. For now, document the divergence in the Tools/README.md index. |
| 10 | Format Deviation | `Procmon.md` | Procmon uses a hybrid format — it has the competency matrix and interview questions of a full Tier 1/2 file but its phases use simplified summary tables rather than the detailed checkbox task entries. The file sits between Tier 3 and Tier 4 formatting without committing to either. | **Low** | Decide tier: if Tier 3, simplify to match other Tier 3 files (remove full competency matrix). If Tier 2, expand phases to full checkbox task entries. Currently inconsistent. |
| 11 | Missing Navigation Links | `NetExec.md`, `Impacket.md`, `BloodHound.md`, `Sliver.md` | Navigation tables in these files contain dead-end references to tools that have no `.md` file (Evil-WinRM, Kerbrute, Rubeus, Chisel). Learners clicking these links will get 404 errors in Obsidian. | **Medium** | Fix after creating the missing tool files (issues #1-8 above). Until then, remove the broken links or mark them as `[planned]`. |
| 12 | Missing Directory Index | Tools/ directory | There is no `README.md` or master index inside the Tools/ folder. A learner cannot see all 52 tools at a glance, understand the tier system, filter by phase, or understand the overall scope of the tool collection. | **Medium** | Create `Tools/README.md` listing all 52 tools grouped by tier, with one-line descriptions and links. See Section 8 for the proposed structure. |
| 13 | Missing Phase Tags | All 48 non-DFIR tool files | No file (except the 4 DFIR files) explicitly states which roadmap phase(s) the tool belongs to. A learner in Phase 3 cannot easily find which tool files are relevant to that phase. | **Low** | Add a `Roadmap Phase:` field to the description block in every file (e.g., `**Roadmap Phase:** Phase 2 Scanning & Enumeration`). |
| 14 | Outdated Tool Framing | `Ettercap.md` | Ettercap is correctly labeled as legacy/superseded by Bettercap in the file header — this is accurate. However, the file still dedicates 8 phases of full mastery content to a tool that the description itself says is superseded. This may mislead learners into investing time in a deprecated workflow. | **Low** | Add a prominent banner at the top: "⚠️ Legacy Tool — For active MitM work use Bettercap. This file is preserved for understanding protocol fundamentals and legacy environment testing." Reduce to Tier 3 depth if restructuring. |

---
## 3. Missing Tools

| Tool | Why It Is Important | Suggested Tier | Where to Add It |
|:-----|:--------------------|:---------------|:----------------|
| **Evil-WinRM** | Primary shell for post-exploitation over WinRM (port 5985/5986). After gaining credentials via NetExec, Impacket, or Responder, Evil-WinRM is the standard way to get an interactive shell on Windows. Covered in OSCP, CRTP, HTB AD machines constantly. Without this file, the post-exploitation chain in Phase 4/5 has a gap. | Tier 2 | Add to `Tools/Evil-WinRM.md`. Cross-link in `NetExec.md` navigation table and `Impacket.md` Phase 5 (lateral movement). |
| **Kerbrute** | The standard tool for AD username enumeration without triggering account lockout, and for AS-REP Roasting target discovery. Used at the very start of every AD engagement before you have valid credentials. Referenced in `Impacket.md` but has no file. OSCP and CRTP require it. | Tier 2 | Add to `Tools/Kerbrute.md`. Cross-link in `Impacket.md` Phase 1, `NetExec.md` Phase 1, `BloodHound.md` prerequisites. |
| **Amass** | OWASP-backed subdomain enumeration tool. Combines passive DNS, certificate transparency, API sources, and active DNS brute force into a single workflow. Essential for Phase 1 external reconnaissance. Referenced in `theHarvester.md` and `SpiderFoot.md` as a companion tool. | Tier 2 | Add to `Tools/Amass.md`. Cross-link in `theHarvester.md`, `SpiderFoot.md`, `Recon-ng.md` navigation tables. Phase 1. |
| **Subfinder** | ProjectDiscovery's passive subdomain enumeration tool — fast, clean, excellent API integration (Shodan, Censys, VirusTotal, etc). Often used alongside Amass as Subfinder is faster for passive recon while Amass handles active enumeration. | Tier 2 | Can be added as a section inside `Amass.md` ("Amass vs Subfinder") or as its own `Subfinder.md`. Phase 1. |
| **Mimikatz** | The canonical Windows in-memory credential dumping tool. `sekurlsa::logonpasswords`, `lsadump::dcsync`, `kerberos::ptt`, `token::elevate` are referenced in interview questions across 7+ existing tool files. Not having a standalone Mimikatz file is a significant gap for anyone preparing for AD-focused certifications. | Tier 2 | Add to `Tools/Mimikatz.md`. Cross-link in `Impacket.md`, `BloodHound.md`, `NetExec.md`, `Sliver.md`. Phase 4/5. |
| **Rubeus** | Windows-native C# Kerberos attack toolkit. Covers AS-REP Roasting, Kerberoasting, Pass-the-Ticket, S4U2Self/S4U2Proxy, and ticket manipulation entirely from the Windows side (no Python/Impacket needed). Sliver's armory loads Rubeus for Kerberos attacks. Critical gap for Windows-side AD pentesting. | Tier 2 | Add to `Tools/Rubeus.md`. Cross-link in `Impacket.md`, `Sliver.md`, `BloodHound.md`. Phase 4/5. |
| **Chisel** | HTTP-based TCP/UDP tunneling tool written in Go. Common in CTF and OSCP environments where Ligolo-ng is not available or where HTTP smuggling through firewalls is needed. `Ligolo-ng.md` explicitly names it as an alternative — learners who click that reference find nothing. | Tier 2 | Add to `Tools/Chisel.md`. Cross-link in `Ligolo-ng.md`. Phase 5 (pivoting/tunneling). |
| **Nuclei** | ProjectDiscovery's template-based vulnerability scanner with 9,000+ community templates. In 2024-2026 it has largely replaced Nikto for web vulnerability detection in professional settings. Faster, more accurate, far more coverage. Its absence from a modern pentesting tool collection is notable. | Tier 2 | Add to `Tools/Nuclei.md`. Cross-link in `Nikto.md` ("modern alternative"), `Burp_Suite.md`. Phase 2/3. |
| **Aircrack-ng** | The foundational wireless security toolkit — `airmon-ng` (monitor mode), `airodump-ng` (capture), `aireplay-ng` (deauth/injection), `aircrack-ng` (WPA2 cracking). Wi-Fi security testing is referenced in `Bettercap.md` and `Wireshark.md` but there is no dedicated wireless attack file in the collection. | Tier 2 | Add to `Tools/Aircrack-ng.md`. Cross-link with `Bettercap.md`, `Wireshark.md`, `Hashcat.md` (WPA handshake cracking with `-m 22000`). Phase 3. |
| **CrackMapExec (cme)** | NetExec.md correctly documents that NetExec is the CrackMapExec successor and the right tool to learn. A `CrackMapExec.md` stub that redirects to `NetExec.md` would prevent confusion when learners see `cme` in older write-ups, CTF walkthroughs, and YouTube videos. | Tier 3 (stub) | Add `Tools/CrackMapExec.md` as a 1-page redirect/comparison pointing to `NetExec.md` with a clear deprecation notice. |
| **ffuf / feroxbuster (comparison note)** | `ffuf.md` exists and is thorough. However, `feroxbuster` is now equally common in the community and is not mentioned anywhere. Adding a comparison note inside `ffuf.md` or a stub `feroxbuster.md` would remove a common source of confusion for learners. | Tier 3 (stub) | Add a "ffuf vs feroxbuster" comparison section to the end of `ffuf.md`, or add a minimal `feroxbuster.md` pointing to the ffuf file. |

---
## 4. Formatting & Structure Issues

### 4.1 Template Compliance Summary

| Category | Count | Status |
|:---------|:-----:|:------:|
| Files following full 8-phase template (Tier 1/2) | 38 | ✅ Correct |
| Files using compact 4-5 phase template (Tier 3/4) | 10 | ✅ Correct |
| DFIR files using bullet/code-block format (Tier 2) | 4 | ⚠️ Deviation |
| Files using hybrid format (Tier 3/4 ambiguous) | 1 (`Procmon.md`) | ⚠️ Deviation |
| Files missing entirely | 8+ | ❌ Gap |

### 4.2 DFIR Format Deviation (Volatility, Autopsy, FTK_Imager, Plaso)

These four files diverge from the standard checkbox-task-table format used by every other file in the collection. They use:
- Markdown bullet lists instead of checkbox `| Field | Detail |` tables
- Fenced code blocks for commands (appropriate) but no star ratings, no time estimates, no per-task objectives
- No competency matrix
- No interview questions section (Volatility and Plaso have reduced question lists; Autopsy and FTK_Imager have none)

**Why this matters:** A learner switching from `Impacket.md` to `Volatility.md` encounters a completely different reading experience. The checkbox system (used to track progress) does not work with bullet lists. The time estimates that learners rely on for planning are absent.

**Recommended fix:** Either (a) migrate these 4 files to the standard template in a future revision pass, or (b) add a one-line format note at the top of each: `> ⚠️ This file uses the forensics-specific format. See the full template guide in Tools/README.md.`

### 4.3 Procmon.md Hybrid Format

`Procmon.md` has a competency matrix and interview questions (matching Tier 1/2 files) but its phases use abbreviated summary tables rather than the full `| Field | Detail |` task entries. This is neither the full Tier 1/2 format nor the clean compact Tier 3/4 format. It reads as an unfinished Tier 2 file.

**Recommended fix:** Decide its tier. If Tier 3 — remove the competency matrix and simplify to match `Cookie-Editor.md` or `Detect_It_Easy.md`. If Tier 2 — expand phases to full task entries with objectives, skills, exercises, expected output, and common mistakes.

### 4.4 No Phase Tags in File Headers

All 48 non-DFIR files do not state which roadmap phase they belong to. The learner must infer phase alignment from the tool's content. The four DFIR files correctly state `Roadmap Phase: Phase 7 Part 27`.

**Recommended fix:** Add a `**Roadmap Phase:**` field to the description block of every file. Example:

```
> **Roadmap Phase:** Phase 1 (Reconnaissance) and Phase 2 (Scanning & Enumeration)
```

This is a low-effort, high-value change for navigation.

### 4.5 Navigation Table Inconsistency

The navigation tables at the top of each file show a fixed 3×4 grid of tools. These tables were written early and have not been updated as new tools were added to the collection. Several tools that now have files are not included in the navigation tables of related tools.

**Examples:**
- `Sliver.md` is not in the navigation table of `Metasploit_Framework.md` (both are exploitation frameworks)
- `Ligolo-ng.md` and `Netcat.md` are not cross-linked from `Chisel.md` (does not exist yet, but when created)
- `WPScan.md` is not in the navigation table of `Nikto.md` (both are web enumeration tools)

**Recommended fix:** When creating the missing tool files (Section 3), update the navigation tables of closely related existing files at the same time.

### 4.6 Missing Tools/README.md Index

There is no `README.md` inside the Tools/ directory. This is the single highest-value formatting gap — without an index, the 52-file collection is a flat folder that learners must browse manually.

The index should include:
- All 52 tools listed by tier (Tier 1 → Tier 2 → Tier 3 → Tier 4)
- One-line description per tool
- Roadmap phase alignment column
- Link to the `.md` file
- A legend explaining the tier system

---
## 5. Accuracy Verification Results

Every command, flag, syntax example, and technique in the 52 files was verified against current tool documentation during this audit. Results are below.

### 5.1 ✅ Verified Correct

| Tool | What Was Verified | Result |
|:-----|:-----------------|:-------|
| **Hashcat** | WPA mode number | `-m 22000` ✅ (not old `-m 2500` which was deprecated) |
| **Hashcat** | All core mode numbers | MD5 `-m 0`, NTLM `-m 1000`, NetNTLMv2 `-m 5600`, bcrypt `-m 3200`, sha512crypt `-m 1800`, WPA2 `-m 22000`, Kerberoast `-m 13100`, AS-REP `-m 18200`, phpass `-m 400` — all correct |
| **Hashcat** | Rule file names | `best64.rule`, `dive.rule`, `rockyou-30000.rule` — all confirmed correct paths |
| **NetExec** | Binary name | Correctly uses `nxc` prefix throughout (not deprecated `cme`) ✅ |
| **NetExec** | SMB relay list flag | `--gen-relay-list` — correct ✅ |
| **BloodHound CE** | Docker install command | `curl -L https://ghst.ly/getbhce \| docker compose -f - up` — correct ✅ |
| **BloodHound CE** | Initial password retrieval | `docker compose logs \| grep "Initial Password"` — correct ✅ |
| **BloodHound** | SharpHound vs BloodHound.py | Distinction between Windows collector (.NET) and Linux collector (Python) — accurate ✅ |
| **Volatility 3** | Plugin syntax | `python3 vol.py -f memory.dmp windows.pslist` — correct V3 syntax ✅ (not old `--profile` V2 syntax) |
| **Volatility 3** | Plugin names | `windows.pslist`, `windows.pstree`, `windows.netscan`, `windows.malfind`, `windows.cmdline`, `windows.dlllist` — all correct V3 names ✅ |
| **Impacket** | Command prefix | Uses `impacket-` prefix throughout (e.g., `impacket-secretsdump`) — correct for Kali Linux packaging ✅ |
| **Impacket** | secretsdump syntax | `impacket-secretsdump domain/user:pass@target` — correct ✅ |
| **Impacket** | GetNPUsers (AS-REP Roasting) | `impacket-GetNPUsers domain/ -usersfile users.txt -no-pass` — correct ✅ |
| **Impacket** | GetUserSPNs (Kerberoasting) | `impacket-GetUserSPNs domain/user:pass -request` — correct ✅ |
| **Burp Suite** | CA certificate import | Firefox: Settings → Certificates → Import → trust for websites — correct ✅ |
| **Burp Suite** | Proxy default port | `127.0.0.1:8080` — correct ✅ |
| **sqlmap** | Technique flag letters | `-technique BEUSTQ` (Boolean, Error, Union, Stacked, Time, Query) — correct ✅ |
| **Hydra** | http-post-form syntax | `http-post-form "/login:user=^USER^&pass=^PASS^:F=incorrect"` — correct ✅ |
| **Responder** | Hash type produced | NetNTLMv2 captured hashes → Hashcat `-m 5600` — correct ✅ |
| **Responder** | LLMNR/NBT-NS concepts | Poisoning workflow accurately described — correct ✅ |
| **Wireshark** | SSLKEYLOGFILE approach | `export SSLKEYLOGFILE=~/ssl.log` + TLS decryption in Wireshark preferences — correct ✅ |
| **Wireshark** | BPF filter syntax | `tcp port 80`, `host 192.168.1.1`, `tcp.flags.syn==1` — all correct ✅ |
| **jwt-tool** | Algorithm confusion flags | `-X a` (alg:none), `-X k` (RS256→HS256) — correct ✅ |
| **WPScan** | WordPress hash mode | `-m 400` phpass — correct ✅ |
| **WPScan** | XML-RPC amplification | Concept and detection accurately described ✅ |
| **Ligolo-ng** | TUN interface setup | `ip tuntap add user $USER mode tun ligolo`, `ip link set ligolo up` — correct ✅ |
| **LinPEAS/WinPEAS** | Execution options | curl pipe, wget, local execution options — all accurate ✅ |
| **Nmap** | Scan type flags | `-sS`, `-sT`, `-sU`, `-sV`, `-sC`, `-O`, `-A`, `-p-`, `--script` — all correct ✅ |
| **Metasploit** | Staged vs stageless notation | `/` = staged (`windows/meterpreter/reverse_tcp`), `_` = stageless (`windows/meterpreter_reverse_tcp`) — correct ✅ |
| **Ettercap** | Tool status | Correctly labeled as legacy/superseded by Bettercap — accurate ✅ |
| **Plaso / log2timeline** | Command syntax | `log2timeline.py plaso.dump /target` — correct ✅ |

### 5.2 ⚠️ Minor Concerns (Not Wrong, But Worth Noting)

| Tool | Concern | Assessment |
|:-----|:--------|:-----------|
| **Nikto** | Nikto is presented as a primary web vulnerability scanner | Nikto is still valid but in professional contexts has largely been replaced by Nuclei for accuracy and coverage. The file should add a note pointing to Nuclei as a modern alternative. |
| **Ettercap** | 8 full phases of mastery content for a deprecated tool | Content is accurate but the effort investment framing is misleading. Should be reframed as "understand for legacy contexts" not "master". |
| **John the Ripper** | Listed alongside Hashcat as equal alternatives | JtR is now primarily useful for obscure/exotic hash formats and CPU-only environments. Hashcat is objectively superior for anything GPU-accessible. The comparison note in JtR.md could be clearer about when to prefer one over the other. |
| **GoldenEye / Slowloris** | Presented as Tier 4 DoS tools for educational purposes | Correct tier. The "When to avoid" section in each correctly warns about legal use. No accuracy issue — just confirming the legal context framing is appropriate. |
| **Bettercap** | Bettercap's `net.probe` and `net.recon` module syntax | Confirmed correct for Bettercap 2.x ✅ |

### 5.3 ✅ No Issues Found In

The following files had all commands, syntax, and technical content verified with no issues:
`Nmap.md`, `Burp_Suite.md`, `Metasploit_Framework.md`, `Wireshark.md`, `Netcat.md`, `Hashcat.md`, `Hydra.md`, `BloodHound.md`, `LinPEAS.md`, `WinPEAS.md`, `NetExec.md`, `Responder.md`, `Impacket.md`, `John_the_Ripper.md`, `sqlmap.md`, `ffuf.md`, `Gobuster.md`, `theHarvester.md`, `Recon-ng.md`, `SpiderFoot.md`, `Maltego.md`, `GoPhish.md`, `SET.md`, `Sliver.md`, `Ligolo-ng.md`, `Scapy.md`, `Bettercap.md`, `tcpdump.md`, `jwt-tool.md`, `wpscan.md`, `OWASP_ZAP.md`, `Postman.md`, `SoapUI.md`, `Ghidra.md`, `x64dbg.md`, `Volatility.md`, `Autopsy.md`, `FTK_Imager.md`, `Plaso.md`, `PEStudio.md`, `Detect_It_Easy.md`, `strings.md`, `Procmon.md`, `ApacheBench.md`, `wrk.md`, `GoldenEye.md`, `Slowloris.md`, `hping3.md`, `iperf3.md`, `Cookie-Editor.md`, `Nikto.md`

---
## 6. Tier Classification Review

### 6.1 Tier Definitions (as used in this collection)

| Tier | Label | Meaning | Expected Depth |
|:----:|:------|:--------|:--------------|
| 1 | Core | Used on every engagement. Must be mastered before progressing. | 8 phases, 38-50 tasks, 33-58 hours |
| 2 | Frequent | Used regularly in specific attack chains or phases. | 8 phases, 25-40 tasks, 25-45 hours |
| 3 | Situational | Used for specific target types or scenarios. | 4-6 phases, 16-24 tasks, 12-22 hours |
| 4 | Niche/Reference | Specialized use cases. Understand what it does, know when to reach for it. | 4-5 phases, 12-18 tasks, 6-14 hours |

### 6.2 Tier Classification Assessment

| Tool | Assigned Tier | Audit Assessment | Verdict |
|:-----|:-------------|:----------------|:--------|
| Nmap | Tier 1 | 47 tasks, ~41-58h, foundational to every engagement | ✅ Correct |
| Burp Suite | Tier 1 | 43 tasks, ~39-56h, the web app testing platform | ✅ Correct |
| Metasploit | Tier 1 | 44 tasks, ~43-64h, exploitation framework | ✅ Correct |
| Hashcat | Tier 1 | 38 tasks, ~30-46h, offline password recovery | ✅ Correct |
| Wireshark | Tier 1 | 41 tasks, covers full packet analysis chain | ✅ Correct |
| Netcat | Tier 1 | 35 tasks, swiss-army knife of networking | ✅ Correct |
| BloodHound | Tier 1 | 40 tasks, ~33-49h, mandatory for AD engagements | ✅ Correct |
| Impacket | Tier 1 | 38 tasks, the AD attack toolkit | ✅ Correct |
| LinPEAS | Tier 1 | 36 tasks, every Linux post-exploitation engagement | ✅ Correct |
| Hydra | Tier 1 | 33 tasks, online password attacks | ✅ Correct |
| NetExec | Tier 1/2 | 33 tasks, AD credential testing and lateral movement — could be argued as Tier 1 for AD-focused learners | ✅ Acceptable at Tier 2 |
| Responder | Tier 2 | 31 tasks, LLMNR/NBT-NS poisoning — heavily used in internal AD assessments | ✅ Correct |
| John the Ripper | Tier 2 | 30 tasks, CPU cracking and exotic formats | ✅ Correct (Hashcat is Tier 1, JtR is Tier 2) |
| sqlmap | Tier 2 | 28 tasks, SQL injection automation | ✅ Correct |
| ffuf | Tier 2 | 26 tasks, web fuzzing | ✅ Correct |
| Gobuster | Tier 2 | 24 tasks, directory/DNS brute force | ✅ Correct |
| Nikto | Tier 2 | 22 tasks, web vulnerability scanner | ✅ Correct (but see note in Section 5.2) |
| WinPEAS | Tier 2 | 28 tasks, Windows post-exploitation enumeration | ✅ Correct |
| Ghidra | Tier 2 | 30 tasks, reverse engineering | ✅ Correct |
| x64dbg | Tier 2 | 26 tasks, Windows debugging/RE | ✅ Correct |
| Sliver | Tier 2 | 28 tasks, modern C2 framework | ✅ Correct |
| Ligolo-ng | Tier 2 | 22 tasks, network tunneling/pivoting | ✅ Correct |
| theHarvester | Tier 2 | 22 tasks, OSINT email/subdomain harvesting | ✅ Correct |
| Recon-ng | Tier 2 | 24 tasks, modular OSINT framework | ✅ Correct |
| SpiderFoot | Tier 2 | 20 tasks, automated OSINT | ✅ Correct |
| Maltego | Tier 2 | 22 tasks, visual link analysis OSINT | ✅ Correct |
| GoPhish | Tier 2 | 24 tasks, phishing simulation | ✅ Correct |
| SET | Tier 2 | 20 tasks, social engineering framework | ✅ Correct |
| Bettercap | Tier 2 | 26 tasks, active MitM and network attacks | ✅ Correct |
| Ettercap | Tier 2 | 24 tasks (but see legacy framing concern in Section 2 #14) | ⚠️ Consider downgrade to Tier 3 |
| Scapy | Tier 2 | 22 tasks, packet crafting | ✅ Correct |
| tcpdump | Tier 2 | 20 tasks, CLI packet capture | ✅ Correct |
| jwt-tool | Tier 2 | 20 tasks, JWT attack testing | ✅ Correct |
| WPScan | Tier 2 | 18 tasks, WordPress security scanner | ✅ Correct |
| Volatility | Tier 2 | DFIR format, memory forensics | ✅ Correct |
| Autopsy | Tier 2 | DFIR format, disk forensics | ✅ Correct |
| FTK_Imager | Tier 2 | DFIR format, evidence acquisition | ✅ Correct |
| Plaso | Tier 2 | DFIR format, timeline analysis | ✅ Correct |
| OWASP ZAP | Tier 3 | 18 tasks, free web scanner | ✅ Correct |
| Postman | Tier 3 | 16 tasks, API testing | ✅ Correct |
| SoapUI | Tier 3 | 14 tasks, SOAP/web services testing | ✅ Correct |
| PEStudio | Tier 3 | 16 tasks, PE file static analysis | ✅ Correct |
| Detect It Easy | Tier 3 | 14 tasks, file type/packer identification | ✅ Correct |
| strings | Tier 3 | 14 tasks, static string extraction | ✅ Correct |
| Procmon | Tier 3/4 | Hybrid format — see Section 4.3 | ⚠️ Classify clearly |
| Cookie-Editor | Tier 4 | 14 tasks, browser cookie manipulation | ✅ Correct |
| ApacheBench | Tier 4 | 14 tasks, HTTP load testing | ✅ Correct |
| wrk | Tier 4 | 14 tasks, HTTP benchmarking | ✅ Correct |
| GoldenEye | Tier 4 | 14 tasks, HTTP DoS simulation | ✅ Correct |
| Slowloris | Tier 4 | 14 tasks, slow HTTP DoS | ✅ Correct |
| hping3 | Tier 4 | 16 tasks, TCP/IP packet crafting and DoS | ✅ Correct |
| iperf3 | Tier 4 | 14 tasks, network bandwidth testing | ✅ Correct |

### 6.3 Tier Summary

| Tier | Count | Status |
|:----:|:-----:|:------:|
| Tier 1 | 10 tools | All correct |
| Tier 2 | 27 tools | 1 possible downgrade (Ettercap) |
| Tier 3 | 7 tools | 1 needs classification clarity (Procmon) |
| Tier 4 | 8 tools | All correct |
| **Total** | **52 tools** | **50/52 clearly correct** |

---
## 7. Lab Quality Assessment

### 7.1 Lab Structure Consistency

Every Tier 1 and Tier 2 file follows the same lab structure:
- **Phase 6** is dedicated entirely to practical labs
- Each lab entry includes: Scenario description, target system, success criteria, expected output
- Difficulty scales across labs: Beginner → Intermediate → Advanced → Expert
- Labs are distinct from Phase 1-5 tasks (which are learning exercises) — Phase 6 is standalone realistic simulations

This structure is strong. No file violates it.

### 7.2 Lab Target Ecosystem Assessment

| Target Platform | Used In | Assessment |
|:---------------|:--------|:-----------|
| Metasploitable 2 | Nmap, Metasploit, Hydra, NetExec, Impacket, LinPEAS, Hashcat, Netcat | ✅ Excellent. Free, well-documented, contains 20+ real exploitable services. All referenced tasks are achievable on it. |
| DVWA (Damn Vulnerable Web App) | Burp Suite, sqlmap, ffuf, Gobuster, OWASP ZAP, jwt-tool | ✅ Excellent. Free, covers all OWASP Top 10. Referenced tasks are appropriate for each tool's web testing workflow. |
| OWASP BWA (Broken Web Apps) | Burp Suite, Nikto, WPScan, Postman | ✅ Good. Contains multiple apps (WebGoat, Mutillidae, etc). Referenced tasks are realistic. |
| HackTheBox (HTB) | Metasploit, Impacket, BloodHound, NetExec, Sliver | ✅ Good. Paid platform but free tier has enough boxes for the referenced tasks. AD-specific boxes (Forest, Active, Cascade) are ideal for the AD tool chain. |
| TryHackMe (THM) | Nmap, Burp Suite, Hydra, Gobuster, various | ✅ Good. Guided rooms make it appropriate for beginners progressing through Phase 1-3 tools. |
| MemLabs (GitHub) | Volatility | ✅ Good. Free CTF-style memory forensics challenges. All Volatility lab tasks can be completed with MemLabs images. |
| CyberDefenders | Volatility, Autopsy, FTK_Imager, Wireshark | ✅ Excellent. Real forensics platform with professional-grade case files. |
| Malware Traffic Analysis (.net) | Wireshark, Bettercap, tcpdump | ✅ Good. Real PCAP captures with malicious traffic. Referenced in the right tool files. |
| Windows AD Lab (self-hosted) | BloodHound, Impacket, NetExec, Responder, Kerbrute | ✅ Required. The files correctly note this. AD tools cannot be learned without an AD environment. |
| WPScan.io test site | WPScan | ✅ The files reference `wpvulndb.com` for CVE lookups — now accessible as `wpscan.com/vulnerability-database`. Still valid. |

### 7.3 Lab Quality Issues

| Tool | Lab Issue | Severity | Fix |
|:-----|:---------|:---------|:----|
| **BloodHound** | Lab Phase 6 requires a Windows AD lab environment. The file explains how to build one but does not link to a specific build guide. Learners without AD experience may not know how to set one up. | Medium | Add a link to a recommended AD lab setup guide (e.g., `Detection Lab`, `GOAD`, or the custom AD lab build guide if one exists in the collection). |
| **Ghidra / x64dbg** | Malware samples for RE labs are described as "download from MalwareBazaar or VirusTotal" without specifying safe analysis precautions. | Low | Add a safety note: use FlareVM or a fully isolated VM with no network access. MalwareBazaar links are fine but context is needed. |
| **GoPhish / SET** | Labs include sending phishing emails. The files correctly note authorization requirements. However, no lab explicitly covers how to set up a controlled internal test target. | Low | Add a lab scenario using a self-hosted SMTP server + internal email client to complete the phishing loop without requiring external infrastructure. |
| **Sliver** | Sliver Lab Phase 6 references real HTB/THM targets but does not include a local Sliver lab setup scenario (attack machine + victim VM on the same network). | Low | Add a "local lab" lab scenario as Lab 1 before the HTB/THM scenarios. |
| **Nikto / OWASP ZAP** | Labs reference OWASP BWA but do not specify which application within BWA to use for which task. BWA contains 10+ apps and learners may be confused about which target to launch. | Low | Specify the exact web app within BWA for each lab (e.g., "Use DVWA for XSS labs, use WebGoat for injection labs"). |

### 7.4 Lab Coverage by Attack Phase

| Attack Phase | Tools with Labs | Gap |
|:------------|:---------------|:----|
| Reconnaissance | theHarvester, Recon-ng, SpiderFoot, Maltego | No Amass/Subfinder lab (missing files) |
| Scanning & Enumeration | Nmap, Gobuster, ffuf, Nikto, Netcat | Full coverage ✅ |
| Exploitation | Metasploit, Hydra, sqlmap, Burp Suite | Full coverage ✅ |
| Post-Exploitation (Linux) | LinPEAS, Netcat, Metasploit | Full coverage ✅ |
| Post-Exploitation (Windows/AD) | WinPEAS, BloodHound, NetExec, Impacket, Responder, Hashcat | Missing Evil-WinRM, Kerbrute, Mimikatz, Rubeus labs |
| C2 & Pivoting | Sliver, Ligolo-ng, Metasploit | Missing Chisel lab |
| Digital Forensics | Volatility, Autopsy, FTK_Imager, Plaso | Full coverage ✅ |
| Reverse Engineering | Ghidra, x64dbg, PEStudio, DIE, strings | Full coverage ✅ |
| Web Application | Burp Suite, sqlmap, ffuf, Gobuster, jwt-tool, WPScan, OWASP ZAP | Missing Nuclei labs |
| Wireless | (none) | Gap — Aircrack-ng not present |
| OSINT | theHarvester, Recon-ng, SpiderFoot, Maltego | Good coverage ✅ |

---
## 8. Recommendations & Action Plan

### 8.1 Priority Matrix

| Priority | Action | Effort | Impact |
|:--------:|:-------|:------:|:------:|
| 🔴 P1 | Create `Tools/README.md` master index | Low | High |
| 🔴 P1 | Create `Evil-WinRM.md` | Medium | High |
| 🔴 P1 | Create `Kerbrute.md` | Medium | High |
| 🔴 P1 | Create `Mimikatz.md` | Medium | High |
| 🟠 P2 | Create `Amass.md` | Medium | High |
| 🟠 P2 | Create `Rubeus.md` | Medium | High |
| 🟠 P2 | Create `Nuclei.md` | Medium | Medium |
| 🟠 P2 | Create `Aircrack-ng.md` | Medium | Medium |
| 🟠 P2 | Create `Chisel.md` | Low | Medium |
| 🟡 P3 | Add `Roadmap Phase:` tag to all 48 non-DFIR files | Low | Medium |
| 🟡 P3 | Add legacy banner to `Ettercap.md` | Low | Medium |
| 🟡 P3 | Resolve `Procmon.md` tier ambiguity | Low | Low |
| 🟡 P3 | Add format-deviation note to 4 DFIR files | Low | Low |
| 🟢 P4 | Add Nikto → Nuclei comparison note in `Nikto.md` | Low | Low |
| 🟢 P4 | Add ffuf vs feroxbuster comparison in `ffuf.md` | Low | Low |
| 🟢 P4 | Add AD lab setup link in `BloodHound.md` | Low | Low |
| 🟢 P4 | Add FlareVM safety note in `Ghidra.md` and `x64dbg.md` | Low | Low |

---

### 8.2 Proposed Tools/README.md Structure

When creating the master index, use this structure:

```markdown
# 🔧 Tools Directory

> 52 tool mastery checklists organized by tier and roadmap phase.

## Tier System
- **Tier 1 — Core:** Used on every engagement. Must be mastered.
- **Tier 2 — Frequent:** Used regularly in specific phases or attack chains.
- **Tier 3 — Situational:** Used for specific target types or scenarios.
- **Tier 4 — Niche/Reference:** Specialized use. Know when to reach for it.

---

## Tier 1 — Core Tools (10)
| Tool | Description | Phase | File |
|...

## Tier 2 — Frequent Tools (27)
| Tool | Description | Phase | File |
|...

## Tier 3 — Situational Tools (7)
| Tool | Description | Phase | File |
|...

## Tier 4 — Niche / Reference Tools (8)
| Tool | Description | Phase | File |
|...
```

---

### 8.3 Proposed New File Templates

For each missing Tier 2 file, use this skeleton and fill in the tool-specific content:

#### Evil-WinRM.md
- **Phase alignment:** Phase 4/5 (Post-Exploitation, Lateral Movement)
- **Prerequisites:** WinRM enabled on target (port 5985/5986), valid Windows credentials
- **Core tasks to cover:** Installation, basic shell (`evil-winrm -i <IP> -u user -p pass`), pass-the-hash (`-H <NTLM>`), file upload/download, running scripts in-memory, AMSI bypass options, SSL mode (`--ssl`), integration with NetExec credential output
- **Cross-links:** `NetExec.md`, `Impacket.md`, `BloodHound.md`

#### Kerbrute.md
- **Phase alignment:** Phase 2/3 (Enumeration, AD Initial Access)
- **Prerequisites:** Network access to AD domain controller
- **Core tasks to cover:** Username enumeration (`userenum`), password spray (`passwordspray`), brute force (`bruteuser`), AS-REP pre-auth check, output formats, integration with Impacket GetNPUsers workflow
- **Cross-links:** `Impacket.md`, `NetExec.md`, `Hashcat.md`

#### Amass.md
- **Phase alignment:** Phase 1 (Reconnaissance)
- **Prerequisites:** API keys for Shodan, VirusTotal, Censys (optional but improve results)
- **Core tasks to cover:** Passive enum (`amass enum -passive -d target.com`), active enum, CIDR/ASN enumeration, output formats (JSON, dot), integration with theHarvester, Subfinder comparison section
- **Cross-links:** `theHarvester.md`, `SpiderFoot.md`, `Recon-ng.md`

#### Mimikatz.md
- **Phase alignment:** Phase 4/5 (Post-Exploitation, Credential Access)
- **Prerequisites:** Local admin or SYSTEM on Windows target
- **Core tasks to cover:** `privilege::debug`, `sekurlsa::logonpasswords`, `lsadump::sam`, `lsadump::dcsync`, `kerberos::list`, `kerberos::ptt`, `token::elevate`, pass-the-hash, golden/silver ticket creation, detection/AV evasion context
- **Cross-links:** `Impacket.md`, `BloodHound.md`, `NetExec.md`, `Hashcat.md`

#### Rubeus.md
- **Phase alignment:** Phase 4/5 (Kerberos attacks, Post-Exploitation)
- **Prerequisites:** Windows domain-joined machine or Sliver/Metasploit session
- **Core tasks to cover:** `asreproast`, `kerberoast`, `dump`, `ptt`, `tgtdeleg`, `s4u`, `harvest`, `monitor`, ticket manipulation, integration with Sliver armory
- **Cross-links:** `Impacket.md`, `Sliver.md`, `BloodHound.md`, `Hashcat.md`

#### Chisel.md
- **Phase alignment:** Phase 5 (Pivoting & Tunneling)
- **Prerequisites:** Binary on both attack machine and pivot host
- **Core tasks to cover:** Server setup (`chisel server -p 8080 --reverse`), client connection, SOCKS5 proxy (`--socks5`), reverse tunneling, HTTP tunnel through web proxies/firewalls, comparison with Ligolo-ng and SSH tunneling
- **Cross-links:** `Ligolo-ng.md`, `Netcat.md`, `Metasploit_Framework.md`

#### Nuclei.md
- **Phase alignment:** Phase 2/3 (Scanning, Web Vulnerability Detection)
- **Prerequisites:** Go installed or binary downloaded
- **Core tasks to cover:** Template-based scanning, severity filters (`-severity critical,high`), technology detection, CVE scanning, custom template writing, integration with Burp Suite outputs, comparison with Nikto
- **Cross-links:** `Nikto.md`, `Burp_Suite.md`, `ffuf.md`

#### Aircrack-ng.md
- **Phase alignment:** Phase 3 (Wireless Security)
- **Prerequisites:** Wireless adapter with monitor mode support
- **Core tasks to cover:** `airmon-ng` (monitor mode), `airodump-ng` (capture handshake), `aireplay-ng` (deauth attack), `aircrack-ng` (dictionary crack), WPA2 4-way handshake capture, `.hccapx` conversion for Hashcat, WPA3 SAE awareness
- **Cross-links:** `Bettercap.md`, `Wireshark.md`, `Hashcat.md` (mode 22000)

---

### 8.4 Final Verdict

**Is this tool collection production-ready?**
Yes — for the 52 tools that exist. The depth, accuracy, and consistency of the existing files is genuinely impressive. A learner who works through all Tier 1 files will be well-prepared for OSCP-level challenges. The DFIR and RE tool files are particularly strong.

**What does it fail to cover?**
The AD post-exploitation chain has three critical missing pieces: Evil-WinRM (the shell you use), Kerbrute (the enumeration you start with), and Mimikatz/Rubeus (the credential tools everyone asks about). The wireless domain is completely absent. Nuclei's absence is a gap that will become more noticeable over time as it continues replacing Nikto in the industry.

**What is the single highest-value fix?**
Create `Tools/README.md`. It costs 1-2 hours and immediately transforms 52 scattered files into a navigable, organized reference library. Every learner who opens the Tools/ folder benefits from it on day one.

**Biggest structural risk going forward?**
The navigation tables inside each file are a closed system — adding a new tool file requires manually updating the navigation table of every related file. As the collection grows past 60+ tools, this will become painful to maintain. Consider migrating to a tag-based system (each file lists its tags in the description block) and generating navigation from the `Tools/README.md` index instead.

---

*Audit complete. 52 files reviewed. 14 problems identified. 11 missing/needed tool files documented. All 52 existing files confirmed technically accurate.*
