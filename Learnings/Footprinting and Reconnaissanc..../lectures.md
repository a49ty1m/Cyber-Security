# Footprinting / Reconnaissance — Basics (TIL)

**Source:** Module 5 — Footprinting / Reconnaissance. :contentReference[oaicite:1]{index=1}

---

## 1 — What is footprinting?
Footprinting = the first step of an attack: systematically collecting public information about a target (company, domain, or network) to build an intelligence picture.  
It can be **passive** (no direct interaction; low/no detection) or **active** (interacts with target assets; more accurate but noisy). :contentReference[oaicite:2]{index=2}

---

## 2 — Primary goals / objectives
- Learn the target’s **security posture** and find weak spots.  
- Identify **IP ranges, hosts, services, and technology stacks**.  
- Map the network logically (services → hosts → access points).  
- Collect **organizational info** (employees, emails, phone numbers, job postings).  
- Locate juicy artifacts: open ports, exposed services, misconfigured DNS, leakable backups. :contentReference[oaicite:3]{index=3}

---

## 3 — Types of footprinting
- **Passive footprinting** — search engines, public records, social media, archives (no direct probes). :contentReference[oaicite:4]{index=4}  
- **Active footprinting** — DNS queries, traceroute, direct probes, service banners (can alert the target). :contentReference[oaicite:5]{index=5}

---

## 4 — What to collect (categories)
- **Network:** domain names, IP ranges, subdomains, active hosts, open TCP/UDP services, routing/traceroute info. :contentReference[oaicite:6]{index=6}  
- **System:** banners, OS versions, SNMP data, routing tables, system names. :contentReference[oaicite:7]{index=7}  
- **Org / People:** employee names, roles, job ads (reveal tech stacks), contact details, press releases. :contentReference[oaicite:8]{index=8}  
- **Website artifacts:** HTML comments, directories, robots.txt, sitemap, server headers, CMS info. :contentReference[oaicite:9]{index=9}

---

## 5 — Common techniques & tools (quick practicals)
> **Passive / OSINT**
- **Search engines / Google dorks** — find hidden pages, files, and login portals.  
  - Examples: `site:target.com inurl:admin`, `site:target.com filetype:env`, `intitle:"index of" site:target.com`. :contentReference[oaicite:10]{index=10}  
- **Archives & caches** — Google Cache, Wayback Machine to recover removed pages.  
- **Social media / people search** — LinkedIn, Twitter, GitHub for employees & tech hints. :contentReference[oaicite:11]{index=11}  
- **Job sites** — job descriptions often list exact software/hardware (useful for attack surface). :contentReference[oaicite:12]{index=12}  
- **Alerts** — Google Alerts / Twitter Alerts to monitor target activity. :contentReference[oaicite:13]{index=13}

> **Active (lab / with permission)**  
- **WHOIS** — get registrar, name servers, contact info, registration dates.  
  ```bash
  whois example.com
