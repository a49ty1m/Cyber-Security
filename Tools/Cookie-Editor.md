# 🍪 Cookie-Editor: Complete Reference

> **What is Cookie-Editor?** Cookie-Editor is a browser extension (Chrome, Firefox, Edge, Safari) that provides a clean GUI for viewing, editing, adding, deleting, importing, and exporting HTTP cookies for the current page. It eliminates the need to navigate browser DevTools to manipulate cookies during web application testing, making session hijacking tests, cookie attribute validation, and token-swapping operations faster and more accessible.
>
> **When to use it:** Testing session management: can you replace a session cookie with another user's? Testing cookie security attributes (HttpOnly, Secure, SameSite). Manual JWT or session token swap for authorization testing. Importing/exporting cookie sets between browsers for cross-account testing. Quick session fixation testing.
>
> **Tier 4 Reminder:** Cookie manipulation is built into browser DevTools and Burp Suite. Cookie-Editor is a convenience tool — know it exists, know the security attributes you're testing, and understand when it's faster than alternatives.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Cookie Security Fundamentals | 4 | 1–2 hours |
| 2 | Cookie-Editor Usage | 4 | 1–2 hours |
| 3 | Security Testing | 4 | 1–2 hours |
| 4 | Alternatives & Integration | 3 | 45 min |
| 5 | Mastery Check | 2 | 20 min |
| | **Total** | **17** | **~4–7 hours** |

---

# PHASE 1: COOKIE SECURITY FUNDAMENTALS

---

### Task 1.1 — What Cookies Are

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Definition** | Small key-value pairs stored by the browser, sent automatically with every HTTP request to the matching domain. Primary use: session management, user preferences, tracking. |
| **Cookie Attributes** | `Name=Value` — the data. `Domain` — which domain the cookie is sent to. `Path` — URL path scope. `Expires/Max-Age` — persistence. `Secure` — only send over HTTPS. `HttpOnly` — not accessible via JavaScript. `SameSite` — CSRF protection. |
| **Security Relevance** | Session cookies identify the user to the server. Stealing or modifying a session cookie = session hijacking. Missing security attributes = vulnerabilities. |

---

### Task 1.2 — Security Attribute Analysis

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **HttpOnly** | Cookie NOT readable by JavaScript (`document.cookie` returns nothing). Prevents XSS cookie theft. **Missing** = XSS can steal session. |
| **Secure** | Cookie ONLY sent over HTTPS. **Missing** = cookie transmitted in plaintext over HTTP → interceptable via MITM. |
| **SameSite** | `Strict`: never sent cross-site. `Lax`: sent on top-level navigations only. `None`: always sent (requires `Secure`). **Missing or None** = CSRF risk. |
| **Domain Scope** | `.example.com` (leading dot) = sent to all subdomains. `example.com` (no dot) = only that domain. Over-broad domain = cookie accessible to more subdomains than intended. |

---

### Task 1.3 — Session Cookie vs. Other Cookies

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Session Cookie** | No Expires or Max-Age — deleted when browser closes. Identifies the user's server session. Most security-sensitive cookie. |
| **Persistent Cookie** | Has Expires/Max-Age — survives browser close. Used for "remember me" tokens. |
| **Tracking/Analytics** | Third-party cookies from ad networks. Less security-sensitive for pentesting (unless scope includes tracking). |

---

### Task 1.4 — Cookie Theft Vectors

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **XSS** | If HttpOnly is missing: `document.cookie` in an XSS payload exfiltrates the session cookie. |
| **MITM** | If Secure is missing: MITM attacker reads cookie from HTTP traffic. |
| **Subdomain XSS** | If Domain is too broad (`.example.com`): XSS on `blog.example.com` steals cookies for `bank.example.com`. |
| **CSRF** | If SameSite is missing/None: an attacker's site can trigger authenticated requests using the victim's cookies. |

---

# PHASE 2: COOKIE-EDITOR USAGE

---

### Task 2.1 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 5 min

| Field | Detail |
|:---|:---|
| **Chrome/Edge** | Chrome Web Store → search "Cookie-Editor" by cgagnier → Install. |
| **Firefox** | Firefox Add-ons → Cookie-Editor → Add to Firefox. |
| **Access** | Click the Cookie-Editor extension icon in browser toolbar. Opens panel showing all cookies for the current domain. |

---

### Task 2.2 — Interface Overview

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Cookie List** | All cookies for the current domain listed. Click any cookie → expand → see all attributes (Name, Value, Domain, Path, Expires, Secure, HttpOnly, SameSite). |
| **Edit** | Click cookie → edit any field → Save. |
| **Add** | Plus (+) button → create new cookie with any attributes. |
| **Delete** | Trash icon on a cookie → delete that cookie. Delete All → remove all cookies for domain. |
| **Import/Export** | Import: paste JSON array of cookie objects. Export: copy all cookies as JSON. |

---

### Task 2.3 — Editing a Session Cookie

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Workflow** | Log in as User A → open Cookie-Editor → copy session cookie value. Log out (or open incognito). Log in as User B → open Cookie-Editor → replace session cookie value with User A's value. Refresh page → are you now User A? |
| **Use Case** | Testing session token acceptance (cookie reuse). Testing if session is tied to IP or browser fingerprint (some apps invalidate sessions on IP change). |

---

### Task 2.4 — Import/Export Cookies

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Export Format** | JSON array: `[{"name":"session","value":"abc123","domain":"target.com","path":"/","expires":-1,"httpOnly":true,"secure":true,"sameSite":"Lax"}]`. |
| **Cross-Browser Test** | Export cookies from Chrome → share with team member → Import into their Firefox. Both test with identical session state. |
| **Automated Testing** | Export session cookie → use in Burp Suite or curl: `curl -b "session=abc123" https://target.com/api`. |

---

# PHASE 3: SECURITY TESTING

---

### Task 3.1 — Attribute Audit

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Objective** | Check every cookie for missing security attributes. |
| **Check** | Open Cookie-Editor on every major page of the application (login, dashboard, admin, payment). For each cookie, verify: Secure = true (required for production HTTPS apps). HttpOnly = true (for session cookies). SameSite = Strict or Lax (not None unless justified). Expires = appropriate (session cookies should be session-scoped or short-lived). |
| **Report** | Document every missing attribute as a finding. Missing HttpOnly on session cookie = high severity if XSS exists. Missing Secure on any production cookie = medium severity. |

---

### Task 3.2 — Session Fixation Testing

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Vulnerability** | Session fixation: attacker sets a known session ID before login, victim logs in with it, attacker uses the now-authenticated session. |
| **Test** | Note session cookie value before login. Log in. Check Cookie-Editor: is the session cookie value the same after login? Same value = vulnerable (server didn't regenerate a new session on login). New value = protected. |
| **Fix** | Server must issue a new session ID on every successful authentication. |

---

### Task 3.3 — Cross-Account IDOR via Cookie

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Objective** | Test if session cookies grant access to other users' resources. |
| **Method** | User A: log in → export cookies via Cookie-Editor. User B: log in → delete cookies via Cookie-Editor → import User A's cookies → refresh. Does User B now have User A's session? Can User B access User A's data? |
| **Combine with Burp** | Proxy User B's requests through Burp. Replace session cookie with User A's in Burp Repeater. Test each user-specific endpoint. |

---

### Task 3.4 — JWT in Cookie Testing

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Identify JWT** | Session cookie that starts with `eyJ` = base64-encoded JWT header. Three dot-separated base64 sections = JWT. |
| **Decode** | Copy value → paste to `jwt.io` → see header and payload (claims). |
| **Modify** | Decode → modify claim (e.g., `"role":"user"` → `"role":"admin"`) → re-sign or attempt `alg:none` attack. Use jwt_tool for systematic attacks. Cookie-Editor: paste the modified JWT back into the cookie value field. |

---

# PHASE 4: ALTERNATIVES & INTEGRATION

---

### Task 4.1 — Browser DevTools vs. Cookie-Editor

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **DevTools** | F12 → Application → Cookies. Same functionality. Slower to access. No import/export. |
| **Cookie-Editor** | One click to open. Import/export (JSON). Cleaner UI for editing. No keyboard shortcut away but often faster for frequent cookie manipulation. |
| **Conclusion** | Cookie-Editor is a QoL improvement over DevTools for cookie manipulation. Same capabilities, faster workflow. |

---

### Task 4.2 — Burp Suite Cookie Management

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Burp Advantages** | Burp sees all cookies in transit (including HttpOnly — Cookie-Editor can't show HttpOnly cookies because JavaScript can't read them). Burp can modify cookies in every request via Proxy. |
| **HttpOnly Gap** | Cookie-Editor CANNOT show or edit HttpOnly cookies (by design — they're protected from JavaScript). Burp Proxy CAN intercept and modify them (it operates at the HTTP level, not JavaScript). |
| **Combined** | Cookie-Editor for non-HttpOnly cookie management. Burp for HttpOnly cookies and proxy-level manipulation. |

---

### Task 4.3 — Cookie-Editor in Automation

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Selenium/Puppeteer** | For automated cross-account testing: use Selenium to log in as User A → get cookies via `driver.get_cookies()` → set cookies in User B session. More reliable than manual Cookie-Editor for regression testing. |
| **curl** | Export cookies from Cookie-Editor → pass to curl: `curl -b "name=value; other=val" https://target.com`. |

---

# PHASE 5: MASTERY CHECK

---

### Task 5.1 — Competency Self-Assessment

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Competency | Self-Assessment |
|:---|:---:|
| Can explain all cookie security attributes and their purpose | ☐ |
| Can audit a web application's cookies for missing security flags | ☐ |
| Can replace one user's session cookie with another's | ☐ |
| Can test for session fixation using Cookie-Editor | ☐ |
| Knows that Cookie-Editor cannot access HttpOnly cookies | ☐ |
| Knows when to use Cookie-Editor vs. Burp Suite for cookie manipulation | ☐ |

---

### Task 5.2 — Interview Questions

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

1. What are the security attributes for HTTP cookies and what does each protect against?
2. What is the impact of a missing HttpOnly attribute on a session cookie?
3. What is session fixation and how do you test for it?
4. Why can't Cookie-Editor display HttpOnly cookies?
5. How would you use Cookie-Editor to test for cross-account session reuse?
6. When would you use Burp Suite instead of Cookie-Editor for cookie manipulation?
