# 🎣 GoPhish: Complete Mastery Checklist

> **What is GoPhish?** GoPhish is an open-source phishing framework that lets you run complete phishing campaigns — create email templates, design landing pages (credential capture portals), manage target lists, send campaign emails, and track results (who opened, who clicked, who submitted credentials) — all through a web UI. It is the industry standard free phishing simulation platform.
>
> **Why does it exist?** Running phishing simulations manually requires coordinating multiple tools and tracking results by hand. GoPhish integrates everything: email sending (via SMTP relay), landing page hosting, real-time tracking, and campaign analytics — in one platform. It turns what would take days to set up into a task that takes hours.
>
> **When to use it:** Red team engagements with a social engineering component. Phishing awareness campaigns for organizations (authorized). Testing human susceptibility in security assessments. Building and testing email lures before a real engagement.
>
> **Legal / Ethics:** Only use on authorized targets. Phishing without authorization is a crime. GoPhish campaigns must be explicitly included in the engagement scope.
>
> **Roadmap Phase:** Phase 6 (Social Engineering and Phishing Simulation)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | Infrastructure | 4 | 2–3 hours |
| 3 | Email Templates | 4 | 2–3 hours |
| 4 | Landing Pages | 3 | 2–3 hours |
| 5 | Campaigns | 4 | 2–3 hours |
| 6 | Results Analysis | 3 | 1–2 hours |
| 7 | Practical Labs | 3 | 3–5 hours |
| 8 | Mastery Challenges | 2 | 2–3 hours |
| | **Total** | **27** | **~15–24 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — Phishing Campaign Anatomy

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Email Template** | The lure email. Subject, body, links. Impersonates legitimate entity. |
| **Landing Page** | The page victims are sent to when they click the link. Can: clone a legitimate site for credential capture, serve a file download (payload), display an "awareness" page. |
| **Sending Profile** | SMTP configuration for sending the campaign emails. |
| **Users & Groups** | Target list: victim email addresses and names. |
| **Campaign** | Combines all of the above. Start date, from name, SMTP profile, target group, email template, landing page URL. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Download** | `getgophish.com` → download binary for your platform. |
| **Run** | `./gophish` — starts server. Default: admin interface at `https://127.0.0.1:3333`. API at `http://0.0.0.0:80`. |
| **Password** | First run: auto-generated admin password shown in terminal output. Change immediately after login. |
| **TLS** | Admin interface uses self-signed TLS by default. Accept the browser warning. |

---

### Task 1.3 — Ethics and Legal

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Authorization** | GoPhish campaigns MUST be explicitly authorized in the statement of work or engagement agreement. |
| **Scope** | Only send to email addresses explicitly in scope. |
| **Notification** | Some engagements: HR/legal notified (but not the targets). Some: blind test. |
| **Credential Handling** | Captured credentials: store securely, report to client, never use for actual access unless explicitly in scope. |

---

### Task 1.4 — GoPhish Components Overview

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Dashboard** | Campaign results overview. Click-through rates, credential submissions. |
| **Campaigns** | Create/manage campaigns. |
| **Users & Groups** | Manage target email lists. |
| **Email Templates** | Lure email content. |
| **Landing Pages** | Credential capture or payload delivery pages. |
| **Sending Profiles** | SMTP relay configuration. |

---

# PHASE 2: INFRASTRUCTURE

---

### Task 2.1 — Domain and Hosting

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Domain** | Register a convincing lookalike domain: `corporate-helpdesk.com`, `it-support-portal.net`. Check: brand similarity, DNS, email deliverability. |
| **Categorization** | New domains are flagged by email gateways and proxies as uncategorized. Solutions: use aged domains, submit domain for categorization, use a categorized proxy domain. |
| **VPS** | Host GoPhish on a dedicated VPS (DigitalOcean, Vultr). Not on shared hosting. Port 80/443 open. |

---

### Task 2.2 — Sending Profile (SMTP)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Create** | Sending Profiles → New Profile. Host: SMTP server. Port: 587 (TLS) or 465 (SSL). Username/Password: SMTP auth credentials. From: `IT Support <support@yourdomain.com>`. |
| **SMTP Options** | Mailgun, SendGrid (paid, better deliverability). Self-hosted Postfix. Gmail app password (limited). |
| **SPF/DKIM/DMARC** | Configure DNS records for your sending domain: SPF, DKIM, DMARC. Dramatically improves deliverability and avoids spam filtering. |
| **Test** | Sending Profiles → Send Test Email → verify it arrives and looks correct. |

---

### Task 2.3 — Email Deliverability

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **SPF** | `v=spf1 ip4:your_vps_ip include:mailgun.org ~all`. Tells receiving servers your VPS is authorized to send from your domain. |
| **DKIM** | DomainKeys Identified Mail — digital signature on outgoing emails. Verify: `mail-tester.com`. |
| **DMARC** | `v=DMARC1; p=none; rua=mailto:postmaster@domain.com`. Tells receivers what to do with failed SPF/DKIM. |
| **Check** | `mail-tester.com` — score your email deliverability before the campaign. Aim for 10/10. |

---

### Task 2.4 — SSL Certificate

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Let's Encrypt** | `certbot --nginx -d yourdomain.com` — free TLS cert. Victims see the green padlock — increases trust. |
| **GoPhish Config** | Edit `config.json`: `"phish_server": {"listen_url": "0.0.0.0:443", "use_tls": true, "cert_path": "cert.pem", "key_path": "key.pem"}`. |

---

# PHASE 3: EMAIL TEMPLATES

---

### Task 3.1 — Creating an Email Template

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Create** | Email Templates → New Template. |
| **Import** | Import Email → paste raw email source (from a real email you're cloning) → GoPhish parses it. |
| **HTML** | Use HTML editor for polished, legitimate-looking emails. Match font, colors, logo of the impersonated entity. |
| **Variables** | `{{.FirstName}}` — target's first name. `{{.Email}}` — target's email. `{{.URL}}` — phishing link (auto-populated with tracking link). `{{.From}}` — sender name. |

---

### Task 3.2 — Effective Lure Design

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Urgency** | "Your account will be locked in 24 hours." "Immediate action required." |
| **Authority** | Impersonate IT department, CEO, HR. |
| **Relevance** | Reference real events the target cares about: "Your VPN password expires today." |
| **Low Friction** | Simple call to action: one clear link. "Click here to verify your account." |
| **Clone** | Clone a real legitimate email from the organization (IT notification, DocuSign, Office 365 MFA). |

---

### Task 3.3 — Tracking Pixel

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Built-in** | GoPhish auto-embeds a 1x1 tracking pixel in all HTML emails. When email opened → GoPhish records "opened" event. |
| **Note** | Email clients blocking remote images → open event not recorded. Open tracking is approximate. |

---

### Task 3.4 — Link and Attachment Options

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Link** | `{{.URL}}` in template → GoPhish inserts unique per-target tracking URL → records who clicked. |
| **No Attachment in GoPhish** | GoPhish does not handle malicious attachments natively. For payload delivery: create a landing page that serves a file download. Or use a separate tool (SET, manual). |

---

# PHASE 4: LANDING PAGES

---

### Task 4.1 — Clone a Login Page

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Import** | Landing Pages → New Page → Import Site → enter URL → GoPhish downloads the HTML/CSS. |
| **Tweak** | Review cloned page. Ensure form action captures credentials (GoPhish replaces the action). Fix any broken references. |
| **Common Targets** | Microsoft 365 login, Outlook Web Access, VPN portals, corporate SSO. |

---

### Task 4.2 — Credential Capture

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Capture Credentials** | Check "Capture Submitted Data" → GoPhish captures all form fields. |
| **Redirect** | "Redirect to" URL: after submission, redirect to the real legitimate page. Victim has no idea. Or: show an "awareness" page explaining this was a phishing simulation. |

---

### Task 4.3 — Awareness Page

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Content** | "You have been phished as part of a security awareness campaign. Here's what to look for in real phishing emails..." |
| **Training** | Include training resources. Turns the click into a teaching moment. |

---

# PHASE 5: CAMPAIGNS

---

### Task 5.1 — Creating a Campaign

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Create** | Campaigns → New Campaign. Name, Email Template, Landing Page, URL (your phishing domain), Launch Date, Sending Profile, Groups. |
| **URL** | The base URL of your GoPhish phishing server (e.g., `https://corporate-helpdesk.com`). |
| **Launch** | Click Launch. GoPhish sends emails according to schedule. |

---

### Task 5.2 — Scheduling

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Send By** | Set a "Send Emails By" date → GoPhish spaces emails over time to avoid flooding (better deliverability, less suspicious). |
| **Timing** | Send during business hours (9–11 AM local time) → highest open rates. Avoid weekends. |

---

### Task 5.3 — Target Groups

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Import CSV** | Users & Groups → Import CSV. Format: `First Name,Last Name,Email,Position`. |
| **Targeting** | Create targeted groups: IT staff, finance, executives, all employees. Different campaigns per group with tailored lures. |

---

### Task 5.4 — Multi-Step Campaigns

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Concept** | Multiple campaigns targeting the same group: initial lure → follow-up to those who didn't click → escalated lure for those who did click but didn't submit. |
| **Advanced** | Use GoPhish API to programmatically manage multi-step campaigns. |

---

# PHASE 6: RESULTS ANALYSIS

---

### Task 6.1 — Reading Campaign Results

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Metrics** | Emails sent. Email opened. Link clicked. Data submitted. |
| **Timeline** | See when each event occurred. |
| **Per User** | Who opened, who clicked, who submitted. With what data. |

---

### Task 6.2 — Captured Credentials

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **View** | Campaign → Results → click individual user → see submitted form data. |
| **Handling** | Document credentials securely. Report to client. Never use credentials for further access unless explicitly in scope and authorized. |

---

### Task 6.3 — Campaign Report

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Content** | Click rate, submission rate, time to click (how quickly users fell for it). Most vulnerable departments. Recommendations for awareness training. |
| **Benchmark** | Industry average: 20–30% click rate on well-crafted phishing. Compare client results. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — Lab Phishing Campaign

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 45 min

| **Scenario** | Lab: set up GoPhish. Create sending profile (use local Postfix or Mailhog for lab). Create a cloned login page. Create email template. Create a group with your own test email. Run campaign. Track results. |
| **Success Criteria** | Campaign runs. Email received. Click tracked. Credential submitted and captured. |

---

### Lab 7.2 — Credential Harvest to Access

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Authorized phishing simulation: user submits credentials via GoPhish landing page. Use captured credentials to log in to the service as that user. Document the escalation chain. |
| **Success Criteria** | Credentials captured. Used successfully for access (with authorization). Attack chain documented. |

---

### Lab 7.3 — Full Campaign Report

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | Write a professional phishing campaign report from a GoPhish campaign. Include: methodology, template used, results (click rate, submission rate), most vulnerable group, recommendations. |
| **Success Criteria** | Professional report suitable for a client deliverable. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Bypass Email Gateway

- [ ] **Completed** · ⭐⭐⭐⭐⭐ Expert · ⏱️ 90 min

| **Scenario** | Lab with an email gateway (Proofpoint, Mimecast sandbox). Create a phishing email that bypasses the gateway and arrives in the inbox. Document: which filters were triggered initially, what changes were needed to bypass. |
| **Success Criteria** | Email delivered to inbox through the gateway. Bypass technique documented. |

---

### Challenge 8.2 — Spear Phishing Campaign

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Design a spear phishing campaign targeting a specific role (e.g., CFO persona). Use OSINT (LinkedIn, company website) to craft a highly personalized email. Run against a test target (yourself). Document the OSINT-to-lure pipeline. |
| **Success Criteria** | Personalized lure using OSINT data. Campaign run. OSINT-to-lure pipeline documented. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can install and configure GoPhish | ☐ |
| Can configure a sending profile with proper SPF/DKIM/DMARC | ☐ |
| Can create an effective email template with tracking variables | ☐ |
| Can clone a login page and set up credential capture | ☐ |
| Can run a full campaign and read results | ☐ |
| Can write a phishing campaign report | ☐ |
| Understands ethical/legal requirements for phishing campaigns | ☐ |
| Can use OSINT to create personalized spear phishing | ☐ |

---

## 🎯 Interview Questions

1. What are the components of a GoPhish campaign?
2. How do you configure email deliverability (SPF, DKIM, DMARC)?
3. What makes a phishing email effective?
4. How do you clone a login page in GoPhish?
5. What metrics does GoPhish track and what do they mean?
6. How do you handle captured credentials in a pentest?
7. What is a spear phishing campaign and how does it differ from mass phishing?
8. What are the legal and ethical requirements for running phishing campaigns?
