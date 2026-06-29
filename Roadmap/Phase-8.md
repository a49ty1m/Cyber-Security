# Phase 8: Governance, Supply Chain, DevSecOps & Architecture

---

### 🧭 Navigation
◀ [Phase 7](Phase-7.md) | 🏠 [Master Roadmap](README.md) | [Phase 9](Phase-9.md) ➔

---

> [!NOTE]
> **Phase Overview**
> - **⏱️ Time Commitment (Full-Time):** 1–2 months
> - **⏱️ Time Commitment (Part-Time):** 2–4 months
> - **🎯 Primary Focus:** GRC frameworks (NIST, ISO 27001, PCI-DSS, DPDP Act), supply chain security (SBOM, SLSA, dependency confusion), DevSecOps integration (SAST/DAST/SCA, secrets scanning, IaC security), and security architecture & engineering (Zero Trust, defense-in-depth design, segmentation, reference architectures).

---

### 🗂️ Table of Contents
- [Part 35: Governance, Risk & Compliance (GRC)](#part-35-governance-risk-compliance-grc)
  - [Stage 1: Security Frameworks & Standards](#stage-1-security-frameworks-standards)
  - [Stage 2: Industry Regulations & Legal Requirements](#stage-2-industry-regulations-legal-requirements)
  - [Stage 3: Risk Management & Assessment](#stage-3-risk-management-assessment)
  - [Stage 4: Audit, Scope & Compliance Testing](#stage-4-audit-scope-compliance-testing)
  - [Lab Progression](#lab-progression)
- [Part 36: Supply Chain Security](#part-36-supply-chain-security)
  - [Stage 1: Understanding the Attack Surface](#stage-1-understanding-the-attack-surface)
  - [Stage 2: Dependency & Package Attacks](#stage-2-dependency-package-attacks)
  - [Stage 3: Build System & CI/CD Attacks](#stage-3-build-system-cicd-attacks)
  - [Stage 4: Open-Source & Third-Party Risk](#stage-4-open-source-third-party-risk)
  - [Stage 5: Defense & Verification](#stage-5-defense-verification)
- [Part 37: DevSecOps & Secure SDLC](#part-37-devsecops-secure-sdlc)
  - [Stage 1: Security in the Development Lifecycle](#stage-1-security-in-the-development-lifecycle)
  - [Stage 2: Static Analysis (SAST)](#stage-2-static-analysis-sast)
  - [Stage 3: Dynamic Analysis (DAST & IAST)](#stage-3-dynamic-analysis-dast-iast)
  - [Stage 4: Software Composition Analysis (SCA)](#stage-4-software-composition-analysis-sca)
  - [Stage 5: Secrets Detection & Pipeline Security](#stage-5-secrets-detection-pipeline-security)
  - [Secure Coding & Pipeline Lab Progression](#secure-coding-pipeline-lab-progression)
- [Part 43: Security Architecture & Engineering](#part-43-security-architecture-engineering)
  - [Stage 1: Security Design Principles](#stage-1-security-design-principles)
  - [Stage 2: Zero Trust Architecture](#stage-2-zero-trust-architecture)
  - [Stage 3: Network Security Architecture](#stage-3-network-security-architecture)
  - [Stage 4: Data Security Architecture](#stage-4-data-security-architecture)
  - [Stage 5: Disaster Recovery & Business Continuity](#stage-5-disaster-recovery-business-continuity)
  - [Lab Progression](#lab-progression)

---

## Part 35: Governance, Risk & Compliance (GRC)

### **Stage 1: Security Frameworks & Standards**

> [!TIP]
> **Goal:** : Understand the regulatory and standards landscape that defines what pentesters test against.

- [ ] **NIST Cybersecurity Framework (CSF):** Master the **5 functions (Identify, Protect, Detect, Respond, Recover)** and how they map to security controls.

- [ ] **NIST 800-53 / 800-171:** Understand **security control families** (Access Control, Audit, Incident Response) used in **federal and defense** compliance.

- [ ] **ISO 27001/27002:** Know the **ISMS (Information Security Management System)** framework, **Annex A controls**, and **certification audit process**.

- [ ] **CIS Controls (v8):** Master the **18 Critical Security Controls** as a prioritized, actionable defense checklist; understand **Implementation Groups (IG1-IG3)**.

- [ ] **MITRE ATT&CK as Compliance:** Use **ATT&CK coverage mapping** to demonstrate detection maturity against specific adversary techniques.

---

### **Stage 2: Industry Regulations & Legal Requirements**

> [!TIP]
> **Goal:** : Know the laws and regulations that dictate security requirements across industries.

- [ ] **PCI-DSS (Payment Card Industry):** Understand the **12 requirements** for protecting cardholder data; know **scope reduction (network segmentation), SAQ types**, and how pentesters validate Requirement 11.3.

- [ ] **HIPAA (Healthcare):** Understand **PHI (Protected Health Information)** safeguards, **technical/administrative/physical** controls, and **breach notification requirements**.

- [ ] **GDPR (EU Data Protection):** Know **data subject rights, lawful basis for processing, Data Protection Impact Assessments (DPIA), breach notification (72-hour rule)**, and **extraterritorial scope**.

- [ ] **SOC 2 (Service Organizations):** Understand **Trust Services Criteria (Security, Availability, Processing Integrity, Confidentiality, Privacy)** and how pentest findings map to SOC 2 reports.

- [ ] **SOX (Sarbanes-Oxley):** Know **IT General Controls (ITGCs)** for financial system integrity — **access control, change management, backup/recovery**.

- [ ] **DPDP Act (India):** Understand **India's Digital Personal Data Protection Act** — consent-based processing, Data Fiduciary obligations, cross-border transfer rules, and **Board penalties**.

- [ ] **Computer Fraud & Abuse Act (CFAA):** Understand US federal law on **unauthorized access**; know how **scope of engagement** and **written authorization** protect pentesters legally.

---

### **Stage 3: Risk Management & Assessment**

> [!TIP]
> **Goal:** : Quantify and communicate risk so findings drive action.

- [ ] **Risk Equation:** Master **Risk = Threat × Vulnerability × Impact** and use it to **prioritize findings** over raw CVSS scores.

- [ ] **Risk Assessment Methodologies:** Understand **NIST 800-30 (qualitative), FAIR (quantitative), OCTAVE, CRAMM** for structured risk evaluation.

- [ ] **Threat Modeling:** Apply **STRIDE, PASTA, Attack Trees** to proactively identify **threats to systems before testing** and guide scope selection.

- [ ] **Business Impact Analysis (BIA):** Map **technical vulnerabilities to business consequences** — revenue loss, reputational damage, regulatory fines, operational downtime.

- [ ] **Risk Appetite & Tolerance:** Understand how organizations define **acceptable risk levels** and how pentest recommendations must align with business context.

---

### **Stage 4: Audit, Scope & Compliance Testing**

> [!TIP]
> **Goal:** : Execute engagements that satisfy compliance requirements.

- [ ] **Scoping for Compliance:** Define pentest scope to cover **specific compliance requirements** (e.g., PCI-DSS Req 11.3 requires internal/external pentest + segmentation testing).

- [ ] **Control Validation:** Test whether **implemented controls** (MFA, encryption, logging, access controls) actually function as documented in policies.

- [ ] **Evidence Collection:** Gather **screenshots, logs, packet captures, configuration exports** formatted for **auditor review** and compliance documentation.

- [ ] **Gap Analysis Reporting:** Identify **missing controls, partial implementations, policy violations** and map them to **specific framework requirements** with remediation guidance.

- [ ] **Third-Party Risk:** Assess **vendor/supplier security posture** via **questionnaires, pentest scoping, SLA review**, and **supply chain risk evaluation**.

- [ ] **Continuous Compliance:** Understand shift from **point-in-time audits** to **continuous monitoring, automated compliance checks, and DevSecOps integration**.

---

### **Lab Progression**

> [!TIP]
> **Goal:** : Make GRC practical by producing audit-ready artifacts.

- [ ] **Risk Register Lab:** Build a risk register for your home lab or a sample SaaS system with likelihood, impact, owner, treatment, and due date.
- [ ] **Policy Lab:** Write one access-control policy and one incident-response policy with scope, roles, exceptions, and review cadence.
- [ ] **Control Mapping Lab:** Map 10 technical controls to NIST CSF, CIS Controls, or ISO 27001 Annex A.
- [ ] **Vendor Risk Lab:** Create a lightweight vendor security questionnaire and score a fictional third-party service.
- [ ] **Business Continuity Lab:** Write a basic BIA and recovery priority list for a sample business process.
> [!IMPORTANT]
> **Move-On Gate:** Produce an audit evidence pack with policy, risk register, control mapping, and remediation plan.

<a id="toc-part-36-supply-chain-security"></a>
## Part 36: Supply Chain Security

### **Stage 1: Understanding the Attack Surface**

> [!TIP]
> **Goal:** : Map how software and hardware dependencies become attack vectors.

- [ ] **Supply Chain Threat Model:** Understand the **three attack vectors**: compromised **source code** (SolarWinds), compromised **build/distribution** (XZ Utils backdoor), and compromised **dependencies** (event-stream npm).

- [ ] **SBOM (Software Bill of Materials):** Generate and analyze **SBOM (CycloneDX, SPDX format)** to inventory all third-party components, transitive dependencies, and their known CVEs.

- [ ] **Dependency Inventory:** Map **direct + transitive dependencies** across package ecosystems (**npm, PyPI, Maven, NuGet, RubyGems**) to understand total exposed surface.

---

### **Stage 2: Dependency & Package Attacks**

> [!TIP]
> **Goal:** : Exploit weaknesses in open-source package ecosystems.

- [ ] **Dependency Confusion:** Register **public packages with the same name** as internal private packages; force targets to download your malicious version when their registry falls back to public PyPI/npm.

- [ ] **Typosquatting:** Publish packages with **names one keystroke away** from popular packages (`reqeusts`, `colourama`, `crypt0`) to catch developer typos during `pip install`.

- [ ] **Malicious Package Injection:** Study real cases (**event-stream, PyTorch-nightly, ctx**) where **legitimate packages were backdoored** post-compromise of the maintainer account.

- [ ] **Version Pinning Attacks:** Target packages using **unpinned `latest`** or **broad version ranges** (`>=1.0`); understand how **lock files (package-lock.json, Pipfile.lock)** mitigate this.

- [ ] **Protestware & Intentional Sabotage:** Understand cases where **maintainers intentionally introduced bugs/wipes** (colors.js, node-ipc) and the supply chain trust model risks this exposes.

---

### **Stage 3: Build System & CI/CD Attacks**

> [!TIP]
> **Goal:** : Compromise the pipeline that produces software.

- [ ] **Pipeline Poisoning:** Inject **malicious steps into CI/CD workflows** (GitHub Actions, Jenkins, GitLab CI) to **steal secrets, alter artifacts, plant backdoors** in compiled output.

- [ ] **Workflow Injection:** Exploit **untrusted input in GitHub Actions expressions** (`${{ github.event.pull_request.title }}`) to achieve **command injection in CI runners**.

- [ ] **Secrets Exfiltration:** Steal **CI/CD secrets (API keys, deploy tokens, signing certs)** from **environment variables, GitHub Secrets, HashiCorp Vault** during pipeline execution.

- [ ] **Artifact Tampering:** Replace **legitimate build artifacts** post-build but pre-deployment; understand **artifact signing (Sigstore/Cosign)** as a defense.

- [ ] **SLSA Framework:** Understand **Supply-chain Levels for Software Artifacts (SLSA)** maturity model (L1-L4) and what each level proves about build provenance.

---

### **Stage 4: Open-Source & Third-Party Risk**

> [!TIP]
> **Goal:** : Assess and test third-party component security.

- [ ] **OSS Vulnerability Scanning:** Use **Trivy, Grype, Snyk, OWASP Dependency-Check** to scan project dependencies for **known CVEs** and **license violations**.

- [ ] **Maintainer Account Takeover:** Understand how **compromised npm/PyPI maintainer accounts** (via credential stuffing or social engineering) enable **silent package backdooring**.

- [ ] **Repo Jacking:** Exploit **GitHub repository namespace reuse** — when a user changes their username, old repo URLs can be claimed by attackers to serve malicious packages.

- [ ] **Trojanized Tooling:** Test environments for **compromised developer tools** (malicious VS Code extensions, backdoored CLI tools, modified build systems).

---

### **Stage 5: Defense & Verification**

> [!TIP]
> **Goal:** : Know how to validate supply chain integrity.

- [ ] **Sigstore / Cosign:** Verify **container image and artifact signatures** to ensure provenance; understand **keyless signing with OIDC identity**.

- [ ] **Dependency Pinning:** Enforce **exact version pinning + hash verification** in lock files; use **Renovate/Dependabot** for automated safe updates.

- [ ] **Private Registries:** Maintain **internal package mirrors (Artifactory, Nexus)** with **allowlisting** to prevent dependency confusion attacks.

- [ ] **Code Signing:** Implement **code signing for all releases**; verify signatures in deployment pipelines before execution.

---

<a id="toc-part-37-devsecops--secure-sdlc"></a>
## Part 37: DevSecOps & Secure SDLC

### **Stage 1: Security in the Development Lifecycle**

> [!TIP]
> **Goal:** : Understand where security integrates across the SDLC.

- [ ] **SDLC Security Gates:** Map **security activities to SDLC phases** — threat modeling (design), SAST (code), SCA (build), DAST (test), pentest (pre-release), monitoring (production).

- [ ] **Shift-Left Security:** Understand the **cost and benefit model** — finding a bug in design costs 10x less than finding it in production; align testing earlier in the cycle.

- [ ] **Threat Modeling:** Apply **STRIDE to application architecture** — identify **Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege** risks before coding.

- [ ] **Secure Design Principles:** Master **least privilege, defense-in-depth, fail securely, complete mediation, open design, separation of privilege** as architectural requirements.

---

### **Stage 2: Static Analysis (SAST)**

> [!TIP]
> **Goal:** : Find vulnerabilities in source code without executing it.

- [ ] **SAST Tools:** Use **Semgrep, SonarQube, Checkmarx, Bandit (Python), Brakeman (Rails), SpotBugs (Java)** to scan source code for **injection flaws, insecure crypto, hardcoded secrets**.

- [ ] **Custom SAST Rules:** Write **Semgrep rules** to detect **organization-specific insecure patterns** (custom crypto usage, missing input validation in internal frameworks).

- [ ] **False Positive Management:** Triage SAST output — distinguish **true positives, false positives, and low-risk findings**; suppress noise without hiding real issues.

- [ ] **IDE Integration:** Understand how **security plugins (Snyk IDE, SonarLint, Semgrep VS Code)** give developers **real-time feedback** during coding.

---

### **Stage 3: Dynamic Analysis (DAST & IAST)**

> [!TIP]
> **Goal:** : Test running applications for security flaws.

- [ ] **DAST Tools:** Use **OWASP ZAP, Burp Suite Pro (automated scan), Nikto** to **black-box test** running applications for **OWASP Top 10 vulnerabilities** in CI pipelines.

- [ ] **IAST (Interactive Application Security Testing):** Understand how **IAST agents (Contrast Security, Seeker)** instrument running code to detect vulnerabilities from the inside during functional tests.

- [ ] **API DAST:** Configure **ZAP or Burp** with **OpenAPI specs** to automatically fuzz all API endpoints for **injection, auth bypass, and BOLA**.

- [ ] **Authenticated Scanning:** Configure DAST tools with **session cookies or API keys** to test **post-login functionality** inaccessible to anonymous scans.

---

### **Stage 4: Software Composition Analysis (SCA)**

> [!TIP]
> **Goal:** : Find vulnerabilities in third-party dependencies.

- [ ] **SCA Tools:** Use **Snyk, Dependabot, OWASP Dependency-Check, Black Duck** to continuously scan **package manifests** for **CVEs, outdated versions, license violations**.

- [ ] **Vulnerability Prioritization:** Understand **reachability analysis** — not every CVE in a dependency is exploitable; prioritize based on **actual code paths** that use the vulnerable function.

- [ ] **License Compliance:** Identify **copyleft licenses (GPL, AGPL)** that may require open-sourcing proprietary code; flag **license conflicts** in dependency trees.

---

### **Stage 5: Secrets Detection & Pipeline Security**

> [!TIP]
> **Goal:** : Prevent credential leakage through code and pipelines.

- [ ] **Secrets Scanning:** Use **truffleHog, gitleaks, git-secrets** to scan **git history** (not just current HEAD) for **API keys, passwords, private keys, connection strings**.

- [ ] **Pre-commit Hooks:** Install **pre-commit framework with detect-secrets or gitleaks** to block secret commits before they reach the remote repository.

- [ ] **Pipeline Hardening:** Apply **least-privilege to CI service accounts**, use **short-lived OIDC tokens** instead of long-lived secrets, scope permissions to **minimum required for each job**.

- [ ] **Container Image Security:** Scan **base images and Dockerfiles** with **Trivy, Dockle** for CVEs, misconfigurations, and secrets baked into image layers.

- [ ] **IaC Security:** Scan **Terraform, CloudFormation, Helm charts** with **Checkov, tfsec, kics** for **open security groups, public storage, missing encryption, IAM over-permission**.

### **Secure Coding & Pipeline Lab Progression**

> [!TIP]
> **Goal:** : Prove you can prevent vulnerabilities, not only scan for them.

- [ ] **Secure Coding Fix Lab:** Take a small vulnerable app and fix SQL injection, XSS, command injection, path traversal, insecure deserialization, weak auth, and insecure direct object reference patterns.
- [ ] **Code Review Lab:** Review one intentionally vulnerable repository and produce findings with file/line references, exploitability notes, and safe remediation.
- [ ] **GitHub Actions Security Lab:** Build a CI pipeline with Semgrep, gitleaks, Trivy, dependency scanning, and artifact upload.
- [ ] **Break-the-Build Gate:** Configure the pipeline to fail on critical secrets, critical dependency CVEs, and high-confidence SAST findings.
- [ ] **Threat Model Lab:** Draw a DFD for a sample app and map trust boundaries, abuse cases, and required controls.
> [!IMPORTANT]
> **Move-On Gate:** Produce a before/after report showing vulnerable code, fixed code, tests, and CI evidence.

---

<a id="toc-part-43-security-architecture--engineering"></a>
## Part 43: Security Architecture & Engineering

_Phase 8 — Governance, Supply Chain, DevSecOps & Architecture | This module fills the identified gap in security architecture training. A security professional who can only break systems but not design secure ones is incomplete._

### **Stage 1: Security Design Principles**

- [ ] **Defense-in-Depth as Architecture:** Design layered defenses where no single control failure compromises the system. Map controls to **preventative, detective, corrective, and compensating** categories.

- [ ] **Least Privilege & Separation of Duties:** Apply these principles to **network design, IAM, application architecture**, and **data access** across all tiers.

- [ ] **Fail-Safe Defaults:** Design systems that **deny by default**, require explicit grants, and **fail closed** rather than open.

- [ ] **Security by Design:** Integrate security from **requirements through deployment**, not as a bolt-on. Understand **NIST Secure Software Development Framework (SSDF)** and **OWASP SAMM**.

### **Stage 2: Zero Trust Architecture**

- [ ] **Zero Trust Principles:** Understand **"never trust, always verify"** across **identity, device, network, application, and data** pillars.

- [ ] **NIST SP 800-207:** Study the **Zero Trust Architecture** publication — understand **Policy Engine, Policy Administrator, Policy Enforcement Point** components.

- [ ] **Identity-Centric Security:** Design access control around **identity verification (MFA, SSO, RBAC/ABAC)** rather than network location.

- [ ] **Microsegmentation:** Implement **network microsegmentation** to isolate workloads. Understand **east-west traffic monitoring** and **lateral movement prevention**.

- [ ] **Continuous Verification:** Design systems that **re-authenticate and re-authorize** based on **context changes** (location, device health, behavior anomalies).

### **Stage 3: Network Security Architecture**

- [ ] **Network Segmentation Design:** Design **DMZ, internal zones, management zones, database zones** with proper **firewall rules and ACLs** between them.

- [ ] **Reference Architectures:** Study **SABSA (Sherwood Applied Business Security Architecture)** and **TOGAF security architecture** for enterprise design patterns.

- [ ] **Cloud Security Architecture:** Design secure **VPC/VNet layouts, security groups, NACLs, private endpoints, transit gateways**, and **hub-spoke network topologies** for AWS/Azure/GCP.

- [ ] **Secure Remote Access:** Design **VPN, ZTNA (Zero Trust Network Access), SASE** architectures for remote workforce security.

### **Stage 4: Data Security Architecture**

- [ ] **Data Classification:** Implement **classification schemes** (Public, Internal, Confidential, Restricted) with **automated labeling** and **DLP policy enforcement**.

- [ ] **Encryption Architecture:** Design **encryption at rest (disk, database, file), in transit (TLS, IPSec), and in use (secure enclaves, confidential computing)**.

- [ ] **Key Management:** Design **KMS architecture** with **key rotation, separation of duties, HSM backing**, and **disaster recovery** for cryptographic keys.

- [ ] **Privacy Engineering:** Implement **data anonymization, pseudonymization, tokenization** for GDPR/DPDP Act compliance. Understand **Privacy by Design** principles.

### **Stage 5: Disaster Recovery & Business Continuity**

- [ ] **DR/BCP Fundamentals:** Understand **RPO (Recovery Point Objective)** and **RTO (Recovery Time Objective)** and how they drive architecture decisions.

- [ ] **Backup Strategies:** Design **3-2-1 backup strategies** (3 copies, 2 media types, 1 offsite). Understand **immutable backups** for ransomware resilience.

- [ ] **Failover Architecture:** Design **active-passive, active-active, and pilot light** DR architectures. Understand **cold, warm, hot** site classifications.

- [ ] **DR Testing:** Plan and execute **tabletop exercises, simulation tests, and full failover tests** on a regular schedule.

### **Lab Progression**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Design a network architecture for a 3-tier web application | Architecture diagram with security controls |
| 2 | Create a Zero Trust access policy for a hybrid workforce | Policy document with NIST 800-207 mapping |
| 3 | Design a cloud security architecture (VPC, security groups, WAF) | Cloud architecture diagram |
| 4 | Develop a DR/BCP plan for a hypothetical organization | DR plan with RPO/RTO targets |
| 5 | Conduct a security architecture review of an existing design | Review findings report with recommendations |
| 6 | Design and deploy a complete monitoring stack (SIEM + EDR + NDR + SOAR + log pipeline) in a lab | End-to-end detection architecture document with data flow diagram |

> [!IMPORTANT]
> **Move-On Gate:** You can design a secure network architecture from scratch, apply Zero Trust principles, create data classification and encryption strategies, and develop DR/BCP plans with realistic RPO/RTO targets.

---

<a id="toc-part-38-ai--llm-red-teaming"></a>