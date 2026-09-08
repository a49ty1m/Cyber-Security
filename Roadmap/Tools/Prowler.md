# ☁️ Prowler: Complete Mastery Checklist

> **What is Prowler?** Prowler is an open-source cloud security tool that performs security assessments, audits, and compliance checks across AWS, Azure, and Google Cloud Platform. It runs hundreds of automated checks against cloud environments — checking IAM misconfigurations, exposed S3 buckets, unencrypted data stores, missing logging, over-privileged roles, network security group gaps, and compliance with frameworks like CIS Benchmarks, SOC 2, GDPR, HIPAA, and PCI DSS.
>
> **Why does it exist?** Cloud misconfiguration is the #1 cause of cloud security breaches. Manual auditing of cloud environments with thousands of resources is impossible at scale. Prowler automates this — giving a complete security posture assessment in minutes that would take a human team days.
>
> **When to use it:** Cloud security assessments during pentests, as the first tool run on any cloud engagement after obtaining IAM credentials, continuous compliance monitoring in DevSecOps pipelines, and as an attacker to understand what the defender can see (run Prowler with compromised credentials to see what's exposed).
>
> **When to avoid it:** Prowler requires API access — it won't find vulnerabilities in resources it can't enumerate. It's a configuration scanner, not an exploitation tool. It finds the attack surface; exploitation requires tools like Pacu (AWS) or manual exploitation.
>
> **What mastering Prowler unlocks:** Cloud security assessment capability, compliance reporting against major frameworks, understanding of the most common cloud attack surfaces (exposed buckets, overprivileged roles, missing MFA), and the reconnaissance capability needed before Pacu exploitation.
>
> **Roadmap Phase:** Phase 6 — Enterprise & Cloud Security (Cloud Security Assessment)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](README.md)

| Cloud Security | AD/Enterprise | Exploitation |
|:--------------|:-------------|:-------------|
| **☁️ Prowler** (you are here) | [🩸 BloodHound](BloodHound.md) | [🐦 Pacu](Pacu.md) |
| [🔑 Certipy](Certipy.md) | [🔧 Impacket](Impacket.md) | [💀 NetExec](NetExec.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & AWS Configuration | 5 | 1–2 hours |
| 2 | Core AWS Checks | 8 | 3–4 hours |
| 3 | IAM & Privilege Analysis | 7 | 3–4 hours |
| 4 | Network & Storage Security | 6 | 2–3 hours |
| 5 | Compliance Framework Scans | 4 | 2–3 hours |
| 6 | Azure & GCP Coverage | 5 | 2–3 hours |
| 7 | Practical Labs | 4 | 3–5 hours |
| | **Total** | **39** | **~16–24 hours** |

**Prerequisites:** Phase 1 CLI basics. Basic understanding of AWS core services (IAM, S3, EC2, VPC). An AWS account (free tier works). Phase 6 cloud fundamentals.

---

# PHASE 1: INSTALLATION & AWS CONFIGURATION

---

## 1.1 Installation

```bash
# Install Prowler (Python-based)
pip3 install prowler

# Verify
prowler --version

# Alternative: Docker
docker run -it --rm toniblyx/prowler --version

# From source
git clone https://github.com/prowler-cloud/prowler
cd prowler && pip3 install .
```

## 1.2 AWS Credentials Configuration

```bash
# Method 1: AWS CLI profile (preferred)
aws configure --profile prowler-audit
# Enter: Access Key ID, Secret Access Key, Region, Output format

# Run Prowler with the profile
prowler aws --profile prowler-audit

# Method 2: Environment variables
export AWS_ACCESS_KEY_ID="AKIA..."
export AWS_SECRET_ACCESS_KEY="..."
export AWS_DEFAULT_REGION="us-east-1"
prowler aws

# Method 3: IAM Role (for assumed role / cross-account)
prowler aws --role arn:aws:iam::123456789:role/ProwlerAuditRole

# Method 4: Instance metadata (when running on EC2 with an IAM role attached)
prowler aws   # Automatically uses instance metadata credentials
```

## 1.3 Required IAM Permissions

Prowler works best with read-only permissions. The minimum required policy is:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:Get*",
        "iam:List*",
        "iam:Generate*",
        "s3:Get*",
        "s3:List*",
        "ec2:Describe*",
        "cloudtrail:Get*",
        "cloudtrail:Describe*",
        "cloudtrail:List*",
        "config:Get*",
        "config:Describe*",
        "config:List*"
      ],
      "Resource": "*"
    }
  ]
}
```

> [!TIP]
> AWS provides a managed policy `arn:aws:iam::aws:policy/SecurityAudit` that Prowler's documentation recommends. For full coverage, also attach `arn:aws:iam::aws:policy/job-function/ViewOnlyAccess`.

---

# PHASE 2: CORE AWS CHECKS

---

## 2.1 Running a Full AWS Scan

```bash
# Full scan of all AWS services and checks
prowler aws

# Scan specific services only
prowler aws --service iam
prowler aws --service s3
prowler aws --service ec2
prowler aws --service cloudtrail
prowler aws --service rds

# Scan multiple services
prowler aws --service iam s3 ec2

# Scan all regions (default is configured region)
prowler aws --regions us-east-1 us-west-2 eu-west-1

# Output formats
prowler aws --output-formats csv json html   # Multiple formats
prowler aws -o /tmp/prowler_results/          # Custom output directory
```

## 2.2 Critical AWS Checks by Category

### IAM
```
iam_root_hardware_mfa_enabled          — Root account must have hardware MFA
iam_root_mfa_enabled                   — Root account MFA check
iam_user_mfa_enabled_console_access    — All console users must have MFA
iam_password_policy_*                  — Password policy strength checks
iam_no_root_access_key                 — Root account access keys must not exist
iam_user_accesskey_unused              — Unused access keys (>90 days)
iam_policy_attached_only_to_groups_or_roles — No direct policy attachments to users
```

### S3
```
s3_bucket_public_access_block_*        — Public access block settings
s3_bucket_acl_prohibit_public_read     — No public read ACLs
s3_bucket_default_encryption           — Server-side encryption required
s3_bucket_versioning_enabled           — Versioning for data protection
s3_bucket_secure_transport_policy      — Force HTTPS (deny HTTP requests)
s3_bucket_object_lock                  — Immutability for compliance
```

### EC2
```
ec2_securitygroup_allow_ingress_from_internet_to_all_ports  — Open security groups
ec2_instance_public_ip                 — Public IPs exposed
ec2_ebs_volume_encryption              — EBS volume encryption
ec2_instance_imdsv2_enabled            — IMDSv2 required (SSRF protection)
```

### CloudTrail
```
cloudtrail_multi_region_enabled        — Multi-region logging required
cloudtrail_log_file_validation_enabled — Log integrity validation
cloudtrail_s3_dataevents_read_enabled  — S3 data event logging
```

---

# PHASE 3: IAM & PRIVILEGE ANALYSIS

---

## 3.1 IAM Findings to Prioritize

```bash
# Run IAM-only scan and view results
prowler aws --service iam --output-formats json -o /tmp/
cat /tmp/prowler_*.json | jq '.[] | select(.status=="FAIL") | {check_id, region, resource, status_extended}'
```

**Critical IAM misconfigurations to understand:**

```
1. Root account access keys exist (CRITICAL)
   - Root should NEVER have programmatic access keys
   - Root should use hardware MFA

2. Users with inline policies (HIGH)
   - Inline policies bypass SCPs and are hard to audit
   - All permissions should be in managed policies on groups

3. Overprivileged policies — AdministratorAccess attached to users/roles (CRITICAL)
   - Principle of least privilege violated
   - Attack surface for privilege escalation

4. Cross-account roles without external ID (MEDIUM)
   - Confused deputy vulnerability
   - Should always require ExternalId for cross-account trust

5. IAM Access Keys not rotated > 90 days (HIGH)
   - Stale keys are risk — they survive employee departures
```

## 3.2 Generating IAM Credential Report

```bash
# Prowler check: iam_generate_credential_report
# This triggers AWS to generate the credential report, then Prowler analyzes it

# Also generate manually to see raw data
aws iam generate-credential-report
aws iam get-credential-report --query Content --output text | base64 -d | column -t -s,

# Shows for every user: password enabled, MFA active, access keys, last used dates
```

---

# PHASE 4: NETWORK & STORAGE SECURITY

---

## 4.1 Key Network Findings

```bash
# Security groups allowing unrestricted inbound access
prowler aws --check ec2_securitygroup_allow_ingress_from_internet_to_all_ports
prowler aws --check ec2_securitygroup_allow_ingress_from_internet_to_port_22   # SSH open to 0.0.0.0/0
prowler aws --check ec2_securitygroup_allow_ingress_from_internet_to_port_3389 # RDP open to 0.0.0.0/0

# VPC flow logs
prowler aws --check vpc_flow_logs_enabled

# Default VPC check (should not be used in production)
prowler aws --check ec2_vpc_default_security_group_with_no_inbound_outbound_traffic
```

## 4.2 S3 Bucket Enumeration as Attacker

```bash
# From an attacker's perspective with stolen credentials,
# enumerate S3 buckets for sensitive data
aws s3 ls s3://   # List all accessible buckets
aws s3 ls s3://bucket-name/ --recursive   # List contents
aws s3 cp s3://bucket-name/sensitive.txt .  # Download files

# Prowler checks that catch these exposures:
prowler aws --check s3_bucket_public_access_block_account
prowler aws --check s3_bucket_public_access_block_bucket
```

---

# PHASE 5: COMPLIANCE FRAMEWORK SCANS

---

```bash
# Scan against CIS AWS Benchmark (most common compliance framework)
prowler aws --compliance cis_1.5_aws

# SOC 2 compliance
prowler aws --compliance soc2_aws

# GDPR
prowler aws --compliance gdpr_aws

# PCI DSS
prowler aws --compliance pci_3.2.1_aws

# HIPAA
prowler aws --compliance hipaa_aws

# NIST 800-53
prowler aws --compliance nist_800_53_revision_5_aws

# List all available compliance frameworks
prowler aws --list-compliance

# Generate compliance report in HTML (for client deliverable)
prowler aws --compliance cis_1.5_aws --output-formats html -o /tmp/report/
```

---

# PHASE 6: AZURE & GCP COVERAGE

---

```bash
# Azure scan
# First authenticate: az login
prowler azure --sp-env-auth   # Service Principal via environment variables
prowler azure --service iam storage network

# GCP scan
# First authenticate: gcloud auth application-default login
prowler gcp
prowler gcp --project-id my-project-123 --service iam compute storage
```

**Key Azure checks:**
```
azure_iam_user_mfa_enabled              — MFA for all users
azure_storage_account_public_access     — No public blob access
azure_sql_server_auditing_enabled       — SQL audit logging
azure_key_vault_logging_enabled         — Key Vault access logging
azure_network_security_group_ssh_access — SSH open to internet
```

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — AWS Account Audit:** Run `prowler aws` against an AWS free tier account (your own, or a lab account). Review all FAIL findings. Categorize by severity. Identify and fix the top 5 critical findings. Re-run to confirm remediation.

- [ ] **Lab 2 — IAM Misconfiguration:** Deliberately create a vulnerable IAM user: no MFA, access key older than 90 days, AdministratorAccess attached directly. Run `prowler aws --service iam`. Confirm all 3 issues are flagged. Then remediate and re-scan.

- [ ] **Lab 3 — S3 Exposure Scenario:** Create an S3 bucket with public read access. Upload a "sensitive" test file. Run `prowler aws --service s3`. Document which checks flag it. Then practice the attacker's workflow: use `aws s3 ls` and `aws s3 cp` to demonstrate how an attacker would access the exposed data.

- [ ] **Lab 4 — Compliance Report:** Run a CIS Benchmark scan against your AWS account. Generate an HTML report. Write a 1-page executive summary of the findings, prioritizing the top 3 issues, their risk, and recommended remediation. This is exactly what a cloud pentest report looks like.

---

## 📝 Operational Notes

- **Prowler vs ScoutSuite:** ScoutSuite is an alternative cloud auditing tool by NCC Group. Both cover similar ground. Prowler has broader compliance framework coverage and faster check development. ScoutSuite's HTML reports are sometimes more client-friendly. Know both exist.
- **Rate limiting:** Prowler makes many API calls. AWS may rate-limit you. Use `--log-level ERROR` to suppress noise. For large accounts, scan service-by-service rather than all at once.
- **Attacker perspective:** Run Prowler with compromised IAM credentials on a pentest to understand the victim's cloud posture from the inside. The findings tell you what misconfigurations to exploit — Prowler does your reconnaissance automatically.
- **Prowler in CI/CD:** Prowler integrates with GitHub Actions, AWS CodePipeline, and similar CI/CD systems. A DevSecOps pipeline that runs Prowler on every infrastructure change catches misconfigurations before they reach production.
- **Cost awareness:** Prowler's read-only API calls have minimal cost, but some checks (like generating credential reports or querying AWS Config) can trigger service costs in large organizations. Know which checks are expensive before running in production accounts.
