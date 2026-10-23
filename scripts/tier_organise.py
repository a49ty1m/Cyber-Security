#!/usr/bin/env python3
"""
tier_organise.py
----------------
Moves each Tools/<Tool>/ folder into Tools/Tier-N_<Label>/<Tool>/
based on the tier tables in Tools/README.md.

Usage:
    python3 scripts/tier_organise.py --dry-run
    python3 scripts/tier_organise.py
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

# ── Config ────────────────────────────────────────────────────────────────────

GIT_ROOT  = Path(__file__).resolve().parent.parent   # Cyber-Security/
TOOLS_DIR = GIT_ROOT / "Roadmap" / "Tools"

# Tier folder names — must match the README headings (in order)
TIER_FOLDERS = {
    1: "Tier-1_Core",
    2: "Tier-2_Frequent",
    3: "Tier-3_Situational",
    4: "Tier-4_Niche",
}

# ── Parse README for tier membership ─────────────────────────────────────────

TIER_HEADING_RE = re.compile(r'^## Tier (\d+)', re.MULTILINE)
WIKILINK_RE     = re.compile(r'\[\[([^\]|#\\]+?)(?:[\\|#][^\]]*?)?\]\]')

def parse_tier_map(readme_path: Path) -> dict[str, int]:
    """
    Returns {tool_stem: tier_number} by scanning the README tier tables.
    Tool stem is the first segment of the wikilink target, e.g. 'Nmap' from [[Nmap|...]].
    """
    text = readme_path.read_text(encoding="utf-8")

    # Split on tier headings
    parts = TIER_HEADING_RE.split(text)
    # parts = [preamble, '1', tier1_body, '2', tier2_body, ...]

    tier_map: dict[str, int] = {}
    i = 1
    while i < len(parts) - 1:
        tier_num = int(parts[i])
        body     = parts[i + 1]

        # Stop at next major section that isn't a tier
        # (body may contain the next tier heading but we split on it already)
        for m in WIKILINK_RE.finditer(body):
            stem = m.group(1).strip()
            # wikilinks in tier tables are bare stems like "Nmap" or "Burp_Suite"
            # some may have path prefixes — take just the last segment
            stem = stem.split("/")[-1]
            if stem and stem not in tier_map:
                tier_map[stem] = tier_num
        i += 2

    return tier_map


# ── Git helpers ───────────────────────────────────────────────────────────────

def is_git_repo(path: Path) -> bool:
    r = subprocess.run(
        ["git", "-C", str(path), "rev-parse", "--is-inside-work-tree"],
        capture_output=True, text=True
    )
    return r.returncode == 0


def git_mv(src: Path, dst: Path, dry_run: bool) -> bool:
    rel_src = src.relative_to(GIT_ROOT)
    rel_dst = dst.relative_to(GIT_ROOT)
    if dry_run:
        print(f"   [DRY] git mv {rel_src} → {rel_dst}")
        return True
    r = subprocess.run(
        ["git", "-C", str(GIT_ROOT), "mv", str(rel_src), str(rel_dst)],
        capture_output=True, text=True
    )
    if r.returncode != 0:
        print(f"❌ git mv failed: {r.stderr.strip()}")
        return False
    print(f"   ✅ git mv {rel_src} → {rel_dst}")
    return True


# ── Main ──────────────────────────────────────────────────────────────────────

def run(dry_run: bool):
    print(f"\n{'═'*60}")
    print(f"  Tier Organiser — {'DRY RUN' if dry_run else 'LIVE RUN'}")
    print(f"{'═'*60}")

    readme = TOOLS_DIR / "README.md"
    if not readme.exists():
        print("❌ README.md not found in Tools/"); sys.exit(1)

    tier_map = parse_tier_map(readme)
    print(f"  Tools parsed from README: {len(tier_map)}")

    use_git = is_git_repo(GIT_ROOT)
    print(f"  Git repo: {'yes — using git mv' if use_git else 'no — using shutil'}\n")

    stats = dict(moved=0, skipped=[], errors=[])

    # Collect all tool folders currently sitting directly inside TOOLS_DIR
    tool_dirs = sorted(
        [d for d in TOOLS_DIR.iterdir() if d.is_dir() and not d.name.startswith("Tier-")],
        key=lambda d: d.name.lower()
    )

    # Safety: check every tool folder has a tier assignment
    unmapped = [d.name for d in tool_dirs if d.name not in tier_map]
    if unmapped:
        print("⚠️  These tool folders have NO tier assignment in README and will be SKIPPED:")
        for u in unmapped:
            print(f"   • {u}")
        print()

    for tool_dir in tool_dirs:
        tool = tool_dir.name

        if tool not in tier_map:
            stats["skipped"].append((tool, "not in README tier tables"))
            continue

        tier_num    = tier_map[tool]
        tier_folder = TOOLS_DIR / TIER_FOLDERS[tier_num]
        dest        = tier_folder / tool

        # Idempotency
        if dest.exists():
            stats["skipped"].append((tool, f"already in {TIER_FOLDERS[tier_num]}"))
            print(f"⏭  {tool} → already in {TIER_FOLDERS[tier_num]}, skipped")
            continue

        print(f"\n📦 {tool}  →  {TIER_FOLDERS[tier_num]}/")

        # Create tier folder
        if not tier_folder.exists():
            if dry_run:
                print(f"   [DRY] mkdir {tier_folder.relative_to(GIT_ROOT)}")
            else:
                tier_folder.mkdir(parents=True, exist_ok=True)
                print(f"   ✅ mkdir {tier_folder.relative_to(GIT_ROOT)}")

        # Move
        ok = git_mv(tool_dir, dest, dry_run) if use_git else _plain_mv(tool_dir, dest, dry_run)
        if ok:
            stats["moved"] += 1
        else:
            stats["errors"].append(tool)

    # ── Update Structure Convention in README ─────────────────────────────────
    _update_readme_convention(readme, dry_run)

    # ── Summary ───────────────────────────────────────────────────────────────
    print(f"\n{'═'*60}")
    print(f"  Summary — {'DRY RUN' if dry_run else 'LIVE RUN'}")
    print(f"{'═'*60}")
    print(f"  Folders moved : {stats['moved']}")
    if stats["skipped"]:
        print(f"  Skipped ({len(stats['skipped'])}):")
        for t, r in stats["skipped"]:
            print(f"    • {t}: {r}")
    if stats["errors"]:
        print(f"  ❌ Errors ({len(stats['errors'])}): {', '.join(stats['errors'])}")
    else:
        print("  ✅ No errors.")

    if dry_run:
        print("\n  Run without --dry-run to apply changes.")


def _plain_mv(src: Path, dst: Path, dry_run: bool) -> bool:
    import shutil
    if dry_run:
        print(f"   [DRY] mv {src.relative_to(GIT_ROOT)} → {dst.relative_to(GIT_ROOT)}")
    else:
        shutil.move(str(src), str(dst))
        print(f"   ✅ mv {src.relative_to(GIT_ROOT)} → {dst.relative_to(GIT_ROOT)}")
    return True


def _update_readme_convention(readme: Path, dry_run: bool):
    """Replace the Structure Convention code block with the new tiered layout."""
    old_block = """\
```
Tools/
├── README.md
└── <Tool>/
    ├── <Tool>.md          ← checklist (curriculum tasks, competency matrix, interview Qs)
    └── <Tool>_Notes.md    ← my personal notes (never regenerated, never overwritten)
```"""
    new_block = """\
```
Tools/
├── README.md
├── Tier-1_Core/
│   └── <Tool>/
│       ├── <Tool>.md          ← checklist
│       └── <Tool>_Notes.md    ← personal notes
├── Tier-2_Frequent/
├── Tier-3_Situational/
└── Tier-4_Niche/
```"""
    text = readme.read_text(encoding="utf-8")
    if old_block not in text:
        print("\n  ℹ️  README structure block already updated or not found — skipping.")
        return
    new_text = text.replace(old_block, new_block, 1)
    if dry_run:
        print("\n  [DRY] update Structure Convention block in README.md")
    else:
        readme.write_text(new_text, encoding="utf-8")
        print("\n  ✅ Updated Structure Convention block in README.md")


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    p = argparse.ArgumentParser(description="Organise Tools/ into Tier sub-folders.")
    p.add_argument("--dry-run", action="store_true")
    args = p.parse_args()
    run(dry_run=args.dry_run)

if __name__ == "__main__":
    main()
