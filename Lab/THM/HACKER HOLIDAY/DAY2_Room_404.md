# Day 3 – Room 404

> _This room introduced me to something completely new: **exposed Git repositories**. I had never dealt with website dumps or Git leaks before, so this room definitely pushed me out of my comfort zone. I did take some help from YouTube to understand the workflow, but I made sure to follow each step and understand what was happening._

## Objective

Find the hidden flag from an exposed website source code.

## Initial Observation

The website looked... well, empty.

The only hint I had was:

- The **source code was exposed**.
- Find the hidden flag.

At first, I tried opening the website on my local machine, but it wouldn't load. So, I switched to the **TryHackMe AttackBox**, where the website opened without any issues.

## Investigation

I started by inspecting the website's source code.

There, I noticed a suspicious reference to a **`.git`** directory.

Trying to browse it manually didn't reveal much, so I followed a tutorial to understand how to investigate exposed Git repositories.

### Step 1 – Directory Enumeration (`dirb`)

I used **`dirb`**, a directory enumeration tool, to discover hidden paths on the web server.

It found an interesting endpoint:

```text
/.git/HEAD
```

That confirmed the server had an **exposed Git repository**.

### Step 2 – Dumping the Git Repository

Simply browsing the `.git` folder wasn't enough.

So I installed **Git Dumper** from GitHub and used it to download the exposed Git repository.

After dumping the repository, I recovered several project files, including:

- `index.html`
- `README.md`
- Other Git metadata

I opened the **README** file...

...and the flag was patiently waiting for me. 😄

## Flag

```text
THM{byt3_l0tus_n3v3r_f0rg3ts}
```

## New Tools I Learned

### `dirb`

- A **web content scanner** used to discover hidden files and directories on a web server.
- Useful for finding resources that aren't linked on the main website (e.g., admin panels, backups, `.git` folders).

### Git Dumper

- A tool used to **download an exposed `.git` repository** from a web server.
- Helps recover source code, commit history, and other files that developers accidentally leave publicly accessible.

## Key Takeaways

- An exposed **`.git` directory** can leak an entire website's source code.
- **`dirb`** helps discover hidden directories and files during web reconnaissance.
- **Git Dumper** can recover the contents of an exposed Git repository.
- Sometimes the flag isn't on the website itself—it's hidden in the project's source code.

> _This room introduced me to two completely new tools: **`dirb`** and **Git Dumper**. Right now, I only know enough to use them for this lab, not enough to explain them in depth. That's okay—I know they're important, and I'll revisit them properly when I study web application security. For now, I'm happy knowing **what** they do and **why** they were useful here._
