# 📡 Aircrack-ng: Complete Mastery Checklist

> **What is Aircrack-ng?** Aircrack-ng is the standard open-source wireless network security auditing toolkit. It consists of four main components: `airmon-ng` (enable monitor mode), `airodump-ng` (capture packets and handshakes), `aireplay-ng` (inject frames — deauth attacks, ARP replay), and `aircrack-ng` (crack WEP keys and WPA/WPA2 handshakes). It is the foundational tool for all Wi-Fi security testing.
>
> **Why does it exist?** Wi-Fi networks are broadcast by nature — every packet is transmitted through the air and receivable by anyone in range. Aircrack-ng exploits this to capture authentication handshakes and crack pre-shared keys offline, exposing weak Wi-Fi passwords that put an entire network at risk.
>
> **When to use it:** During wireless security assessments (authorized). For WPA2 pre-shared key strength testing. When testing if corporate Wi-Fi can be cracked with a dictionary attack. For understanding wireless attack chains in lab environments. For Wi-Fi-related CTF challenges.
>
> **When to avoid it:** Without explicit written authorization — intercepting wireless communications is illegal in most jurisdictions. When Hashcat is doing the actual cracking (Aircrack-ng captures the handshake; Hashcat cracks it). When the target uses WPA3-SAE (Aircrack-ng's traditional handshake capture does not work against WPA3).
>
> **What mastering Aircrack-ng unlocks:** Complete Wi-Fi security assessment capability. Understanding of WPA2 authentication weaknesses. Deauth attack understanding (DoS and forced handshake capture). Wireless security awareness for all network security roles. CEH, OSCP (wireless section), and eWPT readiness.
>
> **Roadmap Phase:** Phase 3 (Wireless Security — Network Attack Surface)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

| Network Attacks | Packet Analysis | Credential Access | MitM |
|:----------------|:----------------|:-----------------|:-----|
| [🗺️ Nmap](Nmap.md) | [🦈 Wireshark](Wireshark.md) | [🔥 Hashcat](Hashcat.md) | [🕵️ Bettercap](Bettercap.md) |
| [🔨 hping3](hping3.md) | [📻 tcpdump](tcpdump.md) | [🔑 John the Ripper](John_the_Ripper.md) | [🐛 Ettercap](Ettercap.md) |
| **📡 Aircrack-ng** (you are here) | [📦 Scapy](Scapy.md) | [🔓 Hydra](Hydra.md) | [🕵️ Bettercap](Bettercap.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & Wireless Theory | 5 | 3–4 hours |
| 2 | Core Toolkit — Monitor, Capture, Crack | 6 | 5–7 hours |
| 3 | Intermediate — Deauth, PMKID, Evil Twin | 5 | 5–7 hours |
| 4 | Advanced — WPA3, Enterprise Wi-Fi, WPS | 4 | 4–6 hours |
| 5 | Tool Integration | 4 | 2–3 hours |
| 6 | Practical Labs | 4 | 5–8 hours |
| 7 | Methodology & Legal Context | 3 | 2–3 hours |
| 8 | Mastery Challenges | 3 | 4–6 hours |
| | **Total** | **34** | **~30–44 hours** |

**Prerequisites:** Understanding of 802.11 Wi-Fi standards (a/b/g/n/ac/ax). Linux CLI basics. A wireless adapter with monitor mode and packet injection support (recommended: Alfa AWUS036ACH or similar). A dedicated lab AP and target network you own or have written authorization to test.

**Legal Warning:** Intercepting wireless communications without authorization violates computer crime laws in virtually every jurisdiction (CFAA in the US, Computer Misuse Act in the UK, etc.). Only test networks you own or have written permission to test. **Never test against public, hotel, workplace, or neighbor networks.**

**Alternatives:** Bettercap (modern MitM including wireless), Hashcat (WPA cracking after handshake capture — faster than aircrack-ng's built-in cracker), hcxdumptool + hcxtools (PMKID capture — no deauth needed).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — 802.11 Wi-Fi Standards and WPA2 Authentication

- [ ] **Completed** · ⭐ Beginner · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand WPA2-PSK authentication well enough to know exactly what Aircrack-ng captures and cracks. |
| **Skills Learned** | 802.11 frame types (management, control, data), WPA2-PSK 4-way handshake (EAPOL frames exchanged to derive the PTK), what the handshake contains (ANonce, SNonce, MIC), why the MIC is crackable offline (it is derived from the PSK — guess the PSK, verify the MIC). |
| **Practical Exercise** | Draw the WPA2 4-way handshake: AP sends ANonce → Client sends SNonce + MIC → AP verifies MIC (derives PTK from ANonce+SNonce+PMK, verifies MIC — if MIC matches, PSK is correct). This is the exact operation Aircrack-ng/Hashcat performs offline. |
| **Expected Output** | 4-way handshake diagram with annotations explaining which values are captured and how the offline crack works. |

### Task 1.2 — Monitor Mode and Wireless Adapter Requirements

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand what monitor mode is and why standard wireless adapters cannot capture all 802.11 traffic without it. |
| **Skills Learned** | Normal managed mode (only receives packets addressed to your MAC), monitor mode (receives ALL 802.11 frames in range regardless of destination), packet injection capability (needed for deauth attacks), which chipsets support injection (Atheros, Ralink/Mediatek, Realtek RTL8812AU). |
| **Practical Exercise** | Check your wireless adapter: `iw list \| grep -A 10 "Supported interface modes"` — if `monitor` appears, your adapter supports monitor mode. Check injection: `aireplay-ng --test wlan0`. |
| **Expected Output** | Confirmation of monitor mode support. Understanding that VM wireless adapters usually do NOT support injection (use USB adapter passed through to VM). |

### Task 1.3 — The Aircrack-ng Suite Components

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Know each tool in the suite and its specific role. |
| **Skills Learned** | `airmon-ng` (enable/disable monitor mode), `airodump-ng` (passive sniffing and handshake capture), `aireplay-ng` (frame injection: deauth, ARP replay, fake auth), `aircrack-ng` (key cracking from captured files), `airbase-ng` (fake AP — evil twin), `airdecap-ng` (decrypt captured packets). |
| **Expected Output** | Reference table: tool → function → when to use. |

### Task 1.4 — Installation and Dependency Check

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Practical Exercise** | `sudo apt install aircrack-ng` → `airmon-ng --version`. Check `iw`, `iwconfig`, `hostapd` also installed. On Kali Linux — all pre-installed. On other distros: `sudo apt install iw wireless-tools hostapd`. Verify: `airmon-ng` lists your wireless interfaces. |

### Task 1.5 — Wireless Survey: Understanding the Environment

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand what is visible in the wireless environment before attacking. |
| **Practical Exercise** | `sudo airmon-ng start wlan0` → `sudo airodump-ng wlan0mon` → read output columns: BSSID (AP MAC), PWR (signal), #Data (data frames), #/s (rate), CH (channel), ENC (encryption type — WPA2/WPA3/OPN), ESSID (network name). Identify your lab target. Note channel number for focused capture. |
| **Expected Output** | Understanding of airodump-ng survey output. Target AP identified with BSSID and channel. |

---

# PHASE 2: CORE WORKFLOW — CAPTURE & CRACK

---

### Task 2.1 — Enable Monitor Mode (airmon-ng)

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Put the wireless adapter into monitor mode. |
| **Practical Exercise** | Kill interfering processes: `sudo airmon-ng check kill`. Enable monitor mode: `sudo airmon-ng start wlan0` → adapter becomes `wlan0mon`. Verify: `iwconfig wlan0mon` shows `Mode:Monitor`. To stop: `sudo airmon-ng stop wlan0mon` → `sudo service NetworkManager restart`. |
| **Expected Output** | `wlan0mon` in monitor mode. Network Manager stopped (otherwise it restarts managed mode). |
| **Common Mistakes** | Not killing interfering processes first (NetworkManager, wpa_supplicant fight monitor mode). Forgetting to restore managed mode after testing (no internet access until reverted). |

### Task 2.2 — Targeted Capture with airodump-ng

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Lock capture to a specific target AP and channel to collect the WPA2 handshake. |
| **Skills Learned** | `--bssid` (target AP MAC), `--channel` (lock to AP channel — reduces noise), `--write` (save capture to .cap file). |
| **Practical Exercise** | `sudo airodump-ng --bssid AA:BB:CC:DD:EE:FF --channel 6 --write capture wlan0mon`. Output file: `capture-01.cap`. Monitor the top-right corner of the display for `[ WPA handshake: AA:BB:CC:DD:EE:FF ]` — this appears when a client connects or is forced to reconnect. |
| **Expected Output** | Capture file created. Waiting for handshake (may take minutes if no clients are actively authenticating). |

### Task 2.3 — Forced Handshake via Deauth (aireplay-ng)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Send deauthentication frames to force a client to reconnect — triggering the WPA2 4-way handshake capture. |
| **Skills Learned** | `aireplay-ng --deauth` attack (`-0` mode), targeted deauth (specific client) vs broadcast deauth (all clients), why deauth works (802.11 management frames are unauthenticated — any device can spoof them). |
| **Practical Exercise** | In a second terminal (airodump-ng still running in first): `sudo aireplay-ng --deauth 5 -a AA:BB:CC:DD:EE:FF -c CC:DD:EE:FF:00:11 wlan0mon`. (`-a` = AP BSSID, `-c` = client MAC, `5` = send 5 deauth frames). Switch to airodump-ng terminal — should show `[ WPA handshake: ... ]` within seconds. |
| **Expected Output** | WPA handshake captured in airodump-ng. `capture-01.cap` file contains the EAPOL frames. |
| **Common Mistakes** | Sending too many deauth frames (disrupts the network noticeably). Not having a client connected (deauth without clients does nothing). Not watching airodump-ng for the handshake confirmation. |

### Task 2.4 — Verify Handshake Capture

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Verify the captured .cap file actually contains a complete, crackable 4-way handshake. |
| **Practical Exercise** | Method 1: `aircrack-ng capture-01.cap` → if handshake present, shows `1 handshake` for the target BSSID. Method 2: Open in Wireshark → filter `eapol` → confirm 4 EAPOL frames (messages 1-4). Method 3: `hcxtools: hcxpcapngtool capture-01.cap -o test.hc22000` → if no error, handshake is usable. |
| **Expected Output** | Confirmed complete 4-way handshake in capture file. Ready for cracking. |

### Task 2.5 — Convert to Hashcat Format (.hc22000)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Convert the .cap file to Hashcat's WPA format for GPU-accelerated cracking — much faster than aircrack-ng's built-in cracker. |
| **Skills Learned** | `hcxpcapngtool` (from hcxtools), `.hc22000` format, Hashcat mode 22000 for WPA. |
| **Practical Exercise** | `sudo apt install hcxtools` → `hcxpcapngtool -o handshake.hc22000 capture-01.cap` → `hashcat -m 22000 handshake.hc22000 /usr/share/wordlists/rockyou.txt`. |
| **Expected Output** | `.hc22000` file ready. Hashcat cracking at GPU speeds (millions of candidates/second vs thousands with CPU-only aircrack-ng). |

### Task 2.6 — Cracking with aircrack-ng (CPU)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Crack the WPA handshake directly with aircrack-ng and a wordlist (CPU-based — slower than Hashcat but simpler). |
| **Practical Exercise** | `aircrack-ng -w /usr/share/wordlists/rockyou.txt -b AA:BB:CC:DD:EE:FF capture-01.cap`. Watch progress: keys tested/second, time remaining. For a weak password in rockyou.txt, this succeeds in seconds. |
| **Expected Output** | `KEY FOUND! [ password123 ]` if the password is in the wordlist. Understanding that for strong passwords, Hashcat + GPU is required. |

---

# PHASE 3: INTERMEDIATE TECHNIQUES

---

### Task 3.1 — PMKID Attack (No Deauth Required)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Capture the PMKID from the first EAPOL frame without waiting for a client to connect — no deauth needed, no client needed. |
| **Skills Learned** | PMKID concept (derived from PMK + AP/client MAC — calculable without client interaction), `hcxdumptool` for PMKID capture, converting to Hashcat format. |
| **Practical Exercise** | `sudo apt install hcxdumptool hcxtools` → `sudo hcxdumptool -o pmkid.pcapng --enable-status=1 -i wlan0mon` → stop after a few minutes → `hcxpcapngtool -o pmkid.hc22000 pmkid.pcapng` → `hashcat -m 22000 pmkid.hc22000 rockyou.txt`. |
| **Expected Output** | PMKID captured without any clients connected. Hashcat cracking without requiring deauth. |

### Task 3.2 — Deauth DoS Attack Concept

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the deauthentication flood as a DoS attack and why it is a fundamental 802.11 weakness. |
| **Skills Learned** | Continuous deauth flood (`--deauth 0` = infinite), why management frame authentication is a design flaw (IEEE 802.11w adds management frame protection — MFP/PMF to fix this), detection via Wireshark (high rate of deauth frames from spoofed MAC), real-world impact. |
| **Practical Exercise** | Lab only: `sudo aireplay-ng --deauth 0 -a <your_lab_AP> wlan0mon` → observe clients disconnecting continuously. Stop with Ctrl+C. Check: does your AP support 802.11w (PMF)? If yes — deauth attack has reduced effectiveness. |
| **Expected Output** | Understanding of deauth as both a tool for handshake capture AND as a standalone DoS. Knowledge of 802.11w as the defense. |

### Task 3.3 — Evil Twin / Rogue AP (airbase-ng)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 50 min

| Field | Detail |
|:---|:---|
| **Objective** | Create a rogue access point that mimics a legitimate AP to capture credentials or perform MitM. |
| **Skills Learned** | `airbase-ng` for fake AP creation, deauth clients from real AP → clients connect to evil twin, traffic capture through the fake AP, captive portal credential harvesting (combine with Bettercap). |
| **Practical Exercise** | Lab: `sudo airbase-ng -e "TargetSSID" -c 6 wlan0mon` → rogue AP created on `at0` interface → bridge with internet (`brctl`) → clients connecting get internet (avoids detection) and traffic is captured. |
| **Expected Output** | Rogue AP running and visible to clients. Understanding of when captive portals are used to harvest WPA2 passwords (WPA2 evil twin attack). |

### Task 3.4 — WPS PIN Attack (reaver / bully)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand and exploit Wi-Fi Protected Setup (WPS) PIN authentication weakness. |
| **Skills Learned** | WPS PIN concept (8-digit PIN with design flaw — only 11,000 combinations needed due to split validation), `wash` to identify WPS-enabled APs, `reaver` or `bully` for WPS brute-force, WPS lockout detection. |
| **Practical Exercise** | Survey: `sudo wash -i wlan0mon` → identify WPS-enabled APs. Attack (lab only): `sudo reaver -i wlan0mon -b <BSSID> -vv` → watch PIN attempts. Modern APs have WPS lockout — may take hours or fail if locked. |
| **Expected Output** | Understanding of WPS weakness. If a lab AP has WPS enabled and no lockout: PSK recovered via WPS PIN attack. |

### Task 3.5 — Enterprise Wi-Fi (WPA2-Enterprise / RADIUS)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand WPA2-Enterprise authentication and how it differs from PSK (and why it is harder to crack). |
| **Skills Learned** | 802.1X EAP authentication (each user has their own credential — no shared PSK), EAP types (PEAP, EAP-TTLS, EAP-TLS), rogue RADIUS AP attack (hostapd-wpe to capture PEAP/MSCHAPv2 credentials), NTLMv2 hash extraction from PEAP challenge/response. |
| **Practical Exercise** | Review `hostapd-wpe` concept: set up a rogue WPA2-Enterprise AP with a valid-looking certificate → clients connect → MSCHAPv2 handshakes captured → crack with `hashcat -m 5500` (NetNTLMv1) or `-m 5600` (NetNTLMv2). |
| **Expected Output** | Understanding that WPA2-Enterprise eliminates PSK cracking but introduces PEAP credential theft attacks. |

---

# PHASE 4: ADVANCED

---

### Task 4.1 — WPA3 SAE: What Changed and What Broke

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand WPA3's Simultaneous Authentication of Equals (SAE) protocol and why it defeats traditional handshake capture. |
| **Skills Learned** | SAE (Dragonfly handshake) — prevents offline dictionary attacks by requiring real-time interaction for each guess, Forward Secrecy in WPA3, Dragonblood vulnerabilities (side-channel attacks against early WPA3 implementations), Transition mode weakness (WPA3/WPA2 mixed allows downgrade attacks). |
| **Practical Exercise** | Research: can airodump-ng capture a WPA3 SAE handshake for offline cracking? (No — SAE handshake is not vulnerable to offline dictionary attack by design.) What attack still works? (Dragonblood side-channel on vulnerable APs, evil twin with forced WPA2 downgrade via transition mode.) |
| **Expected Output** | Written comparison of WPA2 vs WPA3 attack surface. Understanding of when WPA3 is and isn't vulnerable. |

### Task 4.2 — Wireless Network Reconnaissance Deep Dive

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Build a complete picture of a wireless environment before attacking. |
| **Skills Learned** | Band awareness (2.4 GHz vs 5 GHz — need dual-band adapter for 5 GHz), hidden SSID de-cloaking (probe requests reveal hidden SSIDs when clients connect), signal mapping, identifying all connected clients per AP. |
| **Practical Exercise** | `sudo airodump-ng wlan0mon` → collect data for 5 minutes → export to CSV: `--output-format csv` → analyse which APs have the most clients, which use weak encryption, which are on auto-channel. |

### Task 4.3 — Cracking Strategy: Wordlists and Rules

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Build an effective cracking strategy for WPA2 passwords beyond plain rockyou.txt. |
| **Skills Learned** | Wi-Fi passwords are often: router defaults (8-char alphanumeric — use manufacturer-specific wordlists), ISP defaults (e.g., BT Hub uses 8-char hex), phone numbers, addresses, family names. `hashcat -m 22000` with rules: `best64.rule`, SSID-based mangling (people use SSID in password: `HomeWifi2024`). |
| **Practical Exercise** | Build a targeted wordlist for a test AP: SSID name, owner's name (from OSINT), common local patterns → apply `hashcat` rules → try before rockyou.txt. |

### Task 4.4 — Capturing Traffic from Connected Clients

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | After cracking the PSK, decrypt captured traffic from connected clients. |
| **Practical Exercise** | `airdecap-ng -e "SSID" -p "cracked_password" capture-01.cap` → decrypted packets in `capture-01-dec.cap` → open in Wireshark → inspect HTTP, DNS, and other plaintext protocols. |
| **Expected Output** | Decrypted packet capture. Understanding that cracking the WPA2 PSK means all past and future traffic on that network can be decrypted if you captured it. |

---

# PHASE 5: TOOL INTEGRATION

---

### Task 5.1 — Aircrack-ng → Hashcat Pipeline

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min
| Field | Detail |
|:---|:---|
| **Objective** | Use Aircrack-ng for capture, Hashcat for cracking — the standard professional workflow. |
| **Practical Exercise** | Capture `.cap` → `hcxpcapngtool` convert to `.hc22000` → `hashcat -m 22000` with GPU. Always prefer Hashcat for cracking — aircrack-ng's built-in cracker is CPU-only and much slower. |

### Task 5.2 — Airodump-ng → Wireshark Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min
| Field | Detail |
|:---|:---|
| **Practical Exercise** | Open `capture-01.cap` in Wireshark → `eapol` filter → inspect 4-way handshake frames → `wlan.fc.type_subtype == 0x0c` for deauth frames → document the full attack sequence visible in the packet capture. |

### Task 5.3 — Bettercap Wireless + Aircrack-ng

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min
| Field | Detail |
|:---|:---|
| **Objective** | Use Bettercap's wireless modules alongside Aircrack-ng for a complete wireless assessment. |
| **Practical Exercise** | Aircrack-ng for WPA2 handshake capture → Bettercap for 802.11 probe sniffing (`wifi.recon on`), deauth (`wifi.deauth`), and captive portal attacks. Compare capabilities of each. |

### Task 5.4 — Aircrack-ng Findings in a Pentest Report

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min
| Field | Detail |
|:---|:---|
| **Objective** | Document wireless security findings professionally. |
| **Practical Exercise** | Write a finding: "WPA2-PSK Weak Pre-Shared Key — Risk: High. The wireless network SSID X was found to use a weak PSK recoverable via offline dictionary attack in under 60 seconds. Recommendation: enforce complex PSK (20+ random characters), consider WPA3, enable 802.11w MFP." |

---

# PHASE 6: PRACTICAL LABS

---

### Lab 6.1 — Home Lab: Full WPA2 PSK Crack

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 2–3 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Set up a test AP with a weak PSK (`password123`). Full chain: airmon-ng → airodump-ng → aireplay-ng deauth → handshake capture → hcxpcapngtool → hashcat crack. |
| **Success Criteria** | PSK cracked. Full chain documented with screenshots. |

### Lab 6.2 — Home Lab: PMKID Attack (No Client)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 1–2 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Same test AP. Capture PMKID with hcxdumptool (no deauth, no connected client needed). Crack with Hashcat. |
| **Success Criteria** | PMKID captured. PSK cracked. Compared time to capture vs deauth method. |

### Lab 6.3 — CTF: Wi-Fi Capture Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 2 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Download a WPA2 capture file from a CTF challenge (HackTheBox, CTFtime) or generate one from your lab. Crack the PSK and decrypt the traffic to find the flag. |
| **Success Criteria** | PSK cracked from .cap file. Traffic decrypted. Flag found in HTTP/DNS traffic. |

### Lab 6.4 — WPA2 vs WPA3 Comparison Lab

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 2 hours
| Field | Detail |
|:---|:---|
| **Scenario** | Configure one AP as WPA2-PSK and another as WPA3-SAE (both with the same weak password). Attempt the same handshake capture + crack against both. Document what succeeds and fails. |
| **Success Criteria** | WPA2 cracked successfully. WPA3 SAE handshake not crackable via same method. Documented the security improvement. |

---

# PHASE 7: METHODOLOGY & LEGAL CONTEXT

---

### Task 7.1 — Wireless Pentest Methodology

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min
| Field | Detail |
|:---|:---|
| **Objective** | Follow a structured wireless security assessment methodology. |
| **Expected Output** | Methodology: (1) Passive survey — identify all APs, clients, encryption types. (2) Passive capture — record traffic without injection. (3) PMKID capture (passive, no deauth). (4) Forced handshake via deauth (only if authorized). (5) Offline cracking. (6) Decrypted traffic analysis. (7) Findings report. |

### Task 7.2 — Legal Authorization Requirements

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min
| Field | Detail |
|:---|:---|
| **Objective** | Understand the legal landscape for wireless security testing. |
| **Skills Learned** | Written authorization scope must explicitly include wireless testing. Monitor mode scanning of all APs in range (even without connecting) may be legally ambiguous in some jurisdictions. Deauth attacks are a DoS attack — they affect ALL clients. Never test hotel, coffee shop, neighbour, or employer Wi-Fi without explicit written authorization. |

### Task 7.3 — Hardening Wi-Fi Against These Attacks

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min
| Field | Detail |
|:---|:---|
| **Objective** | Advise organizations on wireless security hardening. |
| **Skills Learned** | Use WPA3-SAE, enable 802.11w (PMF/MFP) to prevent deauth attacks, use long random PSK (20+ chars) or WPA2-Enterprise for corporate, disable WPS, disable hidden SSID (security through obscurity), network segmentation (IoT VLAN, guest network). |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Timed WPA2 Crack

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 2 hours
Set up test AP with a password from the top 1000 rockyou.txt entries. Complete the full chain — monitor mode → capture → crack — in under 15 minutes. Document time for each step.

### Challenge 8.2 — Hardened AP Bypass

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 3 hours
Configure test AP with 802.11w enabled (PMF required). Attempt deauth — observe reduced effectiveness. Switch to PMKID attack (not blocked by PMF). Document the attack surface that remains despite hardening.

### Challenge 8.3 — Full Wireless Pentest Report

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 3–4 hours
Conduct a complete wireless security assessment of your home lab (multiple APs if possible). Write a professional pentest report covering: scope, methodology, findings, severity ratings, evidence (redacted screenshots), and remediation recommendations.

---

## 🎓 Competency Matrix

| Skill | Beginner | Intermediate | Advanced |
|:------|:--------:|:------------:|:--------:|
| Enable monitor mode and kill interfering processes | [ ] | | |
| Survey wireless environment with airodump-ng | [ ] | | |
| Targeted handshake capture | | [ ] | |
| Deauthentication frame injection | | [ ] | |
| PMKID capture with hcxdumptool | | [ ] | |
| Convert .cap to .hc22000 and crack with Hashcat | | [ ] | |
| Decrypt captured WPA2 traffic | | [ ] | |
| Evil twin / rogue AP setup | | | [ ] |
| WPA2-Enterprise PEAP credential theft | | | [ ] |
| WPA3 vs WPA2 attack surface comparison | | [ ] | |

---

## 💬 Interview Questions

1. Explain the WPA2 4-way handshake and exactly what Aircrack-ng captures from it.
2. Why does monitor mode need to be enabled before capturing wireless traffic?
3. What is a deauthentication attack and why does it work against standard 802.11?
4. What is the PMKID attack and why is it better than waiting for a deauth handshake?
5. Why is Hashcat preferred over aircrack-ng's built-in cracker for WPA2 cracking?
6. What is 802.11w (Management Frame Protection) and how does it reduce deauth attack effectiveness?
7. How does WPA3-SAE prevent offline dictionary attacks that succeed against WPA2-PSK?
8. What are the legal considerations when performing wireless security testing?
9. What is a WPA2-Enterprise network and how does it differ from PSK from a security perspective?
10. Walk through the full chain from discovering a target Wi-Fi network to cracking its PSK.
