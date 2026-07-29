# Phase 6: Infrastructure & Identity

---

### 🧭 Navigation
◀ [Phase 5](Phase-5.md) | 🏠 [Master Roadmap](README.md) | [Phase 7](Phase-7.md) ➔

---

> [!NOTE]
> **Phase Overview**
> - **⏱️ Time Commitment (Full-Time):** 6–9 months
> - **⏱️ Time Commitment (Part-Time):** 10–14 months
> - **🎯 Primary Focus:** Active Directory & Entra ID (on-prem + hybrid cloud identity), cloud computing attacks (AWS/Azure/GCP), container & Kubernetes security, OT/ICS/SCADA industrial systems, and adversary emulation & purple teaming.

---

> [!NOTE]
> ### 📝 Phase 6 Documentation Requirements
> Enterprise infrastructure work must be thoroughly documented. Required artifacts:
> - **BloodHound exports** — attack path graphs with annotated findings
> - **Cloud attack evidence** — CloudTrail logs, IAM policy analysis, exploitation screenshots
> - **Terraform/CloudFormation configs** — infrastructure-as-code for lab environments committed to Git
> - **Purple team ATT&CK heatmap** — technique coverage matrix showing detection gaps
> - **Git commits** — all configs, exports, and reports committed
>
> _By the end of Phase 6, you should have enterprise attack documentation rivaling junior consultant deliverables._

---

### 🗂️ Table of Contents
- [Part 23: Active Directory & Entra ID](#part-23-active-directory-entra-id)
  - [Stage 1: Discovery & Enumeration](#stage-1-discovery-enumeration)
  - [Stage 2: Credential & Auth Attacks](#stage-2-credential-auth-attacks)
  - [Stage 3: Delegation, ACL, and ADCS Abuse](#stage-3-delegation-acl-and-adcs-abuse)
  - [Stage 4: Lateral Movement & Persistence](#stage-4-lateral-movement-persistence)
  - [Stage 5: Entra ID (Azure AD) & Hybrid Attacks](#stage-5-entra-id-azure-ad-hybrid-attacks)
  - [Lab Progression (Part 23: Active Directory & Entra ID)](#lab-progression-part-23-active-directory-entra-id)
- [Part 24: Cloud Computing](#part-24-cloud-computing)
  - [Stage 1: Architecture & Governance](#stage-1-architecture-governance)
  - [Stage 2: Storage & Data Security](#stage-2-storage-data-security)
  - [Stage 3: Modern Infrastructure & Deployment](#stage-3-modern-infrastructure-deployment)
  - [Stage 4: Automation & Scripting](#stage-4-automation-scripting)
  - [Stage 5: Cloud-Specific Attack Vectors](#stage-5-cloud-specific-attack-vectors)
  - [Stage 6: IAM & PAM Attack Surface](#stage-6-iam-pam-attack-surface)
- [Part 25: Container & Orchestration Security](#part-25-container-orchestration-security)
  - [Stage 1: Container Fundamentals & Attacks](#stage-1-container-fundamentals-attacks)
  - [Stage 2: Kubernetes Security](#stage-2-kubernetes-security)
  - [Stage 3: Container Runtime Security](#stage-3-container-runtime-security)
  - [Stage 4: Secrets & Configuration Management](#stage-4-secrets-configuration-management)
  - [Stage 5: CI/CD & Workflow Automation Attacks](#stage-5-cicd-workflow-automation-attacks)
  - [Lab Progression (Part 25: Container & Orchestration Security)](#lab-progression-part-25-container-orchestration-security)
- [Part 26: OT/ICS/SCADA Security \[OPTIONAL SPECIALIZATION\]](#part-26-oticsscada-security)
  - [Stage 1: Industrial Protocol Fundamentals](#stage-1-industrial-protocol-fundamentals)
  - [Stage 2: PLC & HMI Exploitation](#stage-2-plc-hmi-exploitation)
  - [Stage 3: Safety System Attacks](#stage-3-safety-system-attacks)
  - [Stage 4: OT Network Segmentation & Defense](#stage-4-ot-network-segmentation-defense)
  - [Lab Progression (Part 26: OT/ICS/SCADA Security)](#lab-progression-part-26-oticscada-security)
- [Part 16: Adversary Emulation & Purple Teaming](#part-16-adversary-emulation-purple-teaming) _(Phase 6 Capstone)_
  - [Stage 1: MITRE ATT&CK Framework Mastery](#stage-1-mitre-attck-framework-mastery)
  - [Stage 2: APT & Threat Actor Emulation](#stage-2-apt-threat-actor-emulation)
  - [Stage 3: Purple Team Exercises](#stage-3-purple-team-exercises)
  - [Stage 4: Metrics & Reporting](#stage-4-metrics-reporting)
  - [Lab Progression (Part 16: Adversary Emulation & Purple Teaming)](#lab-progression-part-16-adversary-emulation-purple-teaming)

---

<a id="part-23-active-directory-entra-id"></a>
## Part 23: Active Directory & Entra ID

<a id="stage-1-discovery-enumeration"></a>
### **Stage 1: Discovery & Enumeration**

> [!TIP]
> **Goal:** Map identity surfaces across on-prem AD and Entra ID (Azure AD).

- [ ] **Domain Recon:** Enumerate **domains/forests, trusts, sites, subnets, FSMO roles**; collect **OU/Group/ACL** data.

- [ ] **Identity Inventory:** List **users, computers, service accounts, Tier0 assets, SPNs**, and **LAPS** posture.

- [ ] **Policy & Exposure:** Audit **GPOs, login scripts, startup tasks**, and **Unconstrained/Constrained/RBCD** exposure.

- [ ] **Entra ID/Cloud Recon:** Enumerate **tenants, apps, service principals, consented permissions, conditional access** and **enterprise apps**.

---

<a id="stage-2-credential-auth-attacks"></a>
### **Stage 2: Credential & Auth Attacks**

> [!TIP]
> **Goal:** Steal or replay credentials to gain higher privilege.

- [ ] **Kerberoast / AS-REP Roast:** Extract **TGS/AS-REP** tickets for offline cracking; prioritize **high-priv SPNs**.

- [ ] **NTLM Relay/SMB/HTTP:** Abuse **NTLM relays** against **SMB/LDAP/HTTP/ADCS HTTP endpoints**; combine with **mTLS gaps**.

- [ ] **Token Abuse:** Steal **TGT/TGS, DPAPI, LSASS, browser tokens**, and **OAuth refresh tokens** across hybrid joins.

- [ ] **Password Hygiene:** Spray with **safe lockout windows**, target **legacy auth (POP/IMAP/SMTP)**, and downgrade to **basic auth** where possible.

---

<a id="stage-3-delegation-acl-and-adcs-abuse"></a>
### **Stage 3: Delegation, ACL, and ADCS Abuse**

> [!TIP]
> **Goal:** Abuse trust relationships and misconfigurations for escalation.

- [ ] **Delegation Abuse:** Exploit **Unconstrained, Constrained (service/alt service), and Resource-Based Constrained Delegation (RBCD)** for impersonation.

- [ ] **ACL/ACE Abuse:** Exploit **WriteOwner, WriteDACL, GenericAll/GenericWrite, AddMember** on critical principals (DA, EA, DCs, Tier0 groups).

- [ ] **Shadow Credentials:** Abuse **msDS-KeyCredentialLink** to add rogue keys for persistence.

- [ ] **ADCS (PKI) Abuse:** Exploit **ESC1-ESC8** templates (ENROLLEE_SUPPLIES_SUBJECT, weak EKUs, SAN impersonation) to mint **golden certs**; target **HTTP enrollment endpoints** for relays.

---

<a id="stage-4-lateral-movement-persistence"></a>
### **Stage 4: Lateral Movement & Persistence**

> [!TIP]
> **Goal:** Move horizontally and maintain footholds.

- [ ] **Lateral Paths:** Use **WinRM/SMB/RDP/WMI/PowerShell Remoting**, **admin shares**, and **task/svc installs** guided by **BloodHound** paths.

- [ ] **GPO Persistence:** Implant via **logon scripts, immediate scheduled tasks, startup items**; abuse **restricted groups** for re-add.

- [ ] **DC Sync / DC Shadow:** Abuse **Replicating Directory Changes** to pull **NTDS.dit** or inject rogue DC changes.

- [ ] **Golden/Silver Tickets:** Forge **krbtgt/service hashes** for long-lived access; manage **ticket lifetime/renewal** OPSEC.

---

<a id="stage-5-entra-id-azure-ad-hybrid-attacks"></a>
### **Stage 5: Entra ID (Azure AD) & Hybrid Attacks**

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
## Part 24: Cloud Computing

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
### **Stage 1: Architecture & Governance**


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
### **Stage 2: Storage & Data Security**

> [!TIP]
> **Goal:** Enumerate, audit, and exploit cloud storage misconfigurations — the most common source of cloud data breaches.

- [ ] **Object Storage Security:** Audit `S3` buckets and `Common Cloud Storage` (Drive, Box) for public access and enforce encryption.

- [ ] **Access Control:** Implement strict IAM policies ensuring only authorized identities can access storage blobs.

- [ ] **S3 Bucket Enumeration:** Use `aws s3api list-buckets` to enumerate all buckets in-scope. For each bucket, run `aws s3api get-bucket-acl`, `get-bucket-policy`, `get-bucket-cors`, and `get-public-access-block` to map the full exposure surface. Use **cloudbrute** for unauthenticated bucket discovery against organization name variants.

- [ ] **ACL & Policy Audit:** Identify buckets with `AllUsers` (public) or `AuthenticatedUsers` (any AWS account) grants in their ACL. Identify bucket policies with `"Principal": "*"` without a restrictive condition. Both patterns create read/write exposure without authentication.

- [ ] **CORS Misconfiguration:** Retrieve CORS config with `aws s3api get-bucket-cors`. Permissive CORS (`AllowedOrigin: *` + `AllowCredentials: true` patterns) enables cross-origin data theft from authenticated browser sessions. Test with a crafted request from an attacker origin.

- [ ] **Secrets in Object Storage:** Use **trufflehog** (`trufflehog s3 --bucket=<name>`) to scan bucket contents for hardcoded credentials, API keys, database connection strings, and private certificates that developers have uploaded and forgotten.

---

<a id="stage-3-modern-infrastructure-deployment"></a>
### **Stage 3: Modern Infrastructure & Deployment**

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
### **Stage 4: Automation & Scripting**

> [!TIP]
> **Goal:** Use automation to enumerate, audit, and monitor cloud environments — understand what defenders see so you know what to avoid generating.

- [ ] **Cloud Automation:** Use **Python (Boto3), Terraform, CloudFormation** to audit security groups and IAM roles automatically.

- [ ] **Admin Scripting:** Master **Bash, PowerShell, AWS CLI, Azure CLI** to manage instances and automate operations.

- [ ] **CI/CD Security:** Integrate **security scanning** (SAST, DAST, dependency checks) into deployment pipelines.

- [ ] **CloudTrail Log Analysis:** Query **CloudTrail** (`aws cloudtrail lookup-events --lookup-attributes AttributeKey=EventName,AttributeValue=ConsoleLogin`) to identify unauthorized API calls, credential use from unusual IPs, role assumption chains, and resource creation events. Understand log retention gaps — events older than 90 days require S3 log archive access.

- [ ] **AWS CLI Enumeration Commands:** Build a systematic enumeration checklist: `aws iam list-users`, `aws iam list-roles`, `aws iam get-account-authorization-details` (dumps all policies, users, roles in one call), `aws ec2 describe-instances`, `aws s3api list-buckets`, `aws lambda list-functions`. For Azure: `az account list`, `az role assignment list --all`, `az vm list`. Run these as the first step after any credential compromise.

- [ ] **Cross-Account Audit Automation:** Use **Prowler's multi-account mode** or write Boto3 scripts using `sts:AssumeRole` to enumerate security posture across all accounts in an AWS Organization from a single auditor role. Understand how cross-account role trust policies create lateral movement paths.

> [!IMPORTANT]
> **Move-On Gate (Part 24: Cloud Computing):** You are ready to continue when you can: (1) run ScoutSuite or Prowler against a lab AWS account and interpret the findings report; (2) enumerate all S3 buckets, their ACLs, bucket policies, and CORS configurations using the AWS CLI; (3) use trufflehog to scan an S3 bucket for secrets; (4) run checkov against a Terraform template and explain each HIGH finding; (5) query CloudTrail to identify at least one suspicious API event in a lab environment. If you cannot do all five without looking up the commands, revisit Stages 2–4 before proceeding.

---

<a id="stage-5-cloud-specific-attack-vectors"></a>
### **Stage 5: Cloud-Specific Attack Vectors**

> [!TIP]
> **Goal:** Understand unique cloud threats.

- [ ] **IAM Exploitation:** Abuse **overprivileged roles, AssumeRole chains, resource-based policies** for privilege escalation.

- [ ] **Storage Misconfigurations:** Find **public S3 buckets, blob containers** via enumeration and exploitation.

- [ ] **Metadata Services:** Query **IMDS (169.254.169.254)** for IAM credentials, instance metadata.

- [ ] **Serverless Attacks:** Exploit **Lambda environment variables, excessive permissions, function injection**.

- [ ] **Container Escapes:** Break out of **Docker, Kubernetes pods** via misconfigurations. 📌 _See Part 25 Stage 1 for full container escape techniques and Part 25 Stage 2 for Kubernetes-specific attacks._

- [ ] **Multi-Tenancy Issues:** Understand **side-channel attacks, resource exhaustion** in shared cloud environments.

---

<a id="stage-6-iam-pam-attack-surface"></a>
### **Stage 6: IAM & PAM Attack Surface**

> [!TIP]
> **Goal:** Master identity-based attack techniques in cloud and enterprise environments.

- [ ] **IAM Policy Analysis:** Enumerate and analyze **IAM policies** using **Pacu, enumerate-iam, ScoutSuite, Prowler** to find **overprivileged roles, wildcard permissions (*)**, and privilege escalation paths across **AWS/Azure/GCP**.

- [ ] **Role Chaining & Federation Abuse:** Exploit **AssumeRole chains, cross-account trust relationships, OIDC federation, SAML assertion manipulation** to escalate from low-privilege to administrative access.

- [ ] **Service Account & Managed Identity Abuse:** Target **service accounts, managed identities, workload identity federation** with excessive permissions or leaked credentials. Understand **key rotation failures** and **long-lived access key risks**.

- [ ] **Conditional Access & Policy Bypass:** Test **Azure Conditional Access policies, AWS SCPs (Service Control Policies), GCP Organization Policies** for bypass conditions — **device compliance gaps, location spoofing, legacy auth exemptions, MFA registration weaknesses**.

- [ ] **Privileged Access Management (PAM):** Understand **CyberArk, Delinea (Thycotic), BeyondTrust** vault architecture — **credential vaulting, session recording, just-in-time (JIT) access, credential rotation**. Know the attack surface: **vault admin compromise, session proxy hijacking, checkout abuse, emergency break-glass exploitation**.

- [ ] **Identity Governance:** Understand **access reviews, entitlement management, separation of duties (SoD)**, and how **identity lifecycle gaps** (orphaned accounts, excessive standing privileges, stale service principals) create attack opportunities.

---

<a id="toc-part-25-container--orchestration-security"></a>
<a id="part-25-container-orchestration-security"></a>
## Part 25: Container & Orchestration Security

<a id="stage-1-container-fundamentals-attacks"></a>
### **Stage 1: Container Fundamentals & Attacks**

> [!TIP]
> **Goal:** Understand containerization and its security implications.

- [ ] **Container Anatomy:** Master **namespaces, cgroups, capabilities, seccomp, AppArmor/SELinux** as isolation mechanisms.

- [ ] **Image Vulnerabilities:** Scan images with **Trivy, Clair, Grype** for **CVEs, secrets, misconfigs** in layers.

- [ ] **Dockerfile Security:** Audit **Dockerfiles** for **running as root, exposed secrets, vulnerable base images, unnecessary packages**.

- [ ] **Container Escape:** Exploit **--privileged flag, CAP_SYS_ADMIN, mounted docker.sock, kernel exploits** to break out to host.

- [ ] **Docker API Exploitation:** Abuse **exposed Docker API (2375/2376)** to spawn privileged containers and compromise host.

---

<a id="stage-2-kubernetes-security"></a>
### **Stage 2: Kubernetes Security**

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
### **Stage 3: Container Runtime Security**

> [!TIP]
> **Goal:** Detect and prevent malicious container activity.

- [ ] **Runtime Monitoring:** Deploy **Falco, Sysdig, Aqua** to detect **suspicious syscalls, process execution, network connections**.

- [ ] **Admission Control:** Use **OPA (Open Policy Agent), Kyverno** to enforce **security policies at admission time**.

- [ ] **Image Signing:** Implement **Notary, Cosign** for **image provenance verification** and supply chain security.

- [ ] **Runtime Protection:** Enable **seccomp profiles, AppArmor/SELinux policies** to restrict container capabilities.

- [ ] **Network Segmentation:** Deploy **Calico, Cilium** network policies to **microsegment pod-to-pod communication**.

---

<a id="stage-4-secrets-configuration-management"></a>
### **Stage 4: Secrets & Configuration Management**

> [!TIP]
> **Goal:** Secure sensitive data in containerized environments.

- [ ] **Secret Stores:** Use **HashiCorp Vault, AWS Secrets Manager, Azure Key Vault** instead of K8s native secrets.

- [ ] **Init Containers:** Fetch secrets at **pod startup** via init containers instead of baking into images.

- [ ] **Sealed Secrets:** Encrypt secrets in Git using **Bitnami Sealed Secrets, SOPS** for GitOps workflows.

- [ ] **Workload Identity:** Use **cloud provider workload identity** (AWS IRSA, GCP Workload Identity) for keyless authentication.

- [ ] **Secret Rotation:** Implement **automatic secret rotation** and short-lived credentials.

---

<a id="stage-5-cicd-workflow-automation-attacks"></a>
### **Stage 5: CI/CD & Workflow Automation Attacks**

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
> [!IMPORTANT]
> **Move-On Gate:** Produce a Kubernetes hardening report with RBAC, network policy, admission control, image scanning, and runtime detection notes.

<a id="toc-part-26-oticsscada-security"></a>
<a id="part-26-oticsscada-security"></a>

## Part 26: OT/ICS/SCADA Security [OPTIONAL SPECIALIZATION]

> [!NOTE]
> **Optional Specialization:** OT/ICS/SCADA security is a distinct career track targeting industrial control systems in energy, utilities, manufacturing, and critical infrastructure. If your career goal is ICS pentesting, SCADA security engineering, or critical infrastructure defense, complete this Part in full. If your goal is general offensive security, cloud, or enterprise AD — treat this Part as awareness-level reading and return to it when specializing. Do not let OT/ICS block your progress into Phase 7.

<a id="stage-1-industrial-protocol-fundamentals"></a>
### **Stage 1: Industrial Protocol Fundamentals**

> [!TIP]
> **Goal:** Understand operational technology communication.

- [ ] **Modbus TCP/RTU:** Master **function codes (read coils, write registers)**, perform **unauthenticated reads/writes** to PLCs.

- [ ] **DNP3:** Understand **SCADA protocol** used in utilities; exploit **lack of authentication, replay attacks**.

- [ ] **IEC 61850:** Learn **power substation protocol**; understand **GOOSE messages, MMS** for substation automation.

- [ ] **BACnet:** Audit **building automation systems**; enumerate **devices, read/write points** without authentication.

- [ ] **OPC UA:** Exploit **OPC servers** for **data exfiltration, authentication bypass, denial of service**.

---

<a id="stage-2-plc-hmi-exploitation"></a>
### **Stage 2: PLC & HMI Exploitation**

> [!TIP]
> **Goal:** Compromise industrial controllers and interfaces.

- [ ] **PLC Enumeration:** Use **Nmap NSE scripts, plcscan** to identify **Siemens S7, Allen-Bradley, Schneider** devices.

- [ ] **Ladder Logic Analysis:** Reverse engineer **PLC programs** to understand **control logic, safety interlocks**.

- [ ] **Firmware Manipulation:** Extract and modify **PLC firmware** to inject malicious logic or backdoors.

- [ ] **HMI Exploitation:** Exploit **HMI software vulnerabilities, default credentials, SQL injection** in SCADA interfaces.

- [ ] **Engineering Workstation:** Target **engineering stations** with **phishing, malware** as gateway to OT network.

---

<a id="stage-3-safety-system-attacks"></a>
### **Stage 3: Safety System Attacks**

> [!TIP]
> **Goal:** Understand attacks on critical safety instrumented systems.

- [ ] **Safety PLC:** Identify **safety-rated PLCs** and understand **fail-safe vs fail-operational** modes.

- [ ] **Interlock Bypass:** Manipulate **logic to disable safety interlocks** causing unsafe operational states.

- [ ] **Sensor Manipulation:** Spoof **sensor values** (temperature, pressure, level) to trigger incorrect responses.

- [ ] **Emergency Shutdown (ESD):** Understand **ESD systems** and potential for **malicious activation/deactivation**.

- [ ] **Physical Impact:** Assess **real-world consequences** of cyber attacks (equipment damage, safety incidents, environmental harm).

---

<a id="stage-4-ot-network-segmentation-defense"></a>
### **Stage 4: OT Network Segmentation & Defense**

> [!TIP]
> **Goal:** Implement defense-in-depth for industrial environments.

- [ ] **Purdue Model:** Apply **ISA-95/Purdue Enterprise Reference Architecture** for **zone-based segmentation**.

- [ ] **DMZ Architecture:** Deploy **data diodes, unidirectional gateways** to isolate OT from IT networks.

- [ ] **Protocol Whitelisting:** Use **industrial firewalls** to whitelist **allowed protocols, function codes, device communications**.

- [ ] **Anomaly Detection:** Deploy **OT-aware IDS (Claroty, Nozomi, Dragos)** to detect **protocol deviations, unauthorized commands**.

- [ ] **Asset Inventory:** Maintain **passive discovery** of all OT assets using **network taps, SPAN ports**.

- [ ] **Patch Management:** Implement **risk-based patching** with **change control, redundancy, rollback procedures**.

---

<a id="lab-progression-part-26-oticscada-security"></a>
### **Lab Progression (Part 26: OT/ICS/SCADA Security)**

> [!TIP]
> **Goal:** Gain hands-on experience with industrial control system attacks and defenses.

| Level | Task | Deliverable |
|-------|------|-------------|
| 1 | Set up GRFICSv2 or SWaT testbed and explore Modbus/DNP3 traffic with Wireshark | Protocol analysis report with annotated packet captures |
| 2 | Attack an OpenPLC controller in lab (scan, enumerate, modify ladder logic) | PLC exploitation walkthrough with screenshots |
| 3 | Design ICS network segmentation using Purdue Model zones and data diodes | ICS security architecture document with network diagram |

> [!IMPORTANT]
> **Move-On Gate:** You can enumerate OT protocols, explain the Purdue Model, and demonstrate safe ICS network segmentation.

---

<a id="part-16-adversary-emulation-purple-teaming"></a>
## Part 16: Adversary Emulation & Purple Teaming _(Phase 6 Capstone)_

> [!NOTE]
> **Navigational Note — Why Part 16 Is Here:** Part 16 is the **Phase 6 Capstone** — it synthesizes all content from Parts 23–26 (Active Directory, Cloud, Containers, OT) into a unified adversary emulation exercise. It is numbered 16 because it was originally placed sequentially after Phase 3's Part 15 (OSINT & Threat Intelligence) in the roadmap's initial design. It belongs contextually in Phase 6 as the synthesis capstone of Parts 23–26. When you see cross-references to "Part 16" elsewhere in the roadmap, they refer to this section in Phase 6.


> [!WARNING]
> **Prerequisites:** This Part requires both offensive (Phase 2) AND defensive (Phase 3) maturity plus enterprise infrastructure knowledge from the Parts above (AD, Cloud, Containers, OT). Complete all prior Phase 6 content before attempting this. Purple teaming is the culmination of offense-defense integration at enterprise scale.

<a id="stage-1-mitre-attck-framework-mastery"></a>
### **Stage 1: MITRE ATT&CK Framework Mastery**

> [!TIP]
> **Goal:** Understand the universal language of adversary behavior.

- [ ] **Tactic Familiarity:** Master all **14 tactics** (Initial Access → Impact) and their relationships in the attack lifecycle.

- [ ] **Technique Deep-Dive:** Study **100+ core techniques** with focus on **prevalence, detection difficulty, impact** ratings.

- [ ] **Sub-Technique Granularity:** Understand **sub-technique variations** for precise emulation (e.g., T1059.001 PowerShell vs T1059.003 CMD).

- [ ] **Data Source Mapping:** Link techniques to **detection data sources** (process creation, network traffic, registry modifications).

- [ ] **Mitigation Strategies:** Review **MITRE mitigations** for each technique to understand defensive controls.

---

<a id="stage-2-apt-threat-actor-emulation"></a>
### **Stage 2: APT & Threat Actor Emulation**

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
### **Stage 3: Purple Team Exercises**

> [!TIP]
> **Goal:** Collaborative offense-defense improvement.

- [ ] **Joint Planning:** Define **objectives, scope, techniques, success criteria** with both red and blue teams.

- [ ] **Live Detection Tuning:** Execute **attacks in controlled environment** while defenders **tune detection rules in real-time**.

- [ ] **Gap Analysis:** Identify **detection blind spots, control failures, response deficiencies** through collaborative testing.

- [ ] **Playbook Development:** Create **detection playbooks** with **queries, alerts, response procedures** for each emulated technique.

- [ ] **Iterative Improvement:** Run **multiple rounds** of testing with **incremental detection improvements** to measure progress.

---

<a id="stage-4-metrics-reporting"></a>
### **Stage 4: Metrics & Reporting**

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

### 🏆 Phase 6 Capstone Project

**Build an AD Forest, Attack It End-to-End, Secure It, Then Validate with Purple Teaming**

- [ ] **Build a 2-domain AD forest** (parent + child) with realistic GPOs, service accounts, and certificate services
- [ ] **Attack the entire environment** — enumerate with BloodHound, Kerberoast, escalate to Domain Admin, move laterally
- [ ] **Secure the environment** — implement tiered admin model, LAPS, disable NTLM where possible, harden ADCS
- [ ] **Validate with purple teaming** — map the attack path to MITRE ATT&CK, tune detections, and measure MTTD/MTTR
- [ ] **Verify defenses** — re-run attacks and confirm they are mitigated or detected

**Deliverables:**
- [ ] AD attack-path report with BloodHound graphs showing the complete compromise chain
- [ ] Hardening guide documenting every security control implemented
- [ ] ATT&CK heatmap and detection coverage matrix for the emulated techniques
- [ ] Before/after comparison showing which attacks were mitigated or detected
- [ ] All documentation committed to your Git repository

> [!IMPORTANT]
> **Capstone Gate:** Your report must show a complete attack chain, a complete remediation path, and purple-team validation. The before/after comparison must demonstrate measurable security improvement.

---

### 🧭 Phase 6 Reflection & Competency Check

- [ ] **Reflection:** Which enterprise surface created the most risk in your lab: identity, cloud, containers, OT/ICS, or detection gaps?
- [ ] **Reflection:** What changed after remediation, and how did you measure the improvement?
- [ ] **Competency:** Can you attack and harden AD/Entra ID paths with clear evidence?
- [ ] **Competency:** Can you explain cloud, container, and network misconfigurations in terms of blast radius?
- [ ] **Competency:** Can you run a purple team exercise that maps techniques to telemetry, detections, and remediation?

> [!IMPORTANT]
> **Phase Completion Gate:** Move on only when you can demonstrate a full enterprise attack path, document remediation, and prove measurable detection or control improvement.

---
