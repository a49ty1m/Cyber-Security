# Stage 5: Advanced & Specialized Operations

---

### 🧭 Navigation
◀ [Stage 4: Enterprise](Stage-4_Enterprise.md) | 🏠 [Master Roadmap](README.md) | [Shelf: Post-Hire](Shelf_Post-Hire.md) ➔

---

> [!NOTE]
> **Stage Overview**
> - **⏱️ Time Commitment:** 4–6 months
> - **🎯 Primary Focus:** Custom C2 development, binary loaders, shellcode injection, AMSI/ETW evasion, AI & LLM red teaming, advanced red team campaign infrastructure, and public portfolio development.

---

<a id="module-27-offensive-development--tooling"></a>
<a id="part-42-offensive-development-tooling"></a>

## Module 27: Offensive Development & Tooling


> [!IMPORTANT]
> **Start here — before Part 42 and Part 28.** This is the deferred half of Phase 1 Stage 7. C and C++ require debugger experience and binary analysis context to learn meaningfully. You now have that context. Complete this stage before starting Part 42 (Offensive Development) or Part 28 (Reverse Engineering). Return to Stage-1_Foundation.md for the structural marker — this is the actual content.

> [!TIP]
> **Goal:** Build the C and C++ foundations required for shellcode writing, exploit development, Windows API exploitation, and reverse engineering of compiled binaries. These are not general-purpose programming languages at this stage — they are the substrate of offensive development and RE.

### **C Language — Systems Programming & Exploit Foundations**

- [ ] **Memory Model & Pointers:** Understand the difference between stack and heap allocation. Master pointer arithmetic, pointer-to-pointer, function pointers, void pointers. Know why `int *p = &x` vs `int *p = malloc(sizeof(int))` have different lifetime semantics.

- [ ] **Memory Layout:** Understand the process address space: text segment (code), data segment (globals/statics), BSS (uninitialised globals), heap (grows up), stack (grows down). Know how local variables, function arguments, and return addresses are laid out on the stack. Draw this from memory — it is the foundation of all stack-based exploitation.

- [ ] **Stack Frames:** Understand function prologue/epilogue (`push rbp; mov rbp, rsp` / `pop rbp; ret`). Know where the return address lives relative to local variables. Know why `gets()`, `strcpy()`, and `sprintf()` are dangerous by design. Understand buffer overflow mechanics at the C level before touching pwntools.

- [ ] **C Standard Library (Security-Relevant Subset):**
  - String functions: `strcpy/strncpy`, `sprintf/snprintf`, `gets/fgets`, `strlen`, `memcpy/memmove`, `memset`
  - File I/O: `fopen`, `fread`, `fwrite`, `fclose`, `mmap`
  - Process/system: `system()`, `execve()`, `fork()`, `exit()`, `signal()`
  - Dynamic memory: `malloc`, `calloc`, `realloc`, `free` — and what happens when you double-free, use-after-free, or heap-overflow

- [ ] **Compilation Pipeline:** Understand: C source → preprocessor → compiler → assembler → linker → ELF/PE binary. Know what `gcc -g -O0 -fno-stack-protector -no-pie` does and why those flags matter for exploit development. Understand debug symbols, DWARF format, and stripped vs unstripped binaries.

- [ ] **Inline Assembly & `__asm__`:** Write basic inline assembly from C — read/write register values, invoke syscalls directly. Understand why this is the bridge between C and shellcode writing.

- [ ] **Win32 API Basics (Windows C):**
  - Process and thread creation: `CreateProcess`, `OpenProcess`, `CreateRemoteThread`
  - Memory operations: `VirtualAlloc`, `VirtualProtect`, `WriteProcessMemory`, `ReadProcessMemory`
  - Handle management: `OpenProcess`, `CloseHandle`, `DuplicateHandle`
  - These are the primitives behind every Windows process injection technique.

**Lab:** Write a C program that: allocates memory with `VirtualAlloc`, copies shellcode into it, calls `VirtualProtect` to make it executable, then executes it with a function pointer. This is the simplest process injection in its own process — understand every line.

---

### **C++ — Reverse Engineering Context**

- [ ] **Object Model & Memory Layout:** Understand how C++ objects are laid out in memory: the this pointer, member variables at fixed offsets, vtable pointer at offset 0 for polymorphic objects. Know why `sizeof(MyClass)` may surprise you (padding, vtable pointer).

- [ ] **Virtual Function Tables (vtables):** Understand that each polymorphic class has one vtable (a static array of function pointers). Each instance has a vtptr (hidden pointer to the vtable). Virtual dispatch = dereference vtptr → index into vtable → call function. Know what this looks like in disassembly: `mov rax, [rcx]; call [rax+0x18]`. This pattern appears constantly in RE of Windows binaries.

- [ ] **RTTI (Run-Time Type Information):** Understand what `dynamic_cast` and `typeid` produce in compiled code — the `__RTTICompleteObjectLocator` structure preceding the vtable. Know how to read it in a disassembler.

- [ ] **Smart Pointers & RAII:** Understand `unique_ptr`, `shared_ptr`, `weak_ptr`. In RE context, recognise `shared_ptr` patterns (reference count + control block layout) in compiled code.

- [ ] **STL Internals (Recognise in RE):** Know the memory layout of `std::string` (SSO), `std::vector` (pointer + size + capacity), and `std::map` (red-black tree node structure). You will encounter these constantly when reversing C++ binaries.

**Lab:** Compile a C++ class with a virtual function, disassemble it with objdump or Ghidra, locate the vtable, and manually trace the virtual dispatch mechanism. Then do the same with a class hierarchy (base + derived) and verify the vtptr is overwritten correctly.

---

### **Move-On Gate (Stage 7B)**

> [!IMPORTANT]
> You are ready to proceed to Part 42 (Offensive Development) when:
> - [ ] You can write a C program that performs shellcode execution via `VirtualAlloc` + `VirtualProtect` + function pointer
> - [ ] You can explain what happens at each instruction of a function call (stack frame construction, argument passing, return address, local variables)
> - [ ] You can open a compiled C++ binary in Ghidra and locate the vtable of a polymorphic class
> - [ ] You understand why `gets()` is exploitable and can draw the stack layout that makes a basic buffer overflow work

---

<a id="toc-part-42-offensive-development--tooling"></a>
<a id="part-42-offensive-development-tooling"></a>



> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Black Hat Python 2nd Edition` — Primary companion — C2 building, RAT development, evasion, and custom offensive tooling
> - 🟡 `Black Hat Go Go Programming For Hackers and Pentesters` — Full — modern Go-based offensive tooling and implant development
> - 🟡 `Gray Hat Python - Seitz, Justin` — Full — debugging, fuzzing, shellcode injection, and process manipulation via Python
> - 🟢 `REALWORLDPYTHON Hackers Guide 2020` — Full — real-world offensive Python automation projects

> **Prerequisite Placement Note:** Part 42 is positioned here at the entrance of Phase 7 (immediately following Stage 7B: C/C++ Systems Programming) because it forms the mandatory offensive development foundation required for Part 29 (Modern Exploitation) and advanced tradecraft. Complete Part 42 before tackling memory corruption in Part 29.

<a id="stage-1-exploit-development-foundation"></a>
### **Stage 1: Exploit Development Foundation** — `🔬 Practical`

- [ ] **Exploit Prototyping:** Use Python with **pwntools, [impacket](Tools/Impacket.md)** for **rapid PoC development**, **fuzzing harnesses**, and **custom C2 implant logic**.

- [ ] **Buffer Overflow Mastery:** Write **stack-based buffer overflow exploits**, understand **stack frame layout, return address overwrite, NOP sleds**, and **bad character identification**.

- [ ] **Shellcode Writing:** Craft **position-independent shellcode** for **reverse shells, bind shells, staged loaders** avoiding null bytes and bad characters.

- [ ] **Egghunters:** Build **egghunter shellcode** to locate payloads in memory when buffer space is limited.

- [ ] **x86/x64 Assembly:** Develop working fluency in **MOV, PUSH, POP, CALL, JMP, INT, SYSCALL** and understand **calling conventions (cdecl, stdcall, fastcall, System V AMD64)**.

- [ ] **Disassembly Reading:** Confidently read **disassembled output** in **Ghidra, IDA Pro, radare2** to identify vulnerabilities and understand compiled logic.

<a id="stage-2-windows-offensive-development"></a>
### **Stage 2: Windows Offensive Development** — `🔬 Practical`

- [ ] **Win32 API Exploitation:** Use **CreateProcess, VirtualAlloc, WriteProcessMemory, CreateRemoteThread** for **process injection, DLL loading, and token manipulation**.

- [ ] **EDR Architecture & Telemetry Sources:**
  - **Userland API Hooking:** Understand how EDRs inject custom DLLs into new processes to hook NTDLL exported syscall stubs (`NtProtectVirtualMemory`, `NtWriteVirtualMemory`) with `JMP` instructions to redirect control flow to inspection engines.
  - **Bypassing Hooks:** Implement API unhooking (reloading clean `.text` section from disk NTDLL or `KnownDlls`), direct syscalls (`Syswhispers3`), and indirect syscalls (jumping into existing syscall instructions within NTDLL to preserve call stack legitimacy).
  - **Kernel Callbacks & Minifilters:** Understand telemetry generated via `PsSetCreateProcessNotifyRoutineEx`, `PsSetCreateThreadNotifyRoutine`, `ObRegisterCallbacks` (process handle stripping), and filesystem minifilter drivers.
  - **ETW-TI (Threat Intelligence):** Understand kernel-level ETW telemetry provided directly by the Windows kernel to EDR sensors, bypassing userland hooks.

- [ ] **C# & .NET Offensive Tooling:** Master **P/Invoke and D/Invoke** to call **native Win32 APIs** from managed code. Understand tools like **SharpHound, Rubeus, Seatbelt, SharpUp, Certify** and how to **modify/recompile** them to evade signatures.

- [ ] **In-Memory Execution:** Master **.NET assembly loading (Assembly.Load), reflection, and inline execution** to run offensive tools without dropping files to disk.

- [ ] **AMSI/ETW Bypass:** Understand how **.NET interacts with AMSI** and **ETW** and techniques to patch or disable them at runtime.

- [ ] **Offensive PowerShell:** Master **download cradles, constrained language mode escape, script block logging evasion**, and **AMSI bypass in PowerShell**.

<a id="stage-3-linux-offensive-development"></a>
### **Stage 3: Linux Offensive Development** — `🔬 Practical`

- [ ] **Linux C Development:** Interact with **POSIX APIs, /proc filesystem, ptrace**, and **LD_PRELOAD hooking** for rootkit/implant development.

- [ ] **ELF Binary Manipulation:** Understand **ELF format, GOT/PLT, dynamic linking** for binary patching and implant injection.

<a id="stage-4-c2-implant-development"></a>
### **Stage 4: C2 & Implant Development** — `🔬 Practical`

- [ ] **C2 Architecture:** Design **client-server implant architecture** with **modular payloads, encrypted channels, and sleep obfuscation**.

- [ ] **Protocol Selection:** Choose and implement **HTTP/HTTPS, DNS, named pipes, or cloud API** channels for C2 communication.

- [ ] **C++ Tooling:** Build **custom implants, packers, crypters**, and **network tools** requiring performance and low-level control.

- [ ] **Evasion Integration:** Combine **sleep obfuscation, call stack spoofing, indirect syscalls, and API unhooking** into implant design.

<a id="lab-progression-part-42-offensive-development-tooling"></a>
### **Lab Progression (Part 42: Offensive Development & Tooling)**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Exploit a basic stack buffer overflow (SLMail/Brainpan) | Working exploit script |
| 2 | Write custom shellcode for a reverse shell (x86) | Shellcode + test harness |
| 3 | Build a basic C2 implant (Python client → Python server) | Working C2 demo in lab |
| 4 | Modify a SharpHound/Rubeus tool to evade signatures | Modified tool + AV scan comparison |
| 5 | Implement AMSI bypass + in-memory .NET execution chain | End-to-end evasion demo in lab |

> [!IMPORTANT]
> **Move-On Gate:** You can write working exploits, develop custom shellcode, build basic C2 implants, modify existing offensive tools to evade detection, and bypass AMSI/ETW in a controlled lab environment.

---

<a id="part-27-digital-forensics"></a>

---

<a id="module-28-ai--llm-red-teaming"></a>
<a id="part-38-ai-llm-red-teaming"></a>

## Module 28: AI & LLM Red Teaming


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
### **Stage 1: AI Fundamentals for Security Practitioners** — `🧠 Conceptual`

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
### **Stage 2: Attack Surface & Frameworks** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Map the AI/LLM attack surface using structured threat models.

- [ ] **OWASP LLM Top 10 (2025):** Prioritize **LLM01 Prompt Injection**, **LLM02 Sensitive Information Disclosure**, and **LLM10 Unbounded Consumption (denial-of-wallet)**; build test cases for each.

- [ ] **Model Scoping:** Identify **system prompts, guardrails, plugins/tools, retrieval sources, rate limits** and what data the model can reach.

- [ ] **Safety Policy Mapping:** Map controls to **content filters, tool permission boundaries, data classification**, and measure gaps.

---

<a id="stage-3-adversarial-techniques-llm01llm06"></a>
### **Stage 3: Adversarial Techniques (LLM01/LLM06)** — `🔬 Practical`

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
### **Stage 4: RAG & Data Supply Chain Attacks** — `🔬 Practical`

> [!TIP]
> **Goal:** Poison or subvert the knowledge base feeding the model.

- [ ] **RAG Poisoning:** Inject **malicious documents or vectors** into **vector DBs/indices** to induce **hallucinations or payload delivery**.

- [ ] **Retrieval Abuse:** Manipulate **chunking, scoring, metadata filters** to force **malicious context** into responses.

- [ ] **Data Exfil via RAG:** Weaponize **document recall** to leak **sensitive embeddings or proprietary content**.

---

<a id="stage-5-language-model-specific-attacks"></a>
### **Stage 5: Language Model Specific Attacks** — `🔬 Practical`

> [!TIP]
> **Goal:** Exploit LLM architecture and fine-tuning vulnerabilities.

- [ ] **Prompt Injection (LLM01):** Master **direct, indirect, multi-turn, and encoding-based injections** to override safety guardrails.

- [ ] **Excessive Agency (LLM06):** Force LLM-powered agents to **call unintended tools, escalate permissions, bypass access controls**.

- [ ] **Training Data Leakage:** Extract **memorized training data** via **completion, prefix completion, membership inference**.

- [ ] **Instruction Hierarchy Bypass:** Exploit **conflicting instructions** (system prompt vs. user input) to cause **unsafe behavior**.

- [ ] **Sycophancy & Alignment Hacking:** Manipulate models to prioritize **user approval over accuracy, safety**, causing deceptive outputs.

---

<a id="stage-6-multi-model-agent-attacks"></a>
### **Stage 6: Multi-Model & Agent Attacks** — `🔬 Practical`

> [!TIP]
> **Goal:** Exploit weaknesses in agentic and multi-model systems.

- [ ] **Agent Jailbreaking:** Trick **agents with tool access** to call **disallowed APIs or perform escalated actions**.

- [ ] **Tool Confusion:** Supply **conflicting or misleading tools** to cause **agent to misuse capabilities**.

- [ ] **Multi-Model Poisoning:** Compromise **upstream models** in a pipeline to degrade **downstream results**.

- [ ] **Agent Exfiltration:** Use **agent tool calls** to exfiltrate **data, model outputs, system information**.

- [ ] **Prompt Leakage via Agents:** Trigger **verbose logging or error messages** to leak **system prompts, API keys, context**.

---

<a id="stage-7-adversarial-examples-ml-robustness"></a>
### **Stage 7: Adversarial Examples & ML Robustness** — `🔬 Practical`

> [!TIP]
> **Goal:** Craft inputs that cause model misclassification or unexpected behavior.

- [ ] **Adversarial Patch Generation:** Create **minimal perturbations** (pixel-level or token-level) to flip model predictions (e.g., misclassify objects, bypass spam filters).

- [ ] **Universal Adversarial Perturbations (UAP):** Develop **single perturbation sequences** that fool the model across many inputs.

- [ ] **Text-Based Adversarial Examples:** Generate **typos, special chars, unicode tricks** to bypass **content filters, keyword detection**.

- [ ] **Robustness Testing Frameworks:** Use tools like **CleverHans, Foolbox, Adversarial-Robustness-Toolbox** to systematically find weaknesses.

- [ ] **Defense Evasion via Adversarial Samples:** Understand how **adversarial training, input sanitization, ensemble defenses** are applied.

---

<a id="stage-8-model-extraction-inversion"></a>
### **Stage 8: Model Extraction & Inversion** — `🔬 Practical`

> [!TIP]
> **Goal:** Steal or reverse-engineer the model's behavior and weights.

- [ ] **Model Extraction via API:** Use **probing queries, decision boundary mapping** to reverse-engineer **model architecture, layer sizes**.

- [ ] **Training Data Extraction:** Use **membership inference attacks** to determine if **specific data was in training set**.

- [ ] **Prompt Leakage:** Extract **system prompts, fine-tuning instructions, API keys** via **prompt injection, log manipulation**.

- [ ] **Functionality Cloning:** Build **surrogate model** that mimics extracted behavior, cheaper than using the original API.

---

<a id="stage-9-dataset-poisoning-backdoors"></a>
### **Stage 9: Dataset Poisoning & Backdoors** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Corrupt training pipelines to install persistent behavior changes.

- [ ] **Label Flipping:** Inject **mislabeled examples** during training to degrade model accuracy on target classes.

- [ ] **Trojan/Backdoor Attacks:** Insert **trigger patterns** that cause specific misbehavior only when triggered (e.g., misclassify specific images when watermark present).

- [ ] **Gradual Poisoning:** Inject **subtle, distributed poisoning** to avoid detection while degrading performance.

- [ ] **Federated Learning Poisoning:** Attack **distributed training** by sending malicious gradients from compromised workers.

- [ ] **Supply Chain Poisoning:** Compromise **training data sources, pre-trained models, dependencies** to plant backdoors.

---

<a id="stage-10-privacy-attacks-pii-leakage"></a>
### **Stage 10: Privacy Attacks & PII Leakage** — `🔬 Practical`

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
### **Stage 11: AI-Augmented Red Team Workflow** — `🔬 Practical`

> [!TIP]
> **Goal:** Force-multiply your existing red team toolkit with AI-native tooling.

- [ ] **[Burp Suite](Tools/Burp_Suite.md) AI Plugins:** Install and operate AI-powered Burp extensions — use **AI-assisted scanning, request analysis, and vulnerability explanation** plugins to accelerate web app assessments.

- [ ] **AutoRecon + LLM Analysis:** Run **AutoRecon** for automated multi-tool recon; pipe structured output into an **LLM (GPT/Claude/Gemini)** for intelligent prioritization, service context, and attack path recommendations.

- [ ] **PentestGPT:** Use **PentestGPT** (LLM-guided pentest assistant) to navigate complex engagement steps — test its guidance quality, understand its failure modes, and learn to correct its reasoning.

- [ ] **AI-Assisted Report Writing:** Use LLMs to draft **findings, risk ratings, and executive summaries** from structured notes; review and correct output for accuracy, then refine prompts for consistency.

- [ ] **AI Threat Modeling:** Apply LLM-assisted **STRIDE/PASTA threat modeling** — feed system architecture descriptions into an AI to enumerate threats; validate against manual analysis.

- [ ] **AI Forensics Concepts:** Understand how **AI systems leave forensic artifacts** (inference logs, model versioning, embedding stores) and how to investigate AI-assisted attacks post-incident.

---

<a id="stage-12-agentic-ai-autonomous-attack-infrastructure"></a>
### **Stage 12: Agentic AI & Autonomous Attack Infrastructure** — `🔬 Practical`

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
### **Stage 13: Tooling & Evaluation** — `🔬 Practical`

> [!TIP]
> **Goal:** Automate and measure AI red team coverage.

- [ ] **Red Team Tooling:** Use **PyRIT (Microsoft)**, **Garak**, **DeepTeam**, alongside traditional frameworks (**[Metasploit](Tools/Metasploit_Framework.md)**) for orchestration.

- [ ] **Benchmarking:** Track **success rates** across **OWASP LLM Top 10** and **agent/tool abuse cases**; log **prompt, response, decision traces**.

- [ ] **Safety Regression:** Build **automated test suites** to prevent **prompt regressions** after model or policy updates.

---

<a id="stage-14-defense-responsible-ai"></a>
### **Stage 14: Defense & Responsible AI** — `🧠 Conceptual`

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
### **Stage 15: Shadow AI & Organizational AI Risk** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Understand and prevent unauthorized AI usage that creates organizational exposure.

- [ ] **Shadow AI Identification:** Detect **unauthorized use of public LLMs (ChatGPT, Gemini, Claude)** by employees pasting **source code, customer data, internal documents, API keys** into external AI services — creating **data leakage vectors** invisible to traditional DLP.

- [ ] **AI Data Loss Prevention (DLP):** Implement **DLP policies specific to AI services** — block/monitor traffic to **api.openai.com, generativelanguage.googleapis.com, api.anthropic.com** at the proxy/firewall level; deploy **endpoint DLP agents** that detect copy-paste of classified content into AI web interfaces.

- [ ] **AI Acceptable Use Policy:** Draft and enforce organizational **AI usage policies** defining **approved tools, data classification restrictions, prohibited use cases**, and **consequences for violations** — align with **NIST AI RMF** and **EU AI Act** requirements.

- [ ] **Approved AI Tooling:** Deploy **sanctioned, self-hosted AI solutions** (enterprise ChatGPT, Azure OpenAI, AWS Bedrock, local Ollama instances) with **audit logging, data retention controls, and access management** to replace shadow AI usage.

- [ ] **AI Supply Chain Risk:** Assess **third-party AI integrations** (Copilot, Grammarly, Jasper, AI coding assistants) for **data handling, model training opt-out, and contractual data protection** — treat each as a potential exfiltration channel.

---

<a id="stage-16-defensive-ai-operations"></a>
### **Stage 16: Defensive AI Operations** — `🧠🔬 Mixed`

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
### **Stage 17: AI Security Projects & Portfolio** — `🔬 Practical`


> [!TIP]
> **Goal:** Prove production capability through real, complex, integrated AI-security projects.

- [ ] **AI-Driven Fuzzer (C/C++):** Build a **machine learning-guided fuzzer** in C/C++ that uses coverage feedback and learned mutation strategies to discover vulnerabilities faster than traditional dumb fuzzing.

- [ ] **Automated Payload Obfuscator:** Develop an AI-assisted tool that **automatically transforms payloads** (shellcode, scripts) to evade AV/EDR signatures using LLM-guided encoding, variable substitution, and structure mutation.

- [ ] **Integrated AI-Security Project (GitHub):** Push **2–3 highly complex, integrated AI-security tools** to a public GitHub repository — include README, architecture diagrams, usage examples, and documented attack scenarios.

- [ ] **Technical Writeups (Medium/LinkedIn):** Write **substantive, technical breakdowns** of your AI security research — document methodology, failures, and findings in long-form posts targeting both practitioners and hiring managers.

- [ ] **Community Presentation:** Present findings at **local hacker meetups, BSides, or DEF CON AI Village** — build credibility through live demonstrations and Q&A with the community.

---

<a id="stage-18-ai-security-career-targeting"></a>
### **Stage 18: AI Security Career Targeting** — `🧠 Conceptual`

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

---

<a id="module-29-red-team-operations--tradecraft"></a>
<a id="part-40-red-team-operations-tradecraft"></a>

## Module 29: Red Team Operations & Tradecraft


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Red Team Field Manual v3` — ⚡ Keep open at all times — the fastest command reference for every red team tool and technique
> - 🟡 `The Red Report 2023` — Full — current attacker TTP trends and attacker behavior data from real incidents
> - 🟡 `Threat Intelligence Handbook` — Full — CTI methodology for adversary profiling and red team planning
> - 🟢 `Cybersecurity Attack-and-Defense Strategies 2nd` — Reference — structured red team operation planning


> **Why This Exists:** Penetration testing finds vulnerabilities. Red teaming tests the organization's ability to detect, respond, and contain a determined adversary. This Part covers the operational tradecraft, C2 infrastructure, and campaign management that separates a pentester from a red team operator. Building on the foundational scoping and reporting frameworks of Part 39, Part 40 focuses on executing stealthy, multi-stage adversary simulations.

<a id="strategy-core-operations"></a>
<a id="stage-1-campaign-planning-infrastructure"></a>

### **Stage 1: Campaign Planning & Infrastructure** — `🔬 Practical`

> [!TIP]
> **Goal:** Define the operation's objectives, rules of engagement, and build the technical infrastructure before any offensive action begins.

- [ ] **Red Team vs Pentest vs Vuln Assessment:** Understand the fundamental differences — pentests find vulnerabilities with broad scope; red teams test **specific objectives** (e.g., "can an attacker reach the CEO's inbox?") with stealth as a constraint; vulnerability assessments are breadth-first, red teams are depth-first.

- [ ] **Campaign Planning & Objectives:** Define **clear objectives** aligned with business risk — data exfiltration, domain compromise, physical access to server room, insider threat simulation. Write a **red team campaign plan** with rules of engagement, communication protocols, deconfliction procedures, and abort criteria.

- [ ] **C2 Framework Mastery:** Deploy and operate at least 2 C2 frameworks — **Sliver** (open-source, modern), **Mythic** (modular, multi-platform), Cobalt Strike (industry standard, commercial), or **Havoc**. Understand **listener types, payload generation, staging vs stageless, sleep/jitter tuning, and kill dates**.

- [ ] **Infrastructure Setup:** Build **resilient attack infrastructure** — redirectors (Apache mod_rewrite, Nginx reverse proxy, cloud functions), domain categorization for reputation, HTTPS certificates (Let's Encrypt), CDN fronting, and infrastructure teardown procedures. Separate **short-haul (interactive) and long-haul (persistent) C2 channels**.

---

<a id="stage-2-initial-access-payload-delivery"></a>

### **Stage 2: Initial Access & Payload Delivery** — `🔬 Practical`

> [!TIP]
> **Goal:** Gain a foothold using tradecraft that survives email gateways, sandboxes, and EDR — and leaves minimal forensic trace.

- [ ] **Initial Access Tradecraft:** Master **phishing (spearphishing with pretexting, HTML smuggling, macro-free Office exploitation)**, **external service exploitation**, and **supply chain vectors**. Build payloads that survive email gateways, sandboxes, and EDR.

---

<a id="stage-3-opsec-persistence-lateral-movement"></a>

### **Stage 3: OPSEC, Persistence & Lateral Movement** — `🔬 Practical`

> [!TIP]
> **Goal:** Maintain stealth while expanding access — blend with normal traffic, establish redundant persistence, and move laterally without triggering detection.

- [ ] **OPSEC Discipline:** Maintain **operational security** throughout campaigns — avoid detection by **blending with normal traffic patterns, using legitimate tools (LOLBins), timestomping, log manipulation, and process injection into trusted processes**. Monitor your own indicators: if a defender could fingerprint your C2 beacon pattern, you've failed.

- [ ] **Persistence Mechanisms:** Implement **multiple persistence layers** — registry run keys, scheduled tasks, WMI subscriptions, DLL search order hijacking, golden/silver tickets, and **out-of-band persistence** (cloud-based implants, trusted application abuse). Test persistence across reboots and credential rotations.

- [ ] **Lateral Movement & Pivoting:** Traverse networks using **Pass-the-Hash, Pass-the-Ticket, overpass-the-hash, DCOM, WMI, WinRM, SSH tunneling, SOCKS proxies**. Document every pivot and maintain network maps during operations.

---

<a id="stage-4-data-exfiltration-impact"></a>

### **Stage 4: Data Exfiltration & Impact** — `🔬 Practical`

> [!TIP]
> **Goal:** Reach the campaign objective — exfiltrate data or demonstrate impact — without triggering DLP or anomaly-based detection.

- [ ] **Data Exfiltration:** Practice **covert exfiltration** — DNS tunneling, HTTPS over legitimate SaaS (Slack, Teams, Google Drive), steganography, scheduled low-and-slow transfers. Measure data rates and detection thresholds.

---

<a id="stage-5-deconfliction-reporting-wrap-up"></a>

### **Stage 5: Deconfliction, Reporting & Wrap-Up** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Close the operation safely, hand off findings, and produce a campaign report that improves the client's detection capability.

- [ ] **Campaign Reporting:** Write **red team reports** distinct from pentest reports — focus on **attack narrative (timeline of actions), detection opportunities missed by defenders, and organizational resilience assessment**. Include **detection timeline analysis** showing what the blue team saw vs what they missed.

- [ ] **Deconfliction & Safety:** Maintain a **real-time deconfliction log** with the client's point of contact. Know when to **pause, abort, or escalate** — finding real compromises during a red team engagement requires immediate deconfliction. Never cause unintended business impact.

### **Lab Progression (Part 40: Red Team Operations & Tradecraft)**

| Level | Task                                                                                                                       | Deliverable                                                            |
| ----- | -------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| 1     | Deploy Sliver or Mythic C2, generate payloads, and establish callbacks in your lab                                         | C2 deployment guide with listener/payload configuration                |
| 2     | Build a redirector infrastructure (cloud VM + domain + HTTPS + mod_rewrite)                                                | Infrastructure diagram + setup documentation                           |
| 3     | Execute a full red team campaign against your AD lab — initial access, persistence, lateral movement, objective completion | Campaign report with timeline, detection analysis, and recommendations |

> [!IMPORTANT]
> **Move-On Gate (Part 40):** You can plan a red team campaign, deploy C2 infrastructure with redirectors, execute a full attack lifecycle with OPSEC discipline, and produce a campaign report that analyzes detection gaps.

---

<a id="toc-part-41-proof-of-work--career-portfolio"></a>
<a id="part-41-proof-of-work-career-portfolio"></a>


---

<a id="module-30-proof-of-work--career-portfolio"></a>
<a id="part-41-proof-of-work-career-portfolio"></a>

## Module 30: Proof of Work & Career Portfolio


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🟡 `cyber security interview questions` — Reference — preparation for technical interviews
> - 🟡 `Cybersecurity First Principles A Reboot of Strategy and Tactics` — Reference — strategic framing for senior-level interviews and portfolio positioning
> - 🟢 `The Threat Detection Report 2023` — Reference — current threat landscape context for interview discussions


> **Core Principle:** Theory without evidence is worthless. Every technical skill in this roadmap must be validated through _unfakeable_ proof of work — tools you've built, reports you've written, certifications you've earned, and bugs you've found. This section ties it all together.

<a id="stage-1-certification-roadmap"></a>

### **Stage 1: Certification Roadmap** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Validate skills through industry-recognized, hands-on certifications.

**Offensive Security Certifications (Hands-On Priority):**

- [ ] **OSCP (Offensive Security Certified Professional):** The **gold standard** for penetration testing. Complete the **PEN-200 course** and pass the **24-hour practical exam** — demonstrates you can hack real machines, not just answer multiple-choice questions.

- [ ] **OSWE (Offensive Security Web Expert):** Earn the **WEB-300 certification** for advanced **white-box web application exploitation** — source code review, custom exploit development, authentication bypass.

- [ ] **OSED (Offensive Security Exploit Developer):** Earn the **EXP-301 certification** for **Windows userland exploitation** — buffer overflows, DEP/ASLR bypass, shellcode development, ROP chains.

- [ ] **OSEP (Offensive Security Experienced Penetration Tester):** Earn the **PEN-300 certification** for **advanced evasion techniques** — AMSI bypass, process injection, lateral movement in hardened environments.

**Application Security Certifications:**

- [ ] **BSCP (Burp Suite Certified Practitioner):** Complete **PortSwigger Web Security Academy** labs and pass the **practical exam** — validates OWASP Top 10 exploitation, JWT attacks, SSRF, deserialization, and advanced web hacking skills.

- [ ] **CWEE (Certified Web Exploitation Expert):** HTB's certification focused on **advanced web exploitation** — SQL injection, template injection, file upload attacks, deserialization chains.

**AI Security Certifications (Emerging):**

- [ ] **COAE (Certified Offensive AI Expert):** Earn Hack The Box's **AI security certification** covering **LLM exploitation, prompt injection, RAG poisoning, AI red teaming methodology**.

- [ ] **OSAI (OffSec AI-300):** Complete OffSec's **AI security certification** for **offensive AI testing** — validate ability to test and attack AI/ML systems in enterprise environments.

- [ ] **Google AI Essentials / DeepLearning.AI Specialization:** Complete foundational AI courses to validate **understanding of model architecture, training pipelines, and ML math** before specializing in AI security.

**Blue Team & Cloud Certifications:**

- [ ] **BTL1 (Blue Team Level 1):** Validate **SOC analyst skills** — log analysis, SIEM usage, incident response, threat detection.

- [ ] **CCD (Certified CyberDefender):** CyberDefenders certification for **DFIR and threat hunting** — memory forensics, malware analysis, log analysis.

- [ ] **AWS SAA / Azure AZ-500 / GCP Security:** Earn **cloud security certifications** to validate **IAM, networking, compliance, and cloud-native security** skills.

---

<a id="stage-2-technical-portfolio-github-presence"></a>

### **Stage 2: Technical Portfolio & GitHub Presence** — `🔬 Practical`

> [!TIP]
> **Goal:** Build a public portfolio that proves you can build, not just study.

- [ ] **GitHub Repository Strategy:** Maintain a **clean, professional GitHub profile** with **2–5 significant security projects** — each with **README, architecture diagrams, usage examples, and documented attack scenarios**.

- [ ] **Clean Commit History:** Practice **atomic commits with descriptive messages** — hiring managers and security teams review your commit history to assess engineering discipline.

- [ ] **Project Categories:** Build projects across multiple domains to demonstrate breadth:
  - **Offensive tool** (custom scanner, exploit framework, payload generator)
  - **Defensive tool** (log analyzer, detection rule generator, YARA rule suite)
  - **AI security tool** (prompt injection tester, LLM red team framework, RAG poisoning PoC)
  - **Automation** (recon pipeline, report generator, CI/CD security scanner)

- [ ] **Documentation Quality:** Every project must include: **installation instructions, usage examples, architecture overview, limitations, and license**. Poor documentation kills credibility.

- [ ] **Contribution to Open Source:** Contribute to **established security tools** (Impacket, BloodHound, Garak, PyRIT, Nuclei, OWASP projects) — demonstrates ability to work with existing codebases, not just greenfield projects.

---

<a id="stage-3-technical-writing-content"></a>

### **Stage 3: Technical Writing & Content** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Demonstrate depth of understanding through published analysis.

- [ ] **Technical Blog Posts (Medium / Personal Site):** Write **5–10 substantive, technical breakdowns** of your security research — document **methodology, failures, findings, and remediation guidance** in long-form posts targeting both practitioners and hiring managers.

- [ ] **CTF Writeups:** Publish **detailed writeups for solved CTF challenges** — explain the thought process, dead ends, and eventual solution with code snippets and screenshots.

- [ ] **Vulnerability Disclosures:** Document any **responsibly disclosed vulnerabilities** with **CVE identifiers, impact analysis, and timeline** — these are the most credible proof of offensive capability.

- [ ] **Cheat Sheets & Reference Guides:** Create **condensed reference materials** (OSCP cheat sheet, AD attack playbook, API pentesting checklist) — demonstrates synthesis of complex knowledge and helps the community.

- [ ] **LinkedIn Technical Content:** Post **regular technical insights, tool reviews, and industry commentary** — LinkedIn is the primary hiring platform for security roles; build a professional narrative.

---

<a id="stage-4-bug-bounties-community-engagement"></a>

### **Stage 4: Bug Bounties & Community Engagement** — `🔬 Practical`

> [!TIP]
> **Goal:** Validate offensive skills against real-world targets and build reputation.

- [ ] **Bug Bounty Platforms:** Maintain active profiles on **HackerOne, Bugcrowd, Synack, Intigriti, Immunefi (Web3)** — prioritize programs in your specialization (web, API, cloud, AI).

- [ ] **First 10 Valid Findings:** Target **low-hanging fruit first** (open redirects, IDOR, info disclosure) to build platform reputation, then escalate to **critical-severity findings**.

- [ ] **Hall of Fame & Acknowledgments:** Collect **public acknowledgments** from bug bounty programs — these serve as third-party validation of your skills on your resume.

- [ ] **CTF Competitions:** Compete regularly in **picoCTF, NahamCon, HTB CTF, Google CTF, DEFCON CTF qualifiers, AI-specific CTFs (Gandalf, HackAPrompt)** — track your ranking progression.

- [ ] **Community Presentations:** Present findings at **local hacker meetups, BSides, DEFCON villages, OWASP chapter meetings** — build credibility through live demonstrations and Q&A.

- [ ] **Mentorship & Teaching:** Contribute to the community by **mentoring junior practitioners, answering StackOverflow/Reddit questions, creating educational content** — teaching deepens understanding and builds network.

---

<a id="stage-5-career-positioning-job-search-strategy"></a>

### **Stage 5: Career Positioning & Job Search Strategy** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Convert skills and proof into career opportunities.

- [ ] **Role Targeting:** Identify specific roles matching your skill profile:
  - **Offensive:** Penetration Tester, Red Team Operator, Exploit Developer, Bug Bounty Hunter
  - **Defensive:** SOC Analyst, Detection Engineer, Incident Responder, Threat Hunter
  - **AppSec:** Application Security Engineer, Security Code Reviewer, DevSecOps Engineer
  - **AI Security:** LLM Red Teamer, AI Safety Engineer, ML Security Researcher, Prompt Security Engineer
  - **Cloud:** Cloud Security Architect, Cloud Pentester, IAM Security Engineer

- [ ] **Resume Engineering:** Structure your resume around **impact and capability delivered** — not just technologies listed. Quantify results: _"Discovered 47 vulnerabilities across 12 bug bounty programs; built automated recon pipeline reducing initial assessment time by 60%."_

- [ ] **Portfolio Coherence:** Ensure your **GitHub, blog, LinkedIn, bug bounty profiles, and certifications** tell a **coherent, unified story** — each project links to a writeup, each writeup links to working code, each certification validates the skills demonstrated in projects.

- [ ] **Interview Preparation:** Practice **technical interviews** covering **live hacking demonstrations, CTF-style challenges, architecture review, threat modeling exercises**, and **behavioral questions** about incident handling and team collaboration.

- [ ] **Continuous Skill Maintenance:** Security is a **continuous learning field** — maintain certifications (OSCP requires CPEs), continue bug bounty hunting, publish new research, attend conferences, and stay current with emerging threats and tools.

---

<a id="stage-5b-technical-interview-preparation"></a>

### **Stage 5B: Technical Interview Preparation** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Convert technical competence into hired. Hiring managers are skilled at identifying candidates who know tools but cannot think under pressure. Stage 5B closes the gap between "I can do this in a lab" and "I can demonstrate this in 45 minutes with someone watching."

- [ ] **Security System Design Questions:** Practice designing secure systems from scratch under time pressure. Common prompts: "Design a secure authentication system for 10 million users," "How would you architect a zero-trust access control system for a hybrid cloud environment?", "Design the logging and alerting infrastructure for a 500-person company." Practice on a whiteboard or draw.io. Structure your answer: **requirements → threat model → component design → data flow → control gaps → trade-offs**. Never jump to components before stating requirements.

- [ ] **Live Hacking / CTF Demonstrations:** Some interviews include live exploitation challenges. Practice solving HTB/THM boxes verbally as you work — narrate your reasoning out loud. Interviewers are evaluating _how you think_, not just whether you solve it. Practice: "I notice port 8080 is open with a Tomcat banner. My first step is to check for the default manager credentials because default deployments are common in enterprise environments..."

- [ ] **Behavioral Question Framing (STAR Method):** Prepare answers using **Situation → Task → Action → Result** for common security behavioral questions:
  - _"Tell me about a critical vulnerability you found."_ → Describe the finding, what you had to figure out, the steps you took, the impact if exploited, and how it was remediated.
  - _"Describe a time you disagreed with a security decision."_ → Frame as professional disagreement, evidence-based argument, outcome respected regardless of decision made.
  - _"Tell me about a time you worked with a team under a tight incident deadline."_ → Show decision-making under pressure, communication to leadership, and what you learned.

- [ ] **Technical Depth Calibration:** Know what you know deeply vs. broadly. In an interview, say "I've worked with X and understand it at depth level Y" rather than claiming expertise across everything. Interviewers who probe your claimed expertise and find a shallow answer will rank you below candidates who admitted the gap honestly. Integrity beats bluffing.

- [ ] **Mock Interviews:** Conduct at minimum **2 full mock interviews** with a peer, mentor, or community member before applying. Use real job descriptions to set the scenario. Record yourself and review: Did you fill silence with confident reasoning or nervous filler? Did you structure answers or ramble? Did you ask clarifying questions or make assumptions?

- [ ] **Platform Prep:**
  - **Coding challenges:** LeetCode or HackerRank — solve 10–15 medium-level Python problems focused on string manipulation, data structures, and file parsing (common in security scripting tests).
  - **System design prep:** "System Design Interview" by Alex Xu (Chapters 1, 5, 10) for the patterns; apply security overlays from your own knowledge.
  - **Behavioral prep:** "The STAR Interview" by Misha Yurchenko for structure; adapt examples from your own pentest/CTF/bug bounty work.

<a id="stage-6-soft-skills-professional-communication"></a>
### **Stage 6: Soft Skills & Professional Communication** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Bridge the gap between technical skill and professional impact. These skills separate mid-level practitioners from senior leaders.


- [ ] **Executive Summary Writing:** For every lab report and pentest deliverable, write a **1-page executive summary** that a non-technical CFO or CISO could understand. Practice: take your most technical finding and explain the **business impact, risk level, and recommended action** without using jargon.

- [ ] **Stakeholder Presentation:** Practice **presenting findings to hostile audiences** — developers who disagree with your findings, managers who don't want to fund remediation, and executives who want a one-sentence answer. Build a **5-slide template**: (1) What we tested, (2) What we found, (3) What could happen, (4) What to fix, (5) What it costs.

- [ ] **Delivering Bad News:** Practice communicating **critical findings** under pressure — a zero-day in production, a breach in progress, or a failed compliance audit. Structure: **impact first, evidence second, recommendation third, timeline fourth**. Never bury the lede.

- [ ] **Handling Pushback:** Prepare for common objections: _"That's not exploitable in our environment," "We accept the risk," "This is a false positive," "We don't have budget."_ Build a **response playbook** for each: acknowledge the concern, present evidence, propose alternatives, document the risk acceptance decision.

- [ ] **Scope & Expectation Management:** Practice **negotiating engagement scope** — what's in, what's out, what changes require re-scoping. Document scope creep conversations. Know when to say _"This is out of scope but here's what I observed"_ vs _"This requires a scope change and additional time."_

- [ ] **Team Collaboration:** Practice **SOC shift handoffs, red team debrief sessions, security review feedback, and cross-functional incident response coordination**. Write **clear, actionable handoff notes** that another analyst can act on immediately. Learn to give and receive code review feedback without ego.

- [ ] **Written Communication Drill:** For every 3 lab reports you produce, rewrite the executive summary **three times**: once for a CISO (business risk), once for a development team lead (technical remediation), and once for a compliance officer (regulatory impact). Same finding, three audiences, three completely different summaries.

---

### **Lab Progression (Part 41: Career Portfolio)**

| Level | Task                                                                                                         | Deliverable                                                |
| ----- | ------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------- |
| 1     | Write 3 pentest reports with executive summaries tailored for CISO, engineering lead, and compliance officer | Reports with 3 audience-specific executive summaries       |
| 2     | Build GitHub portfolio with 2–5 security tools and publish 5+ technical blog posts                           | Live GitHub + blog with cross-linked content               |
| 3     | Submit 5 valid bug bounty findings and present at a local meetup or BSides                                   | Bug bounty acknowledgments + presentation slides/recording |

> [!IMPORTANT]
> **Move-On Gate (Part 41):** Produce one pentest report with three executive summaries (CISO, engineering lead, compliance officer) for the same set of findings, and have a live portfolio with working tools, published writeups, and at least one industry-recognized certification.

---

### 🏆 Phase 10 Capstone Project

**Compile Your Complete Portfolio and Present Your Professional Identity**

- [ ] **Curate your GitHub portfolio** — 2–5 security tools/projects with professional READMEs, architecture diagrams, and demo recordings
- [ ] **Publish 5+ technical blog posts** — each linked to a project or lab from a previous phase
- [ ] **Select 3 capstone highlights** from Phases 1–9 as your strongest portfolio pieces
- [ ] **Build a unified professional presence** — GitHub + blog + LinkedIn + bug bounty profiles tell one coherent story
- [ ] **Write 3 executive summaries** for your best pentest report (CISO, engineering lead, compliance officer versions)

**Deliverables:**

- [ ] Live GitHub portfolio with pinned projects
- [ ] Published blog/Medium with 5+ posts
- [ ] Professional resume quantifying impact
- [ ] 3 capstone pieces polished to presentation quality
- [ ] All documentation committed and organized in your Git repository

> [!IMPORTANT]
> **Capstone Gate:** A hiring manager should be able to review your GitHub, blog, and resume and understand your capabilities without a single conversation. Your portfolio must tell a coherent story of progressive skill development.

---

### 🧭 Phase 10 Reflection & Competency Check

- [ ] **Reflection:** What story does your portfolio tell about your strongest security direction?
- [ ] **Reflection:** Which older artifacts should remain private, be rewritten, or be removed because they no longer represent your current standard?
- [ ] **Competency:** Can a reviewer understand your skills from your public work without extra explanation?
- [ ] **Competency:** Can you present the same technical project to a recruiter, engineer, manager, and security lead?
- [ ] **Competency:** Can you maintain a realistic learning plan for the next 6 months after completing the roadmap?

> [!IMPORTANT]
> **Roadmap Completion Gate:** You are done when your portfolio is coherent, current, ethically publishable, and aligned with the roles you are applying for.

---

---

<a id="tool-priority-reference"></a>

## 🛠️ Tool Priority Reference

> **How to Use This Section:** This is your master toolkit map — 38 tools, ordered by priority across 4 tiers. Tiers are about **frequency of use in real engagements**, not difficulty. A Tier 1 tool is on your screen in every lab and engagement. A Tier 4 tool is situational and domain-specific.
>
> Every tool has a dedicated mastery checklist in the `Tools/` directory. Study them in priority order. Don't go deep on Ghidra before you're fluent with Nmap.

---

### 🔴 Tier 1 — Core Pentest Essentials

*14 tools. You will use these on nearly every lab, CTF, and engagement. OSCP requires most of them. Master all 14 before moving to Tier 2.*

| # | Tool | Domain | Signature Use Case |
|:-:|:-----|:-------|:-------------------|
| 1 | [🗺️ Nmap](Tools/Nmap.md) | Recon & Scanning | First tool on every engagement. Host discovery, port scan, service/version fingerprinting. |
| 2 | [🔌 Netcat](Tools/Netcat.md) | Networking / Shells | Reverse shells, bind shells, banner grabbing, port forwarding. The duct tape of pentesting. |
| 3 | [🕷️ Burp Suite](Tools/Burp_Suite.md) | Web App Testing | The #1 tool for manual web app testing. Proxy, Repeater, Intruder, active scanner. |
| 4 | [💀 Metasploit Framework](Tools/Metasploit_Framework.md) | Exploitation | CVE exploitation, auxiliary modules, Meterpreter post-exploitation. OSCP-standard. |
| 5 | [💨 ffuf](Tools/ffuf.md) | Web Fuzzing | High-speed content discovery — directories, parameters, vhosts. Fastest fuzzer available. |
| 6 | [🔍 Gobuster](Tools/Gobuster.md) | Web Fuzzing | DNS subdomain, directory, and vhost brute-force. Simpler syntax than ffuf for quick runs. |
| 7 | [🐲 LinPEAS](Tools/LinPEAS.md) | Post-Exploitation / Linux | Linux privesc enumeration. Run the moment you get a Linux shell. |
| 8 | [🪟 WinPEAS](Tools/WinPEAS.md) | Post-Exploitation / Windows | Windows privesc enumeration. Run the moment you get a Windows shell. |
| 9 | [🔨 Hydra](Tools/Hydra.md) | Credential Attacks | Multi-protocol brute-force — SSH, FTP, HTTP, RDP, SMB, WinRM. |
| 10 | [#️⃣ Hashcat](Tools/Hashcat.md) | Password Cracking | GPU-accelerated hash cracking. Go-to for large wordlists and rule-based attacks. |
| 11 | [🔑 John the Ripper](Tools/John_the_Ripper.md) | Password Cracking | Format-auto-detecting hash cracker. Best for shadow files, ZIP, SSH keys, rare formats. |
| 12 | [💉 sqlmap](Tools/sqlmap.md) | Web App Testing | Automated SQL injection detection and exploitation. Run after Burp confirms the endpoint. |
| 13 | [📣 Responder](Tools/Responder.md) | Sniffing & Spoofing | LLMNR/NBT-NS/mDNS poisoning. Passive NTLMv2 hash capture on Windows networks. |
| 14 | [📡 tcpdump](Tools/tcpdump.md) | Packet Capture | Headless CLI packet capture. Use on servers and pivots where Wireshark is unavailable. |

> [!IMPORTANT]
> **Gate:** Every one of these 14 tools must be muscle memory before starting Tier 2. Tools 1–8 appear on the OSCP exam. Tools 9–14 appear in virtually every AD and web lab.

---

### 🔶 Tier 2 — Important, Frequent Use

*12 tools. Critical for Active Directory attacks, network analysis, red teaming, and web specialization. You will use these in most serious engagements — just not on every single target like Tier 1.*

| # | Tool | Domain | Signature Use Case |
|:-:|:-----|:-------|:-------------------|
| 15 | [🐍 Impacket](Tools/Impacket.md) | Active Directory | Python suite for SMB, Kerberos, DCOM. `secretsdump`, `psexec`, `ntlmrelayx`, `GetUserSPNs`. |
| 16 | [🩸 BloodHound](Tools/BloodHound.md) | Active Directory | AD attack path visualization. Shortest path to Domain Admin from your current position. |
| 17 | [🕸️ NetExec (nxc)](Tools/NetExec.md) | Active Directory / Red Team | SMB enumeration, password spraying, lateral movement, BloodHound collection. Successor to CrackMapExec. |
| 18 | [🦈 Wireshark](Tools/Wireshark.md) | Packet Analysis | GUI deep-packet inspection. Protocol analysis, CTF pcap challenges, credential extraction. |
| 19 | [🌐 Nikto](Tools/Nikto.md) | Web App Testing | Fast automated web server scanner. Finds misconfigs, outdated software, dangerous files. |
| 20 | [🔴 wpscan](Tools/wpscan.md) | Web App Testing | WordPress enumeration — plugins, themes, users, CVEs. Mandatory on any WordPress target. |
| 21 | [🌾 theHarvester](Tools/theHarvester.md) | OSINT / Recon | Passive email, subdomain, and IP harvest from search engines and threat intel APIs. |
| 22 | [🔭 Recon-ng](Tools/Recon-ng.md) | OSINT / Recon | Structured, database-backed OSINT framework with module chaining and report generation. |
| 23 | [🔀 Ligolo-ng](Tools/Ligolo-ng.md) | Red Team / Pivoting | TUN interface pivoting — full network access through a compromised host. No proxychains needed. |
| 24 | [🗡️ Sliver](Tools/Sliver.md) | Red Team / C2 | Open-source C2. Persistent implants, beacons, mTLS/HTTPS/DNS protocols, multi-operator. |
| 25 | [🛡️ OWASP ZAP](Tools/OWASP_ZAP.md) | Web App Testing | Free active scanner + AJAX spider. Best Burp Suite Community alternative and CI/CD integration. |
| 26 | [🐝 Bettercap](Tools/Bettercap.md) | Sniffing & Spoofing | ARP/DNS poisoning, MITM, credential sniffing, Wi-Fi deauth and handshake capture. |

> [!TIP]
> **Tier 2 study path:** AD cluster first (Impacket → BloodHound → NetExec). Network (Wireshark → Bettercap). Web specialization (Nikto → wpscan → OWASP ZAP). Red team (Ligolo-ng → Sliver). OSINT (theHarvester → Recon-ng) runs in parallel.

---

### 🔷 Tier 3 — Specialized / Situational

*12 tools. Essential within their specific domain, but not universally needed. Pick the sub-group that matches your track.*

| # | Tool | Domain | When You Need It |
|:-:|:-----|:-------|:-----------------|
| 27 | [🐍 Scapy](Tools/Scapy.md) | Packet Crafting | Craft any custom packet in Python. Build scanners, ARP poisoners, protocol fuzzers from scratch. |
| 28 | [🐉 Ghidra](Tools/Ghidra.md) | Malware Analysis / RE | Static binary reverse engineering. NSA's free IDA Pro alternative — disassembly, decompiler, scripting. |
| 29 | [🔑 jwt_tool](Tools/jwt-tool.md) | Web / API Testing | JWT attack suite — `alg:none`, RS256→HS256 confusion, weak secret brute-force, `kid` injection. |
| 30 | 📮 Postman | Web / API Testing | Manual REST API testing. Build, replay, and document API requests; manage auth flows. |
| 31 | 🐙 Ettercap | Sniffing & Spoofing | Legacy MITM tool. Understand it for older environments; use Bettercap for modern labs. |
| 32 | 🦶 SpiderFoot | OSINT | Automated OSINT with relationship graph. More automated than Recon-ng with less manual control. |
| 33 | 🕵️ Maltego | OSINT | Visual intelligence mapping. Turns raw OSINT data into an interactive relationship graph. |
| 34 | 🎣 GoPhish | Social Engineering | Phishing campaign framework — manages email sending, landing pages, and click/credential tracking. |
| 35 | 🎭 Social-Engineer Toolkit (SET) | Social Engineering | Credential harvesting sites, malicious payload delivery, spear-phishing, phone phishing vectors. |
| 36 | 🔬 x64dbg | Malware Analysis | Dynamic analysis on Windows — live debugging, API call tracing, memory breakpoints. |
| 37 | 🖼️ PEStudio | Malware Analysis | Static PE triage — imports, strings, entropy, VirusTotal score. First tool opened on any sample. |

> [!NOTE]
> **Study Tier 3 by track:** Malware analyst → PEStudio → Ghidra → x64dbg. Web/API tester → jwt_tool → Postman. OSINT investigator → SpiderFoot → Maltego. Social engineer → GoPhish → SET. Scapy is cross-track.

---

### 🔹 Tier 4 — Niche / Concept-Focused

*11 tools. Know what each does and when to call for it. Deep practice is optional unless DoS testing or low-level malware analysis is your specific role.*

| # | Tool | Domain | What It Does |
|:-:|:-----|:-------|:-------------|
| 28 | 🧬 Detect It Easy (DiE) | Malware Analysis | PE packer and compiler identification. First step before attempting to unpack a binary. |
| 30 | 👁️ Procmon | Malware Analysis | Windows process activity monitor — real-time file, registry, and network event capture during execution. |
| 31 | 🧵 strings | Malware Analysis | Extract all printable strings from a binary. Fastest first-pass indicator extraction before Ghidra. |
| 32 | 🧼 SoapUI | API Testing | SOAP/WSDL web service testing. Use for legacy XML-based enterprise APIs. |
| 33 | 🍪 Cookie-Editor | Session Hijacking | Browser extension for viewing, modifying, and importing session cookies during web testing. |
| 34 | 🦥 Slowloris | DoS Testing | HTTP slow-connection DoS. Tests whether a server is vulnerable to partial-request socket exhaustion. |
| 35 | 💛 GoldenEye | DoS Testing | HTTP Layer 7 DoS tool. Use for demonstrating DoS concepts in isolated lab environments. |
| 36 | ⚖️ ApacheBench (ab) | Performance / DoS | HTTP benchmarking. Understand server throughput and concurrency before a load test. |
| 37 | 🔧 wrk | Performance / DoS | Modern sustained HTTP load tester. More realistic than ApacheBench for high-concurrency scenarios. |
| 38 | 📶 iperf3 | Network Performance | Raw TCP/UDP bandwidth measurement between two hosts. Validates lab network capacity. |

> [!NOTE]
> **Tier 4 is conceptual.** You should be able to explain what each tool does and run a basic test — that's it. You do not need to master these to be a working penetration tester.

---

### 📐 Tool Selection Decision Tree

```
WHAT DO YOU NEED TO DO?
│
├─ Discover hosts / open ports
│   └─ Nmap (always first)
│
├─ Enumerate web content
│   ├─ Fast fuzzing → ffuf
│   └─ Simple run → Gobuster
│
├─ Test a web application
│   ├─ Manual testing → Burp Suite
│   ├─ Automated scan → OWASP ZAP
│   ├─ Quick misconfiguration check → Nikto
│   └─ WordPress target → wpscan
│
├─ Exploit a vulnerability
│   ├─ Known CVE with a module → Metasploit
│   ├─ SQL injection → sqlmap
│   └─ JWT weakness → jwt_tool
│
├─ Crack a password / hash
│   ├─ GPU available, large wordlist → Hashcat
│   └─ Unknown format, quick detection → John the Ripper
│
├─ Brute-force a login
│   └─ Hydra (SSH, FTP, RDP, HTTP, SMB, WinRM)
│
├─ Active Directory
│   ├─ Enumerate / spray credentials → NetExec
│   ├─ Visualize attack paths → BloodHound
│   ├─ Hash dumping / PTH / relay → Impacket (secretsdump, ntlmrelayx)
│   ├─ Kerberoasting / AS-REP → Impacket + NetExec
│   └─ NTLM hash capture (passive) → Responder
│
├─ Pivot to an internal network
│   ├─ Need full tool support (Nmap SYN, ICMP) → Ligolo-ng
│   └─ SOCKS proxy is enough → SSH -D or Chisel
│
├─ Post-exploitation
│   ├─ Linux → LinPEAS
│   └─ Windows → WinPEAS
│
├─ Capture or analyze network traffic
│   ├─ GUI, deep inspection → Wireshark
│   └─ Headless / pivot host → tcpdump
│
├─ MITM attack on a LAN
│   └─ Bettercap (ARP poison + sniff + DNS spoof)
│
├─ OSINT on a target
│   ├─ Quick automated sweep → theHarvester
│   └─ Structured investigation + reporting → Recon-ng
│
├─ Persistent red team access
│   └─ Sliver (C2 beacons, mTLS, multi-operator)
│
├─ Analyze a malware sample
│   ├─ First-pass static → PEStudio → strings
│   └─ Deep reverse engineering → Ghidra (static) + x64dbg (dynamic)
│
├─ Phishing campaign
│   └─ GoPhish (tracking + reporting) + SET (harvester pages)
│
└─ Build a custom network tool or packet
    └─ Scapy
```

---

### 🗓️ Suggested Study Order

*Start from Block 1. Complete each block before moving to the next.*

| Block | Weeks | Tools | Focus |
|:-----:|:-----:|:------|:------|
| 1 | 1–2 | Nmap · Netcat · tcpdump | Networking fundamentals — understand the infrastructure before attacking it |
| 2 | 3–4 | Burp Suite · ffuf · Gobuster · Nikto | Web recon and manual testing baseline |
| 3 | 5–6 | Hydra · Hashcat · John the Ripper · sqlmap | Credential attacks and web exploitation |
| 4 | 7–8 | Metasploit · LinPEAS · WinPEAS | Exploitation and post-exploitation flow |
| 5 | 9–10 | NetExec · Responder · Impacket · BloodHound | Full Active Directory attack chain |
| 6 | 11–12 | Wireshark · Bettercap · Scapy | Network analysis and MITM attacks |
| 7 | 13–14 | wpscan · OWASP ZAP · jwt_tool · Postman | Web and API specialization |
| 8 | 15–16 | theHarvester · Recon-ng | OSINT and passive reconnaissance |
| 9 | 17–18 | Ligolo-ng · Sliver | Pivoting and red team C2 |
| 10 | 19–22 | GoPhish · SET · SpiderFoot · Maltego | Social engineering and advanced OSINT |
| 11 | 23–26 | Ghidra · x64dbg · PEStudio · strings · DiE · Procmon | Malware analysis track (skip if not your focus) |
| 12 | 27+ | Tier 4 tools as needed | Situational — study when a lab or role specifically requires them |

---


---

<a id="final-gate"></a>

## 🏁 Final Gate — Mastery & Career Validation

> [!IMPORTANT]
> **Mastery Capstone Exit Gate:**
> - Deploy a custom C2 implant and redirector infrastructure in an isolated testing environment.
> - Publish original research, a detailed tool, or an AI jailbreak / red-teaming assessment report.
> - 3+ comprehensive professional penetration testing / red team engagement reports in Git portfolio.
> - OSCP / CRTO / practical offensive certification attained.
