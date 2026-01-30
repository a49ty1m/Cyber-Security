# 🔍 Footprinting & Reconnaissance Notes

## 📑 Table of Contents
1. [Internet Archive (archive.org)](#internet-archive-archiveorg)
2. [wget](#wget)
3. [HTTrack](#httrack)
4. [WHOIS Database](#whois-database)
5. [DNSDumpster](#dnsdumpster)
6. [Google DNS / DNS over HTTPS](#dnsgoogle-dnsgooglecom)
7. [Google Dorking](#google-dorking)
8. [traceroute](#traceroute)
9. [Maltego](#maltego)
10. [OSINT Framework](#osint-framework)
11. [theHarvester](#theharvester)
12. [Robtex](#robtex)
13. [Shodan](#shodan)
14. [WhatWeb](#whatweb)
15. [Sublist3r](#sublist3r)
16. [Pentesting-Tools (pentest-tools.com)](#pentesting-tools-httpspentest-toolscom)
17. [VirusTotal](#virustotal)
18. [netdiscover](#netdiscover)
19. [Nirsoft (nirsoft.net)](#nirsoft-nirsoftnet)
20. [Reference Links](#reference-links)

## Tools Learned

### Internet Archive (archive.org)
**What it is:** Digital archive of websites and files  
**Key Feature:** Wayback Machine - view old versions of websites

**Why useful for recon:**
- Find old contact info, emails, employee details
- See removed content or directories  
- Track website changes over time

**Quick use:**
1. Go to `web.archive.org`
2. Enter target domain
3. Browse historical snapshots
4. Look for sensitive info in old versions

### wget
**What it is:** Command-line tool for downloading files and websites  
**Key Feature:** Can mirror entire websites locally

**Why useful for recon:**
- Download complete website copies for offline analysis
- Gather all files from a target domain
- Available on Kali Linux and most Linux distros

**Quick use:**
```bash
wget -r -p -k -np http://target-website.com
```

### HTTrack
**What it is:** Website copier with GUI interface  
**Key Feature:** User-friendly with many configuration options

**Why useful for recon:**
- Beginner-friendly alternative to wget
- More options and filters for selective downloading
- Good for exploring website structure

**Quick use:**
1. Launch HTTrack from Kali menu
2. Create new project
3. Enter target URL
4. Configure download options
5. Start mirroring

### WHOIS Database
**What it is:** Database containing domain registration information  
**Key Feature:** Shows domain owner details, registration dates, DNS info

**Why useful for recon:**
- Find domain owner contact information
- Check registration and expiry dates
- Identify DNS servers and registrar
- ICANN is the most famous WHOIS database

**Quick use:**
```bash
whois target-domain.com
```
### DNSDumpster
**What it is:** Passive DNS / asset discovery service (dnsdumpster.com)

**Key Feature:** Aggregates publicly available DNS records and visualizes subdomains, hosts and their relationships.

**Why useful for recon:**
- Quickly discover public subdomains and their IP addresses.
- Find mail servers (MX), name servers (NS), and TXT records (SPF/DKIM hints).
- Produce a simple asset map to spot leftover or exposed hosts.

**Quick use:**
1. Open https://dnsdumpster.com
2. Enter the target domain and run the search
3. Review the table of records and the generated network map

**Quick commands / alternatives:**
- `dig +short A example.com` — list A records
- `dig +short MX example.com` — list MX records
- Tools: `amass`, `subfinder`, `assetfinder` for broader subdomain discovery

**Caveats:** Passive/public data only — verify findings, follow rules of engagement and local law, and be aware results may be stale or incomplete.

### DNS.Google (dns.google.com)
**What it is:** Google Public DNS web UI and DNS-over-HTTPS API  
**Key Feature:** Reliable resolver with JSON output (DoH API)

**Why useful for recon:**
- Verify DNS records from an external, well-known resolver
- Bypass local DNS cache/filtering to see public truth
- Query all common record types (A, AAAA, MX, NS, TXT, CNAME)

**Quick use:**
- Web: open https://dns.google.com and query a domain/record type
```bash
# From terminal
dig @8.8.8.8 example.com A
curl -s -H "accept: application/dns-json" \
	"https://dns.google/resolve?name=example.com&type=TXT"
```

**Alternatives:** Cloudflare (1.1.1.1), Quad9 (9.9.9.9), standard `dig` / `nslookup`

### Google Dorking
**What it is:** Advanced search technique using Google's search operators to find specific information indexed by Google  
**Key Feature:** Uses special query syntax to filter and target search results for reconnaissance

**Why useful for recon:**
- Discover sensitive files, directories, and information exposed on websites
- Find login pages, admin panels, and configuration files
- Identify vulnerable systems and outdated software versions
- Gather email addresses, usernames, and contact information
- Locate subdomains and related infrastructure

**Quick use:**
1. Go to google.com
2. Use dorks like: `site:example.com filetype:pdf` or `inurl:admin`
3. Combine operators: `site:example.com intitle:"index of" inurl:backup`

**Google Dork operators:**
- `site:` - Limit search to a specific site or domain
- `filetype:` or `ext:` - Search for specific file extensions (pdf, doc, xls, sql, etc.)
- `inurl:` - Search for URLs containing specific words
- `allinurl:` - All specified terms must appear in the URL
- `intitle:` - Search for pages with terms in the title
- `allintitle:` - All specified terms must appear in the title
- `intext:` - Search within the body text of pages
- `allintext:` - All specified terms must appear in the body text
- `inanchor:` - Search for pages linked with specific anchor text
- `cache:` - View Google's cached version of a page
- `link:` - Find pages that link to a specific URL
- `related:` - Find websites related to a given URL
- `info:` - Get information about a specific URL
- `numrange:` - Search within a numerical range (e.g., numrange:1-100)
- `daterange:` - Search within a date range (use Julian dates)
- `before:` - Results published before a specific date
- `after:` - Results published after a specific date
- `location:` - Search for location-based results
- `source:` - Search within specific news sources
- `OR` - Logical OR operator
- `AND` - Logical AND operator (implied)
- `NOT` or `-` - Exclude terms from search
- `~` - Include synonyms of a word
- `*` - Wildcard for unknown terms
- `..` - Number range (e.g., 1..10)
- `define:` - Get definitions of terms
- `weather:` - Get weather information
- `stocks:` - Get stock quotes

**Popular dorks for recon:**
```bash
# Find login pages
site:example.com inurl:login
# Find admin panels
site:example.com inurl:admin
# Find backup files
site:example.com filetype:sql | filetype:backup | filetype:bak
# Find exposed directories
site:example.com intitle:"index of"
# Find email addresses
"@example.com" -site:example.com
# Find subdomains
site:*.example.com -www
```

**Tools to automate:** Google Dorking scripts, or use with tools like theHarvester, but primarily manual

**Alternatives:** Bing dorks, DuckDuckGo advanced search, specialized search engines

**Caveats:** Google may block automated queries; respect robots.txt and terms of service; results depend on what's indexed; some information may be outdated

### traceroute
**What it is:** Network path tracing tool  
**Key Feature:** Shows intermediate hops/routers and round-trip times

**Why useful for recon:**
- Map network paths, ISPs/AS boundaries, and potential choke points
- Reveal filtering or asymmetric routing along the path

**Quick use:**
```bash
# Linux/Kali
traceroute target-domain.com

# Windows
tracert target-domain.com

# Use ICMP instead of UDP (can behave differently through filters)
traceroute -I target-domain.com
```

**What you'll see:** hop number, hostname/IP (if resolvable), and RTTs; `* * *` means no reply

**Caveats:** Firewalls/rate limits can hide hops; geo-inference is approximate

### Maltego
**What it is:** Graph-based OSINT and link analysis tool  
**Key Feature:** "Transforms" to pivot across entities (domains, emails, IPs, people)

**Why useful for recon:**
- Correlate data from multiple sources into a single visual graph
- Quickly discover relationships between infrastructure and personas

**Quick use:**
1. Install/launch Maltego (Community Edition available)
2. Create a new graph; seed with a domain/email/IP
3. Run transforms (DNS, WHOIS, social, Shodan, etc.)
4. Export the graph or screenshot for reporting

**Alternatives:** SpiderFoot, Recon-ng

### OSINT Framework
**What it is:** Categorized collection of free OSINT tools and resources (osintframework.com)  
**Key Feature:** Interactive tree structure organizing tools by target type (username, email, domain, IP, social media)

**Why useful for recon:**
- Quick reference to find specialized OSINT tools for specific tasks
- All resources are free and publicly available
- Categories include: Username search, Email verification, DNS/Domain tools, IP geolocation, Social media, Images/Videos, Documents, Phone numbers

**Quick use:**
1. Visit https://osintframework.com
2. Click category matching your target type
3. Expand nodes to see specific tools
4. Click tool names to access directly

**Example tools from framework:**
```bash
# Username search
sherlock username

# Email harvesting
theHarvester -d example.com -b all

# Subdomain enumeration
sublist3r -d example.com
```

**Alternatives:** IntelTechniques, Aware-Online, Bellingcat toolkit

**Caveats:** Tool availability changes; some have rate limits or require registration; always respect ToS and legal boundaries

### theHarvester
**What it is:** OSINT gathering tool for email, subdomain, and host enumeration  
**Key Feature:** Aggregates data from multiple public sources (search engines, PGP servers, Shodan, etc.)

**Why useful for recon:**
- Discover email addresses associated with a domain
- Find subdomains and hosts
- Identify IPs, URLs, and ASN information
- Gather data from 30+ different sources in one tool
- Pre-installed on Kali Linux

**Quick use:**
```bash
# Basic search
theHarvester -d example.com -b all

# Limit results and save output
theHarvester -d example.com -b bing -l 200 -f output.html

# Search with multiple sources
theHarvester -d example.com -b google,bing,yahoo
```

**Popular data sources (-b flag):**
- `google` - Google search
- `bing` - Bing search
- `linkedin` - LinkedIn profiles
- `twitter` - Twitter mentions
- `shodan` - Shodan database (requires API key)
- `dnsdumpster` - DNS records
- `virustotal` - VirusTotal (requires API key)
- `certspotter` - Certificate transparency logs
- `all` - Query all available sources

**Common flags:** `-d` domain, `-b` sources, `-l` limit, `-f` file output, `-n` DNS resolution
- `-c` perform DNS brute force

**What you can find:**
- Employee email addresses
- Subdomains and virtual hosts
- Open ports and services (via Shodan)
- IP addresses and network ranges
- Names and job titles from social media

**Alternatives:** Recon-ng, SpiderFoot, Amass

**Caveats:** Some sources require API keys; results quality varies by source; rate limits apply; always respect ToS and legal boundaries

### Robtex
**What it is:** Free network intelligence service (robtex.com)  
**Key Feature:** Maps relationships between IP addresses, domain names, and network infrastructure

**Why useful for recon:**
- Discover domains hosted on the same IP (shared hosting)
- Find historical DNS records and IP changes
- Identify ASN (Autonomous System Number) and network ownership
- Map routing paths and network topology
- Reverse DNS and forward DNS lookups

**Quick use:**
1. Visit https://www.robtex.com
2. Enter IP address or domain name
3. View network graph and relationships
4. Explore shared IPs, DNS history, and ASN details

**Key features:**
```bash
# View IP details: AS number, owner, geolocation
# Check domain DNS records: A, AAAA, MX, NS, TXT
# Find all domains on same IP (virtual hosting)
# Track DNS history and changes over time
# Explore BGP routing information
```

**What you can find:**
- **Shared Hosting:** Other domains on same IP
- **DNS Records:** Complete DNS profile of target
- **Network Owner:** AS number and organization
- **Historical Data:** Past IP addresses for domain
- **Mail Servers:** MX records and mail infrastructure

**Alternatives:** SecurityTrails, ViewDNS.info, HackerTarget

**Caveats:** Public data only; historical records may be limited on free tier; some features require account

### Shodan
**What it is:** Search engine for internet-connected devices/services  
**Key Feature:** Indexed service banners with powerful filters

**Why useful for recon:**
- Find exposed services by product/version, port, org, ASN, country
- Identify vulnerable or misconfigured hosts and tech stacks

**Quick use:**
- Web: https://www.shodan.io
```bash
# Example queries (web/CLI syntax)
http.title:"Apache2 Ubuntu Default Page" country:IN
ssl.cert.subject.cn:"example.com"
port:22 "OpenSSH"
```

**Caveats:** Public-facing data only; respect ToS and legal scope; rate limits apply

### WhatWeb
**What it is:** Website fingerprinting tool with 1800+ plugins  
**Key Feature:** Detects technologies (CMS, frameworks, web servers, WAFs, analytics, CDNs)

**Why useful for recon:**
- Quickly identify stack: server, language, CMS, plugins, and security products
- Guide next steps (version checks, default paths, vuln research)

**Quick use:**
```bash
# Basic scan
whatweb -v example.com

# Increase aggression (1=passive, 4=heavy) and be verbose
whatweb -a 3 -v example.com

# Input list, custom User-Agent, JSON output
whatweb -i targets.txt -U "Mozilla/5.0" --log-json=out.json
```

**Useful flags:** `-a` aggression (1-4), `-v` verbose, `-i` input file, `-U` user-agent, `--log-json`, `--log-xml`, `--proxy` host:port

**Alternatives:** Wappalyzer, BuiltWith, Nmap HTTP NSE scripts (e.g., `http-server-header`, `http-title`)

**Caveats:** Signature-based; can be noisy at higher `-a` levels and trigger WAFs — stay within scope and rules of engagement

### Sublist3r
**What it is:** Fast and automated subdomain enumeration tool  
**Key Feature:** Aggregates results from 9+ DNS sources to discover subdomains

**Why useful for recon:**
- Discover all subdomains of a target domain
- Uses OSINT and passive DNS sources (no direct traffic to target)
- Pre-installed on Kali Linux
- Lightweight and quick to execute
- Returns valid subdomains with IP addresses

**Quick use:**
```bash
# Basic subdomain enumeration
sublist3r -d example.com

# Enable DNS brute force for additional subdomains
sublist3r -d example.com -b

# Verbose output and save to file
sublist3r -d example.com -o subdomains.txt -v

# No output to console (quiet mode)
sublist3r -d example.com -o subdomains.txt -q

# Increase thread count for faster enumeration
sublist3r -d example.com -t 100
```

**Data sources:** Google, Yahoo, Bing, DNSDumpster, VirusTotal, etc.

**Common flags:**
- `-d` domain to search
- `-b` enable DNS brute force (slower but finds more)
- `-o` output file path
- `-v` verbose output
- `-q` quiet mode
- `-t` number of threads (default 16)

**What you can find:**
- All public subdomains of target domain
- IP addresses hosting those subdomains
- Potential attack surface (e.g., dev.example.com, admin.example.com)
- Related infrastructure and services

**Alternatives:** Amass, Subfinder, Assetfinder, DNSRecon

**Caveats:** DNS brute force can be slow and noisy; results depend on public DNS records; always ensure you have permission before enumerating

### Pentesting-Tools (https://pentest-tools.com/)
**What it is:** A commercial web-based platform offering a suite of reconnaissance and vulnerability scanning tools (pentest-tools.com).

**Key Features:**
- Consolidated scanners for subdomains, ports, web vulnerabilities (XSS, SQLi), and network services
- Pre-built checks, proof-of-concept generation, and exportable reports (PDF/HTML)
- Team features and API access for automation (subscription required)

**Why useful for recon/pentesting:**
- Fast, centralized UI to run many reconnaissance and quick-vulnerability checks without installing multiple local tools
- Useful for rapid triage, reporting, and client demos
- Integrates multiple data sources which can speed up early-phase discovery

**Quick use:**
1. Visit https://pentest-tools.com and choose the relevant module (e.g., domain scanner, web scanner, port scan).
2. Enter target domain or IP and adjust scan profile (passive/active, depth, authentication if allowed).
3. Review findings, validate high-confidence results manually, and export the report.

**Alternatives:** Intruder, Detectify, Qualys (enterprise), Open-source options: OWASP ZAP, Nmap, Nikto, Burp Suite (community/pro).

**Caveats:** Paid service with active scanning that can be intrusive — always obtain explicit permission and follow rules of engagement; verify scanner findings manually to avoid false positives.

### VirusTotal
**What it is:** Online service that aggregates antivirus, URL, domain and file scan results and enrichment data (virustotal.com).

**Key Features:**
- File and URL scanning across many AV engines
- Public search for domains, IPs, URLs, and files
- Passive DNS, SSL certificate data, and related-file/domain graphs
- Public API and `vt` CLI for automation (API key required)

**Why useful for recon/analysis:**
- Quickly check whether a file, URL, or domain is known-malicious
- Find related IoCs (domains, IPs, samples) via relationships and passive DNS
- Aggregate community detections and metadata to prioritise follow-up

**Quick use:**
1. Web: visit https://www.virustotal.com, paste a URL or upload a file, or search a domain/IP.
2. CLI/API (requires API key):
```bash
curl -s -H "x-apikey: $VT_API_KEY" \
	"https://www.virustotal.com/api/v3/domains/example.com"
```
3. Use the `vt` CLI for downloads and quick lookups: `vt file scan <file>` or `vt domain report example.com`.

**Caveats:**
- Uploading files may expose sensitive data to a public service — avoid uploading private, confidential, or regulated data.
- API access is rate-limited and may require a paid plan for higher volumes.
- A detection on VirusTotal is a signal, not definitive proof — validate with local analysis.

### netdiscover
**What it is:** ARP-based network discovery tool for local networks (often included in Kali). It finds live hosts using ARP requests and passive sniffing.

**Key Features:**
- Fast ARP scans of local subnets
- Passive mode to observe traffic without sending probes
- Shows IP, MAC, and vendor (OUI) to help identify device types

**Why useful for recon:**
- Quickly build an inventory of live hosts on a LAN before deeper scanning
- Identify devices by MAC vendor (IoT, routers, printers)
- Useful in internal assessments and lab environments to map reachable hosts

**Quick use:**
```bash
# Active scan of a /24 network (requires root)
sudo netdiscover -r 192.168.1.0/24

# Specify interface
sudo netdiscover -i eth0 -r 10.0.0.0/24

# Passive mode (listen only)
sudo netdiscover -p -i wlan0
```

**Caveats:**
- Only works on the same layer-2 network (LAN) — not for Internet-wide discovery
- ARP probing can trigger IDS/filters on careful networks; obtain permission
- Requires root privileges for active scans

### Nirsoft (nirsoft.net)
**What it is:** Website by Nir Sofer providing a collection of free Windows utilities for system administration, security analysis, and information gathering. Many tools are portable and don't require installation.

**Key Feature:** Specialized IP and network analysis tools that provide detailed geolocation and assignment information without requiring online lookups for some functions.

**Why useful for recon:**
- Obtain comprehensive IP address details including country, region, city, ISP, and organization
- Analyze IP ranges and network assignments by country
- Perform offline geolocation lookups using built-in databases
- Useful for mapping network infrastructure and identifying geographic distribution of assets
- Tools are lightweight and can be run from USB drives for field work

**Quick use:**
1. Visit https://www.nirsoft.net/ and download relevant IP tools
2. For IP information: Run IPNetInfo.exe or IPInfoOffline.exe
3. Enter target IP address or range
4. View detailed location, network, and assignment data

**Popular IP-related tools:**
- **IPNetInfo:** Displays IP address information including country, ISP, and network details
- **IPInfoOffline:** Offline IP geolocation tool with detailed mapping
- **CountryTraceRoute:** Enhanced traceroute showing country flags and location info for each hop
- **IPCountryTracer:** Maps IP addresses to countries with visual representation

**What you can find:**
- Geographic location (country, region, city)
- ISP and organization information
- Network range assignments
- Autonomous System Numbers (ASN)
- Contact information for network owners

**Alternatives:** MaxMind GeoIP, IP2Location, WhatIsMyIP services

**Caveats:** Primarily Windows-based tools; some features require internet for real-time data; respect privacy laws when analyzing IP information

## Reference Links

- [Internet Archive / Wayback Machine](https://web.archive.org)
- [wget manual](https://www.gnu.org/software/wget/manual/)
- [HTTrack](https://www.httrack.com/)
- [ICANN WHOIS](https://whois.icann.org/)
- [DNSDumpster](https://dnsdumpster.com)
- [Google DNS / DNS-over-HTTPS](https://dns.google.com)
- [traceroute man page](https://linux.die.net/man/8/traceroute)
- [Netdiscover (Kali Tools)](https://tools.kali.org/information-gathering/netdiscover)
- [Maltego](https://www.maltego.com/)
- [OSINT Framework](https://osintframework.com/)
- [theHarvester (GitHub)](https://github.com/laramies/theHarvester)
- [Robtex](https://www.robtex.com/)
- [Shodan](https://www.shodan.io/)
- [WhatWeb (GitHub)](https://github.com/urbanadventurer/WhatWeb)
- [Sublist3r (GitHub)](https://github.com/aboul3la/Sublist3r)
- [Pentest-Tools](https://pentest-tools.com)
- [VirusTotal](https://www.virustotal.com/)
- [Nirsoft](https://www.nirsoft.net/)
- [Google Hacking Database](https://www.exploit-db.com/google-hacking-database)

[⬆ Back to top](#-footprinting--reconnaissance-notes)
