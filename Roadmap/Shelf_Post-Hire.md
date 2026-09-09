# 📦 Shelf: Post-Hire & Elective Specializations

---

### 🧭 Navigation
◀ [Stage 5: Specialized](Stage-5_Specialized.md) | 🏠 [Master Roadmap](README.md)

---

> [!CAUTION]
> **POST-HIRE ONLY — Do NOT include in your pre-employment critical path.**
>
> These topics are specialized tracks, compliance domains, or niche disciplines. Studying these pre-employment dilutes your focus from mastering the core offensive pipeline (Linux, Windows, Networking, Web, Active Directory, and Tooling).
> 
> Return to these modules only after securing your target offensive security role or when an employer engagement explicitly mandates them.

---

<a id="shelf-01-wireless-network-security"></a>
<a id="part-21"></a>

## Shelf 01: Wireless Network Security


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Wireless Hacking` — Full — core wireless attack methodology (WPA2 cracking, PMKID, Evil AP setup)
> - 🟡 `Wireless Network Security` — Reference — defensive perspective; informs OPSEC and detection awareness
> - 🔴 `Wireless Hacking Cheat Sheet v1.1` — ⚡ Keep open during all Part 21 labs
> - 🟢 `Wifi & Security` / `WiFi hacking article` — Supplementary reference PDFs


> [!IMPORTANT]
> **Hardware Acquisition Checklist — Purchase Before Starting Phase 5**
>
> Phase 5 requires physical hardware for wireless and mobile labs. A student with no hardware can read the content but cannot execute any technique. Budget and acquire the following before starting:
>
> | Hardware | Required For | Why Needed | Approx. Cost |
> |---|---|---|---|
> | **Alfa AWUS036ACH** (802.11ac) | WiFi monitor mode + packet injection | Most built-in laptop adapters cannot enter monitor mode or inject packets | $35–50 |
> | **Alfa AWUS036ACHM** (802.11ax/WiFi 6) | WPA3 testing | WPA3 testing requires WiFi 6 capable adapter | $50–70 |
> | **Proxmark3 Easy or RDV4** | RFID/NFC labs (Stage 6) | Read/write/clone RFID/NFC cards | $80–200 |
> | **Flipper Zero** (optional) | Sub-GHz, IR, RFID/NFC, BadUSB | Versatile multi-protocol tool; optional but highly useful | $170 |
> | **HackRF One** (optional, Stage 8) | SDR analysis — OPTIONAL specialization | Required only if pursuing Stage 8 (marked optional) | $300 |
> | **Android test device (rooted)** | Mobile dynamic analysis (Part 22) | Rooted device needed for Frida, Objection, Burp cert install | $50–150 (used) |
> | **Wireless AP (WPA3-capable)** | WPA3 evil twin testing | Must support WPA3-SAE for Stage 2 | $50–100 |
>
> **Mobile Lab Setup Time:** First-time setup of a rooted Android device, Frida installation, Burp certificate pinning, and objection deployment typically takes **1–3 weeks**. Budget this into your Phase 5 timeline.
>
> **Budget Estimate:** Minimum functional kit (Alfa adapter + test Android device) ≈ $85–200. Full kit with Proxmark3 + Flipper Zero ≈ $350–500.

> **Safety Gate:** RF testing must stay inside legal spectrum rules and authorized lab targets. Use your own access points, Faraday isolation where appropriate, low power settings, and written permission. GPS jamming/spoofing and unauthorized wireless interference can create real-world safety issues.

<a id="stage-1-rf-reconnaissance-setup"></a>
### **Stage 1: RF Reconnaissance & Setup** — `🔬 Practical`

> [!TIP]
> **Goal:** Map the airspace and identify targets.

- [ ] **Monitor Mode:** Configure hardware to capture raw 802.11 frames.

- [ ] **Protocol Audit:** Identify the target's encryption: **WPA vs WPA2 vs WPA3 vs WEP**. Note that WEP is obsolete but trivial to crack; WPA3 is resistant to dictionary attacks.

- [ ] **WPS Check:** Scan for **WPS** enabled APs. If active, this is the primary high-value target for PIN brute-forcing (Pixie Dust).

---

<a id="stage-2-access-point-assault-the-breaching-of-keys"></a>
### **Stage 2: Access Point Assault (The Breaching of Keys)** — `🔬 Practical`

> [!TIP]
> **Goal:** Obtain the credentials to join the network.

- [ ] **Handshake Capture:** Execute a **Deauth Attack** against a connected client to force a reconnection and capture the 4-way handshake.

- [ ] **Replay Attacks:** (For legacy/WEP) Use **Replay Attack** techniques to generate traffic and accelerate IV collection for cracking.

- [ ] **Offline Cracking:** Run the captured handshake against wordlists using [Hashcat](Tools/Hashcat.md)/Aircrack-ng.

---

<a id="stage-3-enterprise-client-attacks-the-man-in-the-middle"></a>
### **Stage 3: Enterprise & Client Attacks (The Man-in-the-Middle)** — `🔬 Practical`

> [!TIP]
> **Goal:** Steal individual user identities or hijack connections.

- [ ] **Evil Twin Deployment:** Launch an **Evil Twin** attack to impersonate the target SSID. Use a captive portal to harvest credentials.

- [ ] **Enterprise Stripping:** Target **EAP vs PEAP** configurations. Downgrade encryption or crack the challenge-response hashes (MSCHAPv2) captured from the Evil Twin.

- [ ] **Rogue AP:** Plant a **Rogue Access Point** physically in the facility to create an unauthorized backdoor into the LAN.

- [ ] **KRACK Attack:** Exploit **Key Reinstallation Attack** against WPA2 to decrypt traffic (requires client participation, patches available).

- [ ] **PMKID Attack:** Extract **PMKID** from unassociated clients for offline cracking (faster than 4-way handshake, works against WPA2/WPA3).

---

<a id="stage-4-bluetooth-ble-attacks"></a>
### **Stage 4: Bluetooth & BLE Attacks** — `🔬 Practical`

> [!TIP]
> **Goal:** Compromise Bluetooth connections and devices.

- [ ] **BLE Fundamentals:** Understand **Bluetooth Low Energy** (BLE) **GATT/GAP, advertising, pairing mechanisms, security modes**.

- [ ] **Bluejacking:** Send **unsolicited messages** to BLE devices (informational, not harmful, for PoC).

- [ ] **Bluesnarfing:** Gain **unauthorized access** to BLE device data (contacts, calendar, files).

- [ ] **KNOB Attack:** Exploit **Key Negotiation of Bluetooth** to negotiate weak encryption keys.

- [ ] **BLE Pairing Bypass:** Exploit **weak pin/oob verification** or perform **man-in-the-middle attacks** on pairing to intercept keys.

- [ ] **Bluetooth Eavesdropping:** Use tools like **ubertooth, Proxmark** to capture Bluetooth packets and attempt decryption.

---

<a id="stage-5-zigbee-z-wave-iot-attacks"></a>
### **Stage 5: Zigbee, Z-Wave & IoT Attacks** — `🔬 Practical`

> [!TIP]
> **Goal:** Compromise smart home and industrial IoT networks.

- [ ] **Zigbee Basics:** Understand **Zigbee mesh networking, 802.15.4 radio, AES-128 encryption, default keys**.

- [ ] **Zigbee Sniffing:** Use **USRP, cc2531 dongles** to capture **Zigbee traffic** and extract **network keys** from initial joins.

- [ ] **Zigbee Replay:** Capture and replay **legitimate frames** to trigger device actions (turn lights on/off, unlock).

- [ ] **Z-Wave Attacks:** Exploit **Z-Wave security flaws** (obsolete S0, weak S2 implementations) to hijack devices.

- [ ] **Default Credentials:** Test **Zigbee/Z-Wave hubs** for **default passwords, backdoor accounts**.

- [ ] **Firmware Extraction:** Dump **device firmware** via **UART, JTAG** to find **hardcoded keys or vulnerabilities**.

---

<a id="stage-6-nfc-rfid-attacks"></a>
### **Stage 6: NFC & RFID Attacks** — `🔬 Practical`

> [!TIP]
> **Goal:** Compromise Near-Field Communication and passive identification systems.

- [ ] **NFC Basics:** Understand **ISO14443-A/B, Mifare protocols, Type 1-4 tags, Android NFC API**.

- [ ] **NFC Cloning:** Extract **NFC card data** using **Proxmark, ACR122U** and write to **blank cards/tags**.

- [ ] **NFC Relay Attack:** Set up **two NFC readers** at distance to **relay communication** between reader and card (e.g., contactless payment fraud).

- [ ] **RFID Spoofing:** Craft **malicious RFID tags** to bypass access control readers (badges, building entry).

- [ ] **RFID Skimming:** Read **unencrypted RFID tags** from distance using **passive readers** (passport, credit card cloning).

- [ ] **ISO7816 Smartcard Attacks:** Understand **smartcard protocols** and exploit **weak implementations, timing attacks, power analysis**.

---

<a id="stage-7-gps-satellite-spoofing"></a>

### **Stage 7: GPS & Satellite Spoofing [OPTIONAL SPECIALIZATION]** — `🔬 Practical`

> [!NOTE]
> **Optional Specialization:** GPS spoofing and satellite security require expensive specialized hardware (USRP B200/B210 starts at $800+), operate in legally restricted frequency bands (GPS jamming is a federal felony in the US), and serve a very narrow career path (drone security research, maritime/aviation security testing, critical infrastructure GPS dependency analysis). If this aligns with your career goal, complete this stage fully. If not, read for awareness and proceed to Stage 9 (Defense) or Part 22 (Mobile). **Do not let this stage block your progress.**

> [!TIP]
> **Goal:** Manipulate location services and navigation.

- [ ] **GPS Basics:** Understand **GPS signal structure, GNSS systems (GPS/GLONASS/Galileo), pseudoranges, civilian vs military**.

- [ ] **GPS Spoofing:** Use **USRP or GPS simulators** to transmit **fake GPS signals** and cause devices to report false locations.

- [ ] **GPS Jamming:** Transmit **noise** on **L1 frequency (1575.42 MHz)** to deny GPS service (illegal but demonstrable in lab).

- [ ] **Satellite Communication Hacking:** Understand **Inmarsat, Iridium, Globalstar satellites**; identify **ground stations** for signal theft.

- [ ] **Drone GPS Hijacking:** Spoof **drone GPS** to cause drift, return-to-home corruption, or loss of control.

---

<a id="stage-8-sdr-spectrum-analysis"></a>

### **Stage 8: SDR & Spectrum Analysis [OPTIONAL SPECIALIZATION]** — `🔬 Practical`

> [!NOTE]
> **Optional Specialization:** Software-Defined Radio analysis requires hardware (HackRF One ~$300, USRP ~$800+) and strong RF/signal processing background. It is primarily used in RF security research, telecom security, and critical infrastructure assessments. For general pentesting and red teaming careers, SDR is awareness-level knowledge. If you are targeting RF security or telecom roles, complete this stage in full. Otherwise, read for awareness and proceed.

> [!TIP]
> **Goal:** Understand software-defined radio and RF reconnaissance.

- [ ] **SDR Fundamentals:** Know tools like **USRP, HackRF, BladeRF** and frameworks like **GNU Radio, CubicSDR**.

- [ ] **Spectrum Scanning:** Use **spectrum analyzers** to identify **active RF signals, frequency bands, modulation types**.

- [ ] **Signal Demodulation:** Demodulate **AM, FM, FSK, PSK, QPSK** signals and extract **data streams**.

- [ ] **Cellular Eavesdropping:** Understand **2G/3G/4G/5G protocols** and attempt to capture **downlink signals** (law enforcement only in licensed contexts).

- [ ] **Protocol Fuzzing:** Use **GrFuzz, AFLplusplus** to fuzz **RF protocols** and find **unexpected states or crashes**.

---

<a id="stage-9-defense-hardening-the-shield"></a>
### **Stage 9: Defense & Hardening (The Shield)** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Secure the airwaves.

- [ ] **Protocol Hardening:** Migrate all APs to **WPA3 (SAE)** to mitigate handshake cracking; disable **WPS** immediately.

- [ ] **Certificate Enforcement:** For **EAP/PEAP** networks, enforce **server certificate validation** on all client devices to neutralize **Evil Twin** attacks.

- [ ] **Wireless IPS:** Deploy **WIDS/WIPS** sensors to detect **deauth attacks, rogue APs, evil twins, unusual RF patterns**.

- [ ] **Network Segmentation:** Isolate wireless networks via **VLANs, guest networks**; implement **802.1X authentication** for enterprise.

- [ ] **Physical Security:** Secure AP placement to prevent **physical tampering, rogue AP installation**; use **tamper-evident seals**.

---

<a id="toc-part-22-mobile-platform-pentesting"></a>
<a id="part-22-mobile-platform-pentesting"></a>

---

<a id="shelf-02-mobile-platform-pentesting"></a>
<a id="part-22"></a>

## Shelf 02: Mobile Platform Pentesting


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Hacking android` — Full — Android attack surface, APK analysis, and exploitation
> - 🔴 `Hacking and securing ios applications` — Full — iOS binary analysis, Jailbreak exploitation, runtime hooking
> - 🟡 `Cybersecurity for Mobile Devices` — Reference — broad mobile security coverage
> - 🟢 `Best of Mobile Hacking` — Reference — supplementary attack techniques
> - 🟢 `Hacking Android Smartphones with NFC Tags` / `Bluetooth Low Energy Hacking` — Reference only if your labs include BLE/NFC vectors


<a id="stage-0-mobile-architecture-foundations"></a>
### **Stage 0: Mobile Architecture Foundations** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Understand Android and iOS architecture and security models before attempting exploitation. If you completed the awareness-level coverage in Part 1 Stage 6, this stage provides the full depth.

**Android Architecture:**

- [ ] **APK Structure:** Understand **APK format, AndroidManifest.xml, resources, assets, DEX bytecode**, and signed vs. unsigned APKs.

- [ ] **Android Security Model:** Learn **application sandboxing, SELinux enforcement, permissions model (runtime vs install-time, M+)**, and **Google Play Protect verification**.

- [ ] **Rooting & SuperUser:** Understand what **rooting** means, how it bypasses the security model, implications for security testing, and the difference from iOS jailbreaking.

- [ ] **Android Storage:** Know **internal vs. external storage**, **app-specific storage**, **SharedPreferences**, and permission implications for data access.

**iOS Architecture:**

- [ ] **IPA Structure:** Understand **IPA format, Mach-O binaries, Info.plist**, provisioning profiles, and code signing requirements.

- [ ] **iOS Security Model:** Learn **mandatory code signing**, **Secure Enclave Processor**, **Data Protection classes (NSFileProtection)**, and **sandbox restrictions**.

- [ ] **Jailbreaking:** Understand what **jailbreaking** means, types (tethered/semi-tethered/untethered), and implications for device security testing.

- [ ] **iOS Permissions & Privacy:** Know **privacy labels**, **App Tracking Transparency (ATT)**, **TCC (Transparency, Consent, and Control)**, and entitlements.

**Cross-Platform Security Concepts:**

- [ ] **Certificate Pinning:** Understand why apps implement **SSL/TLS certificate pinning**, how it prevents MITM, and why testers must bypass it.

- [ ] **Biometric Authentication:** Know **fingerprint/face recognition APIs** (Android BiometricPrompt, iOS LocalAuthentication) and their security model (local vs. server-side verification).

- [ ] **Hardware-Backed Keystores:** Understand **Android Keystore (TEE/StrongBox)** and **iOS Keychain (Secure Enclave)** for cryptographic key storage and credential management.

---

<a id="stage-1-lab-setup-reconnaissance"></a>
### **Stage 1: Lab Setup & Reconnaissance** — `🔬 Practical`

> [!TIP]
> **Goal:** Prepare the environment and understand the target.

- [ ] **Environment Prep:** Configure a Rooted (Android) or Jailbroken (iOS) device to bypass **Operating System Hardening**.

- [ ] **Binary Acquisition:** Extract the APK or IPA and perform **Basics of Reverse Engineering** using tools like `jadx` or `[Ghidra](Tools/Ghidra.md)`.

- [ ] **Reconnaissance:** Map the app's attack surface (activities, services, URL schemes) and identify backend endpoints.

---

<a id="stage-2-static-analysis-code-review"></a>
### **Stage 2: Static Analysis (Code Review)** — `🔬 Practical`

> [!TIP]
> **Goal:** Find hardcoded secrets and configuration flaws.

- [ ] **Manifest/Plist Audit:** Check for exported components or insecure permissions that violate **Zero Trust** principles.

- [ ] **Secret Hunting:** Search decompiled code for **Key Exchange** material, API tokens, or hardcoded credentials.

- [ ] **Crypto Audit:** Verify if the app uses weak **Hashing** or **Salting** algorithms for local storage.

---

<a id="stage-3-dynamic-analysis-runtime-manipulation"></a>
### **Stage 3: Dynamic Analysis (Runtime Manipulation)** — `🔬 Practical`

> [!TIP]
> **Goal:** Bypass client-side controls.

- [ ] **Security Control Bypass:** Use Frida to bypass Root Detection and SSL Pinning (breaking the **SSL vs TLS** trust chain).

- [ ] **Logic Manipulation:** Hook functions to bypass **Authentication vs Authorization** checks (e.g., bypassing a PIN screen).

- [ ] **Memory Dumping:** Analyze device memory for sensitive data that should have been cleared (violating **Confidentiality** in the **CIA Triad**).

---

<a id="stage-4-network-api-attacks"></a>
### **Stage 4: Network & API Attacks** — `🔬 Practical`

> [!TIP]
> **Goal:** Compromise the backend server.

- [ ] **Traffic Interception:** Proxy traffic to analyze **Secure vs Unsecure Protocols** and payload structures.

- [ ] **API Vulnerability Testing:** Test backend endpoints for **OWASP10** vulnerabilities like **SQL Injection**, **IDOR**, and **Broken Access Control**.

- [ ] **Session Management:** Test for weak **Session ID** generation or lack of **MFA & 2FA** on the mobile endpoints.

---

<a id="stage-5-local-data-storage-defense"></a>
### **Stage 5: Local Data Storage & Defense** — `🔬 Practical`

> [!TIP]
> **Goal:** Assess data at rest security.

- [ ] **Insecure Storage Check:** Inspect local files (**SQLite, SharedPreferences, Plist, Keychain**) for unencrypted **PII, credentials, API keys**.

- [ ] **Log Analysis:** Check system **logs (Logcat/Syslog)** for sensitive data leakage during app usage.

- [ ] **Backup Analysis:** Extract and analyze **iOS/Android backups** for sensitive data exposure.

---

<a id="stage-6-defense-secure-development"></a>
### **Stage 6: Defense & Secure Development** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Build security into mobile apps.

- [ ] **Secure Storage:** Use **Android Keystore, iOS Keychain** for sensitive data; encrypt local databases.

- [ ] **Certificate Pinning:** Implement **SSL/certificate pinning** to prevent MITM attacks.

- [ ] **Code Obfuscation:** Use **ProGuard (Android), Swift obfuscation** to hinder reverse engineering.

- [ ] **Runtime Protection:** Implement **root/jailbreak detection, debugger detection, integrity checks**.

- [ ] **Secure Communication:** Enforce **TLS 1.2+**, validate **certificates**, use **certificate pinning** for API calls.

---

### **Lab Progression (Part 21: Wireless Pentesting)**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Capture a WPA2 4-way handshake from your own AP using Aircrack-ng and crack it with a wordlist | Handshake capture file + successful crack report |
| 2 | Execute an evil twin attack with [Bettercap](Tools/Bettercap.md)/hostapd-mana and capture credentials in your lab | MITM attack walkthrough with evidence screenshots |
| 3 | Perform BLE enumeration and GATT service analysis of an IoT device using Bettercap or GATTacker | BLE security audit report with service map |

> [!IMPORTANT]
> **Move-On Gate (Part 21):** Crack a WPA2 handshake, execute an evil twin attack, and enumerate BLE services — all in your own lab with your own equipment.

---

### **Lab Progression (Part 22: Mobile Pentesting)**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Perform static analysis of DIVA or InsecureBankv2 using MobSF and document all findings | Mobile app static analysis report |
| 2 | Use Frida/Objection to bypass root detection and SSL pinning on a test app, then intercept API traffic | Dynamic analysis walkthrough with method hooks and traffic captures |
| 3 | Complete a full mobile pentest (static + dynamic + network + local storage) on a vulnerable app | Professional mobile assessment report following OWASP MSTG |

> [!IMPORTANT]
> **Move-On Gate (Part 22):** Complete a full mobile app assessment (static + dynamic + network + storage) and produce a professional report following OWASP MSTG methodology.

---

### 🏆 Phase 5 Capstone Project

**Conduct a Wireless Security Audit and Mobile App Assessment**

- [ ] **Wireless audit:** Assess your own lab AP — capture handshakes, test evil twin, evaluate encryption settings
- [ ] **Mobile assessment:** Perform static + dynamic + network analysis on a vulnerable app (DIVA or InsecureBankv2)
- [ ] **Document both assessments** as professional reports

**Deliverables:**
- [ ] Wireless security audit report (methodology, findings, risk ratings, remediation)
- [ ] Mobile application security assessment report following OWASP MSTG
- [ ] All capture files, scripts, and evidence committed to your Git repository

> [!IMPORTANT]
> **Capstone Gate:** Both reports must follow professional assessment methodologies and contain reproducible findings with evidence.

---

### 🧭 Phase 5 Reflection & Competency Check

- [ ] **Reflection:** Which constraints made wireless or mobile testing harder: hardware, tooling, OS versions, or evidence capture?
- [ ] **Reflection:** What did your reports communicate well, and what would a client still ask you to clarify?
- [ ] **Competency:** Can you safely capture, analyze, and explain wireless evidence from your own lab?
- [ ] **Competency:** Can you perform static, dynamic, network, and local-storage analysis on a test mobile app?
- [ ] **Competency:** Can you separate exploitable findings from platform behavior and false positives?

> [!IMPORTANT]
> **Phase Completion Gate:** Move on only when your wireless and mobile reports contain reproducible evidence, clear risk ratings, and practical remediation guidance.

---

<a id="phase-5-mini-projects"></a>

## 🛠️ Phase 5 Mini Projects

> [!TIP]
> **Why this project is here:** Phase 5 is dedicated to wireless and mobile security. The Wi-Fi Network Scanner belongs here because it requires 802.11 protocol knowledge, monitor mode, and beacon frame analysis — all concepts introduced in Part 21. Build it after completing Part 21 Stage 1 (RF Reconnaissance & Setup).

---

### Project 12 — Wi-Fi Network Scanner

**Maps to:** Part 21 (Wireless Pentesting) → Stage 1: RF Reconnaissance & Setup

**What it is:** A wireless network discovery tool that places a wireless adapter into monitor mode, passively captures 802.11 beacon frames and probe responses, and displays a real-time table of discovered networks showing: SSID, BSSID (MAC address of AP), channel, signal strength (RSSI in dBm), encryption type (Open, WEP, WPA, WPA2, WPA3), and observed clients. Optionally captures probe requests from clients to identify devices looking for known networks.

**What you need before building it:**
- 802.11 frame types: management frames (beacon, probe request/response, association) vs data frames vs control frames
- Monitor mode: a wireless adapter in monitor mode captures all 802.11 frames in range, not just those addressed to your device (unlike normal managed mode)
- Linux wireless tools: `airmon-ng` (enable monitor mode), `iwconfig`/`iw` (interface management)
- `scapy` with 802.11 support: `from scapy.all import *; sniff(iface='wlan0mon', prn=handler, store=False)`
- Beacon frame structure: the `Dot11Beacon` layer in scapy — contains SSID (in `Dot11Elt` with ID=0), channel, supported rates, RSN (WPA2/WPA3 info element)
- RSSI extraction: signal strength is in the `RadioTap` header, not the 802.11 frame itself
- Encryption detection: parse RSN Information Element (IE) for WPA2/WPA3, check for WPA IE for WPA, check `capability` field for WEP

**Why build it:**
Wi-Fi is a chronically underestimated attack surface. Building a scanner forces you to confront how much information access points broadcast to the world without any authentication: their SSID, supported security protocols, vendor OUI (from BSSID), channel, and supported rates. Capturing probe requests reveals what networks a device's "remembered networks" list contains — a privacy leak exploitable by evil twin attacks.

This project also teaches a key wireless security lesson: WPA2-Personal (password-based) is only as strong as the password. The PMKID attack (discovered in 2018) allows capturing enough information to attempt offline password cracking without ever connecting to the network — information your scanner can passively collect in seconds. After building this, you understand *why* WPA3 exists and what it actually fixes.

**Deliverable:** Python script using `scapy` that:
- Checks for a wireless interface in monitor mode (exit with clear instructions if not)
- Captures beacon frames and updates a live terminal table (use `rich` or `curses` for display)
- Shows: SSID, BSSID, Channel, RSSI (dBm), Encryption, Client count
- Optionally logs probe requests with client MAC and requested SSID

README must explain: what monitor mode is, why root is required, how to enable monitor mode (`airmon-ng start wlan0`), and what PMKID is and why it allows offline cracking without a 4-way handshake capture.

> [!CAUTION]
> This tool must only be used in your own lab environment or networks you own. Capturing wireless traffic from networks you do not own is illegal in most jurisdictions under computer misuse and wiretapping laws. Document this disclaimer prominently in your README.

---

> [!IMPORTANT]
> **Phase 5 Project Completion Gate:** Your Wi-Fi scanner must correctly identify encryption types and display real captured data from your own lab network. The README must explain *why* PMKID changed the wireless attack landscape in 2018 — not just what it is, but what it enabled that wasn't possible before.

---

<a id="shelf-03-otics-scada-security"></a>
<a id="part-26"></a>

## Shelf 03: OT/ICS/SCADA Security



> [!CAUTION]
> **OPTIONAL SPECIALIZATION — NOT PART OF THE RED TEAM CRITICAL PATH.**
>
> OT/ICS/SCADA security is a **separate career field** targeting industrial control systems in energy, utilities, manufacturing, water treatment, and critical infrastructure. It requires specialized knowledge of industrial protocols (Modbus, DNP3, Profinet), PLC/HMI architecture, and operational safety constraints that are entirely distinct from enterprise IT security.
>
> **Skip this Part if:** Your target is general penetration testing, enterprise red teaming, cloud security, or AI security. Do NOT let OT/ICS block your progress to Phase 7.
>
> **Complete this Part only if:** You are explicitly targeting ICS/OT pentesting roles (energy sector, industrial consultancies), critical infrastructure defense, or SCADA security engineering. These roles have specific hiring pipelines and certifications (GICSP, ICS-CERT training) that are separate from the standard Red Team track.
>
> This content is available here for completeness. Treat it as post-hire optional alongside Phase 5 and Phase 8.



<a id="stage-1-industrial-protocol-fundamentals"></a>
### **Stage 1: Industrial Protocol Fundamentals** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Understand operational technology communication.

- [ ] **Modbus TCP/RTU:** Master **function codes (read coils, write registers)**, perform **unauthenticated reads/writes** to PLCs.

- [ ] **DNP3:** Understand **SCADA protocol** used in utilities; exploit **lack of authentication, replay attacks**.

- [ ] **IEC 61850:** Learn **power substation protocol**; understand **GOOSE messages, MMS** for substation automation.

- [ ] **BACnet:** Audit **building automation systems**; enumerate **devices, read/write points** without authentication.

- [ ] **OPC UA:** Exploit **OPC servers** for **data exfiltration, authentication bypass, denial of service**.

---

<a id="stage-2-plc-hmi-exploitation"></a>
### **Stage 2: PLC & HMI Exploitation** — `🔬 Practical`

> [!TIP]
> **Goal:** Compromise industrial controllers and interfaces.

- [ ] **PLC Enumeration:** Use **[Nmap](Tools/Nmap.md) NSE scripts, plcscan** to identify **Siemens S7, Allen-Bradley, Schneider** devices.

- [ ] **Ladder Logic Analysis:** Reverse engineer **PLC programs** to understand **control logic, safety interlocks**.

- [ ] **Firmware Manipulation:** Extract and modify **PLC firmware** to inject malicious logic or backdoors.

- [ ] **HMI Exploitation:** Exploit **HMI software vulnerabilities, default credentials, SQL injection** in SCADA interfaces.

- [ ] **Engineering Workstation:** Target **engineering stations** with **phishing, malware** as gateway to OT network.

---

<a id="stage-3-safety-system-attacks"></a>
### **Stage 3: Safety System Attacks** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Understand attacks on critical safety instrumented systems.

- [ ] **Safety PLC:** Identify **safety-rated PLCs** and understand **fail-safe vs fail-operational** modes.

- [ ] **Interlock Bypass:** Manipulate **logic to disable safety interlocks** causing unsafe operational states.

- [ ] **Sensor Manipulation:** Spoof **sensor values** (temperature, pressure, level) to trigger incorrect responses.

- [ ] **Emergency Shutdown (ESD):** Understand **ESD systems** and potential for **malicious activation/deactivation**.

- [ ] **Physical Impact:** Assess **real-world consequences** of cyber attacks (equipment damage, safety incidents, environmental harm).

---

<a id="stage-4-ot-network-segmentation-defense"></a>
### **Stage 4: OT Network Segmentation & Defense** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Implement defense-in-depth for industrial environments.

- [ ] **Purdue Model:** Apply **ISA-95/Purdue Enterprise Reference Architecture** for **zone-based segmentation**.

- [ ] **DMZ Architecture:** Deploy **data diodes, unidirectional gateways** to isolate OT from IT networks.

- [ ] **Protocol Whitelisting:** Use **industrial firewalls** to whitelist **allowed protocols, function codes, device communications**.

- [ ] **Anomaly Detection:** Deploy **OT-aware IDS (Claroty, Nozomi, Dragos)** to detect **protocol deviations, unauthorized commands**.

- [ ] **Asset Inventory:** Maintain **passive discovery** of all OT assets using **network taps, SPAN ports**.

- [ ] **Patch Management:** Implement **risk-based patching** with **change control, redundancy, rollback procedures**.

---

<a id="lab-progression-part-26-oticscada-security"></a>
### **Lab Progression (Part 26: OT/ICS/SCADA Security)**

> [!TIP]
> **Goal:** Gain hands-on experience with industrial control system attacks and defenses.

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Set up GRFICSv2 or SWaT testbed and explore Modbus/DNP3 traffic with [Wireshark](Tools/Wireshark.md) | Protocol analysis report with annotated packet captures |
| 2 | Attack an OpenPLC controller in lab (scan, enumerate, modify ladder logic) | PLC exploitation walkthrough with screenshots |
| 3 | Design ICS network segmentation using Purdue Model zones and data diodes | ICS security architecture document with network diagram |

> [!IMPORTANT]
> **Move-On Gate:** You can enumerate OT protocols, explain the Purdue Model, and demonstrate safe ICS network segmentation.

---

### 🏆 Phase 6 Capstone Project

**Build an AD Forest, Attack It End-to-End, Secure It, Then Validate with Purple Teaming**

- [ ] **Build a 2-domain AD forest** (parent + child) with realistic GPOs, service accounts, and certificate services
- [ ] **Attack the entire environment** — enumerate with BloodHound, Kerberoast, escalate to Domain Admin, move laterally
- [ ] **Secure the environment** — implement tiered admin model, LAPS, disable NTLM where possible, harden ADCS
- [ ] **Validate with purple teaming** — map the attack path to MITRE ATT&CK, tune detections, and measure MTTD/MTTR
- [ ] **Verify defenses** — re-run attacks and confirm they are mitigated or detected

**Deliverables:**
- [ ] AD attack-path report with BloodHound graphs showing the complete compromise chain
- [ ] Hardening guide documenting every security control implemented
- [ ] ATT&CK heatmap and detection coverage matrix for the emulated techniques
- [ ] Before/after comparison showing which attacks were mitigated or detected
- [ ] All documentation committed to your Git repository

> [!IMPORTANT]
> **Capstone Gate:** Your report must show a complete attack chain, a complete remediation path, and purple-team validation. The before/after comparison must demonstrate measurable security improvement.

---

### 🧭 Phase 6 Reflection & Competency Check

- [ ] **Reflection:** Which enterprise surface created the most risk in your lab: identity, cloud, containers, OT/ICS, or detection gaps?
- [ ] **Reflection:** What changed after remediation, and how did you measure the improvement?
- [ ] **Competency:** Can you attack and harden AD/Entra ID paths with clear evidence?
- [ ] **Competency:** Can you explain cloud, container, and network misconfigurations in terms of blast radius?
- [ ] **Competency:** Can you run a purple team exercise that maps techniques to telemetry, detections, and remediation?

> [!IMPORTANT]
> **Phase Completion Gate:** Move on only when you can demonstrate a full enterprise attack path, document remediation, and prove measurable detection or control improvement.

---

---

<a id="shelf-04-digital-forensics"></a>
<a id="part-27"></a>

## Shelf 04: Digital Forensics


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `The Art of Memory Forensics` — Primary companion — the definitive memory forensics reference; mandatory reading
> - 🟡 `Hacking Exposed Computer Forensics Secrets & Solutions 2nd` — Full — disk and network forensics methodology
> - 🔴 `SANS DFIR Cheatsheets and Notebooks` — ⚡ Keep open during all Part 27 labs as quick reference
> - 🟡 `Effective Threat Investigation` — Full — structured threat investigation methodology and evidence chaining
> - 🟢 `Smartphone Forensics Cheatsheet by SANS` — Reference — mobile evidence acquisition quick ref


<a id="stage-1-preparation-first-response"></a>
### **Stage 1: Preparation & First Response** — `🔬 Practical`

> [!TIP]
> **Goal:** Secure the scene without corrupting evidence.

- [ ] **Incident Identification:** Trigger the `Incident Response Process` upon `Identification` of a breach.

- [ ] **Volatile Collection:** Capture RAM immediately using `memdump` before the system is powered off or rebooted.

- [ ] **Linux Memory Acquisition (LiME):** For Linux systems, use **LiME (Linux Memory Extractor)** — a loadable kernel module. Build for the target kernel version: `make` against target kernel headers. Load: `sudo insmod lime.ko path=/tmp/memory.lime format=lime`. Volatility 3 accepts LiME format directly. Use `format=raw` for Volatility 2 compatibility. For capture without writing to the local filesystem: `path=tcp:4444` streams the memory image over the network.

- [ ] **Static Acquisition:** Create a forensic image of hard drives using `[FTK Imager](Tools/FTK_Imager.md)` or `dd`, ensuring a write-blocker is used.

---

<a id="stage-2-evidence-analysis-the-deep-dive"></a>
### **Stage 2: Evidence Analysis (The Deep Dive)** — `🔬 Practical`

> [!TIP]
> **Goal:** Find the needle in the haystack.

- [ ] **Disk Analysis:** Load the evidence into `autopsy` to recover deleted files, analyze web history, and search for keywords.

- [ ] **Binary Inspection:** Use `winhex` to manually inspect file headers (signatures) to identify files with changed extensions (e.g., an EXE renamed to JPG).

- [ ] **Log Review:** Correlate actions by analyzing `Event Logs` (Login times, Service installs) and `syslogs`.

---

<a id="stage-3-memory-forensics"></a>
### **Stage 3: Memory Forensics** — `🔬 Practical`

> [!TIP]
> **Goal:** Extract evidence from volatile memory — the richest source of attacker artifacts.

- [ ] **Memory Acquisition:** Capture live RAM using **WinPMEM, DumpIt, LiME (Linux Memory Extractor)** before system shutdown. Understand **hibernation files (hiberfil.sys)** and **crash dumps** as alternative memory sources.

- [ ] **Volatility 3 Fundamentals:** Install and configure **Volatility 3**. Understand **symbol tables, ISF (Intermediate Symbol Format)**, and how to select the correct OS profile for analysis.

- [ ] **Process Analysis:** Use **pslist, pstree, malfind, handles, dlllist, cmdline** to identify **suspicious processes, injected code, hidden modules, hollowed processes**, and **unusual parent-child relationships** (e.g., svchost spawning PowerShell).

- [ ] **Network from Memory:** Extract **netscan** results to identify **active network connections, listening ports, and remote C2 addresses** that may not appear in disk-based logs.

- [ ] **Credential Extraction:** Dump **LSASS memory contents, cached domain hashes, Kerberos tickets, DPAPI master keys** from memory images to understand credential exposure scope.

- [ ] **Rootkit Detection:** Use **ssdt, idt, callbacks, driverirp, modscan** plugins to detect **kernel-mode rootkits, SSDT hooks, and hidden drivers** that are invisible to usermode tools.

- [ ] **Memory Timeline:** Extract **process creation times, loaded module timestamps, command history (consoles plugin)**, and **clipboard contents** to reconstruct attacker actions in volatile memory.

- [ ] **Named Practice Targets:** Begin with the **[MemLabs](https://github.com/stuxnet999/MemLabs)** challenge series (github.com/stuxnet999/MemLabs) using Volatility 3. Complete Labs 1–3 before moving to CyberDefenders memory forensics challenges. MemLabs images have known solutions publicly available — attempt the analysis independently first, then compare your approach to the published writeup to identify gaps in your methodology.

> [!IMPORTANT]
> **Intermediate Gate — Memory Forensics:** Before proceeding to Stage 4 (Network Forensics), you must be able to: (1) acquire a memory image from a live or offline system using WinPMEM/LiME; (2) load it into Volatility 3 with the correct symbol table; (3) identify at least one suspicious process using pslist/pstree/malfind; (4) extract network connections and at least one credential artifact. If you cannot do these four things without referencing a tutorial step-by-step, repeat Stage 3 before continuing.

---

<a id="stage-4-network-forensics"></a>
### **Stage 4: Network Forensics** — `🔬 Practical`

> [!TIP]
> **Goal:** Trace the attacker's path through network evidence.

- [ ] **Traffic Reconstruction:** Open **packet captures (PCAP)** in **[Wireshark](Tools/Wireshark.md)** to find **C2 communication patterns, data exfiltration, lateral movement, cleartext credentials**, and **DNS tunneling indicators**.

- [ ] **Flow Analysis:** When full packets are missing, use **NetFlow/sFlow/IPFIX logs** to identify **connections to malicious IPs, unusual traffic volumes, beaconing patterns (regular interval connections)**, and **data exfiltration spikes**.

- [ ] **Protocol Anomaly Detection:** Identify **protocol abuse** — DNS queries with encoded payloads, ICMP data exfiltration, HTTP/S beaconing with unusual User-Agent [strings](Tools/strings.md), encrypted traffic to non-standard ports.

- [ ] **TLS Forensics:** Analyze **JA3/JA4 fingerprints, certificate details, SNI values** to identify **malicious encrypted traffic** without decryption.

> [!IMPORTANT]
> **Intermediate Gate — Network Forensics:** Before proceeding to Stage 5 (Cloud & Mobile Forensics), you must be able to: (1) open a PCAP in Wireshark and apply protocol and string filters to isolate specific traffic; (2) identify at least one C2 beaconing pattern by regularity of interval connections; (3) reconstruct a file transfer or credential from a cleartext protocol capture; (4) identify DNS tunneling indicators from query patterns. Run Lab Level 4 (PCAP analysis for C2 and exfiltration) before moving on.

---

<a id="stage-5-cloud-mobile-forensics"></a>
### **Stage 5: Cloud & Mobile Forensics** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Collect and analyze evidence from cloud and mobile sources.

- [ ] **Cloud Log Forensics:** Analyze **AWS CloudTrail, Azure Activity Log, GCP Audit Logs** for **unauthorized access, privilege escalation, resource creation, data exfiltration, and API abuse**. Understand **log retention policies and gaps**.

- [ ] **Cloud Storage Forensics:** Examine **S3 access logs, Azure Blob storage access patterns, GCS audit logs** for **unauthorized data access, deleted object recovery, and versioning exploitation**.

- [ ] **Container Forensics:** Collect evidence from **Docker containers** (layer analysis, runtime snapshots, container diff) and **Kubernetes audit logs** (API server requests, RBAC violations, pod scheduling anomalies).

- [ ] **Mobile Device Forensics:** Extract evidence from **Android** (adb backup, JTAG, chip-off) and **iOS** (iTunes/Finder backup, Cellebrite, GrayKey) devices. Analyze **app data (SQLite databases, plist files, SharedPreferences)**, **communication logs**, and **location data**.

- [ ] **SaaS Forensics:** Collect evidence from **Microsoft 365 Unified Audit Log, Google Workspace Admin logs, Slack export** for **account compromise, data theft, insider threat investigation**.

---

<a id="stage-6-advanced-analysis-reporting"></a>
### **Stage 6: Advanced Analysis & Reporting** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Understand the "How" and tell the story.

- [ ] **Malware Analysis:** Use **static/dynamic analysis, sandbox detonation, reverse engineering** to understand malware behavior and IOCs. 📌 _Full reverse engineering methodology is covered in Part 28._

- [ ] **Timeline Construction:** Build **complete attack timeline** from artifacts (file timestamps, logs, registry, prefetch, memory, network) using **[Plaso](Tools/Plaso.md)/log2timeline, Timeline Explorer**.

- [ ] **Anti-Forensics Detection:** Look for signs of **timestomping, log clearing, secure deletion, encryption, steganography** indicating a sophisticated attacker who is actively hiding tracks.

- [ ] **Attribution Analysis:** Correlate **TTPs, IOCs, tools, infrastructure** with known threat actors using **MITRE ATT&CK, threat intelligence platforms (MISP, OpenCTI)**, and **Diamond Model** analysis.

---

<a id="stage-7-legal-reporting"></a>
### **Stage 7: Legal & Reporting** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Present findings professionally and maintain legal admissibility.

- [ ] **Chain of Custody:** Maintain strict **evidence handling, hash verification (SHA-256), transfer documentation** for legal admissibility. Understand **Daubert/Frye standards** for expert testimony.

- [ ] **Technical Report:** Document **methodology, findings, evidence location, IOCs, MITRE ATT&CK mapping** for technical teams and incident [responder](Tools/Responder.md)s.

- [ ] **Executive Summary:** Translate technical findings into **business impact, risk assessment, regulatory implications** for management and board-level communication.

- [ ] **Legal Coordination:** Work with **legal counsel, HR, law enforcement, insurance** on evidence disclosure, prosecution, breach notification, and regulatory reporting.

---

<a id="lab-progression-part-27-digital-forensics"></a>
### **Lab Progression (Part 27: Digital Forensics)**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Acquire a forensic image using FTK Imager from a lab VM | Forensic image + hash verification document |
| 2 | Analyze a memory dump with Volatility 3 (identify injected process) | Process analysis report with IOCs |
| 3 | Reconstruct attack timeline from Windows Event Logs + Prefetch + Shimcache | Timeline spreadsheet with evidence citations |
| 4 | Analyze a PCAP for C2 beaconing and data exfiltration patterns | Network forensics report |
| 5 | Complete a CyberDefenders DFIR challenge end-to-end | Full forensic report using Part 39 template |

> [!IMPORTANT]
> **Move-On Gate:** You can acquire forensic images without evidence corruption, analyze memory dumps for malware artifacts, reconstruct attack timelines from multiple evidence sources, and produce court-admissible forensic reports.

---

<a id="toc-part-28-reverse-engineering--malware-analysis"></a>
<a id="part-28-reverse-engineering-malware-analysis"></a>

---

<a id="shelf-05-reverse-engineering--malware-analysis"></a>
<a id="part-28"></a>

## Shelf 05: Reverse Engineering & Malware Analysis


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Reversing Secrets of Reverse Engineering - Eldad Eilam` — Primary companion — the foundational RE textbook; read early in Part 28
> - 🟢 `Best of Reverse Engineering` / `Reverse Engineering Hacking and Cracking` — Supplementary RE techniques
> - 🟡 `The Android Malware Handbook (2023)` — Full — mobile malware RE; use if Part 28 covers mobile malware variants
> - 🟡 `Designing BSD rootkit` — Full — rootkit internals, evasion, and persistence mechanisms
> - 🟢 `The Rootkit Arsenal Escape and Evasion in the Dark Corners` — Reference — deepest rootkit engineering reference; read after basic RE is solid


<a id="stage-1-static-analysis-foundations"></a>
### **Stage 1: Static Analysis Foundations** — `🔬 Practical`

> [!TIP]
> **Goal:** Analyze binaries without executing them.

- [ ] **File Identification:** Use **file, exiftool, DIE (Detect It Easy)** to identify **file type, architecture, compiler, packer** before loading into a disassembler.

- [ ] **PE/ELF/Mach-O Structure:** Master **executable format headers, sections (.text, .data, .rdata, .bss), import/export tables, relocation entries**, and **entry points**.

- [ ] **Disassembly Tools:** Develop proficiency in **Ghidra** (free) and **IDA Pro** (industry standard) for **disassembly, decompilation, cross-referencing, and function signature recognition**.

- [ ] **String Analysis:** Extract **hardcoded URLs, IPs, registry keys, API calls, encryption keys, error messages** using **strings, FLOSS (FLARE Obfuscated String Solver)**.

- [ ] **Import/Export Analysis:** Identify **suspicious API imports** (VirtualAlloc, CreateRemoteThread, WriteProcessMemory, InternetOpenUrl) that reveal **injection, download, or persistence behavior**.

- [ ] **Control Flow Analysis:** Trace **function call graphs, conditional branches, loops** to understand **program logic, decision points, and hidden functionality**.

- [ ] **.NET/Java Reversing:** Decompile **managed code** using **dnSpy, ILSpy** (.NET) or **JD-GUI, JADX, CFR** (Java/Android) for near-source-level analysis.

---

<a id="stage-2-dynamic-analysis-debugging"></a>
### **Stage 2: Dynamic Analysis & Debugging** — `🔬 Practical`

> [!TIP]
> **Goal:** Observe malware behavior during live execution.

- [ ] **Sandbox Execution:** Detonate samples in **isolated VMs** (FlareVM, REMnux) with **snapshots**; monitor using **[Procmon](Tools/Procmon.md), Process Hacker, Regshot, Wireshark, FakeNet-NG**.

- [ ] **Behavioral Indicators:** Document **file system changes, registry modifications, network connections, process creation, mutex creation, service installs** during execution.

- [ ] **Debugger Proficiency:** Master **[x64dbg](Tools/x64dbg.md)/x32dbg** (Windows) and **GDB with gef/pwndbg** (Linux) for **breakpoints, stepping, memory inspection, register manipulation**.

- [ ] **API Hooking & Tracing:** Use **API Monitor, Frida, strace/ltrace** to intercept and log **system calls and library calls** at runtime.

- [ ] **Memory Forensics During Execution:** Dump **process memory** with **Volatility, procdump** to find **decrypted payloads, injected code, unpacked stages** that only exist in RAM.

- [ ] **Network Traffic Analysis:** Capture **C2 communications, DNS queries, HTTP beacons, exfiltration attempts** using **Wireshark, mitmproxy, INetSim** during detonation.

> [!IMPORTANT]
> **Intermediate Gate — Dynamic Analysis:** Before proceeding to Stage 3 (Anti-Reverse Engineering & Evasion Techniques), you must demonstrate debugger capability: (1) set a breakpoint on a specific function in x64dbg or GDB and inspect register state at that point; (2) step through a loop and observe how a variable changes; (3) patch a conditional jump (`JZ`/`JNZ`) in a toy binary to force the alternate branch; (4) dump a decrypted string from memory that is not visible in static analysis. Stage 3 (anti-debugging, anti-VM, unpacking) requires this foundation — students who skip to Stage 3 without debugger proficiency will not be able to bypass anti-analysis techniques they haven't learned to interact with.

---

<a id="stage-3-anti-reverse-engineering-evasion-techniques"></a>
### **Stage 3: Anti-Reverse Engineering & Evasion Techniques** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Understand and defeat techniques malware uses to resist analysis.

- [ ] **Anti-Debugging:** Detect and bypass **IsDebuggerPresent, NtQueryInformationProcess, timing checks (RDTSC), int 2D/int 3, TLS callbacks** used to detect debuggers.

- [ ] **Anti-VM/Anti-Sandbox:** Identify checks for **VMware/VirtualBox artifacts (registry keys, MAC prefixes, CPUID), mouse movement, screen resolution, uptime, username** and patch them out.

- [ ] **Packing & Crypters:** Unpack **UPX, Themida, VMProtect, custom packers** using **manual unpacking (OEP finding, IAT reconstruction)** and automated tools.

- [ ] **Obfuscation:** Defeat **control flow flattening, dead code insertion, string encryption, opaque predicates** through **symbolic execution, pattern matching, and scripting**.

- [ ] **Code Virtualization:** Understand **VM-based protectors** (Themida, VMProtect) that translate code to **custom bytecode**; use **devirtualization techniques** and trace analysis.

---

<a id="stage-4-malware-classification-threat-intelligence"></a>
### **Stage 4: Malware Classification & Threat Intelligence** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Categorize malware and extract actionable intelligence.

- [ ] **Malware Taxonomy:** Classify samples as **RAT, ransomware, worm, rootkit, bootkit, stealer, loader, dropper, wiper, cryptominer, botnet agent** based on behavior.

- [ ] **IOC Extraction:** Extract **file hashes (MD5/SHA256), domains, IPs, URLs, mutexes, registry keys, YARA signatures** for threat intelligence sharing.

- [ ] **YARA Rule Writing:** Write **custom YARA rules** to detect malware families by **string patterns, byte sequences, file structure, import combinations**.

- [ ] **MITRE ATT&CK Mapping:** Map observed **malware behaviors** to **specific techniques/sub-techniques** for standardized reporting and detection engineering.

- [ ] **Campaign Attribution:** Correlate **code similarities, infrastructure overlaps, TTPs, timestamps, language artifacts** to link samples to **threat actor groups**.

---

<a id="stage-5-advanced-re-automation"></a>
### **Stage 5: Advanced RE & Automation** — `🔬 Practical`

> [!TIP]
> **Goal:** Scale analysis with scripting and handle complex targets.

- [ ] **Ghidra Scripting:** Write **Ghidra scripts (Java/Python)** to automate **function renaming, string decryption, pattern searching, cross-reference analysis**.

- [ ] **IDAPython:** Use **IDAPython scripts** for **bulk analysis, signature generation, automated deobfuscation, plugin development**.

- [ ] **Binary Diffing:** Use **BinDiff, Diaphora** to compare **patched vs. unpatched binaries** to identify **vulnerability patches and 1-day exploit targets**.

- [ ] **Emulation:** Use **Unicorn Engine, QEMU, Qiling** to **emulate code snippets** (decryption routines, shellcode) without full execution.

- [ ] **Firmware RE:** Apply RE skills to **embedded firmware** (binwalk extraction, architecture identification, cross-compilation debugging).

- [ ] **Kernel-Level RE:** Analyze **drivers, rootkits, bootkits** using **WinDbg kernel debugging, IDA with kernel symbols, Volatility memory analysis**.

---

<a id="lab-progression-part-28-reverse-engineering-malware-analysis"></a>
### **Lab Progression (Part 28: Reverse Engineering & Malware Analysis)**

> [!TIP]
> **Goal:** Build reverse-engineering muscle memory in a safe malware-analysis environment.

- [ ] **Lab Setup:** Deploy FLARE VM and REMnux in isolated VMs with snapshots and no shared folders.
- [ ] **Static Analysis Lab:** Analyze 5 benign or training binaries with strings, PE/ELF headers, imports, sections, and entropy.
- [ ] **Dynamic Analysis Lab:** Execute controlled samples in a sandbox and capture filesystem, registry, process, and network behavior.
- [ ] **Debugger Lab:** Use x64dbg/GDB to set breakpoints, step through functions, inspect stack/registers, and patch one branch in a toy binary.
- [ ] **YARA Lab:** Write 3 YARA rules for training samples and test false positives against clean files.
> [!IMPORTANT]
> **Move-On Gate:** Produce one malware-analysis-style report with IOCs, behavior summary, ATT&CK mapping, and detection logic.

<a id="toc-part-29-modern-exploitation"></a>
<a id="part-29-modern-exploitation"></a>

---

<a id="shelf-06-modern-exploitation"></a>
<a id="part-29"></a>

## Shelf 06: Modern Exploitation


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Hacking_ The Art Of Exploitation 2nd Edition` — Primary companion — shellcode, stack overflows, heap exploitation; read fully in Part 29
> - 🟡 `Exploit Development on Linux Platform` — Full — Linux-specific exploit writing and shellcode injection
> - 🟡 `Exploit Development Wintel Platform` — Full — Windows-specific exploit development (SEH, ROP chains)
> - 🟢 `Build Your Own EXPLOITS` — Full — practical exploit building projects from concept to working PoC


> **Prerequisite Gate:** Complete Part 1 Stages 3–4 (Memory Management, Data Representation), Part 1 Stage 7 (C fundamentals), and Part 42 (Offensive Development — exploit writing, shellcode, assembly) before starting this Part. Modern exploitation builds directly on these foundations.

<a id="stage-1-recon-triage-tooling"></a>
### **Stage 1: Recon, Triage & Tooling** — `🔬 Practical`

> [!TIP]
> **Goal:** Prepare targets and environments for exploit development.

- [ ] **Binary Recon:** Identify **arch, compiler, protections (ASLR, DEP/NX, PIE, RELRO, Stack Canaries, CFG, CET/PAC/BTI)**.

- [ ] **Debug Setup:** Configure **GDB/gef/pwndbg, WinDbg, Frida**; obtain **symbols, PDBs, DWARF** where possible.

- [ ] **Fuzzing:** Use **AFL++, libFuzzer, honggfuzz, Peach**; seed corpora, add **sanitizers (ASan/UBSan/MSan)**; triage crashes.

---

<a id="stage-2-memory-exploitation-userland"></a>
### **Stage 2: Memory Exploitation (Userland)** — `🔬 Practical`

> [!TIP]
> **Goal:** Exploit memory-safety bugs under modern mitigations.

- [ ] **Buffer Overflows:** Master how data can overwrite adjacent memory to hijack the **EIP/RIP (Instruction Pointer)**; understand **stack vs heap overflows**.

- [ ] **Stack/Heap Primitives:** Develop **overflow, UAF, double-free, type confusion, OOB read/write** primitives.

- [ ] **Bypass Strategies:** Use **ROP/JOP/SROP, ret2libc, ret2dlresolve, stack pivoting**, and **heap grooming** (tcache/fastbin/largebin, LFH) to gain PC control.

- [ ] **Exploit Mitigations:** Study **ASLR** (Address Space Layout Randomization) and **DEP/NX** (Data Execution Prevention); master **ROP** (Return Oriented Programming) to bypass them. Learn **stack canary** bypass via leaks.

- [ ] **Mitigation Bypass:** Defeat **RELRO/PIE**, **CFG/CET/PAC/BTI** with **COOP, SIGRETURN, pointer authentication bypass**, or **JIT spraying**.

- [ ] **Sandbox Escape:** Target **browser/render sandboxes**, **container seccomp/AppArmor**, and **Win32k lockdown** using **IPC/shmem/race** primitives.

---

<a id="stage-3-advanced-targets"></a>
### **Stage 3: Advanced Targets** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Move beyond basic binaries to complex environments.

- [ ] **Kernel Exploitation:** Leverage **UAF/race/logic bugs**, bypass **SMEP/SMAP/KASLR/KPTRR**, and use **token stealing/privilege escalation** primitives.

- [ ] **Browser & JS Engines:** Exploit **JIT/IC/GC** bugs; chain **type confusion → infoleak → RCE → sandbox escape**.

- [ ] **Deserialization & Logic:** Exploit **Java/.NET/Python/PHP** gadget chains, **serialization format** confusion, and **race conditions**.

- [ ] **Cloud/Serverless:** Abuse **function sandboxes, cold-start leaks, metadata services (IMDS), and SSRF-to-role** chains.

---

<a id="stage-4-exploit-delivery-opsec"></a>
### **Stage 4: Exploit Delivery & OPSEC** — `🔬 Practical`

> [!TIP]
> **Goal:** Deliver and operate exploits stealthily.

- [ ] **Stagers & Payloads:** Build **stageless/staged** payloads with **in-memory loaders, reflective DLL/ELF**, and **syscall/indirect syscall** execution.

- [ ] **Evasion:** Apply **sleep obfuscation, call-stack spoofing, DLL hollowing, APC/ETW/AMSI tampering**, and **PPID spoofing**.

- [ ] **Crash Handling:** Implement **auto-retry, watchdogs, safe-fail** to avoid blue screens/service crashes.

- [ ] **Telemetry Shaping:** Throttle **network/beacon timing**, pad **packet sizes**, and mimic **legit protocol usage**.

---

<a id="stage-5-post-exploitation-hardening-safety"></a>
### **Stage 5: Post-Exploitation Hardening & Safety** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Maintain control while minimizing detection and impact.

- [ ] **Cleanup & Rollback:** Remove **artifacts, logs, crash dumps**, restore configs; support **idempotent rollback**.

- [ ] **Persistence Choices:** Select **low-noise persistence** (scheduled tasks, services, WMI events, cron/systemd timers) with **time-bounded lifetimes**.

- [ ] **Safety & Blast Radius:** Gate exploit use with **kill-switches, rate limits, environment checks**, and **canary endpoints** to avoid collateral damage.

---

<a id="lab-progression-part-29-modern-exploitation"></a>
### **Lab Progression (Part 29: Modern Exploitation)**

> [!TIP]
> **Goal:** Approach exploitation with prerequisites, safety controls, and repeatable labs.

- [ ] **Assembly Gate:** Complete x86/x64 basics: registers, stack frames, calling conventions, `call`, `ret`, jumps, and memory layout.
- [ ] **pwn.college / ROP Emporium Lab:** Complete beginner shellcode, stack overflow, and ROP exercises before touching harder targets.
- [ ] **Fuzzing Lab:** Build a toy parser, fuzz it, crash it, triage the crash, and write a minimal proof of concept.
- [ ] **Mitigation Lab:** Demonstrate how NX, ASLR, stack canaries, PIE, and RELRO change exploitability.
> [!IMPORTANT]
> **Move-On Gate:** Produce one exploit writeup with root cause, crash analysis, exploit reliability notes, and mitigation guidance.

<a id="toc-part-30-hardware-hacking--embedded-systems"></a>

---

<a id="shelf-07-hardware-hacking--embedded-systems"></a>
<a id="part-30"></a>

## Shelf 07: Hardware Hacking & Embedded Systems


<a id="stage-1-hardware-reconnaissance"></a>
### **Stage 1: Hardware Reconnaissance** — `🔬 Practical`

> [!TIP]
> **Goal:** Identify attack surface on physical devices.

- [ ] **Chip Identification:** Identify **MCU/SoC models** by reading chip markings; research **datasheets, known vulnerabilities**.

- [ ] **PCB Analysis:** Trace **PCB layouts** to identify **debug ports, test points, memory chips, communication buses**.

- [ ] **Debug Port Discovery:** Locate **JTAG, UART, SPI, I2C** interfaces using **multimeter, logic analyzer, JTAGulator**.

- [ ] **Pinout Mapping:** Use **oscilloscope** to identify **TX/RX pins, clock signals, voltage levels** on unknown headers.

- [ ] **Firmware Extraction:** Dump firmware via **debug interfaces, external flash chip reading, bootloader exploits**.

---

<a id="stage-2-firmware-analysis"></a>
### **Stage 2: Firmware Analysis** — `🔬 Practical`

> [!TIP]
> **Goal:** Reverse engineer and find vulnerabilities in firmware.

- [ ] **Binary Extraction:** Use **binwalk** to extract **filesystems, compressed data, encryption keys** from firmware images.

- [ ] **Architecture Identification:** Determine **CPU architecture (ARM, MIPS, x86)** using **file, binwalk, Ghidra**.

- [ ] **Filesystem Analysis:** Mount extracted **SquashFS, JFFS2, UBIFS** to analyze **configs, credentials, certificates**.

- [ ] **Static Analysis:** Reverse engineer binaries with **Ghidra, IDA Pro, radare2** to find **buffer overflows, backdoors, hardcoded keys**.

- [ ] **Crypto Analysis:** Extract **encryption keys, certificates, private keys** from firmware for decryption or impersonation.

> [!NOTE]
> **Supply Chain Hardware Implants — Awareness Sidebar:** Physical hardware supply chain attacks represent a distinct threat class from software supply chain. Security practitioners advising on infrastructure procurement, critical infrastructure protection, or high-security environments should understand this threat model:
> - **BIOS/UEFI Implants:** Malicious firmware installed in the BIOS/UEFI before delivery or during maintenance can survive OS reinstallation, disk replacement, and most forensic investigation. Detection requires specialised firmware scanning tools (Binarly, Eclypsium) or manual ROM extraction.
> - **BMC (Baseboard Management Controller) Compromise:** BMCs (iDRAC, iLO, IPMI) run independently of the host OS and provide out-of-band management. A compromised BMC has full control over the server regardless of host-level security controls. High-profile research: Bloomberg's 2018 reporting on alleged implanted microchips (denied by vendors but introduced the threat model to mainstream discourse); real BMC vulnerabilities (e.g., Supermicro iDRAC RCE CVEs) are well-documented.
> - **Malicious NICs and PCIe Devices:** PCIe devices perform Direct Memory Access (DMA) — a compromised NIC firmware can read and write host memory directly, bypassing the OS security model entirely. IOMMU (Intel VT-d, AMD-Vi) is the primary mitigation; verify it is enabled in the BIOS.
> - **NIST SP 800-161 (Supply Chain Risk Management):** The framework for managing hardware and software supply chain risk in federal and critical infrastructure contexts. Covers: supplier assurance, secure acquisition procedures, hardware bill of materials (HBOM), and tamper-evident packaging.
> - **Practical Detection:** Firmware integrity measurement via TPM 2.0 Secure Boot, Eclypsium or Binarly firmware scanning, and hardware SBOM (H-SBOM) tracking are the current mitigations. This is not routine pentesting scope — it is architectural risk management for high-value targets.

---

<a id="stage-3-runtime-exploitation"></a>
### **Stage 3: Runtime Exploitation** — `🔬 Practical`

> [!TIP]
> **Goal:** Execute code on live embedded systems.

- [ ] **UART Shell Access:** Connect to **UART** to gain **root shell, bootloader access, kernel logs**.

- [ ] **JTAG Debugging:** Use **OpenOCD, Segger J-Link** to **halt CPU, dump memory, modify registers, inject code**.

- [ ] **Bootloader Exploitation:** Exploit **U-Boot, grub** vulnerabilities to gain **pre-OS execution, modify boot parameters**.

- [ ] **Secure Boot Bypass:** Understand the mechanics used to load malicious, persistent bootloaders before OS security kicks in; master techniques like **boot chain manipulation, secure enclave exploitation, TPM/fTPM bypass**.

- [ ] **Memory Corruption:** Exploit **buffer overflows, format string bugs** in embedded applications.

- [ ] **Firmware Modification:** Patch firmware to **disable authentication, add backdoors, modify functionality**; reflash device.

---

<a id="stage-4-side-channel-physical-attacks"></a>
### **Stage 4: Side-Channel & Physical Attacks** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Extract secrets through non-traditional attack vectors.

- [ ] **Power Analysis:** Use **ChipWhisperer** for **simple/differential power analysis (SPA/DPA)** to extract encryption keys.

- [ ] **Electromagnetic Analysis:** Capture **EM emissions** during crypto operations to recover secrets.

- [ ] **Fault Injection:** Use **voltage glitching, clock glitching** to skip security checks or expose hidden functionality.

- [ ] **Chip Decapping:** Perform **acid decapping** to expose die for **optical inspection, probing, reverse engineering**.

- [ ] **Bus Snooping:** Intercept **SPI/I2C traffic** between chips to capture **flash contents, key exchange, commands**.

---

<a id="stage-5-iot-embedded-defense"></a>
### **Stage 5: IoT & Embedded Defense** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Secure embedded systems against attacks.

- [ ] **Secure Boot:** Implement **cryptographic boot chain verification** to prevent unauthorized firmware.

- [ ] **Debug Port Protection:** Disable or lock **JTAG/SWD** in production; use **debug authentication**.

- [ ] **Encrypted Firmware:** Encrypt firmware images; implement **secure firmware updates** with signature verification.

- [ ] **Tamper Detection:** Add **physical tamper switches, mesh overlays, epoxy coating** to detect intrusion.

- [ ] **Hardware Security Modules:** Use **TPM, secure elements (SE), TrustZone** for key storage and secure execution.

- [ ] **Code Signing:** Sign all firmware and application code; verify signatures before execution.

---

<a id="lab-progression-part-30-hardware-hacking-embedded-systems"></a>
### **Lab Progression (Part 30: Hardware Hacking & Embedded Systems)**

> [!TIP]
> **Goal:** Gain hands-on experience with hardware and embedded system attacks.

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Extract firmware from a consumer IoT device (router, IP camera) using binwalk and analyze the filesystem | Firmware analysis report with extracted credentials/keys |
| 2 | Gain UART shell access on a lab device, dump flash via SPI, and modify firmware | Hardware exploitation walkthrough with photos |
| 3 | Perform side-channel power analysis using ChipWhisperer on a target implementing AES | Side-channel attack report with key recovery evidence |

> [!IMPORTANT]
> **Move-On Gate:** You can extract and analyze firmware, gain debug shell access, and explain side-channel attack fundamentals.

---

<a id="toc-part-31-password-cracking--hash-analysis"></a>



---

<a id="shelf-08-physical-penetration-testing"></a>
<a id="part-32"></a>

## Shelf 08: Physical Penetration Testing


> **Safety Gate:** Physical testing requires written authorization, named locations, dates/times, emergency contacts, stop conditions, and a get-out-of-jail letter. Do not practice bypasses on real facilities, campuses, offices, hotels, apartments, or transit systems.

<a id="stage-1-pre-engagement-reconnaissance"></a>
### **Stage 1: Pre-Engagement & Reconnaissance** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Plan the physical assessment within legal scope.

- [ ] **Scope Definition:** Confirm **written authorization, target facilities, allowed hours, assumed identity (e.g., contractor, vendor)**, and **emergency abort contact** before any physical operation.

- [ ] **Facility OSINT:** Use **Google Maps, Satellite imagery, LinkedIn (employee badge photos), job postings (physical security tools mentioned), public filings** to map facility layout, entry points, and security posture.

- [ ] **Physical Observation:** Conduct **covert surveillance** — observe **employee badge behavior, delivery procedures, tailgate vulnerability, smoking areas, loading docks** as low-security entry vectors.

- [ ] **Social Engineering Pretext:** Prepare **believable personas** (IT contractor, fire inspector, HVAC technician, delivery person) with **supporting props, business cards, uniforms, fake work orders**.

---

<a id="stage-2-entry-access-control-bypass"></a>
### **Stage 2: Entry & Access Control Bypass** — `🔬 Practical`

> [!TIP]
> **Goal:** Defeat physical barriers to gain facility access.

- [ ] **Tailgating / Piggybacking:** Follow authorized personnel through secured doors using **timing, props (heavy boxes, hands full), social confidence**; test anti-tailgate detection systems.

- [ ] **Lock Picking:** Practice **single-pin picking, raking, bump keys** for standard pin-tumbler locks; understand **high-security locks (Medeco, Abloy)** that resist standard attacks.

- [ ] **Bypass Tools:** Use **under-door tools (UDT), latch slipping tools, door gap attacks** to manipulate door hardware without the key.

- [ ] **RFID/NFC Badge Cloning:** Capture **low-frequency (125kHz HID, EM4100)** badge data with **Proxmark3** from up to 30cm; clone to blank T5577 card; understand **13.56MHz (MIFARE, DESFire)** attack complexity.

- [ ] **Electric Strike / Maglock Bypass:** Use **REX (Request-to-Exit) sensor exploitation, power interruption, crash bar manipulation** to open magnetically locked doors.

- [ ] **Elevator & Stairwell Access:** Identify **fire escape stairwells, service elevators, parking garage access** that bypass reception and security desks.

---

<a id="stage-3-hid-usb-payload-attacks"></a>
### **Stage 3: HID & USB Payload Attacks** — `🔬 Practical`

> [!TIP]
> **Goal:** Deploy physical implants and hardware attack tools.

- [ ] **USB HID Attacks (Rubber Ducky / Bash Bunny):** Craft **DuckyScript payloads** to execute **reverse shells, credential theft, backdoor installation** within seconds when plugged into an unlocked machine.

- [ ] **O.MG Cable:** Deploy **USB cables with embedded implants** that appear legitimate but exfiltrate data or execute commands over WiFi.

- [ ] **LAN Turtle / Shark Jack:** Drop **network implants** that provide **remote SSH access, packet capture, and network scanning** from inside the target network.

- [ ] **USB Drop Attacks:** Leave **weaponized USB drives** in common areas (parking lot, reception, bathroom); craft **autorun payloads, LNK files, fake docs** that execute on Windows/Linux.

- [ ] **Rogue Network Devices:** Plant **WiFi Pineapple, rogue AP, network tap** in server rooms, comms closets, or under desks for persistent network access.

---

<a id="stage-4-on-site-operations-data-collection"></a>
### **Stage 4: On-Site Operations & Data Collection** — `🔬 Practical`

> [!TIP]
> **Goal:** Achieve objectives once inside.

- [ ] **Workstation Access:** Target **unlocked machines, password-protected screens (bypass with HID)**, install **implants, keyloggers, screen capture tools**.

- [ ] **Shoulder Surfing:** Observe **password entry, sensitive documents, screen content** in open offices, meeting rooms, and public areas.

- [ ] **Dumpster Diving:** Recover **printed credentials, org charts, hardware serial numbers, network diagrams, decommissioned drives** from trash/recycling.

- [ ] **Server Room / Comms Closet:** Attempt access to **network switches, patch panels, servers**; document **unencrypted hardware, unsecured console ports, accessible management interfaces**.

---

<a id="stage-5-reporting-physical-findings"></a>
### **Stage 5: Reporting Physical Findings** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Document and communicate physical security gaps professionally.

- [ ] **Evidence Collection:** Capture **covert photos/video (within ROE), cloned badge data, dropped USB recovery, access logs** as proof-of-concept evidence.

- [ ] **Risk Mapping:** Map findings to **physical security frameworks (PSIA, ISO 27001 Annex A.11)** and quantify **business impact** (data theft, sabotage, insider threat facilitation).

- [ ] **Remediation Guidance:** Recommend **anti-tailgate turnstiles, RFID upgrade paths, clean desk policy, USB port lockdown, security awareness training, camera placement**.

---

<a id="lab-progression-part-32-physical-penetration-testing"></a>
### **Lab Progression (Part 32: Physical Penetration Testing)**

> [!TIP]
> **Goal:** Gain hands-on experience with physical security assessment techniques.

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Practice lock picking on a training lock set (transparent locks + standard pin tumbler) | Lock bypass skills log with technique notes |
| 2 | Clone a low-frequency RFID badge using Proxmark3 and demonstrate access control bypass in lab | Badge cloning walkthrough with Proxmark3 output |
| 3 | Build and deploy a Rubber Ducky/Bash Bunny payload that establishes a reverse shell within 10 seconds | HID attack payload with demo video and detection guidance |

> [!IMPORTANT]
> **Move-On Gate:** You can pick a standard pin tumbler lock, clone a low-frequency RFID badge, and craft a working HID payload.

---

<a id="toc-part-33-voip--telecommunications-security"></a>

---

<a id="shelf-09-voip--telecommunications-security"></a>
<a id="part-33"></a>

## Shelf 09: VoIP & Telecommunications Security


<a id="stage-1-voip-protocol-fundamentals"></a>
### **Stage 1: VoIP Protocol Fundamentals** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Understand how VoIP systems communicate.

- [ ] **SIP (Session Initiation Protocol):** Master **SIP message structure (INVITE, ACK, BYE, REGISTER, OPTIONS)**, **dialog establishment**, **authentication (Digest Auth)**, and **common ports (UDP/TCP 5060, TLS 5061)**.

- [ ] **RTP (Real-time Transport Protocol):** Understand **media stream transport**, **SRTP (Secure RTP)** for encryption, **RTCP** for control, and how **RTP ports are negotiated via SDP**.

- [ ] **VoIP Infrastructure:** Map **components**: **IP-PBX (Asterisk, FreePBX), SBC (Session Border Controller), SIP Trunk, softphones, IP handsets, voicemail servers**.

- [ ] **Codec Identification:** Identify **G.711, G.729, Opus** codecs from SDP negotiation; understand quality vs. bandwidth tradeoffs and how codecs affect capture/decode.

---

<a id="stage-2-voip-reconnaissance-enumeration"></a>
### **Stage 2: VoIP Reconnaissance & Enumeration** — `🔬 Practical`

> [!TIP]
> **Goal:** Discover and map VoIP infrastructure.

- [ ] **SIP Scanning:** Use **svmap (SIPVicious), [nmap](Tools/Nmap.md) SIP NSE scripts** to discover **SIP-enabled devices, extensions, PBX software versions**.

- [ ] **Extension Enumeration:** Use **svwar** to enumerate **valid SIP extensions** via REGISTER/OPTIONS probing; map **active users and voicemail accounts**.

- [ ] **Banner Grabbing:** Identify **PBX vendor and version** from **SIP User-Agent headers**; cross-reference with **CVE databases** for known exploits.

- [ ] **SDP Analysis:** Parse **Session Description Protocol** messages to identify **media types, codec preferences, RTP port ranges, and IP addresses**.

---

<a id="stage-3-voip-attacks"></a>
### **Stage 3: VoIP Attacks** — `🔬 Practical`

> [!TIP]
> **Goal:** Exploit weaknesses in VoIP deployments.

- [ ] **SIP Brute Force:** Use **svcrack (SIPVicious)** to brute-force **SIP extension passwords**; test default credentials (1234, extension number as password).

- [ ] **RTP Interception:** Position in MITM via **ARP spoofing**; capture **RTP streams with Wireshark**; reassemble and decode audio with **VoIPmonitor, sngrep, rtpbreak**.

- [ ] **Call Hijacking:** Send **spoofed BYE messages** to terminate active calls; send **CANCEL or re-INVITE** to redirect calls to attacker-controlled endpoints.

- [ ] **VoIP Fuzzing:** Use **Sip-Proxy, Codenomicon** to fuzz **SIP parsers** for crashes, memory corruption, and denial of service in PBX software.

- [ ] **Vishing Infrastructure:** Understand how **VoIP enables scalable vishing** — spoofed caller ID, auto-dialers, SIP trunk abuse for mass calling campaigns.

- [ ] **VLAN Hopping to Voice VLAN:** Exploit **voice VLAN misconfiguration** (untagged/double-tagged frames) to access VoIP network segment from data VLAN.

---

<a id="stage-4-ss7-telecom-signaling-attacks"></a>
### **Stage 4: SS7 & Telecom Signaling Attacks** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Understand mobile network signaling vulnerabilities.

- [ ] **SS7 Architecture:** Understand **Signaling System 7 (SS7)** — the global telephone signaling protocol connecting **mobile network operators, MSCs, HLRs, VLRs**.

- [ ] **SS7 Attack Types:** Study **location tracking (SendRoutingInfo), call interception (MAP UpdateLocation), SMS interception (ForwardSM)** — attacks that work against **any mobile network globally**.

- [ ] **Diameter Protocol:** Understand **Diameter** (4G/LTE replacement for SS7) and its own **attack surface** — roaming exploitation, subscriber data disclosure, DoS.

- [ ] **SIM Swapping (Technical):** Understand the **social engineering + SS7/carrier abuse chain** — porting credentials, carrier authentication weaknesses, and MFA bypass consequences.

- [ ] **IMSI Catchers (Stingrays):** Understand how **fake base stations force 2G downgrade**, capture **IMSI identifiers**, and enable **passive interception** of unencrypted traffic.

---

<a id="stage-5-5g-security"></a>
### **Stage 5: 5G Security** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Understand the 5G threat landscape.

- [ ] **5G Architecture:** Understand **5G SA (Standalone) vs NSA (Non-Standalone)**, **gNB (base station), AMF, SMF, UPF** core network functions, and **network slicing**.

- [ ] **5G Attack Surface:** Study **SBA (Service-Based Architecture) HTTP/2 API attacks**, **SUPI/SUCI identifier exposure**, **slice isolation bypass**, **roaming security gaps**.

- [ ] **5G vs 4G Security:** Understand improvements (**SUPI concealment, mandatory mutual auth**) and remaining weaknesses (**legacy 2G/3G fallback, roaming interfaces**).

---

<a id="stage-6-defense-hardening"></a>
### **Stage 6: Defense & Hardening** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Secure VoIP and telecom infrastructure.

- [ ] **SRTP Enforcement:** Mandate **SRTP** for all media streams and **TLS (SIP over TLS/SIPS)** for signaling; disable unencrypted SIP on all production systems.

- [ ] **SBC Hardening:** Configure **Session Border Controllers** to perform **topology hiding, rate limiting, anomaly detection, and geographic call blocking**.

- [ ] **Authentication Hardening:** Enforce **strong SIP digest passwords**, implement **IP allowlisting** for SIP trunks, disable **anonymous REGISTER**.

---

<a id="lab-progression-part-33-voip-telecommunications-security"></a>
### **Lab Progression (Part 33: VoIP & Telecommunications Security)**

> [!TIP]
> **Goal:** Gain hands-on experience with VoIP and telecommunications attacks.

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Set up Asterisk PBX in lab, register SIP clients, and capture SIP/RTP traffic in Wireshark | VoIP protocol analysis report with call flow diagrams |
| 2 | Perform SIP enumeration (svmap, svwar) and eavesdrop on an unencrypted call using Wireshark RTP playback | VoIP exploitation walkthrough with audio extraction evidence |
| 3 | Harden the lab PBX with SRTP, TLS, and SBC rules; verify that previous attacks no longer work | VoIP hardening report with before/after comparison |

> [!IMPORTANT]
> **Move-On Gate:** You can enumerate SIP infrastructure, capture and replay VoIP calls, and harden a PBX with SRTP/TLS.

---

<a id="toc-part-34-blockchain--web3-security"></a>

---

<a id="shelf-10-blockchain--web3-security"></a>
<a id="part-34"></a>

## Shelf 10: Blockchain & Web3 Security


<a id="stage-1-blockchain-fundamentals-for-security"></a>
### **Stage 1: Blockchain Fundamentals for Security** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Understand how blockchain and smart contracts work before attacking them.

- [ ] **Blockchain Mechanics:** Master **distributed ledger, consensus mechanisms (PoW, PoS, PoA)**, **immutability, transaction finality, mempool**, and **public/private key cryptography** in blockchain context.

- [ ] **Smart Contract Architecture:** Understand **EVM (Ethereum Virtual Machine)**, **Solidity language basics**, **ABI (Application Binary Interface)**, **bytecode vs. source code**, and **contract deployment lifecycle**.

- [ ] **DeFi Ecosystem:** Map **protocols**: **DEXs (Uniswap, Curve), lending (Aave, Compound), oracles (Chainlink), bridges, yield aggregators** — understand how they interact and compose.

- [ ] **Wallet Security:** Understand **EOA (Externally Owned Accounts) vs contract wallets**, **seed phrases (BIP39), HD derivation paths, hardware wallets (Ledger, Trezor)**, and **private key storage risks**.

---

<a id="stage-2-smart-contract-vulnerabilities"></a>
### **Stage 2: Smart Contract Vulnerabilities** — `🔬 Practical`

> [!TIP]
> **Goal:** Identify and exploit common Solidity security flaws.

- [ ] **Reentrancy Attacks:** Exploit **recursive external calls before state updates** (The DAO hack pattern); understand `checks-effects-interactions` as the fix; test with **Hardhat/Foundry**.

- [ ] **Integer Overflow/Underflow:** Exploit **arithmetic overflow in Solidity <0.8.0** (e.g., `uint256 balance = 0; balance -= 1;` wraps to MAX); understand SafeMath and Solidity 0.8 built-in checks.

- [ ] **Access Control Flaws:** Find **missing `onlyOwner` modifiers, tx.origin authentication, unprotected `initialize()` functions** in upgradeable contracts.

- [ ] **Logic Flaws & Business Logic Errors:** Exploit **incorrect assumptions** about token prices, balances, or state — often unique to each protocol's design.

- [ ] **Flash Loan Attacks:** Understand **uncollateralized loans within a single transaction**; exploit **oracle price manipulation, liquidity pool imbalances, governance attacks** using flash loans.

- [ ] **Oracle Manipulation:** Exploit **reliance on on-chain DEX spot price as oracle** — manipulate pool price via large swap, exploit contracts that trust it, profit.

- [ ] **Front-Running & MEV:** Understand **Maximal Extractable Value** — sandwich attacks, arbitrage, and liquidation front-running by miners/validators in the mempool.

---

<a id="stage-3-smart-contract-auditing-methodology"></a>
### **Stage 3: Smart Contract Auditing Methodology** — `🔬 Practical`

> [!TIP]
> **Goal:** Systematically audit contracts for vulnerabilities.

- [ ] **Static Analysis Tools:** Use **Slither, MythX, Aderyn, Semgrep Solidity rules** to automatically detect common vulnerability patterns.

- [ ] **Symbolic Execution:** Use **Manticore, Echidna (fuzzer), Halmos (formal verification)** to find edge cases not caught by static analysis.

- [ ] **Manual Code Review:** Read contract logic line-by-line; trace **all external calls, state transitions, and access control checks**; verify invariants hold under all conditions.

- [ ] **PoC in Foundry/Hardhat:** Write **test exploits in Foundry (`forge test`)** forking mainnet to demonstrate real attack viability without deploying to live chain.

- [ ] **Audit Report Writing:** Document findings with **severity (Critical/High/Medium/Low/Informational), impact, likelihood, proof-of-concept, and recommended fix**.

---

<a id="stage-4-web3-infrastructure-attacks"></a>
### **Stage 4: Web3 Infrastructure Attacks** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Attack the broader Web3 ecosystem beyond smart contracts.

- [ ] **Wallet Drainer Attacks:** Understand **malicious `approve()` / `permit()` signatures** that give attackers unlimited token spending rights; study **phishing sites** targeting Web3 users.

- [ ] **Bridge Attacks:** Analyze **cross-chain bridge vulnerabilities** (Ronin $625M, Wormhole $320M) — **validator compromise, signature replay, logic errors in lock/mint mechanisms**.

- [ ] **NFT Security:** Examine **metadata centralization risks, royalty bypass, reentrancy in `onERC721Received`**, and **enumeration attacks** on NFT collections.

- [ ] **Private Key Extraction:** Study attack vectors — **weak entropy in key generation, compromised RNG, phishing for seed phrases, clipboard hijackers, malicious browser extensions**.

- [ ] **RPC Node Attacks:** Understand **exposure of `eth_accounts`, `personal_sign` on misconfigured nodes**; test for **open JSON-RPC endpoints** that can sign transactions.

---

<a id="stage-5-defense-secure-development"></a>
### **Stage 5: Defense & Secure Development** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Build secure smart contracts and Web3 applications.

- [ ] **Security Patterns:** Implement **checks-effects-interactions, pull-over-push payments, rate limiting, circuit breakers (pause mechanisms)** in contract design.

- [ ] **Upgradeable Contract Security:** Use **OpenZeppelin Upgrades Plugins**; understand **storage collision risks, initializer protection, proxy admin key management**.

- [ ] **Formal Verification:** Apply **Certora Prover or K Framework** to mathematically prove critical invariants hold under all possible inputs.

- [ ] **Bug Bounties:** Engage **Immunefi, Code4rena, Sherlock** for smart contract audits and bug bounties; understand **responsible disclosure in Web3 context**.

---

<a id="lab-progression-part-34-blockchain-web3-security"></a>
### **Lab Progression (Part 34: Blockchain & Web3 Security)**

> [!TIP]
> **Goal:** Gain hands-on experience with smart contract auditing and Web3 attacks.

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Complete Ethernaut and Damn Vulnerable DeFi (first 10 challenges each) | Challenge solutions with exploit code and vulnerability explanations |
| 2 | Audit a sample smart contract using Slither + manual review; write a finding report | Smart contract audit report with severity ratings and PoC |
| 3 | Write a Foundry test that demonstrates a flash loan attack against a vulnerable DeFi protocol on a mainnet fork | Flash loan exploit PoC with Foundry test code and impact analysis |

> [!IMPORTANT]
> **Move-On Gate:** You can identify common Solidity vulnerabilities, write Foundry exploit tests, and produce a professional smart contract audit report.

---

### 🏆 Phase 7 Capstone Project

**Perform Malware Analysis on a Real-World Sample OR Write an Exploit for a Known CVE**

Choose one track:

**Track A — Malware Analysis:**
- [ ] Obtain a real-world malware sample from MalwareBazaar or VirusTotal
- [ ] Perform static analysis (PE headers, strings, imports, YARA matching)
- [ ] Perform dynamic analysis (sandbox execution, API monitoring, network traffic)
- [ ] Reverse engineer key functions in IDA/Ghidra
- [ ] Produce a malware analysis report with IOCs (hashes, C2s, YARA rules)

**Track B — Exploit Development:**
- [ ] Select a known CVE with a public advisory (1-day exploit)
- [ ] Analyze the vulnerability root cause (buffer overflow, use-after-free, etc.)
- [ ] Develop a working proof-of-concept exploit in a controlled lab
- [ ] Document the exploitation process and mitigation strategies

**Deliverables:**
- [ ] Professional malware report with IOCs OR exploit writeup with PoC code
- [ ] All analysis artifacts committed to your Git repository

> [!IMPORTANT]
> **Capstone Gate:** Your deliverable must be technical enough to submit to a threat intel team (Track A) or a security research publication (Track B).

---

### 🧭 Phase 7 Reflection & Competency Check

- [ ] **Reflection:** Which advanced domain deserves continued depth, and which optional domains should you intentionally skip for now?
- [ ] **Reflection:** Where did you rely on tooling without fully understanding the underlying artifact, binary, or exploit primitive?
- [ ] **Competency:** Can you produce either a defensible malware analysis report or a working exploit writeup with controlled proof?
- [ ] **Competency:** Can you explain limitations, assumptions, and safety boundaries for your research?
- [ ] **Competency:** Can another technical reviewer reproduce your analysis from your notes and artifacts?

> [!IMPORTANT]
> **Phase Completion Gate:** Move on only when your advanced work is deep, reproducible, ethically scoped, and polished enough for expert review.

---

<a id="toc-part-35-governance-risk--compliance-grc"></a>

---

<a id="shelf-11-governance-risk--compliance-grc"></a>
<a id="part-35"></a>

## Shelf 11: Governance, Risk & Compliance (GRC)


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🟡 `CISSP Study Guide 4th Edition` — Reference — broad governance, risk, and compliance framework coverage
> - 🔴 `Foundations of Information Security - Jason Andress` — Security policy and risk management fundamentals
> - 🟢 `The Practical Guide to HIPAA Privacy and Security Compliance 2nd` — Reference — compliance framework depth for healthcare/regulated environments


<a id="stage-1-security-frameworks-standards"></a>
### **Stage 1: Security Frameworks & Standards** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Understand the regulatory and standards landscape that defines what pentesters test against.

- [ ] **NIST Cybersecurity Framework (CSF):** Master the **5 functions (Identify, Protect, Detect, Respond, Recover)** and how they map to security controls.

- [ ] **NIST 800-53 / 800-171:** Understand **security control families** (Access Control, Audit, Incident Response) used in **federal and defense** compliance.

- [ ] **ISO 27001/27002:** Know the **ISMS (Information Security Management System)** framework, **Annex A controls**, and **certification audit process**.

- [ ] **CIS Controls (v8):** Master the **18 Critical Security Controls** as a prioritized, actionable defense checklist; understand **Implementation Groups (IG1-IG3)**.

- [ ] **MITRE ATT&CK as Compliance:** Use **ATT&CK coverage mapping** to demonstrate detection maturity against specific adversary techniques.

---

<a id="stage-2-industry-regulations-legal-requirements"></a>
### **Stage 2: Industry Regulations & Legal Requirements** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Know the laws and regulations that dictate security requirements across industries.

- [ ] **PCI-DSS (Payment Card Industry):** Understand the **12 requirements** for protecting cardholder data; know **scope reduction (network segmentation), SAQ types**, and how pentesters validate Requirement 11.3.

- [ ] **HIPAA (Healthcare):** Understand **PHI (Protected Health Information)** safeguards, **technical/administrative/physical** controls, and **breach notification requirements**.

- [ ] **GDPR (EU Data Protection):** Know **data subject rights, lawful basis for processing, Data Protection Impact Assessments (DPIA), breach notification (72-hour rule)**, and **extraterritorial scope**.

- [ ] **SOC 2 (Service Organizations):** Understand **Trust Services Criteria (Security, Availability, Processing Integrity, Confidentiality, Privacy)** and how pentest findings map to SOC 2 reports.

- [ ] **SOX (Sarbanes-Oxley):** Know **IT General Controls (ITGCs)** for financial system integrity — **access control, change management, backup/recovery**.

- [ ] **DPDP Act (India):** Understand **India's Digital Personal Data Protection Act** — consent-based processing, Data Fiduciary obligations, cross-border transfer rules, and **Board penalties**.

- [ ] **Computer Fraud & Abuse Act (CFAA):** Understand US federal law on **unauthorized access**; know how **scope of engagement** and **written authorization** protect pentesters legally.

- [ ] **Privacy Engineering & LINDDUN:**

  Privacy engineering applies threat modelling methodology to privacy risks — analogous to STRIDE for security threats. LINDDUN identifies seven privacy threat categories against data flows:

  | Threat | Description | Example |
  |--------|-------------|---------|
  | **L**inkability | Link data items/actions across contexts | Correlating user sessions across services |
  | **I**dentifiability | Identify individuals from supposedly anonymous data | Re-identifying users from "anonymised" datasets via quasi-identifiers |
  | **N**on-repudiation | User cannot deny actions they took | Immutable audit logs expose user behaviour to third parties |
  | **D**etectability | Detect existence of data or actions | Timing attacks revealing whether a username exists |
  | **D**isclosure | Expose personal data to unauthorised parties | S3 bucket misconfiguration exposing PII |
  | **U**nawareness | Users don't know what data is collected/processed | Dark patterns hiding data collection in ToS |
  | **N**on-compliance | Processing data in violation of regulations | Missing GDPR consent mechanism or retention policy |

  - [ ] **GDPR Article 25 — Privacy by Design:** Controllers must implement data protection by design and default. In practice: data minimisation (collect only what is necessary), purpose limitation (don't reuse data), pseudonymisation of personal data at rest, default-secure settings (maximum privacy by default, not maximum functionality).

  - [ ] **Data Minimisation as a Security Control:** Systems that collect minimal data have a smaller breach impact. A breach of a pseudonymised dataset is lower severity than a breach of a plaintext PII store. Implement: field-level encryption for sensitive attributes, tokenisation for payment data, synthetic data for test environments.

  - [ ] **Consent Management Architecture:** GDPR requires demonstrable, granular, revocable consent. Architecture implications: consent management platform (CMP) stores per-user per-purpose consent flags, consent is checked before each processing operation, consent withdrawal triggers downstream data deletion cascade. Understand how consent audit logs work and why they must be tamper-evident.

  - [ ] **Privacy Impact Assessment (DPIA/PIA):** Required under GDPR Article 35 for high-risk processing. Process: (1) describe processing, (2) assess necessity and proportionality, (3) identify and assess risks using LINDDUN, (4) identify controls to mitigate risks, (5) consult DPA if residual risk is high. Security architects participate in DPIAs for new systems.

---

<a id="stage-3-risk-management-assessment"></a>
### **Stage 3: Risk Management & Assessment** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Quantify and communicate risk so findings drive action.

- [ ] **Risk Equation:** Master **Risk = Threat × Vulnerability × Impact** and use it to **prioritize findings** over raw CVSS scores.

- [ ] **Risk Assessment Methodologies:** Understand **NIST 800-30 (qualitative), FAIR (quantitative), OCTAVE, CRAMM** for structured risk evaluation.

- [ ] **Threat Modeling:** Apply **STRIDE, PASTA, Attack Trees** to proactively identify **threats to systems before testing** and guide scope selection.

- [ ] **Business Impact Analysis (BIA):** Map **technical vulnerabilities to business consequences** — revenue loss, reputational damage, regulatory fines, operational downtime.

- [ ] **Risk Appetite & Tolerance:** Understand how organizations define **acceptable risk levels** and how pentest recommendations must align with business context.

---

<a id="stage-4-audit-scope-compliance-testing"></a>
### **Stage 4: Audit, Scope & Compliance Testing** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Execute engagements that satisfy compliance requirements.

- [ ] **Scoping for Compliance:** Define pentest scope to cover **specific compliance requirements** (e.g., PCI-DSS Req 11.3 requires internal/external pentest + segmentation testing).

- [ ] **Control Validation:** Test whether **implemented controls** (MFA, encryption, logging, access controls) actually function as documented in policies.

- [ ] **Evidence Collection:** Gather **screenshots, logs, packet captures, configuration exports** formatted for **auditor review** and compliance documentation.

- [ ] **Gap Analysis Reporting:** Identify **missing controls, partial implementations, policy violations** and map them to **specific framework requirements** with remediation guidance.

- [ ] **Third-Party Risk:** Assess **vendor/supplier security posture** via **questionnaires, pentest scoping, SLA review**, and **supply chain risk evaluation**.

- [ ] **Continuous Compliance:** Understand shift from **point-in-time audits** to **continuous monitoring, automated compliance checks, and DevSecOps integration**.

---

<a id="lab-progression-part-35-governance-risk-compliance"></a>
### **Lab Progression (Part 35: Governance, Risk & Compliance)**

> [!TIP]
> **Goal:** Make GRC practical by producing audit-ready artifacts.

- [ ] **Risk Register Lab:** Build a risk register for your home lab or a sample SaaS system with likelihood, impact, owner, treatment, and due date.
- [ ] **Policy Lab:** Write one access-control policy and one incident-response policy with scope, roles, exceptions, and review cadence.
- [ ] **Control Mapping Lab:** Map 10 technical controls to NIST CSF, CIS Controls, or ISO 27001 Annex A.
- [ ] **Vendor Risk Lab:** Create a lightweight vendor security questionnaire and score a fictional third-party service.
- [ ] **Business Continuity Lab:** Write a basic BIA and recovery priority list for a sample business process.
> [!IMPORTANT]
> **Move-On Gate:** Produce an audit evidence pack with policy, risk register, control mapping, and remediation plan.

<a id="toc-part-36-supply-chain-security"></a>
<a id="part-36-supply-chain-security"></a>

---

<a id="shelf-12-supply-chain-security"></a>
<a id="part-36"></a>

## Shelf 12: Supply Chain Security


<a id="stage-1-understanding-the-attack-surface"></a>
### **Stage 1: Understanding the Attack Surface** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Map how software and hardware dependencies become attack vectors.

- [ ] **Supply Chain Threat Model:** Understand the **three attack vectors**: compromised **source code** (SolarWinds), compromised **build/distribution** (XZ Utils backdoor), and compromised **dependencies** (event-stream npm).

- [ ] **SBOM (Software Bill of Materials):** Generate and analyze **SBOM (CycloneDX, SPDX format)** to inventory all third-party components, transitive dependencies, and their known CVEs.

- [ ] **Dependency Inventory:** Map **direct + transitive dependencies** across package ecosystems (**npm, PyPI, Maven, NuGet, RubyGems**) to understand total exposed surface.

---

<a id="stage-2-dependency-package-attacks"></a>
### **Stage 2: Dependency & Package Attacks** — `🔬 Practical`

> [!TIP]
> **Goal:** Exploit weaknesses in open-source package ecosystems.

- [ ] **Dependency Confusion:** Register **public packages with the same name** as internal private packages; force targets to download your malicious version when their registry falls back to public PyPI/npm.

- [ ] **Typosquatting:** Publish packages with **names one keystroke away** from popular packages (`reqeusts`, `colourama`, `crypt0`) to catch developer typos during `pip install`.

- [ ] **Malicious Package Injection:** Study real cases (**event-stream, PyTorch-nightly, ctx**) where **legitimate packages were backdoored** post-compromise of the maintainer account.

- [ ] **Version Pinning Attacks:** Target packages using **unpinned `latest`** or **broad version ranges** (`>=1.0`); understand how **lock files (package-lock.json, Pipfile.lock)** mitigate this.

- [ ] **Protestware & Intentional Sabotage:** Understand cases where **maintainers intentionally introduced bugs/wipes** (colors.js, node-ipc) and the supply chain trust model risks this exposes.

---

<a id="stage-3-build-system-cicd-attacks"></a>
### **Stage 3: Build System & CI/CD Attacks** — `🔬 Practical`

> [!TIP]
> **Goal:** Compromise the pipeline that produces software.

- [ ] **Pipeline Poisoning:** Inject **malicious steps into CI/CD workflows** (GitHub Actions, Jenkins, GitLab CI) to **steal secrets, alter artifacts, plant backdoors** in compiled output.

- [ ] **Workflow Injection:** Exploit **untrusted input in GitHub Actions expressions** (`${{ github.event.pull_request.title }}`) to achieve **command injection in CI runners**.

- [ ] **Secrets Exfiltration:** Steal **CI/CD secrets (API keys, deploy tokens, signing certs)** from **environment variables, GitHub Secrets, HashiCorp Vault** during pipeline execution.

- [ ] **Artifact Tampering:** Replace **legitimate build artifacts** post-build but pre-deployment; understand **artifact signing (Sigstore/Cosign)** as a defense.

- [ ] **SLSA Framework:** Understand **Supply-chain Levels for Software Artifacts (SLSA)** maturity model (L1-L4) and what each level proves about build provenance.

---

<a id="stage-4-open-source-third-party-risk"></a>
### **Stage 4: Open-Source & Third-Party Risk** — `🔬 Practical`

> [!TIP]
> **Goal:** Assess and test third-party component security.

- [ ] **OSS Vulnerability Scanning:** Use **Trivy, Grype, Snyk, OWASP Dependency-Check** to scan project dependencies for **known CVEs** and **license violations**.

- [ ] **Maintainer Account Takeover:** Understand how **compromised npm/PyPI maintainer accounts** (via credential stuffing or social engineering) enable **silent package backdooring**.

- [ ] **Repo Jacking:** Exploit **GitHub repository namespace reuse** — when a user changes their username, old repo URLs can be claimed by attackers to serve malicious packages.

- [ ] **Trojanized Tooling:** Test environments for **compromised developer tools** (malicious VS Code extensions, backdoored CLI tools, modified build systems).

---

<a id="stage-5-defense-verification"></a>
### **Stage 5: Defense & Verification** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Know how to validate supply chain integrity.

- [ ] **Sigstore / Cosign:** Verify **container image and artifact signatures** to ensure provenance; understand **keyless signing with OIDC identity**.

- [ ] **Dependency Pinning:** Enforce **exact version pinning + hash verification** in lock files; use **Renovate/Dependabot** for automated safe updates.

- [ ] **Private Registries:** Maintain **internal package mirrors (Artifactory, Nexus)** with **allowlisting** to prevent dependency confusion attacks.

- [ ] **Code Signing:** Implement **code signing for all releases**; verify signatures in deployment pipelines before execution.

---

<a id="toc-part-37-devsecops--secure-sdlc"></a>
<a id="part-37-devsecops-secure-sdlc"></a>

---

<a id="shelf-13-devsecops--secure-sdlc"></a>
<a id="part-37"></a>

## Shelf 13: DevSecOps & Secure SDLC


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Security for Software Engineers` — Full — secure SDLC, threat modeling, SAST/DAST concepts; maps directly to this Part
> - 🟡 `Web Application Security - Andrew Hoffman` — Reference — secure code patterns from an AppSec engineer perspective


<a id="stage-1-security-in-the-development-lifecycle"></a>
### **Stage 1: Security in the Development Lifecycle** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Understand where security integrates across the SDLC.

- [ ] **SDLC Security Gates:** Map **security activities to SDLC phases** — threat modeling (design), SAST (code), SCA (build), DAST (test), pentest (pre-release), monitoring (production).

- [ ] **Shift-Left Security:** Understand the **cost and benefit model** — finding a bug in design costs 10x less than finding it in production; align testing earlier in the cycle.

- [ ] **Threat Modeling:** Apply **STRIDE to application architecture** — identify **Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege** risks before coding.

- [ ] **Threat Modeling Tool Lab (Threat Dragon / Microsoft Threat Modeling Tool):**

  Threat modelling is only useful when done in a tool that produces reviewable, version-controlled artefacts. Description-only threat models in documents become stale within weeks.

  **Hands-on exercise:** Take a simple 3-tier web application (frontend → API → database + third-party auth):

  1. **Install [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/)** (Electron app or web version at `https://www.threatdragon.com/`). Alternatively use **[Microsoft Threat Modeling Tool](https://aka.ms/threatmodelingtool)** (Windows).

  2. **Construct the Data Flow Diagram (DFD):**
     - Place: user browser, load balancer, API server, database, auth provider (OAuth IdP), admin dashboard
     - Draw data flows between each component
     - Assign **trust boundaries** — what crosses a trust level (internet → DMZ, DMZ → internal, internal → DB)
     - Mark each flow as in-scope or out-of-scope

  3. **Apply STRIDE to each element and flow:**
     - For every trust boundary crossing: what Spoofing, Tampering, or Elevation threat exists?
     - For every data store: what Information Disclosure or Tampering threat exists?
     - For every process: what Denial of Service or Repudiation threat exists?

  4. **Record the output:** Threat Dragon produces a threat list with per-threat severity, status (mitigated/not mitigated), and mitigation description. Export it as JSON and commit to Git.

  5. **Map to controls:** For each identified threat, document: (1) existing control, (2) whether the control is sufficient, (3) recommended additional control if not.

  - [ ] **Microsoft Threat Modeling Tool alternative:** SDL-based; generates threats automatically from DFD element types. Useful for Windows/Azure-centric architectures. Produces a `.tm7` file with threat list and mitigation suggestions.

  - [ ] **Threat Modelling in CI/CD:** Understand that threat models should be updated when architecture changes. Link threat model review to pull request gates for architecture-impacting changes (new data flows, new trust boundaries, new external integrations).

- [ ] **Secure Design Principles:** Master **least privilege, defense-in-depth, fail securely, complete mediation, open design, separation of privilege** as architectural requirements.

---

<a id="stage-2-static-analysis-sast"></a>
### **Stage 2: Static Analysis (SAST)** — `🔬 Practical`

> [!TIP]
> **Goal:** Find vulnerabilities in source code without executing it.

- [ ] **SAST Tools:** Use **Semgrep, SonarQube, Checkmarx, Bandit (Python), Brakeman (Rails), SpotBugs (Java)** to scan source code for **injection flaws, insecure crypto, hardcoded secrets**.

- [ ] **Custom SAST Rules:** Write **Semgrep rules** to detect **organization-specific insecure patterns** (custom crypto usage, missing input validation in internal frameworks).

- [ ] **False Positive Management:** Triage SAST output — distinguish **true positives, false positives, and low-risk findings**; suppress noise without hiding real issues.

- [ ] **IDE Integration:** Understand how **security plugins (Snyk IDE, SonarLint, Semgrep VS Code)** give developers **real-time feedback** during coding.

---

<a id="stage-3-dynamic-analysis-dast-iast"></a>
### **Stage 3: Dynamic Analysis (DAST & IAST)** — `🔬 Practical`

> [!TIP]
> **Goal:** Test running applications for security flaws.

- [ ] **DAST Tools:** Use **[OWASP ZAP](Tools/OWASP_ZAP.md), [Burp Suite](Tools/Burp_Suite.md) Pro (automated scan), [Nikto](Tools/Nikto.md)** to **black-box test** running applications for **OWASP Top 10 vulnerabilities** in CI pipelines.

- [ ] **IAST (Interactive Application Security Testing):** Understand how **IAST agents (Contrast Security, Seeker)** instrument running code to detect vulnerabilities from the inside during functional tests.

- [ ] **API DAST:** Configure **ZAP or Burp** with **OpenAPI specs** to automatically fuzz all API endpoints for **injection, auth bypass, and BOLA**.

- [ ] **Authenticated Scanning:** Configure DAST tools with **session cookies or API keys** to test **post-login functionality** inaccessible to anonymous scans.

---

<a id="stage-4-software-composition-analysis-sca"></a>
### **Stage 4: Software Composition Analysis (SCA)** — `🔬 Practical`

> [!TIP]
> **Goal:** Find vulnerabilities in third-party dependencies.

- [ ] **SCA Tools:** Use **Snyk, Dependabot, OWASP Dependency-Check, Black Duck** to continuously scan **package manifests** for **CVEs, outdated versions, license violations**.

- [ ] **Vulnerability Prioritization:** Understand **reachability analysis** — not every CVE in a dependency is exploitable; prioritize based on **actual code paths** that use the vulnerable function.

- [ ] **License Compliance:** Identify **copyleft licenses (GPL, AGPL)** that may require open-sourcing proprietary code; flag **license conflicts** in dependency trees.

---

<a id="stage-5-secrets-detection-pipeline-security"></a>
### **Stage 5: Secrets Detection & Pipeline Security** — `🔬 Practical`

> [!TIP]
> **Goal:** Prevent credential leakage through code and pipelines.

- [ ] **Secrets Scanning:** Use **truffleHog, gitleaks, git-secrets** to scan **git history** (not just current HEAD) for **API keys, passwords, private keys, connection [strings](Tools/strings.md)**.

- [ ] **Pre-commit Hooks:** Install **pre-commit framework with detect-secrets or gitleaks** to block secret commits before they reach the remote repository.

- [ ] **Pipeline Hardening & Poison Pipeline Execution (PPE) Defense:**
  - **PPE Attack Mechanics:** Understand Direct Poison Pipeline Execution (D-PPE) via malicious PR branch modifications to `.github/workflows/` and Indirect Poison Pipeline Execution (I-PPE) by poisoning build scripts (`Makefile`, `package.json` scripts) executed by privileged runners.
  - **Runner Security:** Understand risks of unhardened self-hosted runners (ephemeral vs persistent runners, Docker-in-Docker socket breakouts, accessing cloud instance metadata from runners).
  - **CI Service Accounts & OIDC:** Apply **least-privilege to CI service accounts**, replace long-lived static cloud keys with **short-lived OIDC federated tokens** (e.g., GitHub OIDC to AWS STS via `assume-role-with-web-identity`), and scope permissions to **minimum required per job**.

- [ ] **Container Image Security:** Scan **base images and Dockerfiles** with **Trivy, Dockle** for CVEs, misconfigurations, and secrets baked into image layers.

- [ ] **IaC Security:** Scan **Terraform, CloudFormation, Helm charts** with **Checkov, tfsec, kics** for **open security groups, public storage, missing encryption, IAM over-permission**.

<a id="secure-coding-pipeline-lab-progression"></a>
### **Secure Coding & Pipeline Lab Progression**

> [!TIP]
> **Goal:** Prove you can prevent vulnerabilities, not only scan for them.

- [ ] **Secure Coding Fix Lab:** Take a small vulnerable app and fix SQL injection, XSS, command injection, path traversal, insecure deserialization, weak auth, and insecure direct object reference patterns.
- [ ] **Code Review Lab:** Review one intentionally vulnerable repository and produce findings with file/line references, exploitability notes, and safe remediation.
- [ ] **GitHub Actions Security Lab:** Build a CI pipeline with Semgrep, gitleaks, Trivy, dependency scanning, and artifact upload.
- [ ] **Break-the-Build Gate:** Configure the pipeline to fail on critical secrets, critical dependency CVEs, and high-confidence SAST findings.
- [ ] **Threat Model Lab:** Draw a DFD for a sample app and map trust boundaries, abuse cases, and required controls.
> [!IMPORTANT]
> **Move-On Gate:** Produce a before/after report showing vulnerable code, fixed code, tests, and CI evidence.

---

<a id="part-37b-secure-code-review-methodology"></a>

---

<a id="shelf-14-secure-code-review-methodology"></a>
<a id="part-37b"></a>

## Shelf 14: Secure Code Review Methodology


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Web Application Security - Andrew Hoffman` — Primary — identifies vulnerable patterns (SQL sinks, XSS outputs, insecure deserialization) in code
> - 🟡 `Security for Software Engineers` — Reference — secure coding patterns across languages


> **Why This Exists:** Automated SAST tools (Part 37) find obvious patterns. Manual code review finds business logic flaws, subtle injection paths, and authentication bypasses that scanners miss entirely. Every AppSec engineer, bug bounty hunter targeting open-source programs, and red teamer reviewing client source code needs this methodology. You cannot triage and improve SAST results without understanding what the scanner is looking for and why it misses things.

<a id="stage-1-code-review-workflow"></a>
### **Stage 1: Code Review Workflow & Entry Point Mapping** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Develop a repeatable, systematic workflow for reviewing any codebase — regardless of language or framework.

- [ ] **Step 1 — Orient:** Understand the technology stack, framework, and architecture before reading code. Identify: language(s), framework (Django, Spring, Rails, Express, Laravel), ORM, template engine, authentication library, and serialization format. Each has known vulnerability classes.

- [ ] **Step 2 — Map Entry Points:** Find all places where **user-controlled input** enters the application:
  - HTTP parameters: `request.GET['id']`, `req.body`, `$_POST['user']`, `@RequestParam`
  - HTTP headers: `request.headers['X-Forwarded-For']`, `Cookie`, `Referer`, `User-Agent` (some apps use these)
  - File uploads: multipart form data, file path parameters
  - WebSocket messages, GraphQL inputs, gRPC parameters
  - Environment variables and config files (for injection into commands/queries)
  - **Rule:** Any variable that originates from user input is a **source**. Track it until it reaches a **sink**.

- [ ] **Step 3 — Identify Dangerous Sinks:** Find where data is *used* in dangerous ways:
  - **SQL Sinks:** `cursor.execute()`, `query()`, `findOne()`, raw string SQL construction
  - **Command Sinks:** `os.system()`, `subprocess.run(shell=True)`, `Runtime.exec()`, `exec()`, `popen()`
  - **Template Sinks:** `render_template_string()`, `Jinja2.from_string()`, `Template(user_input)`
  - **HTML Sinks:** `innerHTML =`, `document.write()`, `.html()` in jQuery, `dangerouslySetInnerHTML` in React
  - **Deserialization Sinks:** `pickle.loads()`, `yaml.load()`, `ObjectInputStream.readObject()`, `unserialize()`
  - **File Sinks:** `open(user_input)`, `fopen()`, `readFile()`, `sendFile()` — path traversal territory
  - **Redirect Sinks:** `redirect(user_input)`, `res.redirect()` — open redirect territory

- [ ] **Step 4 — Trace Source to Sink:** For each dangerous sink, trace backward to find if user input can reach it without sufficient sanitization or parameterization. This is **taint analysis** — the core technique of both manual review and SAST.

- [ ] **Step 5 — Check Sanitization Quality:** Identify what sanitization exists between source and sink:
  - **Parameterized queries:** `cursor.execute("SELECT * FROM users WHERE id = %s", (user_id,))` — correct; cannot inject
  - **String concatenation:** `cursor.execute("SELECT * FROM users WHERE id = " + user_id)` — vulnerable
  - **Regex allowlists:** `re.match(r'^[0-9]+$', user_id)` — allowlisting is strong if correctly anchored
  - **Regex denylists:** Blacklisting specific characters — almost always bypassable
  - **Output encoding:** `html.escape()`, `{{ variable }}` in most template engines — prevents XSS if applied correctly

- [ ] **Step 6 — Check Authentication & Authorization:** For every sensitive action (read sensitive data, modify data, admin function), verify:
  - Is the user authenticated? (Session/JWT check before action)
  - Is the user authorized? (Does the code check the user's permission for the *specific* resource they're accessing, not just any resource?)
  - Look for missing `@login_required`, missing ownership checks, and horizontal privilege escalation (user A accessing user B's data)

---

<a id="stage-2-language-specific-patterns"></a>
### **Stage 2: Language-Specific Vulnerability Patterns** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Know which dangerous functions and patterns appear in each major language/framework so you can grep for them efficiently.

**PHP:**
- [ ] `include($user_input)` / `require($user_input)` — **Local/Remote File Inclusion** (LFI/RFI); any user-controlled path is dangerous
- [ ] `eval($user_input)` / `assert($user_input)` — **Code Injection**; rarely legitimate
- [ ] `extract($_POST)` / `extract($_GET)` — **Variable Injection**; overwrites any variable in scope with attacker-controlled values
- [ ] `unserialize($user_input)` — **PHP Object Injection**; can trigger `__wakeup()`/`__destruct()` magic methods → RCE
- [ ] `preg_replace('/pattern/e', $replacement, $input)` — **Code Execution via deprecated /e modifier** (PHP < 7.0)
- [ ] `$_SERVER['PHP_SELF']` used in form action — **XSS via URL manipulation**
- [ ] Grep targets: `eval(`, `system(`, `exec(`, `passthru(`, `shell_exec(`, `include(`, `require(`, `unserialize(`, `extract(`

**Python:**
- [ ] `pickle.loads(user_data)` — **Arbitrary code execution** via `__reduce__` method; any deserialization of untrusted pickle data is critical
- [ ] `yaml.load(user_data)` (without `Loader=yaml.SafeLoader`) — **Code execution** via YAML tags; always use `yaml.safe_load()`
- [ ] `subprocess.run(user_input, shell=True)` / `os.system(user_input)` — **Command injection**; `shell=True` makes input injection trivial
- [ ] `eval(user_input)` / `exec(user_input)` — **Code injection**; almost never legitimate with user input
- [ ] `render_template_string(user_input)` in Flask / `Template(user_input).render()` in Jinja2 — **Server-Side Template Injection (SSTI)**
- [ ] `open(user_input)` with path from request — **Path traversal** if not normalized with `os.path.realpath()`
- [ ] Grep targets: `pickle.loads`, `yaml.load(`, `eval(`, `exec(`, `shell=True`, `render_template_string(`, `Template(`

**Java:**
- [ ] `ObjectInputStream.readObject()` — **Java deserialization** — one of the highest-impact patterns; exploitable with gadget chains (ysoserial)
- [ ] `Runtime.getRuntime().exec(userInput)` — **Command injection** if user input is not tokenized
- [ ] `String query = "SELECT * FROM users WHERE id = '" + id + "'"` — **SQL injection** via string concatenation; must use `PreparedStatement`
- [ ] XXE (XML External Entity): `DocumentBuilderFactory` without `setFeature("http://apache.org/xml/features/disallow-doctype-decl", true)` — if parsing user XML, XXE can read local files or SSRF
- [ ] `new File(userInput).getCanonicalPath()` without verifying it starts with the intended base path — **Path traversal**
- [ ] JNDI injection (`${jndi:ldap://...}`) — Log4Shell pattern; search for `log.info(userInput)` combined with Log4j usage
- [ ] Grep targets: `readObject()`, `Runtime.exec(`, `Statement.execute(`, `DocumentBuilderFactory`, `getRuntime().exec(`

**JavaScript / Node.js:**
- [ ] `eval(userInput)` / `new Function(userInput)()` — **Code injection**
- [ ] Prototype pollution: `obj[userKey] = userValue` where `userKey` can be `__proto__` — can modify Object.prototype and affect all objects in the process
- [ ] `innerHTML = userInput` / `document.write(userInput)` — **DOM XSS**; use `textContent` instead
- [ ] `child_process.exec(userInput)` / `child_process.execSync(userInput)` — **Command injection**; use `execFile` with argument arrays
- [ ] `require(userInput)` — **Path traversal to arbitrary module loading** if user controls the module path
- [ ] `res.redirect(req.query.next)` without allowlist validation — **Open redirect**
- [ ] Grep targets: `eval(`, `innerHTML`, `document.write(`, `child_process.exec(`, `__proto__`, `prototype[`, `dangerouslySetInnerHTML`

---

<a id="stage-3-semgrep-custom-rules"></a>
### **Stage 3: Semgrep & Custom Rule Writing** — `🔬 Practical`

> [!NOTE]
> **Part 37 vs Part 37B — Same Tool, Different Purpose:** Part 37 Stage 2 used Semgrep as a **CI/CD pipeline tool** — running pre-built rulesets automatically on every commit to catch regressions at scale. This stage teaches **Semgrep rule writing for manual code auditing** — a fundamentally different skill. Here you write custom rules targeting your specific codebase, tune for zero false positives, and use taint tracking to trace sources to sinks. If you ran `semgrep --config=auto` in Part 37 and thought you were done: you weren't. Rule authorship is the skill that separates automated scanning from genuine code review.

> [!TIP]
> **Goal:** Automate pattern matching for language-specific vulnerability patterns using Semgrep rules — the industry standard for lightweight, accurate code auditing.

- [ ] **Semgrep Basics:** Install with `pip install semgrep`. Run a scan: `semgrep --config=auto path/to/code`. Understand rule structure:
  ```yaml
  rules:
    - id: python-yaml-unsafe-load
      pattern: yaml.load(...)
      message: Use yaml.safe_load() to prevent code execution
      languages: [python]
      severity: ERROR
  ```

- [ ] **Pattern Matching Syntax:** Learn Semgrep's metavariables (`$X`, `$...ARGS`), ellipsis operators (`...`), and pattern-not for allowlisting:
  ```yaml
  pattern: $OBJ.execute($QUERY)
  pattern-not: $OBJ.execute($QUERY, $PARAMS)
  ```
  This matches `.execute(query)` (vulnerable concatenation) but not `.execute(query, params)` (parameterized — safe).

- [ ] **Taint Tracking:** Use `mode: taint` in Semgrep to trace sources to sinks automatically:
  ```yaml
  mode: taint
  pattern-sources:
    - pattern: request.args.get(...)
  pattern-sinks:
    - pattern: cursor.execute(...)
  ```

- [ ] **Run Existing Rulesets:** `semgrep --config=p/owasp-top-ten` — runs OWASP Top 10 patterns. `semgrep --config=p/python` — language-specific rules. Review all findings critically — Semgrep has false positives.

- [ ] **Triage False Positives:** Mark known safe patterns with `# nosemgrep: rule-id` inline comment. Document the rationale. Semgrep suppressions are audit evidence that the finding was reviewed.

---

<a id="lab-progression-part-37b"></a>
### **Lab Progression (Part 37B: Secure Code Review)**

| Level | Task | Deliverable |
|---|---|---|
| 1 | Clone DVWA or WebGoat; identify 5 vulnerable functions by reading source code only (no exploitation) | Vulnerability list with file/line references and CWE IDs |
| 2 | Run `semgrep --config=auto` against a small Python/PHP project; triage all findings (true positive, false positive, needs-context) | Triaged findings report with rationale for each decision |
| 3 | Write 3 custom Semgrep rules targeting patterns not covered by default rulesets in your target language | 3 working Semgrep `.yaml` rule files with test cases |
| 4 | Review one GitHub open-source project (~5k–20k lines); produce a findings report with file:line references, exploitability rating, and remediation code | Professional code review report |
| 5 | Attempt code review challenge on HackTheBox or PortSwigger Academy (source code review labs) | Lab completion + write-up |

> [!IMPORTANT]
> **Move-On Gate (Part 37B):** Given an unfamiliar 500-line Python or PHP file with 3 planted vulnerabilities, you can identify all 3 within 30 minutes using a structured source-to-sink methodology without running the application. You can write a Semgrep rule that correctly identifies the vulnerability class and produces zero false positives on a safe variant.

---

<a id="toc-part-43-security-architecture--engineering"></a>
<a id="part-43-security-architecture-engineering"></a>

---

<a id="shelf-15-security-architecture--engineering"></a>
<a id="part-43"></a>

## Shelf 15: Security Architecture & Engineering


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🟡 `CISSP Study Guide 4th Edition` — Reference — security architecture domains (network, identity, cryptography, physical)
> - 🟡 `Foundations of Information Security - Jason Andress` — Architecture and design security principles
> - 🟢 `Cybersecurity First Principles A Reboot of Strategy and Tactics` — Full — strategic security architecture thinking


> **Numbering Note:** Part 43 is numbered non-sequentially. It belongs here in Phase 8 because security architecture and engineering requires GRC context (Part 35), supply chain awareness (Part 36), and DevSecOps experience (Parts 37/37B) as prerequisites. It does not follow Part 42 in the learning sequence — Part 42 is in Phase 7 (Offensive Development & Tooling).

_Phase 8 — Governance, Supply Chain, DevSecOps & Architecture | This module fills the identified gap in security architecture training. A security professional who can only break systems but not design secure ones is incomplete._


<a id="stage-1-security-design-principles"></a>
### **Stage 1: Security Design Principles** — `🧠 Conceptual`

- [ ] **Defense-in-Depth as Architecture:** Design layered defenses where no single control failure compromises the system. Map controls to **preventative, detective, corrective, and compensating** categories.

- [ ] **Least Privilege & Separation of Duties:** Apply these principles to **network design, IAM, application architecture**, and **data access** across all tiers.

- [ ] **Fail-Safe Defaults:** Design systems that **deny by default**, require explicit grants, and **fail closed** rather than open.

- [ ] **Security by Design:** Integrate security from **requirements through deployment**, not as a bolt-on. Understand **NIST Secure Software Development Framework (SSDF)** and **OWASP SAMM**.

<a id="stage-2-zero-trust-architecture"></a>
### **Stage 2: Zero Trust Architecture** — `🧠 Conceptual`

- [ ] **Zero Trust Principles:** Understand **"never trust, always verify"** across **identity, device, network, application, and data** pillars.

- [ ] **NIST SP 800-207:** Study the **Zero Trust Architecture** publication — understand **Policy Engine, Policy Administrator, Policy Enforcement Point** components.

- [ ] **Identity-Centric Security:** Design access control around **identity verification (MFA, SSO, RBAC/ABAC)** rather than network location.

- [ ] **Microsegmentation:** Implement **network microsegmentation** to isolate workloads. Understand **east-west traffic monitoring** and **lateral movement prevention**.

- [ ] **Continuous Verification:** Design systems that **re-authenticate and re-authorize** based on **context changes** (location, device health, behavior anomalies).

- [ ] **ZTNA / SASE Product Landscape:**

  ZTNA (Zero Trust Network Access) replaces VPN with identity-aware, least-privilege application access. SASE (Secure Access Service Edge) bundles ZTNA, SWG, CASB, FWaaS, and SD-WAN into a cloud-delivered platform. As a security architect or pentester, you will encounter these in every large enterprise.

  | Product | Vendor | Type | Architecture |
  |---------|--------|------|-------------|
  | **Zscaler Internet Access (ZIA)** | Zscaler | SWG + CASB + FWaaS | Cloud-delivered proxy; all user traffic tunnelled to Zscaler PoPs |
  | **Zscaler Private Access (ZPA)** | Zscaler | ZTNA | App connector in datacenter; user never touches the network — only the app |
  | **Palo Alto Prisma Access** | Palo Alto | SASE | NGFW policy + GlobalProtect + CASB in cloud |
  | **Cloudflare Access** | Cloudflare | ZTNA | Identity-aware proxy; JWT-based per-request auth; integrates with Okta/Azure AD |
  | **Microsoft Entra Private Access** | Microsoft | ZTNA | Replaces VPN for Azure-integrated environments; Conditional Access integration |

  - [ ] **How ZTNA Replaces VPN:** Traditional VPN grants network access (wide blast radius on credential theft). ZTNA grants *application* access — the user's device never joins the corporate network. A compromised ZTNA session can access one app, not the entire network. Understand: connector-based ZTNA (Zscaler ZPA) vs. reverse-proxy ZTNA (Cloudflare Access).

  - [ ] **Pentesting ZTNA Environments:** ZTNA changes the attack surface:
    - Initial access via phishing still works — you get identity, not network
    - Lateral movement is constrained — no network access means no ARP poisoning, no LLMNR poisoning
    - Focus shifts to: OAuth token theft, SSO session hijacking, ZTNA connector compromise (connector is on the internal network — compromise it for internal access)
    - Cloud CASB bypass: traffic to unapproved cloud apps via split tunnelling gaps

<a id="stage-3-network-security-architecture"></a>
### **Stage 3: Network Security Architecture** — `🧠 Conceptual`

- [ ] **Network Segmentation Design:** Design **DMZ, internal zones, management zones, database zones** with proper **firewall rules and ACLs** between them.

- [ ] **Reference Architectures:** Study **SABSA (Sherwood Applied Business Security Architecture)** and **TOGAF security architecture** for enterprise design patterns.

- [ ] **Cloud Security Architecture:** Design secure **VPC/VNet layouts, security groups, NACLs, private endpoints, transit gateways**, and **hub-spoke network topologies** for AWS/Azure/GCP.

- [ ] **Secure Remote Access:** Design **VPN, ZTNA (Zero Trust Network Access), SASE** architectures for remote workforce security. _(ZTNA product detail in Stage 2 above.)_

- [ ] **CNAPP (Cloud-Native Application Protection Platform):**

  CNAPP unifies CSPM, CWPP, CIEM, and IaC scanning into a single platform. Cloud security engineers are expected to understand this tooling category — it has replaced standalone CSPM/CWPP tools in most enterprise cloud security programmes.

  | Component | What it covers | Standalone tool equivalent |
  |-----------|---------------|---------------------------|
  | **CSPM** (Cloud Security Posture Management) | Cloud configuration misconfigurations | Prowler, ScoutSuite |
  | **CWPP** (Cloud Workload Protection) | VM/container/serverless runtime threats | Falco, Sysdig |
  | **CIEM** (Cloud Infrastructure Entitlement Management) | Overpermissioned IAM roles, lateral movement paths | IAM Access Analyzer |
  | **IaC Scanning** | Misconfigurations in Terraform, Bicep, CloudFormation | Checkov, tfsec |
  | **CNAPP** | All of the above unified with a shared data model and attack path analysis | Wiz, Lacework, Orca Security |

  **Representative CNAPP platforms:**
  - **Wiz:** Agentless cloud scanning via read-only API access. Builds a security graph connecting cloud resources, identities, misconfigs, vulnerabilities, and network exposure. Attack path analysis shows: "this S3 bucket is publicly accessible AND contains credentials that grant admin access to RDS" — a compound finding no standalone tool sees.
  - **Lacework:** Behaviour-based anomaly detection + CSPM. Strong on runtime anomaly detection using ML baseline of normal API call patterns.
  - **Orca Security:** Agentless, reads cloud storage snapshots to scan workloads without deploying agents. Side-scanning avoids agent coverage gaps.

  - [ ] **Architect's perspective:** Understand CNAPP as the cloud security data platform — it provides the unified visibility layer that SOC, DevSecOps, and cloud teams query. Know: what data each component contributes, how attack path analysis works, and what it cannot see (agentless tools miss in-memory threats; CWPP agents fill that gap).

  - [ ] **Pentester's perspective:** CNAPP creates a centralised alert correlation target. Offensive actions that individually look benign (enumerate S3, assume role, access parameter store) may be stitched together by Wiz/Lacework into a high-confidence attack path alert. Understand CNAPP detection logic when planning cloud red team operations.

<a id="stage-4-data-security-architecture"></a>
### **Stage 4: Data Security Architecture** — `🧠 Conceptual`

- [ ] **Data Classification:** Implement **classification schemes** (Public, Internal, Confidential, Restricted) with **automated labeling** and **DLP policy enforcement**.

- [ ] **Encryption Architecture:** Design **encryption at rest (disk, database, file), in transit (TLS, IPSec), and in use (secure enclaves, confidential computing)**.

- [ ] **Key Management:** Design **KMS architecture** with **key rotation, separation of duties, HSM backing**, and **disaster recovery** for cryptographic keys.

- [ ] **Privacy Engineering:** Implement **data anonymization, pseudonymization, tokenization** for GDPR/DPDP Act compliance. Understand **Privacy by Design** principles.

<a id="stage-5-disaster-recovery-business-continuity"></a>
### **Stage 5: Disaster Recovery & Business Continuity** — `🧠 Conceptual`

- [ ] **DR/BCP Fundamentals:** Understand **RPO (Recovery Point Objective)** and **RTO (Recovery Time Objective)** and how they drive architecture decisions.

- [ ] **Backup Strategies:** Design **3-2-1 backup strategies** (3 copies, 2 media types, 1 offsite). Understand **immutable backups** for ransomware resilience.

- [ ] **Failover Architecture:** Design **active-passive, active-active, and pilot light** DR architectures. Understand **cold, warm, hot** site classifications.

- [ ] **DR Testing:** Plan and execute **tabletop exercises, simulation tests, and full failover tests** on a regular schedule.

<a id="lab-progression-part-43-security-architecture-engineering"></a>
### **Lab Progression (Part 43: Security Architecture & Engineering)**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Design a network architecture for a 3-tier web application | Architecture diagram with security controls |
| 2 | Create a Zero Trust access policy for a hybrid workforce | Policy document with NIST 800-207 mapping |
| 3 | Design a cloud security architecture (VPC, security groups, WAF) | Cloud architecture diagram |
| 4 | Develop a DR/BCP plan for a hypothetical organization | DR plan with RPO/RTO targets |
| 5 | Conduct a security architecture review of an existing design | Review findings report with recommendations |
| 6 | Design and deploy a complete monitoring stack (SIEM + EDR + NDR + SOAR + log pipeline) in a lab | End-to-end detection architecture document with data flow diagram |

> [!IMPORTANT]
> **Move-On Gate:** You can design a secure network architecture from scratch, apply Zero Trust principles, create data classification and encryption strategies, and develop DR/BCP plans with realistic RPO/RTO targets.

---

### 🏆 Phase 8 Capstone Project

**Design a Zero Trust Architecture and Create a Compliance Mapping**

- [ ] **Design a Zero Trust architecture** for a fictional mid-size enterprise (500 employees, hybrid cloud, remote workforce)
- [ ] **Create a NIST CSF compliance matrix** mapping controls to the architecture
- [ ] **Design the detection stack** — SIEM + EDR + NDR + SOAR integration with data flow diagram
- [ ] **Write a DR/BCP plan** covering critical system recovery

**Deliverables:**
- [ ] Zero Trust architecture document with network diagrams and data flow diagrams
- [ ] NIST CSF compliance matrix (spreadsheet or markdown table)
- [ ] Detection stack architecture document showing tool integration
- [ ] DR/BCP plan with RTOs and RPOs
- [ ] All documentation committed to your Git repository

> [!IMPORTANT]
> **Capstone Gate:** Your architecture must be defensible in a design review. Each decision must have a documented rationale.

---

### 🧭 Phase 8 Reflection & Competency Check

- [ ] **Reflection:** Which design decision involved the hardest tradeoff between security, usability, cost, and operations?
- [ ] **Reflection:** Which compliance requirement changed the technical architecture most?
- [ ] **Competency:** Can you defend your architecture using threats, controls, and business constraints?
- [ ] **Competency:** Can you map controls to a framework without turning the exercise into checkbox compliance?
- [ ] **Competency:** Can you explain CI/CD, supply chain, monitoring, and recovery controls as one coherent system?

> [!IMPORTANT]
> **Phase Completion Gate:** Move on only when your architecture decisions are documented, reviewable, mapped to risk, and practical to operate.

---

<a id="toc-part-38-ai--llm-red-teaming"></a>

---

<a id="shelf-16-security-operations-expansion"></a>
<a id="part-13b"></a>

## Shelf 16: Security Operations Expansion


_Continuation of Part 13A. These stages cover operational security tools and programs that build on the detection engineering foundation. Complete Part 13A before starting this section._

<a id="stage-11-security-orchestration-automation-response-soar"></a>
### **Stage 11: Security Orchestration, Automation & Response (SOAR)** — `🔬 Practical`

> [!TIP]
> **Goal:** Automate SOC workflows and incident response actions.

- [ ] **SOAR Architecture:** Understand how **SOAR platforms (Splunk SOAR, Cortex XSOAR, Tines, Shuffle)** integrate with **SIEM, EDR, ticketing, email, firewall APIs** to automate response.

- [ ] **Playbook Design:** Build automated **runbooks** for common scenarios: **phishing triage (extract IOCs → check reputation → quarantine email → block sender → create ticket)**, **malware alert enrichment**, **user account lockout on failed logins**.

- [ ] **API Integration:** Use **REST APIs** to connect SOAR to **VirusTotal, AbuseIPDB, Shodan, Active Directory, Slack/Teams** for automated enrichment and notification.

- [ ] **Case Management:** Understand **incident case lifecycle** within SOAR: **alert → triage → investigation → containment → remediation → closure** with evidence tracking.

- [ ] **Metrics & ROI:** Measure **automation coverage, MTTR reduction, analyst time saved** to demonstrate SOAR value.

---

<a id="stage-12-data-loss-prevention-dlp-fundamentals"></a>
### **Stage 12: Data Loss Prevention (DLP) Fundamentals** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Understand DLP as a defensive control, not just something to bypass.

- [ ] **DLP Architecture:** Understand **endpoint DLP** (agent-based monitoring of file operations, clipboard, USB), **network DLP** (inline/tap inspection of traffic), and **cloud DLP** (CASB integration, SaaS monitoring).

- [ ] **Policy Design:** Create DLP policies for **PII detection (SSN, credit cards, IBAN), source code exfiltration prevention, intellectual property protection** using **regex, keywords, fingerprinting, exact data matching**.

- [ ] **Response Actions:** Configure **alert, block, quarantine, encrypt, notify manager** responses based on **policy severity and data classification level**.

- [ ] **CASB Integration:** Understand how **Cloud Access Security Brokers (Netskope, Zscaler, Microsoft Defender for Cloud Apps)** extend DLP to **SaaS platforms (Office 365, Google Workspace, Salesforce)**.

- [ ] **DLP Evasion Awareness:** Know that attackers bypass DLP via **steganography, encryption, encoding, protocol tunneling, and out-of-band channels** — use this knowledge to improve detection, not to circumvent it.

---

<a id="stage-13-vulnerability-management-program"></a>
### **Stage 13: Vulnerability Management Program** — `🔬 Practical`

> [!TIP]
> **Goal:** Understand the full lifecycle of finding, prioritizing, and remediating vulnerabilities at scale.

- [ ] **Scanner Deployment:** Deploy and configure **Nessus, Qualys, Rapid7 InsightVM, or OpenVAS** for authenticated and unauthenticated scanning across infrastructure.

- [ ] **Scan Scheduling:** Design scan schedules that balance **coverage (weekly/monthly), performance impact (off-peak), and compliance requirements (PCI quarterly ASV scans)**.

- [ ] **Prioritization:** Use **CVSS v4.0, EPSS (Exploit Prediction Scoring System), CISA KEV catalog, asset criticality, and business context** to prioritize remediation over raw severity scores.

- [ ] **Patch Management Lifecycle:** Understand **test → stage → deploy → verify → report** patch workflows, emergency patching for zero-days, and compensating controls when patching is infeasible.

- [ ] **Remediation Tracking:** Use **ticketing systems (Jira, ServiceNow)** to track **remediation SLAs, exception requests, risk acceptance decisions**, and produce **vulnerability trending reports** for leadership.

- [ ] **Continuous Monitoring:** Implement **continuous assessment** via agent-based scanning, cloud posture management (CSPM), and integration with SIEM for vulnerability-correlated alerting.

---

<a id="stage-14-insider-threat-detection"></a>
### **Stage 14: Insider Threat Detection** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Detect and investigate threats originating from within the organization.

- [ ] **Insider Threat Types:** Understand **malicious insiders** (disgruntled employees, espionage), **negligent insiders** (accidental data exposure), and **compromised insiders** (credential theft, social engineering victims).

- [ ] **UEBA (User & Entity Behavior Analytics):** Deploy **behavioral analytics** to baseline normal user behavior (login times, accessed resources, data volumes) and alert on **anomalous patterns** (after-hours access, bulk downloads, unusual destinations).

- [ ] **DLP + SIEM Correlation:** Combine **DLP alerts** (data exfiltration attempts) with **SIEM telemetry** (badge access, VPN connections, email volume) to build **insider risk profiles**.

- [ ] **Insider Threat Program:** Understand program components: **governance (policy, legal, HR), technical controls (monitoring, access reviews), behavioral indicators (resignation, PIP, access hoarding), and investigation workflows**.

- [ ] **Privacy & Legal Constraints:** Balance monitoring with **employee privacy rights, legal requirements (works council, GDPR), union agreements**, and ensure monitoring is **proportionate, documented, and authorized**.

---

<a id="lab-progression-parts-13a-13b-combined"></a>
### **Lab Progression (Parts 13A + 13B Combined)**

> [!TIP]
> **Goal:** Build working detection and security operations capabilities, not just vocabulary.

- [ ] **SIEM Build:** Deploy Wazuh, Security Onion, Splunk Free, or ELK in a lab and ingest Windows Event Logs, Sysmon, Linux auth logs, and firewall/DNS logs.
- [ ] **Query Lab:** Write 10 searches across SPL/KQL/Elastic-style syntax for process creation, suspicious PowerShell, failed logons, DNS anomalies, and lateral movement.
- [ ] **Detection Rule Lab:** Write 5 Sigma/YARA/Suricata/Zeek/osquery rules and test them against lab activity.
- [ ] **Incident Timeline Lab:** Reconstruct 2 incidents from logs and produce analyst notes with evidence and containment actions.
- [ ] **SOAR Playbook Lab:** Build one automated phishing triage playbook (extract IOCs → check reputation → quarantine) using Shuffle, Tines, or n8n.
- [ ] **IR Playbook Execution Lab:** Build and run a complete Incident Response playbook for a **ransomware scenario** in your home lab: (1) detect the ransomware beacon via SIEM alert; (2) isolate the infected VM from the network segment; (3) preserve a forensic memory dump and disk image before remediation; (4) identify the initial access vector from logs; (5) eradicate the payload and restore from a clean snapshot; (6) write a post-incident report with a timeline, root cause, and control improvement recommendations. Use a scenario from **[Blue Team Labs Online](https://blueteamlabs.online)**, **[LetsDefend](https://letsdefend.io)**, or **[CyberDefenders](https://cyberdefenders.org)** as your scenario source if you don't want to stage your own.

**Platform Guide for Phase 3:**

| Platform | Best For | Cost |
|----------|----------|------|
| [Blue Team Labs Online](https://blueteamlabs.online) | DFIR investigations, SOC analyst challenges, log analysis, malware triage | Free + Pro |
| [LetsDefend](https://letsdefend.io) | SOC analyst workflows, alert triage, phishing analysis, incident handling | Free + Pro |
| [CyberDefenders](https://cyberdefenders.org) | Blue team CTF challenges, PCAP analysis, forensics, threat hunting | Free + Pro |
| [Hack The Box Sherlocks](https://hackthebox.com) | DFIR forensics investigations in realistic enterprise scenarios | Free + VIP |
| [Splunk Free / Security Onion / Wazuh](https://wazuh.com) | Self-hosted SIEM/EDR lab environments for detection engineering practice | Free (self-hosted) |



> [!IMPORTANT]
> **Stage Gate — Part 13B Completion (Stages 11–14):** Before proceeding to Part 14 (IDS, Firewalls, Honeypots), you must demonstrate all of:
> - [ ] **SOAR:** Built at least 1 automated playbook in Shuffle, Tines, or n8n that executes a real response action (IP reputation check, email quarantine, or ticket creation) when triggered by a SIEM alert
> - [ ] **DLP:** Created a DLP policy in a lab environment (or documented one for a simulated scenario) with at least 3 detection rules targeting different data types (PII, source code, credentials) with appropriate response actions
> - [ ] **Vulnerability Management:** Run an authenticated Nessus/OpenVAS scan against a lab VM and produced a prioritized remediation report using EPSS or CISA KEV to justify priority order — not just raw CVSS scores
> - [ ] **Insider Threat:** Written a UEBA detection hypothesis for at least 1 insider threat scenario (bulk download before resignation, after-hours access to sensitive files) and named the data sources required to execute it

<a id="toc-part-14-ids-firewalls-and-honeypots"></a>
<a id="part-14-ids-firewalls-and-honeypots"></a>

---

<a id="shelf-17-denial-of-service--availability-resilience"></a>
<a id="part-11"></a>

## Shelf 17: Denial of Service & Availability Resilience


> [!CAUTION]
> **Defensive & Resilience Scope:** DoS/DDoS is studied here strictly for architectural awareness, traffic analysis, and availability engineering. Authorized penetration tests and professional red teaming engagements do not perform destructive denial-of-service attacks on client networks.
>
> **Focus:** Understand how protocol exhaustion and volumetric reflection work at Layers 3/4 and Layer 7, and master the defensive mitigations (Anycast, SYN cookies, rate limiting, edge scrubbing).

<a id="stage-1-objective-strategy-the-planning"></a>

### **Stage 1: Threat Model & Mechanics** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Classify DoS vectors across the OSI stack.

- [ ] **Volumetric Attacks (L3/L4):** Saturate network bandwidth using amplification/reflection (DNS, NTP, SNMP, CLDAP) where small spoofed UDP requests generate massive response traffic directed at victim.

- [ ] **Protocol Exhaustion (L4):** Exploit TCP state machine limitations — **SYN floods** consuming embryonic connection backlogs, TCP reset injection, connection pool starvation.

- [ ] **Application-Layer Disruption (L7):** Target resource-intensive endpoints — **Slowloris** (holding HTTP connections open with slow headers), HTTP/2 Rapid Reset (stream cancellation abuse), expensive database search queries, and unauthenticated regex evaluation (ReDoS).

---

<a id="stage-2-defense-mitigation-the-shield"></a>

### **Stage 2: Defense & Engineering Resilience** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Design resilient architectures that absorb and deflect denial-of-service attempts.

- [ ] **Edge Scrubbing & CDN Protection:** Deploy Cloudflare, AWS Shield, or Akamai to absorb volumetric floods before they reach origin servers; enforce Anycast routing to distribute load globally across points of presence (PoPs).

- [ ] **Kernel & Host Hardening:**
  - Enable **TCP SYN Cookies** (`net.ipv4.tcp_syncookies = 1`) to eliminate SYN backlog exhaustion.
  - Tune `tcp_max_syn_backlog`, `tcp_synack_retries`, and `tcp_fin_timeout` for high-throughput resilience.

- [ ] **Application Rate Limiting & Throttling:** Implement sliding-window rate limiters (token bucket/leaky bucket in Nginx/Envoy), adaptive CAPTCHAs, and circuit breakers for slow upstream dependencies.

- [ ] **Network Upstream Coordination:** Configure **BGP Blackholing / Flowspec** with ISPs to drop malicious traffic at the carrier edge before it hits enterprise transit links.

---

> [!NOTE]
> **Curriculum Alignment Note:** Application-layer Session Hijacking & Token Attacks (cookie security attributes, session fixation, JWT tampering, and CSRF) are taught exclusively in **[Stage 3: Module 15](Stage-3_Web-and-App-Sec.md#module-15-session-hijacking--token-attacks)** alongside Web Application Penetration Testing. Network-level packet sniffing and MITM manipulation are covered in [Part 9: Sniffing & Spoofing](#part-9-sniffing-spoofing).

---

---

### 🏆 Phase 2 Capstone Project

**Complete a Full Penetration Test on a Deliberately Vulnerable Lab**

Select a multi-machine vulnerable environment (HTB Pro Lab, VulnHub chain, or your own Phase 1 lab):

- [ ] **Perform full recon** (passive + active footprinting, scanning, enumeration)
- [ ] **Achieve initial access** on at least 2 machines using different vectors
- [ ] **Escalate privileges** to root/SYSTEM on each machine
- [ ] **Demonstrate lateral movement** between at least 2 systems
- [ ] **Document the full kill chain** from recon to impact

**Deliverables:**

- [ ] Professional penetration test report using PTES template (executive summary, methodology, findings, remediation)
- [ ] Attack chain diagram showing the complete path from initial access to domain compromise
- [ ] All evidence (screenshots, tool output, scripts) organized in your Git repository

> [!IMPORTANT]
> **Capstone Gate:** Your report must be structured professionally enough to present to a client. A reader should understand every step without needing to ask questions.

---

### 🧭 Phase 2 Reflection & Competency Check

- [ ] **Reflection:** Which stage of the attack chain required the most iteration: recon, enumeration, exploitation, privilege escalation, or lateral movement?
- [ ] **Reflection:** What would a defender have seen at each major step?
- [ ] **Competency:** Can you perform recon and enumeration without jumping prematurely to exploitation?
- [ ] **Competency:** Can you prove every finding with evidence and explain business impact without exaggeration?
- [ ] **Competency:** Can you produce a complete attack chain diagram and client-ready report from raw notes?

> [!IMPORTANT]
> **Phase Completion Gate:** Move on only when you can complete an authorized lab penetration test end-to-end, document it professionally, and explain both attacker actions and defender visibility.

---

<a id="toc-part-32-physical-penetration-testing"></a>

---

<a id="phase-2-mini-projects"></a>

## 🛠️ Phase 2 Mini Projects

> [!TIP]
> **Why these projects are here:** Phase 2 covers the full offensive lifecycle — recon, scanning, enumeration, and exploitation. These 4 projects map directly to Parts 4, 5, 6, and the vulnerability assessment stage. Build each one _after_ completing its corresponding Part, not before. They are hands-on reinforcements of what you studied, not shortcuts around it.

> [!NOTE]
> **How to use this section:** Each project below maps to a specific Phase 2 Part. All code must be committed to your Git repository. README must cover: what the tool does, what protocols it uses, ethical usage requirements (authorized targets only), and sample output.

---

### Project 10 — Port Scanner

**Maps to:** Part 5 (Scanning) → Stage 2: Port, Service & Protocol Enumeration

**What it is:** A TCP/UDP port scanner that discovers open ports on a target host, attempts banner grabbing to identify services, supports concurrent scanning (threading or asyncio), and outputs results in a structured format. Should support SYN scan (raw sockets, requires root) and TCP connect scan (no root required).

**What you need before building it:**

- TCP 3-way handshake mechanics: SYN → SYN-ACK → ACK (open), SYN → RST (closed), no response (filtered)
- Raw socket programming in Python (`socket` module)
- Threading or `asyncio` — scanning 65,535 ports sequentially takes minutes; concurrent scanning takes seconds
- Service identification via banner grabbing (send a probe, read the response header)
- Study Nmap source behavior before implementing — understand _why_ a SYN scan is stealthier than a full connect scan

**Why build it:**
Nmap already exists. The reason you build your own is to understand _why_ port scanning works at the socket level — what does a TCP RST response mean vs a timeout vs a ICMP unreachable? What does a firewall returning RST vs dropping silently tell you? Building this makes every Nmap flag you use afterward meaningful rather than cargo-culted. This is the foundational recon tool that every subsequent project in this phase depends on.

**Deliverable:** Python CLI — `scan <target> --ports <range> --mode <connect|syn> --threads <n>`. Output: table of open ports with service guesses. README must document the ethical usage requirements and explain the SYN vs connect scan distinction.

---

### Project 11 — Network Packet Sniffer

**Maps to:** Part 9 (Sniffing & Spoofing) → Stage 2: Sniffing & Passive Reconnaissance

**What it is:** A packet capture and analysis tool that captures live network traffic, parses packet headers (Ethernet, IP, TCP, UDP), extracts application-layer data for unencrypted protocols (HTTP, DNS), and displays a real-time stream of summarized traffic. Must run on a designated lab interface only.

**What you need before building it:**

- OSI model internals: know what each layer encapsulates
- Ethernet frame structure, IP header fields (TTL, flags, fragmentation), TCP header (sequence numbers, flags, window size)
- `scapy` (Python) — the standard library for packet crafting and capture
- Requires root/administrator privileges — document this clearly
- DNS query/response format (question section, answer section, record types)
- HTTP request structure (method, path, headers, body)

**Why build it:**
Every network security tool — from Wireshark to IDS/IPS systems — is built on the same packet capture foundation. Understanding how to capture and parse raw packets is essential for network forensics, building detection rules, and understanding what protocol-level data an attacker can see on an unencrypted network. This project also makes TLS's value immediately tangible: after parsing HTTP in plaintext, you understand exactly what TLS hides.

**Deliverable:** Python tool using `scapy` that captures on a specified interface (`--iface eth0`), filters by protocol (`--filter tcp/udp/dns/http`), and displays structured output. README must include sample output and note that this must only run in your own lab environment.

---

### Project 13 — Subdomain Scanner

**Maps to:** Part 4 (Footprinting & Reconnaissance) → Stage 2: Semi-Passive Infrastructure Mapping + Stage 3: Active Footprinting

**What it is:** A subdomain enumeration tool that combines: wordlist-based DNS brute-forcing (active), Certificate Transparency log querying via the crt.sh API (passive — no direct target traffic), and DNS record analysis (A, CNAME, MX). Must implement concurrent DNS resolution and rate limiting.

**What you need before building it:**

- DNS resolution mechanics: how a resolver walks the hierarchy (root → TLD → authoritative)
- DNS record types: A (IPv4), AAAA (IPv6), CNAME (alias), MX (mail), TXT (verification/SPF)
- Certificate Transparency: every TLS certificate issued is logged publicly — `crt.sh` exposes this via API, enabling passive subdomain discovery without touching the target
- `dnspython` or `aiodns` for async DNS resolution
- SecLists subdomain wordlists (the `Discovery/DNS/` directory)

**Why build it:**
The most critical vulnerabilities in a real engagement are often not found on `www.target.com` but on `dev.target.com`, `staging.target.com`, `admin-legacy.target.com`, or `vpn.target.com` — subdomains that exist because developers need them and forget to secure them. Subdomain scanning teaches you to think about the _entire attack surface_ of an organization rather than just its primary domain. The crt.sh passive technique is particularly valuable: it finds subdomains without generating a single packet to the target.

**Deliverable:** Python CLI — `scan <domain> --wordlist <path> --passive --threads <n>`. Output: list of discovered subdomains with resolved IPs. README must distinguish passive vs active discovery and explain Certificate Transparency.

---

### Project 14 — Vulnerability Scanner

**Maps to:** Part 5 (Scanning) → Stage 4: Vulnerability Association & Attack Mapping + Part 6 (Enumeration) → Stage 1: Service Enumeration & Banner Grabbing

**What it is:** A network vulnerability scanner that: uses port scanning (Project 10) as its discovery layer, performs service version fingerprinting via banner grabbing, queries the NIST NVD API to find CVEs associated with identified service versions, scores each finding using CVSS, and generates a structured report. Must only target authorized systems.

**What you need before building it:**

- Project 10 (Port Scanner) completed and working — this scanner uses it as a dependency
- Service version extraction: banner grabbing returns strings like `Apache httpd 2.4.49` — you parse the service name and version
- NIST NVD API: free, no authentication required for basic queries — `https://services.nvd.nist.gov/rest/json/cves/2.0?keywordSearch=<service+version>`
- CVSS scoring: understand what Base Score, Attack Vector, Attack Complexity, and Privileges Required mean
- Report generation: at minimum a structured Markdown or JSON report; optionally HTML

**Why build it:**
This is the Phase 2 capstone project — it combines everything from recon (port scanning) through enumeration (service fingerprinting) into a vulnerability assessment output. It demonstrates you understand the full discovery-to-finding lifecycle that underpins every professional penetration test and vulnerability management program. Tools like Nessus and OpenVAS follow this exact model: discover → fingerprint → correlate CVEs → score → report. Building it yourself means you understand what these tools do under the hood, not just how to click their interfaces.

**Deliverable:** Python CLI — `scan <target> --ports <range>`. Output: structured report listing open ports, identified services, associated CVEs, and CVSS scores. README must explain the CVE/CVSS scoring model and include a sample report.

---

> [!IMPORTANT]
> **Phase 2 Project Completion Gate:** Each of these tools must only ever target systems you own or have explicit written authorization to test. Your README files must include this disclaimer. A tool without an ethics section in its documentation is a tool that cannot be shown to an employer.
