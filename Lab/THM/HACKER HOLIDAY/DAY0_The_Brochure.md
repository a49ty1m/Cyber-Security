# Day 0 – The Brochure (Warm-up)

> _My first step into the **Hackers Holiday** series—and honestly, a nice introduction to OSINT. I was pretty new to reconnaissance, so I didn't really know what to look for or where to find information. But that's part of the fun. I'll learn as I go._

## Objective

Use **OSINT (Open-Source Intelligence)** to gather publicly available information and uncover the hidden flag.

## Initial Observation

The challenge started with a landing page for **Byte Lotus Resort**, which included:

- Flashy promotional content
- Plenty of positive reviews
- An AI assistant named **Vera**, who seemed to help guests with everything

After downloading the **brochure**, the real investigation began.

## The Hint

The brochure looked like a normal resort advertisement, but one line immediately stood out:

> **"Find us on Instagram."**

That caught my attention because **Instagram was the only social media platform mentioned**. It felt less like marketing and more like a deliberate OSINT clue.

## Investigation

- Searched for **Byte Lotus Resort** on Instagram.
- Found the official resort account.
- Noticed it was following **only one account**: **Vera**.

_Whenever something is oddly specific in a CTF, it's usually worth investigating._

## Finding the Clue

Vera's profile contained **three strange strings of text**.

My first thought:

> _"These definitely don't look random... probably encoded."_

I copied all three strings and searched for an online decoder.

Turns out they were **Base64-encoded**.

After decoding them, I recovered the flag:

```text
THM{V3r@s_aCC0unt_h4s_b33n_f0und!}
```

## Key Takeaways

- **OSINT** is all about collecting information from publicly available sources.
- Small hints (like mentioning only one social media platform) can guide the entire investigation.
- If you encounter strange-looking text during a CTF, always consider common encodings like **Base64** before assuming it's encryption.

> _A simple but enjoyable warm-up. It gave me my first real taste of OSINT and showed me that sometimes the biggest clue is hiding in plain sight._
