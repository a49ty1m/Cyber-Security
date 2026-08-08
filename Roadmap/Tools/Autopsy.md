# 🔬 Autopsy: Complete Mastery Checklist

> **What is Autopsy?** Autopsy is a free, open-source digital forensics platform and graphical front-end to The Sleuth Kit (TSK). It allows investigators to analyze disk images, file systems, and artifacts from Windows, Linux, macOS, Android, and iOS devices. It is the most widely used open-source forensic tool in law enforcement, incident response, and security research.
>
> **Why does it exist?** Commercial forensic tools (FTK, EnCase, X-Ways) cost thousands of dollars per seat. Autopsy provides a comparable workflow for free — with a module-based architecture, timeline analysis, keyword searching, hash filtering, and artifact extraction. It is extensively used in CTF forensics challenges and real investigations.
>
> **When to use it:** Disk image analysis after evidence collection. File recovery from formatted or damaged media. Timeline construction from file system metadata. Keyword and regex searching across all files. Artifact extraction (browser history, recent documents, USB device history, Windows Registry hives).
>
> **What mastering Autopsy unlocks:** Full disk forensic investigations. Evidence-grade artifact documentation. Chain of custody preservation. The foundation of Phase 7 Part 27 (Digital Forensics) work.
>
> **Roadmap Phase:** Phase 7 Part 27 (Digital Forensics)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals & Case Setup | 5 | 2–3 hours |
| 2 | File System Analysis | 5 | 3–4 hours |
| 3 | Artifact Extraction | 6 | 4–6 hours |
| 4 | Timeline Analysis | 4 | 3–4 hours |
| 5 | Keyword Search & Ingest Modules | 4 | 3–4 hours |
| 6 | Reporting & Evidence Handling | 4 | 2–3 hours |
| 7 | Practical Labs | 4 | 6–10 hours |
| | **Total** | **32** | **~23–34 hours** |

**Prerequisites:** Understanding of file systems (FAT32, NTFS, ext4). Familiarity with Windows artifacts (Registry, Event Logs, Prefetch). Phase 7 Part 27 Stage 1–2 completion recommended.

---

# PHASE 1: FUNDAMENTALS & CASE SETUP

---

## 1.1 Core Concepts

- [ ] **Forensic Soundness:** Understand what makes a forensic process legally defensible: evidence integrity (hash verification), chain of custody documentation, and non-modification of original evidence. Autopsy enforces this by working from images, not originals.

- [ ] **Evidence Types:** Know what Autopsy can ingest: raw disk images (`.img`, `.dd`), E01 (Expert Witness Format), L01 (logical image), virtual machine disk images (VMDK, VHD), local drives (read-only), and ZIP archives.

- [ ] **The Sleuth Kit Foundation:** Understand that Autopsy is a GUI layer over The Sleuth Kit (TSK) command-line tools. Knowing TSK commands (`mmls`, `fsstat`, `fls`, `icat`, `blkcat`) helps you understand what Autopsy is doing under the hood.

- [ ] **Hash Verification:** Before any analysis, verify the SHA-256 (or MD5) hash of your evidence image matches the acquisition hash. In Autopsy: Case → Data Source Hash. A mismatch means evidence tampering or corruption.

- [ ] **Write Blockers:** Understand that physical drives must be connected through hardware or software write blockers during acquisition. Autopsy does not substitute for a write blocker — it only works on images.

---

## 1.2 Case Setup

- [ ] **New Case Wizard:** Launch Autopsy → New Case → Set case name, case number, examiner name, organization. These populate report headers — use realistic values for professional documentation practice.

- [ ] **Add Data Source:** Add Image File → browse to your evidence `.dd` or `.E01` → Autopsy verifies image integrity and catalogues it. For multi-part E01 sets, add only the `.E01` (first segment).

- [ ] **Ingest Modules Selection:** On data source add, select ingest modules:
  - **Hash Lookup** (MD5/SHA-1 against NSRL known-good database)
  - **Recent Activity** (browser history, downloads, recent documents, installed programs)
  - **Keyword Search** (pre-configured lists: phone numbers, emails, credit cards — add custom lists)
  - **File Type Identification** (MIME type detection regardless of extension)

- [ ] **Multiple Data Sources:** Add multiple data sources to a single case — useful for correlating artifacts across a suspect's laptop drive and USB stick from the same investigation.

---

# PHASE 2: FILE SYSTEM ANALYSIS

---

- [ ] **Directory Tree Navigation:** Navigate allocated files, deleted entries, and unallocated space in the left panel tree.

- [ ] **Deleted File Recovery:** Navigate to `$OrphanFiles` (NTFS). Recover deleted files via right-click → Extract File(s). Recovery succeeds only if clusters have not been overwritten.

- [ ] **File Metadata Analysis:** Click any file → right panel shows: full path, size, MACB timestamps, inode number, MD5 hash, MIME type, and allocation status.

- [ ] **Unallocated Space Analysis:** Right-click a volume → Extract Unallocated Space → export for carving with `photorec` or `scalpel` outside Autopsy.

- [ ] **NTFS Journal (`$UsnJrnl`):** Navigate `$EXTEND\$UsnJrnl:$J` — contains a chronological record of file operations, critical for timeline reconstruction even when file entries are deleted.

---

# PHASE 3: ARTIFACT EXTRACTION

---

- [ ] **Results Tree:** All ingest module findings appear under Results → Extracted Content. Key nodes: Web History, Web Downloads, Web Cookies, Recent Documents, Operating System User Accounts, Installed Programs, Devices Attached, Shell Bags.

- [ ] **Shell Bags (`UsrClass.dat`):** Prove a user browsed a specific folder even if the folder contents are deleted. For detailed analysis use `SBECmd`.

- [ ] **USB History (Devices Attached):** Results → Extracted Content → Devices Attached shows: first connect timestamp, last connect timestamp, device serial number, and friendly name.

- [ ] **Email Artifacts:** Autopsy parses Outlook PST/OST and Thunderbird MBOX files. Results → Extracted Content → Email Messages.

- [ ] **Prefetch Files (`C:\Windows\Prefetch\`):** Each `.pf` file proves a program was executed — last execution time, run count, files accessed.

- [ ] **LNK Files & Jump Lists:** Located in `%APPDATA%\Microsoft\Windows\Recent\`. LNK files contain the original file path, volume serial number, and MAC timestamps of the target — proving a user accessed a file even if the file was deleted.

---

# PHASE 4: TIMELINE ANALYSIS

---

- [ ] **Timeline Interface:** Tools → Timeline. Displays file system events as a horizontal time chart. Zoom to incident window and identify clusters of unusual activity.

- [ ] **MACB Timestamps:** Understand Modified (content changed), Accessed (file read), Changed (MFT metadata changed), Born (created). Each tells a different story.

- [ ] **Timestomping Detection:** Compare `$STANDARD_INFORMATION` vs `$FILE_NAME` timestamps in Autopsy. Discrepancies indicate timestomping — `$FILE_NAME` is harder to manipulate from userland.

- [ ] **Correlating Events:** Reconstruct the sequence: malware drop → first execution (Prefetch) → registry persistence creation → lateral movement → data staging → exfiltration. Annotate pivot points in your report.

---

# PHASE 5: KEYWORD SEARCH & HASH FILTERING

---

- [ ] **Custom Keyword Lists:** Tools → Keyword Lists → Create investigation-specific lists (domain names, usernames, filenames, IP addresses). Run keyword search retroactively without re-ingesting.

- [ ] **Regex Search:** Use regex for credit cards, IP addresses, Windows paths, and custom patterns relevant to your investigation.

- [ ] **NSRL Known-Good Filtering:** Hash Lookup module marks OS/software files as "known" — filter these to focus on investigator-relevant files.

- [ ] **Custom Hash Sets:** Add known malware or contraband hashes via Tools → Hash Sets → Import Hash Set. Autopsy flags matches during ingest.

---

# PHASE 6: REPORTING & EVIDENCE HANDLING

---

- [ ] **HTML Report:** Generate → Results → HTML Report → Self-contained report with all tagged artifacts and metadata. Suitable for case documentation.

- [ ] **Tagging System:** Right-click any file or artifact → Add Tag → Notable Item, Follow Up, or custom tag. Tag everything intended for the report during analysis.

- [ ] **TSV/CSV Export:** Export artifact tables for SIEM import or spreadsheet analysis.

- [ ] **Chain of Custody Notes:** Document: evidence acquisition method, hash values (acquisition + verification), analysis start/end timestamps, investigator name, Autopsy version, any image anomalies.

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **CTF Forensics Lab:** Complete a CyberDefenders forensics challenge (e.g., "Insider Threat") end-to-end: ingest → modules → artifact review → keyword search → timeline → report.

- [ ] **Deleted File Recovery Lab:** Create a test file in a VM, delete it, image with `dd`, ingest into Autopsy, recover and verify hash integrity.

- [ ] **USB Artifact Lab:** Connect/disconnect a USB in a test Windows VM, image, and reconstruct: device identity, connection timestamps, files accessed.

- [ ] **Timeline Reconstruction Lab:** Using an HTB Sherlock or CyberDefenders disk image, reconstruct attacker activity using only Autopsy's timeline module. Write a 1-page investigation narrative with evidence citations.

---

## 📝 Operational Notes

- **Timezone awareness:** Always verify the evidence system's timezone. Configure under Case Properties — Autopsy uses your local timezone by default.
- **Large image performance:** Disable unnecessary ingest modules for images over 500 GB. NSRL hash lookup is slow without a cached database.
- **Autopsy vs. CLI:** For scripted/automated analysis, use TSK CLI tools (`fls`, `icat`, `tsk_recover`) directly. Autopsy is a GUI wrapper.
- **Complementary tools:** Autopsy for disk analysis → Volatility for memory → Wireshark for network PCAPs. A complete DFIR investigation uses all three.
- **Evidence export integrity:** Always hash extracted files and document the hash. The extracted copy's hash must match Autopsy's stored inode hash.
