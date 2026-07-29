# The Game - TryHackMe

## Room Description

> Cipher has gone dark, but intel reveals he's hiding critical secrets inside **Tetris**, a popular video game. Hack it and uncover the encrypted data buried in its code.

When I read this description, my first thought was:

> **"Wait... how? 🤔"**

How can a game hide secrets? Let's find out.

---

# Initial Enumeration

The challenge provided a ZIP file containing the executable.

First things first...

```bash
unzip Tetrix.exe-1741979048280.zip
```

Now I wanted to know what kind of file I was dealing with.

```bash
file Tetrix.exe
```

Output:

```text
Tetrix.exe: PE32+ executable for MS Windows 5.02 (GUI), x86-64 (stripped to external PDB), 13 sections
```

So...

Yep, **obviously it's a Windows executable (binary)**.

---

# Looking for Easy Wins 👀

Whenever I get a binary, one of the first things I check is whether it contains readable strings.

```bash
strings Tetrix.exe
```

Sadly...

Nothing useful.

Well... that would've been too easy anyway.

---

# Time to Dig Deeper

Since `strings` wasn't helping, I remembered something I learned while solving the **Bandit** challenges on **OverTheWire**.

Let's inspect the binary in hexadecimal.

```bash
hexdump -C Tetrix.exe
```

The output was...

**Massive.**

Thousands of lines.

Definitely not something I wanted to read line by line.

Then I had an idea.

---

# Searching for the THM Flag Format

Most TryHackMe flags begin with:

```text
THM{
```

So why not search for "THM" directly?

```bash
hexdump -C Tetrix.exe | grep "THM"
```

Output:

```text
041567f0 55 52 45 5f 41 52 49 54 48 4d 45 54 49 43 00 2c |URE_ARITHMETIC.,|
042502c0 4c 4f 47 41 52 49 54 48 4d 49 43 00 41 54 54 45 |LOGARITHMIC.ATTE|
043906f0 49 4e 47 5f 41 4c 47 4f 52 49 54 48 4d 5f 41 53 |ING_ALGORITHM_AS|
050cf1b0 24 09 1d 2d 34 50 54 48 4d 4d 12 c4 a4 40 53 92 |$..-4PTHMM...@S.|
058b1590 0b 00 00 00 05 00 00 00 17 00 00 00 54 48 4d 7b |............THM{|
```

That **last line** instantly got me excited.

> Wait...
>
> That's `THM{` 👀

Now I just needed to see what came after it.

---

# Learning Something New

I didn't actually know how to display lines around a match using `grep`.

So...

I opened the manual page.

(Yes, sometimes reading the manual actually pays off 😂.)

I learned about:

- `-A` → Show lines **After** the match
- `-B` → Show lines **Before** the match
- `-C` → Show lines **Before and After**

Exactly what I needed.

---

# Getting More Context

```bash
hexdump -C Tetrix.exe | grep -A 5 "THM"
```

Eventually I reached:

```text
058b1590 0b 00 00 00 05 00 00 00 17 00 00 00 54 48 4d 7b |............THM{|
058b15a0 49 5f 43 41 4e 5f 52 45 41 44 5f 49 54 5f 41 4c |I_CAN_READ_IT_AL|
058b15b0 4c 7d 00 04 00 00 00 00 00 40 42 04 00 00 00 00 |L}.......@B.....|
058b15c0 c0 9e 43 04 00 00 00 00 00 af 43 04 00 00 00 00 |..C.......C.....|
058b15d0 40 bf 43 18 00 00 00 02 00 00 00 0c 00 00 00 05 |@.C.............|
058b15e0 00 00 00 0a 00 00 00 47 41 4d 45 20 4f 56 45 52 |.......GAME OVER|
```

There it was.

The flag was sitting right inside the binary.

---

# 🎉 Flag

```text
THM{I_CAN_READ_IT_ALL}
```

**Hurray!** 🥳

---

# What I Learned

This room wasn't really about hacking the game.

It was about understanding that **compiled binaries can still contain readable data**.

A few key takeaways:

- Always perform basic enumeration first.
- `strings` is a quick win, but it won't always find what you're looking for.
- `hexdump` lets you inspect the raw contents of a binary.
- `grep` can save you from manually searching thousands of lines.
- Reading the manual (`man grep`) is sometimes faster than searching the internet.
- Never assume compiled applications don't contain secrets.

---

# My Thought Process

```
Download file
        ↓
Identify file type
        ↓
Try strings
        ↓
No useful output
        ↓
Inspect with hexdump
        ↓
Too much data
        ↓
Search for "THM"
        ↓
Found THM{
        ↓
Need more context
        ↓
Learned grep -A
        ↓
Recovered the full flag
```

---

## Final Thoughts

This was a fun beginner-friendly reverse engineering room.

The coolest part wasn't finding the flag...

It was realising that something I learned in **Bandit (OverTheWire)** came in handy here. That's one of the best feelings while learning cybersecurity—connecting concepts from different platforms.

And yes...

Sometimes the answer isn't a fancy exploit.

Sometimes it's just knowing **which command to use and when.** 😄
