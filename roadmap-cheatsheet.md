# Red Team Roadmap — Cheat Sheet (2026)

**Quick Jump**
- Core: Fundamentals → Networking → Recon/Scanning/Enumeration → System Hacking → Malware/C2 → Detection → Social Eng → DoS → WebApp/WebServer → IDS/FW → Wireless → Mobile → Crypto → Cloud → Forensics → Bug Bounty
- Advanced: OSINT → Adversary Emulation → Containers/K8s → OT/ICS → Hardware/Embedded → AI/LLM → AD/Entra → Modern Exploitation → Ops/Tradecraft

---
## Core Flow (10 bullets)
1) **Recon/Intel:** OSINT, subdomains (Amass/Subfinder), CT logs, Shodan/Censys.
2) **Scanning:** Nmap `-sS -sV -sC -Pn --min-rate 2000`; UDP `-sU --top-100`; vuln NSE `--script vuln` cautiously.
3) **Web App:** OWASP Top 10 + auth/logic + SSRF → IMDS; file upload bypass; GraphQL introspection; IDOR/BOLA; mass assignment.
4) **Cred Attacks:** Spray (safe lockout), STS reuse, MFA fatigue, default creds; wordlists + rules; OTP fatigue.
5) **Initial Access:** Phish (HTML smuggle, OneNote/ISO/LNK), waterhole, drive-by, maldocs/macros, payload staging (Sliver/Havoc/Mythic/Brute Ratel/CS/Metasploit).
6) **PrivEsc:** Windows (UAC bypass, services, tokens, DLL hijack, kernel); Linux (sudo/SUID/caps/cron/systemd); Container/K8s (docker.sock, privileged, hostPath, RBAC gaps); Cloud (AssumeRole, metadata).
7) **Lateral & Persistence:** Pass-the-Hash/Ticket, RDP/WinRM/SMB/WMI, SSH agent hijack, GPO/script/cron/scheduled tasks; SaaS-to-SaaS pivots with OAuth tokens.
8) **Evasion & Exfil:** Sleep obfuscation, call-stack spoofing, indirect syscalls; log tamper; DNS/HTTPS/Cloud API covert exfil; cloud storage pre-signed URLs.
9) **Post-Exploitation:** Data theft impact (crown jewels), ransomware demo, cleanup per ROE, reporting mapped to MITRE/kill chain.
10) **Detection/Purple:** MTTD/MTTR, validated control effectiveness; collaborate live to tune detections.

---
## Identity & Directory (AD / Entra ID)
- **Enum:** Domains/forests, trusts, SPNs, OUs, ACLs, Tier0 assets; Entra apps/service principals, consented perms, CA policies.
- **Cred/Auth:** Kerberoast, AS-REP roast, NTLM relay (SMB/LDAP/HTTP/ADCS HTTP), token theft (TGT/TGS/OAuth/DPAPI/LSASS/browser).
- **Delegation/ACL:** Un/Constrained/RBCD; abuse WriteDACL/GenericAll/WriteOwner/AddMember; shadow creds (msDS-KeyCredentialLink).
- **ADCS:** ESC1-8 (enrollee supplies subject/SAN, weak EKUs); relays to HTTP enrollment; mint golden certs.
- **Hybrid/Cloud:** Illicit consent grants; legacy auth bypass; passkey/FIDO/SSPR abuse; Graph/SharePoint data for pivots; cross-cloud via app roles.

---
## AI & LLM Red Teaming
- **OWASP LLM 2025:** LLM01 Prompt Injection, LLM02 Sensitive Info Disclosure, LLM10 Unbounded Consumption (denial-of-wallet).
- **Adversarial:** Jailbreaks (role-play, crescendo, encoding), agent abuse (tool overreach), RAG poisoning (vector DB pollution), model extraction/inversion.
- **Tooling:** PyRIT, Garak, DeepTeam; log prompts/responses; regression suites after model/policy updates.

---
## Containers / K8s / Supply Chain
- **Container Breakout:** --privileged, CAP_SYS_ADMIN, docker.sock, hostPath, seccomp/AppArmor gaps.
- **K8s:** RBAC misuse, secrets theft (etcd/mount/env/SA token), API unauth, netpol bypass, pod escape via host PID/net.
- **Runtime:** Falco/Sysdig, OPA/Kyverno, Notary/Cosign, Calico/Cilium segmentation.
- **CI/CD:** Pipeline poisoning (GitHub Actions/Jenkins), dependency confusion, artifact signing (Sigstore/Cosign, SLSA provenance).
- **Automation (n8n/Zapier/Workato):** Workflow takeover (e.g., n8n CVE-2026-21858), credential aggregation (API keys, OAuth).

---
## Modern Exploitation (Part 29)
- **Recon/Triage:** Identify arch, mitigations (ASLR/DEP/PIE/RELRO/Canary/CFG/CET/PAC/BTI), symbols; fuzz (AFL++, libFuzzer, honggfuzz) with sanitizers.
- **Memory Bugs:** Overflow, UAF, double-free, OOB, type confusion; heap grooming (tcache/LFH); ROP/JOP/SROP/ret2libc; infoleaks to defeat ASLR.
- **Mitigation Bypass:** Canaries (leak), DEP (ROP), RELRO/PIE tricks; CFG/CET/PAC/BTI bypass (COOP, JIT spray, pointer auth bypass).
- **Advanced Targets:** Kernel (SMEP/SMAP/KASLR bypass, token stealing), Browsers/JS (JIT/IC/GC chains), Deserialization gadgets, Cloud/serverless (IMDS, sandbox escape).
- **Delivery/OPSEC:** Reflective loaders, indirect syscalls, sleep obfuscation, call-stack spoof, DLL hollowing, APC/ETW/AMSI tamper; telemetry shaping.
- **Safety:** Kill-switches, blast-radius limits, cleanup/rollback, time-bounded persistence.

---
## Crypto & Hashing (Modern)
- **Passwords:** Argon2id (tune memory 64–256 MB, iterations, parallelism) or strong bcrypt cost; per-user salts + server-side pepper.
- **Deprecate:** MD5/SHA-1/SHA-256 for password storage; low-iteration PBKDF2.
- **At Rest:** BitLocker/LUKS/FileVault; key custody via HSM/KMS; rotate keys.
- **Attacks:** Padding oracle, timing/side-channel; downgrade TLS; weak RNG; key management failures.

---
## C2 & Tradecraft (Modern)
- **Frameworks:** Sliver, Havoc, Mythic, Brute Ratel C4, plus Metasploit/CS (hardened profiles).
- **Cloud-Native C2:** Microsoft Graph/SharePoint, Slack/Teams webhooks, trusted APIs; redirectors/frontends.
- **Evasion:** Sleep obfuscation, call-stack spoofing, indirect syscalls, memory-only beacons.
- **IaC for Red Teams:** Terraform/Ansible for disposable infra (C2, redirectors, DNS/TLS, storage).

---
## Social Engineering (2026)
- **Deepfakes:** Voice/video for exec impersonation (vishing/meetings).
- **ClickFix/ClearFake:** Fake update errors prompting copy-paste PowerShell/terminal scripts.
- **MFA:** Test fatigue attacks; differentiate phishing-resistant (FIDO2/Passkeys) vs phishable (SMS/Push/OTP).

---
## Quick Commands & Checks
- **Nmap Fast TCP:** `nmap -Pn -sS -sV -sC --min-rate 2000 -p- target`
- **UDP Top 100:** `nmap -sU --top-100 --min-rate 500 target`
- **Web Fuzz:** `ffuf -u https://host/FUZZ -w /path/wordlist -mc all -fs 0`
- **Kerberoast (PowerShell):** `Invoke-Kerberoast -OutputFormat Hashcat`
- **BloodHound Collect:** `SharpHound.exe -c All` or `bloodhound-python -c All`
- **Cloud IMDS:** `curl 169.254.169.254/latest/meta-data/` (AWS) / metadata URLs (Azure/GCP)
- **Argon2id Test:** `python - <<'PY'` to benchmark params; choose memory/iters for target latency

---
## Reporting / Metrics
- Map to **MITRE ATT&CK** and **Kill Chain**; include **MTTD/MTTR** and **validated control effectiveness**; provide exec summary + technical chain + prioritized fixes.

---
## Minimal Prep Checklist
- Calibrate **wordlists**, **proxy/Burp**, **Sliver/Havoc/Mythic/BRc4** profiles, **OPSEC (sleep/jitter/obfuscation)**.
- Confirm **ROE/scope**, data handling, and cleanup plan.
- Set up **Terraform/Ansible** for infra; **logging plan** (what you’ll collect, what you’ll erase per ROE).
