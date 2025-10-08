# 🔍 Footprinting & Reconnaissance Notes

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
---

## Reference Links
- [Internet Archive](https://archive.org)
- [Wayback Machine](https://web.archive.org)