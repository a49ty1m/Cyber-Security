# 🛠️ AI Study Assistant — Roadmap Topic Expansion Prompt

> **How to use:** Fill in the two placeholders below, then copy everything from the `## Prompt` line downward into your AI assistant.

- `[TOPIC]` → exact checklist item or skill name from the roadmap
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
- **Documentation rule:** Every session produces a structured MD note suitable for Obsidian-style tools

---

### Role

Act as my cybersecurity mentor and technical note writer. Create a practical Markdown learning note for the given roadmap topic. The goal is to teach the topic deeply enough to understand and perform it — without padding, repetition, or filler.

---

### Required structure

Use EXACTLY these 8 sections. Do not add extra top-level sections, appendices, or conclusions.

```
# [Topic Name]
**Roadmap:** [Phase] → [Part] → [Stage]

# Section 1 — What it is and where it sits
# Section 2 — How attackers actually use this
# Section 3 — Core concepts and terminology
# Section 4 — Tools and commands
# Section 5 — Defender detection
# Section 6 — Lab task
# Section 7 — Common mistakes
# Section 8 — Move-on gate
```

The note must start with `# [Topic Name]` as the document title, followed immediately by a `**Roadmap:**` breadcrumb line showing the full path.

---

### Section rules

**Section 1**

- 1–2 paragraphs: plain definition, what it produces, where it fits in the attack chain
- Show placement using a simple diagram or tree (`Recon → Passive → This topic → Active → ...`)
- What breaks if you skip or underestimate this skill?
- One sentence connecting it to what came before and what comes next in the roadmap

**Section 2**
_This is the most important section. Be explicit and concrete. "Attackers gather information" is not acceptable._

- Use numbered subsections (`## 2.1`, `## 2.2`, `## 2.3`, etc.)
- What exactly are they looking for? Name it specifically
- Walk through a realistic attacker workflow step-by-step — show what actions are taken and what the results reveal (exact commands live in Section 4)
- Show one **dead-end finding** vs one **high-value finding** and explain concretely why one matters
- Show where results feed next — what does this unlock in the next phase?
- Pivots belong inside Section 2, not as a separate orphan section
- **Keep this section conceptual. Do not put detailed tool commands here.**

**Section 3**

- Define every technical term that appears in the topic — one line each, in plain language
- If there are subtypes or variants, map them in a compact table
- Explain underlying mechanisms only if needed to perform the technique — skip general education

**Section 4**

- This is the primary location for tools and commands — do not scatter commands across other sections
- Table format: `| Tool | Command | What it finds/shows | When to use it |`
- Kali-first, real syntax not pseudocode
- After the table: for **every tool listed**, add a brief example showing what the output looks like and how to interpret it (2–4 lines is enough for well-known tools; more for complex ones)
- Do not put general methodology, warnings, or unrelated notes here

**Section 5**

- What log source or sensor catches this?
- What event ID, signature, or behavioral rule triggers?
- What do defenders commonly miss?
- How do skilled operators reduce their footprint for this specific technique?
- If the topic is genuinely passive (no server-side events), say so in one sentence and skip the rest
- Keep tight — 5–8 bullets maximum

**Section 6**

- One specific, completable task you can do today
- **Platform:** Use a specific TryHackMe room or HTB machine if one directly covers this topic. If no dedicated room exists, use a local Kali lab setup — describe the environment clearly (e.g. "Kali VM targeting a local test domain")
- **Objective:** one sentence — what am I proving I can do?
- **Steps:** numbered, 6–10 steps total, concrete — not generic "try the tool"
- **Expected output:** what does success look like? What should you see?
- **Git artifact:** exactly what folder structure and files to commit, with a realistic `git commit -m "..."` message
- Do not create multiple labs or a giant tutorial

**Section 7**

- 5–7 most important mistakes learners make for this specific topic
- For each: what the mistake is → why it matters → what to do instead

**Section 8**

- Exactly 3 performance tests
- Each must be an action you perform, not a concept you know or describe
- ❌ "Understand how X works"
- ✅ "Run X against [target] and correctly interpret [specific output] without looking at notes"

---

### Output rules

**Style:**

- Explain concretely, with real examples and command output — not abstract definitions
- Use code blocks for workflows, terminal output, and attack chains
- Use tables for tools, operators, and comparisons
- Short paragraphs or bullets — no academic prose walls
- Each concept explained **once**, in its best form — do not repeat the same idea across sections
- Skip a section entirely if it genuinely doesn't apply to this topic

**Tone:** Write like a senior red teamer teaching a capable technical learner. Be explicit, use real examples, and go as deep as the topic requires.

**Length:** Target **600–1200 lines** for the entire note. 600 is the minimum — if the note is under that, it lacks the depth and examples required. Do not exceed 1200 words with padding or repetition; if a section genuinely has nothing to add, skip it.

**Priority order:** offensive perspective first → concrete examples second → defender awareness third → lab fourth

**No:** disclaimers, scope notes, introductions, conclusions, meta-commentary, or sections not listed above.

**No citations to external sources.** Do not write sentences like "The Red Team Guide describes...", "The supplied reference covers...", or "According to [document]...". Present knowledge directly as fact. If you were given context documents, do not cite or reference them by name — extract the knowledge and write it into the note without attribution.

**Use standard industry terminology.** For example: Vishing (not Whishing), Spear Phishing (not Speerfishing), etc. If the roadmap uses a non-standard term, use the standard term and note the alias only if genuinely useful.

---

### Self-check before finalizing

Verify silently before returning the note:

- [ ] Note starts with `# [Topic Name]` and a `**Roadmap:**` breadcrumb line
- [ ] Exactly 8 sections, in order
- [ ] Section 2 uses `## 2.1` / `## 2.2` / `## 2.3` numbering
- [ ] No orphan headings floating outside sections
- [ ] No duplicated commands or workflows between sections
- [ ] All tool commands are in Section 4 only
- [ ] Section 6 has exactly one lab with 6–10 numbered steps
- [ ] Section 7 has 5–7 mistakes
- [ ] Section 8 has exactly 3 performance tests
- [ ] No citations to "supplied" documents, guides, or references
- [ ] Standard industry terminology used throughout
- [ ] Total note length is between 600 and 1200 lines
