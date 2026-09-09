# 🔐 OpenSSL & cryptsetup: Complete Mastery Checklist

> **What is OpenSSL?** OpenSSL is the world's most widely deployed cryptography library and command-line toolkit. It implements TLS/SSL protocols, RSA/ECC/DSA key operations, symmetric ciphers (AES, ChaCha20), hashing (SHA-256, SHA-3), certificate signing, and PKCS standards. It underpins virtually every HTTPS connection, VPN, and PKI deployment on the planet.
>
> **What is cryptsetup?** cryptsetup is the Linux utility for managing LUKS (Linux Unified Key Setup) full-disk and partition encryption. It uses dm-crypt in the kernel to provide transparent AES-XTS block-device encryption. LUKS is the standard for Linux disk encryption.
>
> **Why do they exist?** OpenSSL exists because secure communication requires a trustworthy, audited implementation of cryptographic primitives — not roll-your-own code. cryptsetup exists because OS-level disk encryption requires a standardized, interoperable header format that survives key rotation, multiple passphrases, and forensic attack.
>
> **When to use OpenSSL:** Inspecting TLS certificates and cipher suites on target servers, generating test key pairs and self-signed certs, debugging TLS handshakes, encrypting/decrypting files, hashing and HMAC verification, and understanding every aspect of PKI.
>
> **When to use cryptsetup:** Securing lab VMs and portable drives, understanding full-disk encryption for forensics investigations, and demonstrating data-at-rest controls for compliance contexts.
>
> **What mastering them unlocks:** Deep understanding of TLS internals (essential for attacking misconfigurations), the ability to inspect any certificate chain independently, PKI concepts required for Phase 6 ADCS attacks, and disk forensics awareness for Phase 7.
>
> **Roadmap Stage / Module:** Stage 1: Module 05 (Cryptography)

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| Networking | Crypto & Certs | Packet Analysis | Exploitation |
|:-----------|:---------------|:----------------|:-------------|
| [🗺️ Nmap](Nmap.md) | **🔐 OpenSSL** (you are here) | [🦈 Wireshark](Wireshark.md) | [💀 Metasploit](Metasploit_Framework.md) |
| [🔌 Netcat](Netcat.md) | [📦 socat](socat.md) | [🦭 tcpdump](tcpdump.md) | [🔓 Hashcat](Hashcat.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & Environment | 3 | 1 hour |
| 2 | Symmetric Encryption & Hashing | 6 | 2–3 hours |
| 3 | Asymmetric Keys & PKI | 7 | 3–4 hours |
| 4 | TLS Inspection & Testing | 8 | 3–5 hours |
| 5 | Certificate Authorities & PKCS | 6 | 3–4 hours |
| 6 | cryptsetup & LUKS | 5 | 2–3 hours |
| 7 | Practical Labs | 4 | 4–6 hours |
| | **Total** | **39** | **~18–26 hours** |

**Prerequisites:** Phase 1 Part 1 (Linux CLI basics). Understanding of what encryption, hashing, and digital signatures are conceptually.

---

# PHASE 1: INSTALLATION & ENVIRONMENT

---

## 1.1 Installation & Version Check

```bash
# Check OpenSSL version (most Linux distros ship with it)
openssl version -a

# Install on Debian/Ubuntu if missing
sudo apt install openssl

# Install cryptsetup
sudo apt install cryptsetup

# Verify cryptsetup
cryptsetup --version
```

- [ ] **Understand which version you have:** OpenSSL 1.1.x vs 3.x have different default cipher behavior. Know the difference — OpenSSL 3.x deprecates several legacy ciphers and engines.
- [ ] **Know the manpage structure:** `man openssl` shows all subcommands. `openssl <command> --help` shows options for each command. Always check this before Googling.

## 1.2 OpenSSL Subcommand Map

- [ ] Know these core subcommands exist and what they do at a high level:
  - `openssl s_client` — TLS client/inspector
  - `openssl s_server` — TLS server
  - `openssl req` — Certificate Signing Request (CSR) generation
  - `openssl x509` — Certificate inspection and signing
  - `openssl genrsa` / `openssl genpkey` — Key generation
  - `openssl enc` — Symmetric encryption/decryption
  - `openssl dgst` — Hashing and digital signatures
  - `openssl pkcs12` — PKCS#12 bundle operations
  - `openssl verify` — Certificate chain verification
  - `openssl ca` — Mini Certificate Authority

---

# PHASE 2: SYMMETRIC ENCRYPTION & HASHING

---

## 2.1 Symmetric Encryption with `openssl enc`

```bash
# Encrypt a file with AES-256-CBC (password-based)
openssl enc -aes-256-cbc -salt -pbkdf2 -in secret.txt -out secret.enc

# Decrypt
openssl enc -d -aes-256-cbc -pbkdf2 -in secret.enc -out secret_decrypted.txt

# List all available ciphers
openssl enc -list

# Encrypt with ChaCha20-Poly1305 (modern, authenticated)
openssl enc -chacha20 -pbkdf2 -in secret.txt -out secret.enc
```

- [ ] **Understand `-pbkdf2`:** Without this flag, OpenSSL uses the deprecated EVP_BytesToKey KDF. Always use `-pbkdf2` for modern key derivation. Know why old encrypted files without this flag are weaker.
- [ ] **Understand `-salt`:** Prevents identical plaintexts encrypting to identical ciphertexts. Know what rainbow table attacks look like against unsalted encryption.
- [ ] **AES-CBC vs AES-GCM:** CBC provides confidentiality but not integrity — a padding oracle attack can decrypt CBC without the key. AES-GCM (authenticated encryption) provides both. Know when each is appropriate.

## 2.2 Hashing & HMAC

```bash
# SHA-256 hash of a file
openssl dgst -sha256 file.txt

# SHA-512
openssl dgst -sha512 file.txt

# MD5 (insecure — only for legacy/compatibility understanding)
openssl dgst -md5 file.txt

# HMAC-SHA256 (keyed hash — message authentication)
openssl dgst -sha256 -hmac "supersecretkey" file.txt

# List all digest algorithms
openssl list -digest-algorithms
```

- [ ] **Hash collision resistance:** MD5 and SHA-1 are collision-broken. Know practical attack demos (MD5 collision certificates). Use SHA-256 minimum in any modern context.
- [ ] **HMAC vs Hash:** A plain hash can be forged if you control input (length extension attack on SHA-256). HMAC with a secret key prevents this. Know why HMAC is used for API authentication.
- [ ] **File integrity verification:** Practice hashing a downloaded binary and comparing against the publisher's SHA-256 checksum. This is your first line of supply-chain security.

---

# PHASE 3: ASYMMETRIC KEYS & PKI

---

## 3.1 RSA Key Generation & Inspection

```bash
# Generate a 4096-bit RSA private key
openssl genrsa -out private.key 4096

# Generate with AES-256 passphrase protection
openssl genrsa -aes256 -out private.key 4096

# Extract the public key from a private key
openssl rsa -in private.key -pubout -out public.key

# Inspect a private key (shows modulus, exponents, primes)
openssl rsa -in private.key -text -noout

# Check key size and type
openssl rsa -in private.key -check
```

- [ ] **RSA key sizes:** 1024-bit is broken. 2048-bit is the practical minimum. 4096-bit is preferred for long-lived certificates. Know why key length matters.
- [ ] **Why passphrase protection matters:** An unprotected private key file on disk is immediately usable by anyone with file system access. Know the tradeoff (automation vs security) and how to use SSH agents / hardware tokens.

## 3.2 ECC (Elliptic Curve Cryptography) Keys

```bash
# List available curves
openssl ecparam -list_curves | grep -E "prime256v1|secp384r1|secp521r1"

# Generate an ECDSA key (P-256 — used by most modern TLS)
openssl ecparam -name prime256v1 -genkey -noout -out ec_private.key

# Extract the EC public key
openssl ec -in ec_private.key -pubout -out ec_public.key

# Inspect the EC key
openssl ec -in ec_private.key -text -noout
```

- [ ] **ECC vs RSA:** A 256-bit ECC key provides equivalent security to a 3072-bit RSA key. Modern TLS and JWT implementations prefer ECC. Know `prime256v1` (P-256), `secp384r1` (P-384), and why `secp256k1` (Bitcoin's curve) is different.

## 3.3 Encrypt/Decrypt with RSA Keys

```bash
# Encrypt a small file with a public key (RSA-OAEP)
# Note: openssl rsautl is deprecated in OpenSSL 3.x — use pkeyutl instead
openssl pkeyutl -encrypt -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha256 \
  -pubin -inkey public.key -in secret.txt -out secret.enc

# Decrypt with private key
openssl pkeyutl -decrypt -pkeyopt rsa_padding_mode:oaep -pkeyopt rsa_oaep_md:sha256 \
  -inkey private.key -in secret.enc -out secret_dec.txt

# Sign a file (creates digital signature)
openssl dgst -sha256 -sign private.key -out signature.bin file.txt

# Verify the signature
openssl dgst -sha256 -verify public.key -signature signature.bin file.txt
```

- [ ] **RSA is not for bulk encryption:** RSA can only encrypt data smaller than the key size minus padding. In practice, RSA encrypts a symmetric key (AES), and AES encrypts the data. This is the hybrid encryption model used in TLS.
- [ ] **Digital signature vs encryption:** Encryption uses recipient's public key (only they can decrypt). Signing uses sender's private key (anyone with public key can verify). Know which direction each operation goes.

---

# PHASE 4: TLS INSPECTION & TESTING

---

## 4.1 `openssl s_client` — TLS Inspector

```bash
# Connect to a server and view the TLS handshake + certificate
openssl s_client -connect google.com:443

# Show only the certificate chain (suppress handshake noise)
openssl s_client -connect google.com:443 -showcerts 2>/dev/null | openssl x509 -text -noout

# Test a specific TLS version
openssl s_client -connect target.com:443 -tls1_2
openssl s_client -connect target.com:443 -tls1_3

# Test with SNI (Server Name Indication — required for virtual hosting)
openssl s_client -connect target.com:443 -servername target.com

# Check what cipher was negotiated
openssl s_client -connect target.com:443 2>/dev/null | grep "Cipher is"

# Test SMTP STARTTLS
openssl s_client -connect mail.target.com:25 -starttls smtp

# Test a specific cipher suite
openssl s_client -connect target.com:443 -cipher 'RC4-MD5' 2>/dev/null | grep "Cipher is"
```

- [ ] **What to look for in handshake output:**
  - `Certificate chain` — inspect each cert: CN, SAN, issuer, validity dates
  - `Cipher is` — the negotiated cipher suite. Weak = `RC4`, `3DES`, `NULL`, `EXPORT`
  - `Protocol` — TLS 1.0/1.1 are deprecated. TLS 1.3 is current best practice
  - `Verify return code: 0 (ok)` — chain validates. Any other code = problem
- [ ] **Testing for BEAST/POODLE/SWEET32:** Connect with `-tls1` or `-tls1_1` and `-cipher 'DES-CBC3-SHA'`. If it connects, the server supports deprecated protocols.
- [ ] **Testing for Heartbleed (CVE-2014-0160):** Use `nmap --script ssl-heartbleed` or Metasploit module — but understand what `s_client` tells you about the TLS library version.

## 4.2 Certificate Inspection

```bash
# Inspect a .pem certificate file
openssl x509 -in cert.pem -text -noout

# Check certificate validity dates
openssl x509 -in cert.pem -dates -noout

# Extract certificate from a live server and inspect it
echo | openssl s_client -connect target.com:443 2>/dev/null | openssl x509 -text -noout

# Check the fingerprint (for certificate pinning verification)
openssl x509 -in cert.pem -fingerprint -sha256 -noout

# Check the Subject Alternative Names (SANs)
openssl x509 -in cert.pem -text -noout | grep -A 3 "Subject Alternative"

# Verify a certificate against a CA bundle
openssl verify -CAfile /etc/ssl/certs/ca-certificates.crt cert.pem
```

- [ ] **Certificate fields to understand:**
  - `Subject` / `CN` — who the cert is for
  - `Issuer` — who signed it (the CA)
  - `SAN (Subject Alternative Names)` — all the domains this cert is valid for (CN alone is deprecated)
  - `Not Before / Not After` — validity window
  - `Key Usage` / `Extended Key Usage` — what the cert is authorized to do (server auth, client auth, signing)
  - `Basic Constraints: CA:TRUE` — this cert can sign other certs (a CA cert)
- [ ] **Certificate pinning:** Know what it is, how apps implement it, and why Phase 5 (Mobile) requires bypassing it using Frida.

## 4.3 TLS Server with `openssl s_server`

```bash
# Generate a self-signed cert for testing (all-in-one)
openssl req -x509 -newkey rsa:2048 -keyout server.key -out server.crt \
  -days 365 -nodes -subj "/CN=test.local"

# Start a TLS server on port 4433
openssl s_server -key server.key -cert server.crt -accept 4433

# Connect to your test server from another terminal
openssl s_client -connect localhost:4433

# Run a command on incoming connections (like a TLS netcat listener)
openssl s_server -key server.key -cert server.crt -accept 4433 -quiet
```

- [ ] **Why this matters for pentesting:** Setting up a rogue TLS server to capture data from misconfigured clients. Understanding what a valid vs self-signed cert looks like from the attacker side.

---

# PHASE 5: CERTIFICATE AUTHORITIES & PKCS

---

## 5.1 Certificate Signing Requests (CSR)

```bash
# Generate a key and CSR in one command
openssl req -newkey rsa:2048 -nodes -keyout domain.key -out domain.csr \
  -subj "/C=US/ST=CA/L=SF/O=TestOrg/CN=www.example.com"

# Inspect a CSR before submitting it
openssl req -text -noout -in domain.csr

# Generate CSR from existing key
openssl req -new -key domain.key -out domain.csr
```

## 5.2 Self-Signed Certificates & Mini-CA

```bash
# Generate root CA key and self-signed certificate
openssl genrsa -out ca.key 4096
openssl req -new -x509 -days 3650 -key ca.key -out ca.crt \
  -subj "/CN=MyTestCA/O=TestOrg"

# Sign a CSR with your CA (create a signed server certificate)
openssl x509 -req -days 365 -in domain.csr -CA ca.crt -CAkey ca.key \
  -CAcreateserial -out domain.crt

# Verify the signed cert chains back to your CA
openssl verify -CAfile ca.crt domain.crt
```

- [ ] **Why this matters:** Understanding CA operations is required for Phase 6 ADCS exploitation (Certipy). Know the difference between a root CA, intermediate CA, and leaf certificate. Know what `Basic Constraints: CA:TRUE` means and why it's dangerous if misconfigured.

## 5.3 PKCS#12 Bundles

```bash
# Create a PKCS#12 (.pfx/.p12) bundle (cert + key, for Windows/browsers)
openssl pkcs12 -export -out bundle.pfx -inkey domain.key -in domain.crt -certfile ca.crt

# Extract cert and key from a PKCS#12 bundle
openssl pkcs12 -in bundle.pfx -clcerts -nokeys -out cert.pem
openssl pkcs12 -in bundle.pfx -nocerts -nodes -out key.pem

# Inspect a PKCS#12 file
openssl pkcs12 -in bundle.pfx -info -noout
```

- [ ] **PKCS#12 in Phase 6:** Certipy outputs `.pfx` files. Know how to inspect and use them — including extracting the private key and importing into Rubeus or authenticating with `openssl s_client -cert cert.pem -key key.pem`.

---

# PHASE 6: CRYPTSETUP & LUKS

---

## 6.1 Creating an Encrypted Volume

```bash
# Create a 1GB container file
dd if=/dev/zero of=encrypted.img bs=1M count=1024

# Initialize LUKS on the container (sets passphrase, header)
sudo cryptsetup luksFormat encrypted.img

# Open (decrypt and map) the encrypted volume
sudo cryptsetup luksOpen encrypted.img myvolume

# Format the mapped device with a filesystem
sudo mkfs.ext4 /dev/mapper/myvolume

# Mount it
sudo mount /dev/mapper/myvolume /mnt/secret

# Use it, then unmount and close
sudo umount /mnt/secret
sudo cryptsetup luksClose myvolume
```

## 6.2 Managing LUKS Headers & Keys

```bash
# Inspect the LUKS header (shows key slots, cipher, hash)
sudo cryptsetup luksDump encrypted.img

# Add a second passphrase (LUKS supports up to 8 key slots)
sudo cryptsetup luksAddKey encrypted.img

# Remove a key slot
sudo cryptsetup luksKillSlot encrypted.img 1

# Backup the LUKS header (CRITICAL — losing the header = losing all data)
sudo cryptsetup luksHeaderBackup encrypted.img --header-backup-file header.bak

# Restore a header
sudo cryptsetup luksHeaderRestore encrypted.img --header-backup-file header.bak
```

- [ ] **LUKS vs dm-crypt:** LUKS adds a standardized header on top of raw dm-crypt. The header stores the master key (encrypted by your passphrase). If the header is destroyed, the data is unrecoverable even with the passphrase. Know why header backup is non-optional.
- [ ] **Forensic relevance:** In Phase 7, you'll encounter LUKS-encrypted evidence drives. Know what `cryptsetup luksDump` tells you and what it doesn't (it can't crack the passphrase).

## 6.3 Full Disk Encryption Concepts

- [ ] **LUKS1 vs LUKS2:** LUKS2 supports Argon2 KDF (memory-hard, GPU-resistant) vs LUKS1's PBKDF2. Know which to use for new volumes and why.
- [ ] **Key derivation:** The passphrase is never the encryption key directly. It is run through PBKDF2/Argon2 to derive the slot key, which decrypts the master key. This is why a strong passphrase matters even with GPU cracking.
- [ ] **AES-XTS:** LUKS default cipher mode. XTS (XEX-based Tweaked-codebook mode with ciphertext Stealing) is designed for disk encryption where the same block can be encrypted multiple times with different results based on block position (the "tweak").

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — TLS Recon:** Choose 5 different HTTPS sites (a bank, a news site, a government site, an IoT vendor, an old enterprise app). Use `openssl s_client` to inspect each. Document: TLS version, cipher suite, certificate chain depth, SANs, expiry. Identify any using TLS 1.0/1.1 or weak ciphers.

- [ ] **Lab 2 — Mini PKI:** Build a complete 3-tier PKI from scratch: Root CA → Intermediate CA → Leaf Server Certificate. Sign and verify the chain. Import into Firefox and confirm the browser trusts your site. Understand why the intermediate CA exists.

- [ ] **Lab 3 — Encrypted Comms:** Set up an `openssl s_server` listener with a self-signed cert, then connect with `openssl s_client`, and pipe data through it. Compare this to an unencrypted `netcat` session captured in Wireshark — confirm the s_client/s_server traffic is opaque.

- [ ] **Lab 4 — LUKS Encrypted Drive:** Create an encrypted container with LUKS2/Argon2. Add two key slots (two passphrases). Delete one key slot. Backup and restore the header. Mount and unmount. Simulate a forensic scenario: given only the container file and the passphrase, can you recover the data?

---

## 📝 Operational Notes

- **`-nodes` flag:** Means "no DES" — outputs the private key unencrypted (no passphrase). Use only for automation/testing, never for production keys.
- **OpenSSL 3.x engine deprecation:** The `-engine` flag is deprecated in OpenSSL 3.x. Use providers instead (`-provider legacy` for old ciphers like RC2/RC4).
- **`2>/dev/null`:** `openssl s_client` is verbose by default. Redirect stderr to suppress connection noise when piping to `openssl x509`.
- **Password in commands:** Avoid `-pass pass:mypassword` in production — it exposes the password in process listings (`ps aux`). Use `-pass file:passfile` or environment variables instead.
- **Certificate transparency (CT):** All publicly trusted CAs must log new certificates to CT logs. Use `crt.sh` to enumerate all issued certs for a domain — useful for recon in Phase 2.
- **LUKS forensics:** `cryptsetup luksDump` will tell you the cipher, hash, and whether any key slots are occupied, but cannot reveal the passphrase or master key without the correct passphrase.
