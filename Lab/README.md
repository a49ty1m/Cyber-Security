# 🧪 Cyber Security Labs

> **Purpose:** Hands-on lab practice environments. Labs reinforce the theory from the [Master Roadmap](../Roadmap/README.md). Every lab session should produce a writeup committed to Git.

---

## 📑 Table of Contents

| Lab | Target Skills | Roadmap Alignment | Entry |
|-----|---------------|-------------------|-------|
| 🐧 [Metasploitable 2](Metasploitable_2/TASK_LIST.md) | Network exploitation, service attacks, post-exploitation | Stage 2: Offense I — Modules 08–13 | [Task List](Metasploitable_2/TASK_LIST.md) |
| 🌐 [OWASP Broken WebApps](OWASP_Broken_WebApps/TASK_LIST.md) | OWASP Top 10, web app security, Burp Suite methodology | Stage 3: Web & App Sec — Modules 14–18 | [Task List](OWASP_Broken_WebApps/TASK_LIST.md) |
| 🏰 [OverTheWire Bandit](OverTheWire/Bandit/README.md) | Linux CLI, SSH, file permissions, scripting | Stage 1: Foundation — Module 02 (Linux Admin) | [Levels 0–33](OverTheWire/Bandit/README.md) |

---

## 🗂️ Directory Structure

```
Lab/
├── INFO.md                          # Lab environment setup notes
├── LAB_GUIDE.md                     # Lab methodology guide
├── Metasploitable_2/
│   └── TASK_LIST.md                 # 53 structured tasks + 3 bonus
├── OWASP_Broken_WebApps/
│   └── TASK_LIST.md                 # Web security curriculum
├── OverTheWire/
│   ├── README.md                    # OverTheWire index
│   └── Bandit/
│       ├── README.md                # Level index + progress tracker
│       └── bandit-level-00.md ...   # Individual level writeups (0–33)
└── THM/
    └── WINDOWS.md                   # TryHackMe Windows notes
```

---

## 🔀 Recommended Execution Order (Interleaving)

> [!IMPORTANT]
> Don't grind one lab front-to-back. Interleaving between Metasploitable 2 (network exploitation) and OWASP BWA (web exploitation) prevents burnout and reinforces cross-domain skills.

| Step | Lab | What to Complete | Est. Hours |
|:---:|:---:|:---|:---:|
| 1 | 🐧 MS2 | Phase 1: Foundation & Lab Setup (Tasks 0.1–1.4) | ~4h |
| 2 | 🌐 BWA | Phase 1: Foundation & HTTP Mechanics (Tasks 0.1–2.4) | ~10h |
| 3 | 🐧 MS2 | Phase 2: Deep Enumeration (Tasks 2.1–2.10) | ~8h |
| 4 | 🌐 BWA | Phase 2: Authentication & Input Attacks (Tasks 3.1–5.3) | ~18h |
| 5 | 🐧 MS2 | Phase 3: Exploitation Core (Tasks 3.1–3.12) | ~20h |
| 6 | 🌐 BWA | Phase 3: Injection & File Attacks (Tasks 6.1–8.2) | ~20h |
| 7 | 🐧 MS2 | Phase 4: Post-Exploitation & PrivEsc (Tasks 4.1–4.7) | ~9h |
| 8 | 🌐 BWA | Phase 4: Access Control & Trust Abuse (Tasks 9.1–10.4) | ~10h |
| 9 | 🐧 MS2 | Phase 5: Defense, Reporting & Mastery (Tasks 5.1–5.7) | ~19h |
| 10 | 🌐 BWA | Phase 5: Chaining, Defense & Mastery (Tasks 11.1–13.4) | ~20h |
| 11 | ✍️ Both | **Combined Pentest Report** (MS2 Task 5.7 / BWA Task 13.4) | ~4h |

**Total: ~142h** across both labs (~53 MS2 core tasks + ~50 BWA core tasks + 5 bonus tasks)

1. **Always produce a writeup.** No writeup = the learning didn't happen.
2. **Follow the roadmap sequence.** Do the lab that aligns with my current roadmap Stage/Module.
3. **Commit after every session.** Use descriptive Git messages: `stage2/module09: nmap SYN scan on Metasploitable`
4. **Document failures too.** What didn't work and why is often more valuable than what did.

---

## 🔗 Writeup Format

Every lab writeup should contain:

```
# Lab: [Target] — [Technique]

## Objective
## Environment Setup
## Methodology
## Commands Used
## Findings / Output
## Key Learnings
## What Failed & Why
```
