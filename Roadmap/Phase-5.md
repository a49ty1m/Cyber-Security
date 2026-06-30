# Phase 5: Wireless & Mobile

---

### 🧭 Navigation
◀ [Phase 4](Phase-4.md) | 🏠 [Master Roadmap](README.md) | [Phase 6](Phase-6.md) ➔

---

> [!NOTE]
> **Phase Overview**
> - **⏱️ Time Commitment (Full-Time):** 2–3 months
> - **⏱️ Time Commitment (Part-Time):** 3–5 months
> - **🎯 Primary Focus:** WiFi pentesting (WPA3, evil twin, PMKID), Bluetooth/BLE/Zigbee/NFC/RFID/GPS attacks, SDR spectrum analysis, and Android/iOS dynamic+static analysis.

---

> [!NOTE]
> ### 📝 Phase 5 Documentation Requirements
> Every wireless and mobile assessment must produce professional artifacts. Required artifacts:
> - **Wireless capture files** (.cap/.pcapng) with annotated analysis
> - **Mobile assessment screenshots** — MobSF reports, Frida hook outputs, intercepted traffic
> - **Frida/Objection scripts** — custom hooks committed to your Git repository
> - **Assessment reports** — structured wireless audit and mobile app assessment documents
> - **Git commits** — all capture files, scripts, and reports committed
>
> _By the end of Phase 5, you should have wireless and mobile assessment templates ready for professional use._

---

### 🗂️ Table of Contents
- [Part 21: Wireless Pentesting](#part-21-wireless-pentesting)
  - [Stage 1: RF Reconnaissance & Setup](#stage-1-rf-reconnaissance-setup)
  - [Stage 2: Access Point Assault (The Breaching of Keys)](#stage-2-access-point-assault-the-breaching-of-keys)
  - [Stage 3: Enterprise & Client Attacks (The Man-in-the-Middle)](#stage-3-enterprise-client-attacks-the-man-in-the-middle)
  - [Stage 4: Bluetooth & BLE Attacks](#stage-4-bluetooth-ble-attacks)
  - [Stage 5: Zigbee, Z-Wave & IoT Attacks](#stage-5-zigbee-z-wave-iot-attacks)
  - [Stage 6: NFC & RFID Attacks](#stage-6-nfc-rfid-attacks)
  - [Stage 7: GPS & Satellite Spoofing](#stage-7-gps-satellite-spoofing)
  - [Stage 8: SDR & Spectrum Analysis](#stage-8-sdr-spectrum-analysis)
  - [Stage 9: Defense & Hardening (The Shield)](#stage-9-defense-hardening-the-shield)
- [Part 22: Mobile Platform Pentesting](#part-22-mobile-platform-pentesting)
  - [Stage 0: Mobile Architecture Foundations](#stage-0-mobile-architecture-foundations)
  - [Stage 1: Lab Setup & Reconnaissance](#stage-1-lab-setup-reconnaissance)
  - [Stage 2: Static Analysis (Code Review)](#stage-2-static-analysis-code-review)
  - [Stage 3: Dynamic Analysis (Runtime Manipulation)](#stage-3-dynamic-analysis-runtime-manipulation)
  - [Stage 4: Network & API Attacks](#stage-4-network-api-attacks)
  - [Stage 5: Local Data Storage & Defense](#stage-5-local-data-storage-defense)
  - [Stage 6: Defense & Secure Development](#stage-6-defense-secure-development)

---

## Part 21: Wireless Pentesting

> **Safety Gate:** RF testing must stay inside legal spectrum rules and authorized lab targets. Use your own access points, Faraday isolation where appropriate, low power settings, and written permission. GPS jamming/spoofing and unauthorized wireless interference can create real-world safety issues.

### **Stage 1: RF Reconnaissance & Setup**

> [!TIP]
> **Goal:** Map the airspace and identify targets.

- [ ] **Monitor Mode:** Configure hardware to capture raw 802.11 frames.

- [ ] **Protocol Audit:** Identify the target's encryption: **WPA vs WPA2 vs WPA3 vs WEP**. Note that WEP is obsolete but trivial to crack; WPA3 is resistant to dictionary attacks.

- [ ] **WPS Check:** Scan for **WPS** enabled APs. If active, this is the primary high-value target for PIN brute-forcing (Pixie Dust).

---

### **Stage 2: Access Point Assault (The Breaching of Keys)**

> [!TIP]
> **Goal:** Obtain the credentials to join the network.

- [ ] **Handshake Capture:** Execute a **Deauth Attack** against a connected client to force a reconnection and capture the 4-way handshake.

- [ ] **Replay Attacks:** (For legacy/WEP) Use **Replay Attack** techniques to generate traffic and accelerate IV collection for cracking.

- [ ] **Offline Cracking:** Run the captured handshake against wordlists using Hashcat/Aircrack-ng.

---

### **Stage 3: Enterprise & Client Attacks (The Man-in-the-Middle)**

> [!TIP]
> **Goal:** Steal individual user identities or hijack connections.

- [ ] **Evil Twin Deployment:** Launch an **Evil Twin** attack to impersonate the target SSID. Use a captive portal to harvest credentials.

- [ ] **Enterprise Stripping:** Target **EAP vs PEAP** configurations. Downgrade encryption or crack the challenge-response hashes (MSCHAPv2) captured from the Evil Twin.

- [ ] **Rogue AP:** Plant a **Rogue Access Point** physically in the facility to create an unauthorized backdoor into the LAN.

- [ ] **KRACK Attack:** Exploit **Key Reinstallation Attack** against WPA2 to decrypt traffic (requires client participation, patches available).

- [ ] **PMKID Attack:** Extract **PMKID** from unassociated clients for offline cracking (faster than 4-way handshake, works against WPA2/WPA3).

---

### **Stage 4: Bluetooth & BLE Attacks**

> [!TIP]
> **Goal:** Compromise Bluetooth connections and devices.

- [ ] **BLE Fundamentals:** Understand **Bluetooth Low Energy** (BLE) **GATT/GAP, advertising, pairing mechanisms, security modes**.

- [ ] **Bluejacking:** Send **unsolicited messages** to BLE devices (informational, not harmful, for PoC).

- [ ] **Bluesnarfing:** Gain **unauthorized access** to BLE device data (contacts, calendar, files).

- [ ] **KNOB Attack:** Exploit **Key Negotiation of Bluetooth** to negotiate weak encryption keys.

- [ ] **BLE Pairing Bypass:** Exploit **weak pin/oob verification** or perform **man-in-the-middle attacks** on pairing to intercept keys.

- [ ] **Bluetooth Eavesdropping:** Use tools like **ubertooth, Proxmark** to capture Bluetooth packets and attempt decryption.

---

### **Stage 5: Zigbee, Z-Wave & IoT Attacks**

> [!TIP]
> **Goal:** Compromise smart home and industrial IoT networks.

- [ ] **Zigbee Basics:** Understand **Zigbee mesh networking, 802.15.4 radio, AES-128 encryption, default keys**.

- [ ] **Zigbee Sniffing:** Use **USRP, cc2531 dongles** to capture **Zigbee traffic** and extract **network keys** from initial joins.

- [ ] **Zigbee Replay:** Capture and replay **legitimate frames** to trigger device actions (turn lights on/off, unlock).

- [ ] **Z-Wave Attacks:** Exploit **Z-Wave security flaws** (obsolete S0, weak S2 implementations) to hijack devices.

- [ ] **Default Credentials:** Test **Zigbee/Z-Wave hubs** for **default passwords, backdoor accounts**.

- [ ] **Firmware Extraction:** Dump **device firmware** via **UART, JTAG** to find **hardcoded keys or vulnerabilities**.

---

### **Stage 6: NFC & RFID Attacks**

> [!TIP]
> **Goal:** Compromise Near-Field Communication and passive identification systems.

- [ ] **NFC Basics:** Understand **ISO14443-A/B, Mifare protocols, Type 1-4 tags, Android NFC API**.

- [ ] **NFC Cloning:** Extract **NFC card data** using **Proxmark, ACR122U** and write to **blank cards/tags**.

- [ ] **NFC Relay Attack:** Set up **two NFC readers** at distance to **relay communication** between reader and card (e.g., contactless payment fraud).

- [ ] **RFID Spoofing:** Craft **malicious RFID tags** to bypass access control readers (badges, building entry).

- [ ] **RFID Skimming:** Read **unencrypted RFID tags** from distance using **passive readers** (passport, credit card cloning).

- [ ] **ISO7816 Smartcard Attacks:** Understand **smartcard protocols** and exploit **weak implementations, timing attacks, power analysis**.

---

### **Stage 7: GPS & Satellite Spoofing**

> [!TIP]
> **Goal:** Manipulate location services and navigation.

- [ ] **GPS Basics:** Understand **GPS signal structure, GNSS systems (GPS/GLONASS/Galileo), pseudoranges, civilian vs military**.

- [ ] **GPS Spoofing:** Use **USRP or GPS simulators** to transmit **fake GPS signals** and cause devices to report false locations.

- [ ] **GPS Jamming:** Transmit **noise** on **L1 frequency (1575.42 MHz)** to deny GPS service (illegal but demonstrable in lab).

- [ ] **Satellite Communication Hacking:** Understand **Inmarsat, Iridium, Globalstar satellites**; identify **ground stations** for signal theft.

- [ ] **Drone GPS Hijacking:** Spoof **drone GPS** to cause drift, return-to-home corruption, or loss of control.

---

### **Stage 8: SDR & Spectrum Analysis**

> [!TIP]
> **Goal:** Understand software-defined radio and RF reconnaissance.

- [ ] **SDR Fundamentals:** Know tools like **USRP, HackRF, BladeRF** and frameworks like **GNU Radio, CubicSDR**.

- [ ] **Spectrum Scanning:** Use **spectrum analyzers** to identify **active RF signals, frequency bands, modulation types**.

- [ ] **Signal Demodulation:** Demodulate **AM, FM, FSK, PSK, QPSK** signals and extract **data streams**.

- [ ] **Cellular Eavesdropping:** Understand **2G/3G/4G/5G protocols** and attempt to capture **downlink signals** (law enforcement only in licensed contexts).

- [ ] **Protocol Fuzzing:** Use **GrFuzz, AFLplusplus** to fuzz **RF protocols** and find **unexpected states or crashes**.

---

### **Stage 9: Defense & Hardening (The Shield)**

> [!TIP]
> **Goal:** Secure the airwaves.

- [ ] **Protocol Hardening:** Migrate all APs to **WPA3 (SAE)** to mitigate handshake cracking; disable **WPS** immediately.

- [ ] **Certificate Enforcement:** For **EAP/PEAP** networks, enforce **server certificate validation** on all client devices to neutralize **Evil Twin** attacks.

- [ ] **Wireless IPS:** Deploy **WIDS/WIPS** sensors to detect **deauth attacks, rogue APs, evil twins, unusual RF patterns**.

- [ ] **Network Segmentation:** Isolate wireless networks via **VLANs, guest networks**; implement **802.1X authentication** for enterprise.

- [ ] **Physical Security:** Secure AP placement to prevent **physical tampering, rogue AP installation**; use **tamper-evident seals**.

<a id="toc-part-22-mobile-platform-pentesting"></a>
## Part 22: Mobile Platform Pentesting

### **Stage 0: Mobile Architecture Foundations**

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

### **Stage 1: Lab Setup & Reconnaissance**

> [!TIP]
> **Goal:** Prepare the environment and understand the target.

- [ ] **Environment Prep:** Configure a Rooted (Android) or Jailbroken (iOS) device to bypass **Operating System Hardening**.

- [ ] **Binary Acquisition:** Extract the APK or IPA and perform **Basics of Reverse Engineering** using tools like `jadx` or `Ghidra`.

- [ ] **Reconnaissance:** Map the app's attack surface (activities, services, URL schemes) and identify backend endpoints.

---

### **Stage 2: Static Analysis (Code Review)**

> [!TIP]
> **Goal:** Find hardcoded secrets and configuration flaws.

- [ ] **Manifest/Plist Audit:** Check for exported components or insecure permissions that violate **Zero Trust** principles.

- [ ] **Secret Hunting:** Search decompiled code for **Key Exchange** material, API tokens, or hardcoded credentials.

- [ ] **Crypto Audit:** Verify if the app uses weak **Hashing** or **Salting** algorithms for local storage.

---

### **Stage 3: Dynamic Analysis (Runtime Manipulation)**

> [!TIP]
> **Goal:** Bypass client-side controls.

- [ ] **Security Control Bypass:** Use Frida to bypass Root Detection and SSL Pinning (breaking the **SSL vs TLS** trust chain).

- [ ] **Logic Manipulation:** Hook functions to bypass **Authentication vs Authorization** checks (e.g., bypassing a PIN screen).

- [ ] **Memory Dumping:** Analyze device memory for sensitive data that should have been cleared (violating **Confidentiality** in the **CIA Triad**).

---

### **Stage 4: Network & API Attacks**

> [!TIP]
> **Goal:** Compromise the backend server.

- [ ] **Traffic Interception:** Proxy traffic to analyze **Secure vs Unsecure Protocols** and payload structures.

- [ ] **API Vulnerability Testing:** Test backend endpoints for **OWASP10** vulnerabilities like **SQL Injection**, **IDOR**, and **Broken Access Control**.

- [ ] **Session Management:** Test for weak **Session ID** generation or lack of **MFA & 2FA** on the mobile endpoints.

---

### **Stage 5: Local Data Storage & Defense**

> [!TIP]
> **Goal:** Assess data at rest security.

- [ ] **Insecure Storage Check:** Inspect local files (**SQLite, SharedPreferences, Plist, Keychain**) for unencrypted **PII, credentials, API keys**.

- [ ] **Log Analysis:** Check system **logs (Logcat/Syslog)** for sensitive data leakage during app usage.

- [ ] **Backup Analysis:** Extract and analyze **iOS/Android backups** for sensitive data exposure.

---

### **Stage 6: Defense & Secure Development**

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
| 2 | Execute an evil twin attack with Bettercap/hostapd-mana and capture credentials in your lab | MITM attack walkthrough with evidence screenshots |
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
