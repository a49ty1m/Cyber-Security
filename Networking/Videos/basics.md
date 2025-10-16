# Module: Introduction to Networking — Short Notes
*(Notes compiled up to **Packet Switching**)*

> Source: Lecture notes — *Introduction to Networking*. :contentReference[oaicite:0]{index=0}

---

## 1. What is a Computer Network?
- **Definition:** A collection of computing devices connected to communicate and share resources (wired or wireless). :contentReference[oaicite:1]{index=1}
- **Node/Host:** Any device on the network.
- **Data transfer rate:** Speed at which data moves across the network — a key metric. :contentReference[oaicite:2]{index=2}

---

## 2. Client / Server Model
- **Client/Server:** Servers provide resources or services (file servers, web servers); clients request them. Typical model used across networks. :contentReference[oaicite:3]{index=3}

---

## 3. Types of Networks
- **LAN (Local-Area Network):** Small geographical area (e.g., office, campus). Topologies include:
  - **Ring:** Closed loop, messages travel in one direction.
  - **Star:** Central node connects all others.
  - **Bus:** Single communication line carrying messages both directions. :contentReference[oaicite:4]{index=4}
- **MAN (Metropolitan-Area Network):** Large-city area networks. :contentReference[oaicite:5]{index=5}
- **WAN (Wide-Area Network):** Connects LANs over large distances; the Internet is the ultimate WAN. Gateways often serve as inter-LAN connection points. :contentReference[oaicite:6]{index=6}

---

## 4. Internet Connections & Broadband
- **Backbone:** High-speed networks carrying Internet traffic (provided by major carriers).  
- **ISPs:** Provide Internet access to users/organizations.  
- **Common home connection types:** Dial-up modem, DSL, cable modem.  
- **Broadband:** Transfer speeds faster than 128 kbps; asymmetric download/upload speeds are common. :contentReference[oaicite:7]{index=7}

---

## 5. Common Network Devices
- **Hub:** Layer 1 device; floods packets to all ports; increases collision chances. :contentReference[oaicite:8]{index=8}  
- **Repeater:** Regenerates signals to extend reach. :contentReference[oaicite:9]{index=9}  
- **Modem:** Modulator–demodulator; converts digital↔analog for phone lines. :contentReference[oaicite:10]{index=10}  
- **NIC (Network Interface Card):** Layer 1/2 device; provides physical access and MAC addressing. :contentReference[oaicite:11]{index=11}  
- **Switch:** Forwards frames only to destination port using MAC table; reduces collisions. :contentReference[oaicite:12]{index=12}  
- **Bridge:** Data-link layer device; filters/forwards frames between segments using MAC addresses. :contentReference[oaicite:13]{index=13}  
- **Router:** Network-layer device; routes packets between networks using IP addresses; divides broadcast domains. :contentReference[oaicite:14]{index=14}  
- **Gateway:** Protocol converter; can operate at any layer (often used to interconnect differing protocols). :contentReference[oaicite:15]{index=15}  
- **Wireless Access Point (WAP):** Connects wireless devices to wired networks (Wi-Fi, Bluetooth). :contentReference[oaicite:16]{index=16}

---

## 6. Switching (Why we use switching)
- Connecting many devices by individual point-to-point links is inefficient.  
- Switching uses central devices (switches) to interconnect devices efficiently, forming switched networks. :contentReference[oaicite:17]{index=17}

---

## 7. Types of Switching

### 7.1 Message Switching
- **Concept:** Entire message (including destination address) is forwarded from intermediate node to node; each node stores the full message until the next hop is ready — *store-and-forward*. :contentReference[oaicite:18]{index=18}
- **Advantages:**
  - Many devices can share a channel.
  - Congestion reduction is possible.
  - Supports unlimited message lengths. :contentReference[oaicite:19]{index=19}
- **Disadvantages:**
  - Unsuitable for real-time voice/video.
  - Store-and-forward devices are expensive.
  # Introduction to Networking — Short Notes

  These notes compile fundamentals from networking intro lectures, cleaned and structured for quick study.

  ---

  ## Table of Contents

  - [1. What is a Computer Network?](#1-what-is-a-computer-network)
  - [2. Client / Server Model](#2-client--server-model)
  - [3. Types of Networks](#3-types-of-networks)
  - [4. Internet Connections and Broadband](#4-internet-connections-and-broadband)
  - [5. Common Network Devices](#5-common-network-devices)
  - [6. Switching (Motivation)](#6-switching-motivation)
  - [7. Types of Switching](#7-types-of-switching)
    - [7.1 Message Switching](#71-message-switching)
    - [7.2 Circuit Switching](#72-circuit-switching)
    - [7.3 Packet Switching](#73-packet-switching)
  - [8. Transmission Media](#8-transmission-media)
    - [8.1 Twisted Pair Cable](#81-twisted-pair-cable)
    - [8.2 Coaxial Cable](#82-coaxial-cable)
    - [8.3 Fiber Optic Cable](#83-fiber-optic-cable)
    - [8.4 Unguided Media](#84-unguided-media)
  - [9. Open Systems and OSI Reference Model](#9-open-systems-and-osi-reference-model)
    - [9.1 Seven Layers of OSI](#91-seven-layers-of-osi)
  - [10. Communication Architecture](#10-communication-architecture)
  - [11. TCP/IP Model](#11-tcpip-model)
  - [12. Internet Protocol (IP)](#12-internet-protocol-ip)
    - [12.1 IP Datagram](#121-ip-datagram)
  - [13. IPv4 — Key Concepts](#13-ipv4--key-concepts)
  - [14. IPv6 — Next Generation IP](#14-ipv6--next-generation-ip)
    - [14.1 IPv6 Address Types](#141-ipv6-address-types)
    - [14.2 IPv6 Header Fields](#142-ipv6-header-fields)
    - [14.3 IPv6 Advantages](#143-ipv6-advantages)
  - [15. IPv4 vs IPv6 — Comparison](#15-ipv4-vs-ipv6--comparison)
  - [16. MIME Types](#16-mime-types)
  - [17. Firewalls](#17-firewalls)
  - [18. Network Addressing](#18-network-addressing)
  - [19. Domain Name System (DNS)](#19-domain-name-system-dns)
  - [20. Summary — Key Takeaways](#20-summary--key-takeaways)

  ---

  ## 1. What is a Computer Network?

  - Definition: A collection of computing devices connected to communicate and share resources (wired or wireless).
  - Node/Host: Any device on the network.
  - Data transfer rate: Speed at which data moves across the network — a key metric.

  ## 2. Client / Server Model

  - Client/Server: Servers provide resources or services (file servers, web servers); clients request them. This is the typical model used across networks.

  ## 3. Types of Networks

  - LAN (Local-Area Network): Small geographical area (e.g., office, campus). Topologies include:
    - Ring: Closed loop, messages travel in one direction.
    - Star: Central node connects all others.
    - Bus: Single communication line carrying messages both directions.
  - MAN (Metropolitan-Area Network): Large-city area networks.
  - WAN (Wide-Area Network): Connects LANs over large distances; the Internet is the ultimate WAN. Gateways often serve as inter-LAN connection points.

  ## 4. Internet Connections and Broadband

  - Backbone: High-speed networks carrying Internet traffic (provided by major carriers).
  - ISPs: Provide Internet access to users/organizations.
  - Common home connection types: Dial-up modem, DSL, cable modem.
  - Broadband: Transfer speeds faster than 128 kbps; asymmetric download/upload speeds are common.

  ## 5. Common Network Devices

  - Hub: Layer 1 device; floods packets to all ports; increases collision chances.
  - Repeater: Regenerates signals to extend reach.
  - Modem: Modulator–demodulator; converts digital↔analog for phone lines.
  - NIC (Network Interface Card): Layer 1/2 device; provides physical access and MAC addressing.
  - Switch: Forwards frames only to destination port using MAC table; reduces collisions.
  - Bridge: Data-link layer device; filters/forwards frames between segments using MAC addresses.
  - Router: Network-layer device; routes packets between networks using IP addresses; divides broadcast domains.
  - Gateway: Protocol converter; can operate at any layer (often used to interconnect differing protocols).
  - Wireless Access Point (WAP): Connects wireless devices to wired networks (Wi‑Fi, Bluetooth).

  ## 6. Switching (Motivation)

  - Connecting many devices by individual point-to-point links is inefficient.
  - Switching uses central devices (switches) to interconnect devices efficiently, forming switched networks.

  ## 7. Types of Switching

  ### 7.1 Message Switching

  - Concept: Entire message (including destination address) is forwarded from intermediate node to node; each node stores the full message until the next hop is ready — store-and-forward.
  - Advantages:
    - Many devices can share a channel.
    - Congestion reduction is possible.
    - Supports unlimited message lengths.
  - Disadvantages:
    - Unsuitable for real-time voice/video.
    - Store-and-forward devices are expensive.
    - Potential security issues and lower reliability.

  ### 7.2 Circuit Switching

  - Concept: A dedicated path is established between sender and receiver for the entire session (classic telephone networks). Once established, data flows continuously over that path.
  - Advantages:
    - Guaranteed data rate.
    - No per-switching wait time during session.
    - Good for long continuous transmissions.
  - Disadvantages:
    - Channel is reserved (others cannot use it).
    - Requires more bandwidth.
    - Setup time to establish circuit can be long.

  ### 7.3 Packet Switching

  - Concept: Messages are divided into fixed-sized (or variable) packets, each independently routed through the network using routers. Packets are numbered; routers forward them toward destination (no dedicated path).
  - Key points:
    - Uses routers to direct packets between networks.
    - Packets from the same message may take different routes and can arrive out of order.
  - Advantages:
    - Efficient use of network resources.
    - High data throughput and good for bursty traffic.
    - No large memory requirements at nodes; no need for dedicated path.
    - Cost-effective and suitable for voice/video (with proper QoS).
  - Disadvantages:
    - Packets may arrive out of order.
    - Possible transmission delays and packet loss.
    - Implementation and security overhead.

  ## 8. Transmission Media

  Definition: The physical or wireless paths used to transmit data between network devices.

  Two main categories:

  - Guided Media: Physical cables (Twisted Pair, Coaxial, Fiber Optic).
  - Unguided Media: Wireless transmission (Radio, Microwave, Infrared).

  ### 8.1 Twisted Pair Cable

  Consists of pairs of insulated copper wires twisted together to minimize electromagnetic interference (EMI).

  Types:

  - UTP (Unshielded Twisted Pair): Most common in LANs; cheaper, easier to install.
  - STP (Shielded Twisted Pair): Has metallic shielding for noise resistance.

  Pros: Cheap, flexible, easy to install.

  Cons: Limited range, lower bandwidth, susceptible to noise.

  ### 8.2 Coaxial Cable

  Copper core with metal shielding to block interference. Common in TV and broadband Internet.

  Pros: High frequency support, better noise immunity, higher bandwidth.

  Cons: Bulky, harder to install, grounding required, less secure.

  ### 8.3 Fiber Optic Cable

  Transmits data as pulses of light through glass or plastic fibers.

  Types:

  - Single Mode (SMF): Long-distance, one light path.
  - Multi Mode (MMF): Short-distance, multiple light paths.

  Pros: Very high bandwidth, low attenuation, immune to EMI, secure.

  Cons: Expensive, fragile, difficult to install.

  ### 8.4 Unguided Media

  - Radio Waves: Used in Wi‑Fi, mobile networks — omnidirectional.
  - Microwaves: High frequency, point-to-point communication.
  - Infrared: Short-range, line-of-sight links (remote controls, sensors).

  ## 9. Open Systems and OSI Reference Model

  Proprietary systems restricted interoperability between vendors; this led to open systems and the OSI model (by ISO).

  - Purpose: Provide a standard framework for network communication.
  - Concept: Divide network communication into seven layers — each handling a specific function.

  ### 9.1 Seven Layers of OSI

  | Layer | Name         | Key Function                                   | Example         |
  |------:|--------------|--------------------------------------------------|-----------------|
  | 7     | Application  | User-level services                             | HTTP, FTP, SMTP |
  | 6     | Presentation | Data translation, encryption, compression       | SSL/TLS, JPEG   |
  | 5     | Session      | Establishes, maintains, terminates sessions     | NetBIOS         |
  | 4     | Transport    | Reliable delivery, segmentation, flow control   | TCP, UDP        |
  | 3     | Network      | Logical addressing, routing                     | IP              |
  | 2     | Data Link    | Frames, MAC addressing, error detection         | Ethernet        |
  | 1     | Physical     | Transmission of bits, cables, signals           | NIC, Hubs       |

  Layering benefit: Simplifies troubleshooting and development by isolating functions.

  ## 10. Communication Architecture

  Defines how devices interact and communicate within a network. Provides modularity and flexibility — each layer can evolve independently.

  Example: OSI defines how data travels from one host application to another across a network medium.

  ## 11. TCP/IP Model

  Foundation of the modern Internet. Simpler than OSI.

  Typical layering (4–5 layers):

  - Physical/Data Link: Hardware transmission.
  - Network: Internet Protocol (IP) handles addressing and routing.
  - Transport: Reliable or best-effort delivery (TCP/UDP).
  - Application: User protocols like HTTP, DNS, FTP, SMTP.

  Note: Real-world systems map OSI’s 7 layers into these 4–5 layers for practicality.

  ## 12. Internet Protocol (IP)

  Responsible for packet delivery from source to destination using logical addressing. Operates at the Network layer and provides best‑effort delivery — no guarantee of order, delivery, or error correction.

  ### 12.1 IP Datagram

  - Basic transfer unit (packet) containing header + data.
  - Each packet is independent and may take different routes.
  - IPv4 and IPv6 are the two main versions.

  ## 13. IPv4 — Key Concepts

  - Address Size: 32-bit (≈4.3 billion unique addresses).
  - Address Format: Dotted decimal (e.g., 192.168.1.1).
  - Header fields (selected): Version, Header Length (20–60 B), TOS/DSCP, Total Length, Identification/Flags/Fragment Offset, TTL, Protocol (TCP=6, UDP=17), Checksum, Source/Destination IP.
  - Limitations: Address exhaustion, complex header, no native security.

  ## 14. IPv6 — Next Generation IP

  Developed by IETF to replace IPv4 and fix address exhaustion.

  - Address Size: 128-bit → 2^128 unique addresses.
  - Representation: Colon-separated hexadecimal (e.g., 2001:0db8:85a3::8a2e:0370:7334).

  ### 14.1 IPv6 Address Types

  - Unicast: One-to-one communication.
  - Multicast: One-to-many group communication.
  - Anycast: One-to-nearest node among many (load-balancing, redundancy).

  ### 14.2 IPv6 Header Fields

  - Fixed 40-byte header: Version, Traffic Class, Flow Label, Payload Length, Next Header, Hop Limit, Source, Destination.
  - Extension Headers: Optional extra information linked in sequence (Routing, Fragmentation, Authentication).
  - No checksum or broadcast. Uses Neighbor Discovery Protocol (NDP) instead of ARP.

  ### 14.3 IPv6 Advantages

  - Larger address space.
  - Simplified routing and header processing.
  - Native IPsec support for security.
  - Better mobility and autoconfiguration.

  ## 15. IPv4 vs IPv6 — Comparison

  | Feature         | IPv4                                 | IPv6                                 |
  |-----------------|--------------------------------------|--------------------------------------|
  | Address Length  | 32-bit                               | 128-bit                              |
  | Address Format  | Decimal (e.g., 192.0.2.1)            | Hexadecimal (e.g., 2001:db8::1)      |
  | Configuration   | Manual/DHCP                          | Stateless auto-config + DHCPv6       |
  | Security        | Application-based                    | IPsec built-in                       |
  | Fragmentation   | Sender and Routers                   | Sender only                          |
  | Transmission    | Broadcast                            | Multicast / Anycast                  |
  | Mapping         | ARP                                  | NDP                                  |
  | Header Size     | Variable (20–60 B)                   | Fixed (40 B)                         |

  ## 16. MIME Types

  Multipurpose Internet Mail Extensions (MIME) defines how files are described and transferred between applications. Originally for email, now used across the web and APIs. Format: type/subtype.

  Examples:

  - text/html — HTML webpage
  - image/png — PNG image
  - application/json — JSON data

  Purpose: Ensures browsers, mail clients, and APIs correctly interpret file content.

  ## 17. Firewalls

  Hardware/software systems that filter and control network traffic based on security rules. They sit between trusted internal networks (LAN) and untrusted networks (Internet).

  Functions:

  - Monitor inbound and outbound packets.
  - Block unauthorized access.
  - Enforce access control policies.

  Types of firewalls:

  - Packet-filtering: Checks packet headers (IP, port, protocol). Simple, fast, limited context.
  - Stateful inspection: Tracks connection states; smarter decisions.
  - Proxy (application layer): Interprets and filters specific protocols like HTTP, FTP.
  - Next-gen firewalls: Combine deep packet inspection with intrusion prevention.

  ## 18. Network Addressing

  - Hostname: Human-readable name assigned to a device (e.g., server.company.com).
  - IP Address: Numeric logical identifier for each device (e.g., 192.168.10.1).
  - Structure: IP = Network portion + Host portion.
    - Network portion identifies the network.
    - Host portion identifies the specific machine.
  - Example: 192.168.10.25/24 → Network = 192.168.10.0, Host = 25.

  Addressing enables devices to identify and communicate uniquely within and across networks.

  ## 19. Domain Name System (DNS)

  Distributed, hierarchical system for mapping hostnames to IP addresses.

  Why DNS: Humans use names, machines use numeric IPs.

  Process:

  1. User enters a domain name (e.g., www.google.com).
  2. Browser sends a query to the local DNS resolver.
  3. Resolver queries root, then TLD, then authoritative DNS servers.
  4. IP address is returned to the client; result is cached.

  DNS hierarchy:

  - Root domain (.)
  - Top-Level Domain (TLD): .com, .org, .in, etc.
  - Second-Level Domain: e.g., google in google.com.
  - Subdomain: e.g., mail.google.com.

  Key features:

  - Redundant, distributed database (no single failure point).
  - Uses port 53 (UDP/TCP).
  - Caching speeds up lookups.

  ## 20. Summary — Key Takeaways

  | Concept               | Core Idea                                                             |
  |-----------------------|-----------------------------------------------------------------------|
  | Network               | Collection of devices communicating and sharing resources             |
  | Types of Networks     | LAN (local), MAN (city), WAN (global)                                 |
  | Switching             | Message, Circuit, and Packet — basis of modern networking             |
  | Transmission Media    | Guided (wired) vs. Unguided (wireless)                                |
  | OSI Model             | 7-layer communication standard                                        |
  | TCP/IP Model          | 4–5-layer practical Internet model                                    |
  | IPv4 vs IPv6          | 32-bit vs 128-bit addressing; IPv6 = next-gen protocol                |
  | MIME Types            | Identify and handle file formats in communication                      |
  | Firewalls             | Secure network boundary; control incoming/outgoing traffic            |
  | DNS                   | Translates human-readable domain names into IP addresses              |

  Final notes:

  - Networking aims for efficient communication and secure data exchange.
  - Understand layer functions, not just memorize them — helps blue/red team work.
  - Next topics: subnetting, routing protocols, NAT, and network security tools.
