# Windows Incident Surface — Task 3
### System Profiling

> **Room:** Windows Incident Surface
> **Focus:** DFIR / System Profiling / Network ID / OS Enumeration / Timezone / Group Policy
> **MITRE:** T1484.001

---

## Objective

After fixing compromised tools in Task 2, the next step is to **profile the system** before diving into deeper artefacts. This anchors all later findings.

Questions to answer:

- What is the hostname and domain?
- What network interfaces / IPs / MACs does it have?
- What OS version and build is installed?
- When was the OS installed? When did it last boot?
- What timezone is the system in?
- What Group Policies are currently applied?

---

## The Core Skill: Command Discovery (Don't Memorize)

The real lesson of this task isn't the commands themselves — it's knowing **how to find them**.

`Get-CimInstance` is a query mechanism. The class name (e.g. `Win32_NetworkAdapterConfiguration`) determines what you're querying. You shouldn't memorize class names; you should know how to discover them.

### Discovery workflow

```text
What information do I need?
        ↓
Search CIM classes by keyword
        ↓
Get-CimClass -ClassName *<keyword>*
        ↓
Query the class
        ↓
Get-CimInstance <ClassName>
        ↓
Inspect what properties exist
        ↓
<command> | Get-Member
        ↓
Select / filter / format
```

### Useful discovery commands

```powershell
Get-CimClass -ClassName *Network*          # find network-related classes
Get-CimClass -ClassName *OperatingSystem*  # find OS classes
Get-CimClass -ClassName *Disk*             # find disk classes
Get-Command *Cim*                          # list all CIM cmdlets
Get-Command *GP*                           # list Group Policy cmdlets
Get-Help <cmdlet> -Examples                # see usage examples
<command> | Get-Member                     # inspect returned object's properties
<command> | Select-Object *                # dump all property values
```

---

## How to Go From `Get-CimInstance` → Class → Properties → Filter → Select

This is the part that's never clearly explained. Here's the exact chain.

---

### Step 1: Find the class name

You know `Get-CimInstance` exists. But what do you pass to it?

Use `Get-CimClass` with a wildcard keyword matching what you're looking for:

```powershell
# Looking for network info?
Get-CimClass -ClassName *Network*

# Looking for OS info?
Get-CimClass -ClassName *OperatingSystem*

# Looking for process info?
Get-CimClass -ClassName *Process*
```

This returns a list of matching CIM classes. Scan the names — they're usually self-descriptive:

```text
Win32_NetworkAdapter
Win32_NetworkAdapterConfiguration   ← this one has config/IP/MAC data
Win32_NetworkAdapterSetting
...
```

Pick the one that looks right. If unsure, query both and inspect.

---

### Step 2: Find out what properties and filters exist

Now you have a class name. But how do you know what fields it has — like `IPEnabled`, `DNSHostname`, `IPAddress`?

**Option A — See all properties of a returned instance:**

```powershell
Get-CimInstance Win32_NetworkAdapterConfiguration | Select-Object *
```

This dumps every property and its current value. Scroll through and pick what you need.

**Option B — List just the property names (no values):**

```powershell
Get-CimInstance Win32_NetworkAdapterConfiguration | Get-Member -MemberType Property
```

`Get-Member -MemberType Property` shows only the data properties (filters out methods). Output looks like:

```text
Name                    MemberType Definition
----                    ---------- ----------
DefaultIPGateway        Property   string[] DefaultIPGateway {get;}
DHCPEnabled             Property   bool DHCPEnabled {get;}
DNSHostName             Property   string DNSHostName {get;}
IPAddress               Property   string[] IPAddress {get;}
IPEnabled               Property   bool IPEnabled {get;}
MACAddress              Property   string MACAddress {get;}
...
```

Now you can see `IPEnabled` is a `bool` property. That's how you know you can filter on it.

**Option C — Inspect the class definition directly (no instance needed):**

```powershell
(Get-CimClass -ClassName Win32_NetworkAdapterConfiguration).CimClassProperties |
    Select-Object Name, CimType
```

This gives you property names and their data types without even querying an instance — useful when you just want to browse.

---

### Step 3: Understand `-Filter`

`-Filter` takes a WQL (WMI Query Language) string. The syntax is:

```text
-Filter "PropertyName=Value"
-Filter "PropertyName > Value"
-Filter "PropertyName LIKE '%pattern%'"
```

You need to know a property name and valid values to write a filter. You get those from **Step 2**.

Example: you see `IPEnabled` is a `bool`. So valid values are `TRUE` or `FALSE`:

```powershell
-Filter "IPEnabled=TRUE"    # only interfaces with IP enabled
```

Without a filter, `Get-CimInstance Win32_NetworkAdapterConfiguration` returns every adapter including inactive ones (loopback, virtual, disabled). The filter cuts it down to only the relevant ones.

---

### Step 4: Choose what to `Select-Object`

After steps 2 and 3, you know the property names. Pick the ones you actually need:

```powershell
Get-CimInstance Win32_NetworkAdapterConfiguration `
    -Filter "IPEnabled=TRUE" |
    Select-Object DNSHostName, IPAddress, MACAddress
```

`Select-Object` limits the output to those specific fields. Without it, you'd get all 80+ properties dumped for every adapter — unreadable.

---

### Full chain summarized

```text
Get-CimInstance          ← the query tool
        ↓
Get-CimClass *keyword*   ← find the class name
        ↓
| Select-Object *        ← see all property values (or | Get-Member -MemberType Property for names only)
        ↓
-Filter "Prop=Value"     ← narrow down instances using a property you discovered
        ↓
| Select-Object A, B, C  ← pick only the fields you need
        ↓
| Format-Table / fl      ← readable output
```

---

## 1. Network & Host Identification

### How to arrive at this command independently

1. You need: hostname, IP, MAC address → concept: **network adapter configuration**
2. Search: `Get-CimClass -ClassName *Network*` → find `Win32_NetworkAdapterConfiguration`
3. Query: `Get-CimInstance Win32_NetworkAdapterConfiguration | Get-Member` → find `DNSHostname`, `IPAddress`, `MACAddress`, `IPEnabled`
4. Filter to active interfaces only using `-Filter "IPEnabled=TRUE"`

### Final command

```powershell
Get-CimInstance Win32_NetworkAdapterConfiguration `
    -Filter "IPEnabled=TRUE" |
    Select-Object DNSHostname, IPAddress, MACAddress |
    Format-Table
```

The `-Filter` parameter uses WQL (WMI Query Language) syntax. `IPEnabled=TRUE` is a property on the class — you'd discover it the same way via `Get-Member`.

---

## 2. OS Information

### How to arrive at this command independently

1. You need OS version, build, install date, last boot → concept: **operating system**
2. Search: `Get-CimClass -ClassName *OperatingSystem*` → find `Win32_OperatingSystem`
3. Query: `Get-CimInstance Win32_OperatingSystem | Get-Member` → find relevant properties

### Final command

```powershell
Get-CimInstance -ClassName Win32_OperatingSystem |
    Select-Object CSName, Version, BuildNumber,
                  InstallDate, LastBootUpTime, OSArchitecture |
    Format-List
```

### Key properties

| Property         | Meaning                          |
|------------------|----------------------------------|
| `CSName`         | Computer hostname                |
| `Version`        | OS version string (e.g. 10.0.x) |
| `BuildNumber`    | Build number — different from Version |
| `InstallDate`    | When the OS was installed        |
| `LastBootUpTime` | Last system reboot               |
| `OSArchitecture` | x64 or x86                      |

> Don't confuse `Version` with `BuildNumber` — they are separate fields.

---

## 3. Date & Timezone

```powershell
Get-Date ; Get-TimeZone
```

Simple commands, but critically important for DFIR context.

**Why timezone matters:** A raw timestamp like `10:30 AM` is meaningless without knowing:
- the system's UTC offset
- whether the clock is accurate relative to NTP
- which machine generated the event

Timestamps in event logs, file metadata, scheduled tasks, and network logs must all be interpreted relative to the system's timezone. If the clock is wrong, your timeline will be wrong.

A clock significantly off from NTP is worth noting and investigating — though it could simply be misconfiguration or domain sync failure, not necessarily an attack.

---

## 4. Group Policy — RSoP Report

**Resultant Set of Policy (RSoP)** shows which Group Policies are actually applied to the current user and computer (taking precedence and filtering into account).

### How to discover the command

```powershell
Get-Command *GP*                               # lists GP-related cmdlets
Get-Help Get-GPResultantSetOfPolicy -Examples  # see how to use it
```

### Generate the report

```powershell
Get-GPResultantSetOfPolicy `
    -ReportType HTML `
    -Path (Join-Path -Path (Get-Location).Path -ChildPath "RSOPReport.html")
```

`Join-Path` safely combines the current directory path with the output filename. `Get-Location` returns the current directory. This simply saves the report as `RSOPReport.html` in the current working directory.

### What to look for in the report

Attackers may modify Group Policies to weaken defences or maintain control (T1484.001). Focus on policies affecting:

- Windows Defender / antivirus settings
- Firewall rules
- PowerShell execution policy
- Audit and event logging
- User account restrictions
- Authentication settings
- Script execution

Compare everything against what the organization normally deploys. An unexpected policy is not automatically malicious — it needs context.

---

## Questions & Answers

| # | Question | Source | Property |
|---|----------|--------|----------|
| 1 | Hostname of compromised host | `Get-CimInstance Win32_OperatingSystem` | `CSName` |
| 2 | OS version of compromised host | `Get-CimInstance Win32_OperatingSystem` | `Version` (not `BuildNumber`) |
| 3 | Time ID of compromised host | `Get-TimeZone` | TimeZone ID field |

---

## Command Reference

| Command | Purpose |
|---------|---------|
| `Get-CimInstance` | Query a CIM/WMI class for system info |
| `Get-CimClass` | Discover and browse available CIM classes |
| `Get-Member` | Inspect properties and methods of returned objects |
| `Get-Command` | Find available cmdlets by name pattern |
| `Get-Help` | Read documentation and examples |
| `Get-Date` | Get current system date/time |
| `Get-TimeZone` | Get system timezone |
| `Get-GPResultantSetOfPolicy` | Generate RSoP policy report (HTML/XML) |
| `Get-Location` | Get current working directory |
| `Join-Path` | Safely construct file paths |
| `Select-Object` | Pick specific properties from output |
| `Format-Table` / `ft` | Display results as a table |
| `Format-List` / `fl` | Display results as a vertical list |

---

## DFIR Principles from This Task

1. **Profile before you hunt.** Hostname, timezone, and OS version anchor all later artefact analysis. Get these first.

2. **Discover commands — don't memorize them.** `Get-CimClass -ClassName *keyword*` + `Get-Member` will get you to any system data. The specific class names are secondary.

3. **Timestamps require timezone context.** A timestamp without a timezone is ambiguous and potentially misleading in a timeline reconstruction.

4. **Unusual ≠ malicious.** A wrong clock or unexpected policy is a reason to investigate, not an immediate conclusion of compromise.

5. **Baseline comparison is everything.** Anomalies only stand out when you know what the normal state looks like. Get the RSoP report and compare it.

---

**References:**
- [Win32_NetworkAdapterConfiguration — Microsoft Learn](https://learn.microsoft.com/en-us/windows/win32/cimwin32prov/win32-networkadapterconfiguration)
- [Get-CimClass — Microsoft Learn](https://learn.microsoft.com/en-us/powershell/module/cimcmdlets/get-cimclass)
- [Get-GPResultantSetOfPolicy — Microsoft Learn](https://learn.microsoft.com/en-us/powershell/module/grouppolicy/get-gpresultantsetofpolicy)
