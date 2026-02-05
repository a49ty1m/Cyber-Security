# checking live system
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