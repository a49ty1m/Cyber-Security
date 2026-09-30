# Windows Incident Surface — Task 5: Network Scope

## Objective

Understand the network footprint of a Windows system during an investigation.

We want to answer:

```text
What is communicating?
        ↓
Which process owns the connection?
        ↓
Where is the process located?
        ↓
Which remote system/port is involved?
        ↓
Is the connection expected?
```

The room focuses on: active TCP connections, owning processes, process paths, remote ports, network shares, firewall profiles, and firewall rules.

Attackers may use network connections for **Command & Control (C2)** or **lateral movement**.

---

# Mental Model

The most important concept from this task is **correlation**:

```text
Network Connection → Owning Process → Process Name → Process Path
        ↓
User / Service → File on Disk → Is it legitimate?
```

For example:

```text
Suspicious Remote Connection → PID 1234 → process.exe
        ↓
C:\Users\...\Temp\process.exe → Unexpected location → Potentially suspicious
```

You're not just looking for "bad IP addresses." You're trying to understand **which local program is communicating and why**.

---

# 1. Active TCP Connections

### Question

> What network connections exist, and which processes own them?

```powershell
Get-NetTCPConnection |
select Local*, Remote*, State, OwningProcess,
@{n="ProcName";e={(Get-Process -Id $_.OwningProcess).ProcessName}},
@{n="ProcPath";e={(Get-Process -Id $_.OwningProcess).Path}} |
sort State |
ft -Auto |
tee tcp-conn.txt
```

| Field           | Meaning                        |
| --------------- | ------------------------------ |
| `LocalAddress`  | Local IP address               |
| `LocalPort`     | Local port                     |
| `RemoteAddress` | Remote IP address              |
| `RemotePort`    | Remote port                    |
| `State`         | Connection state               |
| `OwningProcess` | PID responsible for connection |
| `ProcName`      | Process name                   |
| `ProcPath`      | Executable path                |

### Why OwningProcess Is Critical

A connection alone doesn't tell you **what caused it**. The command maps:

```text
OwningProcess → Get-Process → Process Name → Process Path
```

### Connection States

Don't automatically treat every `LISTEN` or `ESTABLISHED` connection as malicious. For example, `lsass.exe` on port 49689 may represent legitimate Windows functionality. **Context is required.**

---

# 2. Establishing Suspicion

When reviewing connections, ask:

### What process owns it?

```text
ProcName
```

### Where is the executable?

```text
ProcPath
```

### Is the location normal?

Expected:

```text
C:\Windows\System32\
C:\Program Files\
```

Suspicious:

```text
C:\Users\...\AppData\
C:\Users\...\Temp\
```

### What remote port is being used?

> Is this expected for this application?

### Is the connection persistent?

A repeated connection may indicate regular communication with another system.

---

# 3. Lab Findings

The room identified several interesting network behaviours:

- **RDP connection** → Expected (investigator's session) — do not treat as malicious
- **Multiple `ssh.exe` connections** → Could indicate an anomaly
- **AnyDesk connections** → Can be legitimate or malicious
- **Process from AppData Temp location** → Deserves investigation

**Lesson:** AnyDesk, SSH, and RDP can all be legitimate. A temporary executable can be legitimate. When several indicators appear together, investigation priority increases.

---

# 4. Bidirectional Investigation

### From Network → Process

```text
Remote Connection → Owning PID → Process Name → Executable Path → File Investigation
```

### From Process → Network

```text
Process → PID → Get-NetTCPConnection → Remote IP → Remote Port → Connection State
```

This works in both directions.

### From User → Network

```text
Suspicious User → Active Session → Processes → Owning PID → Network Connections → Remote System
```

Allows you to investigate **which user's activity is associated with a connection**.

### From Service → Network

```text
Suspicious Service → Service PID → Process → TCP Connection → Remote IP / Port
```

Particularly useful when a service executable is in a suspicious location.

---

# 5. Investigation Matrix

| Starting Point     | Pivot To                     |
| ------------------ | ---------------------------- |
| User               | Session → Process → Network  |
| Process            | PID → Network → File         |
| Service            | PID → Process → Network      |
| File               | Process → PID → Network      |
| Network connection | PID → Process → Path         |
| Firewall rule      | Program → Path → Network     |
| Network share      | User → Files → Remote system |

---

# 6. Network Shares

### Question

> What folders or drives are exposed through Windows network shares?

```powershell
Get-CimInstance -Class Win32_Share | tee net-shares.txt
```

Common Windows administrative/default shares: `ADMIN$`, `C$`, `IPC$` — not suspicious by themselves.

### Why Shares Matter

```text
Compromised Account → Access to Network Share → Upload File → Remote Execution → Lateral Movement
```

**MITRE ATT&CK:** T1039, T1570, T1021, T1080

---

# 7. Firewall Profiles

### Question

> What firewall profiles and rules are currently configured?

```powershell
Get-NetFirewallProfile |
ft Name, Enabled, DefaultInboundAction, DefaultOutboundAction |
tee fw-profiles.txt
```

| Field                   | Meaning                              |
| ----------------------- | ------------------------------------ |
| `Name`                  | Firewall profile (Domain/Private/Public) |
| `Enabled`               | Whether it is active                 |
| `DefaultInboundAction`  | Default handling of inbound traffic  |
| `DefaultOutboundAction` | Default handling of outbound traffic |

### Disabled Firewall Profiles

The lab showed all three profiles as disabled:

```text
Domain  → Disabled
Private → Disabled
Public  → Disabled
```

Don't immediately conclude: *"Firewall disabled = attacker."*

The room points out this could be legitimate if another security layer is in use.

**Always compare against:** organizational baseline + system configuration + other security controls.

---

# 8. Firewall Rules

```powershell
.\fw-summary.ps1 | tee fw-rules.txt
```

Provides: `DisplayName`, `Protocol`, `LocalPort`, `RemotePort`, `RemoteAddress`, `Direction`, `Action`, `Program`.

```text
Which program? → Which protocol? → Which port? → Inbound or outbound? → Allowed or blocked?
```

### Suspicious Firewall Rules

A rule deserves attention when it is:
- Unexpected
- Associated with an unknown program or unusual path
- Allowing an unusual or broad port range
- Different from the organization's baseline

**Lab finding:** AnyDesk rules appeared — the same software also appeared during the TCP investigation:

```text
TCP Connection → AnyDesk Process → AnyDesk Executable → Firewall Rule → Multiple pieces of evidence
```

This is exactly the type of correlation you should practice.

---

# 9. Investigation Workflow

```text
Something looks suspicious
        ↓
Find its PID → Find its process → Find executable path
        ↓
Find its network connections → Identify remote IP + port
        ↓
Check firewall rules → Check associated user/service
        ↓
Correlate everything → Decide whether actually suspicious
```

> Don't treat an unusual port, AnyDesk, SSH, a disabled firewall, or a strange IP as automatic proof of compromise. Always compare baseline and correlate before drawing conclusions.

---

# Quick Revision

| Question                        | Command                                  |
| ------------------------------- | ---------------------------------------- |
| What is communicating?          | `Get-NetTCPConnection`                   |
| Which process owns connection?  | `Get-Process -Id <PID>`                  |
| Where is the executable?        | `(Get-Process -Id <PID>).Path`           |
| What is shared over the network?| `Get-CimInstance -Class Win32_Share`     |
| Is Windows Firewall configured? | `Get-NetFirewallProfile`                 |
| Which programs/ports allowed?   | `.\fw-summary.ps1`                       |

---

# Evidence Files

| File              | Contains                                         |
| ----------------- | ------------------------------------------------ |
| `tcp-conn.txt`    | Active TCP connections and associated processes  |
| `net-shares.txt`  | Windows network shares                           |
| `fw-profiles.txt` | Firewall profile configuration                   |
| `fw-rules.txt`    | Firewall rules                                   |

---

# What I Learned

- Enumerate active TCP connections
- Identify local and remote ports and remote addresses
- Map network connections to PIDs and process names
- Find the executable path of a network-connected process
- Investigate network shares
- Check Windows Firewall profiles
- Investigate firewall rules
- Correlate network evidence with processes, users, services, and files

### Most important lesson

> **A network connection becomes much more useful when you can explain which local process created it and where that process came from.**

```text
Something suspicious → Find PID → Find process → Find executable path
        ↓
Find network connections → Identify remote IP + port
        ↓
Check firewall rules → Check user/service
        ↓
Correlate everything → Decide
```
