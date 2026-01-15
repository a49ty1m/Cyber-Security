# 🔍 Footprinting & Reconnaissance Notes

## 📑 Table of Contents
1. [Internet Archive](#internet-archive-archiveorg)
2. [wget](#wget)
3. [HTTrack](#httrack)
4. [WHOIS Database](#whois-database)
5. [DNSDumpster](#dnsdumpster)
6. [DNS.Google](#dnsgoogle-dnsgooglecom)
7. [traceroute](#traceroute)
8. [Maltego](#maltego)
9. [OSINT Framework](#osint-framework)
10. [theHarvester](#theharvester)
11. [Robtex](#robtex)
12. [Shodan](#shodan)
13. [WhatWeb](#whatweb)
14. [Sublist3r](#sublist3r)
15. [Reference Links](#reference-links)

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
# Basic search across all sources
theHarvester -d example.com -b all

# Search specific source (Google)
theHarvester -d example.com -b google

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

**Common flags:**
- `-d` domain to search
- `-b` data source(s)
- `-l` limit number of results
- `-f` save results to file (HTML/XML/JSON)
- `-n` perform DNS resolution
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
# Basic fingerprint
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

**Data sources used:**
- Google, Yahoo, Bing
- DNSDumpster, Baidu
- Netcraft, VirusTotal
- ThreatCrowd, AnubisDB
- PassiveDNS

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

## Reference Links
- [Internet Archive](https://archive.org)
- [Wayback Machine](https://web.archive.org)
- [wget Manual](https://www.gnu.org/software/wget/manual/)
- [HTTrack](https://www.httrack.com/)
- [ICANN WHOIS](https://whois.icann.org/)
- [DNSDumpster](https://dnsdumpster.com)
- [DNS.Google](https://dns.google.com)
- [Google Public DNS](https://developers.google.com/speed/public-dns)
- [traceroute man page](https://linux.die.net/man/8/traceroute)
- [Maltego](https://www.maltego.com/)
- [SpiderFoot](https://www.spiderfoot.net/)
- [OSINT Framework](https://osintframework.com/)
- [IntelTechniques](https://inteltechniques.com/tools/)
- [Bellingcat Toolkit](https://bit.ly/bcattools)
- [theHarvester (GitHub)](https://github.com/laramies/theHarvester)
- [Robtex](https://www.robtex.com/)
- [Shodan](https://www.shodan.io/)
- [Shodan-Dorks]()
- [WhatWeb (GitHub)](https://github.com/urbanadventurer/WhatWeb)
- [Sublist3r (GitHub)](https://github.com/aboul3la/Sublist3r)
- [Sublist3r Documentation](https://github.com/aboul3la/Sublist3r#sublist3r)

[⬆ Back to top](#-footprinting--reconnaissance-notes)

