# Phase 9: AI Security

> [!IMPORTANT]
> **Sequencing Advisory:** This phase (Phase 9) covers AI & LLM Red Teaming — the full offensive and defensive AI security domain. It requires completion of Phases 1–8 (traditional security foundations, offensive core, web security, infrastructure, and advanced specializations) before attempting. Phase 10 (Operations & Career) builds on the portfolio of work produced across all prior phases. Complete Phase 9 before attempting Phase 10.

---

### 🧭 Navigation
◀ [Phase 8](Phase-8.md) | 🏠 [Master Roadmap](README.md) | [Phase 10](Phase-10.md) ➔

---

> [!NOTE]
> **Phase Overview**
> - **⏱️ Time Commitment (Full-Time):** 3–5 months
> - **⏱️ Time Commitment (Part-Time):** 5–8 months
> - **🎯 Primary Focus:** Layer AI system knowledge on top of mastered traditional security skills. Cover transformer architecture, context windows, temperature/sampling, RAG pipelines, OWASP LLM Top 10, prompt injection, RAG poisoning, adversarial ML, model extraction, dataset backdoors, shadow AI prevention, and defensive AI operations. Build and publish AI security tools and research.

---

> [!NOTE]
> ### 📝 Phase 9 Documentation Requirements
> AI security research must be documented with reproducible methodology. Required artifacts:
> - **Prompt injection payload library** — categorized library of tested payloads with success/failure notes
> - **RAG attack documentation** — poisoning methodology, injected documents, impact evidence
> - **AI tool README + architecture diagrams** — for every tool you build
> - **Research writeups** — methodology, findings, and defensive recommendations
> - **Git commits** — all payloads, tools, and research committed
>
> _By the end of Phase 9, your repository should contain an AI security toolkit and published research. This builds on your traditional security portfolio from Phases 1–8 and feeds directly into the Phase 10 career portfolio._

---

### 🗂️ Table of Contents
- [Part 38: AI & LLM Red Teaming](#part-38-ai-llm-red-teaming)

  **Cluster 1: Foundations (Stages 1–3)** — *Complete before Cluster 2*
  - [Stage 1: AI Fundamentals for Security Practitioners](#stage-1-ai-fundamentals-for-security-practitioners)
  - [Stage 2: Attack Surface & Frameworks](#stage-2-attack-surface-frameworks)
  - [Stage 3: Adversarial Techniques (LLM01/LLM06)](#stage-3-adversarial-techniques-llm01llm06)

  **Cluster 2: Advanced LLM Attacks (Stages 4–10)** — *Requires Cluster 1 gate + Python ML prerequisite*
  - [Stage 4: RAG & Data Supply Chain Attacks](#stage-4-rag-data-supply-chain-attacks)
  - [Stage 5: Language Model Specific Attacks](#stage-5-language-model-specific-attacks)
  - [Stage 6: Multi-Model & Agent Attacks](#stage-6-multi-model-agent-attacks)
  - [Stage 7: Adversarial Examples & ML Robustness](#stage-7-adversarial-examples-ml-robustness)
  - [Stage 8: Model Extraction & Inversion](#stage-8-model-extraction-inversion)
  - [Stage 9: Dataset Poisoning & Backdoors](#stage-9-dataset-poisoning-backdoors)
  - [Stage 10: Privacy Attacks & PII Leakage](#stage-10-privacy-attacks-pii-leakage)

  **Cluster 3: Operational & Defensive AI (Stages 11–18)** — *Requires Cluster 2 gate*
  - [Stage 11: AI-Augmented Red Team Workflow](#stage-11-ai-augmented-red-team-workflow)
  - [Stage 12: Agentic AI & Autonomous Attack Infrastructure](#stage-12-agentic-ai-autonomous-attack-infrastructure)
  - [Stage 13: Tooling & Evaluation](#stage-13-tooling-evaluation)
  - [Stage 14: Defense & Responsible AI](#stage-14-defense-responsible-ai)
  - [Stage 15: Shadow AI & Organizational AI Risk](#stage-15-shadow-ai-organizational-ai-risk)
  - [Stage 16: Defensive AI Operations](#stage-16-defensive-ai-operations)
  - [Stage 17: AI Security Projects & Portfolio](#stage-17-ai-security-projects-portfolio)
  - [Stage 18: AI Security Career Targeting](#stage-18-ai-security-career-targeting)

---

<a id="part-38-ai-llm-red-teaming"></a>
## Part 38: AI & LLM Red Teaming

> [!IMPORTANT]
> **⛔ Phase 9 Entry Gate — Verify BOTH prerequisites before Stage 1**
>
> **Prerequisite 1 — Traditional Security (Required):**
> - [ ] Phases 1–8 are complete (foundations, offensive core, web, infrastructure, advanced specializations, GRC, DevSecOps)
> - [ ] You have completed at least one full attack chain in a lab environment (recon → initial access → privilege escalation → lateral movement)
>
> **Prerequisite 2 — Python ML (Required for Stages 7–10):**
> - [ ] You are comfortable with `numpy` array manipulation, `pandas` DataFrames, and `matplotlib` visualization
> - [ ] You understand what a neural network forward pass does (input → weights → activation → output) and what a loss function measures
> - [ ] You can run a pre-trained `scikit-learn` or `PyTorch` model and inspect its predictions
> - [ ] **If you cannot meet the ML prerequisites:** complete fast.ai Part 1 (Practical Deep Learning for Coders) or Andrew Ng's Machine Learning Specialization (Coursera) **before starting Stage 7** — not now, but before you reach it. Flag this gap so it does not surprise you mid-phase.

---

<a id="stage-1-ai-fundamentals-for-security-practitioners"></a>
### **Stage 1: AI Fundamentals for Security Practitioners**

> [!TIP]
> **Goal:** Understand the raw mechanics of AI/ML models to attack and defend them effectively.

- [ ] **Transformer Architecture:** Study the **Transformer model** (attention heads, tokenization, embeddings, positional encoding) — understand how LLMs generate text at a mechanistic level to identify exploitable behavior.

- [ ] **Context Windows & Token Limits:** Understand how **context window size** (4K, 8K, 32K, 128K+ tokens) affects model behavior — know how **context overflow, truncation, and sliding window strategies** create exploitable edge cases (instruction amnesia, guardrail escape via long contexts).

- [ ] **Temperature & Sampling Parameters:** Learn how **temperature, top-p (nucleus sampling), top-k, and frequency/presence penalties** control output randomness — understand that **higher temperature increases exploitability** by making the model more likely to produce unfiltered or unexpected outputs.

- [ ] **Retrieval-Augmented Generation (RAG):** Understand the full **RAG pipeline** (chunking → embedding → vector DB → retrieval → generation); know how each stage can be poisoned or manipulated.

- [ ] **Fine-Tuning Concepts:** Learn how **supervised fine-tuning (SFT), RLHF, and LoRA** work; understand how fine-tuning changes model behavior and creates new attack surfaces (backdoors, alignment drift).

- [ ] **AI Math Foundations:** Study the underlying math — **gradient descent, loss functions, attention weights, softmax probabilities** — to understand why adversarial inputs work and how to craft more effective attacks.

- [ ] **API Integration (Python & Bash):** Integrate **OpenAI, Claude (Anthropic), and Gemini (Google)** APIs into Python and Bash scripts; build wrappers for security automation tasks (recon summarization, vuln explanation, report drafting).

- [ ] **Prompt Engineering for Security:** Master structured prompting techniques — **system/user role separation, chain-of-thought, few-shot examples** — applied strictly to security contexts (threat modeling, CVE analysis, payload generation assistance).

- [ ] **AI/ML Course Grounding:** Complete foundational AI courses (e.g., **DeepLearning.AI Specialization** or **Google AI Essentials**) to understand the math behind models before testing them offensively.

---

<a id="stage-2-attack-surface-frameworks"></a>
### **Stage 2: Attack Surface & Frameworks**

> [!TIP]
> **Goal:** Map the AI/LLM attack surface using structured threat models.

- [ ] **OWASP LLM Top 10 (2025):** Prioritize **LLM01 Prompt Injection**, **LLM02 Sensitive Information Disclosure**, and **LLM10 Unbounded Consumption (denial-of-wallet)**; build test cases for each.

- [ ] **Model Scoping:** Identify **system prompts, guardrails, plugins/tools, retrieval sources, rate limits** and what data the model can reach.

- [ ] **Safety Policy Mapping:** Map controls to **content filters, tool permission boundaries, data classification**, and measure gaps.

---

<a id="stage-3-adversarial-techniques-llm01llm06"></a>
### **Stage 3: Adversarial Techniques (LLM01/LLM06)**

> [!TIP]
> **Goal:** Break safety controls and force unintended actions.

- [ ] **Jailbreaking:** Use **role-play prompts (e.g., DAN), multi-turn "crescendo" manipulation**, and **character/encoding obfuscation** to bypass safety layers.

- [ ] **Agentic Exploitation (LLM06 Excessive Agency):** Trick autonomous agents into **calling disallowed tools, escalating permissions, or executing dangerous actions**.

- [ ] **Prompt Injection:** Deliver **in-band and out-of-band injections** via user input, files, and linked resources to override system prompts.

---

> [!IMPORTANT]
> **Cluster 1 Move-On Gate (Stages 1–3: Foundations):** Before proceeding to Cluster 2, verify:
> - [ ] You can explain the Transformer architecture at a mechanistic level — attention heads, tokenization, context windows, and how temperature affects exploitability
> - [ ] You can execute 3 distinct prompt injection techniques (direct, indirect, multi-turn) against a live API and explain exactly why each one works at the prompt-processing level
> - [ ] You have tested at least 2 OWASP LLM Top 10 categories (LLM01 Prompt Injection, LLM02 Sensitive Info Disclosure) against a lab model (local Ollama, OpenAI API, or sandbox LLM)
> - [ ] You have built at least 1 Python script using an LLM API (OpenAI/Anthropic/Gemini) for a security task (payload generation, recon summarization, or report drafting)

> [!NOTE]
> **Reminder — Python ML Prerequisite:** Stages 7–10 require the ML skills verified in the Phase Entry Gate above. If you skipped that check or flagged a gap, resolve it before starting Stage 7 — not now, but before you reach it.

<a id="stage-4-rag-data-supply-chain-attacks"></a>
### **Stage 4: RAG & Data Supply Chain Attacks**

> [!TIP]
> **Goal:** Poison or subvert the knowledge base feeding the model.

- [ ] **RAG Poisoning:** Inject **malicious documents or vectors** into **vector DBs/indices** to induce **hallucinations or payload delivery**.

- [ ] **Retrieval Abuse:** Manipulate **chunking, scoring, metadata filters** to force **malicious context** into responses.

- [ ] **Data Exfil via RAG:** Weaponize **document recall** to leak **sensitive embeddings or proprietary content**.

---

<a id="stage-5-language-model-specific-attacks"></a>
### **Stage 5: Language Model Specific Attacks**

> [!TIP]
> **Goal:** Exploit LLM architecture and fine-tuning vulnerabilities.

- [ ] **Prompt Injection (LLM01):** Master **direct, indirect, multi-turn, and encoding-based injections** to override safety guardrails.

- [ ] **Excessive Agency (LLM06):** Force LLM-powered agents to **call unintended tools, escalate permissions, bypass access controls**.

- [ ] **Training Data Leakage:** Extract **memorized training data** via **completion, prefix completion, membership inference**.

- [ ] **Instruction Hierarchy Bypass:** Exploit **conflicting instructions** (system prompt vs. user input) to cause **unsafe behavior**.

- [ ] **Sycophancy & Alignment Hacking:** Manipulate models to prioritize **user approval over accuracy, safety**, causing deceptive outputs.

---

<a id="stage-6-multi-model-agent-attacks"></a>
### **Stage 6: Multi-Model & Agent Attacks**

> [!TIP]
> **Goal:** Exploit weaknesses in agentic and multi-model systems.

- [ ] **Agent Jailbreaking:** Trick **agents with tool access** to call **disallowed APIs or perform escalated actions**.

- [ ] **Tool Confusion:** Supply **conflicting or misleading tools** to cause **agent to misuse capabilities**.

- [ ] **Multi-Model Poisoning:** Compromise **upstream models** in a pipeline to degrade **downstream results**.

- [ ] **Agent Exfiltration:** Use **agent tool calls** to exfiltrate **data, model outputs, system information**.

- [ ] **Prompt Leakage via Agents:** Trigger **verbose logging or error messages** to leak **system prompts, API keys, context**.

---

<a id="stage-7-adversarial-examples-ml-robustness"></a>
### **Stage 7: Adversarial Examples & ML Robustness**

> [!TIP]
> **Goal:** Craft inputs that cause model misclassification or unexpected behavior.

- [ ] **Adversarial Patch Generation:** Create **minimal perturbations** (pixel-level or token-level) to flip model predictions (e.g., misclassify objects, bypass spam filters).

- [ ] **Universal Adversarial Perturbations (UAP):** Develop **single perturbation sequences** that fool the model across many inputs.

- [ ] **Text-Based Adversarial Examples:** Generate **typos, special chars, unicode tricks** to bypass **content filters, keyword detection**.

- [ ] **Robustness Testing Frameworks:** Use tools like **CleverHans, Foolbox, Adversarial-Robustness-Toolbox** to systematically find weaknesses.

- [ ] **Defense Evasion via Adversarial Samples:** Understand how **adversarial training, input sanitization, ensemble defenses** are applied.

---

<a id="stage-8-model-extraction-inversion"></a>
### **Stage 8: Model Extraction & Inversion**

> [!TIP]
> **Goal:** Steal or reverse-engineer the model's behavior and weights.

- [ ] **Model Extraction via API:** Use **probing queries, decision boundary mapping** to reverse-engineer **model architecture, layer sizes**.

- [ ] **Training Data Extraction:** Use **membership inference attacks** to determine if **specific data was in training set**.

- [ ] **Prompt Leakage:** Extract **system prompts, fine-tuning instructions, API keys** via **prompt injection, log manipulation**.

- [ ] **Functionality Cloning:** Build **surrogate model** that mimics extracted behavior, cheaper than using the original API.

---

<a id="stage-9-dataset-poisoning-backdoors"></a>
### **Stage 9: Dataset Poisoning & Backdoors**

> [!TIP]
> **Goal:** Corrupt training pipelines to install persistent behavior changes.

- [ ] **Label Flipping:** Inject **mislabeled examples** during training to degrade model accuracy on target classes.

- [ ] **Trojan/Backdoor Attacks:** Insert **trigger patterns** that cause specific misbehavior only when triggered (e.g., misclassify specific images when watermark present).

- [ ] **Gradual Poisoning:** Inject **subtle, distributed poisoning** to avoid detection while degrading performance.

- [ ] **Federated Learning Poisoning:** Attack **distributed training** by sending malicious gradients from compromised workers.

- [ ] **Supply Chain Poisoning:** Compromise **training data sources, pre-trained models, dependencies** to plant backdoors.

---

<a id="stage-10-privacy-attacks-pii-leakage"></a>
### **Stage 10: Privacy Attacks & PII Leakage**

> [!TIP]
> **Goal:** Extract private information embedded in models.

- [ ] **Membership Inference:** Determine if **specific records were used in training** via prediction confidence analysis.

- [ ] **Attribute Inference:** Deduce **sensitive attributes** of training individuals from model behavior.

- [ ] **Model Inversion:** Reconstruct **training data samples** (e.g., faces from facial recognition model).

- [ ] **Reconstruction Attacks:** Use **gradient descent** to reconstruct **sensitive inputs** from model outputs.

- [ ] **De-anonymization:** Link **anonymized training data** to real identities via **model predictions and external data**.

---

> [!IMPORTANT]
> **Cluster 2 Move-On Gate (Stages 4–10: Advanced LLM Attacks):** Before proceeding to Cluster 3, verify:
> - [ ] You have poisoned a local RAG system (e.g., LangChain + Chroma/FAISS) with a malicious document and demonstrated that the injected content appears in model responses triggered by specific queries
> - [ ] You have used CleverHans, Foolbox, or ART to generate at least 1 adversarial example that causes model misclassification — and you can explain why the perturbation works
> - [ ] You understand the difference between model extraction (reconstructing behavior via API queries) and model inversion (reconstructing training data) and can name the tools used for each
> - [ ] You have written a membership inference experiment: given a trained model and a set of examples, you can estimate which examples were in the training set using confidence scores
> - [ ] You can explain how label flipping and backdoor attacks differ in mechanism, detectability, and defense

<a id="stage-11-ai-augmented-red-team-workflow"></a>
### **Stage 11: AI-Augmented Red Team Workflow**

> [!TIP]
> **Goal:** Force-multiply your existing red team toolkit with AI-native tooling.

- [ ] **[Burp Suite](../Tools/Burp_Suite.md) AI Plugins:** Install and operate AI-powered Burp extensions — use **AI-assisted scanning, request analysis, and vulnerability explanation** plugins to accelerate web app assessments.

- [ ] **AutoRecon + LLM Analysis:** Run **AutoRecon** for automated multi-tool recon; pipe structured output into an **LLM (GPT/Claude/Gemini)** for intelligent prioritization, service context, and attack path recommendations.

- [ ] **PentestGPT:** Use **PentestGPT** (LLM-guided pentest assistant) to navigate complex engagement steps — test its guidance quality, understand its failure modes, and learn to correct its reasoning.

- [ ] **AI-Assisted Report Writing:** Use LLMs to draft **findings, risk ratings, and executive summaries** from structured notes; review and correct output for accuracy, then refine prompts for consistency.

- [ ] **AI Threat Modeling:** Apply LLM-assisted **STRIDE/PASTA threat modeling** — feed system architecture descriptions into an AI to enumerate threats; validate against manual analysis.

- [ ] **AI Forensics Concepts:** Understand how **AI systems leave forensic artifacts** (inference logs, model versioning, embedding stores) and how to investigate AI-assisted attacks post-incident.

---

<a id="stage-12-agentic-ai-autonomous-attack-infrastructure"></a>
### **Stage 12: Agentic AI & Autonomous Attack Infrastructure**

> [!TIP]
> **Goal:** Build autonomous agents that execute security tasks end-to-end.

- [ ] **LangChain for Security Automation:** Build **LangChain-based agents** in Python that chain tools (Nmap, Shodan API, CVE search, Burp) with LLM reasoning to automate multi-step recon and enumeration workflows.

- [ ] **CrewAI Multi-Agent Systems:** Design **CrewAI role-based agent crews** (e.g., Recon Agent + Exploit Agent + Report Agent) that collaborate autonomously on a penetration testing engagement.

- [ ] **Model Context Protocol (MCP):** Learn the **MCP standard** — how AI agents communicate with external tools and data sources; understand MCP server architecture and security implications of poorly scoped MCP permissions.

- [ ] **Adversarial Testing Against Live LLMs:** Practice offensive testing against **production LLMs** (within authorized scope/bug bounty programs) — attempt prompt injection, context manipulation, and tool abuse against real deployed systems.

- [ ] **AI-Specific CTFs:** Participate in **AI/LLM-focused Capture The Flag competitions** (e.g., Gandalf AI CTF, HackAPrompt, CTFd-based AI challenges) to build speed and creativity against novel AI attack scenarios.

- [ ] **Custom GPT for Recon Automation:** Build a **custom GPT or assistant** (via OpenAI API or open-source models) designed solely for reconnaissance automation — feeds it OSINT data, outputs structured attack surface maps and prioritized targets.

---

<a id="stage-13-tooling-evaluation"></a>
### **Stage 13: Tooling & Evaluation**

> [!TIP]
> **Goal:** Automate and measure AI red team coverage.

- [ ] **Red Team Tooling:** Use **PyRIT (Microsoft)**, **Garak**, **DeepTeam**, alongside traditional frameworks (**[Metasploit](../Tools/Metasploit_Framework.md)**) for orchestration.

- [ ] **Benchmarking:** Track **success rates** across **OWASP LLM Top 10** and **agent/tool abuse cases**; log **prompt, response, decision traces**.

- [ ] **Safety Regression:** Build **automated test suites** to prevent **prompt regressions** after model or policy updates.

---

<a id="stage-14-defense-responsible-ai"></a>
### **Stage 14: Defense & Responsible AI**

> [!TIP]
> **Goal:** Harden AI systems against attacks and ensure ethical deployment.

- [ ] **Input Validation & Sanitization:** Filter **prompt injections, adversarial patterns, malicious encodings**.

- [ ] **Output Guardrails:** Implement **content filtering, toxicity detection, sensitive info masking** on responses.

- [ ] **Model Hardening:** Use **adversarial training, regularization, ensemble methods** to improve robustness.

- [ ] **Monitoring & Detection:** Track **unusual queries, repeated failures, extraction signals** to detect attacks.

- [ ] **Audit Logging:** Log **all prompts, model outputs, decisions** for **post-incident forensics and compliance**.

- [ ] **Responsible Disclosure:** Establish **vulnerability bounty programs, responsible disclosure timelines** for AI security researchers.

- [ ] **Threat Model Documentation:** Maintain **risk register** of **known weaknesses, mitigations, residual risk** in AI systems.

---

<a id="stage-15-shadow-ai-organizational-ai-risk"></a>
### **Stage 15: Shadow AI & Organizational AI Risk**

> [!TIP]
> **Goal:** Understand and prevent unauthorized AI usage that creates organizational exposure.

- [ ] **Shadow AI Identification:** Detect **unauthorized use of public LLMs (ChatGPT, Gemini, Claude)** by employees pasting **source code, customer data, internal documents, API keys** into external AI services — creating **data leakage vectors** invisible to traditional DLP.

- [ ] **AI Data Loss Prevention (DLP):** Implement **DLP policies specific to AI services** — block/monitor traffic to **api.openai.com, generativelanguage.googleapis.com, api.anthropic.com** at the proxy/firewall level; deploy **endpoint DLP agents** that detect copy-paste of classified content into AI web interfaces.

- [ ] **AI Acceptable Use Policy:** Draft and enforce organizational **AI usage policies** defining **approved tools, data classification restrictions, prohibited use cases**, and **consequences for violations** — align with **NIST AI RMF** and **EU AI Act** requirements.

- [ ] **Approved AI Tooling:** Deploy **sanctioned, self-hosted AI solutions** (enterprise ChatGPT, Azure OpenAI, AWS Bedrock, local Ollama instances) with **audit logging, data retention controls, and access management** to replace shadow AI usage.

- [ ] **AI Supply Chain Risk:** Assess **third-party AI integrations** (Copilot, Grammarly, Jasper, AI coding assistants) for **data handling, model training opt-out, and contractual data protection** — treat each as a potential exfiltration channel.

---

<a id="stage-16-defensive-ai-operations"></a>
### **Stage 16: Defensive AI Operations**

> [!TIP]
> **Goal:** Deploy AI-powered defensive capabilities and detect AI-generated threats.

- [ ] **Deepfake Detection:** Understand and deploy tools for detecting **AI-generated images, video, and audio** — study **artifact analysis (compression patterns, frequency domain), temporal inconsistency detection, and provenance verification (C2PA/Content Credentials)**.

- [ ] **AI Voice Cloning Defense:** Implement **voice authentication hardening** against **ElevenLabs/RVC-style cloning attacks** — deploy **anti-spoofing liveness detection, challenge-response voice verification**, and **ban voice-only authorization** for sensitive operations.

- [ ] **AI-Enhanced Phishing Detection:** Deploy **ML/NLP-based email analysis** to detect **AI-generated phishing** that bypasses traditional signature-based filters — train classifiers on **stylometric analysis, sender behavior anomalies, and LLM-characteristic writing patterns**.

- [ ] **AI-Powered SOC Integration:** Leverage **AI/ML for security operations** — use **anomaly detection models** for network traffic, **NLP-based log analysis** for threat hunting, and **automated alert triage** to handle volume at scale without analyst burnout.

- [ ] **AI Incident Response:** Develop **playbooks for AI-specific incidents** — compromised model endpoints, data poisoning detection, prompt injection campaigns, unauthorized model access, and **AI-generated social engineering at scale**.

- [ ] **AI Forensics:** Understand how **AI systems leave forensic artifacts** — **inference logs, model versioning, embedding stores, fine-tuning datasets, API call histories** — and how to investigate AI-assisted attacks post-incident.

---

> [!IMPORTANT]
> **Cluster 3 Move-On Gate (Stages 11–16: Operational & Defensive AI):** Before proceeding to the portfolio/career stages (17–18), verify:
> - [ ] You have used an AI tool (PentestGPT, AutoRecon + LLM, Burp AI plugin) to complete a real security task that would have taken you significantly longer manually — and you can explain exactly where the AI helped and where it failed
> - [ ] You have built a working agentic pipeline (LangChain, CrewAI, or MCP-based) that executes at least 2 tool calls in sequence to complete a security research task autonomously
> - [ ] You have deployed at least 1 defensive AI detection: a deepfake detection check, ML-enhanced log anomaly model, or AI phishing classifier — and you can measure its false positive rate against benign data
> - [ ] You can explain 3 forensic artifacts that an LLM-powered attack campaign would leave behind (API call logs, embedding store queries, model version history) and describe how you would collect them during a DFIR engagement

<a id="stage-17-ai-security-projects-portfolio"></a>
### **Stage 17: AI Security Projects & Portfolio**


> [!TIP]
> **Goal:** Prove production capability through real, complex, integrated AI-security projects.

- [ ] **AI-Driven Fuzzer (C/C++):** Build a **machine learning-guided fuzzer** in C/C++ that uses coverage feedback and learned mutation strategies to discover vulnerabilities faster than traditional dumb fuzzing.

- [ ] **Automated Payload Obfuscator:** Develop an AI-assisted tool that **automatically transforms payloads** (shellcode, scripts) to evade AV/EDR signatures using LLM-guided encoding, variable substitution, and structure mutation.

- [ ] **Integrated AI-Security Project (GitHub):** Push **2–3 highly complex, integrated AI-security tools** to a public GitHub repository — include README, architecture diagrams, usage examples, and documented attack scenarios.

- [ ] **Technical Writeups (Medium/LinkedIn):** Write **substantive, technical breakdowns** of your AI security research — document methodology, failures, and findings in long-form posts targeting both practitioners and hiring managers.

- [ ] **Community Presentation:** Present findings at **local hacker meetups, BSides, or DEF CON AI Village** — build credibility through live demonstrations and Q&A with the community.

---

<a id="stage-18-ai-security-career-targeting"></a>
### **Stage 18: AI Security Career Targeting**

> [!TIP]
> **Goal:** Position yourself specifically for AI-native security roles.

- [ ] **AI Security Role Identification:** Target roles explicitly requiring **AI security skills** — LLM Red Teamer, AI Safety Engineer, ML Security Researcher, Prompt Security Engineer — at AI labs, security consultancies, and enterprise AI teams.

- [ ] **Resume Differentiation:** Highlight **autonomous systems engineered, agents built, AI tools integrated** — frame contributions in terms of capability delivered, not just technologies used.

- [ ] **AI Security Community Engagement:** Contribute to **OWASP LLM Top 10 working group**, open-source AI security tools (**Garak, PyRIT**), or AI safety research to build verifiable community presence.

- [ ] **Portfolio Alignment:** Ensure your **GitHub, Medium, and LinkedIn** tell a coherent story — each project links to a writeup, each writeup links to working code.

---

### **Lab Progression (Part 38: AI Security)**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Complete Gandalf AI CTF and HackAPrompt challenges (first 10 levels each) | Challenge solutions with exploit methodology documented |
| 2 | Build a RAG poisoning PoC against a local LangChain/LlamaIndex application | RAG attack report with injection payloads and impact analysis |
| 3 | Build an AI-driven fuzzer or automated payload obfuscator and publish to GitHub | Working tool with README, architecture diagram, and demo |

> [!IMPORTANT]
> **Move-On Gate (Part 38):** Execute prompt injection attacks across multiple models, demonstrate RAG poisoning in a lab, and publish an AI security tool to GitHub with documentation.

---

### 🏆 Phase 9 Capstone Project

**Red-Team an LLM Application and Produce a Professional AI Security Assessment**

- [ ] **Set up a local RAG application** (LangChain/LlamaIndex + local model + vector DB)
- [ ] **Execute a structured AI red team engagement** covering OWASP LLM Top 10 categories
- [ ] **Document attack chains** including prompt injection, RAG poisoning, and agent manipulation
- [ ] **Propose defensive controls** for each finding

**Deliverables:**
- [ ] Professional AI security assessment report (executive summary, methodology, findings, remediation)
- [ ] Categorized payload library (prompt injections, jailbreaks, RAG poisoning vectors)
- [ ] At least 1 AI security tool published to GitHub with README and documentation
- [ ] All research committed to your Git repository

> [!IMPORTANT]
> **Capstone Gate:** Your assessment report must cover at least 5 OWASP LLM Top 10 categories with working proof-of-concept attacks and actionable defensive recommendations.

---

### 🧭 Phase 9 Reflection & Competency Check

- [ ] **Reflection:** Which AI risk depended most on traditional security fundamentals rather than model behavior?
- [ ] **Reflection:** Which experiments failed, and what did those failures reveal about methodology?
- [ ] **Competency:** Can you test prompt injection, RAG poisoning, and agent/tool abuse with repeatable methodology?
- [ ] **Competency:** Can you distinguish model limitations, application design flaws, and infrastructure weaknesses?
- [ ] **Competency:** Can you recommend defenses that are testable, observable, and realistic for engineering teams?

> [!IMPORTANT]
> **Phase Completion Gate:** Move on only when your AI security assessment is reproducible, evidence-backed, and grounded in both AI-specific and traditional security controls.

---
