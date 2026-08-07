# 🔑 jwt_tool: Complete Mastery Checklist

> **What is jwt_tool?** jwt_tool is a Python toolkit for testing, decoding, forging, and attacking JSON Web Tokens (JWTs). JWTs are the dominant authentication mechanism for modern web APIs and SPAs. jwt_tool supports every known JWT attack: algorithm confusion (RS256 → HS256), the `alg:none` bypass, key injection, brute-forcing weak HMAC secrets, and tampered claim testing. It integrates with Burp Suite via a proxy flag.
>
> **Why does it exist?** JWTs are widely misimplemented. The `alg:none` vulnerability and RS256→HS256 confusion attack are so common that a dedicated tool is essential. jwt_tool automates both the attack scanning and the manual token crafting required for JWT exploitation.
>
> **When to use it:** Any web application or API using JWT authentication. Whenever you intercept a JWT token and want to test its security. API pentesting and bug bounty. CTF web challenges with JWT auth.
>
> **What mastering jwt_tool unlocks:** Complete JWT attack surface testing. Understanding of every JWT vulnerability. Ability to forge tokens when the implementation is weak.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | Decoding and Analysis | 3 | 1–2 hours |
| 3 | Core Attacks | 5 | 3–4 hours |
| 4 | Secret Cracking | 3 | 2–3 hours |
| 5 | Advanced Attacks | 3 | 2–3 hours |
| 6 | Integration | 2 | 1 hour |
| 7 | Practical Labs | 3 | 3–5 hours |
| 8 | Mastery Challenges | 2 | 2–3 hours |
| | **Total** | **25** | **~15–23 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — JWT Structure

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Format** | `header.payload.signature` — three base64url-encoded parts joined by dots. |
| **Header** | `{"alg":"HS256","typ":"JWT"}` — algorithm and token type. |
| **Payload** | `{"sub":"1234","name":"alice","role":"user","iat":1234567890}` — claims. |
| **Signature** | `HMACSHA256(base64(header)+"."+base64(payload), secret)` — verifies integrity. |
| **Verification** | Server decodes header → knows algorithm → uses the appropriate key to verify signature. If valid → trusts the payload claims. |

---

### Task 1.2 — Common JWT Vulnerabilities

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **alg:none** | Header `"alg":"none"` → signature not verified. Any payload accepted. |
| **RS256 → HS256 Confusion** | RSA key pair: private (server signs) + public (server verifies). If you forge a token signed with the RS256 public key using HS256 (HMAC), and the server uses the public key as the HMAC secret → accepted. |
| **Weak Secret** | HS256/HS512 with weak/guessable secret → crack offline with hashcat. |
| **JWT Injection (kid/jku/x5u)** | Header parameters `kid`, `jku`, `x5u` — if user-controlled → specify attacker's key or file. |
| **Expired Tokens** | `exp` claim not validated → replay old tokens. |

---

### Task 1.3 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Install** | `git clone https://github.com/ticarpi/jwt_tool; pip3 install -r requirements.txt`. |
| **Run** | `python3 jwt_tool.py <token>`. |
| **Kali** | May be available: `pip3 install jwt_tool` or from the github. |

---

### Task 1.4 — Key Concepts

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **base64url** | JWT uses base64url (not standard base64): `+` → `-`, `/` → `_`, no padding `=`. |
| **Tamper Detection** | Any modification to header or payload invalidates the signature — unless the server doesn't verify it (alg:none) or you have the secret. |
| **Claim Priority** | `sub` = subject (user ID). `role`/`admin` = access level. `exp` = expiry. `iat` = issued at. `jti` = unique ID (prevents replay). |

---

# PHASE 2: DECODING AND ANALYSIS

---

### Task 2.1 — Decode a Token

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Command** | `python3 jwt_tool.py <token>`. Prints decoded header and payload. |
| **Online** | jwt.io — paste token → decoded (not for real engagements, sends token to third party). |
| **Manual** | `echo "base64_part" | base64 -d` (add padding if needed). |

---

### Task 2.2 — Identify Algorithm and Claims

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Algorithm** | Header `alg` field: `HS256`/`HS512` = HMAC (symmetric). `RS256`/`RS512` = RSA (asymmetric). `ES256` = ECDSA. `none` = no signature (bug if accepted). |
| **Target Claims** | Look for: `role`, `admin`, `is_admin`, `group`, `user_id`, `email`. These are attack targets — modify to escalate. |

---

### Task 2.3 — Scan for Vulnerabilities

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Command** | `python3 jwt_tool.py <token> -t http://target.com/api/endpoint -rh "Authorization: Bearer JWT" -M pb`. |
| **Playbook Scan** | `-M pb` — runs through all known JWT attacks automatically. Reports which attacks succeed. |

---

# PHASE 3: CORE ATTACKS

---

### Task 3.1 — alg:none Attack

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | `python3 jwt_tool.py <token> -X a`. Generates tokens with `alg:none` and empty signature. |
| **Claim Modification** | Add `-T` flag to tamper with claims before attack: `python3 jwt_tool.py <token> -X a -T`. |
| **Test** | Send the forged token. If accepted: server doesn't verify algorithm. |

---

### Task 3.2 — RS256 → HS256 Confusion

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Prerequisite** | Original token uses RS256. Get the server's RSA public key (often at `/.well-known/jwks.json`, `/.well-known/openid-configuration`, or in server response headers). |
| **Command** | `python3 jwt_tool.py <token> -X k -pk public_key.pem`. Signs the forged token with the public key as HMAC secret. Changes `alg` to HS256. |
| **Success** | If server confuses the public key as the HMAC secret → accepts the forged token. |

---

### Task 3.3 — Claim Tampering

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Interactive** | `python3 jwt_tool.py <token> -T` — interactive tamper mode. Prompts to modify each claim. Generates tokens with modified claims (still need the secret to re-sign). |
| **Use Case** | Tamper + alg:none = forge admin token without knowing secret. Tamper + known secret = re-sign with new claims. |

---

### Task 3.4 — jwks Injection (jku/x5u)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Concept** | JWT header `jku` parameter specifies URL of JWKS (JSON Web Key Set) that contains the signing key. If the server fetches from an attacker-controlled URL: serve malicious JWKS → sign token with corresponding private key → server accepts. |
| **Command** | `python3 jwt_tool.py <token> -X s -ju http://attacker.com/jwks.json`. Generates key pair, hosts JWKS (or tells you what to host), forges token signed with attacker's key. |

---

### Task 3.5 — kid Injection

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Concept** | `kid` (Key ID) header parameter tells the server which key to use. If used unsafely in SQL query (SQL injection) or path traversal: `kid: ../../../../dev/null` → server reads empty file as key → HMAC of empty string = known value → sign token accordingly. |
| **Test** | Try path traversal values in `kid`. Use `python3 jwt_tool.py <token> -T` to modify kid manually. |

---

# PHASE 4: SECRET CRACKING

---

### Task 4.1 — Brute Force with jwt_tool

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Command** | `python3 jwt_tool.py <token> -C -d wordlist.txt` — dictionary attack on HS256 secret. |
| **Wordlists** | `rockyou.txt`. Common JWT secrets: `secret`, `password`, `jwt_secret`, `your-256-bit-secret`. Try default secrets first. |

---

### Task 4.2 — Crack with Hashcat

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Mode** | Hashcat mode 16500 = JWT (HS256). `hashcat -m 16500 jwt.txt wordlist.txt`. |
| **Format** | Pass the full JWT as the hash: `hashcat -m 16500 "header.payload.signature" wordlist.txt`. |
| **Speed** | Much faster than jwt_tool for large wordlists (GPU). |

---

### Task 4.3 — Using Cracked Secret

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Forge** | With the secret: modify any claim → re-sign: `python3 jwt_tool.py <token> -T -S hs256 -p "cracked_secret"`. |
| **Escalate** | Change `"role":"user"` → `"role":"admin"`. Re-sign with cracked secret. Use forged token. |

---

# PHASE 5: ADVANCED ATTACKS

---

### Task 5.1 — Expired Token Replay

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Test** | Try sending an expired token. If accepted: `exp` claim not validated. |
| **Remove exp** | `python3 jwt_tool.py <token> -T` → remove/extend `exp` claim → re-sign if possible. |

---

### Task 5.2 — Embedded JWK Attack

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Concept** | RFC 7515 allows embedding a JWK (JSON Web Key) directly in the JWT header. If the server uses the embedded key for verification without validation → attacker embeds their own public key → signs with corresponding private key → accepted. |
| **Command** | `python3 jwt_tool.py <token> -X e` — embedded JWK injection. |

---

### Task 5.3 — Null Signature

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Test** | Remove the signature portion completely (keep trailing dot: `header.payload.`). Some implementations don't validate an absent signature. |
| **jwt_tool** | `-X n` — null signature attack. |

---

# PHASE 6: INTEGRATION

---

### Task 6.1 — Burp Suite Integration

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Proxy** | `python3 jwt_tool.py <token> -t http://target -rh "Authorization: Bearer JWT" -pr http://127.0.0.1:8080` — route requests through Burp. |
| **JWT Editor Extension** | Burp Extension: "JWT Editor" — directly in Burp: decode, modify, attack JWT tokens in intercepted requests. Install from BAppStore. |

---

### Task 6.2 — API Workflow

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Workflow** | Log in → get JWT → decode with jwt_tool → identify claims → run playbook scan → if vulnerable: forge admin token → test escalated access. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — DVWA / PortSwigger JWT Labs

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | PortSwigger Web Security Academy JWT labs (free). Work through: alg:none, RS256→HS256 confusion, JWKS injection. Use jwt_tool to exploit each. |
| **Success Criteria** | All 3 labs solved. Each attack technique documented. |

---

### Lab 7.2 — CTF JWT Challenge

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | CTF web challenge using JWT authentication. Decode token. Identify vulnerability. Exploit to get admin access or flag. |
| **Success Criteria** | Flag captured. Exact attack vector documented. |

---

### Lab 7.3 — JWT Secret Cracking

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| **Scenario** | Target with HS256 JWT and weak secret. Use jwt_tool + hashcat to crack. Forge an admin token. Get escalated access. |
| **Success Criteria** | Secret cracked. Admin token forged and accepted. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Full JWT Security Audit

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Web application using JWT. Run complete jwt_tool playbook. Test all attacks. Document which attacks work, which don't, and why. Write remediation recommendations for each finding. |
| **Success Criteria** | All attacks tested. Findings documented with impact and remediation. |

---

### Challenge 8.2 — Custom JWT Attack Script

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Write a Python script (without jwt_tool) that: decodes a JWT, modifies a claim, signs with a known secret or tests alg:none, and sends the forged token to an API. |
| **Success Criteria** | Script functional. Correctly forges tokens and detects successful exploitation. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can decode and analyze a JWT manually | ☐ |
| Can execute the alg:none attack | ☐ |
| Can execute RS256 → HS256 algorithm confusion | ☐ |
| Can crack HS256 secrets with jwt_tool and Hashcat | ☐ |
| Can forge admin tokens with a cracked secret | ☐ |
| Can test jku/x5u/kid injection attacks | ☐ |
| Can use jwt_tool's playbook scan | ☐ |
| Can integrate jwt_tool with Burp Suite | ☐ |

---

## 🎯 Interview Questions

1. What is the structure of a JWT token?
2. How does the alg:none attack work?
3. What is the RS256 → HS256 algorithm confusion attack?
4. How do you crack a weak JWT secret?
5. What is a jku injection attack?
6. What claims do you typically target for privilege escalation?
7. How do you forge an admin JWT after cracking the secret?
8. What is the Burp Suite JWT Editor extension and what does it add?
