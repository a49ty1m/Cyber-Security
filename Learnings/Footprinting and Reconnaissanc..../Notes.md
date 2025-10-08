# Footprinting / Reconnaissance

> Short notes for quick study and a GitHub `README.md` file.

---

## Table of Contents
- [Overview](#overview)
- [Basics of Footprinting](#basics-of-footprinting)
- [Types of Footprinting](#types-of-footprinting)
- [Objectives](#objectives)
- [Footprinting Methods & Tools](#footprinting-methods--tools)
  - [Search Engine Footprinting](#search-engine-footprinting)
  - [OSINT](#osint)
  - [Email Footprinting](#email-footprinting)
  - [Website Footprinting](#website-footprinting)
  - [Google Hacking (Dorks)](#google-hacking-dorks)
  - [Competitive Intelligence](#competitive-intelligence)
  - [DNS Footprinting](#dns-footprinting)
  - [Network Footprinting](#network-footprinting)
  - [Social Engineering](#social-engineering)
- [Countermeasures](#countermeasures)
- [Quick Reference — Tools & Links](#quick-reference--tools--links)
- [Quote](#quote)

---

## Overview
Footprinting (reconnaissance) is the first phase in ethical hacking: collecting as much information about a target (organization, system, or person) as possible to map the attack surface. This can be done passively (stealthy) or actively (interactive and detectable).

---

## Basics of Footprinting
- Purpose: gather domain names, IP addresses, employee info, contact details, software/OS, services, and infrastructure hints.  
- Outcome: a map of the target's public footprint used to prioritize testing and find vulnerabilities.

---

## Types of Footprinting
- **Passive Footprinting**  
  Collecting information without direct interaction with the target (e.g., search engines, archives, public records). Low/no risk of detection.

- **Active Footprinting**  
  Directly interacting with the target's assets (e.g., scanning, probing). Faster and more accurate but may be detected.

---

## Objectives
- **Assess security posture** — find weaknesses and plan tests.  
- **Narrow focus** — identify IP ranges, subdomains, and critical assets.  
- **Find vulnerabilities** — use gathered info to discover weak points.  
- **Map the network** — visualize hosts, services, and relationships.

Information categories:
- **Network:** domain names, IP ranges, exposed services, ACLs, VPN endpoints.  
- **System:** users/groups, banners, routing, SNMP, OS & architecture.  
- **Organizational:** employee names, directories, contact info, press releases, site comments.

---

## Footprinting Methods & Tools

### Search Engine Footprinting
- Use search engines and archives to discover hidden or removed pages, directories, login portals, and developer comments.
- Look for **restricted URLs**, job posts revealing tech, and cached/archived pages.
- Useful tools: **Netcraft**, **SHODAN**, **Google Maps / Google Earth**, **Wayback Machine**.

### OSINT (Open-Source Intelligence)
- Publicly available sources: social media, blogs, code repositories, news, and official websites.
- Goals: find IPs/subdomains, tech stack, exposed credentials, API keys, and leaked configuration files.

### Email Footprinting
- Trace email headers to determine sender IP, mail route, sender identity, and sometimes geolocation.
- Email tracking techniques can reveal recipient behavior, client, and OS info.

### Website Footprinting
- Inspect HTML source, comments, and cookies for developer contact, file paths, CMS info, and server details.
- Use proxies and scanners (Burp Suite, ZAProxy) to capture headers and identify software versions.
- Web spiders and mirroring (wget, HTTrack) help map directories offline.

### Google Hacking (Dorks)
- Advanced Google operators help locate sensitive content:
```text
cache:example.com
site:example.com inurl:admin
intitle:"index of" "backup"
inurl:login site:example.com
filetype:env OR filetype:sql "DB_PASSWORD"
```
- Combine operators to find config files, exposed backups, and admin pages.

### Competitive Intelligence
- Gather competitor/company info from websites, job listings, press releases, reports, and trade journals.
- Monitor site traffic, reputation, product launches, and public filings for strategic insight.

### DNS Footprinting
- Use WHOIS lookups and RIRs (ARIN, RIPE, APNIC, LACNIC, AFRINIC).
- Extract registrant, name servers, creation/expiry dates, and delegated IP blocks.
- DNS records help discover mail servers, subdomains, and potential entry points.

#### DNS Record Types

| Record Type | Purpose | Information Revealed |
|:-----------:|---------|---------------------|
| **A** | Maps domain to IPv4 address | Web server IP, hosting location |
| **AAAA** | Maps domain to IPv6 address | IPv6 infrastructure, modern setup |
| **MX** | Mail exchange servers | Email server IPs, mail routing |
| **CNAME** | Canonical name (alias) | Subdomain structure, CDN usage |
| **NS** | Name servers | DNS infrastructure, hosting provider |
| **TXT** | Text records | SPF, DKIM, verification codes |
| **SOA** | Start of Authority | Primary DNS server, admin contact |
| **PTR** | Reverse DNS lookup | Hostname from IP address |
| **SRV** | Service records | Service locations, ports |

### Network Footprinting
- Identify IP ranges, exposed hosts, services, OS, and patch levels.
- Use traceroute to map network paths and identify gateways and network topology.

### Social Engineering
- Exploit human behavior to extract information:
  - **Eavesdropping** — intercepting communications.
  - **Shoulder surfing** — observing credentials or screens.
  - **Dumpster diving** — retrieving sensitive printed material from trash.
- Social engineering can reveal credentials, infrastructure details, and operational procedures.

---

## Countermeasures
- Limit employee access to social sites on corporate networks; educate staff about oversharing.
- Configure web servers and CMS to avoid info leakage (disable directory listing, remove comments).
- Use WHOIS privacy and anonymous registration for domains.
- Enforce split DNS and restrict zone transfers.
- Apply strict release policies for press/documents; redact sensitive details.
- Use IDS/IPS and monitor for suspicious footprinting patterns.
- Encrypt and password-protect sensitive data and backups.
- Regularly scan public internet presence to remove exposed sensitive assets.

---

## Quick Reference — Tools & Links
- **Search / Recon:** Google (with dorks), Netcraft, Wayback Machine
- **Device & IoT discovery:** SHODAN
- **Web proxies & analysis:** Burp Suite, OWASP ZAP, Paros Proxy, Firebug
- **Mirroring & spiders:** wget, httrack, web spiders
- **WHOIS & RIRs:** ARIN, RIPE, APNIC, LACNIC, AFRINIC
- **Alerts & monitoring:** Google Alerts, Twitter alerts

---

## Quote
*"Hacking is an art, practiced through a creative mind."*