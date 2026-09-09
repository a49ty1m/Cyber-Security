# 🛡️ tfsec: Complete Mastery Checklist

> **What is tfsec?** tfsec is an open-source, Terraform-focused static analysis security scanner. It analyzes Terraform HCL code to identify security misconfigurations, insecure defaults, and violations of security best practices — specifically within Terraform infrastructure definitions. Unlike Checkov (which is multi-framework), tfsec is purpose-built for Terraform, resulting in deeper Terraform-specific checks, better false positive rates, and tighter integration with Terraform's module system.
>
> **Why does it exist?** Terraform is the dominant IaC tool, and Terraform configurations frequently contain security misconfigurations (open security groups, unencrypted storage, over-permissive IAM). tfsec provides Terraform-native static analysis that can be run locally, in CI/CD, and as a pre-commit hook — shifting security left before `terraform apply` ever runs.
>
> **When to use it:** Any Terraform-based infrastructure project, paired with Checkov for complementary coverage, in CI/CD pipelines to block misconfigured infrastructure from reaching production, and during code review of Terraform modules.
>
> **When to avoid it:** tfsec only understands Terraform HCL. For CloudFormation, Kubernetes YAML, Dockerfiles, or other IaC formats, use Checkov instead. For runtime cloud security assessment (scanning deployed infrastructure), use Prowler.
>
> **What mastering tfsec unlocks:** Terraform security analysis proficiency, ability to enforce security standards in Terraform-based DevSecOps pipelines, complementary coverage to Checkov for comprehensive IaC security, and practical skills for cloud security engineering roles.
>
> **Roadmap Stage / Module:** Shelf: Module S13 (DevSecOps & Secure SDLC — IaC)

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| IaC Security | Cloud Assessment | Secrets Scanning |
|:------------|:----------------|:-----------------|
| [✅ Checkov](Checkov.md) | [☁️ Prowler](Prowler.md) | [🕵️ Gitleaks](Gitleaks.md) |
| **🛡️ tfsec** (you are here) | | [🔎 TruffleHog](TruffleHog.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & First Scan | 4 | 1 hour |
| 2 | Core Terraform Checks | 7 | 2–3 hours |
| 3 | Module & Variable Analysis | 5 | 2–3 hours |
| 4 | Custom Checks | 6 | 3–4 hours |
| 5 | CI/CD Integration | 4 | 1–2 hours |
| 6 | tfsec vs Checkov — Combined Workflow | 4 | 1–2 hours |
| 7 | Practical Labs | 4 | 3–4 hours |
| | **Total** | **34** | **~13–19 hours** |

**Prerequisites:** Terraform basics (HCL syntax, resource/module/variable concepts). Phase 1 Linux CLI. Phase 8 DevSecOps context. Checkov.md read first (overlapping concepts).

---

# PHASE 1: INSTALLATION & FIRST SCAN

---

## 1.1 Installation

```bash
# Option 1: Binary download (recommended — fast, no dependencies)
curl -s https://raw.githubusercontent.com/aquasecurity/tfsec/master/scripts/install_linux.sh | bash
tfsec --version

# Option 2: Go install
go install github.com/aquasecurity/tfsec/cmd/tfsec@latest

# Option 3: Docker
docker run --rm -it -v "$(pwd):/src" aquasec/tfsec /src

# Option 4: Homebrew
brew install tfsec

# Option 5: Package managers
snap install tfsec
```

## 1.2 First Scan

```bash
# Scan current directory
tfsec .

# Scan a specific directory
tfsec /path/to/terraform/

# Scan with specific output format
tfsec . --format json
tfsec . --format sarif
tfsec . --format markdown
tfsec . --format junit

# Save output to file
tfsec . --out results.json --format json

# Show only specific severities
tfsec . --minimum-severity HIGH     # Only HIGH and CRITICAL findings
tfsec . --minimum-severity MEDIUM   # MEDIUM, HIGH, and CRITICAL

# Exit code 1 if issues found (for CI/CD)
tfsec . ; echo "Exit: $?"
```

## 1.3 Understanding tfsec Output

```
Result #1 HIGH Security group rule allows ingress from public internet.
─────────────────────────────────────────────────────────────────────────
  ID            aws-ec2-no-public-ingress-sgr
  Impact        Your port exposed to the internet
  Resolution    Set a more restrictive cidr range

  main.tf:10-14
    10 | resource "aws_security_group_rule" "allow_all" {
    11 |   type        = "ingress"
    12 |   from_port   = 0
    13 |   to_port     = 65535
    14 |   cidr_blocks = ["0.0.0.0/0"]    <-- This is the issue
    15 | }

  ID  aws-ec2-no-public-ingress-sgr
  Links:
    - https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/security_group_rule
    - https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html

Results: 1 potential problem(s) detected.
```

---

# PHASE 2: CORE TERRAFORM CHECKS

---

## 2.1 AWS Security Checks (Most Frequently Triggered)

```
aws-ec2-no-public-ingress-sgr        — Security group allows 0.0.0.0/0 ingress
aws-ec2-no-public-ip-subnet          — VPC subnet auto-assigns public IPs
aws-ec2-add-description-to-security-group — SG lacks description (hygiene)
aws-ec2-enable-at-rest-encryption    — EBS volumes not encrypted
aws-ec2-no-secrets-in-user-data      — Credentials in EC2 user data

aws-s3-enable-bucket-encryption      — S3 bucket not encrypted
aws-s3-enable-bucket-logging         — S3 bucket without access logging
aws-s3-enable-versioning             — S3 bucket versioning disabled
aws-s3-no-public-access-with-acl     — S3 bucket allows public ACL
aws-s3-block-public-acls             — S3 block public ACLs disabled

aws-iam-no-policy-wildcards          — IAM policy uses wildcard actions
aws-iam-enforce-mfa                  — IAM user requires MFA for console access
aws-iam-enforce-group-mfa            — IAM group policy requires MFA
aws-iam-block-kms-policy-documents   — IAM policy allows full KMS control

aws-rds-enable-performance-insights  — RDS Performance Insights disabled
aws-rds-encrypt-instance-storage-data — RDS instance not encrypted
aws-rds-no-public-db-access          — RDS instance is publicly accessible

aws-cloudtrail-enable-all-regions    — CloudTrail not multi-region
aws-cloudtrail-enable-log-validation — CloudTrail log validation disabled

aws-eks-enable-control-plane-logging — EKS control plane logging disabled
aws-eks-no-public-cluster-access     — EKS cluster API endpoint public
```

## 2.2 Azure & GCP Checks

```
azure-storage-enforce-https          — Azure storage account allows HTTP
azure-storage-queue-services-logging — Queue storage logging disabled
azure-network-ssh-blocked-from-internet — NSG allows SSH from internet
azure-sql-enable-audit               — SQL Server auditing disabled

google-storage-no-public-access      — GCS bucket public access allowed
google-compute-no-public-ip          — Compute instance has public IP
google-gke-enable-stackdriver-logging — GKE cluster logging disabled
```

---

# PHASE 3: MODULE & VARIABLE ANALYSIS

---

## 3.1 Scanning Modules

```bash
# tfsec automatically follows module references in your code
# Both inline and from Terraform Registry

# Scan with module resolution enabled
tfsec . --include-ignored

# If using local modules:
tfsec /path/to/root/ --workspace staging
```

## 3.2 Variable Analysis

tfsec understands Terraform variables and can trace insecure values:

```hcl
# tfsec detects even when values come from variables
variable "sg_cidr" {
  default = "0.0.0.0/0"   # Insecure default
}

resource "aws_security_group_rule" "example" {
  cidr_blocks = [var.sg_cidr]   # tfsec traces var.sg_cidr → "0.0.0.0/0" → FAIL
}
```

## 3.3 Ignoring Specific Issues

```hcl
# Inline ignore for a specific check
resource "aws_s3_bucket" "logs" {
  #tfsec:ignore:aws-s3-enable-bucket-logging   (logs bucket doesn't need logging)
  bucket = "access-logs"
}

# Ignore with expiry (force re-review after 6 months)
#tfsec:ignore:aws-ec2-no-public-ip-subnet:exp:2024-12-31

# Ignore all issues in a resource
resource "aws_security_group" "dev_only" {
  #tfsec:ignore:*
  name = "dev-testing"
}
```

---

# PHASE 4: CUSTOM CHECKS

---

## 4.1 Custom Checks in JSON/YAML

```yaml
# custom_checks/no_rdp_from_internet.yaml
checks:
  - code: CUS001
    description: Security group rule should not allow RDP from internet
    impact: Exposing RDP to the internet allows brute force attacks
    resolution: Restrict RDP to specific IPs or use VPN
    requiredTypes:
      - resource
    requiredLabels:
      - aws_security_group_rule
    severity: CRITICAL
    errorMessage: "Security group allows RDP (port 3389) from internet"
    matchSpec:
      action: and
      predicateMatchSpec:
        - name: to_port
          action: equals
          value: 3389
        - name: cidr_blocks
          action: contains
          value: "0.0.0.0/0"
        - name: type
          action: equals
          value: ingress
```

```bash
# Run with custom checks directory
tfsec . --custom-check-dir custom_checks/

# List all available checks
tfsec . --list-all-checks
```

---

# PHASE 5: CI/CD INTEGRATION

---

```yaml
# .github/workflows/tfsec.yml
name: tfsec IaC Security Scan

on:
  push:
  pull_request:

jobs:
  tfsec:
    name: tfsec Terraform Scan
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run tfsec
        uses: aquasecurity/tfsec-action@v1.0.0
        with:
          working_directory: ./terraform
          format: sarif
          soft_fail: false          # Fail build on findings
          minimum_severity: HIGH    # Only fail on HIGH+

      # Alternative: binary approach
      - name: Install and Run tfsec
        run: |
          curl -s https://raw.githubusercontent.com/aquasecurity/tfsec/master/scripts/install_linux.sh | bash
          tfsec ./terraform \
            --format sarif \
            --out tfsec.sarif \
            --minimum-severity HIGH

      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: tfsec.sarif
        if: always()
```

---

# PHASE 6: TFSEC VS CHECKOV — COMBINED WORKFLOW

---

## 6.1 Differences at a Glance

| Feature | tfsec | Checkov |
|:--------|:------|:--------|
| **Scope** | Terraform only | Terraform, K8s, CF, Docker, Ansible, Helm |
| **Performance** | Very fast (Go binary) | Slower (Python) |
| **Module support** | Deep — traces through modules | Good |
| **Custom checks** | YAML/JSON checks | Python checks (more flexible) |
| **Variable tracing** | Strong | Good |
| **False positives** | Lower for Terraform | Broader scope, slightly higher |
| **SARIF output** | Yes | Yes |
| **Active development** | Yes (Aqua Security) | Yes (Palo Alto) |

## 6.2 Combined CI/CD Pipeline

```yaml
# Run both for comprehensive coverage
jobs:
  iac-security:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: tfsec (Terraform-specific deep analysis)
        uses: aquasecurity/tfsec-action@v1.0.0
        with:
          soft_fail: true      # Don't fail yet — collect all results

      - name: Checkov (Multi-framework breadth)
        uses: bridgecrewio/checkov-action@master
        with:
          framework: terraform,helm,kubernetes
          soft_fail: true

      - name: Fail if critical findings
        run: |
          # Both tools output SARIF — merge and analyze
          cat tfsec.sarif checkov.sarif | jq '
            [.runs[].results[] | select(.level == "error")]
            | length
          ' | xargs -I{} test {} -eq 0 || exit 1
```

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — Deliberately Vulnerable Terraform:** Write Terraform code that creates: an open security group (0.0.0.0/0 on all ports), an unencrypted S3 bucket with public access, an EC2 instance with a public IP. Run tfsec. Document every finding. Fix each issue and re-scan to pass.

- [ ] **Lab 2 — tfsec vs Checkov Coverage Comparison:** Take the same Terraform code from Lab 1. Run tfsec and Checkov independently. Create a table comparing: which checks each tool flags, which are unique to each tool, and false positive rate. Conclude which is more appropriate for your lab infrastructure stack.

- [ ] **Lab 3 — Custom Check:** Write a custom tfsec YAML check that detects Terraform code creating an `aws_db_instance` resource with `publicly_accessible = true`. Test it against compliant and non-compliant code. Add it to your CI/CD pipeline.

- [ ] **Lab 4 — Full IaC Security Pipeline:** Build a GitHub Actions pipeline that runs tfsec AND Checkov on a Terraform project. Both must pass for the pipeline to succeed. Include `tfsec.ignore` annotations for 2 accepted-risk findings with justification comments. Document the pipeline in the repository README.

---

## 📝 Operational Notes

- **`tfsec` is now `trivy config`:** Aqua Security has migrated tfsec's functionality into their Trivy tool (`trivy config .` for IaC scanning). tfsec still works and is actively maintained, but new features are going into Trivy. Know both commands.
- **Terraform workspace support:** Use `tfsec . --workspace production` to set the Terraform workspace context — affects workspace-conditional configurations.
- **`--exclude` flag:** Skip specific check IDs without inline ignores: `tfsec . --exclude aws-s3-enable-bucket-logging,aws-ec2-add-description-to-security-group`. Use for accepted-risk suppressions that apply to the whole codebase.
- **Concise output:** Add `--concise-output` for a summarized result table instead of full finding details — useful for large codebases with many findings where the full output is overwhelming.
- **Integration with `terraform plan`:** tfsec can scan `terraform plan` JSON output for more accurate analysis: `terraform plan -out plan.tfplan && terraform show -json plan.tfplan | tfsec - --format json`. This resolves variables at scan time for better accuracy.
