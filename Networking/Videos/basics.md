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
  - Potential security issues and lower reliability. :contentReference[oaicite:20]{index=20}

### 7.2 Circuit Switching
- **Concept:** A dedicated path is established between sender and receiver for the entire session (classic telephone networks). Once established, data flows continuously over that path. :contentReference[oaicite:21]{index=21}
- **Advantages:**
  - Guaranteed data rate.
  - No per-switching wait time during session.
  - Good for long continuous transmissions. :contentReference[oaicite:22]{index=22}
- **Disadvantages:**
  - Channel is reserved (others cannot use it).
  - Requires more bandwidth.
  - Setup time to establish circuit can be long. :contentReference[oaicite:23]{index=23}

### 7.3 Packet Switching
- **Concept:** Messages are divided into fixed-sized (or variable) **packets**, each independently routed through the network using routers. Packets are numbered; routers forward them toward destination (no dedicated path). :contentReference[oaicite:24]{index=24}
- **Key points:**
  - Uses routers to direct packets between networks.
  - Packets from the same message may take different routes and can arrive out of order. :contentReference[oaicite:25]{index=25}
- **Advantages:**
  - Efficient use of network resources.
  - High data throughput and good for bursty traffic.
  - No large memory requirements at nodes; no need for dedicated path.
  - Cost-effective and suitable for voice/video (with proper QoS). :contentReference[oaicite:26]{index=26}
- **Disadvantages:**
  - Packets may arrive out of order.
  - Possible transmission delays and packet loss.
  - Implementation and security overhead. :contentReference[oaicite:27]{index=27}

---

### End of notes (stopped at **Packet Switching**).  
If you want, I can:
- Continue notes beyond packet switching (Transmission Media, OSI/TCP-IP, IPv4/IPv6, etc.), or  
- Produce a ready-to-drop `README.md` file (with front-matter, badges, or collapsible sections).  

Which would you like next?
