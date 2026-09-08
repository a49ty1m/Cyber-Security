# 🗂️ Tool Creation Plan — Missing Tier 1 Tools

> **Purpose:** 28 Tier 1 tool `.md` files are referenced in the Phase-1 through Phase-10 mandatory tool stack callouts but do not exist in the Tools folder. This document tracks what needs to be created, in what order, and the completion status.

> **Format Standard:** Every file follows the existing format used in `Netcat.md`, `Volatility.md`, `BloodHound.md`, etc.:
> 1. Title header with emoji + "Complete Mastery Checklist"
> 2. Blockquote intro box: What it is / Why it exists / When to use it / When to avoid it / What mastering it unlocks / Roadmap Phase
> 3. Navigation + cross-links table
> 4. Progress Overview table (phases, tasks, est. time)
> 5. PHASE 1–N sections with practical install snippets, checkbox task items, and operational notes

---

## ✅ Status Legend

- `[ ]` — Not started
- `[/]` — In progress
- `[x]` — Complete

---

## 📦 Files to Create (28 Total)

### Phase 1 — Foundations (1 file)

| # | File | Tool | Roadmap Phase | Status |
|:--|:-----|:-----|:------|:------:|
| 1 | `OpenSSL.md` | OpenSSL & cryptsetup | Phase 1 — Cryptography & TLS | `[ ]` |

---

### Phase 2 — Offensive Fundamentals (1 file)

| # | File | Tool | Roadmap Phase | Status |
|:--|:-----|:-----|:------|:------:|
| 2 | `socat.md` | socat (socket relay — encrypted shells, pivoting) | Phase 2 — Exploitation & Post-Exploitation | `[ ]` |

---

### Phase 3 — Defensive / SOC (6 files)

| # | File | Tool | Roadmap Phase | Status |
|:--|:-----|:-----|:------|:------:|
| 3 | `Splunk.md` | Splunk (Free/Enterprise) | Phase 3 — SIEM & Detection Engineering | `[ ]` |
| 4 | `ELK.md` | Elastic Stack / ELK (Elasticsearch + Logstash + Kibana) | Phase 3 — SIEM & Detection Engineering | `[ ]` |
| 5 | `Wazuh.md` | Wazuh (open-source SIEM/XDR) | Phase 3 — SIEM & Detection Engineering | `[ ]` |
| 6 | `Sysmon.md` | Sysmon (System Monitor) | Phase 3 — Endpoint Telemetry | `[ ]` |
| 7 | `Sigma.md` | Sigma (generic SIEM rule format) | Phase 3 — Detection Rule Writing | `[ ]` |
| 8 | `YARA.md` | YARA (malware pattern matching) | Phase 3 / Phase 7 — Malware Analysis | `[ ]` |

---

### Phase 5 — Wireless & Mobile (4 files)

| # | File | Tool | Roadmap Phase | Status |
|:--|:-----|:-----|:------|:------:|
| 9 | `Frida.md` | Frida dynamic instrumentation framework | Phase 5 — Mobile Pentesting | `[ ]` |
| 10 | `Objection.md` | Objection (Frida-powered runtime explorer) | Phase 5 — Mobile Pentesting | `[ ]` |
| 11 | `jadx.md` | jadx / jadx-gui (Android decompiler) | Phase 5 — Mobile Reverse Engineering | `[ ]` |
| 12 | `APKTool.md` | APKTool (APK disassembler/patcher) | Phase 5 — Mobile Reverse Engineering | `[ ]` |

---

### Phase 6 — Enterprise & Cloud (3 files)

| # | File | Tool | Roadmap Phase | Status |
|:--|:-----|:-----|:------|:------:|
| 13 | `Certipy.md` | Certipy (ADCS exploitation) | Phase 6 — Active Directory / PKI Attacks | `[ ]` |
| 14 | `Prowler.md` | Prowler (AWS/GCP/Azure security scanner) | Phase 6 — Cloud Security Assessment | `[ ]` |
| 15 | `Pacu.md` | Pacu (AWS exploitation framework) | Phase 6 — Cloud Exploitation | `[ ]` |

---

### Phase 7 — Exploit Dev & Reverse Engineering (2 files)

| # | File | Tool | Roadmap Phase | Status |
|:--|:-----|:-----|:------|:------:|
| 16 | `pwntools.md` | pwntools (Python binary exploitation library) | Phase 7 — Binary Exploitation | `[ ]` |
| 17 | `GDB.md` | GDB + pwndbg / GEF (debugger extensions) | Phase 7 — Dynamic Debugging | `[ ]` |

---

### Phase 8 — DevSecOps & Architecture (5 files)

| # | File | Tool | Roadmap Phase | Status |
|:--|:-----|:-----|:------|:------:|
| 18 | `Semgrep.md` | Semgrep (SAST engine) | Phase 8 — Secure SDLC / Code Analysis | `[ ]` |
| 19 | `Gitleaks.md` | Gitleaks (secret scanning) | Phase 8 — CI/CD Security | `[ ]` |
| 20 | `TruffleHog.md` | TruffleHog (secret scanning) | Phase 8 — CI/CD Security | `[ ]` |
| 21 | `Checkov.md` | Checkov (IaC security scanner) | Phase 8 — Infrastructure as Code Security | `[ ]` |
| 22 | `tfsec.md` | tfsec (Terraform-focused IaC security scanner) | Phase 8 — Infrastructure as Code Security | `[ ]` |

---

### Phase 9 — AI & LLM Security (4 files)

| # | File | Tool | Roadmap Phase | Status |
|:--|:-----|:-----|:------|:------:|
| 23 | `Ollama.md` | Ollama (local LLM runner) | Phase 9 — AI Security / LLM Red Teaming | `[ ]` |
| 24 | `Python_AI_SDKs.md` | Python AI SDKs — OpenAI / Anthropic / LangChain (for building & attacking LLM pipelines) | Phase 9 — AI Security / LLM Red Teaming | `[ ]` |
| 25 | `Garak.md` | Garak (LLM vulnerability scanner) | Phase 9 — AI Security / LLM Red Teaming | `[ ]` |
| 26 | `PyRIT.md` | PyRIT — Python Risk Identification Tool (Microsoft) | Phase 9 — AI Red Teaming | `[ ]` |

---

### Phase 10 — Red Team & Capstone (2 files)

| # | File | Tool | Roadmap Phase | Status |
|:--|:-----|:-----|:------|:------:|
| 27 | `Mythic.md` | Mythic C2 framework (collaborative multi-agent C2) | Phase 10 — Red Team Operations & Tradecraft | `[ ]` |
| 28 | `Havoc.md` | Havoc C2 framework (post-exploitation & evasion focused) | Phase 10 — Red Team Operations & Tradecraft | `[ ]` |

---

## 📐 File Structure (Every file follows this skeleton)

```
# <emoji> <ToolName>: Complete Mastery Checklist

> What is it / Why it exists / When to use / When to avoid / What mastering it unlocks / Roadmap Phase

## 🧭 Navigation
## 📊 Progress Overview (phases, tasks, est. time)

# PHASE 1: INSTALLATION & SETUP
# PHASE 2: CORE CONCEPTS & USAGE
# PHASE 3–N: ADVANCED / SPECIALIZED TECHNIQUES
# PHASE N: PRACTICAL LABS

## 📝 Operational Notes
```

---

## 🎯 Execution Order

Files created in **phase order** (Phase 1 → Phase 9):

```
1.  OpenSSL          (P1)
2.  socat            (P2)
3.  Splunk           (P3)
4.  ELK              (P3)  ← was missing
5.  Wazuh            (P3)
6.  Sysmon           (P3)
7.  Sigma            (P3)
8.  YARA             (P3/P7)
9.  Frida            (P5)
10. Objection        (P5)
11. jadx             (P5)
12. APKTool          (P5)
13. Certipy          (P6)
14. Prowler          (P6)
15. Pacu             (P6)
16. pwntools         (P7)
17. GDB              (P7)
18. Semgrep          (P8)
19. Gitleaks         (P8)
20. TruffleHog       (P8)
21. Checkov          (P8)
22. tfsec            (P8)  ← was missing
23. Ollama           (P9)
24. Python_AI_SDKs   (P9)  ← was missing
25. Garak            (P9)
26. PyRIT            (P9)
27. Mythic           (P10) ← was missing
28. Havoc            (P10) ← was missing
```

---

## 🔗 Post-Creation Steps

After all files are created:
1. Update `Tools/README.md` to index all new tools under the correct category.
2. Verify all `file:///` links in Phase-*.md tool stack callouts match exact filenames (case-sensitive).
3. Run `grep -r "file:///.*Tools" Phase-*.md | grep -v "\.md"` to catch any broken refs.
