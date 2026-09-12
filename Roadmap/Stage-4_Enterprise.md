# Stage 4 — Enterprise

---

### 🧭 Navigation
◀ [Stage 3: Web & App Sec](Stage-3_Web-and-App-Sec.md) | 🏠 [Master Roadmap](README.md) | [Stage 5: Specialized](Stage-5_Specialized.md) ➔

---

> [!NOTE]
> **Stage Overview — Modules 19–26**
>
> - **⏱️ Estimated Time:** ~10–13 weeks of consistent daily sessions
> - **🎯 Modules:** `19` Active Directory & Entra ID · `20` Cloud Security · `21` Containers & Kubernetes · `22` Adversary Emulation & Purple Teaming · `23` Sniffing & Spoofing · `24` Social Engineering · `25` Malware & Weaponization (conceptual) · `26` Pentest Reporting
> - **🔴 Gate:** AD domain attacked end-to-end · BloodHound exports in Git · 1 professional report — before moving to Stage 5
> - **🎯 Primary Focus:** Active Directory & Entra ID attack paths, cloud security (AWS/Azure/GCP), container & Kubernetes exploitation, adversary emulation & purple teaming, lateral movement, social engineering, and professional pentest reporting.

---

> [!NOTE]
> ### 📝 Stage 4 Documentation Requirements
> Enterprise infrastructure work must be thoroughly documented. Required artifacts:
> - **[BloodHound](Tools/BloodHound.md) exports** — attack path graphs with annotated findings
> - **Cloud attack evidence** — CloudTrail logs, IAM policy analysis, exploitation screenshots
> - **Terraform/CloudFormation configs** — infrastructure-as-code for lab environments committed to Git
> - **Purple team ATT&CK heatmap** — technique coverage matrix showing detection gaps
> - **Git commits** — all configs, exports, and reports committed
>
> _By the end of Phase 6, you should have enterprise attack documentation rivaling junior consultant deliverables._

> [!IMPORTANT]
> ### 🛠️ Mandatory Tool Stack (Must Master in This Phase)
>
> | Priority | Tool | Purpose & Core Skills |
> | :--- | :--- | :--- |
> | **Tier 1 (Mandatory)** | [BloodHound](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/BloodHound.md) & SharpHound | AD/Azure graph collection, Cypher query analysis, ACL abuse pathing (`ShortestPath to Domain Admins`). |
> | **Tier 1 (Mandatory)** | [Impacket](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/Impacket.md) Suite | Protocol-level attacks (`secretsdump.py`, `psexec.py`, `wmiexec.py`, `GetNPUsers.py`, `GetUserSPNs.py`). |
> | **Tier 1 (Mandatory)** | [Mimikatz](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/Mimikatz.md) & [Rubeus](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/Rubeus.md) | LSASS credential dumping (`sekurlsa::logonpasswords`), Kerberoasting, AS-REP roasting, Overpass-the-Hash, ticket injection. |
> | **Tier 1 (Mandatory)** | **Certipy** | Active Directory Certificate Services (ADCS) enumeration, ESC1/ESC4 template exploitation, shadow credentials. |
> | **Tier 1 (Mandatory)** | [NetExec](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/NetExec.md) (nxc) | Network spray & lateral movement orchestrator across SMB, WinRM, LDAP, MSSQL, and RDP. |
> | **Tier 1 (Mandatory)** | **Prowler & Pacu** | AWS/Azure cloud security posture assessment, IAM privilege escalation, misconfiguration exploitation. |
> | **Tier 2 (Secondary)** | [Evil-WinRM](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/Evil-WinRM.md) | WinRM remote shell execution, DLL payload loading, pass-the-hash administrative control. |
> | **Tier 2 (Secondary)** | [Kerbrute](file:///home/smilo/Desktop/MY_FOLDER/Cyber-Security/Roadmap/Tools/Kerbrute.md) | Fast Active Directory user enumeration and password brute-forcing via Kerberos pre-auth. |
> | **Tier 2 (Secondary)** | **Trivy & ScoutSuite** | Container/Kubernetes image vulnerability scanning and multi-cloud security auditing. |
>
> **Stage 4 Exit Gate:** You cannot pass Stage 4 until you can enumerate domain accounts with `Kerbrute`, collect AD graph data with `SharpHound`, visualize privilege escalation paths in `BloodHound`, exploit an ADCS misconfiguration with `Certipy`, and dump the NTDS.dit database via `secretsdump.py`.

---

### 🗂️ Table of Contents

- [Module 19: Active Directory & Entra ID](#module-19-active-directory--entra-id)
  - [Topic 1: Discovery & Enumeration](#stage-1-discovery-enumeration)
  - [Topic 2: Credential & Auth Attacks](#stage-2-credential-auth-attacks)
  - [Topic 3: Delegation, ACL, and ADCS Abuse](#stage-3-delegation-acl-and-adcs-abuse)
  - [Topic 4: Lateral Movement & Persistence](#stage-4-lateral-movement-persistence)
  - [Topic 5: Entra ID (Azure AD) & Hybrid Attacks](#stage-5-entra-id-azure-ad-hybrid-attacks)
  - [Lab Progression (Active Directory & Entra ID)](#lab-progression-part-23-active-directory-entra-id)
- [Module 20: Cloud Computing](#module-20-cloud-computing)
  - [Topic 1: Architecture & Governance](#stage-1-architecture-governance)
  - [Topic 2: Storage & Data Security](#stage-2-storage-data-security)
  - [Topic 3: Modern Infrastructure & Deployment](#stage-3-modern-infrastructure-deployment)
  - [Topic 4: Automation & Scripting](#stage-4-automation-scripting)
  - [Topic 5: Cloud-Specific Attack Vectors](#stage-5-cloud-specific-attack-vectors)
  - [Topic 6: IAM & PAM Attack Surface](#stage-6-iam-pam-attack-surface)
- [Module 21: Container & Orchestration Security](#module-21-container--orchestration-security)
  - [Topic 1: Container Fundamentals & Attacks](#stage-1-container-fundamentals-attacks)
  - [Topic 2: Kubernetes Security](#stage-2-kubernetes-security)
  - [Topic 3: Container Runtime Security](#stage-3-container-runtime-security)
  - [Topic 4: Secrets & Configuration Management](#stage-4-secrets-configuration-management)
  - [Topic 5: CI/CD & Workflow Automation Attacks](#stage-5-cicd-workflow-automation-attacks)
  - [Lab Progression (Container & Orchestration Security)](#lab-progression-part-25-container-orchestration-security)
- [Module 22: Adversary Emulation & Purple Teaming](#module-22-adversary-emulation--purple-teaming)
  - [Topic 1: MITRE ATT&CK Framework Mastery](#stage-1-mitre-attck-framework-mastery)
  - [Topic 2: APT & Threat Actor Emulation](#stage-2-apt-threat-actor-emulation)
  - [Topic 3: Purple Team Exercises](#stage-3-purple-team-exercises)
  - [Topic 4: Metrics & Reporting](#stage-4-metrics-reporting)
  - [Lab Progression (Adversary Emulation & Purple Teaming)](#lab-progression-part-16-adversary-emulation-purple-teaming)
- [Module 23: Sniffing & Spoofing](#module-23-sniffing--spoofing)
  - [Topic 1: The Environment & Fundamentals](#stage-1-the-environment-fundamentals-the-setup)
  - [Topic 2: Sniffing & Passive Reconnaissance](#stage-2-sniffing-passive-reconnaissance-the-ear)
  - [Topic 3: Spoofing & Active Deception](#stage-3-spoofing-active-deception-the-lie)
  - [Topic 4: Man-in-the-Middle & Exploitation](#stage-4-man-in-the-middle-exploitation-the-kill)
  - [Topic 5: Defenses & Mitigation](#stage-5-defenses-mitigation-the-shield)
  - [Lab Progression (Sniffing & Spoofing)](#lab-progression-part-9-sniffing-spoofing)
- [Module 24: Social Engineering](#module-24-social-engineering)
  - [Topic 0: The Psychology of Social Engineering](#stage-0-the-psychology-of-social-engineering-the-foundation)
  - [Topic 1: Intelligence & Reconnaissance](#stage-1-intelligence-reconnaissance-the-setup)
  - [Topic 2: The Digital Assault](#stage-2-the-digital-assault-remote-vectors)
  - [Topic 3: The Human Element](#stage-3-the-human-element-direct-interaction)
  - [Topic 4: The Physical Breach](#stage-4-the-physical-breach-boots-on-the-ground)
  - [Topic 5: Defense & Awareness](#stage-5-defense-awareness-the-shield)
  - [Lab Progression (Social Engineering)](#lab-progression-part-10-social-engineering)
- [Module 25: Malware & Weaponization (Conceptual)](#module-25-malware--weaponization-conceptual)
  - [Topic 1: The Design & Logic (Architecture)](#stage-1-the-design-logic-architecture)
  - [Topic 2: The Payload & Mechanism](#stage-2-the-payload-mechanism-weaponization)
  - [Topic 3: Evasion & Defense Bypassing](#stage-3-evasion-defense-bypassing-invisibility)
  - [Topic 4: Persistence & Escalation](#stage-4-persistence-escalation-entrenchment)
  - [Topic 5: Counter-Forensics & Cleanup](#stage-5-counter-forensics-professionalism-the-cleanup)
  - [Topic 6: Document & Cloud Weaponization](#stage-6-document-cloud-weaponization)
- [Module 26: Pentest Methodologies & Report Writing](#module-26-pentest-methodologies--report-writing)
  - [Topic 1: Industry-Standard Engagement Frameworks](#stage-1-industry-standard-engagement-frameworks)
  - [Topic 2: Scoping, Legal Frameworks & Engagement Management](#stage-2-scoping-legal-frameworks-engagement-management)
  - [Topic 3: Structured Threat Modeling](#stage-3-structured-threat-modeling)
  - [Topic 4: Vulnerability Scoring & Risk Prioritization](#stage-4-vulnerability-scoring-risk-prioritization)
  - [Topic 5: Professional Report Writing](#stage-5-professional-report-writing)
- [Stage Gate 3](#stage-gate-3)

---

<a id="part-23-active-directory-entra-id"></a>


---

<a id="module-19-active-directory--entra-id"></a>
<a id="part-23-active-directory-entra-id"></a>

## Module 19: Active Directory & Entra ID


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `EA - Windows Security Internals with PowerShell` — Primary companion — AD internals, attack paths (Kerberoasting, DCSync, Golden Ticket), PowerShell enumeration
> - 🟡 `Windows PowerShell Cookbook` — Reference — PowerShell command reference for AD enumeration and post-exploitation
> - 🟡 `Windows Server automation with PowerShell cookbook` — Reference — Group Policy, SYSVOL, service configs
> - 🟢 `Cybersecurity Attack-and-Defense Strategies 2nd` — Enterprise attack chain coverage — red vs blue perspective on AD attacks


> [!IMPORTANT]
> **Prerequisite Patch Required Before Part 23:** Before starting AD attacks, complete Phase 1 **Stage 5** (Active Directory Concepts) and **Stage 6** (Windows Identity & Kerberos Foundations) in Part 1C. Do not skip these — Kerberoasting and delegation attacks are incomprehensible without understanding the Kerberos ticket lifecycle first. This is a targeted patch, not a full Phase 1 restart.

> [!NOTE]
> **Part 23 Internal Learning Sequence** — on-prem AD first, then Entra ID:
>
> ```text
> AD architecture: forest / domain / trust relationships
>         ↓
> Objects: users / groups / computers / OUs / service accounts
>         ↓
> LDAP queries & domain enumeration (BloodHound, ldapsearch)
>         ↓
> Kerberos protocol mechanics (TGT, TGS, KRB_AS_REQ/REP, KRB_TGS_REQ/REP)
>         ↓
> SPNs & service accounts (Kerberoasting attack surface)
>         ↓
> Group Policy Objects (GPO) — abuse vectors
>         ↓
> ACLs & delegation — GenericAll, WriteDACL, ForceChangePassword, etc.
>         ↓
> Credential attacks — Pass-the-Hash, Pass-the-Ticket, Overpass-the-Hash
>         ↓
> Kerberoasting & AS-REP Roasting
>         ↓
> Constrained & unconstrained delegation attacks
>         ↓
> AD Certificate Services (AD CS) — ESC1–ESC8 attack paths
>         ↓
> Lateral movement in AD environments
>         ↓
> Persistence mechanisms in AD
>         ↓
> ── THEN: Entra ID ──
>         ↓
> Entra ID (Azure AD) architecture & hybrid identity
>         ↓
> Federation, conditional access, service principals, managed identities
> ```
>
> **Do not attempt Entra ID / cloud identity before you understand on-prem Kerberos.** Hybrid identity attacks only make sense in context of the on-prem model.


<a id="stage-1-discovery-enumeration"></a>
### **Topic 1: Discovery & Enumeration** — `🔬 Practical`

> [!TIP]
> **Goal:** Map identity surfaces across on-prem AD and Entra ID (Azure AD).

- [ ] **Domain Recon:** Enumerate **domains/forests, trusts, sites, subnets, FSMO roles**; collect **OU/Group/ACL** data.

- [ ] **Identity Inventory:** List **users, computers, service accounts, Tier0 assets, SPNs**, and **LAPS** posture.

- [ ] **Policy & Exposure:** Audit **GPOs, login scripts, startup tasks**, and **Unconstrained/Constrained/RBCD** exposure.

- [ ] **Entra ID/Cloud Recon:** Enumerate **tenants, apps, service principals, consented permissions, conditional access** and **enterprise apps**.

---

<a id="stage-2-credential-auth-attacks"></a>
### **Topic 2: Credential & Auth Attacks** — `🔬 Practical`

> [!TIP]
> **Goal:** Steal or replay credentials to gain higher privilege.

- [ ] **Kerberoast / AS-REP Roast:** Extract **TGS/AS-REP** tickets for offline cracking; prioritize **high-priv SPNs**.

- [ ] **NTLM Relay/SMB/HTTP:** Abuse **NTLM relays** against **SMB/LDAP/HTTP/ADCS HTTP endpoints**; combine with **mTLS gaps**.

- [ ] **Token Abuse:** Steal **TGT/TGS, DPAPI, LSASS, browser tokens**, and **OAuth refresh tokens** across hybrid joins.

- [ ] **Password Hygiene:** Spray with **safe lockout windows**, target **legacy auth (POP/IMAP/SMTP)**, and downgrade to **basic auth** where possible.

---

<a id="stage-3-delegation-acl-and-adcs-abuse"></a>
### **Topic 3: Delegation, ACL, and ADCS Abuse** — `🔬 Practical`

> [!TIP]
> **Goal:** Abuse trust relationships and misconfigurations for escalation.

- [ ] **Delegation Abuse:** Exploit **Unconstrained Delegation** (harvesting TGTs from spooler abuse), **Constrained Delegation** (service/alt service S4U2self & S4U2proxy), and **Resource-Based Constrained Delegation (RBCD)** (configuring `msDS-AllowedToActOnBehalfOfOtherIdentity` via machine account creation).

- [ ] **ACL/ACE Abuse:** Graph abuse paths with BloodHound and execute write primitives: **WriteOwner, WriteDACL, GenericAll, GenericWrite, ExtendedRight (ForceChangePassword), AddMember** on critical principals (Domain Admins, Enterprise Admins, Domain Controllers, Tier0 groups).

- [ ] **Shadow Credentials (`msDS-KeyCredentialLink`):** Exploit `GenericWrite`/`WriteProperty` over computer or user accounts using `certipy shadow auto` or `pywhiskey` to inject raw RSA public keys and authenticate via PKINIT without knowing or changing the victim's password.

- [ ] **ADCS (Active Directory Certificate Services) Deep Dive (ESC1–ESC13 via Certipy):**
  - **Reconnaissance & Auditing:** Run `certipy find -vulnerable -stdout` to enumerate Enterprise CAs, Certificate Templates, and vulnerable enrollment permissions.
  - **ESC1 / ESC2:** Templates with Client Authentication EKU and `CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT` enabled — request a certificate with an arbitrary Subject Alternative Name (SAN, e.g., Domain Admin) using `certipy req -ca <CA-Name> -template <Template> -upn administrator@domain.local`.
  - **ESC3:** Enrollment Agent templates (`Certificate Request Agent` EKU) — request an agent certificate to enroll on behalf of another user.
  - **ESC4:** Vulnerable template access control rights (`WriteDacl`, `WriteOwner`, `GenericAll`) — overwrite template properties to enable `ENROLLEE_SUPPLIES_SUBJECT` and Client Authentication, abuse the template, and restore original configuration.
  - **ESC6 & ESC7:** CA configured with `EDITF_ATTRIBUTESUBJECTALTNAME2` (allows SAN specification on any template) or vulnerable CA access rights (`ManageCA`, `ManageCertificates` — issue pending requests or dump CA private keys for Golden Certificates).
  - **ESC8 (NTLM Relay to ADCS Web Enrollment):** Relay coerced authentication (via PetitPotam or PrinterBug without signing) to HTTP enrollment endpoints (`/certsrv/`) to mint machine/user certificates.
  - **ESC9, ESC10, ESC11, ESC13:** Strong certificate binding bypasses, missing RPC packet privacy (`RPC_C_AUTHN_LEVEL_PKT_PRIVACY`), and issuance policy OID group link privilege escalation.
  - **PKINIT Authentication & UnPAC-the-Hash:** Use `certipy auth -pfx cert.pfx -dc-ip <ip>` to authenticate via PKINIT, obtain a Kerberos TGT, and extract the account's plaintext NT hash directly from the Kerberos PAC (`UnPAC-the-hash`).

---

<a id="stage-4-lateral-movement-persistence"></a>
### **Topic 4: Lateral Movement & Persistence** — `🔬 Practical`

> [!TIP]
> **Goal:** Move horizontally and maintain footholds.

- [ ] **Lateral Paths:** Use **WinRM/SMB/RDP/WMI/PowerShell Remoting**, **admin shares**, and **task/svc installs** guided by **BloodHound** paths.

- [ ] **GPO Persistence:** Implant via **logon scripts, immediate scheduled tasks, startup items**; abuse **restricted groups** for re-add.

- [ ] **DCSync / DCShadow:** Abuse **Replicating Directory Changes** (`DS-Replication-Get-Changes-All`) using Mimikatz or `impacket-secretsdump` to pull **NTDS.dit** hashes or inject rogue domain objects via DCShadow.

- [ ] **Golden/Silver Tickets:** Forge **krbtgt/service hashes** for long-lived access; manage **ticket lifetime/renewal** OPSEC.

- [ ] **Cross-Forest Trust Exploitation & SID History:**
  - Enumerate domain and forest trusts using PowerView (`Get-DomainTrust`, `Get-ForestDomain`) or `netdom query trust`.
  - Exploit bidirectional / parent-child trusts: forge inter-realm referral tickets (cross-realm TGT) using the domain trust key.
  - Exploit missing SID filtering on external or forest trusts: inject privileged SIDs (e.g., Enterprise Admins `EA -519`) into `sIDHistory` to achieve full compromise across the trust boundary.
  - Abuse Foreign Security Principals (FSPs) and cross-forest delegation.

---

<a id="stage-5-entra-id-azure-ad-hybrid-attacks"></a>
### **Topic 5: Entra ID (Azure AD) & Hybrid Attacks** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Exploit cloud identity to pivot and persist.

- [ ] **Consent & OAuth Abuse:** Steal or register **malicious multi-tenant apps**, abuse **illicit consent grants**, and persist via **refresh tokens**.

- [ ] **Conditional Access Bypass:** Exploit **trusted locations, device compliance gaps, legacy auth exemptions**, and **MFA registration weaknesses**.

- [ ] **Passwordless/Passkeys:** Target **FIDO2/Passkey registration flows**, backup methods, and **SSPR** to hijack accounts.

- [ ] **Cross-Cloud Pivot:** Use **Entra app roles** and **federation trusts** to pivot into **AWS/GCP** integrations; harvest **Graph/SharePoint** data for lateral move.

---

<a id="lab-progression-part-23-active-directory-entra-id"></a>
### **Lab Progression (Part 23: Active Directory & Entra ID)**

> [!TIP]
> **Goal:** Build and attack identity infrastructure with evidence and rollback.

- [ ] **AD Lab Build:** Deploy a domain controller, at least one workstation, DNS, domain users/groups, and basic GPOs.
- [ ] **Vulnerable AD Lab:** Use GOAD, DetectionLab, PurpleCloud, or a self-built intentionally weak domain to practice safely.
- [ ] **BloodHound Lab:** Ingest data, identify attack paths, validate one path in the lab, then write the remediation.
- [ ] **Kerberos Lab:** Perform lab-only AS-REP roasting/Kerberoasting and crack only synthetic passwords created for the exercise.
- [ ] **Entra ID Lab:** Create test users, app registrations, conditional access policies, and sign-in logs; document identity detections.
> [!IMPORTANT]
> **Move-On Gate:** Produce an AD/Entra attack-path report with screenshots, graph evidence, event IDs, and hardening steps.

<a id="toc-part-24-cloud-computing"></a>
<a id="part-24-cloud-computing"></a>

---

<a id="module-20-cloud-computing"></a>
<a id="part-24-cloud-computing"></a>

## Module 20: Cloud Computing


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Cloud_Hacking (1)` — Full — cloud attack methodology overview (misconfigs, SSRF to metadata, IAM abuse)
> - 🟢 `Trusted Cloud Computing` — Reference — cloud security architecture and defensive design context


> [!IMPORTANT]
> **Cloud Lab Setup Requirements — Read Before Starting**
>
> Cloud attack techniques CANNOT be practiced without a real cloud account. Unlike Phase 2 Linux labs (which run locally), cloud labs require live infrastructure. Before starting this part:
>
> **Account Setup:**
> - [ ] Create a dedicated **AWS Free Tier account** (separate from any personal/work account) at aws.amazon.com/free — Free Tier covers most EC2, S3, IAM labs for 12 months
> - [ ] Create a dedicated **Azure Free Account** (separate from any personal/work account) — $200 credit for 30 days + 12 months of free services
> - [ ] (Optional) Create a **GCP Free Account** — $300 credit for 90 days
>
> **Cost Controls (Mandatory — Set Before Any Lab Work):**
> - [ ] **AWS Billing Alert:** Go to CloudWatch → Alarms → Billing → create alert at $5/month threshold; also enable Cost Explorer
> - [ ] **Azure Budget Alert:** Go to Cost Management → Budgets → set $5/month alert
> - [ ] Never leave EC2 instances, RDS databases, or NAT Gateways running when not actively using them
> - [ ] Use `aws ec2 stop-instances` or the console to stop (not just terminate) instances to avoid data loss; terminate when done with the lab
>
> **Intentionally-Vulnerable Cloud Lab Environments:**
>
> | Platform | Provider | What It Teaches | Setup |
> |---|---|---|---|
> | **CloudGoat** | Rhino Security Labs | AWS IAM privilege escalation, SSRF, Lambda exploitation, S3 misconfigs | `pip install cloudgoat` then `cloudgoat config` |
> | **AzureGoat** | INE Security | Azure IAM, SSRF, storage attacks, Kubernetes in Azure | GitHub: ine-labs/AzureGoat |
> | **GCPGoat** | INE Security | GCP service account abuse, Cloud Run, storage | GitHub: ine-labs/GCPGoat |
> | **flaws.cloud** | Scott Piper (AWS) | S3 misconfiguration CTF walkthrough | flaws.cloud |
> | **flaws2.cloud** | Scott Piper (AWS) | IAM escalation CTF (attacker + defender paths) | flaws2.cloud |
>
> > [!WARNING]
> > **Never practice cloud attack techniques against accounts you do not own and have not specifically provisioned for testing.** Cloud APIs leave detailed audit trails in CloudTrail/Activity Log. Unauthorized access to cloud accounts is a federal crime under CFAA and equivalent laws. Always use dedicated lab accounts with explicit resource tagging.

<a id="stage-1-architecture-governance"></a>
### **Topic 1: Architecture & Governance** — `🧠 Conceptual`


> [!TIP]
> **Goal:** Define the battlefield and the rules of engagement — understand the cloud responsibility model, IAM structure, and baseline security posture tools before touching any attack techniques.

- [ ] **Model Selection:** Select the correct `Cloud Models` (`Public`, `Private`, `Hybrid`) based on data sensitivity.

- [ ] **Responsibility Mapping:** Apply the **Shared Responsibility Model** based on the service type (`IaaS`, `PaaS`, `SaaS`) to identify what you must secure vs. the provider.

- [ ] **Environment Setup:** Initialize the tenant in a `Common Cloud Environment` (`AWS`, `GCP`, or `Azure`) with a secure root account setup.

- [ ] **IAM Architecture Review:** Understand the **IAM hierarchy** for your target cloud — AWS (root → organizations → accounts → users/roles/policies), Azure (Entra tenant → subscriptions → resource groups → resources), GCP (org → folders → projects → service accounts). Know which identity types are exploitable at each level.

- [ ] **Security Posture Baseline:** Run **ScoutSuite** (`scout aws --report-dir ./report`) or **Prowler** (`prowler aws`) to generate a baseline cloud security posture assessment across IAM, S3, networking, logging, and encryption. Read the full output — these tools reveal the attack surface before you start.

- [ ] **Resource Tagging & Environment Hygiene:** Understand how **resource tagging** (Owner, Environment, CostCenter) enables defenders to identify unauthorized resources. From an attacker's perspective: resources without standard tags are likely shadow IT or misconfigurations worth targeting.

---

<a id="stage-2-storage-data-security"></a>
### **Topic 2: Storage & Data Security** — `🔬 Practical`

> [!TIP]
> **Goal:** Enumerate, audit, and exploit cloud storage misconfigurations — the most common source of cloud data breaches.

- [ ] **Object Storage Security:** Audit `S3` buckets and `Common Cloud Storage` (Drive, Box) for public access and enforce encryption.

- [ ] **Access Control:** Implement strict IAM policies ensuring only authorized identities can access storage blobs.

- [ ] **S3 Bucket Enumeration:** Use `aws s3api list-buckets` to enumerate all buckets in-scope. For each bucket, run `aws s3api get-bucket-acl`, `get-bucket-policy`, `get-bucket-cors`, and `get-public-access-block` to map the full exposure surface. Use **cloudbrute** for unauthenticated bucket discovery against organization name variants.

- [ ] **ACL & Policy Audit:** Identify buckets with `AllUsers` (public) or `AuthenticatedUsers` (any AWS account) grants in their ACL. Identify bucket policies with `"Principal": "*"` without a restrictive condition. Both patterns create read/write exposure without authentication.

- [ ] **CORS Misconfiguration:** Retrieve CORS config with `aws s3api get-bucket-cors`. Permissive CORS (`AllowedOrigin: *` + `AllowCredentials: true` patterns) enables cross-origin data theft from authenticated browser sessions. Test with a crafted request from an attacker origin.

- [ ] **Secrets in Object Storage:** Use **trufflehog** (`trufflehog s3 --bucket=<name>`) to scan bucket contents for hardcoded credentials, API keys, database connection [strings](Tools/strings.md), and private certificates that developers have uploaded and forgotten.

---

<a id="stage-3-modern-infrastructure-deployment"></a>
### **Topic 3: Modern Infrastructure & Deployment** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Audit and attack the compute layer and the deployment pipeline — misconfigurations here grant persistent, privileged access.

- [ ] **Code-Defined Security:** Use `Infrastructure as Code` (IaC) to template firewalls and permissions, preventing human configuration errors.

- [ ] **Serverless Hardening:** Secure `Serverless` functions by minimizing privileges and auditing dependencies for vulnerabilities.

- [ ] **Pipeline Security:** Audit the `general flow of deploying in the cloud` to ensure secrets (API keys) are not hardcoded in the deployment scripts.

- [ ] **IaC Security Scanning:** Run **checkov** (`checkov -d ./terraform/`) against Terraform/CloudFormation/CDK templates to identify misconfigurations before deployment — open security groups, unencrypted storage, overly permissive IAM roles. Also run **tfsec** (Terraform-specific) and **cfn-nag** (CloudFormation-specific) for complementary coverage.

- [ ] **Terraform State File Exposure:** Terraform state files (`terraform.tfstate`) contain plaintext resource metadata including IAM role ARNs, IP addresses, and sometimes credentials. Check for state files stored in public S3 buckets, unencrypted S3 with broad access, or committed to Git repositories. This is one of the highest-value targets in a cloud engagement.

- [ ] **CDK & Serverless Security Patterns:** Audit AWS CDK constructs and serverless framework configurations (`serverless.yml`) for: Lambda functions with `*` in IAM policies, environment variables containing plaintext secrets, API Gateway endpoints without authentication, and functions with `VpcConfig` that bypass security group controls.

---

<a id="stage-4-automation-scripting"></a>
### **Topic 4: Automation & Scripting** — `🔬 Practical`

> [!TIP]
> **Goal:** Use automation to enumerate, audit, and monitor cloud environments — understand what defenders see so you know what to avoid generating.

- [ ] **Cloud Automation:** Use **Python (Boto3), Terraform, CloudFormation** to audit security groups and IAM roles automatically.

- [ ] **Admin Scripting:** Master **Bash, PowerShell, AWS CLI, Azure CLI** to manage instances and automate operations.

- [ ] **CI/CD Security:** Integrate **security scanning** (SAST, DAST, dependency checks) into deployment pipelines.

- [ ] **CloudTrail Log Analysis:** Query **CloudTrail** (`aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=ConsoleLogin`) to identify unauthorized API calls, credential use from unusual IPs, role assumption chains, and resource creation events. Understand log retention gaps — events older than 90 days require S3 log archive access.

- [ ] **AWS CLI Enumeration Commands:** Build a systematic enumeration checklist: `aws iam list-users`, `aws iam list-roles`, `aws iam get-account-authorization-details` (dumps all policies, users, roles in one call), `aws ec2 describe-instances`, `aws s3api list-buckets`, `aws lambda list-functions`. For Azure: `az account list`, `az role assignment list --all`, `az vm list`. Run these as the first step after any credential compromise.

- [ ] **Cross-Account Audit Automation:** Use **Prowler's multi-account mode** or write Boto3 scripts using `sts:AssumeRole` to enumerate security posture across all accounts in an AWS Organization from a single auditor role. Understand how cross-account role trust policies create lateral movement paths.

> [!IMPORTANT]
> **⚠️ Stage 4 Intermediate Checkpoint (Part 24: Cloud Computing) — NOT the Part Exit Gate**
> You must still complete **Stages 5 and 6** before leaving Part 24. This checkpoint verifies Stage 1–4 readiness only. You are ready to continue to Stage 5 when you can: (1) run ScoutSuite or Prowler against a lab AWS account and interpret the findings report; (2) enumerate all S3 buckets, their ACLs, bucket policies, and CORS configurations using the AWS CLI; (3) use trufflehog to scan an S3 bucket for secrets; (4) run checkov against a Terraform template and explain each HIGH finding; (5) query CloudTrail to identify at least one suspicious API event in a lab environment. If you cannot do all five without looking up the commands, revisit Stages 2–4 before proceeding. **Then continue to Stage 5 (Cloud Attack Vectors) and Stage 6 (IAM & PAM).**

---

<a id="stage-5-cloud-specific-attack-vectors"></a>
### **Topic 5: Cloud-Specific Attack Vectors** — `🔬 Practical`

> [!TIP]
> **Goal:** Understand unique cloud threats.

- [ ] **IAM Exploitation & Role Chaining:**
  - Abuse **AssumeRole trust chains** across AWS accounts; enumerate trust policies using `pacu` or `enumerate-iam`.
  - Exploit `iam:PassRole` attached to EC2 or Lambda to elevate privileges to higher-tier service roles.
  - Roll back IAM policies to insecure previous versions using `iam:SetDefaultPolicyVersion`.

- [ ] **Storage Misconfigurations:** Find **public S3 buckets, Azure blob containers, and GCP storage buckets** via unauthenticated enumeration, CORS manipulation, and unencrypted snapshot exports.

- [ ] **Metadata Services (IMDSv1 vs IMDSv2 Deep Dive):**
  - **IMDSv1 Vulnerability:** Query `http://169.254.169.254/latest/meta-data/iam/security-credentials/<role-name>` directly via simple GET in SSRF payloads to extract temporary STS access keys, secret keys, and session tokens.
  - **IMDSv2 Defense & Bypass Surface:** IMDSv2 enforces session-oriented requests requiring a `PUT` request with `X-aws-ec2-metadata-token-ttl-seconds: 21600` to generate a session token, then requires passing the token in `X-aws-ec2-metadata-token: <token>`. Understand how this neutralizes blind SSRF and reverse proxies without header forwarding, but remains vulnerable to full SSRF with custom header injection or command injection on host/container processes.

- [ ] **Serverless Attacks:** Exploit **Lambda/Cloud Functions environment variables, excessive execution permissions, event injection, and cold-start persistence**.

- [ ] **Container Escapes:** Break out of **Docker, Kubernetes pods** via misconfigurations. 📌 _See Part 25 Stage 1 for full container escape techniques and Part 25 Stage 2 for Kubernetes-specific attacks._

- [ ] **Multi-Tenancy & Supply Chain:** Understand **cross-tenant data leakage, shared VPC routing oversights, and CI/CD runner poisoning**.

---

<a id="stage-6-iam-pam-attack-surface"></a>
### **Topic 6: IAM & PAM Attack Surface** — `🔬 Practical`

> [!TIP]
> **Goal:** Master identity-based attack techniques in cloud and enterprise environments.

- [ ] **IAM Policy Analysis & CIEM:** Enumerate and analyze **IAM policies** using **Pacu, enumerate-iam, ScoutSuite, Prowler** to find **overprivileged roles, wildcard permissions (*)**, and privilege escalation paths across **AWS/Azure/GCP**. Implement **CIEM (Cloud Infrastructure Entitlement Management)** concepts to identify toxic combinations and unused excessive permissions.

- [ ] **Role Chaining & Federation Abuse:** Exploit **AssumeRole chains, cross-account trust relationships, OIDC federation, SAML assertion manipulation** to escalate from low-privilege to administrative access.

- [ ] **Service Account & Managed Identity Abuse:** Target **service accounts, managed identities, workload identity federation** with excessive permissions or leaked credentials. Understand **key rotation failures** and **long-lived access key risks**.

- [ ] **Conditional Access & Policy Bypass:** Test **Azure Conditional Access policies, AWS SCPs (Service Control Policies), GCP Organization Policies** for bypass conditions — **device compliance gaps, location spoofing, legacy auth exemptions, MFA registration weaknesses**.

- [ ] **Privileged Access Management (PAM):** Understand **CyberArk, Delinea (Thycotic), BeyondTrust** vault architecture — **credential vaulting, session recording, just-in-time (JIT) access, credential rotation**. Know the attack surface: **vault admin compromise, session proxy hijacking, checkout abuse, emergency break-glass exploitation**.

- [ ] **Identity Governance:** Understand **access reviews, entitlement management, separation of duties (SoD)**, and how **identity lifecycle gaps** (orphaned accounts, excessive standing privileges, stale service principals) create attack opportunities.

> [!IMPORTANT]
> **Move-On Gate (Part 24: Cloud Computing):** You are ready to proceed to Part 25 when you can: (1) execute an IAM privilege escalation path in a CloudGoat lab from low-privilege user to admin using only misconfigured policies; (2) identify a Conditional Access bypass condition in a lab Azure tenant and explain why it exists; (3) explain the difference between a SAML token, an OAuth access token, and a Kerberos TGT — and what happens when each is stolen.

---

<a id="toc-part-25-container--orchestration-security"></a>
<a id="part-25-container-orchestration-security"></a>

---

<a id="module-21-container--orchestration-security"></a>
<a id="part-25-container-orchestration-security"></a>

## Module 21: Container & Orchestration Security


<a id="stage-1-container-fundamentals-attacks"></a>
### **Topic 1: Container Fundamentals & Attacks** — `🔬 Practical`

> [!TIP]
> **Goal:** Understand containerization and its security implications.

- [ ] **Container Anatomy:** Master **namespaces (PID, NET, MNT, IPC, UTS, USER), cgroups (v1/v2 resource limits), capabilities (POSIX capabilities), seccomp profiles, AppArmor/SELinux** as isolation mechanisms.

- [ ] **Image Vulnerabilities:** Scan images with **Trivy, Clair, Grype** for **CVEs, secrets, misconfigs** in layers.

- [ ] **Dockerfile Security:** Audit **Dockerfiles** for **running as root, exposed secrets, vulnerable base images, unnecessary packages**.

- [ ] **Container Escape Primitives & Host Takeover:**
  - **`--privileged` Mode Exploitation:** Containers run without seccomp filtering and with all capabilities enabled; mount the underlying host hard disk (`mount /dev/sda1 /mnt`) and chroot to gain instant host root.
  - **Abuse of Capabilities (`CAP_SYS_ADMIN`):** Exploit cgroup v1 `release_agent` (`notify_on_release`) to execute arbitrary host commands when the cgroup terminates.
  - **Mounted Docker Socket (`/var/run/docker.sock`):** Issue commands to the host Docker daemon from inside the container to spawn a sibling privileged container: `docker -H unix:///var/run/docker.sock run -v /:/host -it alpine chroot /host`.
  - **Namespace Hijacking (`hostPID` + `nsenter`):** If `--pid=host` is enabled, list host processes and use `nsenter -t 1 -m -u -i -n -p -- /bin/bash` to enter the host's root namespace.
  - **Shared Kernel Exploits:** Kernel vulnerabilities (e.g., Dirty COW, Dirty Pipe CVE-2022-0847, CVE-2022-0492) that compromise the host kernel directly through container syscalls.

- [ ] **Docker API Exploitation:** Abuse **exposed Docker API (2375 unauthenticated / 2376 TLS misconfigured)** to remotely spawn privileged containers and compromise host.

---

<a id="stage-2-kubernetes-security"></a>
### **Topic 2: Kubernetes Security** — `🔬 Practical`

> [!TIP]
> **Goal:** Attack and defend container orchestration platforms.

- [ ] **K8s Architecture:** Understand **control plane (API server, etcd, scheduler)** vs **data plane (kubelet, kube-proxy)** components.

- [ ] **RBAC Exploitation:** Abuse **overprivileged service accounts, role bindings, cluster-admin** for privilege escalation.

- [ ] **Pod Escape:** Break out via **hostPath mounts, hostNetwork, hostPID, privileged pods** to access host filesystem.

- [ ] **Secrets Extraction:** Steal **Kubernetes secrets** from **etcd, mounted volumes, environment variables, service account tokens**.

- [ ] **API Server Abuse:** Exploit **unauthenticated API, certificate theft, kubeconfig exposure** for cluster control.

- [ ] **Network Policy Bypass:** Pivot through **missing network policies** to access isolated pods and services.

---

<a id="stage-3-container-runtime-security"></a>
### **Topic 3: Container Runtime Security** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Detect and prevent malicious container activity.

- [ ] **Runtime Monitoring:** Deploy **Falco, Sysdig, Aqua** to detect **suspicious syscalls, process execution, network connections**.

- [ ] **Admission Control:** Use **OPA (Open Policy Agent), Kyverno** to enforce **security policies at admission time**.

- [ ] **Image Signing:** Implement **Notary, Cosign** for **image provenance verification** and supply chain security.

- [ ] **Runtime Protection:** Enable **seccomp profiles, AppArmor/SELinux policies** to restrict container capabilities.

- [ ] **Network Segmentation:** Deploy **Calico, Cilium** network policies to **microsegment pod-to-pod communication**.

---

<a id="stage-4-secrets-configuration-management"></a>
### **Topic 4: Secrets & Configuration Management** — `🔬 Practical`

> [!TIP]
> **Goal:** Secure sensitive data in containerized environments.

- [ ] **Secret Stores:** Use **HashiCorp Vault, AWS Secrets Manager, Azure Key Vault** instead of K8s native secrets.

- [ ] **Init Containers:** Fetch secrets at **pod startup** via init containers instead of baking into images.

- [ ] **Sealed Secrets:** Encrypt secrets in Git using **Bitnami Sealed Secrets, SOPS** for GitOps workflows.

- [ ] **Workload Identity:** Use **cloud provider workload identity** (AWS IRSA, GCP Workload Identity) for keyless authentication.

- [ ] **Secret Rotation:** Implement **automatic secret rotation** and short-lived credentials.

---

<a id="stage-5-cicd-workflow-automation-attacks"></a>
### **Topic 5: CI/CD & Workflow Automation Attacks** — `🔬 Practical`

> [!TIP]
> **Goal:** Compromise the software supply chain and automation tier.

- [ ] **Pipeline Poisoning:** Inject malicious steps into **GitHub Actions/Jenkins** to alter builds, steal artifacts, or plant backdoors.

- [ ] **Dependency Confusion:** Publish **public packages** matching internal names to hijack build dependency resolution.

- [ ] **Workflow Takeover:** Exploit **workflow automation (n8n, Zapier, Workato)** misconfigs (e.g., **n8n CVE-2026-21858**) to pivot into **AWS/Azure**.

- [ ] **Credential Aggregation:** Treat automation platforms as **credential vaults**; dump **API keys, OAuth tokens, cloud creds** for lateral movement.

- [ ] **Build Artifact Integrity:** Enforce **signing (Sigstore/Cosign)** and **attestations (SLSA/Provenance)** to detect tampering.

---

<a id="lab-progression-part-25-container-orchestration-security"></a>
### **Lab Progression (Part 25: Container & Orchestration Security)**

> [!TIP]
> **Goal:** Practice container and Kubernetes security with real clusters, not diagrams.

- [ ] **Container Escape Awareness Lab:** Run a deliberately misconfigured container and document which Linux primitives made it unsafe: capabilities, mounts, namespaces, cgroups, seccomp, AppArmor/SELinux.
- [ ] **KubernetesGoat / k8s-ctf Lab:** Complete at least 5 Kubernetes attack scenarios and map each to a control failure.
- [ ] **Image Security Lab:** Build an image, scan it with Trivy/Grype, fix high-risk findings, and rebuild.
- [ ] **Secrets Lab:** Demonstrate unsafe secret exposure, then fix it using Kubernetes secrets, external secret managers, or workload identity.

---

<a id="stage-6-hypervisor-security"></a>

### **Topic 6: Hypervisor Security** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Understand the attack surface one layer below containers — the hypervisor. Container escape gets defender attention; hypervisor-level attacks are less understood and harder to detect. Enterprise pentests against virtualised infrastructure encounter these regularly.

- [ ] **VMware ESXi Attack Surface:** ESXi is the dominant enterprise bare-metal hypervisor. Key attack vectors:
  - **Unauthenticated ESXi Shell Access:** Legacy ESXi deployments may have SSH enabled with default or weak credentials (`root` / empty). `esxcli` and `vim-cmd` provide full VM management from the shell.
  - **vCenter Server Vulnerabilities:** vCenter (the management plane) has had critical unauthenticated RCE CVEs (CVE-2021-21985, CVE-2021-22005). A compromised vCenter = control over all managed ESXi hosts and all VMs.
  - **VMDK Credential Extraction:** Mount a VMDK file offline to extract credentials from Windows VMs: boot into recovery mode or use `7-zip` / `qemu-nbd` to mount and access the NTDS.dit/SAM + SYSTEM hive. This bypasses runtime protections entirely.
  - **Snapshot Credential Theft:** VM snapshots freeze memory state. A snapshot of a running Windows DC contains LSASS memory — mountable offline for credential extraction without triggering EDR.

- [ ] **Proxmox Attack Surface:** Open-source hypervisor used in SMBs and test environments:
  - Default API endpoint at `https://host:8006/api2/json` — enumerate with unauthenticated calls to identify version and nodes
  - Proxmox VE < 7.x had CSRF and auth bypass vulnerabilities
  - `pveum` and `qm` CLI allow full VM control from the Proxmox shell

- [ ] **VM Escape CVE Awareness:** True VM escapes (guest → hypervisor) are rare but high-value:
  - **VENOM (CVE-2015-3456):** QEMU virtual floppy disk controller buffer overflow — allowed guest-to-host escape on QEMU/KVM and Xen
  - **Escape via VMware Tools:** VMware Tools (running inside guest) has historically had privilege escalation and local escape vulnerabilities
  - **Shared Clipboard / Drag-and-Drop:** VMware and VirtualBox guest isolation can be broken via clipboard injection or shared folder misconfigurations

- [ ] **Nested Virtualisation Security:** Understand security implications of nested VMs (VM inside a VM): hypervisor isolation assumptions break down; snapshot-based lab environments using nested VMs may expose host credentials through nested VM memory.

- [ ] **Defensive Controls — Hypervisor Hardening:**
  - Enable lockdown mode on ESXi (restricts shell and API access to vCenter only)
  - Disable SSH on ESXi hosts in production; use vCenter for management
  - Enforce vCenter RBAC — no shared `administrator@vsphere.local` accounts
  - Network-segregate the management network (VMkernel port) from VM traffic
  - Enable VM encryption (vSphere VM Encryption) for sensitive VMs to prevent offline VMDK extraction

> [!IMPORTANT]
> **Move-On Gate:** Produce a Kubernetes hardening report with RBAC, network policy, admission control, image scanning, and runtime detection notes. Additionally, document: (1) two ESXi attack vectors and their mitigations, (2) how VMDK credential extraction works and what prevents it.

<a id="part-16-adversary-emulation-purple-teaming"></a>

---

<a id="module-22-adversary-emulation--purple-teaming"></a>
<a id="part-16-adversary-emulation-purple-teaming"></a>

## Module 22: Adversary Emulation & Purple Teaming


> [!NOTE]
> **Navigational Note — Why Part 16 Is Here:** Part 16 is the **Phase 6 Capstone** — it synthesizes all content from Parts 23–26 (Active Directory, Cloud, Containers, OT) into a unified adversary emulation exercise. It is numbered 16 because it was originally placed sequentially after Phase 3's Part 15 (OSINT & Threat Intelligence) in the roadmap's initial design. It belongs contextually in Phase 6 as the synthesis capstone of Parts 23–26. When you see cross-references to "Part 16" elsewhere in the roadmap, they refer to this section in Phase 6.


> [!WARNING]
> **Prerequisites:** This Part requires both offensive (Phase 2) AND defensive (Phase 3) maturity plus enterprise infrastructure knowledge from the Parts above (AD, Cloud, Containers, OT). Complete all prior Phase 6 content before attempting this. Purple teaming is the culmination of offense-defense integration at enterprise scale.

<a id="stage-1-mitre-attck-framework-mastery"></a>
### **Topic 1: MITRE ATT&CK Framework Mastery** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Understand the universal language of adversary behavior.

- [ ] **Tactic Familiarity:** Master all **14 tactics** (Initial Access → Impact) and their relationships in the attack lifecycle.

- [ ] **Technique Deep-Dive:** Study **100+ core techniques** with focus on **prevalence, detection difficulty, impact** ratings.

- [ ] **Sub-Technique Granularity:** Understand **sub-technique variations** for precise emulation (e.g., T1059.001 PowerShell vs T1059.003 CMD).

- [ ] **Data Source Mapping:** Link techniques to **detection data sources** (process creation, network traffic, registry modifications).

- [ ] **Mitigation Strategies:** Review **MITRE mitigations** for each technique to understand defensive controls.

---

<a id="stage-2-apt-threat-actor-emulation"></a>
### **Topic 2: APT & Threat Actor Emulation** — `🔬 Practical`

> [!TIP]
> **Goal:** Replicate real-world adversary campaigns.

- [ ] **APT Profiling:** Study **APT groups** (APT28, APT29, Lazarus, FIN7) including **TTPs, tools, targeting, infrastructure**.

- [ ] **Campaign Recreation:** Emulate **documented campaigns** step-by-step using **MITRE ATT&CK Navigator** for technique mapping.

- [ ] **Tool Replication:** Use **adversary tools** (Mimikatz, Cobalt Strike, Empire, custom malware) to match TTP fidelity.

- [ ] **Infrastructure Mimicry:** Build **attack infrastructure** (domains, IPs, C2) that mimics **APT patterns and behaviors**.

- [ ] **Operational Tempo:** Match **adversary dwell time, persistence patterns, exfil timing** for realistic simulation.

- [ ] **Adversary Emulation Plans:** Execute **MITRE ATT&CK Adversary Emulation Plans** for groups like **APT29, Scattered Spider** to test realistic kill chains.

---

<a id="stage-3-purple-team-exercises"></a>
### **Topic 3: Purple Team Exercises** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Collaborative offense-defense improvement.

- [ ] **Joint Planning:** Define **objectives, scope, techniques, success criteria** with both red and blue teams.

- [ ] **Live Detection Tuning:** Execute **attacks in controlled environment** while defenders **tune detection rules in real-time**.

- [ ] **Gap Analysis:** Identify **detection blind spots, control failures, response deficiencies** through collaborative testing.

- [ ] **Playbook Development:** Create **detection playbooks** with **queries, alerts, response procedures** for each emulated technique.

- [ ] **Iterative Improvement:** Run **multiple rounds** of testing with **incremental detection improvements** to measure progress.

---

<a id="stage-4-metrics-reporting"></a>
### **Topic 4: Metrics & Reporting** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Quantify security posture improvement.

- [ ] **Detection Coverage:** Calculate **% of ATT&CK techniques** with detection coverage across the matrix.

- [ ] **MTTD/MTTR:** Measure **Mean Time to Detect** and **Mean Time to Respond** for each technique tested.

- [ ] **False Positive Rate:** Track **alert accuracy** and **tuning effectiveness** over multiple exercises.

- [ ] **Control Effectiveness:** Rate **preventative, detective, responsive** controls against each technique (None/Partial/Full).

- [ ] **Trend Analysis:** Compare **metrics across time** to demonstrate **security maturity improvement**.

<a id="lab-progression-part-16-adversary-emulation-purple-teaming"></a>
### **Lab Progression (Part 16: Adversary Emulation & Purple Teaming)**

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Map a single APT group's TTPs to MITRE ATT&CK Navigator | ATT&CK heatmap export |
| 2 | Execute Atomic Red Team tests for 5 techniques in a lab | Detection results per technique |
| 3 | Run a full APT emulation plan (e.g., APT29) in lab | Emulation report with detection gaps |
| 4 | Build detection rules for each gap identified | Updated detection coverage matrix |
| 5 | Conduct a full purple team exercise with metrics | MTTD/MTTR report + improvement recommendations |

> [!IMPORTANT]
> **Move-On Gate:** You can execute adversary emulation plans, measure detection coverage, calculate MTTD/MTTR, and produce actionable purple team reports demonstrating security posture improvement.

---

<a id="toc-part-26-oticsscada-security"></a>
<a id="part-26-oticsscada-security"></a>


---

<a id="module-23-sniffing--spoofing"></a>
<a id="part-9-sniffing-spoofing"></a>

## Module 23: Sniffing & Spoofing


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `The Power of Scapy V2` — ARP spoofing, packet injection chapters — tool mastery for MitM and packet manipulation
> - 🟡 `Wireshark Cheat Sheet` — Keep open during all capture and analysis labs
> - 🟢 `Hacking and Network Defense` — Sniffing chapter — defender detection of sniffing activity (informs OPSEC)


<a id="stage-1-the-environment-fundamentals-the-setup"></a>

### **Topic 1: The Environment & Fundamentals (The Setup)** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Understand the battlefield. You cannot spoof what you cannot map.

- [ ] **Protocol Hierarchy & Trust:** Differentiate between **MAC Addresses** (Layer 2 - Local Trust) and **IP Addresses** (Layer 3 - Routing). Spoofing relies on exploiting the trust mismatch between these layers.

- [ ] **Secure vs. Insecure Protocols:** Identify targets using cleartext protocols like **HTTP, FTP, Telnet, DNS**. These are trivial to sniff. Encrypted protocols like **TLS/HTTPS** and **SSH** require advanced downgrade attacks or decryption to bypass.

- [ ] **The Switch vs. Hub Reality:** Modern networks use switches which segment traffic by MAC. You cannot passively sniff; you must **ARP spoof, MAC flood**, or **VLAN hop** to bypass segmentation.

- [ ] **Interface Configuration:** Configure NIC to **Promiscuous Mode** (tcpdump, Wireshark) to capture all traffic, not just destined to your MAC; practice with **monitor mode** on wireless cards.

- [ ] **Handshake & Session Logic:** Study **TCP/TLS handshakes** (SYN/ACK, ClientHello/ServerHello) to identify session boundaries; understand **sequence numbers, window size, timestamps** for **replay and hijack** timing.

---

<a id="stage-2-sniffing-passive-reconnaissance-the-ear"></a>

### **Topic 2: Sniffing & Passive Reconnaissance (The Ear)** — `🔬 Practical`

> [!TIP]
> **Goal:** Capture data without alerting the target. "Listen before act."

- [ ] **Passive Packet Capture:** Use **tcpdump/Wireshark** to capture broadcast/multicast traffic (ARP, DHCP, mDNS) to identify active hosts, gateways, and services without sending directed traffic.

- [ ] **Wireless Interception:** Set wireless NIC to **monitor mode**; capture **WPA2/WPA3 4-way handshakes, PMKID** for offline cracking; identify **SSID, client MAC, AP MAC** patterns.

- [ ] **Protocol Analysis:** Filter **pcap** by protocol (HTTP, FTP, SMTP, DNS); identify **cleartext credentials, API keys, session tokens**, and software **User-Agent/Server banners**.

- [ ] **Stream Reassembly:** Use **tcpflow, Wireshark Follow TCP Stream** to reassemble files, images, emails, or form submissions from fragmented packets.

---

<a id="stage-3-spoofing-active-deception-the-lie"></a>

### **Topic 3: Spoofing & Active Deception (The Lie)** — `🔬 Practical`

> [!TIP]
> **Goal:** Inject false information into the network to redirect or manipulate traffic.

- [ ] **ARP Spoofing:** Flood the network with **gratuitous ARP packets** linking your MAC to the **gateway IP**; forces the switch to route victim traffic through you; use **arpspoof, dsniff, b[ettercap](Tools/Ettercap.md)**.

- [ ] **DNS Spoofing:** Respond to **DNS queries faster than the legitimate server**; redirect victims to malicious login pages for **credential harvesting** or **malware distribution**.

- [ ] **DHCP Starvation & Rogue DHCP:** Exhaust legitimate DHCP pools and serve your own **gateway/DNS** to all clients; enables **MITM and traffic redirection**.

- [ ] **MAC Spoofing:** Change burned-in MAC to bypass **MAC filtering, NAC (Network Access Control), DHCP reservations**; use **macchanger** (Linux) or **SetMACAddress** (Windows).

- [ ] **IP Spoofing:** Forge **source IP** in packet headers to **hide identity, impersonate trusted hosts**, or launch **reflection/amplification attacks** in DDoS.

- [ ] **SSL Stripping & HTTP Downgrade:** Intercept **HTTPS traffic** and downgrade to **HTTP** by breaking the TLS handshake; use **sslstrip, mitmproxy** to expose encrypted traffic in cleartext.

---

<a id="stage-4-man-in-the-middle-exploitation-the-kill"></a>

### **Topic 4: Man-in-the-Middle & Exploitation (The Kill)** — `🔬 Practical`

> [!TIP]
> **Goal:** Intercept, modify, and relay traffic to extract or manipulate data.

- [ ] **MITM Positioning:** Establish yourself between victim and gateway via **ARP spoofing, DNS redirection, rogue DHCP, or rogue AP**; use **ettercap, mitmproxy, [Burp Suite](Tools/Burp_Suite.md)** to intercept and modify traffic in real-time.

- [ ] **Session Hijacking:** Extract **session cookies, JWT tokens, CSRF tokens** from sniffed **HTTP headers** and **POST bodies**; inject stolen tokens to impersonate user without password.

- [ ] **Credential Sniffing:** Capture **cleartext logins** (FTP, Telnet, HTTP Basic Auth, SMTP); extract **form credentials** from unencrypted POST requests.

- [ ] **Replay Attacks:** Capture valid **authentication tokens, API requests, or RF signals** and retransmit later to bypass time-based controls; works for **garage door openers, payment terminals, VoIP**.

- [ ] **Rogue Access Point / Evil Twin:** Deploy **fake Wi-Fi AP** with legitimate SSID + stronger signal; force users to connect and route all traffic through your box for **MITM harvesting**.

- [ ] **Traffic Injection & Modification:** Inject malicious **JavaScript, HTML, iframes** into unencrypted HTTP responses; modify **DNS responses** to redirect to attacker servers.

---

<a id="stage-5-defenses-mitigation-the-shield"></a>

### **Topic 5: Defenses & Mitigation (The Shield)** — `🧠 Conceptual`

- [ ] **Encryption & VPN:** Force all traffic through **TLS/HTTPS, IPSec VPN, or VPN tunneling**; renders sniffed payloads unreadable; watch for **HSTS, certificate pinning** as anti-bypass measures.

- [ ] **Switch-Level Protection:** **Dynamic ARP Inspection (DAI)**, **DHCP Snooping**, **port security** reject malformed ARP/DHCP; **802.1X authentication** prevents rogue device connection.

- [ ] **Network Segmentation:** **VLAN isolation, micro-segmentation, zero trust** limits sniffing scope per compromised segment; east-west traffic encryption adds extra layers.

- [ ] **Detection Systems:** **IDS/IPS** flag high ARP packet volume, **MITM tools (ettercap signatures)**, SSL downgrade attempts; **Netflow/sFlow** detects unusual traffic patterns.

- [ ] **User Awareness:** Train users to verify **SSL certificates**, recognize **phishing login pages**, and use **password managers** to avoid clipboard paste attacks.

<a id="lab-progression-part-9-sniffing-spoofing"></a>

### **Lab Progression (Part 9: Sniffing & Spoofing)**

| Level | Task                                                                       | Deliverable                               |
| ----- | -------------------------------------------------------------------------- | ----------------------------------------- |
| 1     | Capture traffic with Wireshark in a home lab (HTTP, FTP, DNS)              | Annotated pcap with credential extraction |
| 2     | Perform ARP spoofing + MITM with [Bettercap](Tools/Bettercap.md) in lab | Screenshot of intercepted traffic         |
| 3     | Execute DNS spoofing to redirect lab traffic to phishing page              | DNS spoof lab report                      |
| 4     | Perform SSL stripping against a lab web server without HSTS                | Before/after traffic comparison           |
| 5     | Full MITM chain: ARP spoof → DNS redirect → credential capture             | End-to-end MITM lab report                |

> [!IMPORTANT]
> **Move-On Gate:** You can perform a complete MITM attack chain in a lab, capture credentials from unencrypted and downgraded traffic, and explain exactly which defenses (DAI, HSTS, certificate pinning) would have prevented each technique.

---

---

---

<a id="toc-part-10-social-engineering"></a>


---

<a id="module-24-social-engineering"></a>
<a id="part-10-social-engineering"></a>

## Module 24: Social Engineering


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `Social Engineering The Art of Human Hacking` — The definitive book on SE — read this fully during Part 10
> - 🟡 `The Social Engineers Playbook` — Full (short) — practical tactical scripts and pretexts


> **Safety Gate:** Social engineering practice must use consented simulations only. Do not target real people, employers, classmates, public organizations, or family accounts. Unauthorized phishing and impersonation are not "practice"; they are operational and legal exposure.

<a id="stage-0-the-psychology-of-social-engineering"></a>
<a id="stage-0-the-psychology-of-social-engineering-the-foundation"></a>

### **Topic 0: The Psychology of Social Engineering (The Foundation)** — `🧠 Conceptual`

> [!IMPORTANT]
> **Read this before any other Stage in Part 10.** Social engineering is not a collection of clever tricks — it is applied psychology. Every phishing email, vishing call, and pretexting scenario works because it exploits specific, documented cognitive patterns. Understanding these patterns is what separates an operator who succeeds from one who improvises and fails. Defenders must also understand them to design effective awareness training.

> [!TIP]
> **Goal:** Understand the psychological machinery that makes humans predictable under social engineering pressure.

**Cialdini's 6 Principles of Influence (The SE Attacker's Toolkit)**

Robert Cialdini's research on influence identified six universal principles that attackers weaponize. Know each one, recognize it in real-world phishing/pretexting scenarios, and understand both the offensive use and the defensive countermeasure:

- [ ] **1. Reciprocity:** People feel obligated to return favors. Attackers exploit this by sending small gifts, providing helpful information, or doing something "nice" before making a request. Example: Attacker sends a "free" IT tool or helps with a minor problem, then requests access credentials as a natural follow-up.
  - _Defensive awareness:_ Question why an unsolicited party is offering help. Favors from unknown parties are often hooks.

- [ ] **2. Commitment & Consistency:** Once a person commits to something (even trivially), they are psychologically compelled to behave consistently with that commitment. Attackers use small initial requests ("Could you confirm your department?") to build toward larger ones. Example: Foot-in-the-door technique — escalating from harmless questions to credential requests.
  - _Defensive awareness:_ Recognizing that you've agreed to small requests from someone does not obligate you to agree to larger, unusual ones.

- [ ] **3. Social Proof:** People look at what others are doing to determine correct behavior, especially in uncertain situations. Attackers fabricate social proof: "Everyone on your team has already verified their account" or "The CISO approved this procedure." Example: Mass-phishing emails claiming widespread adoption of a fake security update.
  - _Defensive awareness:_ Verify claims of "everyone is doing it" through independent channels — not through links or numbers provided by the requester.

- [ ] **4. Authority:** People comply with perceived authority figures — especially in professional environments. Attackers impersonate executives (CEO fraud/BEC), IT helpdesk, auditors, law enforcement, or regulators. Example: "This is John from IT Security. We detected suspicious activity on your account. I need your current password to verify."
  - _Defensive awareness:_ Real authority figures with legitimate needs never require your password. Verify identity through a known, independent channel before complying.

- [ ] **5. Liking:** People are more likely to comply with requests from people they like or who are similar to them. Attackers build rapport, mirror body language, reference shared interests, claim mutual connections, use flattery. Example: LinkedIn profile mining to find shared connections and mention them in a phishing email to build perceived familiarity.
  - _Defensive awareness:_ Likeability is not trust. A pleasant, familiar-seeming contact can be a well-prepared attacker.

- [ ] **6. Scarcity:** Perceived scarcity creates urgency that bypasses rational decision-making. "This offer expires in 10 minutes," "Your account will be suspended in 24 hours," "Only you can fix this." Urgency is the primary switch that disables critical thinking. Example: Phishing emails with countdown timers or imminent threat messaging.
  - _Defensive awareness:_ Real systems with legitimate urgency allow time for verification. Artificial urgency is a psychological weapon — slow down when you feel rushed.

---

**Cognitive Biases Exploited in Social Engineering**

- [ ] **Urgency Bias (System 1 Thinking):** Under time pressure, humans switch from deliberate analytical thinking (System 2) to fast, pattern-matching intuition (System 1). Attackers manufacture urgency to prevent System 2 thinking. Countermeasure: Organizations should establish policies that require verification delays for unusual requests regardless of stated urgency.

- [ ] **Authority Bias:** The tendency to trust and obey authority figures. Manifests as compliance with requests from anyone displaying authority markers (uniform, title, confident tone). Particularly effective via email where visual deception is easy.

- [ ] **Familiarity/Exposure Effect:** Mere repeated exposure to a name, brand, or scenario increases trust in it. Attackers send "drip" campaigns — multiple low-pressure contacts before the actual attack — to build familiarity before the high-pressure request.

- [ ] **In-Group Bias:** People are more cooperative with members of their perceived in-group. Attackers research corporate culture, use internal jargon, name-drop colleagues, and reference recent company events to establish perceived membership. LinkedIn, Glassdoor, job postings, and conference agendas are primary intelligence sources for this.

- [ ] **Fear of Negative Consequence:** The threat of something bad happening (job loss, account suspension, legal action, IT lockout) overrides rational verification behavior. Attackers combine authority + scarcity + threat in "warning emails" from fake IT/HR/legal.

---

**Pretext Construction Methodology**

- [ ] **Pretext Definition:** A pretext is a fabricated scenario, identity, and backstory that the attacker uses to justify the unusual request they are making. A strong pretext is internally consistent, draws on real intelligence about the target, and anticipates objections.

- [ ] **Pretext Construction Framework:** A professional pretext must answer five questions before deployment:
  1. **Who am I?** (role, organization, relationship to target)
  2. **Why am I contacting this person?** (plausible reason grounded in reality)
  3. **What am I asking for?** (specific, reasonable-sounding request)
  4. **Why now?** (urgency rationale that doesn't trigger suspicion)
  5. **What objections might arise, and what is my answer?** (anticipate resistance)

- [ ] **Pretext Intelligence Requirements:** A pretext draws from real OSINT:
  - Employee names, titles, reporting structure (LinkedIn, company website)
  - Recent company events, announcements, projects (press releases, social media)
  - Technology stack used (job postings reveal software in use)
  - Corporate language, acronyms, cultural references (Glassdoor, LinkedIn posts)
  - Physical location details (office address, badge vendor, building layout)

- [ ] **Persona Maintenance:** Once deployed, a pretext must be maintained consistently. Common operator failure: deviating from the stated identity under pressure or failing to answer follow-up questions consistently. A strong pretext is rehearsed, not improvised. Practice the pretext scenario out loud before deployment.

- [ ] **Pretext Failure Modes:** Know what causes pretexts to collapse:
  - Using insider jargon incorrectly (calls out external nature)
  - Unable to answer natural follow-up questions
  - Requesting information that the stated role wouldn't need
  - Inconsistency between email domain, phone number, and stated identity
  - Targets who independently verify through official channels (the defense)

---

<a id="stage-1-intelligence-reconnaissance-the-setup"></a>

### **Topic 1: Intelligence & Reconnaissance (The Setup)** — `🔬 Practical`

> [!TIP]
> **Goal:** Know the target better than they know themselves.

- [ ] **Digital Recon:** Execute **OSINT** using **Google Dorks, LinkedIn scraping, GitHub dorking** to extract employee names, emails, roles, tech stacks, and company structure.

- [ ] **Physical Recon:** Perform **dumpster diving** to recover **org charts, vendor invoices, sticky notes** with passwords; observe **badge access patterns, delivery procedures**.

- [ ] **Domain & Infrastructure Prep:** Register **typo-squatting domains** (e.g., `companysupport.com`, `company-login.net`) that mimic target portals; prepare **phishing landing pages**.

- [ ] **Social Media Profiling:** Mine **LinkedIn, Twitter, GitHub, Glassdoor** for **personal details, relationships, job changes** to craft personalized lures.

---

<a id="stage-2-the-digital-assault-remote-vectors"></a>

### **Topic 2: The Digital Assault (Remote Vectors)** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Compromise the target from a distance via electronic channels.

- [ ] **Mass Campaign:** Launch **broad phishing campaigns** with generic lures (password resets, package delivery) for large-scale **credential harvesting**.

- [ ] **Executive Targeting:** Execute **whaling attacks** against **C-suite/CFO** using deep **OSINT context** (recent news, personal interests, vendor relationships) to bypass skepticism.

- [ ] **Mobile Vector:** Deploy **SMS phishing (smishing)** with **MFA reset codes, delivery notifications, bank alerts**; use **VoIP/voice phishing (vishing)** to call employees directly.

- [ ] **Watering Hole:** Compromise **industry-specific forums, GitHub repos, or shared tools** to inject **malware/tracking code** that targets specific teams via **drive-by downloads**.

- [ ] **Deepfake Vishing:** Use **voice cloning/video deepfakes** (e.g., ElevenLabs) for **executive impersonation** in calls/meetings.

- [ ] **ClickFix/ClearFake:** Simulate browser/OS errors that instruct users to **copy-paste provided PowerShell/terminal scripts** ("fix/update now").

- [ ] **Email Authentication Bypass (DMARC/DKIM/SPF Offensive):** Understand how to send convincing email as or near a target domain, bypassing authentication controls:
  - **DMARC alignment bypass:** DMARC passes when the From header domain _aligns_ with either the SPF envelope-from or the DKIM signing domain. A target with `p=quarantine` but no subdomain policy (`sp=none`) allows subdomain spoofing — register `mail.target.com` and send from a subdomain not covered by the DMARC policy.
  - **Missing DMARC / weak p=none:** Check with `dig TXT _dmarc.target.com` — if the record is absent or `p=none`, the domain can be directly spoofed without filtering. Use [dmarc.postmarkapp.com](https://dmarc.postmarkapp.com) or `checkdmarc` to scan targets during recon.
  - **Homoglyph domains:** Register visually identical domains using Unicode lookalike characters (e.g., `Ⅰ` for `l`, `а` for `a`). IDN homoglyph attack: `xn--paypl-h2a.com` renders as `payрal.com` in some email clients. Tools: `dnstwist` with `--registered` flag.
  - **Subdomain takeover for mail spoofing:** If a dangling CNAME on a target subdomain points to an unclaimed third-party service (SendGrid, Mailchimp, GitHub Pages), claim the service and send email from that subdomain. It passes SPF and DKIM because it is a legitimate sending service now controlled by you.
  - **Spoofed display names:** Many mail clients show only the display name, not the From address. `"CEO Name <attacker@random.com>"` passes all authentication controls and appears as CEO to a mobile viewer. Combine with similar-looking reply-to addresses.
  - **SPF softfail exploitation:** A `~all` SPF record (softfail) means DMARC still evaluates — but many recipients accept softfail-flagged mail if DMARC is absent or `p=none`.
  - **Defensive counter-reference:** See Phase 3 Part 14 Stage 6 for the defender-side SPF/DKIM/DMARC configuration and detection.

---

<a id="stage-3-the-human-element-direct-interaction"></a>

### **Topic 3: The Human Element (Direct Interaction)** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Use psychology and social manipulation to bypass logic.

- [ ] **Voice Pretexting:** Call as **IT support, HR, vendor, auditor, law enforcement** using social engineering pretexts; use **authority, urgency, fear** to bypass critical thinking.

- [ ] **Authority & Compliance Trigger:** Leverage **IT/Security/Auditor/Legal persona** to demand compliance; abuse **helpfulness bias** to force password resets or system access.

- [ ] **Reciprocity & Obligation:** Provide small **favors (tech help, free tools)** to create sense of obligation; ask for credentials or access in return.

---

<a id="stage-4-the-physical-breach-boots-on-the-ground"></a>

### **Topic 4: The Physical Breach (Boots on the Ground)** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Gain physical access to networks and facilities.

- [ ] **Tailgating:** Follow **authorized employees** into secure zones using badges/access cards; use **coffee cup hold, uniform/vendor persona** to bypass visual checks.

- [ ] **Shoulder Surfing:** Observe **PIN entry, password typing, screen content** in public spaces (airports, coffee shops, open offices) to capture credentials.

- [ ] **Badge Cloning:** Capture **RFID badge data** using **Proxmark3, ACR122U** and clone to malicious card; bypass **magnetic stripe readers** via cloning.

- [ ] **Physical Device Placement:** Plant **USB drops, rogue access points, hardware keyloggers** in common areas for **auto-execution** when connected by unsuspecting users.

---

<a id="stage-5-defense-awareness-the-shield"></a>

### **Topic 5: Defense & Awareness (The Shield)** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Prevent the human hack through training and controls.

- [ ] **Authentication:** Enforce **MFA/2FA** (TOTP, hardware keys, push notifications) so password compromise alone doesn't grant access; watch for **MFA fatigue attacks**.

- [ ] **Verification Protocols:** Train staff to **challenge unknown callers** via **secondary channel callback**; never trust caller ID alone; verify requests through official channels.

- [ ] **Physical Security:** Enforce **no-tailgating policies, visitor escorts, badge display requirements, clean desk policies** to prevent **dumpster diving and shoulder surfing**.

- [ ] **Security Awareness:** Regular **phishing simulations, red team testing, security training** to build **skepticism and reporting culture**; reward **security-first behavior**.

- [ ] **MFA Resilience:** Teach differences between **phishing-resistant MFA (FIDO2/Passkeys)** vs **phishable MFA (SMS/Push/OTP)**; test and mitigate **MFA fatigue** scenarios.

<a id="lab-progression-part-10-social-engineering"></a>

### **Lab Progression (Part 10: Social Engineering)**

> [!TIP]
> **Goal:** Learn social engineering defensively and ethically.

- [ ] **Email Authentication Lab:** Configure and validate SPF, DKIM, and DMARC on a test domain or lab mail stack.
- [ ] **Header Forensics Lab:** Analyze benign/phishing email headers and identify sender path, SPF/DKIM/DMARC result, and suspicious infrastructure.
- [ ] **[GoPhish](Tools/GoPhish.md) Simulation Lab:** Run a consented internal lab campaign against test inboxes only; measure open/click/report rates.
- [ ] **Pretext Review:** Write three pretexts and then write the defensive awareness guidance that would defeat them.
  > [!IMPORTANT]
  > **Move-On Gate:** Produce a social-engineering simulation plan with ROE, consent model, metrics, and debrief template.

---

---

<a id="toc-part-11-denial-of-service"></a>
<a id="part-11-denial-of-service"></a>


---

<a id="module-25-malware--weaponization-conceptual"></a>
<a id="part-8-malware-weaponization"></a>

## Module 25: Malware & Weaponization (Conceptual)


> **Safety Gate:** Malware work is restricted to isolated local labs with snapshots, host-only networking, no shared clipboard, no mounted host folders, and no third-party targets. Before running any sample or payload, define expected behavior, logging sources, rollback steps, and containment checks.

> [!NOTE]
> **Scope of This Part — Read Carefully:** This Part teaches malware as a **survey course**, not an implementation course. At this stage you have not yet studied how malware works at the binary/code level — that knowledge comes in **Part 28 (Reverse Engineering & Malware Analysis, Phase 7)**. Without that foundation, any malware you write will be a copy-paste artifact you cannot debug, fix, or adapt when it fails (and it will fail).
>
> **What IS covered here (practitioner-level):**
>
> - Malware taxonomy and attack lifecycle (categories, architecture decisions, C2 design thinking)
> - Tool-based weaponization: `msfvenom`, Metasploit payload generation, framework-managed C2 (Sliver, Mythic)
> - How AV/EDR detects malware conceptually (signature, heuristic, behavioral scanning)
> - Document and cloud delivery vectors — the initial access tradecraft that red teamers use operationally
>
> **What Stages 2–5 teach (exposure-level, not implementation-level):**
> Stages 2, 3, 4, and 5 describe techniques — shellcode injection, EDR bypass, anti-forensics — at the level of _what they are and how they work conceptually_. They are not implementation labs. Each of those stages carries an explicit `[!WARNING]` marker. When you see that marker: understand the concept, understand what defenders see, move on. Do **not** attempt custom code implementation until you have completed **Part 28 (RE & Malware Analysis)** and **Part 42 (Offensive Development, Phase 7)**.
>
> **Why this sequencing matters:** Students who attempt custom malware engineering before Part 28 produce tools they cannot debug, cannot evade EDR reliably, and cannot modify under time pressure. The correct sequence is: _understand the attack here (Part 8) → understand binaries and malware internals (Part 28) → build your own tooling (Part 42)._

<a id="stage-1-the-design-logic-architecture"></a>

### **Topic 1: The Design & Logic (Architecture)** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Understand how malware is architected at a design level — the decisions an attacker makes before writing a single line of code.

- [ ] **Target the CIA Triad:** Define the malware's objective — does it attack **Confidentiality** (RAT, spyware, credential harvester), **Integrity** (wiper, data corruption), or **Availability** (ransomware, DDoS bot)? The objective drives every architectural decision.

- [ ] **Malware Taxonomy:** Understand the full taxonomy — **dropper, loader, stager, RAT, rootkit, worm, ransomware, wiper, infostealer, spyware, adware, botnet agent** — and how each category relates to the attack lifecycle phase it serves.

- [ ] **C2 Protocol Selection:** Understand the trade-offs between **HTTP/S beaconing, DNS tunneling, ICMP covert channels, and legitimate SaaS API abuse** — not to implement them at this stage, but to understand why attackers choose one over another based on network visibility risk. Implementation comes in Part 42.

- [ ] **Persistence Architecture:** Survey the persistence mechanisms available — **registry run keys, scheduled tasks, WMI subscriptions, DLL hijacking, boot sector** — understand their detection footprint differences conceptually. Implementation and lab practice comes in Part 7 (system hacking) and Part 42.

- [ ] **Kill Chain Mapping:** Use the **Cyber Kill Chain** or **MITRE ATT&CK** to map a hypothetical malware campaign from **Reconnaissance → Weaponization → Delivery → Exploitation → Installation → C2 → Actions on Objectives**. This mapping exercise trains your mind to think like an attacker planning a campaign, not just using a tool.

- [ ] **Diamond Model:** Apply the **Diamond Model** to a real APT's malware — adversary, capability, infrastructure, victim — to understand why the same malware capability looks different depending on the targeted victim sector.

---

<a id="stage-2-the-payload-mechanism-weaponization"></a>

### **Topic 2: The Payload & Mechanism — Exposure Survey** — `🧠🔬 Mixed`

> [!WARNING]
> **Exposure-Only Stage:** This stage describes weaponization techniques at a conceptual level. Do not attempt to implement custom payloads, shellcode injection, or custom C2 until you have completed **Part 28 (Reverse Engineering & Malware Analysis, Phase 7)** and **Part 42 (Offensive Development, Phase 7)**. Your goal here is to understand _what_ these techniques do and _why_ defenders flag them — not to build them.

> [!TIP]
> **Goal:** Understand how payloads execute and what defenders detect at each stage.

- [ ] **Memory-Based Execution:** Understand that attackers inject code into running processes (shellcode injection, process hollowing, DLL injection) to avoid writing to disk and evade file-scanning AV. _Conceptual understanding only — implementation in Part 42._

- [ ] **Delivery Vectors:** Understand **phishing, drive-by download, watering hole, and supply chain injection** as the four primary delivery mechanisms; know what each one requires from the attacker and what it looks like to defenders. _Practical delivery lab in Stage 6 (document weaponization) below._

- [ ] **Staged Payload Architecture:** Understand the difference between **stageless** (one-shot complete payload) and **staged** (stager fetches the full payload at runtime) delivery — know why staged reduces initial payload size but requires an active C2 listener. Use `msfvenom` to generate both and compare their byte sizes and detection rates against VirusTotal (educational only — never upload customer/lab-specific payloads).

- [ ] **Framework-Managed C2:** Deploy **[Sliver](Tools/Sliver.md)** or **Mythic** in your lab, generate an implant, and establish a callback — understand listener configuration, sleep/jitter tuning, and how traffic patterns affect detection. This is the operational-tool-based weaponization that is in scope at this stage.

> **🔬 Observation Lab (Stage 2):** Run EICAR test file (`https://www.eicar.org/download/eicar.com`) through VirusTotal and note detection rate. Then generate an msfvenom stageless payload (`msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=127.0.0.1 LPORT=4444 -f exe -o stageless.exe`) and a staged payload (`msfvenom -p windows/x64/meterpreter/reverse_tcp LHOST=127.0.0.1 LPORT=4444 -f exe -o staged.exe`). Compare: (1) file sizes, (2) VirusTotal detection rates for both. Record which AV engines flag them and whether detections are signature-based or heuristic. Never execute either payload outside a controlled lab VM with no network access.

---

<a id="stage-3-evasion-defense-bypassing-invisibility"></a>

### **Topic 3: Evasion & Defense Bypassing — Exposure Survey** — `🧠 Conceptual`

> [!WARNING]
> **Exposure-Only Stage:** This stage teaches _how_ AMSI bypass, EDR hook removal, and memory-based evasion work at a conceptual level. Do not attempt to implement these at this stage. Custom evasion requires understanding the Windows internals that these techniques exploit — that knowledge is in **Part 28 (Reverse Engineering & Malware Analysis)**. Practical evasion implementation is in **Part 42 (Offensive Development, Phase 7)**.

> [!TIP]
> **Goal:** Understand how the defensive stack detects malware and what attackers do to evade each layer.

> **Prerequisite Context:** This stage references AMSI, EDR, and ETW. Those systems are covered from the defender's perspective in **Phase 3 (Part 13A: Stages 3–5)**. If you have not completed Phase 3 yet, read those stages before studying evasion — evasion without understanding the detection model is guesswork.

- [ ] **Static Analysis Evasion:** Understand that AV signature detection works by matching known byte patterns — attackers evade it by changing the binary (packing, encoding, obfuscation). Know _that_ this works conceptually; implementing a custom packer requires PE format knowledge from Part 28.

- [ ] **Sandbox Detection:** Understand that sandboxes run samples in controlled VMs — attackers detect this by checking for VM artifacts (driver names, low CPU count, no mouse movement), then go dormant. Know the technique; study the implementation in Part 28.

- [ ] **EDR Userland Hooking Bypass:** Understand that EDR products hook Windows API functions at userland to intercept suspicious calls — attackers bypass this by calling syscalls directly or by unhooking. _Conceptual understanding only — syscall implementation in Part 42._

- [ ] **Memory-Based Evasion Concepts:** Understand _what_ sleep obfuscation, call stack spoofing, and indirect syscalls do — each is a technique that makes a beacon harder to detect during memory scanning. Implementation and lab practice in Part 42.

> **🔬 Observation Lab (Stage 3):** In a Windows sandbox VM: (1) Run `Procmon` (Sysinternals), filter on `powershell.exe`. Execute `powershell -Command "Write-Host hello"` and observe the API calls. Now run `powershell -EncodedCommand` with a base64-encoded version of the same command. Compare the Procmon output — same result, different invocation path. This is the "encoded = suspicious" detection signal that AMSI catches. Document what `ScriptBlock Logging` Event ID 4104 shows for each.

---

<a id="stage-4-persistence-escalation-entrenchment"></a>

### **Topic 4: Persistence & Escalation — Exposure Survey** — `🧠 Conceptual`

> [!WARNING]
> **Exposure-Only Stage:** Persistence mechanisms and privilege escalation are taught as canonical practitioner skills in **Part 7 (System Hacking, Phase 2)** already. This stage reviews them in the context of malware architecture — what a long-running implant uses to survive reboots and credential rotations. Rootkit-level persistence (BOOTKIT, UEFI implants, kernel drivers) requires kernel internals knowledge from Part 28. Do not attempt rootkit implementation at this stage.

> [!TIP]
> **Goal:** Understand what persistence mechanisms a malware implant uses and why each has a different detection footprint.

- [ ] **Userland Persistence Review:** Map the common mechanisms — **registry run keys, scheduled tasks, WMI subscriptions, DLL search order hijacking, Startup folder, COM object hijacking** — to their Windows Event Log artifacts (which Event IDs indicate each mechanism was set). This is the defender-aware review; you practiced them in Part 7.

- [ ] **Privileged Persistence Concepts:** Understand that kernel-level and UEFI-level persistence (bootkits, driver implants) exist and require privileged access plus deep OS internals knowledge — covered in Part 28. Recognizing their artifacts is the skill to acquire here.

- [ ] **Defense Disabling (Conceptual):** Understand that advanced malware terminates AV/EDR processes or disables tamper protection when running as SYSTEM — recognizing this behavior in logs is the defender-relevant skill; the implementation is in Part 42.

> **🔬 Observation Lab (Stage 4):** In a Windows sandbox VM with Sysmon installed: (1) Create a scheduled task with `schtasks /create /sc onlogon /tn "Updater" /tr "calc.exe"`. (2) Open Event Viewer → Applications and Services Logs → Microsoft → Windows → TaskScheduler → Operational. Find the task creation event (Event ID 106). Document: what the event records, what fields an analyst would use to detect malicious scheduled tasks, and what `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` looks like in Autoruns. Delete the task when done.

---

<a id="stage-5-counter-forensics-professionalism-the-cleanup"></a>

### **Topic 5: Counter-Forensics & Cleanup — Exposure Survey** — `🧠 Conceptual`

> [!WARNING]
> **Exposure-Only Stage:** Anti-forensics (log manipulation, timestamp modification, artifact scrubbing) are covered conceptually here. Implementing effective anti-forensics requires understanding _what_ forensic artifacts exist — that knowledge is in **Part 27 (Digital Forensics, Phase 7)**. The skill to develop here is recognizing what evidence an attacker would try to destroy, so you can look for its _absence_ during an investigation. Operationally, within a legitimate red team engagement, artifact cleanup must stay within Rules of Engagement and must never destroy evidence on production systems.

> [!TIP]
> **Goal:** Understand what artifacts malware and operators leave behind, and what attackers do to reduce their forensic footprint.

- [ ] **Windows Artifact Landscape:** Know the key artifacts that survive after an attack — **Windows Event Logs, Prefetch files, Shimcache, Amcache, LNK files, MFT records, browser history, $MFT journal, registry hives** — and understand which artifacts survives a reboot, a log clear, or a disk wipe.

- [ ] **Log Manipulation Awareness:** Understand that attackers clear Event Logs using `wevtutil cl System` and that this clearing _itself_ generates Event ID 1102 (Security log cleared) — defenders look for the clearing event, not just empty logs. Also understand that SIEMs receive log forwarding — clearing local logs after a SIEM has already ingested them accomplishes nothing.

- [ ] **Anti-Forensics Counter-Detection:** Know the defender techniques that defeat anti-forensics: **Write-Protect + Memory Forensics (Volatility)**, **SIEM log forwarding**, **EDR telemetry that bypasses local log clearing**, **backup snapshot retention**, and **network forensic reconstruction from PCAP**.

- [ ] **ROE Compliance:** In a red team engagement, anti-forensics and log cleanup are controlled by Rules of Engagement — know exactly what your RoE permits before touching any log or artifact, and never destroy data on production systems regardless of privilege level.

> **🔬 Observation Lab (Stage 5):** In a Windows sandbox VM: (1) Run `wevtutil cl Security` to clear the Security event log. Open Event Viewer and confirm the log is empty. Now check the same Security log — observe Event ID 1102 ("The audit log was cleared"). (2) Open PowerShell history file (`%APPDATA%\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt`) and note what is logged. Delete one entry manually — run `Get-History` in a new session and compare. Document: which artifacts survived the clearance attempt and what a defender reviewing logs 5 minutes after the clear would still find.

---

<a id="stage-5b-windows-persistence-memory-forensics"></a>

### **Topic 5b: Windows Persistence Analysis & Memory Forensics** — `🧠 Conceptual`

> [!NOTE]
> **Scope:** This is a conceptual exposure pass — you learn what the techniques are and what artifacts they leave so you can identify them on an engagement or in a blue-team investigation. Deep Volatility memory analysis and advanced rootkit internals are covered post-hire in Shelf S21 (Advanced Windows Internals).

> [!TIP]
> **Goal:** Know every common Windows persistence location an attacker would use, the forensic artifact each produces, and the Volatility plugin or Sysinternals tool that surfaces it.

**Windows Persistence Mechanisms (with detection artifacts):**

- [ ] **Registry Run Keys:** `HKCU\Software\Microsoft\Windows\CurrentVersion\Run`, `HKLM\...\Run`, `RunOnce`, `RunServices`. Detection: Autoruns.exe (Sysinternals), reg query output, Sysmon Event ID 13 (registry value set), Windows Event 4657.

- [ ] **Scheduled Tasks:** `schtasks /create` or via Task Scheduler XML dropped to `C:\Windows\System32\Tasks\`. Detection: `schtasks /query /fo LIST /v`, Sysmon Event ID 1 (process create), Windows Event ID 4698 (scheduled task created), 4702 (modified).

- [ ] **Windows Services:** `sc create EvilSvc binPath= "C:\backdoor.exe" start= auto`. Detection: `sc query`, Windows Event ID 7045 (new service installed), 4688 (process created with SYSTEM token from service).

- [ ] **DLL Search Order Hijacking (Persistence variant):** Place a malicious DLL in a directory searched before the legitimate DLL location for a service/application that auto-starts. Detection: Process Monitor (DLL load events), Sysmon Event ID 7 (image loaded), comparing DLL path against known-good baselines.

- [ ] **WMI Event Subscriptions:** Create `__EventFilter` + `CommandLineEventConsumer` + `__FilterToConsumerBinding` — survives reboots, no registry or file drop required if using "fileless" WMI subscriptions. Detection: `Get-WMIObject -Namespace root\subscription -Class __EventFilter`, Sysmon Event ID 19/20/21 (WMI activity), Windows Event 5861.

- [ ] **Startup Folder Persistence:** Drop a LNK or executable into `C:\Users\<user>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup` or the system-wide equivalent. Detection: Autoruns, directory listing with timestamps, Sysmon Event ID 11 (file created).

- [ ] **Boot/Pre-OS Persistence:** Awareness only — bootkit, MBR/VBR overwrites, UEFI implants. Not lab-practiced at this stage. Detect via: offline bootable scanner, Secure Boot attestation, TPM measurement comparison.

**Windows Memory Forensics (Conceptual — Volatility awareness):**

- [ ] **Why Memory Forensics:** Many advanced threats (fileless malware, in-memory shellcode, process injection) leave minimal or no disk artifacts. Memory forensics captures the running state: process list, network connections, injected code, decrypted credentials, and encryption keys that never touch disk.

- [ ] **Key Volatility 3 Plugins to know:**
  - `windows.pslist` / `windows.pstree` — list running processes and their parent/child relationships; look for orphaned processes or unusual parent-child pairs (e.g., `Word.exe` spawning `cmd.exe`)
  - `windows.cmdline` — show command-line arguments for each process; reveals powershell `-EncodedCommand` or suspicious flags
  - `windows.netscan` — active and recently closed network connections from memory; catches C2 callbacks that are not in `netstat` anymore
  - `windows.dlllist` — DLLs loaded per process; look for DLLs loaded from `%TEMP%`, `%APPDATA%`, or unusual paths
  - `windows.malfind` — scan process memory for regions that are `PAGE_EXECUTE_READWRITE` and contain PE headers or shellcode signatures — primary plugin for detecting injected shellcode
  - `windows.handles` — open handles per process; reveals processes holding handles to suspicious files, registry keys, or mutexes
  - `windows.dumpfiles` / `windows.procdump` — extract files and process executables from memory for static analysis

- [ ] **Memory Acquisition:** Understand the difference between live acquisition (`winpmem`, `DumpIt`, `RAMMap`) vs. crash dump (`%SystemRoot%\MEMORY.DMP`) vs. hibernation file (`hiberfil.sys`). Know that `hiberfil.sys` and `pagefile.sys` contain memory artifacts even without a live acquisition tool.

- [ ] **Lab (Conceptual):** Download a pre-made memory image from [MemLabs](https://github.com/stuxnet999/MemLabs) or [Volatility Foundation samples](https://github.com/volatilityfoundation/volatility/wiki/Memory-Samples). Run `windows.pslist`, `windows.malfind`, and `windows.netscan` on it. Document what looks suspicious and why. This is awareness-level — you are learning to read the output, not yet building full DFIR investigation workflows (that is Shelf S04 / Stage-5 parallel).

---



### **Topic 6: Document & Cloud Weaponization** — `🔬 Practical`

> [!TIP]
> **Goal:** Weaponize documents, email clients, and cloud services for initial access, persistence, and exfiltration. This is the **operational implementation stage** for Part 8 — the techniques here are in-scope for lab practice because they use documented attack patterns that do not require binary internals knowledge.

> **Prerequisite:** Complete Part 7 (System Hacking), Part 9 (Sniffing & Spoofing), and Part 10 (Social Engineering) before this stage.

**Office & Document Exploits:**

- [ ] **VBA & XLM 4.0 Macros (Legacy — Declining):** Understand VBA macro payload construction and template injection (`remote DOTM`) — note that **Microsoft's February 2022 change blocks VBA macros from internet-sourced Office files by default** across Office 365 and 2019/2021. Macro-based delivery is now uncommon in phishing campaigns without specific user interaction (Enable Content prompt). Know the technique; prioritize modern alternatives below.

- [ ] **HTML Smuggling (Current Primary Vector):** Build HTML files that use the **`Blob` API and `createObjectURL`** to reconstruct a payload inside the browser, bypassing email gateway and web proxy file-type scanning. HTML smuggling now accounts for a significant proportion of red team initial access because attachments are not downloaded — they are assembled client-side. Practice building a minimal smuggler that delivers an EXE or ZIP without triggering gateway inspection.

- [ ] **OneNote/PDF/Embedded Files (Current Vector):** Weaponize **OneNote pages** (`.one` files with embedded scripts triggered by click), **PDF JavaScript** for opener execution, and **ISO/IMG container files** that bypass MOTW (Mark of the Web) on older Windows builds. Understand the **MOTW bypass path** (ISO → LNK → Script) and why Microsoft's October 2022 patches partially closed it.

- [ ] **DDE & Template Abuse:** Trigger code via **DDEAUTO**, external DOTM template injection, and **Follina-style** (`CVE-2022-30190`) URL template fetch — understand the patch status of each and what still fires in unpatched environments.

- [ ] **Browser-in-the-Browser (BitB) Attacks:** Build a **fake browser pop-up window** inside a legitimate page that mimics an SSO login dialog — bypasses awareness training because the URL displayed looks authentic. No code execution required; credentials are harvested directly.

**Email Client Abuse:**

- [ ] **Outlook Rules & Forms:** Create **client-side rules** for auto-forwarding/persistence and malicious **custom forms/add-ins**.

- [ ] **MAPI/Extended MAPI:** Leverage **Redemption/Outlook interop** for covert access and exfil.

**Cloud & SaaS Persistence:**

- [ ] **OAuth Consent Phishing:** Steal **refresh tokens** via malicious app registration; understand **scopes** and consent screens. _(See also Part 19: API Security and Part 23: Entra ID for deeper OAuth coverage.)_

- [ ] **Device Code & App Passwords:** Abuse **device code flow**, **legacy auth**, and **app passwords** for bypassing MFA.

- [ ] **Conditional Access Gaps:** Identify mis-scoped policies, **trusted locations**, and bypass paths.

- [ ] **Shared Mailboxes & Delegation:** Maintain access via **delegate rights** and mailbox rules.

**Data Exfiltration & Covert Channels:**

- [ ] **Cloud Storage APIs:** Use **Drive/OneDrive/Dropbox** APIs with **service accounts/tokens**; rotate tokens for persistence.

- [ ] **Covert Channels:** Exfil via **DNS-over-HTTPS**, **S3 pre-signed URLs**, **steganography in images/docs**, and throttled uploads.

- [ ] **Egress Controls:** Understand common **CASB/SWG** controls and how to mimic normal user traffic patterns.

**Logging, Forensics, and Cleanup:**

- [ ] **O365/Azure Audit:** Know where **Sign-In, Audit, Unified Audit** logs land; plan for artifacts.

- [ ] **Google Workspace Logs:** Review **Admin/Drive/Access Transparency** for trace evidence.

- [ ] **Artifact Hygiene:** Track **recent documents, registry keys, LNK files**, and clear only when within ROE.

### **Lab Progression (Part 8: Malware & Weaponization)**

| Level | Task                                                                                                       | Deliverable                                         |
| ----- | ---------------------------------------------------------------------------------------------------------- | --------------------------------------------------- |
| 1     | Generate 5 payload types with `msfvenom` (staged + stageless, EXE/DLL/PS1/ELF) and compare detection rates | VirusTotal screenshots + payload comparison report  |
| 2     | Deploy Sliver or Mythic in your lab, generate an implant, establish callback, and configure sleep/jitter   | C2 lab setup guide + beacon screenshot              |
| 3     | Build an HTML smuggler that delivers a test payload (EICAR) through a simulated email gateway              | HTML smuggler code + gateway bypass evidence        |
| 4     | Weaponize a OneNote file with an embedded script that calls back to your Sliver listener                   | Weaponized `.one` file + callback screenshot        |
| 5     | Map your lab campaign to MITRE ATT&CK — from delivery through C2 establishment                             | ATT&CK navigator layer JSON + technique annotations |

> [!IMPORTANT]
> **Move-On Gate (Part 8):** You can explain the malware taxonomy and choose the correct category for a given attack objective; generate payloads using `msfvenom` and a C2 framework; understand conceptually how Stages 2–5 techniques work and what defenders detect; deliver a weaponized document in a lab environment; and map a simulated campaign to MITRE ATT&CK. You are not expected to implement custom implants, PE packers, or EDR bypass code at this stage — that comes after Part 28 and in Part 42.

---

---

<a id="toc-part-9-sniffing--spoofing"></a>
<a id="part-9-sniffing-spoofing"></a>


---

<a id="module-26-pentest-methodologies--report-writing"></a>
<a id="part-39-penetration-testing-methodologies-report-writing"></a>

## Module 26: Pentest Methodologies & Report Writing


> [!NOTE]
> **📚 Recommended Books for This Part**
> - 🔴 `The Pentester Blueprint` — 🥇 Full book — pentest career methodology, report writing, and professional conduct; read fully before starting Part 39
> - 🔴 `From Hacking to Report Writing` — Full — report structure, evidence packaging, and finding articulation
> - 🟢 `Web Application Pentest Methodology` — Reference — structured methodology for web pentest engagements


> **Why This Exists:** Knowing how to exploit is useless if you can't structure an engagement professionally or communicate findings in a way that drives remediation. This part covers the "how to operate" layer that transforms technical skills into a professional practice. While its reporting templates (PTES, CVSS v3.1/v4.0, remediation matrices) are introduced in Phase 2 for documenting your first rooted lab machines, here in Phase 10 you master the end-to-end commercial engagement lifecycle: formal legal scoping, threat modeling, executive debriefing, and enterprise deliverable packaging.

<a id="stage-1-industry-standard-engagement-frameworks"></a>

### **Topic 1: Industry-Standard Engagement Frameworks** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Understand the structured methodologies that govern professional engagements.

- [ ] **PTES (Penetration Testing Execution Standard):** Master all **7 phases** — Pre-Engagement Interactions, Intelligence Gathering, Threat Modeling, Vulnerability Research, Exploitation, Post-Exploitation, Reporting; know what deliverables each phase produces and why skipping a phase breaks engagement quality.

- [ ] **OWASP Web Security Testing Guide (WSTG v4.x):** Use the **WSTG test case IDs** (WSTG-INFO-001 → WSTG-BUSL-009) as a structured web assessment checklist; map every finding to a WSTG ID for client-facing credibility and compliance evidence.

- [ ] **NIST SP 800-115 (Technical Guide to Information Security Testing):** Understand the federal-grade methodology covering **examination, identification, and validation techniques**; required knowledge for US government and regulated-industry engagements.

- [ ] **OWASP MASTG (Mobile Application Security Testing Guide):** Apply dedicated **MASTG test cases** for Android/iOS assessments; use the **MAS Checklist** for compliance-grade mobile audits; map findings to MASVS security requirements.

- [ ] **OSSTMM (Open Source Security Testing Methodology Manual):** Understand the **RAV (Risk Assessment Value)** scoring model and the concept of **attack surface measurement** — useful for mature clients who want quantified security metrics beyond CVSS.

- [ ] **Methodology Selection:** Know when to invoke each — PTES for comprehensive red team ops, NIST 800-115 for compliance-driven audits, OWASP WSTG for web-focused engagements, MASTG for mobile; document your methodology selection in every report.

---

<a id="stage-2-scoping-legal-frameworks-engagement-management"></a>

### **Topic 2: Scoping, Legal Frameworks & Engagement Management** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Define engagement boundaries that protect the tester and client legally and operationally.

- [ ] **Statement of Work (SoW) Construction:** Draft and review SoW language covering **scope definition (IP ranges, domains, application URLs), deliverables, timelines, payment milestones, liability caps, and IP ownership** of testing artifacts; ambiguous scope = legal exposure.

- [ ] **Rules of Engagement (RoE) Document:** Define in writing: **authorized IP ranges and domains, permitted testing hours (business hours vs. 24/7), testing exclusions (life-safety systems, production DBs), escalation contacts, emergency abort criteria, and data handling requirements**.

- [ ] **Get-Out-of-Jail Letter:** Understand the format and legal requirements of the **written authorization letter** — verify the signatory has authority to authorize testing, check it covers all target systems, and carry it during physical tests; know what makes it legally binding vs. inadequate.

- [ ] **Legal Framework Awareness:** Understand how **CFAA (US), Computer Misuse Act 1990 (UK), IT Act 2000 + Amendment 2008 (India), GDPR, and EU Cybersecurity Act** define criminal vs. authorized access; know how cross-border engagements create dual-jurisdiction liability.

- [ ] **Evidence & Data Handling Policy:** Establish rules for how **captured credentials, PII, financial records, source code, and exfiltrated data are classified, encrypted at rest, access-controlled, and securely destroyed** post-engagement; include this in every SoW.

- [ ] **Engagement Communication Cadence:** Define **weekly status calls, critical finding escalation (phone within 1 hour), interim report delivery, and final debrief meeting** structure; never let a critical finding sit unannounced for 24+ hours.

---

<a id="stage-3-structured-threat-modeling"></a>

### **Topic 3: Structured Threat Modeling** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Apply structured threat identification before testing begins — not after.

- [ ] **STRIDE Threat Model:** Decompose target system components into **processes, data stores, data flows, and external entities**; apply Spoofing / Tampering / Repudiation / Information Disclosure / Denial of Service / Elevation of Privilege to each element; generate a ranked threat list that scopes the test. _(See also: Part 43 Stage 1 — STRIDE applied to architecture design rather than test scoping.)_

- [ ] **PASTA (Process for Attack Simulation and Threat Analysis):** Apply the **7-stage business-centric model** — define objectives → technical scope → application decomposition → threat analysis → vulnerability analysis → attack enumeration → risk/impact analysis; produces a business-risk-aligned test plan. _(See also: Part 35 Stage 3 — PASTA applied in GRC risk management context.)_

- [ ] **Attack Trees:** Build **hierarchical attack tree diagrams** rooted at the attack goal with sub-goals as branches; use AND/OR nodes to model alternative paths; identify which branches are highest probability × highest impact for prioritized testing.

- [ ] **Data Flow Diagram (DFD) Trust Boundaries:** Draw Level 0–2 DFDs to identify **trust boundaries, data stores, external entities, and inter-process data flows**; every trust boundary crossing is an attack surface that must be tested.

- [ ] **MITRE ATT&CK as Pre-Test Input:** Use ATT&CK to **pre-identify likely adversary TTPs** based on target industry, known threat actor profiles, and previously disclosed incidents in the sector; build your test plan around these TTPs.

- [ ] **LINDDUN (Privacy Threat Model):** Apply LINDDUN (Linkability, Identifiability, Non-repudiation, Detectability, Disclosure of information, Unawareness, Non-compliance) for privacy-focused assessments — required for GDPR/HIPAA compliance-mapped tests.

---

<a id="stage-4-vulnerability-scoring-risk-prioritization"></a>

### **Topic 4: Vulnerability Scoring & Risk Prioritization** — `🧠 Conceptual`

> [!TIP]
> **Goal:** Rate findings objectively and communicate risk in business terms — not just CVSS numbers.

- [ ] **CVSS v3.1 Base Metrics:** Master all **8 base metrics** (Attack Vector, Attack Complexity, Privileges Required, User Interaction, Scope, Confidentiality/Integrity/Availability Impact); calculate scores manually before using calculators to build intuition.

- [ ] **CVSS v4.0 Changes:** Understand the **new Supplemental Metrics group** (Automatable, Recovery, Value Density, Response Effort, Provider Urgency) and the replacement of Temporal Metrics with **Threat Metrics (Exploit Maturity)**; know which scoring version your client's compliance framework requires.

- [ ] **EPSS (Exploit Prediction Scoring System):** Use **EPSS probability scores** alongside CVSS to distinguish actively exploited vulnerabilities from theoretical ones; a CVSS 9.8 with 0.1% EPSS differs operationally from a CVSS 7.5 with 95% EPSS.

- [ ] **Business Risk Contextualization:** Calculate **Risk = Likelihood × Business Impact** — map vulnerabilities to: revenue exposure, regulatory fine potential, reputational damage, operational downtime, and data breach notification costs; a CVSS 5.4 on a public-facing OAuth token endpoint may carry more business risk than a CVSS 8.1 on an isolated dev server.

- [ ] **Vulnerability Chaining Analysis:** Identify when **individually low-severity findings combine** into critical-severity attack chains (e.g., SSRF [Medium] + IMDS credential access [Low] + overprivileged IAM role [Medium] = Full Cloud Compromise [Critical]); document chains as unified findings with individual component breakdowns.

- [ ] **Finding Deduplication:** When a single root cause produces multiple manifestations (e.g., 50 instances of the same SQLi pattern), report as **one finding with representative samples** and a count — not 50 separate findings that inflate severity perception and waste remediation effort.

---

<a id="stage-5-professional-report-writing"></a>

### **Topic 5: Professional Report Writing** — `🧠🔬 Mixed`

> [!TIP]
> **Goal:** Deliver findings in a format that survives executive scrutiny and drives budgeted remediation.

- [ ] **Report Architecture:** Master the standard structure: **Cover Page → Executive Summary → Engagement Overview (scope, methodology, timeline) → Attack Narrative → Findings by Severity → Remediation Roadmap → Appendices (evidence, tooling, methodology references, CVSS breakdowns)**.

- [ ] **Executive Summary (Non-Technical):** Write a **1–2 page narrative** for the C-suite covering: overall security posture rating, total findings by severity, most critical business risks, and top 3 priority actions — written for a CFO reading at 35,000 feet, not a sysadmin.

- [ ] **Technical Finding Template:** Each finding must include: **Title | Severity | CVSS Score (v3.1/v4.0) | EPSS % | Affected Asset | Vulnerability Description | Business Impact | Proof of Concept (exact request/response/screenshot) | Remediation Guidance (specific, actionable, with code examples where applicable) | References (CVE, CWE, OWASP ID)**.

- [ ] **Attack Narrative / Kill Chain Story:** Write a **linear narrative** tracing the attacker's path from initial foothold through escalation to maximum impact — this is the section that gets security budgets approved; make it read like a post-breach incident report, not a bullet list.

- [ ] **Remediation Specificity:** Write remediation as **executable technical steps** — e.g., "Apply parameterized queries using `mysqli_prepare()` with bound parameters" not "fix SQL injection"; include patch version numbers, configuration file paths, and code snippets; vague remediation = finding stays open.

- [ ] **Proof-of-Concept Discipline:** PoCs must be **reproducible, minimally invasive, and clearly annotated** — include exact HTTP request/response, commands run, and observed vs. expected behavior; redact real credentials and PII captured; test PoC steps against your own notes before submission.

- [ ] **Remediation Roadmap Tiering:** Tier findings into **Immediate (< 7 days — critical/exploited), Short-term (< 30 days — high), Medium-term (< 90 days — medium), Long-term / Strategic (low + systemic architectural issues)**; include effort estimates and responsible team assignments.

- [ ] **Re-test Procedures:** Document **exactly how the client verifies each remediation** — include test steps, expected output, and acceptance criteria; schedule and execute a **formal re-test engagement** where contracted; issue a re-test supplement report with delta findings.

- [ ] **Report Versioning & Delivery:** Maintain **draft → client review → final** versioning; deliver reports in **password-protected PDF** with restricted printing/copying; PGP-encrypt email attachments; define report retention and destruction policy in the SoW.

### **Lab Progression (Part 39: Penetration Testing Methodologies & Report Writing)**

| Level | Task                                                                                                                  | Deliverable                                                   |
| ----- | --------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------- |
| 1     | Draft an SoW and RoE document for a fictional engagement using a provided scenario                                    | Complete SoW + RoE document pair                              |
| 2     | Apply STRIDE to a target application's DFD and produce a ranked threat list                                           | Threat model document with STRIDE matrix                      |
| 3     | Write a full pentest report (executive summary + 3 findings with PoC + remediation roadmap) for an enterprise lab engagement | Professional pentest report in PDF format, password-protected |

> [!IMPORTANT]
> **Move-On Gate (Part 39):** You can select and apply the correct engagement methodology (PTES, NIST 800-115, WSTG), produce an SoW and RoE document, perform STRIDE threat modeling, calculate CVSS scores manually, and write a complete pentest report with executive summary, technical findings, and remediation roadmap.

---

<a id="toc-part-40-red-team-operations--tradecraft"></a>
<a id="part-40-red-team-operations-tradecraft"></a>


---

> [!TIP]
> ### 🎮 Concurrent CTF Practice — Stage 4
>
> Enterprise environments require enterprise practice. Standard HTB/THM boxes are no longer enough — you need pro labs.
>
> | Module | Platform | Lab / Box | Why |
> |---|---|---|---|
> | 19 Active Directory | HackTheBox | **Forest** · **Monteverde** · **Cascade** | Kerberoasting, AS-REP, ACL abuse, Pass-the-Hash |
> | 19 Active Directory | TryHackMe | **Active Directory Basics** · **Attacktive Directory** | Guided AD attack path from scratch |
> | 19 Active Directory | HackTheBox Pro Labs | **Offshore** or **RastaLabs** | Full multi-domain enterprise AD simulation |
> | 20 Cloud | [flaws.cloud](http://flaws.cloud) + [flaws2.cloud](http://flaws2.cloud) | All levels | AWS S3, IAM, metadata exploitation |
> | 20 Cloud | [CloudGoat](https://github.com/RhinoSecurityLabs/cloudgoat) | All scenarios | Rhino Security's vulnerable-by-design AWS env |
> | 21 Containers | HackTheBox | **Unobtainium** · **Registry** | Container escape + Kubernetes privilege escalation |
> | 22–26 Full chain | HackTheBox Pro Labs | **Dante** (OSCP prep) | Full network penetration test simulation |
>
> **Rule:** For every AD box: export your BloodHound graph, annotate the attack path, commit it to Git. That is a portfolio artifact.

<a id="stage-gate-3"></a>

## 🏁 Stage Gate 3 — Enterprise Domain Compromise & Reporting

> [!IMPORTANT]
> **Stage 4 Exit Gate:** Before moving to Advanced Offensive Development (Stage 5), you must prove:
> - Full end-to-end compromise of a multi-forest Active Directory lab (Kerberoasting/AS-REP roasting -> DCSync -> Golden Ticket).
> - BloodHound visualization and execution of shortest attack path committed to Git.
> - One complete, client-ready, professional penetration test report following PTES/CVSS standards.
