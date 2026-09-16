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
│   └── TASK_LIST.md                 # 109 structured exploitation tasks
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

## 📋 Lab Rules

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
