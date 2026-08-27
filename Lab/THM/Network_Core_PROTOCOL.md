Absolutely. I checked the current TryHackMe room first. **Networking Core Protocols** is the third room in TryHackMe’s networking sequence, after *Networking Concepts* and *Networking Essentials*. Its focus is the practical behavior of **DNS, WHOIS, HTTP, FTP, SMTP, POP3, and IMAP**. ([TryHackMe][1])

One important point: the current room page marks Tasks 2–9 as **Premium**, so I can’t reliably reproduce every lab instruction from the room itself. I can, however, build you a proper study/lab note around the room's objectives and publicly verifiable material. ([TryHackMe][2])

# Networking Core Protocols — TryHackMe Notes

[TryHackMe — Networking Core Protocols](https://tryhackme.com/room/networkingcoreprotocols?utm_source=chatgpt.com)

## 1. Lab Overview

**Room:** Networking Core Protocols
**Category:** Networking
**Position:** 3rd room in the Networking series

### Learning objectives

By completing this room, you should understand:

* DNS
* WHOIS
* HTTP / HTTPS
* FTP
* SMTP
* POP3
* IMAP
* Basic client-server communication
* How these protocols can be interacted with from the command line

TryHackMe specifically expects prior knowledge of:

* OSI model
* TCP/IP model
* Ethernet
* IP
* TCP ([TryHackMe][2])

---

# 2. Core Idea — What Is a Network Protocol?

A **network protocol** is a defined set of rules that determines how systems communicate.

Think of it as a language between computers.

For example:

```text
Client                         Server
  |                              |
  |-------- HTTP Request ------->|
  |                              |
  |<------- HTTP Response -------|
```

Both sides must understand the protocol's rules.

Different protocols solve different problems:

| Protocol | Main Purpose                    |
| -------- | ------------------------------- |
| DNS      | Name → IP resolution            |
| WHOIS    | Domain registration information |
| HTTP     | Web communication               |
| FTP      | File transfer                   |
| SMTP     | Sending email                   |
| POP3     | Downloading/receiving email     |
| IMAP     | Synchronizing/accessing email   |

Most of these operate at the **Application layer** of the TCP/IP model. ([TryHackMe][3])

---

# 3. DNS — Domain Name System

## What is DNS?

DNS translates human-readable domain names into IP addresses.

Example:

```text
example.com
     ↓
93.184.216.34
```

Without DNS, users would need to remember IP addresses instead of domain names.

### Basic process

```text
User
 ↓
Browser
 ↓
DNS Resolver
 ↓
DNS Server
 ↓
IP Address
 ↓
Web Server
```

---

## Important DNS Record Types

| Record | Purpose                                            |
| ------ | -------------------------------------------------- |
| A      | IPv4 address                                       |
| AAAA   | IPv6 address                                       |
| MX     | Mail server                                        |
| CNAME  | Alias for another domain                           |
| NS     | Authoritative name server                          |
| TXT    | Arbitrary text / verification / policy information |
| PTR    | Reverse DNS lookup                                 |
| SOA    | Zone authority information                         |

### Remember

```text
A       → IPv4
AAAA    → IPv6
MX      → Mail server
CNAME   → Alias
NS      → Name server
TXT     → Text/policy
PTR     → IP → hostname
```

The room specifically tests **AAAA** for IPv6 and **MX** for email servers. ([GitHub][4])

---

## Useful Commands

### Resolve a domain

```bash
nslookup example.com
```

or:

```bash
dig example.com
```

### Query a specific record

```bash
dig example.com A
```

```bash
dig example.com AAAA
```

```bash
dig example.com MX
```

```bash
dig example.com NS
```

### Security relevance

DNS is extremely important during reconnaissance.

You can discover:

```text
Domain
 ↓
DNS records
 ↓
IP addresses
 ↓
Mail infrastructure
 ↓
Name servers
 ↓
Potential attack surface
```

For penetration testing, DNS enumeration can help identify infrastructure belonging to an organization.

---

# 4. WHOIS

## What is WHOIS?

**WHOIS** is used to retrieve registration information about Internet resources such as domains.

Depending on the registry and privacy settings, information may include:

* Registrar
* Registration date
* Expiration date
* Nameservers
* Domain status
* Registrant information
* Administrative information

Privacy regulations and registrar privacy services mean that personal information is often hidden.

---

## Command

```bash
whois example.com
```

Example workflow:

```bash
whois x.com
```

The room uses WHOIS to investigate domain registration information. Public walkthrough material reports the historical creation dates for `x.com` and `twitter.com` as **1993-04-02** and **2000-01-21**, respectively. ([GitHub][4])

### Security relevance

WHOIS is useful during:

**Passive reconnaissance**

You can potentially determine:

```text
Target domain
      ↓
Registrar
      ↓
Registration information
      ↓
Nameservers
      ↓
Infrastructure clues
```

---

# 5. HTTP — Hypertext Transfer Protocol

## What is HTTP?

HTTP is the protocol used for communication between web clients and web servers.

Basic model:

```text
Browser
   |
   | HTTP Request
   ↓
Web Server
   |
   | HTTP Response
   ↓
Browser
```

HTTP normally uses:

```text
TCP/80
```

HTTPS normally uses:

```text
TCP/443
```

---

# 6. HTTP Request

A basic HTTP request looks conceptually like:

```http
GET / HTTP/1.1
Host: example.com
```

Important request methods:

| Method | Purpose                              |
| ------ | ------------------------------------ |
| GET    | Retrieve resource                    |
| POST   | Submit data                          |
| PUT    | Replace/update resource              |
| PATCH  | Partially update resource            |
| DELETE | Delete resource                      |
| HEAD   | Retrieve headers without normal body |

---

# 7. HTTP Response

A server responds with something like:

```http
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: ...
```

### Important status codes

| Code | Meaning               |
| ---- | --------------------- |
| 200  | OK                    |
| 201  | Created               |
| 301  | Permanent redirect    |
| 302  | Temporary redirect    |
| 400  | Bad request           |
| 401  | Unauthorized          |
| 403  | Forbidden             |
| 404  | Not found             |
| 500  | Internal server error |
| 503  | Service unavailable   |

---

# 8. HTTP From the Command Line

You can interact with HTTP without a browser.

### curl

```bash
curl http://TARGET_IP
```

Headers only:

```bash
curl -I http://TARGET_IP
```

Verbose communication:

```bash
curl -v http://TARGET_IP
```

### Telnet

You can manually communicate with an HTTP server:

```bash
telnet TARGET_IP 80
```

Then:

```http
GET / HTTP/1.1
Host: TARGET_IP

```

Notice the blank line at the end.

That blank line tells the server that the HTTP headers are finished.

---

## Security relevance

Understanding HTTP at this level is fundamental for web security.

You need to understand:

```text
Request
 ↓
Method
 ↓
URL
 ↓
Headers
 ↓
Parameters
 ↓
Body
 ↓
Server processing
 ↓
Response
```

This becomes important when studying:

* SQL injection
* XSS
* Authentication vulnerabilities
* IDOR
* CSRF
* SSRF
* Request smuggling
* Web enumeration

---

# 9. FTP — File Transfer Protocol

## What is FTP?

FTP is a protocol designed for transferring files between a client and server.

Traditional FTP commonly uses:

```text
TCP/21 → Control connection
```

FTP has historically been used for:

* Uploading files
* Downloading files
* Directory listing
* File management

---

## Basic FTP interaction

Connect:

```bash
ftp TARGET_IP
```

Common commands:

```text
ls
pwd
cd
get
put
bye
```

Example:

```text
ftp TARGET_IP
```

Then:

```text
Name: anonymous
Password: anonymous
```

if anonymous access is enabled.

---

## Downloading a file

```text
get flag.txt
```

Then leave:

```text
bye
```

The room's publicly documented exercise involves connecting to the lab FTP server and retrieving `flag.txt`; a public walkthrough records the resulting lab flag as `THM{FAST-FTP}`. ([GitHub][4])

---

# 10. FTP Security

Traditional FTP is **not encrypted**.

That means credentials and transferred information can potentially be exposed to someone able to observe the traffic.

This is why modern environments commonly use alternatives such as:

```text
SFTP
FTPS
```

Don't confuse:

```text
FTP
SFTP
FTPS
```

They are different technologies.

---

# 11. SMTP — Simple Mail Transfer Protocol

## What is SMTP?

SMTP is primarily responsible for **sending email**.

Think:

```text
Email Client
     ↓
SMTP Server
     ↓
Recipient Mail Server
```

Typical SMTP ports include:

```text
25
587
465
```

Port usage depends on the deployment and security mechanism.

---

# 12. SMTP Commands

Important SMTP commands include:

```text
HELO
EHLO
MAIL FROM:
RCPT TO:
DATA
QUIT
```

Example conceptual interaction:

```text
Client → EHLO example.com
Server → 250 ...

Client → MAIL FROM:<alice@example.com>
Server → 250 ...

Client → RCPT TO:<bob@example.com>
Server → 250 ...

Client → DATA
Server → 354 ...

Client → Email content
Client → .
Server → 250 ...
```

### Important point

`DATA` tells the server that the client is beginning the actual email content.

A single:

```text
.
```

on a line by itself indicates that the email content has finished.

The room specifically tests both of these concepts. ([GitHub][4])

---

# 13. SMTP Security Relevance

SMTP knowledge matters for understanding:

* Email spoofing
* Phishing
* Mail server enumeration
* SPF
* DKIM
* DMARC
* Email infrastructure

For your cybersecurity roadmap, SMTP is particularly important because it connects networking fundamentals to **email security and reconnaissance**.

---

# 14. POP3 — Post Office Protocol 3

## What is POP3?

POP3 is designed primarily for retrieving email from a mail server.

Typical port:

```text
TCP/110
```

Secure variant:

```text
TCP/995
```

Conceptually:

```text
Mail Server
     |
     | POP3
     ↓
Email Client
```

POP3 traditionally focuses on downloading messages to the client.

---

# 15. POP3 Commands

Common commands:

```text
USER
PASS
STAT
LIST
RETR
DELE
QUIT
```

Example:

```text
USER username
PASS password
LIST
RETR 1
```

### RETR

`RETR` retrieves a particular email message.

For example:

```text
RETR 4
```

retrieves message number 4.

The room uses Telnet to interact with the POP3 service and retrieve a flag from the fourth message. Publicly documented walkthrough material identifies the server as **Dovecot** and records the lab flag as `THM{TELNET_RETR_EMAIL}`. ([GitHub][4])

---

# 16. IMAP — Internet Message Access Protocol

## What is IMAP?

IMAP allows clients to access and synchronize mail stored on a server.

Typical port:

```text
TCP/143
```

Secure IMAP commonly uses:

```text
TCP/993
```

The important conceptual difference:

### POP3

```text
Server
  ↓
Download mail
  ↓
Client
```

### IMAP

```text
Server
 ↕
Synchronize mailbox
 ↕
Client
```

IMAP is much better suited to situations where you access the same mailbox from:

* Laptop
* Phone
* Tablet
* Webmail

because messages and mailbox state can remain synchronized on the server.

---

# 17. IMAP Commands

IMAP commands are slightly different from POP3.

Example:

```text
A LOGIN username password
```

Select mailbox:

```text
A SELECT INBOX
```

Retrieve a message:

```text
A FETCH 4 BODY[]
```

The room specifically asks which IMAP command retrieves the fourth email message; publicly documented material gives:

```text
FETCH 4 BODY[]
```

([GitHub][4])

---

# 18. POP3 vs IMAP

| Feature                | POP3                 | IMAP                     |
| ---------------------- | -------------------- | ------------------------ |
| Main purpose           | Retrieve email       | Access/synchronize email |
| Server storage         | Often downloads mail | Mail remains server-side |
| Multi-device use       | Poorer               | Better                   |
| Folder synchronization | Limited              | Yes                      |
| Server-side management | Limited              | Extensive                |
| Common port            | 110                  | 143                      |
| Secure version         | POP3S 995            | IMAPS 993                |

### Easy memory trick

```text
POP3 → Pull mail
IMAP → Manage mail on server
SMTP → Send mail
```

---

# 19. Telnet — Why Are We Using It?

This is one of the most important lessons of the room.

Telnet is not the protocol being studied for most of these tasks.

It is being used as a **basic TCP client** that lets you manually talk to services.

For example:

```bash
telnet TARGET_IP 80
```

means:

```text
Telnet
  ↓
TCP connection
  ↓
Port 80
  ↓
HTTP service
```

Similarly:

```bash
telnet TARGET_IP 110
```

connects to the POP3 service.

This strips away the GUI and lets you see the underlying protocol.

---

# 20. Protocol → Port Cheat Sheet

Memorize this:

| Service         | Protocol      | Common Port |
| --------------- | ------------- | ----------: |
| DNS             | DNS           |          53 |
| HTTP            | HTTP          |          80 |
| HTTPS           | HTTPS         |         443 |
| FTP             | FTP           |          21 |
| SMTP            | SMTP          |          25 |
| SMTP Submission | SMTP          |         587 |
| POP3            | POP3          |         110 |
| IMAP            | IMAP          |         143 |
| POP3S           | POP3 over TLS |         995 |
| IMAPS           | IMAP over TLS |         993 |

**Don't blindly memorize ports without understanding the service.** During enumeration, the port is a clue, not proof of what is actually running.

---

# 21. Protocol Relationships

This is the bigger picture you should understand:

```text
                    NETWORKING
                        |
        +---------------+---------------+
        |               |               |
       DNS            WEB             EMAIL
        |               |               |
      DNS             HTTP          SMTP/POP3/IMAP
        |               |               |
   Name → IP       Client ↔ Server    Mail
```

And the email flow:

```text
                    SMTP
Sender ─────────────────────→ Sender Mail Server
                                  |
                                  | SMTP
                                  ↓
                            Recipient Server
                                  |
                           POP3 / IMAP
                                  |
                                  ↓
                           Recipient Client
```

---

# 22. Cybersecurity Perspective

This is where you should stop thinking of the room as "just networking."

These protocols directly appear during security assessments.

### DNS

Useful for:

* Infrastructure discovery
* Subdomain enumeration
* Mail server discovery
* Mapping external assets

### WHOIS

Useful for:

* Passive reconnaissance
* Registrar identification
* Registration timeline
* Infrastructure research

### HTTP

Critical for:

* Web enumeration
* Web application testing
* Authentication testing
* Request manipulation
* Vulnerability research

### FTP

Useful for:

* Anonymous login testing
* File enumeration
* Misconfiguration discovery
* Sensitive file exposure

### SMTP

Useful for understanding:

* Email infrastructure
* Mail-server behavior
* Spoofing
* Phishing
* SPF/DKIM/DMARC

### POP3 / IMAP

Useful for:

* Email investigations
* Mailbox enumeration
* Credential exposure analysis
* Incident response

---

# 23. Commands to Keep in Your Notes

```bash
# DNS
nslookup example.com
dig example.com
dig example.com MX
dig example.com AAAA

# WHOIS
whois example.com

# HTTP
curl http://TARGET_IP
curl -I http://TARGET_IP
curl -v http://TARGET_IP

# FTP
ftp TARGET_IP

# Raw TCP interaction
telnet TARGET_IP 80
telnet TARGET_IP 110
```

For a real assessment, you'd normally also use tools such as:

```bash
nmap
nc
curl
dig
nslookup
whois
```

---

# 24. Important Commands vs Concepts

Don't make the mistake of memorizing every command without understanding what is happening.

Your priority should be:

**Level 1 — Understand**

```text
What is DNS?
What is HTTP?
What is FTP?
What is SMTP?
What is POP3?
What is IMAP?
```

**Level 2 — Understand communication**

```text
Client
   ↓
TCP connection
   ↓
Service
   ↓
Protocol commands
   ↓
Response
```

**Level 3 — Interact manually**

```bash
telnet
curl
ftp
dig
whois
```

**Level 4 — Analyze security implications**

```text
What information is exposed?
What happens without encryption?
What can be enumerated?
What can be misconfigured?
What can an attacker observe?
```

That's the level that actually matters for your pentesting path.

---

# 25. Room Questions / Answers to Know

Based on publicly available walkthrough material, the commonly documented answers include: ([GitHub][4])

| Question                              | Answer           |
| ------------------------------------- | ---------------- |
| DNS record for IPv6                   | `AAAA`           |
| DNS record for email server           | `MX`             |
| x.com creation date                   | `1993-04-02`     |
| twitter.com creation date             | `2000-01-21`     |
| SMTP command starting message content | `DATA`           |
| SMTP message terminator               | `.`              |
| POP3 server identified in lab         | `Dovecot`        |
| IMAP command for 4th email            | `FETCH 4 BODY[]` |

For the actual flags, **I recommend you retrieve them yourself in the lab rather than treating a walkthrough's flag as your learning objective**. The point of this room is learning how to communicate with the services manually.

---

# 26. Final Revision Sheet

If you have only **5 minutes before an exam/interview**, remember this:

```text
DNS
→ Converts domain names to IP addresses
→ A = IPv4
→ AAAA = IPv6
→ MX = mail server

WHOIS
→ Domain registration information
→ whois example.com

HTTP
→ Web communication
→ TCP/80
→ GET, POST, PUT, DELETE
→ 200, 301, 403, 404, 500

FTP
→ File transfer
→ TCP/21
→ get / put / ls
→ Traditional FTP is plaintext

SMTP
→ Sends email
→ 25 / 587 / 465
→ MAIL FROM
→ RCPT TO
→ DATA
→ . terminates message

POP3
→ Retrieves email
→ TCP/110
→ RETR retrieves message
→ POP3S = 995

IMAP
→ Server-side email access/synchronization
→ TCP/143
→ IMAPS = 993
→ FETCH retrieves message

TELNET
→ Basic TCP client
→ Useful for manually interacting with plaintext services
```

### The mental model

```text
        DNS
        ↓
  "Where is the server?"
        ↓
       HTTP
        ↓
  "Give me the webpage"
        ↓
       FTP
        ↓
  "Give/send me this file"
        ↓
      SMTP
        ↓
  "Send this email"
        ↓
   POP3 / IMAP
        ↓
  "Let me access my mail"
```

This room is worth taking seriously because it gives you the **protocol-level foundation** underneath later work with Nmap, Wireshark, Burp Suite, web exploitation, email security, and network enumeration. TryHackMe itself places *Networking Secure Protocols* immediately after this room, where those plaintext protocols are revisited with TLS, SSH, SFTP/FTPS, and VPN security. ([TryHackMe][5])

[1]: https://tryhackme.com/room/networkingcoreprotocols?utm_source=chatgpt.com "TryHackMe | Networking Core Protocols"
[2]: https://tryhackme.com/room/networkingcoreprotocols "TryHackMe | Networking Core Protocols"
[3]: https://tryhackme.com/room/networkingconcepts?utm_source=chatgpt.com "TryHackMe | Networking Concepts"
[4]: https://github.com/cosmicline/TryHackMe-Answers/blob/main/Networking%20Core%20Protocols?utm_source=chatgpt.com "TryHackMe-Answers/Networking Core Protocols at main · cosmicline/TryHackMe-Answers · GitHub"
[5]: https://tryhackme.com/room/networkingsecureprotocols?utm_source=chatgpt.com "TryHackMe | Networking Secure Protocols"
