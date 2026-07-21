# 🩸 BloodHound: Complete Mastery Checklist

> **What is BloodHound?** BloodHound is a graph-based Active Directory reconnaissance and attack path analysis tool. It maps relationships between AD objects — users, groups, computers, GPOs, ACLs, sessions, trusts — and uses graph theory to reveal hidden attack paths that would be invisible through manual enumeration.
>
> **Why does it exist?** Active Directory environments contain thousands of objects with complex relationships. A user may be a member of a group that has GenericWrite on another group that has DCSync rights on the domain — this three-hop path is invisible to manual enumeration but trivial for BloodHound to find. BloodHound makes the invisible visible.
>
> **When to use it:** Every Active Directory penetration test. After gaining any domain credentials (even low-privilege). During internal network assessments. For identifying attack paths to Domain Admin. For identifying high-value targets and misconfigurations. For AD security posture assessment (defensive).
>
> **When to avoid it:** Non-Windows/non-AD environments. External assessments without internal access. When stealth is critical (data collection is detectable). When you only need simple enumeration (use CrackMapExec for quick checks).
>
> **What mastering BloodHound unlocks:** The ability to find attack paths that no amount of manual enumeration would reveal. OSCP/OSEP/CRTP exam readiness. Understanding of AD security at a deep level. Both offensive AND defensive AD analysis skills. Career differentiation — BloodHound proficiency is highly valued.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md) · [🐧 Metasploitable 2 Lab](../Lab/Metasploitable_2/TASK_LIST.md) · [🌐 OWASP BWA Lab](../Lab/OWASP_Broken_WebApps/TASK_LIST.md)

| Recon & Scanning | Exploitation | Post-Exploitation | Web & Traffic |
|:-----------------|:-------------|:-------------------|:--------------|
| [🗺️ Nmap](Nmap.md) | [💀 Metasploit](Metasploit_Framework.md) | [🐉 LinPEAS](LinPEAS.md) | [🕷️ Burp Suite](Burp_Suite.md) |
| [🔌 Netcat](Netcat.md) | [🐍 Impacket](Impacket.md) | **🩸 BloodHound** (you are here) | [🦈 Wireshark](Wireshark.md) |
| | [🔓 Hydra](Hydra.md) | [🔥 Hashcat](Hashcat.md) | |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & AD Graph Theory | 6 | 3–4 hours |
| 2 | Core Data Collection & Import | 7 | 5–7 hours |
| 3 | Intermediate (Queries & Analysis) | 7 | 5–7 hours |
| 4 | Advanced (Custom Queries, Edge Abuse) | 5 | 5–7 hours |
| 5 | Tool Integration | 4 | 2–4 hours |
| 6 | Practical Labs | 4 | 6–10 hours |
| 7 | Methodology & Defensive Usage | 4 | 3–4 hours |
| 8 | Mastery Challenges | 3 | 4–6 hours |
| | **Total** | **40** | **~33–49 hours** |

**Prerequisites:** Active Directory fundamentals (domains, forests, trusts, groups, GPOs). Understanding of Kerberos and NTLM authentication. Domain user credentials (any privilege level). A Windows AD lab environment.

**Editions:** **BloodHound CE (Community Edition)** — latest version with a web UI, Docker deployment, and API. **BloodHound Legacy** — original Electron app with Neo4j backend. This guide covers both but emphasizes CE as the current standard.

**Alternatives:** PingCastle (AD security audit, automated report), PlumHound (BloodHound data reporting), ADRecon (AD enumeration report), Purple Knight (AD security assessment), Adalanche (open-source AD visualization).

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Why Graph-Based AD Analysis Matters

- [ ] **Completed** · ⭐ Beginner · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand why graph databases reveal attack paths that flat enumeration tools (like net commands, PowerView, or ldapsearch) cannot. AD is a graph of relationships — users belong to groups, groups have permissions on objects, computers have sessions, trusts connect domains. Attack paths follow these relationships. |
| **Skills Learned** | Graph theory basics (nodes, edges, paths), why relationship-based analysis is superior for AD security, the concept of "transitive permissions" (Group A → member of Group B → has permissions on Object C), shortest path algorithms applied to AD attacks. |
| **Practical Exercise** | Draw a simple AD graph: 5 users, 3 groups, 2 computers, 1 domain. Add membership edges, session edges, admin edges. Trace a path from a low-privilege user to Domain Admin. Count how many "hops" it takes. |
| **Expected Output** | Understanding that AD attack paths are GRAPH problems, not flat enumeration problems. The shortest path from "compromised user" to "Domain Admin" is BloodHound's core value. |
| **Common Mistakes** | Thinking BloodHound is just another enumeration tool (it's a GRAPH ANALYSIS tool — the visualization is the product, not just data collection). Not understanding that attack paths can be 5-10 hops long and invisible to manual analysis. |

---

### Task 1.2 — BloodHound Architecture

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the three-component architecture: (1) **Collectors** (SharpHound, BloodHound.py) gather AD data from the environment. (2) **Database** (Neo4j for Legacy, PostgreSQL for CE) stores the graph. (3) **UI** (Electron app for Legacy, Web UI for CE) visualizes and queries the graph. |
| **Skills Learned** | Component roles, data flow (Collector → JSON/ZIP → Database → UI), why each component exists, CE vs Legacy architecture differences. |
| **Practical Exercise** | Draw the architecture: SharpHound runs on domain-joined machine → produces ZIP file → uploaded to BloodHound → stored in database → queried through UI. |
| **Expected Output** | Architecture diagram with data flow. Understanding that the collector and UI are SEPARATE — you collect data in the target environment and analyze it on your machine. |
| **Common Mistakes** | Running BloodHound itself on the target (only the COLLECTOR runs on the target — BloodHound UI runs on your attack machine). Confusing SharpHound (Windows collector, .NET) with BloodHound.py (Python collector, runs from Linux). |

---

### Task 1.3 — BloodHound CE Installation (Docker)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Install BloodHound Community Edition using Docker Compose. CE is the current recommended version with a modern web interface, API access, and PostgreSQL backend. |
| **Practical Exercise** | `curl -L https://ghst.ly/getbhce | docker compose -f - up` (official one-liner). Access UI at `http://localhost:8080`. Find the initial admin password in the Docker logs: `docker compose logs | grep "Initial Password"`. Log in and change the password. |
| **Expected Output** | BloodHound CE running in Docker. Web UI accessible. Admin account configured. |
| **Common Mistakes** | Not having Docker/Docker Compose installed. Not checking logs for the initial password. Port 8080 already in use (change in docker-compose). Not allocating enough memory to Docker (BloodHound CE needs ~4GB minimum). |

---

### Task 1.4 — BloodHound Legacy Installation (Neo4j)

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Install BloodHound Legacy (Electron app + Neo4j) as a fallback and for environments where CE isn't available. Many tutorials and resources still reference Legacy. |
| **Practical Exercise** | Install Neo4j: `sudo apt install neo4j`. Start: `sudo neo4j start`. Access Neo4j at `http://localhost:7474` → change default password (neo4j:neo4j). Install BloodHound: `sudo apt install bloodhound` or download from GitHub releases. Launch: `bloodhound` → connect to Neo4j (`bolt://localhost:7687`). |
| **Expected Output** | Neo4j running. BloodHound Legacy connected to the database. Empty graph ready for data import. |
| **Common Mistakes** | Not changing Neo4j's default password (BloodHound won't connect). Java version incompatibility with Neo4j (Neo4j 4.x needs Java 11). Not starting Neo4j before launching BloodHound. Port conflicts with other services. |

---

### Task 1.5 — Understanding AD Objects as Graph Nodes

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the AD objects that become graph nodes in BloodHound: **Users**, **Groups**, **Computers**, **Domains**, **GPOs**, **OUs** (Organizational Units), **Containers**. Each has properties (SID, description, last logon, admin count, password last set, etc.). |
| **Key Node Types** | **User:** Domain accounts — target for credential attacks. **Group:** Permission containers — membership grants permissions transitively. **Computer:** Domain-joined machines — targets for lateral movement. **Domain:** The AD domain itself — target for dominance. **GPO:** Group Policy Objects — modification = control over OU members. **OU:** Organizational Unit — GPO application scope. |
| **Expected Output** | Understanding of each node type and its significance in attack paths. |

---

### Task 1.6 — Understanding AD Relationships as Graph Edges

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand the relationship types (edges) that connect nodes in BloodHound. These edges ARE the attack paths — each edge represents a way to move from one object to another. |
| **Key Edge Types** | **MemberOf:** User/Group is a member of a Group (transitive permissions). **AdminTo:** User/Group has local admin on a Computer. **HasSession:** Computer has an active session from a User (credential harvesting). **CanRDP:** User/Group can RDP to a Computer. **GenericAll:** Full control over an object (reset password, modify group membership). **GenericWrite:** Can write to object properties (modify SPN for Kerberoasting, write to msDS-AllowedToActOnBehalfOfOtherIdentity for RBCD). **WriteDACL:** Can modify the object's ACL (grant yourself GenericAll). **WriteOwner:** Can change the object's owner (then modify DACL). **ForceChangePassword:** Can reset a user's password without knowing the current one. **AddMember:** Can add members to a group. **DCSync:** Has DS-Replication permissions (can dump all domain hashes). **GPLink:** GPO is linked to an OU. **Contains:** OU contains an object. **TrustedBy:** Domain trust relationship. |
| **Expected Output** | Complete edge type reference. Understanding that each edge type represents a specific abuse technique. Ability to read a BloodHound path and explain each hop's exploitation method. |
| **Common Mistakes** | Not understanding transitive group membership (User → Group A → Group B → Group C; if Group C has GenericAll on Domain, the User indirectly has it too). Ignoring edges that seem "minor" like WriteDACL (it's actually extremely powerful — modify the ACL to grant yourself any permission). |

---

# PHASE 2: DATA COLLECTION & IMPORT

---

### Task 2.1 — SharpHound: Windows Data Collection

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Run SharpHound (the Windows/.NET collector) from a domain-joined machine to gather ALL AD data: users, groups, computers, sessions, ACLs, trusts, GPOs, OUs. |
| **Syntax** | Executable: `.\SharpHound.exe -c All`. PowerShell: `Import-Module .\SharpHound.ps1; Invoke-BloodHound -CollectionMethod All`. Output: `*_BloodHound.zip` file containing JSON data files. Collection methods: `All`, `Default`, `Session`, `ACL`, `Group`, `Trusts`, `ObjectProps`, `Container`, `GPOLocalGroup`. |
| **Real-World Scenario** | You have any domain user credentials. Run SharpHound to collect the entire AD graph. Even as a low-privilege user, you can enumerate most AD objects because AD is readable by all authenticated users by default. |
| **Expected Output** | ZIP file containing comprehensive AD data. Understanding that SharpHound needs to run from a domain-joined Windows machine (or with domain credentials). |
| **Common Mistakes** | Not collecting `All` (missing ACLs or sessions means missing attack paths). Running SharpHound without domain credentials (it needs at least a domain user). Not understanding that SharpHound queries LDAP and SMB — it generates network traffic that may be detected. AV flagging SharpHound (use obfuscated versions or AMSI bypass). |

---

### Task 2.2 — BloodHound.py: Linux-Based Collection

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Collect AD data from Linux using `bloodhound-python` (the Python-based collector). This is the standard collection method when you're attacking from a Kali/Linux machine. |
| **Syntax** | `bloodhound-python -u user -p 'password' -d domain.local -ns <DC-IP> -c All`. With hash: `bloodhound-python -u user --hashes :NTLM -d domain.local -ns <DC-IP> -c All`. Output: JSON files in the current directory. |
| **Real-World Scenario** | You've obtained domain credentials through Kerberoasting or credential stuffing. Run bloodhound-python from your Kali machine — no need to touch a Windows machine. |
| **Expected Output** | JSON files ready for import into BloodHound. Understanding that bloodhound-python queries the same LDAP/SMB data as SharpHound but from Linux. |
| **Common Mistakes** | DNS resolution failures (use `-ns <DC-IP>` to specify the DC as DNS server, or add the DC to `/etc/resolv.conf`). Not specifying the domain correctly (FQDN: `domain.local`, not just `domain`). Missing data compared to SharpHound (bloodhound-python may not collect all edge types — session collection is limited). |

---

### Task 2.3 — Data Import into BloodHound CE

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Import collected data (ZIP or JSON files) into BloodHound CE through the web UI or API. |
| **Practical Exercise** | BloodHound CE: Click upload icon → select ZIP file → wait for ingestion. Verify: search for a known user → check that relationships appear. API upload: `curl -X POST http://localhost:8080/api/v2/file-upload -F 'file=@data.zip' -H 'Authorization: Bearer <token>'`. |
| **Expected Output** | Data ingested into BloodHound. Graph populated with AD objects and relationships. Search returning results. |
| **Common Mistakes** | Uploading incompatible data format (CE expects CE-format JSON; Legacy expects Legacy-format). Not waiting for ingestion to complete (large environments take minutes). Not verifying the import (search for known objects to confirm). |

---

### Task 2.4 — Data Import into BloodHound Legacy

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Import data into BloodHound Legacy via the Electron app's drag-and-drop interface. |
| **Practical Exercise** | Launch BloodHound → connect to Neo4j → drag and drop the ZIP file onto the BloodHound window. Watch the import progress bar. Verify: search for "Domain Admins" → check member count. |
| **Expected Output** | Data imported into Neo4j. Graph queryable through the BloodHound UI. |
| **Common Mistakes** | Neo4j not running (must start it before launching BloodHound). Importing old data on top of new data (clear database first: Database Info → Clear Database). Memory issues with large datasets (increase Neo4j heap size in neo4j.conf). |

---

### Task 2.5 — Collection Method Deep Dive

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Understand each collection method and when to use subsets instead of `All`: `Session` (who is logged in where — most volatile), `ACL` (permissions — most attack paths come from here), `Group` (memberships), `Trusts` (domain trust relationships), `GPOLocalGroup` (GPO-defined local admins). |
| **When to Use Subsets** | **Stealth:** Collect `Group` and `ACL` only (less noisy than session collection). **Re-collection:** Run `Session` periodically (sessions change constantly — new sessions = new attack paths). **Large environments:** Split collection into chunks to avoid timeouts. |
| **Expected Output** | Understanding of each collection method's data source, noise level, and value. Strategy for targeted collection in stealth-sensitive environments. |
| **Common Mistakes** | Only collecting once (sessions are volatile — run session collection multiple times during an engagement). Using `All` when `Default` is sufficient for initial analysis. Not understanding that ACL collection is the most valuable (most attack paths come from misconfigured ACLs). |

---

### Task 2.6 — Stealth Collection Techniques

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Minimize detection during data collection: reduce LDAP query volume, avoid session enumeration (SMB-heavy), use specific collection methods, and understand what triggers alerts. |
| **Detection Indicators** | High-volume LDAP queries from a single source. SMB connections to many workstations (session enumeration). Unusual access to SYSVOL (GPO collection). SPN queries (part of Kerberoasting detection). |
| **Stealth Options** | SharpHound: `--Stealth` flag (only collects from DCs, avoids workstation contact). Specific methods: `-c Group,ACL,Trusts` (skip sessions). Jitter: `--RandomDelay <ms>` (add random delays between queries). |
| **Expected Output** | Reduced-footprint data collection strategy. Understanding of the detection/completeness trade-off. |

---

### Task 2.7 — Data Validation & Freshness

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Validate imported data for completeness and understand data freshness: session data goes stale within hours, but group memberships and ACLs change less frequently. |
| **Practical Exercise** | After import: check node counts (Users, Computers, Groups). Compare with expected counts (`net group "Domain Users" /domain` should roughly match). Check session data timestamp. Re-collect sessions after 24 hours and re-import. |
| **Expected Output** | Validated data with known completeness. Strategy for session re-collection during multi-day engagements. |

---

# PHASE 3: QUERIES & ANALYSIS

---

### Task 3.1 — Built-In Queries: Shortest Path to Domain Admin

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use BloodHound's pre-built queries to find the most common attack paths. The most important query: "Shortest Paths to Domain Admins from Owned Principals." |
| **Key Built-In Queries** | "Find all Domain Admins" → shows DA group members. "Shortest Paths to Domain Admins" → shows ALL paths from ANY user to DA. "Shortest Paths to Domain Admins from Owned Principals" → shows paths from users you've compromised. "Find Principals with DCSync Rights" → direct path to domain compromise. "Find Computers where Domain Users are Local Admin" → easy lateral movement. "Shortest Paths to High Value Targets" → paths to all high-value objects. |
| **Practical Exercise** | Run each built-in query. For each result, read the path from left to right — each edge is an exploitation step. Document the shortest path you find. |
| **Expected Output** | Attack paths identified. Understanding that each edge in the path represents a specific exploitation technique. The shortest path = your attack plan. |
| **Common Mistakes** | Not marking owned principals (BloodHound needs to know which users you've compromised to calculate paths from them — right-click → "Mark as Owned"). Running queries before marking owned users (results are generic instead of personalized). Not reading the path edge-by-edge (each edge is a step you must execute). |

---

### Task 3.2 — Marking Owned Principals & High-Value Targets

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Mark compromised users/computers as "Owned" and critical targets as "High Value." This enables personalized attack path queries and prioritizes your analysis. |
| **Practical Exercise** | Right-click a user you've compromised → "Mark as Owned." Right-click a critical server → "Mark as High Value" (DCs, file servers, database servers are auto-marked). Run "Shortest Paths from Owned Principals to High Value Targets." |
| **Expected Output** | Personalized attack paths from YOUR compromised accounts to YOUR targets. |
| **Common Mistakes** | Forgetting to mark owned principals (most powerful queries require it). Not marking enough high-value targets (add application servers, database servers, PAW stations). Not updating owned status as you compromise more accounts during the engagement. |

---

### Task 3.3 — Node Information Analysis

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Click on any node to see its detailed properties and relationships. This panel reveals everything BloodHound knows about an object — critically important information for exploitation. |
| **Key Properties (User)** | Display Name, SID, Enabled, Last Logon, Password Last Set, AdminCount, ServicePrincipalNames (Kerberoastable?), "Do not require Kerberos preauthentication" (AS-REP Roastable?), Group Memberships, Local Admin Rights, Sessions, Outbound Control (objects this user can abuse), Inbound Control (who can abuse this user). |
| **Key Properties (Computer)** | OS, OS Version, Enabled, Unconstraineddelegation, Local Admins, Sessions, Outbound/Inbound Control. |
| **Expected Output** | Ability to extract actionable intelligence from any node's properties. Identification of Kerberoastable accounts, AS-REP Roastable accounts, and stale/disabled accounts. |

---

### Task 3.4 — Path Analysis: Reading Attack Chains

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Read BloodHound paths end-to-end and translate each edge into a concrete exploitation step. Each hop in the path requires a specific tool and technique. |
| **Edge-to-Exploitation Mapping** | **MemberOf** → group membership (no exploitation needed — you inherit the group's permissions). **AdminTo** → use psexec/wmiexec for remote execution, harvest credentials. **HasSession** → compromise the computer → harvest the logged-in user's credentials (Mimikatz). **GenericAll on User** → reset the user's password: `net user <user> NewPass123 /domain`. **GenericAll on Group** → add yourself to the group: `net group "<group>" <your-user> /add /domain`. **GenericWrite** → modify SPN for Kerberoasting OR modify msDS-AllowedToActOnBehalfOfOtherIdentity for RBCD. **WriteDACL** → grant yourself GenericAll, then abuse it. **WriteOwner** → take ownership, then modify DACL, then abuse. **ForceChangePassword** → reset password without knowing current. **AddMember** → add yourself or a controlled user to the group. **DCSync** → run secretsdump.py to extract all domain hashes. |
| **Practical Exercise** | For a BloodHound path of 4+ hops, write out each step: "Step 1: I have user X. Step 2: User X is MemberOf Group Y. Step 3: Group Y has GenericAll on User Z. I will reset Z's password. Step 4: User Z is AdminTo Computer W. I will psexec to W. Step 5: Computer W has a session from Domain Admin. I will dump credentials from W." |
| **Expected Output** | Complete exploitation plan derived from a BloodHound path. Understanding that every edge is a concrete, executable step. |
| **Common Mistakes** | Seeing a path but not knowing how to exploit each edge (learn the exploitation technique for every edge type). Not realizing that HasSession requires compromising the COMPUTER to harvest the USER's credentials. Not understanding transitive group membership (you may need to trace through multiple MemberOf edges). |

---

### Task 3.5 — Kerberoastable & AS-REP Roastable Account Identification

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Use BloodHound to identify accounts vulnerable to Kerberoasting (have SPNs) and AS-REP Roasting (pre-auth disabled). These are often quick wins for credential access. |
| **Practical Exercise** | Query: "List all Kerberoastable Accounts." Check each account's group memberships — prioritize those in privileged groups. Query: "List all AS-REP Roastable Users." Cross-reference with Impacket: `impacket-GetUserSPNs` and `impacket-GetNPUsers`. |
| **Expected Output** | List of Kerberoastable accounts prioritized by privilege level. AS-REP Roastable accounts identified. Attack plan for each. |

---

### Task 3.6 — Session-Based Attack Paths

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Exploit "HasSession" edges: if a high-value user has a session on a computer you can admin, you can harvest their credentials from that computer. |
| **Attack Chain** | BloodHound shows: Domain Admin "HasSession" on SERVER01 → You have AdminTo on SERVER01 → psexec to SERVER01 → run Mimikatz → extract DA credentials → DCSync. |
| **Expected Output** | Session-based attack paths identified and prioritized. Understanding that session data is volatile — re-collect frequently. |
| **Common Mistakes** | Not re-collecting sessions (a DA might log in to a server you can admin TOMORROW — today's data won't show it). Not understanding that HasSession means you need to compromise the COMPUTER to get the USER's credentials. |

---

### Task 3.7 — Group Delegation & Trust Analysis

- [ ] **Completed** · ⭐⭐⭐⭐ Intermediate-Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Analyze domain trust relationships, unconstrained/constrained delegation, and resource-based constrained delegation (RBCD) opportunities identified by BloodHound. |
| **Key Queries** | "Find Computers with Unconstrained Delegation" → compromise these to capture TGTs. "Find all users with constrained delegation" → delegation abuse. "Map Domain Trusts" → identify cross-domain attack paths. |
| **Expected Output** | Delegation targets identified. Trust relationships mapped. Cross-domain attack paths documented. |

---

# PHASE 4: ADVANCED ANALYSIS

---

### Task 4.1 — Custom Cypher Queries (Legacy/Neo4j)

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 40 min

| Field | Detail |
|:---|:---|
| **Objective** | Write custom Cypher queries for Neo4j (BloodHound Legacy) to find specific attack paths, misconfigurations, and patterns not covered by built-in queries. |
| **Key Cypher Queries** | All DA sessions: `MATCH (c:Computer)-[:HasSession]->(u:User) WHERE u.admincount=true RETURN u.name, c.name`. Kerberoastable admins: `MATCH (u:User {hasspn:true, admincount:true}) RETURN u.name, u.serviceprincipalnames`. Users with DCSync: `MATCH (u)-[:MemberOf*1..]->(g:Group)-[:DCSync|GetChanges|GetChangesAll*1..]->(d:Domain) RETURN u.name`. Shortest path from owned to DA: `MATCH p=shortestPath((u:User {owned:true})-[*1..]->(g:Group {name:"DOMAIN ADMINS@DOMAIN.LOCAL"})) RETURN p`. Computers where Domain Users are local admin: `MATCH (g:Group {name:"DOMAIN USERS@DOMAIN.LOCAL"})-[:AdminTo]->(c:Computer) RETURN c.name`. |
| **Expected Output** | Custom queries answering specific engagement questions. Ability to extend BloodHound's analysis beyond built-in queries. |
| **Common Mistakes** | Wrong syntax (Cypher is case-sensitive for labels, properties use lowercase). Not escaping domain names properly. Queries returning too many results (add LIMIT). Not using `shortestPath` when you want efficient pathfinding. |

---

### Task 4.2 — ACL Abuse Chains

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 35 min

| Field | Detail |
|:---|:---|
| **Objective** | Identify and exploit complex ACL-based attack chains where multiple permission abuses are chained together. These multi-hop ACL paths are BloodHound's most powerful findings. |
| **Example Chain** | User A → WriteDACL on Group B → grant GenericAll → add User A to Group B → Group B has GenericAll on User C (service account) → Kerberoast User C → crack password → User C is AdminTo Server D → psexec → Server D has session from Domain Admin → Mimikatz → DCSync. |
| **Tools for Each Step** | WriteDACL: `PowerView: Add-DomainObjectAcl`. AddMember: `net group "GroupB" UserA /add /domain`. GenericAll on User: `net user UserC NewPass /domain`. Kerberoast: `impacket-GetUserSPNs`. Psexec: `impacket-psexec`. Mimikatz: `sekurlsa::logonpasswords`. DCSync: `impacket-secretsdump`. |
| **Expected Output** | Multi-step ACL abuse chains identified and mapped to specific tools. Understanding that ACL misconfigurations are the most common and most powerful attack vectors in real AD environments. |

---

### Task 4.3 — GPO Abuse Analysis

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Objective** | Identify GPOs that can be modified (WriteDACL, GenericWrite, GenericAll) and the OUs they're linked to. Modifying a GPO lets you push malicious configurations (scheduled tasks, startup scripts, registry keys) to every computer and user in the linked OU. |
| **Query (Cypher)** | `MATCH (u:User)-[r:GenericAll|GenericWrite|WriteDACL]->(g:GPO)-[:GpLink]->(ou:OU) RETURN u.name, g.name, ou.name`. |
| **Expected Output** | Modifiable GPOs identified with their scope (which OUs/computers they affect). Understanding that GPO abuse = code execution on every machine in the OU. |

---

### Task 4.4 — Cross-Domain & Forest Trust Analysis

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Analyze trust relationships between domains and forests. Identify attack paths that cross trust boundaries — compromising one domain to pivot into another. |
| **Key Concepts** | Intra-forest trusts (bidirectional by default, SID history abuse possible). External trusts (one-way or two-way, SID filtering may apply). Forest trusts (limited trust, SID filtering enforced). |
| **Expected Output** | Trust relationship map. Cross-domain attack paths identified. Understanding of SID filtering and its bypasses. |

---

### Task 4.5 — Defensive BloodHound: Identifying & Remediating Weaknesses

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| Field | Detail |
|:---|:---|
| **Objective** | Use BloodHound from a defensive perspective: identify the most critical misconfigurations and provide remediation recommendations. This is how blue teams and AD admins should use BloodHound. |
| **Key Defensive Queries** | Count of users with paths to DA → prioritize remediation. Identify "choke points" — edges that appear in many attack paths (removing one edge breaks many paths). Find over-privileged service accounts. Identify stale admin sessions (DAs logged into workstations). Find computers with unconstrained delegation (shouldn't be on workstations). |
| **Expected Output** | Prioritized remediation recommendations. Understanding that removing ONE critical edge can break dozens of attack paths. |

---

# PHASE 5: TOOL INTEGRATION

---

### Task 5.1 — Impacket → BloodHound → Impacket Pipeline

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| **Workflow** | Impacket credentials (Kerberoast/secretsdump) → mark owned in BloodHound → find attack path → Impacket executes each path step (psexec, wmiexec, secretsdump) → mark new owned → find next path → repeat until Domain Admin. |

---

### Task 5.2 — CrackMapExec + BloodHound

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Workflow** | CrackMapExec validates credentials across multiple hosts → mark owned in BloodHound → BloodHound finds paths → CrackMapExec executes lateral movement. CrackMapExec can also export BloodHound-compatible data. |

---

### Task 5.3 — BloodHound + Hashcat Pipeline

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 15 min

| **Workflow** | BloodHound identifies Kerberoastable accounts → Impacket GetUserSPNs extracts hashes → Hashcat cracks them → mark cracked accounts as owned in BloodHound → new attack paths appear. |

---

### Task 5.4 — BloodHound + Metasploit Pipeline

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| **Workflow** | BloodHound identifies AdminTo paths → Metasploit psexec for exploitation → Meterpreter for credential harvesting → mark newly compromised accounts as owned → re-analyze paths. |

---

# PHASE 6–8: LABS, METHODOLOGY & MASTERY

---

### Lab 6.1 — Beginner: First Data Collection & Import

- [ ] **Completed** · ⭐⭐ Beginner · ⏱️ 60 min

| **Scenario** | Set up BloodHound (CE or Legacy). Collect data from an AD lab with bloodhound-python or SharpHound. Import data. Run all built-in queries. |
| **Success Criteria** | Data imported successfully. All built-in queries executed. At least one attack path identified. |

---

### Lab 6.2 — Intermediate: Path-Guided Attack

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 120 min

| **Scenario** | Use BloodHound to find the shortest path from a low-privilege user to Domain Admin. Execute every step in the path using the appropriate tools. |
| **Success Criteria** | Complete path executed. Domain Admin achieved by following BloodHound's guidance. Each step documented with tool used and evidence. |

---

### Lab 6.3 — Advanced: Multi-Path Analysis

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 120 min

| **Scenario** | Find and execute THREE different paths to Domain Admin in the same environment. Compare paths by: number of hops, tools required, stealth level, and difficulty. |
| **Success Criteria** | Three distinct attack paths documented and compared. At least one path using ACL abuse. Recommendation for which path a real attacker would choose. |

---

### Lab 6.4 — Expert: Defensive Assessment

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 180 min

| **Scenario** | Perform a defensive BloodHound assessment: import data, find all attack paths, identify the top 10 misconfigurations, and produce a prioritized remediation report for the AD administrator. |
| **Success Criteria** | Top 10 findings with CVSS-like severity. Remediation steps for each finding. "Choke point" analysis showing which single fixes break the most paths. Executive summary suitable for management. |

---

### Task 7.1 — BloodHound in the Pentest Lifecycle

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| **Objective** | Map BloodHound to PTES: Reconnaissance (AD enumeration via collectors), Vulnerability Analysis (attack path identification), Exploitation (path-guided exploitation), Reporting (graph-based evidence). BloodHound transforms AD pentesting from "try everything" to "follow the path." |

---

### Task 7.2 — BloodHound Limitations

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 10 min

| **Key Limitations** | Only works with Active Directory (not Azure AD natively — use AzureHound for cloud). Collection is detectable (LDAP queries, SMB session enumeration). Session data goes stale quickly. Doesn't identify all edge types (some custom applications create unlisted permissions). Doesn't exploit anything (analysis only — you execute the attacks). Large environments may have performance issues. |

---

### Task 7.3 — OPSEC for Data Collection

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 15 min

| **Key Points** | SharpHound triggers AV/EDR (obfuscate or use bloodhound-python). Session collection touches every workstation (noisy). LDAP queries are logged on DCs (Event ID 1644 if enabled). Use `--Stealth` for reduced footprint. Time your collection during business hours (blends with normal LDAP traffic). |

---

### Task 7.4 — Reporting with BloodHound Data

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Export BloodHound attack paths as screenshots and data for professional penetration test reports. Create clear, visual representations of attack chains that non-technical stakeholders can understand. |
| **Tools** | Screenshot attack paths directly from BloodHound UI. Use PlumHound for automated reporting from BloodHound data. Export custom Cypher queries as CSV for spreadsheet analysis. Create Mermaid diagrams from path data for markdown reports. |
| **Expected Output** | Professional report section with visual attack paths, step-by-step exploitation narrative, and remediation recommendations. |

---

### Challenge 8.1 — Blind AD Assessment

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 180 min

| **Scenario** | Given only a set of low-privilege domain credentials and a DC IP, perform a complete AD assessment: collect data, identify all attack paths, execute the most efficient path to DA, and produce a professional report. |

---

### Challenge 8.2 — Custom Query Library

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 120 min

| **Scenario** | Build a library of 20+ custom Cypher queries covering: delegation abuse, GPO abuse, certificate attacks, tier model violations, stale admin sessions, service account risks, and trust abuse. Document each query with its purpose and expected results. |

---

### Challenge 8.3 — Teach BloodHound

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 60 min

| **Scenario** | Prepare a 25-minute BloodHound workshop: AD graph theory, collection, import, built-in queries, reading attack paths, edge-to-exploitation mapping. Live demo showing a path from low-priv to DA with tools executing each step. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can install and configure BloodHound (CE and Legacy) | ☐ |
| Can collect AD data with SharpHound and bloodhound-python | ☐ |
| Can import data and run built-in queries | ☐ |
| Can mark owned principals and find personalized attack paths | ☐ |
| Can read attack paths and map each edge to an exploitation technique | ☐ |
| Can write custom Cypher queries for Neo4j | ☐ |
| Can identify and exploit ACL abuse chains | ☐ |
| Can analyze delegation, trusts, and GPO attack surfaces | ☐ |
| Can use BloodHound defensively for remediation recommendations | ☐ |
| Can integrate BloodHound with Impacket, Hashcat, and CrackMapExec | ☐ |
| Can produce professional reports with BloodHound evidence | ☐ |
| Can teach BloodHound to another person | ☐ |

---

## 🎯 Interview Questions

1. What is BloodHound and why is graph-based analysis superior for AD security?
2. What is the difference between SharpHound and BloodHound.py?
3. Explain the concept of "edges" in BloodHound and name five edge types with their exploitation techniques.
4. How does the "Shortest Path to Domain Admins" query work?
5. What is the difference between GenericAll, GenericWrite, and WriteDACL?
6. How do you exploit a HasSession edge?
7. What is a multi-hop ACL abuse chain? Give an example.
8. How would you use BloodHound defensively to prioritize AD hardening?
9. What are the OPSEC considerations for running SharpHound?
10. How do you identify "choke points" — single fixes that break the most attack paths?
