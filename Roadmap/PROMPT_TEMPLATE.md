# 🛠️ AI Study Assistant — Roadmap Topic Expansion Prompt

> **How to use:** Fill in the two placeholders, copy everything from the line below into your AI assistant.

- `[TOPIC]` → exact checklist item or skill name
- `[CONTEXT]` → Phase + Part + Stage (e.g. `Phase 2 / Part 4 / Stage 1 — Passive OSINT`)

---

## Prompt (copy from here ↓)

---

**TOPIC:** `[TOPIC]`  
**CONTEXT:** `[CONTEXT]`

---

### My profile

- **Career target:** Penetration Tester → Red Team Operator → Advanced Offensive Security → AI Red Teaming
- **Lab environment:** Kali Linux + home VMs, TryHackMe, HackTheBox, PortSwigger Web Security Academy
- **Documentation rule:** Every session produces a structured MD note sutable for obsidian like tools

---

### Output rules — apply these throughout

**Length:** No arbitrary cap — but every sentence must earn its place. If a section has nothing new to add, skip it.

**Style:**

- Explain things concretely, with real examples and command output — not abstract definitions
- Use code blocks to show workflows, terminal output, and attack chains
- Use tables for tools, operators, and comparisons
- Short paragraphs or bullets — no academic prose walls
- Each concept explained **once**, in its best form — do not repeat the same idea across sections
- Skip a section entirely if it genuinely doesn't apply to this topic

**Tone:** Write like a senior red teamer teaching a capable technical learner. Be explicit, use real examples, and go as deep as the topic requires — but never repeat the same point twice across sections.

**Priority order:** offensive perspective first → concrete examples second → defender awareness third → lab fourth

---

### Section 1 — What it is and where it sits

- 1–2 short paragraphs: plain definition, what it produces, and what phase of an attack/engagement it belongs to
- Show where it fits in the attack chain using a simple diagram or tree (like `Recon → Passive → Search Dorking → Active → ...`)
- What breaks if you skip or underestimate this skill?
- One sentence connecting it to what came before and what comes next in the roadmap

---

### Section 2 — How attackers actually use this

_This is the most important section. Be explicit and concrete. Generic "attackers gather information" answers are not acceptable._

- What exactly are they looking for? Name it specifically.
- Walk through a realistic attacker workflow step-by-step with code blocks showing the actual commands and what the output reveals
- Show one example of a **dead-end finding** vs one example of a **high-value finding** — and explain concretely why one is useful and the other isn't
- Show where this feeds next — what does the result unlock in the next phase?

Format the workflow like this:

```
Step 1 — [Action]
→ command: [exact command]
→ output reveals: [what you learn]

Step 2 — [Next action]
→ command: [exact command]
→ output reveals: [what you learn]

→ Pivot to: [what you do next with this]
```

---

### Section 3 — Core concepts and terminology

- Define every technical term that appears in the topic — one line each, in plain language
- If there are subtypes or variants (e.g. scan types, protocol differences, attack variants), map them in a compact table
- Explain underlying mechanisms only if needed to actually perform the technique — skip general education

---

### Section 4 — Tools and commands

Table format:

| Tool | Command (with realistic placeholder) | What it finds / shows | When to use it |
| ---- | ------------------------------------ | --------------------- | -------------- |

- Kali-first
- Real syntax, not pseudocode
- After the table: for any non-obvious tool, add 3–5 lines showing what the output looks like and how to interpret it

---

### Section 5 — Defender detection

Keep this tight — 5–8 bullets maximum.

- What log source or sensor catches this?
- What event ID, signature, or behavioral rule triggers?
- What do defenders commonly miss?
- How do skilled operators reduce their footprint for this specific technique?

If this topic is genuinely passive (no server-side events), say so in one sentence and skip the rest.

---

### Section 6 — Lab task

**One specific, completable task you can do today.**

- **Platform:** [Specific TryHackMe room name / HTB machine / local Kali setup]
- **Objective:** [One sentence — what am I proving I can do?]
- **Steps:** [Numbered, 6–10 steps, concrete — not generic "try the tool"]
- **Expected output:** [What does success look like? What should you see?]
- **Git artifact:** [Exactly what folder structure and files to commit, with a realistic `git commit -m "..."` message]

---

### Section 7 — Common mistakes

5 mistakes max. For each:

- What the mistake is (one sentence)
- Why it matters (one sentence)
- What to do instead (one sentence or command)

---

### Section 8 — Move-on gate

3 performance tests only. Each must be an action you perform, not a concept you know.

❌ "Understand how X works"  
✅ "Run X against [target] and correctly interpret [specific output] without looking at notes"

1. [Performance test]
2. [Performance test]
3. [Performance test]
