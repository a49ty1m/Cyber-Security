# 🌐 Networking Notes (Video Learning Summary)
### Day 1 of video basics

---

### 🧩 **Introduction to Networking**
- A **computer network** is a group of interconnected devices (nodes/hosts) that share data and resources.
- Connections can be **wired (Ethernet, fiber)** or **wireless (Wi-Fi, infrared, radio)**.
- Key term: **Data Transfer Rate** → the speed of data movement between devices.
- Networks enable the **Client-Server Model** where servers provide services (like web or file sharing) to clients.

---

### 🧭 **Types of Networks**
| Type | Description | Example |
|------|--------------|----------|
| **LAN (Local Area Network)** | Covers small areas like buildings or campuses. | College lab |
| **MAN (Metropolitan Area Network)** | Connects multiple LANs within a city. | City ISPs |
| **WAN (Wide Area Network)** | Connects LANs globally — forms the Internet. | The Internet |

**Topologies:**
- 🌀 **Ring** → data flows one way around the loop.  
- ⭐ **Star** → all devices connect to a central hub/switch.  
- ➖ **Bus** → single communication line shared by all.

---

### ⚙️ **Network Devices**
| Device | Function |
|--------|-----------|
| **Hub** | Broadcasts packets to all ports (no intelligence). Works at OSI Layer 1. |
| **Repeater** | Boosts weak signals to extend range. |
| **Modem** | Converts digital ↔ analog data for transmission via phone/cable lines. |
| **NIC (Network Interface Card)** | Connects a computer to the network (Layer 1 & 2). Uses MAC addresses. |
| **Switch** | Forwards packets only to the intended destination (Layer 2). |
| **Bridge** | Connects multiple network segments and filters traffic using MAC addresses. |
| **Router** | Directs packets between different networks (Layer 3). |
| **Gateway** | Translates between different network protocols. |
| **Wireless Access Point (WAP)** | Enables wireless devices to connect to a wired network. |

---

### 🔄 **Switching**
- Connecting every device point-to-point is inefficient → switching solves this.  
- **Switched network:** multiple devices connected via intelligent nodes called *switches*.  

#### Types of Switching
| Type | Description | Key Traits |
|------|--------------|-------------|
| **Message Switching** | Entire message stored and forwarded hop by hop. | Slow, high memory need, not for real-time. |
| **Circuit Switching** | Dedicated path established before communication. | Reliable, fixed rate, inefficient bandwidth use. |
| **Packet Switching** | Message divided into small packets that travel independently. | Efficient, cheap, but may have delay & reordering. |

✅ *Packet Switching* is the foundation of the Internet — used in TCP/IP networks.  
Each packet has source + destination info and is routed via multiple paths for best efficiency.

---

**Key takeaway:**  
Modern networks re
