# Scanning live system
## Ping Command

### What is Ping?
Ping is a network utility command that tests the reachability of a host on an IP network. It sends ICMP (Internet Control Message Protocol) echo request packets to a target host and waits for responses, measuring the round-trip time.

### Purpose
- **Check connectivity**: Determine if a host is reachable and connected to the internet
- **Measure latency**: Find the response time (RTT - Round Trip Time) between your computer and the target
- **Verify network connectivity**: Troubleshoot network issues and identify unreachable hosts
- **Reconnaissance**: During security assessments, ping can help identify live hosts on a network

### Basic Syntax
```bash
ping [options] <hostname or IP address>
```

### Common Usage Examples
```bash
ping google.com                 # Ping a domain
ping 8.8.8.8                   # Ping an IP address
ping -c 4 192.168.1.1          # Send 4 packets (Linux/Mac)
ping -n 4 192.168.1.1          # Send 4 packets (Windows)
ping -i 2 192.168.1.1          # Set interval of 2 seconds between packets
```

### Common Options
| Option | Description |
|--------|------------|
| `-c count` | Number of packets to send (Linux/Mac) |
| `-n count` | Number of packets to send (Windows) |
| `-i interval` | Wait interval between packets (in seconds) |
| `-W timeout` | Timeout in milliseconds for each reply |
| `-t` | Continuous ping until stopped (Windows) |
| `-s size` | Packet size in bytes |

### Interpreting Ping Output
```
64 bytes from 8.8.8.8: icmp_seq=1 ttl=119 time=20.5ms
```
- **bytes**: Size of the echo reply packet
- **icmp_seq**: Sequence number of the packet
- **ttl**: Time To Live (hops remaining)
- **time**: Round-trip time in milliseconds

### Important Notes
- Ping uses ICMP protocol, which can be blocked by firewalls
- A successful ping response means the host is reachable
- Timeouts indicate the host is unreachable or blocking ICMP
- In pentesting, ping sweeps can help discover live hosts on a network

## Angry IP Scanner

### What is Angry IP Scanner?
Angry IP Scanner (also known as ipscan) is a fast, open-source, cross-platform network scanner designed to scan IP addresses and ports. It's widely used by network administrators and security professionals for network discovery and reconnaissance.

### Key Features
- **Fast and lightweight**: Uses multi-threaded approach for rapid scanning
- **Cross-platform**: Available for Windows, Linux, and macOS
- **Port scanning**: Can scan specific ports or port ranges
- **Host discovery**: Identifies live hosts on a network
- **Hostname resolution**: Resolves IP addresses to hostnames
- **NetBIOS information**: Retrieves NetBIOS computer names
- **MAC address detection**: Shows MAC addresses of devices
- **Exportable results**: Export scan results to CSV, TXT, XML formats
- **Plugin support**: Extendable with Java-based plugins

### Installation
```bash
# Linux (Debian/Ubuntu)
sudo apt install ipscan

# Download from official website
# https://angryip.org/download/

# Run on Linux (if downloaded .jar)
java -jar ipscan-x.x.x.jar
```

### Basic Usage
1. **Specify IP range**: Enter the start and end IP addresses
2. **Choose scanning options**: Select what information to gather
3. **Start scan**: Click "Start" button to begin scanning
4. **View results**: Live hosts and their information will appear in the results pane

### Common Scan Options
| Option | Description |
|--------|------------|
| IP Range | Define start and end IP addresses to scan |
| Hostname | Enable/disable hostname resolution |
| Ports | Specify which ports to scan |
| Pinger | Choose ping method (ICMP, TCP, UDP) |
| Fetchers | Select additional information to retrieve |
| Threads | Number of concurrent threads (affects speed) |

### Use Cases
- **Network inventory**: Discover all devices on a network
- **Security auditing**: Identify unauthorized devices
- **Troubleshooting**: Locate network connectivity issues
- **Port analysis**: Check which ports are open on hosts
- **IP address management**: Track IP address usage

### Advantages
- Free and open-source
- No installation required (portable version available)
- Simple and intuitive GUI
- Fast scanning with multi-threading
- Minimal resource consumption
- Customizable scanning options

### Limitations
- Basic port scanning capabilities (not as advanced as Nmap)
- May be detected by intrusion detection systems
- Requires Java Runtime Environment (JRE)
- Limited vulnerability assessment features

### Important Notes for Pentesting
- Always have authorization before scanning networks
- Aggressive scanning may trigger security alerts
- Can be used for initial network reconnaissance
- Results should be verified with more advanced tools
- Useful for quickly identifying live hosts before deeper enumeration

# Nmap
## What is Nmap?
Nmap (Network Mapper) is a free, open-source network scanning tool used for network discovery, security auditing, and vulnerability scanning. It's one of the most popular and powerful tools in cybersecurity for discovering hosts, services, operating systems, and potential vulnerabilities on a network.

### Key Features
- **Host discovery**: Identify live hosts on a network
- **Port scanning**: Detect open, closed, and filtered ports
- **Service detection**: Determine service names and versions
- **OS detection**: Fingerprint operating systems
- **Scriptable interaction**: NSE (Nmap Scripting Engine) for advanced tasks
- **Flexible targeting**: Scan single hosts, ranges, or entire subnets
- **Output formats**: Multiple output formats (normal, XML, grepable)
- **Stealth capabilities**: Various techniques to evade detection
- **IPv6 support**: Full support for IPv6 scanning

### Installation
```bash
# Linux (Debian/Ubuntu)
sudo apt update
sudo apt install nmap

# Linux (RHEL/CentOS/Fedora)
sudo yum install nmap

# macOS
brew install nmap

# Verify installation
nmap --version
```

### Basic Syntax
```bash
nmap [Scan Type] [Options] {target specification}
```

## Common Scan Types

### 1. TCP Connect Scan (-sT)
```bash
nmap -sT 192.168.1.1
```
- Completes full TCP three-way handshake
- Most reliable but easily detected
- Default scan when run without root privileges
- Slower than SYN scan

### 2. SYN Scan (-sS)
```bash
sudo nmap -sS 192.168.1.1
```
- Half-open scan (doesn't complete TCP handshake)
- Stealthier than TCP connect scan
- Requires root/administrator privileges
- Default scan when run with privileges
- Fast and efficient

### 3. UDP Scan (-sU)
```bash
sudo nmap -sU 192.168.1.1
```
- Scans UDP ports (DNS, DHCP, SNMP, etc.)
- Slower than TCP scans
- Often overlooked but important
- Requires root privileges

### 4. Comprehensive Scan (-sC -sV)
```bash
nmap -sC -sV 192.168.1.1
```
- `-sC`: Run default NSE scripts
- `-sV`: Detect service versions
- Provides detailed information about services

### 5. Aggressive Scan (-A)
```bash
nmap -A 192.168.1.1
```
- Enables OS detection, version detection, script scanning, and traceroute
- Comprehensive but noisy (easily detected)
- Combines multiple scan types

## Target Specification

### Single Hosts
```bash
nmap 192.168.1.1              # Single IP
nmap scanme.nmap.org          # Single hostname
```

### Multiple Hosts
```bash
nmap 192.168.1.1 192.168.1.5  # Multiple IPs
nmap 192.168.1.1-20           # IP range
nmap 192.168.1.0/24           # Subnet (CIDR notation)
nmap 192.168.1.*              # Wildcard
```

### Input from File
```bash
nmap -iL targets.txt          # Read targets from file
```

### Exclude Targets
```bash
nmap 192.168.1.0/24 --exclude 192.168.1.1
nmap 192.168.1.0/24 --excludefile exclude.txt
```

## Port Specification

```bash
nmap -p 22 192.168.1.1              # Single port
nmap -p 22,80,443 192.168.1.1       # Multiple ports
nmap -p 1-1000 192.168.1.1          # Port range
nmap -p- 192.168.1.1                # All 65535 ports
nmap -p http,https 192.168.1.1      # Port by service name
nmap --top-ports 100 192.168.1.1    # Top 100 most common ports
nmap -F 192.168.1.1                 # Fast scan (100 most common ports)
```

## Timing and Performance

```bash
nmap -T0 192.168.1.1    # Paranoid (slowest, stealthiest)
nmap -T1 192.168.1.1    # Sneaky
nmap -T2 192.168.1.1    # Polite
nmap -T3 192.168.1.1    # Normal (default)
nmap -T4 192.168.1.1    # Aggressive (faster)
nmap -T5 192.168.1.1    # Insane (fastest, least accurate)
```

### Custom Timing
```bash
nmap --max-retries 2 192.168.1.1        # Limit retries
nmap --host-timeout 30m 192.168.1.1     # Host timeout
nmap --min-rate 100 192.168.1.1         # Minimum packets/second
nmap --max-rate 1000 192.168.1.1        # Maximum packets/second
```

## Service and OS Detection

```bash
# Service version detection
nmap -sV 192.168.1.1                    # Standard intensity
nmap -sV --version-intensity 9 192.168.1.1  # Maximum intensity (0-9)
nmap -sV --version-light 192.168.1.1    # Light mode (intensity 2)
nmap -sV --version-all 192.168.1.1      # Try all probes

# OS detection
nmap -O 192.168.1.1                     # Enable OS detection
nmap -O --osscan-guess 192.168.1.1      # Aggressive OS guessing
nmap -O --osscan-limit 192.168.1.1      # Limit to promising targets
```

## Nmap Scripting Engine (NSE)

### Script Categories
- **auth**: Authentication related scripts
- **broadcast**: Network broadcast discovery
- **brute**: Brute force attacks
- **default**: Default safe scripts (-sC)
- **discovery**: Network/service discovery
- **dos**: Denial of Service detection
- **exploit**: Exploitation scripts
- **external**: Scripts using external resources
- **fuzzer**: Fuzzing scripts
- **intrusive**: Scripts that may crash systems
- **malware**: Malware detection
- **safe**: Scripts unlikely to cause issues
- **version**: Version detection enhancement
- **vuln**: Vulnerability detection

### Using NSE Scripts
```bash
# Run default scripts
nmap -sC 192.168.1.1

# Run specific script
nmap --script=http-title 192.168.1.1

# Run multiple scripts
nmap --script=http-title,http-headers 192.168.1.1

# Run script category
nmap --script=vuln 192.168.1.1

# Run all scripts in multiple categories
nmap --script=vuln,exploit 192.168.1.1

# Get script help
nmap --script-help=http-title

# Update script database
nmap --script-updatedb
```

### Useful NSE Scripts
```bash
# Vulnerability scanning
nmap --script=vuln 192.168.1.1

# HTTP enumeration
nmap --script=http-enum 192.168.1.1

# SMB enumeration
nmap --script=smb-enum-shares,smb-enum-users 192.168.1.1

# SSL/TLS analysis
nmap --script=ssl-cert,ssl-enum-ciphers 192.168.1.1

# FTP anonymous login check
nmap --script=ftp-anon 192.168.1.1

# SQL injection check
nmap --script=http-sql-injection 192.168.1.1
```

## Firewall/IDS Evasion

```bash
# Fragment packets
nmap -f 192.168.1.1

# Specify MTU
nmap --mtu 24 192.168.1.1

# Decoy scan (hide among decoys)
nmap -D RND:10 192.168.1.1
nmap -D decoy1,decoy2,ME,decoy3 192.168.1.1

# Spoof source IP
nmap -S 192.168.1.5 192.168.1.1

# Spoof source port
nmap --source-port 53 192.168.1.1

# Randomize target order
nmap --randomize-hosts 192.168.1.0/24

# Add random data
nmap --data-length 25 192.168.1.1

# Idle scan (zombie scan)
nmap -sI zombie_host target_host
```

## Output Options

```bash
# Normal output (default)
nmap -oN output.txt 192.168.1.1

# XML output
nmap -oX output.xml 192.168.1.1

# Grepable output
nmap -oG output.gnmap 192.168.1.1

# All formats
nmap -oA scan_results 192.168.1.1

# Verbose output
nmap -v 192.168.1.1
nmap -vv 192.168.1.1  # Even more verbose

# Debug output
nmap -d 192.168.1.1
nmap -dd 192.168.1.1  # More debug info
```

## Host Discovery Options

```bash
# Ping scan only (no port scan)
nmap -sn 192.168.1.0/24

# TCP SYN ping
nmap -PS22,80,443 192.168.1.0/24

# TCP ACK ping
nmap -PA22,80,443 192.168.1.0/24

# UDP ping
nmap -PU53,161 192.168.1.0/24

# ICMP ping types
nmap -PE 192.168.1.0/24  # ICMP echo
nmap -PP 192.168.1.0/24  # Timestamp
nmap -PM 192.168.1.0/24  # Netmask

# Skip host discovery (treat all as online)
nmap -Pn 192.168.1.1

# ARP ping (local network)
nmap -PR 192.168.1.0/24
```

## Practical Examples

### 1. Quick Network Sweep
```bash
nmap -sn 192.168.1.0/24
```
Discover all live hosts on the network without port scanning.

### 2. Basic Port Scan
```bash
nmap 192.168.1.100
```
Scan most common 1000 ports on a single host.

### 3. Comprehensive Service Scan
```bash
nmap -sV -sC -p- -T4 192.168.1.100
```
Scan all ports, detect services, run default scripts, aggressive timing.

### 4. Stealth Scan
```bash
sudo nmap -sS -T2 -f 192.168.1.100
```
SYN scan with polite timing and packet fragmentation.

### 5. Vulnerability Assessment
```bash
nmap -sV --script=vuln 192.168.1.100
```
Detect services and run vulnerability detection scripts.

### 6. Web Server Enumeration
```bash
nmap -p 80,443 --script=http-enum,http-headers,http-methods 192.168.1.100
```
Enumerate web server information and directories.

### 7. Network Inventory
```bash
nmap -sP -PE -PA21,23,80,3389 192.168.1.0/24 -oA network_inventory
```
Discover hosts and save results in all formats.

### 8. Full Security Audit
```bash
sudo nmap -sS -sV -sC -O -A -p- -T4 --script=vuln -oA full_audit 192.168.1.100
```
Comprehensive scan with OS detection, service detection, vulnerability scanning.

## Port States

Nmap classifies ports into six states:

| State | Description |
|-------|-------------|
| **open** | Application is accepting connections on this port |
| **closed** | Port is accessible but no application is listening |
| **filtered** | Firewall or filter is blocking/dropping packets |
| **unfiltered** | Port is accessible but can't determine if open/closed |
| **open\|filtered** | Can't determine if open or filtered |
| **closed\|filtered** | Can't determine if closed or filtered |

## Best Practices

### Legal and Ethical Considerations
- **Always get authorization** before scanning networks you don't own
- Unauthorized scanning is illegal in many jurisdictions
- Follow responsible disclosure for discovered vulnerabilities
- Document your authorization and scope of testing

### Scanning Tips
1. **Start passive**: Begin with minimal scanning to avoid detection
2. **Incremental approach**: Start with host discovery, then port scan, then deep scanning
3. **Save results**: Always use output options to document findings
4. **Verify results**: Use multiple tools to confirm critical findings
5. **Be mindful of timing**: Aggressive scans can disrupt services or trigger alerts
6. **Target specification carefully**: Use exclude options to avoid unintended targets
7. **Keep updated**: Regularly update Nmap for latest features and NSE scripts
8. **Read the documentation**: Nmap has excellent documentation at nmap.org

### Operational Security
- Use VPN or authorized testing environment
- Monitor your own traffic to understand detection signatures
- Be aware that scans leave logs on target systems
- Time your scans appropriately (with client approval)
- Understand the impact of different scan types

## Useful Combinations

### Quick Discovery Scan
```bash
nmap -sn --top-ports 10 192.168.1.0/24 -oG quick_discovery.txt
```

### Standard Penetration Test Scan
```bash
nmap -sS -sV -sC -O -p- -T4 --script=default,vuln -oA pentest_scan 192.168.1.100
```

### Stealth Reconnaissance
```bash
nmap -sS -T2 -f -D RND:10 --source-port 53 -p 21,22,23,25,80,443 192.168.1.100
```

### Web Application Scan
```bash
nmap -p 80,443,8080,8443 --script=http-* --script-args http.useragent="Mozilla/5.0" 192.168.1.100
```

### Database Server Scan
```bash
nmap -p 1433,3306,5432,27017 --script=*-enum,*-brute 192.168.1.100
```

## Common Errors and Troubleshooting

### "You requested a scan type which requires root privileges"
Solution: Use `sudo` before the command
```bash
sudo nmap -sS 192.168.1.1
```

### "Packet send via eth0 failed. Device is up and not busy"
Solution: Check network connectivity and firewall rules

### Slow Scans
Solutions:
- Increase timing template: `-T4` or `-T5`
- Reduce port range: `-p 1-1000` instead of `-p-`
- Use `--max-retries 1` or `--host-timeout 5m`
- Scan fewer hosts simultaneously

### No Results Returned
Possible causes:
- Target is offline or firewalled
- ICMP is blocked (use `-Pn`)
- Wrong network interface (use `-e eth0`)
- Network connectivity issues

## Additional Resources

- **Official Website**: https://nmap.org
- **Reference Guide**: https://nmap.org/book/man.html
- **NSE Documentation**: https://nmap.org/nsedoc/
- **Nmap Network Scanning Book**: Free online at nmap.org/book/
- **Practice**: Use test sites like scanme.nmap.org (legally)

## Summary

Nmap is an indispensable tool for:
- Network reconnaissance and mapping
- Security auditing and vulnerability assessment
- Network inventory and asset discovery
- Compliance verification
- Penetration testing

Master the basics first (host discovery, port scanning), then progress to advanced features (NSE scripts, evasion techniques). Always scan responsibly and legally.