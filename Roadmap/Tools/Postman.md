# 📮 Postman: Complete Mastery Checklist

> **What is Postman?** Postman is an API development and testing platform. It provides a GUI for constructing, sending, and inspecting HTTP/HTTPS requests to any API — REST, GraphQL, SOAP, WebSocket. For security professionals, it is the tool for understanding and testing API endpoints: managing authentication flows, organizing requests into collections, writing test assertions, and documenting API behavior found during reconnaissance.
>
> **Why does it exist?** APIs are the dominant interface for modern applications and the primary attack surface for web pentesting. Postman lets you work with APIs systematically — replay requests, modify parameters, manage tokens and auth flows, and organize findings by collection. It bridges the gap between understanding an API and testing it.
>
> **When to use it:** API security testing on REST and GraphQL endpoints. Managing authentication tokens (Bearer, OAuth2, API keys) during long assessments. Organizing API endpoint collections from reconnaissance. Sending complex API requests that are difficult to craft in curl. Fuzzing API parameters before automating with ffuf.
>
> **What mastering Postman unlocks:** Efficient API attack surface exploration. Complex authentication flow handling. Organized API security testing. The foundation for every modern API pentest.

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Fundamentals | 4 | 1–2 hours |
| 2 | Request Building | 5 | 2–3 hours |
| 3 | Authentication | 4 | 2–3 hours |
| 4 | Collections | 3 | 1–2 hours |
| 5 | Security Testing | 4 | 3–4 hours |
| 6 | Automation | 3 | 2–3 hours |
| 7 | Practical Labs | 3 | 3–5 hours |
| 8 | Mastery Challenges | 2 | 2–3 hours |
| | **Total** | **28** | **~16–25 hours** |

---

# PHASE 1: FUNDAMENTALS

---

### Task 1.1 — REST API Concepts

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Resources** | API resources identified by URLs: `/api/users`, `/api/orders/123`. |
| **Methods** | `GET` — read. `POST` — create. `PUT`/`PATCH` — update. `DELETE` — delete. `OPTIONS` — list supported methods. |
| **Status Codes** | 200 OK. 201 Created. 400 Bad Request. 401 Unauthorized. 403 Forbidden. 404 Not Found. 500 Server Error. |
| **Auth** | `Authorization: Bearer <token>`. API key in header or query. Basic auth. OAuth2. |
| **Content-Type** | `application/json` (most common). `application/x-www-form-urlencoded`. `multipart/form-data`. |

---

### Task 1.2 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Download** | `postman.com` → Download the desktop app. |
| **Linux** | `snap install postman` or download tar.gz. |
| **Account** | Free account for collections sync. Or use offline mode. |
| **Alternatives** | Insomnia (similar GUI). Bruno (open source, no account needed). `httpie` (CLI). |

---

### Task 1.3 — Interface Overview

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Workspace** | Top: workspace selector. Sidebar: collections, environments, history. Center: request builder. Bottom: response viewer. |
| **Request Tab** | URL bar. Method selector. Params, Headers, Body, Auth, Pre-request Script, Tests tabs. |
| **Response** | Body (raw, pretty, preview), Headers, Status code, Time, Size. |

---

### Task 1.4 — Environments and Variables

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Variables** | `{{base_url}}`, `{{token}}` — placeholders replaced by environment values. |
| **Environment** | Set of key-value pairs: `base_url: http://api.target.com`, `token: eyJhbG...`. Switch between environments (dev, staging, prod). |
| **Use** | All requests in a collection use `{{base_url}}` → change one variable → affects all requests. |

---

# PHASE 2: REQUEST BUILDING

---

### Task 2.1 — Basic GET Request

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Create** | New request → Select `GET` → Enter URL → Send. |
| **Params** | Params tab → add key-value pairs → auto-appended to URL as `?key=value&key2=value2`. |
| **Headers** | Headers tab → add `Accept: application/json` etc. |

---

### Task 2.2 — POST with JSON Body

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Create** | Select `POST` → Body tab → raw → JSON → enter payload: `{"username":"admin","password":"test"}`. |
| **Content-Type** | Set automatically when you select JSON in raw dropdown. Or manually: `Content-Type: application/json`. |

---

### Task 2.3 — Headers and Custom Headers

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Add** | Headers tab → key: value. |
| **Security Relevant** | `X-Forwarded-For: 127.0.0.1` — IP spoofing tests. `X-Custom-IP-Authorization: 127.0.0.1` — some apps trust this. `Origin: https://evil.com` — CORS testing. |

---

### Task 2.4 — Request History and Import

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **History** | Left sidebar → History. All past requests. Re-run any previous request. |
| **Import cURL** | File → Import → Paste cURL command. Postman converts it to a request. From Burp: right-click → Copy as cURL → paste into Postman. |
| **Import from Burp** | Export Burp items → import Burp collection format in Postman. |

---

### Task 2.5 — File Upload

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Form Data** | Body → form-data → key: `file`, type: File → select file. Tests file upload endpoints. |
| **Security** | Change file extension, MIME type, content to test file upload vulnerabilities. Upload PHP shell as image.php with image/jpeg Content-Type. |

---

# PHASE 3: AUTHENTICATION

---

### Task 3.1 — Bearer Token

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Auth Tab** | Auth tab → Bearer Token → paste token. Postman auto-adds `Authorization: Bearer <token>` header. |
| **Variable** | Use `{{token}}` → update once in environment → applies to all requests. |

---

### Task 3.2 — API Key Auth

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Header** | Auth tab → API Key → key: `X-API-Key`, value: `your_api_key`, add to: Header. |
| **Query** | Or add to query params: `?api_key=value`. |

---

### Task 3.3 — OAuth2 Flow

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Configure** | Auth tab → OAuth 2.0 → Fill: Token URL, Auth URL, Client ID, Client Secret, Scope → Get New Access Token. |
| **Auto-Refresh** | Postman handles token refresh automatically when configured. |
| **Security** | Test OAuth flows: CSRF in state parameter, authorization code leakage, PKCE bypass, token scope elevation. |

---

### Task 3.4 — Basic and Digest Auth

- [ ] **Completed** · ⭐ Beginner · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Basic** | Auth tab → Basic Auth → Username + Password. Adds `Authorization: Basic base64(user:pass)`. |
| **Digest** | Auth tab → Digest Auth → Username + Password. More secure than Basic (not transmitted in base64). |

---

# PHASE 4: COLLECTIONS

---

### Task 4.1 — Creating Collections

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Create** | New Collection → name it after the target. Add folders by functionality: `/auth`, `/users`, `/admin`, `/api/v1`. |
| **Save Requests** | Save each request to the collection. Organized by endpoint. |
| **Share** | Export collection as JSON → share with team. Import Postman collection from target's public API docs. |

---

### Task 4.2 — Collection-Level Auth

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **Inherit** | Set auth on the collection → all requests inherit it. Individual requests can override. |
| **Efficiency** | Set `{{token}}` in collection auth → update one environment variable → all requests authenticated. |

---

### Task 4.3 — Import API Specs

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **OpenAPI** | File → Import → OpenAPI JSON/YAML → Postman generates a complete collection with all endpoints. |
| **Swagger** | Same import flow. All endpoints, parameters, and schemas populated automatically. |
| **Value** | Instant full collection for a documented API. No manual request building needed. |

---

# PHASE 5: SECURITY TESTING

---

### Task 5.1 — IDOR Testing

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Concept** | Insecure Direct Object Reference: change object ID in URL to access another user's data. `/api/users/1/profile` → change to `/api/users/2/profile`. |
| **Postman** | Duplicate request. Change ID. Compare responses. If user 2's data is returned without authorization check: IDOR. |
| **Automate** | Use Collection Runner with CSV of IDs. Postman iterates through all IDs automatically. |

---

### Task 5.2 — Mass Assignment Testing

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Concept** | API accepts more fields than expected and binds them to the object. `POST /api/users {"name":"alice","role":"admin"}` — does the server accept and apply `role`? |
| **Test** | Add extra parameters to POST/PUT body: `"is_admin":true`, `"role":"admin"`, `"balance":99999`. Send → check response and subsequent GET for the field. |

---

### Task 5.3 — HTTP Method Testing

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Test All Methods** | Duplicate the same URL → test GET, POST, PUT, PATCH, DELETE, OPTIONS, HEAD, TRACE. Some methods may be allowed unintentionally. |
| **Response** | 405 Method Not Allowed = correct. 200/201 = method allowed. 403 = method exists but access denied. |

---

### Task 5.4 — GraphQL Testing

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 25 min

| Field | Detail |
|:---|:---|
| **Introspection** | `POST /graphql` with `{"query":"{__schema{types{name}}}"}` — check if introspection is enabled. Returns full schema. |
| **Queries** | Build queries based on schema. Test for: missing auth on queries, over-fetching (returning sensitive fields), mutation authorization bypass. |
| **Batching** | Send multiple queries in one request — may bypass rate limits. |

---

# PHASE 6: AUTOMATION

---

### Task 6.1 — Collection Runner

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Run** | Collection → Run. Executes all requests in order. Set iterations and delay. |
| **CSV Data** | Import CSV → variables replaced per iteration. Bulk IDOR testing with all IDs in a CSV. |
| **Reports** | Pass/fail for each request based on test assertions. |

---

### Task 6.2 — Test Assertions

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Tests Tab** | JavaScript in Tests tab runs after response received. `pm.test("Status 200", () => pm.response.to.have.status(200));`. |
| **Response Body** | `pm.test("Has admin field", () => pm.expect(pm.response.json().role).to.eql("admin"));`. |
| **Use** | Auto-detect when privilege escalation succeeds. When `role==admin` in response: test passes = IDOR/mass assignment worked. |

---

### Task 6.3 — newman (CLI Runner)

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Install** | `npm install -g newman`. |
| **Run** | `newman run collection.json -e environment.json --reporters cli,html`. |
| **CI/CD** | Run Postman collections in CI/CD pipelines for automated API security regression testing. |

---

# PHASE 7: PRACTICAL LABS

---

### Lab 7.1 — REST API Recon and Testing

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 30 min

| **Scenario** | Target with a REST API (OWASP crAPI, Juice Shop API, or HTB machine). Discover all endpoints (import Swagger if available, or use ffuf → import to Postman). Authenticate. Test each endpoint for IDOR, mass assignment, and authorization bypass. |
| **Success Criteria** | All endpoints documented. At least 1 vulnerability found. |

---

### Lab 7.2 — OAuth2 Attack

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | PortSwigger OAuth lab or HackTheBox OAuth machine. Map the OAuth flow in Postman. Find and exploit: missing state parameter, authorization code leakage, or scope elevation. |
| **Success Criteria** | OAuth vulnerability exploited. Access to another user's account or elevated scope. |

---

### Lab 7.3 — GraphQL Security Test

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 30 min

| **Scenario** | Target with GraphQL endpoint. Run introspection to get schema. Build queries for sensitive data. Test for: introspection enabled, missing auth on queries, mutation authorization. |
| **Success Criteria** | Full schema retrieved. At least 1 authorization issue found. |

---

# PHASE 8: MASTERY CHALLENGES

---

### Challenge 8.1 — Full API Security Report

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 60 min

| **Scenario** | Complete API security assessment using Postman. Import spec → test all endpoints → find IDOR, mass assignment, method flaws, auth bypass. Write professional findings report. |
| **Success Criteria** | Professional report. All OWASP API Top 10 categories tested. |

---

### Challenge 8.2 — Automated Security Suite

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 45 min

| **Scenario** | Build a Postman collection with test assertions for every endpoint. Run with newman. All security tests automated. Pass/fail per test. |
| **Success Criteria** | Full automated test suite. newman run produces clear pass/fail security report. |

---

# 📋 FINAL COMPETENCY MATRIX

| Competency | Self-Assessment |
|:---|:---:|
| Can build GET, POST, PUT, DELETE requests with headers and body | ☐ |
| Can manage Bearer, API key, and OAuth2 authentication | ☐ |
| Can import OpenAPI/Swagger specs into Postman | ☐ |
| Can test IDOR by modifying object IDs | ☐ |
| Can test mass assignment by adding extra fields | ☐ |
| Can use Collection Runner with CSV data for bulk testing | ☐ |
| Can write test assertions to detect vulnerabilities | ☐ |
| Can run collections via newman CLI | ☐ |
| Can test GraphQL endpoints with introspection queries | ☐ |

---

## 🎯 Interview Questions

1. What is IDOR and how do you test for it in Postman?
2. How do you test mass assignment in a REST API?
3. How do you import an OpenAPI spec into Postman?
4. What is Collection Runner and how do you use it with a CSV file?
5. How do you write a test assertion that detects privilege escalation?
6. How do you test all HTTP methods on an API endpoint?
7. What does GraphQL introspection reveal and how do you check if it's enabled?
8. How do you run a Postman collection from the command line?
