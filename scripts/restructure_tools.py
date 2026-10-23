#!/usr/bin/env python3
"""
restructure_tools.py
--------------------
Restructures Obsidian Tools/ folder so every tool checklist lives in its own
sub-folder and gets a companion _Notes.md file.

Usage:
    python3 scripts/restructure_tools.py --dry-run   # preview only
    python3 scripts/restructure_tools.py             # execute
"""

import argparse
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

# ── Configuration ─────────────────────────────────────────────────────────────

VAULT_ROOT   = Path(__file__).resolve().parent.parent.parent   # MY_FOLDER/
GIT_ROOT     = Path(__file__).resolve().parent.parent           # Cyber-Security/
TOOLS_DIR    = GIT_ROOT / "Roadmap" / "Tools"
SKIP_FILES   = {"README.md"}

NOTES_TEMPLATE = """\
---
tool: {tool}
type: notes
---
# 📝 {tool} Notes

⬅️ [[{tool}|Back to checklist]]
"""

LINK_LINE_TEMPLATE = "📝 [[{tool}_Notes|Notes]]\n"


# ── Helpers ───────────────────────────────────────────────────────────────────

def log(msg):
    print(msg)


def find_tool_files(tools_dir):
    """Return all .md files in tools_dir (non-recursive) that are not in SKIP_FILES."""
    files = [
        f for f in tools_dir.iterdir()
        if f.is_file() and f.suffix == ".md" and f.name not in SKIP_FILES
    ]
    return sorted(files, key=lambda f: f.name.lower())


def has_frontmatter(content):
    return content.startswith("---\n") or content.startswith("---\r\n")


def find_h1_insert_index(lines):
    """
    Return the line index *after* the H1 (first # heading) line (0-indexed).
    If there is YAML frontmatter, skip past the closing --- first.
    Returns 0 if no H1 is found.
    """
    i = 0
    # Skip frontmatter block
    if lines and lines[0].rstrip() == "---":
        i = 1
        while i < len(lines) and lines[i].rstrip() not in ("---", "..."):
            i += 1
        i += 1  # skip closing ---

    # Now find first H1
    while i < len(lines):
        if lines[i].startswith("# "):
            return i + 1   # insert AFTER this line
        i += 1
    return 0


def insert_notes_link(content, tool):
    """
    Insert the Notes link line directly after the H1.
    Returns the new content, or None if link already present.
    """
    link_line = LINK_LINE_TEMPLATE.format(tool=tool)
    # Idempotency: already inserted?
    if "[[{}_Notes|Notes]]".format(tool) in content:
        return None

    lines = content.splitlines(keepends=True)
    insert_at = find_h1_insert_index(lines)

    # Insert a blank line + link line after H1
    lines.insert(insert_at, "\n")
    lines.insert(insert_at + 1, link_line)
    return "".join(lines)


def is_git_repo(path):
    result = subprocess.run(
        ["git", "-C", str(path), "rev-parse", "--is-inside-work-tree"],
        capture_output=True, text=True
    )
    return result.returncode == 0


def git_mv(src, dst, dry_run):
    """Run git mv src -> dst. Returns True on success."""
    if dry_run:
        log("   [DRY] git mv {} → {}".format(
            src.relative_to(GIT_ROOT), dst.relative_to(GIT_ROOT)))
        return True
    result = subprocess.run(
        ["git", "-C", str(GIT_ROOT), "mv",
         str(src.relative_to(GIT_ROOT)),
         str(dst.relative_to(GIT_ROOT))],
        capture_output=True, text=True
    )
    if result.returncode != 0:
        log("❌ git mv failed: {}".format(result.stderr.strip()))
        return False
    return True


# ── Wikilink scanner ──────────────────────────────────────────────────────────

WIKILINK_RE = re.compile(r'\[\[([^\]|#]+?)(?:[|#][^\]]*?)?\]\]')

def scan_wikilinks(vault_root):
    """
    Scan all .md files in the vault for wikilinks.
    Returns dict: link_target -> [(file_path, line_no), ...]
    """
    links = {}
    for md in vault_root.rglob("*.md"):
        if ".obsidian" in md.parts:
            continue
        try:
            text = md.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            for m in WIKILINK_RE.finditer(line):
                target = m.group(1).strip()
                links.setdefault(target, []).append((md, lineno))
    return links


def build_filename_index(vault_root):
    """Map every .md filename stem -> list of paths (to detect ambiguity)."""
    index = {}
    for md in vault_root.rglob("*.md"):
        if ".obsidian" in md.parts:
            continue
        index.setdefault(md.stem, []).append(md)
    return index


def check_link_integrity(vault_root, tool_stems, phase):
    """
    Check wikilink integrity for tool files.
    Returns a result dict.
    """
    print("\n" + "─"*60)
    print("🔍 Link integrity check — {}".format(phase))
    print("─"*60)

    all_links   = scan_wikilinks(vault_root)
    file_index  = build_filename_index(vault_root)

    # Only consider links whose target stem matches a tool stem
    tool_links = {}
    for target, occurrences in all_links.items():
        stem = Path(target).stem
        if stem in tool_stems:
            tool_links.setdefault(target, []).extend(occurrences)

    total_link_refs = sum(len(v) for v in tool_links.values())
    print("  Tool wikilink references found: {}".format(total_link_refs))

    broken = []
    for target, occurrences in tool_links.items():
        stem = Path(target).stem
        if stem not in file_index or len(file_index[stem]) == 0:
            broken.append((target, occurrences))

    ambiguous = []
    for stem in tool_stems:
        paths = file_index.get(stem, [])
        if len(paths) > 1:
            ambiguous.append((stem, paths))

    if broken:
        print("\n  ❌ BROKEN links ({}):".format(len(broken)))
        for target, occurrences in broken:
            for fpath, lineno in occurrences:
                print("     [[{}]] in {}:{}".format(
                    target, fpath.relative_to(vault_root), lineno))
    else:
        print("  ✅ No broken tool links")

    if ambiguous:
        print("\n  ⚠️  Ambiguous filenames ({}) — multiple files share the same stem:".format(len(ambiguous)))
        for stem, paths in ambiguous:
            for p in paths:
                print("     {}".format(p.relative_to(vault_root)))
    else:
        print("  ✅ No ambiguous tool filenames")

    return {
        "phase": phase,
        "total_link_refs": total_link_refs,
        "broken": broken,
        "ambiguous": ambiguous,
    }


# ── Safety pre-flight ─────────────────────────────────────────────────────────

def preflight(tool_files):
    """
    Abort if two files share the same stem, or a folder name would collide
    with an existing non-directory file.
    """
    stems = {}
    for f in tool_files:
        stems.setdefault(f.stem, []).append(f)

    ok = True
    for stem, paths in stems.items():
        if len(paths) > 1:
            print("❌ ABORT: duplicate stem '{}': {}".format(stem, [str(p) for p in paths]))
            ok = False

    for f in tool_files:
        folder = TOOLS_DIR / f.stem
        if folder.exists() and not folder.is_dir():
            print("❌ ABORT: '{}' exists as a FILE, not a directory.".format(folder))
            ok = False

    return ok


# ── Main restructure loop ─────────────────────────────────────────────────────

def restructure(dry_run):
    print("\n" + "═"*60)
    print("  Obsidian Tools Restructure — {}".format("DRY RUN" if dry_run else "LIVE RUN"))
    print("═"*60)
    print("  Vault root : {}".format(VAULT_ROOT))
    print("  Git root   : {}".format(GIT_ROOT))
    print("  Tools dir  : {}".format(TOOLS_DIR))

    use_git = is_git_repo(GIT_ROOT)
    print("  Git repo   : {}".format("yes — using git mv" if use_git else "no — using shutil.move"))

    tool_files = find_tool_files(TOOLS_DIR)
    print("  Tool files : {} (excluding {})".format(len(tool_files), ", ".join(SKIP_FILES)))

    if not preflight(tool_files):
        sys.exit(1)

    tool_stems = {f.stem for f in tool_files}

    # ── Pre-run link check ────────────────────────────────────────────────────
    pre_result = check_link_integrity(VAULT_ROOT, tool_stems, "BEFORE")
    if pre_result["broken"]:
        print("\n❌ Broken links detected BEFORE restructure. Fix these first. Aborting.")
        sys.exit(1)

    # ── Process each tool ─────────────────────────────────────────────────────
    print("\n" + "─"*60)
    print("  Processing tools…")
    print("─"*60)

    stats = {
        "folders_created": 0,
        "notes_created": 0,
        "checklists_moved": 0,
        "link_lines_inserted": 0,
        "skipped": [],
    }

    for tool_file in tool_files:
        tool = tool_file.stem
        tool_dir = TOOLS_DIR / tool
        dest_file = tool_dir / tool_file.name
        notes_file = tool_dir / "{}_Notes.md".format(tool)

        # ── Idempotency check ─────────────────────────────────────────────────
        already_moved = tool_dir.is_dir() and dest_file.exists()
        already_has_notes = notes_file.exists()

        if already_moved and already_has_notes:
            stats["skipped"].append((tool, "already complete"))
            print("⏭  {}: already complete — skipped".format(tool))
            continue

        print("\n📦 {}".format(tool))

        # ── Create folder ──────────────────────────────────────────────────────
        if not tool_dir.exists():
            if dry_run:
                print("   [DRY] mkdir {}".format(tool_dir.relative_to(GIT_ROOT)))
            else:
                tool_dir.mkdir(parents=True, exist_ok=True)
                print("   ✅ mkdir {}".format(tool_dir.relative_to(GIT_ROOT)))
            stats["folders_created"] += 1
        else:
            print("   ℹ️  dir exists: {}".format(tool_dir.relative_to(GIT_ROOT)))

        # ── Move checklist ─────────────────────────────────────────────────────
        if not already_moved:
            if use_git:
                success = git_mv(tool_file, dest_file, dry_run)
            else:
                if dry_run:
                    print("   [DRY] mv {} → {}".format(
                        tool_file.name, dest_file.relative_to(GIT_ROOT)))
                    success = True
                else:
                    shutil.move(str(tool_file), str(dest_file))
                    print("   ✅ mv {} → {}".format(
                        tool_file.name, dest_file.relative_to(GIT_ROOT)))
                    success = True
            if success:
                stats["checklists_moved"] += 1
        else:
            print("   ℹ️  checklist already in place")

        # ── Insert notes link into checklist ───────────────────────────────────
        read_path = tool_file if dry_run else dest_file
        if read_path.exists():
            content = read_path.read_text(encoding="utf-8")
            new_content = insert_notes_link(content, tool)
            if new_content is None:
                print("   ℹ️  notes link already present in checklist")
            else:
                if dry_run:
                    print("   [DRY] insert '📝 [[{}_Notes|Notes]]' after H1 in {}".format(
                        tool, tool_file.name))
                else:
                    dest_file.write_text(new_content, encoding="utf-8")
                    print("   ✅ inserted notes link after H1 in {}".format(tool_file.name))
                stats["link_lines_inserted"] += 1
        elif dry_run:
            print("   [DRY] would insert notes link after H1 in {}".format(tool_file.name))
            stats["link_lines_inserted"] += 1

        # ── Create Notes file ──────────────────────────────────────────────────
        if already_has_notes:
            print("   ℹ️  {}_Notes.md already exists — not overwriting".format(tool))
            stats["skipped"].append((tool, "{}_Notes.md already exists".format(tool)))
        else:
            notes_content = NOTES_TEMPLATE.format(tool=tool)
            if dry_run:
                print("   [DRY] create {}".format(notes_file.relative_to(GIT_ROOT)))
            else:
                notes_file.write_text(notes_content, encoding="utf-8")
                print("   ✅ created {}".format(notes_file.relative_to(GIT_ROOT)))
            stats["notes_created"] += 1

    # ── Post-run link check ───────────────────────────────────────────────────
    if not dry_run:
        post_result = check_link_integrity(VAULT_ROOT, tool_stems, "AFTER")
    else:
        post_result = None
        print("\n[DRY RUN] Skipping post-run link check (no files were changed).")

    # ── Summary ───────────────────────────────────────────────────────────────
    print("\n" + "═"*60)
    print("  Summary — {}".format("DRY RUN" if dry_run else "LIVE RUN"))
    print("═"*60)
    print("  Folders created     : {}".format(stats["folders_created"]))
    print("  Checklists moved    : {}".format(stats["checklists_moved"]))
    print("  Notes links inserted: {}".format(stats["link_lines_inserted"]))
    print("  Notes files created : {}".format(stats["notes_created"]))
    if stats["skipped"]:
        print("  Skipped ({}):".format(len(stats["skipped"])))
        for tool, reason in stats["skipped"]:
            print("    • {}: {}".format(tool, reason))

    if post_result:
        if post_result["broken"]:
            print("\n❌ BROKEN LINKS AFTER RESTRUCTURE — review before committing!")
        else:
            print("\n✅ All tool wikilinks resolve correctly after restructure.")
        if pre_result["total_link_refs"] != post_result["total_link_refs"]:
            print("⚠️  Link count changed: {} → {} (investigate)".format(
                pre_result["total_link_refs"], post_result["total_link_refs"]))
        else:
            print("✅ Link count stable: {} references before and after.".format(
                post_result["total_link_refs"]))


# ── Entry point ───────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Restructure Obsidian Tools/ folder.")
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Print every action without touching any file."
    )
    args = parser.parse_args()
    restructure(dry_run=args.dry_run)


if __name__ == "__main__":
    main()
