# Networking — Notes & Labs (Simple README)

A minimal, practical README for storing your networking notes from Forouzan and video lectures, plus lab writeups and tools. Keep it short and focused.

## Purpose

* Capture short book notes, video takeaways, and lab evidence (pcaps, scripts).
* Provide an easy structure so you can find and share learning artifacts quickly.

## How to use

1. Read 4–5 pages/day from Forouzan and add a short note file under `book/forouzan/`.
2. Watch lecture videos and save notes under `videos/`.
3. After reading/watching, run a short lab and save writeups in `labs/writeups/` and pcaps in `labs/pcaps/`.
4. Save scripts and automation under `tools/scripts/` and scan outputs under `tools/nmap/`.

## Minimal repo structure

```
networking/
├─ book/forouzan/
├─ videos/
├─ labs/
│  ├─ writeups/
│  └─ pcaps/
├─ tools/
│  ├─ nmap/
│  └─ scripts/
└─ README.md
```

## Quick templates

* Book note: `chapter-XX-pg-YY.md` (title, date, 3 bullet takeaways)
* Video note: `<source>-<topic>-YYYYMMDD.md` (key points, action to try)
* Lab writeup: `lab-name-YYYYMMDD.md` (objective, commands, findings, reflection)

## Safety & privacy

* Only add artifacts from your isolated lab. Do NOT include real credentials or data from live systems.

## Next steps

* Add today's Forouzan note and a short lab writeup.
* Keep commits small and descriptive.

---

Happy hacking — keep it legal, keep it clean.
