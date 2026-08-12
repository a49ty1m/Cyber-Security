# 🛠️ AI Study Assistant — Roadmap Topic Expansion Prompt

> **How to use:** Copy the entire prompt block below, paste into ChatGPT, Claude, or Gemini.
> Fill in only the two placeholders at the top. Everything else stays as-is.

---

## Quick Start

1. Identify the topic you want to expand from any phase file
2. Replace `[TOPIC]` and `[ROADMAP CONTEXT]` at the top of the prompt
3. Paste the full prompt — including all instructions below — into an AI assistant
4. Use the output as your structured study session for that topic

---

## Prompt (copy everything below this line)

---

**TOPIC:** `[Paste the exact checklist item or topic name here]`

**ROADMAP CONTEXT:** `[Paste the Phase + Part + Stage, e.g. "Phase 2 / Part 4 / Reconnaissance → Organizational Intelligence Gathering"]`

---

### My Profile — read this before answering anything

I am a cybersecurity student and engineer working through a structured 10-phase roadmap toward the following career:

**Career target:** Penetration Tester → Red Team Operator → Advanced Offensive Security → AI Red Teaming

**Current position:** Phase 2A — actively studying Footprinting, Reconnaissance, Scanning, and Enumeration.

**Completed foundations:**
- Linux CLI and system administration
- Windows administration, PowerShell basics
- TCP/IP, OSI model, DNS, HTTP/HTTPS at a practical level
- Networking fundamentals and basic traffic analysis
- Cryptography fundamentals, TLS basics
- HTTP, cookies, SOP, REST APIs, authentication patterns (JWT, OAuth 2.0, OIDC)
- Basic Python scripting, Bash, PowerShell cmdlets

**Known skill gaps** (patch as needed):
- Deep Wireshark / packet dissection — not fully practiced yet
- TLS internals — high level only
- Linux service administration — still building
- Active Directory and Kerberos — foundational only

**Lab environment:** Kali Linux + home lab with VMs. Access to TryHackMe, HackTheBox, OverTheWire, PortSwigger Web Security Academy.

**Learning behavior I am actively correcting:**
- I have a tendency to jump topics — keep answers linear and stage-based
- I prefer knowing what to do *first*, not a wall of theory
- I learn best when theory is paired immediately with a specific command, tool output, or lab step

**Documentation rule:** Everything I learn must produce a Git-committed artifact. Keep this in mind when defining lab outputs.

---

### What I need from you

Expand the topic above into a complete, structured learning module. Follow this exact structure:

---

## Section 1 — What This Is and Why It Matters

- One-paragraph plain-English definition, written for a technical learner — not a beginner, not an expert
- Which phase of a penetration test or red team operation this belongs to
- What goes wrong if you skip or underestimate this skill
- How this connects to what I studied before and what I will study next on my roadmap

---

## Section 2 — How Attackers Actually Use This

_This is the most important section. Be specific. Generic "attackers gather information" answers are useless._

- What exactly do attackers look for?
- How do they find it? (specific methods, not generic categories)
- What does a high-value finding look like vs. a dead-end?
- What is the realistic attacker workflow for this topic, step by step?
- Where does this feed into the next phase of the attack (initial access, privilege escalation, lateral movement, etc.)?

---

## Section 3 — What Defenders Do About It

_Explain this from an attacker's perspective — not as a compliance checklist._

- What detection controls exist for this technique?
- What log sources would expose this activity? (event IDs, SIEM queries, tool names)
- What do defenders commonly miss?
- How do skilled attackers evade the common defensive controls?

_This section is here to make me a better attacker, not to teach me to be a SOC analyst._

---

## Section 4 — Core Concepts and Terminology

- Define every technical term that appears in the topic
- Explain underlying protocols or mechanisms only if needed to perform the technique — not as general education
- If there are multiple variants, subtypes, or sub-techniques, map them clearly (a table is fine)

---

## Section 5 — Tools and Commands

Provide a practical reference. For each tool:

| Tool | What it does for this topic | Key flags / syntax | When to use it |
|------|----------------------------|---------------------|----------------|
| ...  | ...                        | ...                 | ...            |

- Lead with the tools I am most likely to have on Kali Linux
- Show real command examples with realistic targets (use `10.10.x.x`, `example.com`, or `target.htb` as placeholders)
- Explain what the output means — not just how to run the command

---

## Section 6 — Step-by-Step Practical Methodology

_Write this as an operator checklist — what I actually do, in order._

For a realistic engagement scenario (external pentest, internal pentest, or red team — choose the most relevant), walk through:

1. **Start:** what condition triggers this technique / when do I reach for this?
2. **Execute:** specific steps in order, with commands where applicable
3. **Document:** what do I record and how? (tool output, screenshots, findings)
4. **Analyze:** how do I interpret the results?
5. **Pivot:** what does this finding unlock? What do I do next?

---

## Section 7 — Lab Practice

Give me a concrete, completable lab task that I can do today in my environment (Kali + TryHackMe or HackTheBox).

- **Lab objective:** one sentence — what am I proving I can do?
- **Setup / target:** which platform, room, or machine (suggest a specific TryHackMe room, HTB box, or describe a Kali local setup)
- **Task:** numbered steps — what exactly do I do?
- **Expected output:** what does success look like?
- **Documentation artifact:** what do I commit to Git from this session?

---

## Section 8 — Common Mistakes and Failure Modes

- What do beginners get wrong about this topic?
- What assumptions break in real environments vs. CTF environments?
- What gets you caught or causes engagement failure?
- What are the ethical and legal boundaries I must understand?

---

## Section 9 — Move-On Gate

Give me 5 specific things I must be able to do — without looking at notes — before I can consider this topic complete and move on.

Each item should be phrased as a performance test, not a knowledge test:

- ❌ "Understand what Nmap does" (knowledge — too vague)
- ✅ "Run a full Nmap SYN scan with OS detection and version detection against a target and correctly interpret every open port in the output" (performance — specific)

---

## Section 10 — Key Takeaways

Three to five concise statements that capture:
- What professionals actually care about for this topic
- The most important pattern recognition or heuristic to internalize
- The single biggest mistake to never make

---

**Output rules:**
- Be specific and concrete. No vague "you should familiarize yourself with" language.
- Treat me as a technical learner who can handle detail — do not over-explain basic concepts.
- Every code block should be copy-pasteable or clearly explained.
- If a section genuinely does not apply to this topic, say "Not applicable for this topic" and move on — do not pad it.
- Prioritize the offensive perspective throughout. The defensive sections exist to make me harder to detect, not to train me as a defender.
