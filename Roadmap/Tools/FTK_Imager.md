# 💾 FTK Imager: Complete Mastery Checklist

> **What is FTK Imager?** FTK Imager (Forensic Toolkit Imager) is a free disk imaging and evidence preservation tool from AccessData (now Exterro). It creates forensically sound images of hard drives, SSDs, USB drives, and memory. It is the most widely used acquisition tool in digital forensics — law enforcement, corporate investigators, and security researchers all rely on it for evidence-grade disk imaging.
>
> **Why does it exist?** Forensic investigations require evidence preservation before analysis. FTK Imager creates verified, bit-for-bit copies of storage media with hash verification, supporting multiple output formats (E01, DD, AD1) compatible with major forensic analysis tools (Autopsy, EnCase, FTK). It also performs live memory acquisition and can preview a drive's contents before committing to a full image.
>
> **When to use it:** Live acquisition from a running Windows system (disk + RAM). Creating forensic images for offline analysis with Autopsy or EnCase. Previewing file system contents of a suspect drive before imaging. Mounting forensic images as read-only drives for analysis. Converting between forensic image formats.
>
> **What mastering FTK Imager unlocks:** Evidence-grade acquisition workflow. Chain of custody documentation. Forensic image creation and verification. Foundation for Phase 7 Part 27 (Digital Forensics) field work.
>
> **Roadmap Phase:** Phase 7 Part 27 (Digital Forensics)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Core Concepts & Installation | 4 | 1–2 hours |
| 2 | Disk Image Acquisition | 5 | 2–4 hours |
| 3 | Memory Acquisition | 3 | 1–2 hours |
| 4 | Evidence Preview & File Export | 4 | 2–3 hours |
| 5 | Image Mounting & Format Conversion | 3 | 1–2 hours |
| 6 | Chain of Custody & Documentation | 3 | 1–2 hours |
| 7 | Practical Labs | 4 | 4–6 hours |
| | **Total** | **26** | **~12–21 hours** |

**Prerequisites:** Basic Windows administration. Understanding of disk structure (MBR, GPT, partitions). Phase 7 Part 27 Stage 1 completion recommended before field use.

---

# PHASE 1: CORE CONCEPTS & INSTALLATION

---

## 1.1 Core Forensic Concepts

- [ ] **Forensic Image vs Copy:** A forensic image is a bit-for-bit copy of an entire storage device — including deleted files, slack space, unallocated space, and partition metadata. A file copy (xcopy, robocopy) only copies allocated files. Forensic images preserve all of this.

- [ ] **Hash Verification:** FTK Imager calculates MD5 and SHA-1 (and optionally SHA-256) hashes of both the source media and the resulting image. If source hash = image hash, the image is a perfect forensic copy. Any difference indicates error or tampering.

- [ ] **Write Blocker Requirement:** FTK Imager does NOT write-block the source drive during acquisition. Always connect the source drive through a hardware write blocker (Tableau, WiebeTech, UFED) before imaging. Without a write blocker, any OS access to the drive modifies timestamps and changes the hash.

- [ ] **Image Formats:**
  - **E01 (Expert Witness Format):** Compressed, segmented, supports embedded metadata and case notes. Industry standard. Compatible with EnCase, Autopsy, FTK, X-Ways.
  - **DD / RAW:** Uncompressed bit-for-bit copy. Larger than E01 but universally compatible and simpler for scripting.
  - **AD1 (AccessData Custom Content Image):** Logical image of selected files/folders. Not a full disk image — lacks unallocated space.
  - **AFF (Advanced Forensic Format):** Open format with compression and metadata. Less common than E01.

- [ ] **Installation:** FTK Imager is Windows-only freeware. Download from [Exterro.com](https://www.exterro.com/ftk-product-suite/ftk-imager). For Linux/macOS disk imaging, use `dc3dd` or `ewfacquire` (part of libewf) as alternatives.

---

# PHASE 2: DISK IMAGE ACQUISITION

---

## 2.1 Creating a Forensic Image

- [ ] **Launch & Select Source:** File → Create Disk Image → Select source type:
  - **Physical Drive:** Images the entire physical disk (all partitions, MBR/GPT, unallocated space)
  - **Logical Drive:** Images a single partition/volume (faster, but misses unallocated space between partitions)
  - **Image File:** Converts an existing image to another format
  - **Folder:** Creates an AD1 logical image of a folder's contents

- [ ] **Image Destination Settings:** Add Image Destination → Select format (E01 recommended):
  - **Case Number, Evidence Number, Unique Description, Examiner, Notes:** Populate all fields — these are embedded in the image metadata and appear in Autopsy and EnCase case headers
  - **Image Fragment Size:** Default 1500 MB for E01. Adjust based on filesystem limitations of destination drive (FAT32 = 4 GB max, NTFS/exFAT = no practical limit)
  - **Compression:** 0–9. Compression 6 is a good balance — reduces storage 30–50% with minimal speed impact
  - **AD Encryption:** Optional — encrypts the E01. Required for chain of custody in sensitive cases.

- [ ] **Hash Verification Settings:** Verify images after they are created (MD5, SHA-1 or SHA-256). This adds time but is non-negotiable for forensic work. The verification run compares the image hash to the source hash — document both in chain of custody notes.

- [ ] **Start Imaging:** Click Start → Monitor progress. FTK Imager shows: elapsed time, estimated time remaining, MB/s transfer rate, and bad sector count. Bad sectors are logged — document any bad sectors in the chain of custody report.

- [ ] **Completion Report:** After imaging, FTK Imager displays the source hash and image hash side-by-side. Screenshot this display and save it with your case documentation. Any hash mismatch = acquisition failure — re-image.

---

## 2.2 Imaging Speed Optimization

- [ ] **USB 3.0/Thunderbolt Write Blocker:** Hardware write blocker transfer speed limits imaging rate. USB 3.0 write blockers reach ~130 MB/s, Thunderbolt write blockers reach ~400+ MB/s. For large drives (2+ TB), choose the fastest available interface.

- [ ] **Destination Drive Speed:** Destination drive must be faster than source read rate. Use a fast SSD destination or NAS over gigabit LAN for large acquisitions.

- [ ] **Bad Sector Handling:** By default FTK Imager retries bad sectors multiple times (slows acquisition significantly on damaged media). For speed, reduce retry count — but note: bad sector content is zeroed out in the image, which must be documented.

---

# PHASE 3: MEMORY ACQUISITION

---

```bash
# FTK Imager live RAM capture (must run as Administrator)
# File → Capture Memory → Select destination path → Include pagefile → Capture
```

- [ ] **Live Memory Capture:** File → Capture Memory. FTK Imager injects a driver (`FTKImager_Driver.sys`) to read physical RAM. Select destination path and filename. Check "Include pagefile" for complete memory capture — the pagefile (`pagefile.sys`) may contain memory pages swapped to disk.

- [ ] **Administrator Requirement:** Memory capture requires Administrator privileges. On domain-joined machines, use a domain admin account or local administrator account.

- [ ] **Memory Capture Caveats:** FTK Imager's memory capture modifies the running system (driver injection, file write to destination path). This is unavoidable in live acquisition. Document the acquisition in chain of custody notes. For investigations where zero system modification is critical, use `WinPmem` which has a smaller footprint.

- [ ] **Output Format:** FTK Imager produces `.mem` or `.ad1` format memory captures. Volatility 3 accepts `.mem` and raw `.dmp` files. If Volatility rejects the output, convert with `raw2dmp` (part of WinDbg) or re-acquire with WinPmem.

---

# PHASE 4: EVIDENCE PREVIEW & FILE EXPORT

---

- [ ] **Preview Without Full Image:** File → Add Evidence Item → Physical/Logical Drive → FTK Imager mounts a read-only view of the drive's file system. Browse directories, view file contents, and export specific files WITHOUT creating a full forensic image. Useful for quick triage.

- [ ] **File System Tree:** Once an evidence item is added, the left panel shows the file system tree with allocated and deleted file markers. Navigate to any directory and view file contents in the right panel (text, hex, or picture view).

- [ ] **Export Files:** Right-click any file or folder → Export Files → exports selected items. FTK Imager computes a hash for each exported file. This hash must be documented in chain of custody notes.

- [ ] **Export File List (Directory Listing):** File → Export Directory Listing → exports a CSV of all files with timestamps, sizes, MD5 hashes, and allocation status. This is extremely useful for building a file timeline and identifying suspicious files without manually browsing every directory.

---

# PHASE 5: IMAGE MOUNTING & FORMAT CONVERSION

---

- [ ] **Mount Image as Read-Only Drive:** File → Image Mounting → Browse to E01 or DD image → Mount as physical device or logical drive (read-only) → Image appears in Windows as a drive letter. This allows other Windows forensic tools (X-Ways, Registry Explorer, Timeline Explorer) to access the image without re-ingesting.

- [ ] **Format Conversion:** File → Create Disk Image → Source = Image File → Select existing image → Output in different format. Converts DD to E01, E01 to DD, etc. Hash verification runs on both source and destination.

- [ ] **Unmounting:** Always unmount images through FTK Imager (File → Image Mounting → Unmount) — do not just disconnect. Improper unmount can leave handles open.

---

# PHASE 6: CHAIN OF CUSTODY & DOCUMENTATION

---

- [ ] **Chain of Custody Document:** Every FTK Imager acquisition must be accompanied by a chain of custody document recording:
  - Case number and evidence number
  - Date and time of acquisition (start and end)
  - Investigator name and organization
  - Source device description (make, model, serial number, capacity)
  - Write blocker used (make, model, serial)
  - Source hash (MD5/SHA-256) from FTK Imager completion screen
  - Image hash (MD5/SHA-256) from FTK Imager verification screen
  - Image filename, format, and storage location
  - Any anomalies (bad sectors, acquisition interruptions)

- [ ] **Bad Sector Documentation:** If FTK Imager reports bad sectors, document: sector range, count, and the zero-fill behaviour. A forensic image with bad sectors is still admissible if properly documented.

- [ ] **Evidence Sticker / Label:** Physical media must be labelled with case number, evidence number, date of acquisition, and investigator initials. Photographed before and after acquisition. Store in anti-static bag in secure evidence locker.

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab Acquisition:** Image a USB drive or test VM hard disk to E01 format. Verify hashes match. Document the process as a chain of custody record.

- [ ] **Live Preview Lab:** Add a physical/logical drive as evidence item. Export the directory listing to CSV. Identify 5 files with suspicious timestamps (future dates, identical creation/modification times).

- [ ] **Memory Capture Lab:** Capture RAM from a running VM with FTK Imager. Verify the `.mem` file is accepted by Volatility 3 (`python3 vol.py -f memory.mem windows.pslist`). Compare output against the running VM's task manager.

- [ ] **Full DFIR Workflow Lab:** Acquire disk (FTK Imager E01) + memory (FTK Imager `.mem`) from a test VM → ingest disk into Autopsy → analyse memory with Volatility → correlate artifacts from both sources to reconstruct a simulated incident.

---

## 📝 Operational Notes

- **Always use a write blocker for physical drives** — FTK Imager does not write-block automatically.
- **E01 vs DD:** Use E01 for professional investigations (metadata, compression, case info embedded). Use DD for scripting and cross-platform compatibility.
- **FTK Imager Lite:** A portable version with no installation required — useful for field acquisition from a USB drive.
- **Pagefile capture:** Always capture `pagefile.sys` if possible — it may contain memory pages of interest not present in the RAM dump.
- **Large drives:** For 4 TB+ drives, E01 imaging at compression level 6 takes 8–12+ hours. Plan acquisition time accordingly.
- **Autopsy compatibility:** E01 files from FTK Imager import directly into Autopsy as evidence items with no conversion needed.
