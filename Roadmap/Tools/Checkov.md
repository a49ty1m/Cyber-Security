# ✅ Checkov: Complete Mastery Checklist

> **What is Checkov?** Checkov is an open-source static analysis tool for Infrastructure as Code (IaC) — it scans Terraform, CloudFormation, Kubernetes YAML, Dockerfiles, Helm charts, Ansible, ARM templates, and more to find security misconfigurations before infrastructure is deployed. With 1,000+ built-in checks covering CIS Benchmarks, NIST, SOC 2, PCI DSS, and custom policies, Checkov prevents the cloud misconfigurations that Prowler would find after deployment.
>
> **Why does it exist?** Cloud infrastructure misconfigurations (open security groups, unencrypted S3 buckets, over-privileged IAM roles) are far cheaper to fix in code than in a deployed environment. Checkov shifts security left — finding issues in the IaC templates before `terraform apply` runs, not after the vulnerable infrastructure exists in production.
>
> **When to use it:** Any DevSecOps pipeline that uses IaC (Terraform, CloudFormation, Kubernetes). Run Checkov in CI/CD to fail builds when misconfigurations are introduced. Run against existing IaC codebases to find legacy issues. Use alongside tfsec for complementary Terraform-specific coverage.
>
> **When to avoid it:** Checkov scans configuration, not runtime state. It can't find misconfigurations in manually-provisioned infrastructure (use Prowler for that). For deep Kubernetes runtime security, use Falco or OPA/Gatekeeper in the cluster.
>
> **What mastering Checkov unlocks:** Ability to enforce security standards in IaC codebases via CI/CD gates, understanding of the most common cloud security misconfigurations at the code level, and the Phase 8 exit gate IaC security component.
>
> **Roadmap Stage / Module:** Shelf: Module S13 (DevSecOps & Secure SDLC — IaC)

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| IaC Security | Secrets Scanning | SAST |
|:------------|:----------------|:-----|
| **✅ Checkov** (you are here) | [🕵️ Gitleaks](Gitleaks.md) | [🔍 Semgrep](Semgrep.md) |
| [🛡️ tfsec](tfsec.md) | [🔎 TruffleHog](TruffleHog.md) | |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & First Scan | 4 | 1 hour |
| 2 | Terraform Checks | 8 | 3–4 hours |
| 3 | Kubernetes & Dockerfile Checks | 6 | 2–3 hours |
| 4 | Custom Policies | 7 | 3–4 hours |
| 5 | CI/CD Integration | 5 | 2–3 hours |
| 6 | Baseline & Suppression | 4 | 1–2 hours |
| 7 | Practical Labs | 4 | 3–5 hours |
| | **Total** | **38** | **~15–22 hours** |

**Prerequisites:** Basic Terraform or CloudFormation knowledge. Phase 1 Linux CLI. Phase 8 DevSecOps context.

---

# PHASE 1: INSTALLATION & FIRST SCAN

---

## 1.1 Installation

```bash
# Install via pip
pip3 install checkov

# Verify
checkov --version

# Docker
docker run --rm -v "${PWD}:/tf" bridgecrew/checkov -d /tf

# With Terraform scanner specifically
pip3 install checkov[terraform]
```

## 1.2 First Scan

```bash
# Scan a directory with Terraform files
checkov -d /path/to/terraform/

# Scan a single file
checkov -f main.tf

# Scan Kubernetes YAML
checkov -d /path/to/k8s/ --framework kubernetes

# Scan Dockerfile
checkov -f Dockerfile --framework dockerfile

# Specify framework explicitly
checkov -d . --framework terraform
checkov -d . --framework cloudformation
checkov -d . --framework kubernetes
checkov -d . --framework helm
checkov -d . --framework ansible

# Auto-detect (scans all supported frameworks in the directory)
checkov -d .

# Output formats
checkov -d . --output json > checkov-results.json
checkov -d . --output sarif > checkov-results.sarif
checkov -d . --output junit-xml > results.xml
```

---

# PHASE 2: TERRAFORM CHECKS

---

## 2.1 Common Terraform Misconfigurations Checkov Detects

```
AWS:
CKV_AWS_18  — S3 bucket access logging enabled
CKV_AWS_19  — S3 bucket server-side encryption enabled
CKV_AWS_20  — S3 bucket does not allow public ACL read
CKV_AWS_21  — S3 versioning enabled
CKV_AWS_23  — EC2 EBS volume encryption enabled
CKV_AWS_24  — IAM policy does not allow wildcard actions (*:*)
CKV_AWS_25  — Security group does not allow ingress from 0.0.0.0/0 on all ports
CKV_AWS_40  — IAM user has no direct policy attachment
CKV_AWS_53  — S3 block public access at account level
CKV_AWS_58  — EKS node group instances are not publicly accessible
CKV_AWS_79  — EC2 instance does not have public IP
CKV_AWS_88  — EC2 instance IMDSv2 required
CKV_AWS_130 — VPC subnet does not auto-assign public IPs
CKV2_AWS_6  — S3 public access blocked at bucket level

Azure:
CKV_AZURE_12 — Storage account requires HTTPS
CKV_AZURE_16 — VM managed disks encrypted at rest
CKV_AZURE_50 — SQL server firewall does not allow all Azure services

GCP:
CKV_GCP_29 — GCS bucket uses uniform bucket-level access
CKV_GCP_62 — GCS bucket logging enabled
CKV_GCP_68 — GKE cluster nodes not publicly accessible
```

## 2.2 Running Specific Checks

```bash
# Run only specific check IDs
checkov -d . --check CKV_AWS_20,CKV_AWS_21

# Skip specific checks (known false positives or accepted risks)
checkov -d . --skip-check CKV_AWS_79,CKV_AWS_130

# Run checks for a specific compliance framework
checkov -d . --compliance cis_aws_v1.4
checkov -d . --compliance nist_800_53_rev_4
checkov -d . --compliance pci_dss_v321

# List all available checks
checkov --list-checks --framework terraform
```

## 2.3 Example Terraform Finding

```hcl
# BAD: S3 bucket without encryption or logging
resource "aws_s3_bucket" "data" {
  bucket = "my-company-data"
}
# Checkov FAIL: CKV_AWS_19 (no encryption), CKV_AWS_18 (no logging), CKV_AWS_20 (public ACL not blocked)

# GOOD: Secure S3 bucket
resource "aws_s3_bucket" "data" {
  bucket = "my-company-data"
}
resource "aws_s3_bucket_server_side_encryption_configuration" "data" {
  bucket = aws_s3_bucket.data.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
resource "aws_s3_bucket_versioning" "data" {
  bucket = aws_s3_bucket.data.id
  versioning_configuration { status = "Enabled" }
}
resource "aws_s3_bucket_public_access_block" "data" {
  bucket                  = aws_s3_bucket.data.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}
resource "aws_s3_bucket_logging" "data" {
  bucket        = aws_s3_bucket.data.id
  target_bucket = aws_s3_bucket.logs.id
  target_prefix = "s3-logs/"
}
# Checkov PASS: All checks green
```

---

# PHASE 3: KUBERNETES & DOCKERFILE CHECKS

---

## 3.1 Kubernetes Checks

```bash
# Common Kubernetes misconfigurations:
CKV_K8S_11  — Container CPU limits defined
CKV_K8S_12  — Container memory limits defined
CKV_K8S_14  — Container should not run as root user
CKV_K8S_15  — Image tag should not be 'latest'
CKV_K8S_20  — Container should not use privileged mode
CKV_K8S_28  — Container should not run with allowPrivilegeEscalation
CKV_K8S_30  — Container should have readOnlyRootFilesystem
CKV_K8S_35  — Container does not run as root (runAsNonRoot: true)
CKV_K8S_43  — No containers run as root (runAsUser != 0)
CKV2_K8S_6  — Pod not using host PID namespace
```

```yaml
# BAD Kubernetes pod spec
spec:
  containers:
    - name: app
      image: myapp:latest      # CKV_K8S_15: no "latest" tag
      securityContext:
        privileged: true       # CKV_K8S_20: privileged mode
        runAsUser: 0           # CKV_K8S_43: running as root

# GOOD Kubernetes pod spec
spec:
  containers:
    - name: app
      image: myapp:1.2.3       # Pinned tag
      securityContext:
        privileged: false
        runAsUser: 1000
        runAsNonRoot: true
        allowPrivilegeEscalation: false
        readOnlyRootFilesystem: true
        capabilities:
          drop: ["ALL"]
      resources:
        limits:
          cpu: "500m"
          memory: "512Mi"
```

## 3.2 Dockerfile Checks

```bash
CKV_DOCKER_1  — ADD instead of COPY (ADD has unintended URL fetch behavior)
CKV_DOCKER_2  — Use a non-root user in DOCKERFILE
CKV_DOCKER_3  — Trusted base image registry
CKV_DOCKER_5  — Avoid using 'latest' tag for base image
CKV_DOCKER_6  — No HEALTHCHECK instruction defined
CKV_DOCKER_7  — Use explicit package version pinning in apt-get
CKV_DOCKER_9  — Sensitive information in ARG (passwords in build args)
```

```dockerfile
# BAD Dockerfile
FROM ubuntu:latest             # CKV_DOCKER_5: latest tag
ADD scripts.tar.gz /app/       # CKV_DOCKER_1: use COPY instead
RUN apt-get install -y python3 # CKV_DOCKER_7: no version pinning
# Running as root (implicit) — CKV_DOCKER_2

# GOOD Dockerfile
FROM ubuntu:22.04              # Pinned tag
COPY scripts/ /app/            # COPY instead of ADD
RUN apt-get install -y python3=3.10.6-1ubuntu0.2  # Pinned version
RUN useradd -m -s /bin/bash appuser
USER appuser                   # Non-root user
HEALTHCHECK CMD curl -f http://localhost:8080/health || exit 1
```

---

# PHASE 4: CUSTOM POLICIES

---

```python
# Custom Checkov check in Python
# File: custom_checks/check_no_admin_policy.py

from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories

class NoAdminPolicy(BaseResourceCheck):
    def __init__(self):
        name = "Ensure IAM policies do not have AdministratorAccess"
        id = "CKV_CUSTOM_1"
        supported_resources = ['aws_iam_policy', 'aws_iam_role_policy']
        categories = [CheckCategories.IAM]
        super().__init__(name=name, id=id, categories=categories,
                        supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        policy_doc = conf.get('policy', [{}])[0]
        if isinstance(policy_doc, str):
            import json
            policy_doc = json.loads(policy_doc)
        
        for statement in policy_doc.get('Statement', []):
            if statement.get('Effect') == 'Allow':
                actions = statement.get('Action', [])
                if isinstance(actions, str):
                    actions = [actions]
                if '*' in actions or 'AdministratorAccess' in actions:
                    return CheckResult.FAILED
        return CheckResult.PASSED

check = NoAdminPolicy()
```

```bash
# Run with custom check directory
checkov -d . --external-checks-dir custom_checks/
```

---

# PHASE 5: CI/CD INTEGRATION

---

```yaml
# .github/workflows/checkov.yml
name: IaC Security Scan

on:
  push:
  pull_request:

jobs:
  checkov:
    name: Checkov IaC Scan
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Run Checkov
        uses: bridgecrewio/checkov-action@master
        with:
          directory: .
          framework: terraform
          soft_fail: false                         # Fail build on findings
          output_format: sarif
          output_file_path: checkov-results.sarif
          skip_check: CKV_AWS_130                  # Skip accepted-risk checks

      - name: Upload SARIF
        uses: github/codeql-action/upload-sarif@v3
        with:
          sarif_file: checkov-results.sarif
        if: always()

      # Alternative: binary approach
      - name: Checkov (Binary)
        run: |
          pip install checkov
          checkov -d . \
            --framework terraform \
            --output sarif \
            --output-file-path checkov-results.sarif \
            --compact \
            --hard-fail-on CRITICAL,HIGH    # Only fail on critical/high findings
```

---

# PHASE 6: BASELINE & SUPPRESSION

---

```bash
# Create a baseline (snapshot of current findings to suppress known issues)
checkov -d . --create-baseline
# Creates: .checkov.baseline file

# Run with baseline (only reports NEW findings, not baseline issues)
checkov -d . --baseline .checkov.baseline

# Inline suppression in Terraform code
resource "aws_s3_bucket" "logs" {
  bucket = "my-logs-bucket"
  # checkov:skip=CKV_AWS_18:Logging bucket doesn't need access logging (circular dependency)
  # checkov:skip=CKV_AWS_21:Logging bucket versioning not required
}

# Inline suppression in Kubernetes YAML
metadata:
  annotations:
    checkov.io/skip1: "CKV_K8S_20=Privileged mode required for storage driver"
```

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — Vulnerable Terraform Scan:** Write a Terraform configuration for an AWS environment with deliberately insecure settings (public S3 bucket, open security group, unencrypted RDS). Run Checkov. Identify and categorize all findings. Fix each issue and verify Checkov passes.

- [ ] **Lab 2 — Kubernetes Hardening:** Take any sample Kubernetes deployment YAML (from a public Helm chart). Run Checkov against it. Fix the top 5 most critical findings. Document what each fix does and why it improves security.

- [ ] **Lab 3 — Custom Policy:** Write a custom Checkov check in Python that detects Terraform resources creating EC2 security groups allowing ingress on port 3389 (RDP) from 0.0.0.0/0. Test it against compliant and non-compliant Terraform code. Verify it fires correctly.

- [ ] **Lab 4 — CI/CD Gate (Phase 8 Exit Gate):** Create a GitHub repository with vulnerable Terraform code. Build a GitHub Actions pipeline that runs Checkov and fails on HIGH/CRITICAL findings. Verify the pipeline fails. Fix the Terraform code. Verify the pipeline passes. Document the full workflow in a README.

---

## 📝 Operational Notes

- **Checkov vs tfsec:** Checkov is multi-framework (Terraform, CloudFormation, Kubernetes, Dockerfile, Ansible, Helm). tfsec is Terraform-specific but has deeper Terraform knowledge and faster performance. Use both together for comprehensive Terraform IaC security — they have complementary check coverage.
- **`--compact` flag:** By default, Checkov prints full resource code for each finding. `--compact` shows just the finding ID and resource name — much easier to read for large reports.
- **Terraform plan scanning:** Checkov can scan a Terraform plan JSON (`terraform plan -out plan.json && terraform show -json plan.json > plan.json`). This gives more accurate results than scanning `.tf` files, because it reflects the actual state after variable substitution.
- **SCA (Software Composition Analysis):** Checkov also scans package files (`requirements.txt`, `package.json`, `go.mod`) for known CVEs in dependencies — similar to OWASP Dependency-Check. This is enabled automatically in the default scan.
- **Prisma Cloud integration:** Checkov is maintained by Palo Alto Networks (formerly Bridgecrew). It integrates with Prisma Cloud for centralized policy management, but is fully functional and free as a standalone open-source tool.
