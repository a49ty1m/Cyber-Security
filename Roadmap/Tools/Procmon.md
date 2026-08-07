# 👁️ Procmon: Complete Reference

> **What is Procmon?** Process Monitor (Procmon) is a free Windows Sysinternals tool that captures real-time file system, Windows Registry, and process/thread activity for every process running on the system. Every file create/read/write/delete, every registry key open/set/query, every network connection and DLL load is logged with the calling process, exact timestamp, result code, and full path. It is the definitive tool for understanding what a process is actually doing on a Windows system.
>
> **When to use it:** Dynamic malware analysis — what files does this malware create? What registry keys does it set for persistence? What DLLs does it load? Troubleshooting application behavior. Privilege escalation research (finding misconfigured file/registry paths a privileged process writes to). DLL hijacking discovery. Understanding installation behavior.
>
> **Tier 4 Reminder:** Know how to capture and filter Procmon output during malware analysis and troubleshooting. Depth of mastery is situational.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | Core Usage | 5 | 2–3 hours |
| 3 | Filtering | 4 | 2–3 hours |
| 4 | Malware Analysis Use | 3 | 2–3 hours |
| 5 | Mastery Check | 2 | 30 min |
| | **Total** | **18** | **~8–12 hours** |

**Setup:** Procmon only runs on Windows. Use in a Windows analysis VM. Download from `learn.microsoft.com/sysinternals/downloads/procmon`. No installation — single executable. Requires admin privileges.

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — What Procmon Captures

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **File System** | Every `CreateFile`, `ReadFile`, `WriteFile`, `DeleteFile`, `SetFileAttributes` call. Shows full path, result (SUCCESS/NAME NOT FOUND/ACCESS DENIED), and calling process. |
| **Registry** | Every `RegOpenKey`, `RegSetValue`, `RegQueryValue`, `RegDeleteKey`. Shows key path and value name. |
| **Process/Thread** | Process creation and exit. Thread creation. DLL image loads. |
| **Network** | TCP/UDP connections. Source/destination IP and port. (Less detailed than Wireshark — use both together for complete picture.) |

---

### Task 1.2 — Interface Overview

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Event List** | Main scrolling list: Sequence, Time, Process Name, PID, Operation, Path, Result, Detail. |
| **Toolbar Icons** | Magnifying glass: filter (highlight icon). Funnel: filter. Red record dot: start/stop capture. Blue eraser: clear events. |
| **Capture Toggle** | `Ctrl+E` — toggle event capture. Start Procmon → wait for activity → stop → analyze. |
| **Columns** | Right-click column header → add/remove columns: Duration, User, Authentication ID, etc. |

---

### Task 1.3 — Event Categories

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Toolbar Filters** | Show File System Activity (folder icon). Show Registry Activity (registry icon). Show Network Activity (wifi icon). Show Process & Thread Activity (gear icon). Toggle each on/off to reduce noise. |

---

### Task 1.4 — Saving and Loading Traces

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Save** | File → Save → PML (native format, preserves all data). Or save as CSV for Excel/grep analysis. |
| **Load** | File → Open → load saved PML. Analyze offline (useful: capture on analysis VM, analyze on main machine). |
| **Backing File** | By default, Procmon pages events to disk to avoid running out of RAM. File → Backing Files → configure location. |

---

# PHASE 2: CORE USAGE

---

### Task 2.1 — Basic Capture Workflow

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Workflow** | 1. Clear existing events (`Ctrl+X`). 2. Start capture (`Ctrl+E`). 3. Execute the process/action you want to observe. 4. Stop capture (`Ctrl+E`). 5. Apply filters to isolate relevant events. 6. Analyze. |
| **Malware** | Start Procmon → snapshot VM → execute malware → observe activity in Procmon → stop → filter by malware process name → document all file, registry, network activity. |

---

### Task 2.2 — Filter by Process

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Add Filter** | Filter → Filter (`Ctrl+L`) → `Process Name` `is` `malware.exe` `include`. Add. Apply. Now only events from `malware.exe` are shown. |
| **PID Filter** | If the process name is common (e.g., `powershell.exe`), filter by PID instead: `PID` `is` `1234`. |
| **Exclude Noise** | `Process Name` `is` `Procmon.exe` `exclude` — remove Procmon's own events. |

---

### Task 2.3 — Highlight Events

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Highlight Rules** | Filter → Highlight Rules → add rules: `Operation` `contains` `WriteFile` → color red. `Path` `contains` `HKCU\SOFTWARE\Microsoft\Windows\CurrentVersion\Run` → color green (persistence). |

---

### Task 2.4 — Process Tree

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **View** | Tools → Process Tree → shows all processes that ran during capture, with parent-child relationships. |
| **Malware Use** | See if malware spawned child processes. Example: `malware.exe` → spawns `cmd.exe` → runs `powershell.exe` → downloads payload. |

---

### Task 2.5 — Summary Statistics

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Tools Menu** | Tools → File Summary: most-accessed paths. Tools → Registry Summary: most-accessed keys. Tools → Network Summary: connections made. |
| **Use** | Quick overview of what a process touched — much faster than reading every event. |

---

# PHASE 3: FILTERING

---

### Task 3.1 — Operation Filters

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **File Writes** | `Operation` `is` `WriteFile` `include`. Finds all files written — persistence payloads, dropped files, log files. |
| **Registry Persistence** | `Path` `contains` `CurrentVersion\Run` `include`. Catches common autorun key modifications. |
| **Successful Only** | `Result` `is` `SUCCESS` `include`. Removes all the "NOT FOUND" noise from failed lookup attempts. Very useful. |
| **Access Denied** | `Result` `is` `ACCESS DENIED` `include`. Shows privilege escalation targets — what is the process trying to access that it shouldn't? |

---

### Task 3.2 — Path Filters

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Temp Directory** | `Path` `contains` `\Temp\` `include`. Malware often drops payloads in Temp. |
| **AppData** | `Path` `contains` `AppData` `include`. Common malware persistence location. |
| **System32** | `Path` `contains` `System32` `include`. Detects attempts to write to system directories. |
| **Startup Folder** | `Path` `contains` `Startup` `include`. Persistence via startup folder. |

---

### Task 3.3 — DLL Hijacking Discovery

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Technique** | Run a privileged process (e.g., a Windows service). Filter Procmon: `Operation` `is` `CreateFile`, `Result` `is` `NAME NOT FOUND`, `Path` `ends with` `.dll`. |
| **What You See** | A privileged process looking for a DLL that doesn't exist in the application directory. If you can write to that directory: plant a malicious DLL there → process loads it → code execution as the service's privilege level. |
| **Practical Use** | This technique is used for local privilege escalation. Procmon is the standard tool for finding these opportunities. |

---

### Task 3.4 — Reducing Noise

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Common Noisy Processes** | Exclude: `Procmon.exe`, `svchost.exe` (unless it's your target), `explorer.exe`, `SearchIndexer.exe`, `MsMpEng.exe` (Defender). |
| **Result Filter** | Exclude `NAME NOT FOUND` and `PATH NOT FOUND` if they're not relevant — massively reduces noise from DLL and file search failures. |
| **Event Type** | Focus on File System only (disable Registry and Network temporarily) to reduce visual complexity during initial analysis. |

---

# PHASE 4: MALWARE ANALYSIS USE

---

### Task 4.1 — Malware Behavioral Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Document all filesystem and registry changes made by malware execution. |
| **Key Questions** | What files did it create/modify/delete? What registry keys did it set (especially Run keys → persistence)? What DLLs did it load? What processes did it spawn? Did it access any credential stores (SAM, LSASS paths)? |
| **Evidence Trail** | Every event has a timestamp, result, and exact path. The Procmon log is forensic evidence of what the malware did. |

---

### Task 4.2 — Integrating with x64dbg

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Workflow** | Run both simultaneously: x64dbg for code-level control (step through, breakpoints). Procmon for system-level observation (what does each code section do to the OS?). Step through suspicious code in x64dbg → observe the corresponding file/registry event appear in Procmon. |

---

### Task 4.3 — IOC Extraction

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **From Procmon Log** | File paths created → file IOCs. Registry keys set → registry IOCs. Mutex names (in Process & Thread events). Network destinations → IP/domain IOCs. |
| **Export** | File → Save → CSV → import into Excel/Splunk for IOC extraction and report generation. |

---

# PHASE 5: MASTERY CHECK

---

### Task 5.1 — Competency Self-Assessment

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Competency | Self-Assessment |
|:---|:---:|
| Can capture and stop a Procmon trace | ☐ |
| Can filter events by process name, operation, and path | ☐ |
| Can use the Process Tree to view child process spawning | ☐ |
| Can find persistence registry keys in a malware trace | ☐ |
| Can use Procmon to find DLL hijacking opportunities | ☐ |
| Can extract IOCs from a Procmon log | ☐ |

---

### Task 5.2 — Interview Questions

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

1. What three categories of system activity does Procmon capture?
2. How do you filter Procmon to show only events from a specific process?
3. How do you use Procmon to find DLL hijacking opportunities?
4. What Procmon filter shows all registry persistence keys modified?
5. How do you use Procmon alongside x64dbg in malware analysis?
6. What is the value of filtering on `Result = ACCESS DENIED` during privilege escalation research?
