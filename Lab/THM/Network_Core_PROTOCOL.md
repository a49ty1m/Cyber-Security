# Networking Core Protocols — TryHackMe Notes

> **Room:** [Networking Core Protocols](https://tryhackme.com/room/networkingcoreprotocols)  
> **Series position:** 3rd (after *Networking Concepts* → *Networking Essentials*)  
> **Next room:** [Networking Secure Protocols](https://tryhackme.com/room/networkingsecureprotocols)

---

## Table of Contents

1. [Room Overview](#1-room-overview)
2. [What Is a Network Protocol?](#2-what-is-a-network-protocol)
3. [DNS — Domain Name System](#3-dns--domain-name-system)
4. [WHOIS](#4-whois)
5. [HTTP — Hypertext Transfer Protocol](#5-http--hypertext-transfer-protocol)
6. [HTTP Requests](#6-http-requests)
7. [HTTP Responses](#7-http-responses)
8. [HTTP From the Command Line](#8-http-from-the-command-line)
9. [FTP — File Transfer Protocol](#9-ftp--file-transfer-protocol)
10. [SMTP — Simple Mail Transfer Protocol](#10-smtp--simple-mail-transfer-protocol)
11. [POP3 — Post Office Protocol 3](#11-pop3--post-office-protocol-3)
12. [IMAP — Internet Message Access Protocol](#12-imap--internet-message-access-protocol)
13. [POP3 vs IMAP](#13-pop3-vs-imap)
14. [Telnet — Manual Protocol Testing](#14-telnet--manual-protocol-testing)
15. [Port Reference Cheat Sheet](#15-port-reference-cheat-sheet)
16. [Protocol Relationships](#16-protocol-relationships)
17. [Cybersecurity Perspective](#17-cybersecurity-perspective)
18. [Command Reference](#18-command-reference)
19. [Learning Progression](#19-learning-progression)
20. [Room Q&A Reference](#20-room-qa-reference)
21. [Quick Revision Sheet](#21-quick-revision-sheet)

---

## 1. Room Overview

### Prerequisites

The room expects prior knowledge of:

- OSI model
- TCP/IP model
- Ethernet / IP / TCP fundamentals

### Learning Objectives

By the end of this room you should understand:

- How DNS resolves names to IP addresses
- How WHOIS exposes domain registration data
- How HTTP/HTTPS drives web communication
- How FTP transfers files
- How SMTP sends email
- How POP3 and IMAP retrieve email
- How to interact with all these protocols manually from the command line

---

## 2. What Is a Network Protocol?

A **network protocol** is a defined set of rules that governs how two systems communicate. Think of it as the shared language between a client and a server — both must speak the same protocol or communication breaks.

```text
Client                          Server
  |                               |
  |-------- Request ------------> |
  |                               |
  | <------- Response ----------- |
```

Every protocol in this room operates at the **Application layer** of the TCP/IP model, riding on top of TCP (or UDP for DNS).

### Protocol Purpose Summary

| Protocol | Layer       | Transport | Primary Purpose                 |
| -------- | ----------- | --------- | ------------------------------- |
| DNS      | Application | UDP/TCP   | Name → IP resolution            |
| WHOIS    | Application | TCP       | Domain registration lookup      |
| HTTP     | Application | TCP       | Web communication               |
| FTP      | Application | TCP       | File transfer                   |
| SMTP     | Application | TCP       | Sending email                   |
| POP3     | Application | TCP       | Downloading email               |
| IMAP     | Application | TCP       | Synchronizing/accessing email   |

---

## 3. DNS — Domain Name System

### What Is DNS?

DNS translates human-readable domain names into IP addresses. Without it, every user would need to memorize raw IP addresses.

```text
example.com  →  DNS  →  93.184.216.34
```

### DNS Resolution Flow

```text
User types URL in browser
        ↓
   DNS Resolver (ISP or custom, e.g. 8.8.8.8)
        ↓
   Root Name Server  →  TLD Server (.com)  →  Authoritative NS
        ↓
   IP Address returned
        ↓
   Browser connects to Web Server
```

### DNS Record Types

| Record | Purpose                                              |
| ------ | ---------------------------------------------------- |
| A      | Maps domain to IPv4 address                          |
| AAAA   | Maps domain to IPv6 address                          |
| MX     | Identifies the mail server for a domain              |
| CNAME  | Alias — points one domain to another                 |
| NS     | Specifies the authoritative name server for a domain |
| TXT    | Arbitrary text: SPF, DKIM, domain verification, etc. |
| PTR    | Reverse lookup — IP address → hostname               |
| SOA    | Start of Authority — zone metadata                   |

> **Memory trick:** A → IPv4 · AAAA → IPv6 · MX → mail · CNAME → alias · NS → nameserver · PTR → reverse

### DNS Commands

```bash
# Basic resolution
nslookup example.com
dig example.com

# Query specific record types
dig example.com A
dig example.com AAAA
dig example.com MX
dig example.com NS
dig example.com TXT

# Reverse lookup
dig -x 93.184.216.34

# Use a specific resolver
dig @8.8.8.8 example.com

# Zone transfer attempt (AXFR)
dig axfr @ns1.example.com example.com
```

### Security Relevance

DNS is a **primary recon target**. From a single domain you can map:

```text
Domain
  ↓  A/AAAA records
IP addresses & hosting infrastructure
  ↓  MX records
Mail server provider
  ↓  NS records
DNS hosting provider & potential zone transfer targets
  ↓  TXT records
Email security config (SPF, DKIM, DMARC), third-party integrations
  ↓  CNAME records
Subdomains and CDN/cloud services in use
```

Key tools for DNS recon: `dig`, `nslookup`, `dnsx`, `subfinder`, `amass`, `dnsrecon`

---

## 4. WHOIS

### What Is WHOIS?

WHOIS retrieves registration data about Internet resources (domains, IP blocks, ASNs). Depending on the registrar and privacy settings, a lookup may return:

- Registrar name
- Registration and expiration dates
- Nameservers
- Domain status codes
- Registrant / admin / technical contact details (often redacted)

> **Note:** GDPR and registrar privacy services (e.g. WhoisGuard) frequently mask personal details. You will often see proxy contact info rather than the real registrant.

### Command

```bash
whois example.com
whois 93.184.216.34    # IP WHOIS — returns ASN, org, CIDR block
```

### Security Relevance

WHOIS is a **passive reconnaissance** technique — no packets sent to the target.

Useful for:
- Identifying the registrar and hosting org
- Determining domain age (older domains are often more trusted for email)
- Correlating multiple domains owned by the same entity
- Finding historical registration info via tools like whoxy.com or domaintools.com

---

## 5. HTTP — Hypertext Transfer Protocol

### What Is HTTP?

HTTP is the application-layer protocol that drives communication between web clients (browsers, `curl`, scripts) and web servers.

```text
Client (Browser)
      |
      |  HTTP Request  (TCP/80)
      ↓
  Web Server
      |
      |  HTTP Response
      ↓
Client (Browser)
```

| Variant | Port    | Notes                                            |
| ------- | ------- | ------------------------------------------------ |
| HTTP    | TCP/80  | Plaintext — all traffic visible on the wire      |
| HTTPS   | TCP/443 | HTTP tunneled inside TLS — encrypted in transit  |

> **HTTPS does not mean "secure website."** HTTPS only means the *transport* is encrypted. The application itself can still be vulnerable.

---

## 6. HTTP Requests

### Basic Structure

```http
GET /index.html HTTP/1.1
Host: example.com
User-Agent: curl/7.88.0
Accept: */*

```

> The **blank line** after headers is mandatory — it signals the end of the header section.

### HTTP Methods

| Method  | Purpose                                    | Idempotent? |
| ------- | ------------------------------------------ | ----------- |
| GET     | Retrieve a resource                        | Yes         |
| POST    | Submit data to create/process a resource   | No          |
| PUT     | Replace a resource entirely                | Yes         |
| PATCH   | Partially update a resource                | No          |
| DELETE  | Remove a resource                          | Yes         |
| HEAD    | Same as GET but response body is omitted   | Yes         |
| OPTIONS | Query which methods the server supports    | Yes         |

---

## 7. HTTP Responses

### Basic Structure

```http
HTTP/1.1 200 OK
Content-Type: text/html; charset=UTF-8
Content-Length: 1234
Server: nginx

<html>...
```

### Status Code Categories

| Range | Category      | Meaning                                           |
| ----- | ------------- | ------------------------------------------------- |
| 1xx   | Informational | Request received, processing continues            |
| 2xx   | Success       | Request completed successfully                    |
| 3xx   | Redirection   | Further action required                           |
| 4xx   | Client Error  | Problem with the request                          |
| 5xx   | Server Error  | Server failed to fulfill a valid request          |

### Common Status Codes

| Code | Text                  | Meaning                                      |
| ---- | --------------------- | -------------------------------------------- |
| 200  | OK                    | Request successful                           |
| 201  | Created               | Resource created (after POST/PUT)            |
| 204  | No Content            | Success, no body returned                    |
| 301  | Moved Permanently     | Permanent redirect — update your bookmark    |
| 302  | Found                 | Temporary redirect                           |
| 400  | Bad Request           | Malformed request syntax                     |
| 401  | Unauthorized          | Authentication required                      |
| 403  | Forbidden             | Authenticated but not authorized             |
| 404  | Not Found             | Resource does not exist                      |
| 405  | Method Not Allowed    | HTTP method not supported on this endpoint   |
| 500  | Internal Server Error | Generic server-side failure                  |
| 503  | Service Unavailable   | Server overloaded or down for maintenance    |

> **Security note:** `403` vs `401` matters. `401` = not logged in. `403` = logged in but blocked. Both can indicate interesting resources worth investigating.

---

## 8. HTTP From the Command Line

### curl

```bash
# GET request
curl http://TARGET_IP

# Headers only (HEAD request)
curl -I http://TARGET_IP

# Verbose — shows full request + response headers
curl -v http://TARGET_IP

# Follow redirects
curl -L http://TARGET_IP

# POST with data
curl -X POST -d "username=admin&password=secret" http://TARGET_IP/login

# Custom header
curl -H "X-Custom-Header: value" http://TARGET_IP
```

### Telnet / netcat (Manual TCP)

Both `telnet` and `nc` let you send raw bytes over TCP — useful for hand-crafting HTTP requests:

```bash
# Using telnet
telnet TARGET_IP 80

# Using netcat (nc) — preferred
nc TARGET_IP 80
```

Then type the request manually:

```http
GET / HTTP/1.1
Host: TARGET_IP

```

> The blank line after `Host:` is required — it terminates the headers. Without it the server keeps waiting.

---

## 9. FTP — File Transfer Protocol

### What Is FTP?

FTP transfers files between a client and a server. It uses a **two-channel model**:

| Channel    | Port | Purpose                               |
| ---------- | ---- | ------------------------------------- |
| Control    | 21   | Commands and server responses         |
| Data       | 20*  | Actual file data transfer             |

> *Port 20 is used in **Active mode**. In **Passive mode** the server opens a random high port for data — this is more firewall-friendly and is the default in most modern clients.

### Connecting

```bash
ftp TARGET_IP
```

If anonymous access is enabled:

```text
Name: anonymous
Password: anonymous   (or any email address)
```

### Common FTP Commands

| Command        | Purpose                        |
| -------------- | ------------------------------ |
| `ls`           | List files in current dir      |
| `pwd`          | Print working directory        |
| `cd <dir>`     | Change directory               |
| `get <file>`   | Download a file                |
| `put <file>`   | Upload a file                  |
| `mget *.txt`   | Download multiple files        |
| `binary`       | Switch to binary transfer mode |
| `passive`      | Toggle passive mode            |
| `bye` / `quit` | Close the FTP session          |

### Example Session

```text
ftp> ls
ftp> get flag.txt
ftp> bye
```

### FTP vs SFTP vs FTPS

Traditional FTP is **completely unencrypted** — credentials and file contents are sent in plaintext.

| Protocol | Description                                  | Encrypted? |
| -------- | -------------------------------------------- | ---------- |
| FTP      | Standard File Transfer Protocol              | No         |
| FTPS     | FTP + TLS (explicit or implicit)             | Yes        |
| SFTP     | SSH File Transfer Protocol (different beast) | Yes        |

> SFTP is **not** FTP tunneled over SSH — it is a completely separate subsystem of the SSH protocol. Do not conflate them.

---

## 10. SMTP — Simple Mail Transfer Protocol

### What Is SMTP?

SMTP handles **sending** email — from a mail client to a mail server, and between mail servers.

```text
Sender's Mail Client
        |
        | SMTP (port 587 / 465)
        ↓
  Sender's Mail Server (MTA)
        |
        | SMTP (port 25 — server to server)
        ↓
  Recipient's Mail Server
```

### SMTP Ports

| Port | Usage                                              |
| ---- | -------------------------------------------------- |
| 25   | Server-to-server relay (MTA to MTA)                |
| 587  | Client submission with STARTTLS (modern standard)  |
| 465  | Client submission over implicit TLS (SMTPS)        |

> **STARTTLS** = start a plaintext connection on port 587, then *upgrade* it to TLS mid-session.  
> **Port 465 (SMTPS)** = TLS from the first byte — no unencrypted phase.

### SMTP Commands

| Command        | Purpose                                    |
| -------------- | ------------------------------------------ |
| `HELO`         | Identify the sending host (basic)          |
| `EHLO`         | Extended HELO — used with ESMTP            |
| `MAIL FROM:`   | Declare the sender's address               |
| `RCPT TO:`     | Declare the recipient's address            |
| `DATA`         | Begin the email body                       |
| `.`            | Terminate the email body (on its own line) |
| `QUIT`         | End the session                            |
| `VRFY`         | Verify if a user exists (often disabled)   |
| `EXPN`         | Expand a mailing list (often disabled)     |

### Example Manual SMTP Session

```text
telnet TARGET_IP 25

Client: EHLO attacker.com
Server: 250-TARGET_IP Hello attacker.com

Client: MAIL FROM:<alice@example.com>
Server: 250 Ok

Client: RCPT TO:<bob@example.com>
Server: 250 Ok

Client: DATA
Server: 354 End data with <CR><LF>.<CR><LF>

Client: Subject: Test
Client:
Client: Hello Bob.
Client: .
Server: 250 Ok: queued

Client: QUIT
Server: 221 Bye
```

### Security Relevance

- **Email spoofing:** SMTP has no built-in authentication of the `MAIL FROM:` field
- **SPF:** DNS TXT record listing servers authorized to send for a domain
- **DKIM:** Cryptographic signature in email headers proving authenticity
- **DMARC:** Policy instructing receivers what to do with SPF/DKIM failures
- **User enumeration:** `VRFY` / `RCPT TO` responses can leak valid usernames
- **Open relay:** Misconfigured SMTP server that forwards email for anyone

---

## 11. POP3 — Post Office Protocol 3

### What Is POP3?

POP3 is for **retrieving** email from a mail server to a local client.

```text
Mail Server (stores email)
      |
      | POP3
      ↓
Email Client (downloads and often deletes from server)
```

| Variant | Port | Notes             |
| ------- | ---- | ----------------- |
| POP3    | 110  | Plaintext         |
| POP3S   | 995  | POP3 over TLS     |

> By default POP3 **deletes messages from the server after download**. This makes multi-device access painful.

### POP3 Commands

| Command        | Purpose                                   |
| -------------- | ----------------------------------------- |
| `USER <name>`  | Send username                             |
| `PASS <pass>`  | Send password                             |
| `STAT`         | Number of messages and total size         |
| `LIST`         | List all messages with sizes              |
| `RETR <n>`     | Retrieve message number n                 |
| `DELE <n>`     | Mark message n for deletion               |
| `RSET`         | Reset (unmark any deletions)              |
| `QUIT`         | Apply deletions and close session         |

### Manual POP3 Session

```bash
nc TARGET_IP 110
```

```text
Server: +OK Dovecot ready

Client: USER alice
Server: +OK

Client: PASS password123
Server: +OK Logged in

Client: LIST
Server: +OK 4 messages
1 1024
2 512
3 768
4 2048

Client: RETR 4
Server: +OK 2048 octets
...email content...

Client: QUIT
Server: +OK Logging out
```

---

## 12. IMAP — Internet Message Access Protocol

### What Is IMAP?

IMAP allows a client to **access and synchronize** a mailbox stored on the server. Unlike POP3, mail stays on the server and state (read/unread, folders) is synced across devices.

```text
Mail Server
    (bidirectional sync)
Email Client(s)
```

| Variant | Port | Notes             |
| ------- | ---- | ----------------- |
| IMAP    | 143  | Plaintext         |
| IMAPS   | 993  | IMAP over TLS     |

### IMAP Commands

IMAP commands are prefixed with a **tag** (e.g. `A1`, `A2`) so that pipelined responses can be matched to their requests.

| Command                     | Purpose                                  |
| --------------------------- | ---------------------------------------- |
| `A LOGIN user pass`         | Authenticate                             |
| `A LIST "" "*"`             | List all mailboxes                       |
| `A SELECT INBOX`            | Open INBOX (shows message count)         |
| `A FETCH <n> BODY[]`        | Retrieve full message n                  |
| `A FETCH <n> FLAGS`         | Retrieve flags (read/unread etc.)        |
| `A STORE <n> +FLAGS \Seen`  | Mark message as read                     |
| `A LOGOUT`                  | End session                              |

### Manual IMAP Session

```bash
nc TARGET_IP 143
```

```text
Server: * OK IMAP4rev1 Dovecot ready

Client: A LOGIN alice password123
Server: A OK Logged in

Client: A SELECT INBOX
Server: * 4 EXISTS
Server: A OK [READ-WRITE] Select completed

Client: A FETCH 4 BODY[]
Server: * 4 FETCH (BODY[] {2048}
...email content...
Server: A OK Fetch completed

Client: A LOGOUT
Server: * BYE Logging out
```

---

## 13. POP3 vs IMAP

| Feature                  | POP3                                         | IMAP                                 |
| ------------------------ | -------------------------------------------- | ------------------------------------ |
| Primary action           | Download mail                                | Access/sync mail on server           |
| Mail storage             | Moves to client (deleted from server default) | Stays on server                     |
| Multi-device support     | Poor — mail on one device only               | Excellent — synced everywhere        |
| Folder/label support     | None                                         | Full server-side folder structure    |
| Offline access           | Yes (downloaded locally)                     | Yes (with client-side caching)       |
| Read-state sync          | No                                           | Yes                                  |
| Common port (plaintext)  | 110                                          | 143                                  |
| Secure port              | 995 (POP3S)                                  | 993 (IMAPS)                          |
| Best used when           | Single device, limited server space          | Multiple devices, modern usage       |

### Memory Anchor

```text
POP3  →  Pull and go (like downloading a file to your machine)
IMAP  →  Access in place (like working in Google Drive)
SMTP  →  Send mail out
```

---

## 14. Telnet — Manual Protocol Testing

### Why Telnet?

Telnet is **not** the protocol being studied in most tasks — it is being used as a **raw TCP client** to talk directly to plaintext services. This strips away the GUI and lets you observe the actual protocol exchange.

```bash
telnet TARGET_IP 80    # HTTP
telnet TARGET_IP 25    # SMTP
telnet TARGET_IP 110   # POP3
telnet TARGET_IP 143   # IMAP
telnet TARGET_IP 21    # FTP (control channel)
```

### Netcat (nc) — The Better Alternative

`nc` does the same thing and is more flexible:

```bash
nc TARGET_IP 80
nc TARGET_IP 110
nc -v TARGET_IP 25     # verbose — shows connection status
```

> In CTFs and real assessments, `nc` is preferred over `telnet` because it is available on more systems, handles binary data cleanly, and is scriptable.

### Why This Matters

Manual protocol interaction teaches you:
- What the protocol actually looks like on the wire
- How minimal a valid request can be
- What error messages look like at the protocol level
- How service banners leak software names and version numbers

---

## 15. Port Reference Cheat Sheet

| Service         | Protocol       | Default Port   | Encrypted Port       |
| --------------- | -------------- | -------------- | -------------------- |
| DNS             | UDP (+ TCP)    | 53             | 853 (DoT)            |
| HTTP            | TCP            | 80             | 443 (HTTPS/TLS)      |
| FTP (control)   | TCP            | 21             | 990 (implicit FTPS)  |
| FTP (data)      | TCP            | 20 (active)    | —                    |
| SMTP (relay)    | TCP            | 25             | —                    |
| SMTP (submit)   | TCP            | 587 (STARTTLS) | 465 (SMTPS)          |
| POP3            | TCP            | 110            | 995 (POP3S)          |
| IMAP            | TCP            | 143            | 993 (IMAPS)          |
| Telnet          | TCP            | 23             | — (never encrypted)  |
| SSH             | TCP            | 22             | always encrypted     |

> During pentesting, services do not always run on their default port. Always scan with Nmap — the port number is a hint, not a guarantee.

---

## 16. Protocol Relationships

### Big Picture

```text
                      NETWORKING STACK
                            |
           +----------------+----------------+
           |                |                |
          DNS              WEB             EMAIL
           |                |                |
        A/AAAA/MX         HTTP/HTTPS    SMTP / POP3 / IMAP
           |                |                |
      Name to IP       Browser to Server    Mail flow
```

### Email Flow End-to-End

```text
                        SMTP (587/465)
Alice's Mail Client ─────────────────────> Alice's Mail Server (MTA)
                                                   |
                                            SMTP (port 25)
                                                   |
                                                   v
                                         Bob's Mail Server (MTA)
                                                   |
                                        POP3 (110) or IMAP (143)
                                                   |
                                                   v
                                          Bob's Mail Client
```

---

## 17. Cybersecurity Perspective

### DNS

| Use case             | How                                                              |
| -------------------- | ---------------------------------------------------------------- |
| Infrastructure recon | A/AAAA records map IP ranges                                     |
| Subdomain discovery  | Brute force or certificate transparency logs                     |
| Mail server mapping  | MX records                                                       |
| Zone transfer (AXFR) | `dig axfr @ns1.example.com example.com` — dumps all records if misconfigured |
| Cache poisoning      | Injecting false DNS responses to redirect traffic                |
| DNS tunneling        | Exfiltrating data via DNS TXT/A query payloads                   |

### WHOIS

| Use case                | Notes                                                 |
| ----------------------- | ----------------------------------------------------- |
| Passive recon           | No packets to target — fully passive                  |
| Domain age assessment   | Older domains tend to have more email trust           |
| Registrar correlation   | Find other domains with same registrant email         |
| Historical data         | DomainTools, SecurityTrails, whoxy.com                |

### HTTP

| Use case               | Relevance                                              |
| ---------------------- | ------------------------------------------------------ |
| Web enumeration        | `gobuster`, `ffuf`, `dirb` — brute-force paths/files   |
| Auth testing           | Understand request/response to test login logic        |
| Parameter manipulation | Base for SQLi, XSS, IDOR, SSRF, CSRF                  |
| Header analysis        | Leak server software version, misconfiguration flags   |
| Request smuggling      | HTTP/1.1 + HTTP/2 boundary desync attacks              |

### FTP

| Use case                  | Notes                                                |
| ------------------------- | ---------------------------------------------------- |
| Anonymous login check     | `ftp TARGET` then `user: anonymous`                  |
| Sensitive file exposure   | Config files, credentials, backups                   |
| Writable directory abuse  | Upload webshell if FTP root overlaps web root        |
| Plaintext credential sniff | Capturable with Wireshark on the same LAN           |

### SMTP

| Use case           | Notes                                                          |
| ------------------ | -------------------------------------------------------------- |
| User enumeration   | `VRFY user` or `RCPT TO:` timing/response differences         |
| Email spoofing     | Weak/missing SPF, DKIM, DMARC allows forged sender            |
| Open relay testing | `MAIL FROM: external; RCPT TO: external` — if accepted, it is an open relay |
| Phishing infra     | Understand mail headers to trace phishing origin               |

### POP3 / IMAP

| Use case              | Notes                                              |
| --------------------- | -------------------------------------------------- |
| Credential brute force | `hydra` supports both protocols                   |
| Mailbox enumeration   | IMAP `LIST` dumps full folder structure            |
| Incident response     | Read attacker mailbox during IR engagement         |
| Plaintext exposure    | POP3/IMAP without TLS = credentials in cleartext  |

---

## 18. Command Reference

```bash
# ─── DNS ─────────────────────────────────────────────────────────────
nslookup example.com
dig example.com
dig example.com A
dig example.com AAAA
dig example.com MX
dig example.com NS
dig example.com TXT
dig -x 93.184.216.34                         # Reverse lookup
dig axfr @ns1.example.com example.com        # Zone transfer attempt
dig @8.8.8.8 example.com                     # Use specific resolver

# ─── WHOIS ───────────────────────────────────────────────────────────
whois example.com
whois 93.184.216.34                          # IP/ASN lookup

# ─── HTTP ────────────────────────────────────────────────────────────
curl http://TARGET_IP
curl -I http://TARGET_IP                     # Headers only
curl -v http://TARGET_IP                     # Verbose
curl -L http://TARGET_IP                     # Follow redirects
curl -X POST -d "key=val" http://TARGET_IP/path

# ─── FTP ─────────────────────────────────────────────────────────────
ftp TARGET_IP
# Inside FTP shell: ls / pwd / cd <dir> / get <file> / put <file> / bye

# ─── Raw TCP — HTTP ──────────────────────────────────────────────────
nc TARGET_IP 80
# type: GET / HTTP/1.1
#       Host: TARGET_IP
#       (blank line)

# ─── Raw TCP — POP3 ──────────────────────────────────────────────────
nc TARGET_IP 110
# USER alice → PASS secret → LIST → RETR 4 → QUIT

# ─── Raw TCP — IMAP ──────────────────────────────────────────────────
nc TARGET_IP 143
# A LOGIN alice secret → A SELECT INBOX → A FETCH 4 BODY[] → A LOGOUT

# ─── Raw TCP — SMTP ──────────────────────────────────────────────────
nc TARGET_IP 25
# EHLO x → MAIL FROM:<x@x.com> → RCPT TO:<y@y.com> → DATA → . → QUIT

# ─── Nmap quick scan ─────────────────────────────────────────────────
nmap -sV -p 21,25,80,110,143,443,587,993,995 TARGET_IP
```

---

## 19. Learning Progression

Build understanding in layers — do not just memorize commands:

| Level | Focus                   | Goal                                                         |
| ----- | ----------------------- | ------------------------------------------------------------ |
| 1     | Concept                 | What does this protocol do? What problem does it solve?      |
| 2     | Communication model     | Who talks first? What is the request/response structure?     |
| 3     | Manual interaction      | Can you use `nc` / `curl` / `ftp` / `dig` yourself?         |
| 4     | Security implications   | What is exposed? What can be misused? What defends it?       |

Level 4 is what separates someone who read notes from someone who can actually enumerate a target.

---

## 20. Room Q&A Reference

Commonly documented answers for this TryHackMe room:

| Question                                              | Answer           |
| ----------------------------------------------------- | ---------------- |
| DNS record type for IPv6 address                      | `AAAA`           |
| DNS record type for email server                      | `MX`             |
| `x.com` creation date (WHOIS)                         | `1993-04-02`     |
| `twitter.com` creation date (WHOIS)                   | `2000-01-21`     |
| SMTP command that starts email body input             | `DATA`           |
| Character that terminates an SMTP message body        | `.`              |
| POP3 server software identified in the lab            | `Dovecot`        |
| IMAP command to retrieve the 4th email                | `FETCH 4 BODY[]` |

> Retrieve the actual lab flags yourself — that is the point. If you can manually connect to a POP3 server with `nc` and read an email, you have learned something real.

---

## 21. Quick Revision Sheet

> Use this if you have 5 minutes before an exam or interview.

```text
DNS
  → Name to IP resolution
  → A = IPv4, AAAA = IPv6, MX = mail, CNAME = alias, NS = nameserver
  → dig / nslookup
  → Recon: subdomain enum, zone transfer, infrastructure mapping

WHOIS
  → Domain registration data
  → Passive recon — no contact with target
  → whois example.com

HTTP / HTTPS
  → Web communication
  → TCP/80 (plaintext), TCP/443 (TLS)
  → Methods: GET POST PUT PATCH DELETE HEAD
  → Status: 200 OK, 301 redirect, 401 unauth, 403 forbidden, 404 missing, 500 error
  → curl / nc

FTP
  → File transfer
  → TCP/21 (control), TCP/20 (data, active mode)
  → Anonymous: user=anonymous pass=anonymous
  → get / put / ls / bye
  → PLAINTEXT — prefer SFTP or FTPS

SMTP
  → Sends email (client to server and server to server)
  → Ports: 25 (relay), 587 (STARTTLS), 465 (SMTPS)
  → EHLO → MAIL FROM → RCPT TO → DATA → . → QUIT
  → Defenses: SPF, DKIM, DMARC

POP3
  → Retrieves email to local client
  → TCP/110, POP3S = 995
  → USER → PASS → LIST → RETR n → QUIT
  → Downloads mail (often deletes from server)

IMAP
  → Accesses and syncs mail on the server
  → TCP/143, IMAPS = 993
  → A LOGIN → A SELECT INBOX → A FETCH n BODY[] → A LOGOUT
  → Mail stays on server — great for multi-device use

TELNET / NC
  → Raw TCP clients for manual protocol testing
  → nc TARGET PORT  (preferred over telnet in practice)
```

### Protocol Mental Model

```text
DNS          →  "Where is the server?"
     |
HTTP         →  "Give me the webpage"
     |
FTP          →  "Transfer me this file"
     |
SMTP         →  "Send this email"
     |
POP3 / IMAP  →  "Let me access my mailbox"
```

---

*This room provides the protocol-level foundation underneath later work with Nmap, Wireshark, Burp Suite, web exploitation, email security, and network enumeration. The next room — [Networking Secure Protocols](https://tryhackme.com/room/networkingsecureprotocols) — revisits all of these with TLS, SSH, SFTP/FTPS, and VPN layered on top.*
