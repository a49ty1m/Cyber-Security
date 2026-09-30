# Windows Incident Surface — Task 4: Users & Sessions

## Objective

Identify local user accounts, suspicious or unexpected accounts, account properties, privileged group membership, currently logged-in users, and suspicious active sessions.

Attackers may create accounts or modify existing ones to maintain access or increase privileges.

**MITRE ATT&CK:** T1136 — Create Account | T1098 — Account Manipulation | T1078 — Valid Accounts

---

# Mental Model

```text
Local Users → Who exists?
      ↓
Account Details → Is the account legitimate?
      ↓
Group Membership → What privileges does it have?
      ↓
Active Sessions → Is someone currently using it?
      ↓
Correlate the evidence → Normal / Suspicious
```

### Key Lesson

> **An unusual account is an investigation lead, not automatically proof of compromise.**

Suspicious accounts and sessions need to be correlated with other artefacts and the organization's baseline.

---

# 1. Enumerate Local Users

### Question

> Which local accounts exist on the Windows system?

```powershell
Get-LocalUser | tee l-users.txt
```

Investigate specific accounts:

```powershell
Get-LocalUser -Name Guest | Select * | tee usr-guest.txt
Get-LocalUser -Name Administrator | Select * | tee usr-Administrator.txt
```

### Why Enumerate Users?

Attackers can:
- Create new accounts
- Modify existing accounts
- Enable disabled accounts
- Abuse legitimate accounts
- Use privileged accounts for persistence

The first step is establishing **who exists on the machine**.

---

# 2. What Makes a User Suspicious?

| Indicator                 | Question                                          |
| ------------------------- | ------------------------------------------------- |
| Unexpected account        | Why does this account exist?                      |
| Similar username          | Is it impersonating another account?              |
| Typo in username          | Could it be masquerading as a legitimate account? |
| Enabled unexpectedly      | Why is it enabled?                                |
| Guest account             | Is guest access actually required?                |
| Administrative privileges | Does it really need admin rights?                 |
| Unusual password settings | Are they consistent with policy?                  |
| Active session            | Is someone currently using it?                    |

### Lab Finding

There were multiple accounts whose names appeared to represent administrators:
- Only one was expected
- Another had a deliberate typo
- All had administrative privileges

---

# 3. Account Details Worth Investigating

```text
Name / Enabled / Description / SID
PasswordRequired / PasswordExpires / PasswordChangeable / LastLogon
```

Collect password-related properties across all local accounts:

```powershell
Get-CimInstance -Class Win32_UserAccount -Filter "LocalAccount=True" |
Format-Table Name, PasswordRequired, PasswordExpires, PasswordChangeable
```

### Guest Account Investigation

```powershell
Get-LocalUser -Name Guest | Select * | tee usr-guest.txt
```

The Guest account was suspicious because:

```text
Enabled + No password required + Currently logged in → Deserves investigation
```

A Guest account existing alone isn't malicious — the **combination** is the concern.

### Important Lesson

> **Don't stop at the account name. Investigate the account's properties and activity.**

---

# 4. Investigate Group Membership

### Question

> What privileges do these accounts have?

```powershell
Get-LocalGroup | ForEach-Object {
    $members = Get-LocalGroupMember -Group $_.Name
    if ($members) {
        Write-Output "Group: $($_.Name)"
        $members | ForEach-Object {
            Write-Output "  Member: $($_.Name)"
        }
    }
} | tee gp-members.txt
```

### What This Accomplishes

```text
Local Group → Group Members → Account Privileges
```

This is much more useful than simply listing users.

### Why Groups Matter

```text
User: suspicious-user + Administrators group → Much more important than the username alone
```

Or:

```text
suspicious-user + Backup Operators → Has additional capabilities worth investigating
```

### Privilege Investigation Mindset

```text
Who is the user?
       ↓
What groups are they in?
       ↓
What privileges does that provide?
       ↓
Is that access expected?
       ↓
Who normally uses the account?
```

### Suspicious User vs Suspicious Privilege

```text
Unexpected user
       +
Administrator membership
       +
Recent/unknown activity
       +
Active session
= Much stronger finding
```

The more independent evidence you correlate, the stronger your conclusion.

---

# 5. Active Sessions

### Question

> Who is currently logged into the system?

```powershell
.\PsLoggedon64.exe | tee sessions.txt
```

Tool location: `C:\Users\Administrator\Desktop\tools\utils`

Uses Microsoft Sysinternals PsLoggedon utility.

### Why Sessions Matter

```text
User account   = Potential access
Active session = Current/ongoing access
```

If an attacker is currently connected, session information can provide an immediate lead.

### Lab Finding

Two local sessions found:
1. Administrator-like account (legitimate investigation session)
2. Guest (no password implemented) → particularly interesting

---

# 6. Building the Suspicion Chain

Don't investigate these separately:

```text
Guest exists    (alone = weak)
Guest has no password    (alone = weak)
Guest is logged in    (alone = weak)
```

Instead connect them:

```text
Guest account → Enabled → No password required → Currently logged in
        ↓
Unexpected session → Potential security concern
```

This is how you move from **enumeration** to **investigation**.

---

# 7. Don't Jump to Conclusions

You should **not** conclude:

> "This account is malicious because the username looks weird."

Instead:

```text
Suspicious indicator → Investigate account → Check privileges → Check session
        ↓
Check timestamps → Check other artefacts → Compare against baseline → Conclusion
```

Suspicious accounts and Guest sessions aren't sufficient by themselves to prove malicious activity.

---

# 8. Build a Full Account Profile

When you find a suspicious account, build a profile.

| Category    | Fields                                         |
| ----------- | ---------------------------------------------- |
| Identity    | Username, SID, Description                     |
| State       | Enabled, Password required, Expiry             |
| Privileges  | Administrators, Backup Operators, other groups |
| Activity    | Last logon, current sessions, related processes |
| Correlation | Other artefacts, network activity, persistence |

### Example Investigation Steps

```text
Step 1: Does the account legitimately exist?
Step 2: Is the spelling correct? (deliberate typo check)
Step 3: Is the account enabled?
Step 4: Does it belong to Administrators?
Step 5: Does it have an active session?
Step 6: When did it last log in?
Step 7: What other evidence is associated with it?
```

Now you've built an actual investigation, not just spotted a strange username.

---

# 9. Investigation Flow

```text
USERS
    ↓
Enumerate accounts → Identify anomalies
    ↓
Account details → Group membership → Privileges
    ↓
Current sessions → Correlate timestamps
    ↓
Compare with baseline → Normal / Suspicious
```

---

# Quick Revision

| Action                       | Command                                              |
| ---------------------------- | ---------------------------------------------------- |
| Find local users             | `Get-LocalUser`                                      |
| Investigate specific user    | `Get-LocalUser -Name <username> \| Select *`         |
| Find Administrators          | `Get-LocalGroupMember -Group "Administrators"`       |
| Enumerate all groups/members | `Get-LocalGroup`                                     |
| Find active sessions         | `.\PsLoggedon64.exe`                                 |
| Password properties          | `Get-CimInstance -Class Win32_UserAccount -Filter "LocalAccount=True"` |

---

# Evidence Files

| File                  | Contains                              |
| --------------------- | ------------------------------------- |
| `l-users.txt`         | All local user accounts               |
| `usr-guest.txt`       | Detailed Guest account information    |
| `usr-Administrator.txt`| Detailed Administrator info          |
| `gp-members.txt`      | Local group membership                |
| `sessions.txt`        | Current logon/session information     |

---

# What I Learned

- Enumerate Windows local users with `Get-LocalUser`
- Investigate individual account properties
- Identify suspicious usernames and account configurations
- Identify accounts with excessive privileges
- Map users to local groups with `Get-LocalGroup` and `Get-LocalGroupMember`
- Identify active user sessions using PsLoggedon
- Correlate account information with session information

### Most important lesson

> **A suspicious account becomes much more interesting when you can connect its identity, privileges, configuration, and activity.**

```text
WHO?           → Account
WHAT CAN THEY DO? → Groups / Privileges
ARE THEY USING IT? → Session
WHEN?          → Logon / timestamps
IS IT EXPECTED?   → Baseline + correlation
```

You're not just learning `Get-LocalUser`; you're learning how to **profile an account and determine why it deserves investigation**.
