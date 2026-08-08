# 🧼 SoapUI: Complete Reference

> **What is SoapUI?** SoapUI is an open-source tool for testing SOAP (Simple Object Access Protocol) web services and REST APIs. It provides a GUI for building, sending, and validating XML/WSDL-based SOAP requests as well as REST requests. It is the standard tool for testing legacy enterprise web services — the kind you encounter in banking, healthcare, ERP, and government systems that predate the REST/JSON era.
>
> **When to use it:** Testing SOAP/WSDL APIs on enterprise targets. Understanding WSDL definitions and auto-generating test requests. Testing XML-specific vulnerabilities (XXE, XPATH injection, SOAP action spoofing). API security assessments against legacy enterprise systems. When an engagement scope includes SOA (Service-Oriented Architecture) targets.
>
> **Tier 4 Reminder:** Know what SOAP is, how to import a WSDL and send requests, and be aware of SOAP-specific vulnerabilities. Deep mastery is needed only if your role frequently encounters legacy enterprise web services.
>
> **Roadmap Phase:** Phase 3 (Web Application Attacks — Legacy SOAP/WSDL Services)

---

## 🧭 Navigation

> [🏠 Home](../README.md) · [📋 Roadmap](../Roadmap/README.md)

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | SOAP Fundamentals | 4 | 1–2 hours |
| 2 | Core SoapUI Usage | 5 | 2–3 hours |
| 3 | Security Testing | 4 | 2–3 hours |
| 4 | REST in SoapUI | 3 | 1–2 hours |
| 5 | Mastery Check | 2 | 20 min |
| | **Total** | **18** | **~6–10 hours** |

---

# PHASE 1: SOAP FUNDAMENTALS

---

### Task 1.1 — What SOAP Is

- [ ] **Completed** · ⭐ Beginner · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **SOAP** | Simple Object Access Protocol. XML-based messaging protocol for exchanging structured data over HTTP, SMTP, or TCP. Predecessor to REST APIs. |
| **WSDL** | Web Services Description Language. XML file that describes the SOAP service: available operations (methods), input/output message formats, endpoint URL, and data types. SoapUI imports WSDL to auto-generate all possible requests. |
| **Structure** | SOAP message = `<Envelope>` → `<Header>` (optional: auth, WS-Security) + `<Body>` (the actual request/response). |
| **Why Still Relevant** | Banks, insurance, healthcare, government, ERP systems (SAP, Oracle) — many still expose SOAP services. Bug bounty programs targeting financial/enterprise sectors regularly have SOAP endpoints. |

---

### Task 1.2 — SOAP vs. REST

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **SOAP** | XML only. WSDL contract. Strongly typed. Built-in WS-Security standard. Verbose and complex. Stateful in some implementations. Common in legacy/enterprise. |
| **REST** | JSON (or XML). No formal contract (OpenAPI is voluntary). Less rigid. Lightweight. Stateless. Dominant in modern APIs. |
| **Testing Tool** | REST: Burp Suite, Postman. SOAP: SoapUI. For security testing of SOAP endpoints through a proxy: Burp Suite intercept + SoapUI as the client. |

---

### Task 1.3 — WSDL Reading

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Find WSDL** | Usually at: `http://target.com/service?wsdl`. Or: `http://target.com/service.svc?wsdl`. Or linked from application source. |
| **Key Sections** | `<types>` — data types (XSD). `<message>` — message definitions. `<portType>` — operations (methods) available. `<binding>` — transport and encoding details. `<service>` — endpoint URL. |
| **Attack Surface** | Each `<operation>` is a function you can call. Input types define what parameters are accepted. Understanding WSDL = understanding the entire API surface. |

---

### Task 1.4 — WS-Security

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **WS-Security** | Standards for SOAP security: message authentication, integrity, and encryption at the SOAP header level. |
| **Token Types** | UsernameToken (basic credentials). X.509 certificates. SAML assertions. Kerberos. |
| **Security Tests** | UsernameToken: does the service accept requests without authentication? With empty credentials? With a replayed token? Does it enforce token expiry? |

---

# PHASE 2: CORE SoapUI USAGE

---

### Task 2.1 — Installation

- [ ] **Completed** · ⭐ Beginner · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Download** | `soapui.org` → SoapUI Open Source (free). Available for Windows, Linux, macOS. |
| **SmartBear ReadyAPI** | Commercial version with additional testing and security features. Requires license. Open Source is sufficient for most security testing. |
| **Java Dependency** | Requires Java 11+. Usually bundled with the installer. |

---

### Task 2.2 — Import WSDL and Create Project

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **New Project** | File → New SOAP Project → enter WSDL URL or file path → SoapUI automatically generates all operations and sample requests. |
| **Project Tree** | Left panel: Project → Interfaces → Operations → Requests. Each operation has a pre-built XML request template. |
| **Endpoint** | Auto-extracted from WSDL. Can be overridden (e.g., point at a test vs. production endpoint). |

---

### Task 2.3 — Sending Requests

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Request Editor** | Double-click a request → XML editor on left, response on right. Edit XML values → click green play button → send. |
| **Authentication** | Request → Auth tab → configure Username/Password, WS-Security token, OAuth, etc. |
| **Headers** | Request → Headers tab → add `SOAPAction`, `Content-Type: text/xml`, custom headers. |
| **SOAPAction** | HTTP header required by many SOAP services: `SOAPAction: "http://service.com/GetUser"`. Value defined in WSDL. |

---

### Task 2.4 — Request Templates

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Pre-built Templates** | SoapUI generates valid XML request templates from WSDL. Placeholder values use `?` where you fill in data. |
| **Edit** | Replace `?` placeholders with actual or attack payloads. The XML structure is fixed by the WSDL schema — you can only modify content within the defined elements. |

---

### Task 2.5 — Test Suites

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Test Suite** | Project → New TestSuite → add TestCases → add Test Steps (SOAP Request, REST Request, Assertion, Script). |
| **Assertions** | Assert: HTTP status code, response contains string, response matches XPath. Automate pass/fail checks. |
| **Run** | Run TestSuite → all requests execute → pass/fail report. |

---

# PHASE 3: SECURITY TESTING

---

### Task 3.1 — XXE (XML External Entity) Testing

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Vulnerability** | SOAP services parse XML. If the parser processes external entity references in DOCTYPE declarations, an attacker can read local files, SSRF to internal services, or cause DoS. |
| **Payload** | Add to SOAP request body: `<?xml version="1.0"?><!DOCTYPE foo [<!ENTITY xxe SYSTEM "file:///etc/passwd">]><SOAP-ENV:Envelope...><element>&xxe;</element>`. |
| **Check Response** | Does the service return the file content in the response? Does it return an error disclosing the file content? Does it reach out to a server you control (SSRF)? |
| **SoapUI** | Edit the XML directly in the request editor — SoapUI sends raw XML, so you have full control to inject DOCTYPE and entity declarations. |

---

### Task 3.2 — SOAP Action Spoofing

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Vulnerability** | Some SOAP services dispatch requests based on SOAPAction HTTP header but validate using the SOAP body operation name. Mismatch = potentially bypass authorization. |
| **Test** | Set SOAPAction header to a privileged operation. Set SOAP body to a different (allowed) operation. Or: blank SOAPAction with a valid SOAP body operation. |
| **Expected Vulnerable** | Service accepts and executes the privileged operation because authorization only checked the body, not the header, or vice versa. |

---

### Task 3.3 — XPATH Injection

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Vulnerability** | If the service uses user input to construct XPath queries against an XML database (common in legacy SOAP services), injection can extract unauthorized data. |
| **Payload** | In a string field: `' or '1'='1` (analogous to SQL injection but for XPath). `' or 1=1 or '1'='` — always-true condition. `admin'][1]` — access first element. |
| **Identify** | Look for authentication endpoints that validate credentials against XML. Error messages mentioning XPath or XML parsing. |

---

### Task 3.4 — WS-Security Bypass Testing

- [ ] **Completed** · ⭐⭐⭐⭐ Advanced · ⏱️ 20 min

| Field | Detail |
|:---|:---|
| **Tests** | Remove WS-Security header entirely → does the service reject? Replay a captured valid token → does it validate the timestamp (token replay)? Use an expired token → does the service check expiry? Modify the token payload (tamper with SAML assertion or username) → does the signature validation catch it? |

---

# PHASE 4: REST IN SoapUI

---

### Task 4.1 — REST Project in SoapUI

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **When to Use** | SoapUI supports REST APIs too. If you're already in SoapUI for a SOAP assessment and need to test accompanying REST endpoints, you can use SoapUI. For REST-only assessments, Postman or Burp Suite are better choices. |
| **New REST Project** | File → New REST Project → enter base URL. Manually add resources (paths) and methods (GET/POST/PUT/DELETE). |

---

### Task 4.2 — SoapUI vs. Postman for REST

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Field | Detail |
|:---|:---|
| **SoapUI Advantage** | Better when you have a mixed SOAP + REST service to assess. Assertion system more powerful for automated testing. |
| **Postman Advantage** | Better UX for REST-only. Better collection organization. Better OAuth2 support. Larger community. |
| **Conclusion** | Default to Postman for REST. Use SoapUI when SOAP is involved or you need its specific assertion/test suite capabilities. |

---

### Task 4.3 — Burp Suite Integration

- [ ] **Completed** · ⭐⭐⭐ Intermediate · ⏱️ 15 min

| Field | Detail |
|:---|:---|
| **Setup** | SoapUI → Preferences → Proxy → set HTTP proxy to `127.0.0.1:8080` (Burp proxy). All SoapUI requests now appear in Burp. |
| **Use** | Use SoapUI to generate valid SOAP requests (from WSDL). Intercept in Burp. Modify and fuzz in Burp Repeater or Intruder. Best of both: WSDL-aware request generation + Burp's testing capabilities. |

---

# PHASE 5: MASTERY CHECK

---

### Task 5.1 — Competency Self-Assessment

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

| Competency | Self-Assessment |
|:---|:---:|
| Can explain what SOAP and WSDL are | ☐ |
| Can import a WSDL and generate requests in SoapUI | ☐ |
| Can send a SOAP request and inspect the response | ☐ |
| Can test for XXE injection in a SOAP service | ☐ |
| Can route SoapUI requests through Burp Suite | ☐ |
| Knows when to use SoapUI vs. Postman vs. Burp Suite | ☐ |

---

### Task 5.2 — Interview Questions

- [ ] **Completed** · ⭐⭐ Beginner-Intermediate · ⏱️ 10 min

1. What is SOAP and how does it differ from REST?
2. What is a WSDL and what information does it contain?
3. How do you use SoapUI to auto-generate all operations for a SOAP service?
4. What is XXE and how do you test for it in a SOAP service using SoapUI?
5. What is SOAP action spoofing and how do you test for it?
6. How do you proxy SoapUI traffic through Burp Suite?
7. When would you use SoapUI over Postman for API security testing?
