# 📱 Objection: Complete Mastery Checklist

> **What is Objection?** Objection is a runtime mobile exploration toolkit built on top of Frida. It provides a command-line REPL (interactive console) with pre-built, one-command operations for the most common mobile security testing tasks — SSL pinning bypass, root/jailbreak detection bypass, memory dumping, class enumeration, and more. Where raw Frida requires writing custom JavaScript, Objection provides push-button access to the same capabilities.
>
> **Why does it exist?** Writing Frida scripts from scratch for every engagement is time-consuming. Objection packages the most commonly needed Frida scripts into a structured CLI, making dynamic mobile app analysis accessible without deep JavaScript expertise. It handles the boilerplate so you can focus on finding vulnerabilities.
>
> **When to use it:** Quick SSL pinning bypass in minutes (the Phase 5 exit gate shortcut), automated class/method enumeration on unknown apps, fast memory analysis, bypassing common root/jailbreak detection, and as the first tool to run when approaching any new mobile app.
>
> **When to avoid it:** Objection's pre-built scripts won't bypass custom or hardened pinning/root detection implementations. For those, you need raw Frida scripts (see Frida.md) and deep knowledge of the specific mechanism being used. Objection is the easy-mode starting point — raw Frida is the fallback.
>
> **What mastering Objection unlocks:** Rapid mobile application security assessment capability, SSL pinning bypass without custom script writing, structured mobile app exploration, and an efficient workflow for Phase 5 mobile pentesting engagements.
>
> **Roadmap Stage / Module:** Shelf: Module S02 (Mobile Security)

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| Mobile Security | Dynamic Analysis | Static Analysis | Network |
|:---------------|:----------------|:----------------|:--------|
| [🔬 Frida](Frida.md) | **📱 Objection** (you are here) | [📦 jadx](jadx.md) | [🕷️ Burp Suite](Burp_Suite.md) |
| [🔨 APKTool](APKTool.md) | | | |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & Connection | 4 | 1–2 hours |
| 2 | SSL Pinning Bypass | 5 | 2–3 hours |
| 3 | Root/Jailbreak Detection Bypass | 4 | 2–3 hours |
| 4 | App Exploration & Enumeration | 8 | 3–4 hours |
| 5 | Memory & Runtime Analysis | 6 | 3–4 hours |
| 6 | File System & Data Storage Analysis | 5 | 2–3 hours |
| 7 | Practical Labs | 4 | 4–6 hours |
| | **Total** | **36** | **~17–25 hours** |

**Prerequisites:** Frida installed and working (see Frida.md Phase 1). Rooted Android device or emulator. Burp Suite configured as HTTP proxy.

---

# PHASE 1: INSTALLATION & CONNECTION

---

## 1.1 Installation

```bash
# Install Objection (requires Frida already installed)
pip3 install objection

# Verify
objection --version

# Update to latest
pip3 install --upgrade objection
```

## 1.2 Connecting to an App

```bash
# Prerequisites:
# 1. Frida server running on device: adb shell su -c "/data/local/tmp/frida-server &"
# 2. Device connected via USB with adb

# Explore a running app (attach to already-launched app)
objection -g com.target.app explore

# Spawn the app fresh and explore (preferred — catches early initialization)
objection -g com.target.app explore --startup-command "android sslpinning disable"

# List installed packages to find the correct bundle ID
frida-ps -Uai | grep -i target

# iOS
objection -g com.target.ios.app explore
```

## 1.3 The Objection REPL

Once connected, you're in the Objection REPL:

```
com.target.app on (Android: 13) [usb] #
```

Type `help` for a full command list. Commands are organized by namespace:
- `android` — Android-specific commands
- `ios` — iOS-specific commands
- `memory` — Memory operations
- `jobs` — Background job management
- `env` — Environment information

---

# PHASE 2: SSL PINNING BYPASS

---

## 2.1 One-Command SSL Pinning Bypass

```bash
# In Objection REPL — disable SSL pinning immediately
android sslpinning disable

# Output shows which classes were hooked:
# (agent) Loaded 2 new job(s)!
# (agent) Custom TrustManager registered — bypass active
# (agent) OkHttp3 CertificatePinner — bypass active
# (agent) Webview SSL error handler — bypass active
# (agent) Apache HTTP Client — bypass active
```

This single command covers:
- Custom `TrustManager` implementations
- `OkHttp3` `CertificatePinner`
- `HttpsURLConnection`
- `WebView` SSL error handlers
- Apache HTTP Client

## 2.2 Enable at App Startup (For Early Pinning)

```bash
# Apps that pin during initialization — must bypass before first network call
objection -g com.target.app explore --startup-command "android sslpinning disable"

# Verify it's working: open Burp Suite → All traffic should now intercept
# without "SSL handshake failure" errors
```

## 2.3 When Objection Pinning Bypass Fails

```bash
# Check which SSL framework the app uses (helps determine what to hook)
android hooking list classes | grep -i "ssl\|certificate\|trust\|pinning\|okhttp"

# Look for custom pinning implementations
android hooking search methods check  # Search for methods containing "check"
android hooking search methods pin    # Search for "pin" methods

# Then write a custom Frida hook targeting the specific class/method
# See Frida.md Phase 4 for manual bypass techniques
```

---

# PHASE 3: ROOT/JAILBREAK DETECTION BYPASS

---

```bash
# Disable root/jailbreak detection checks (Android)
android root disable

# Output:
# (agent) Hooking java.io.File.exists() for root checks
# (agent) Hooking android.os.Build.TAGS
# (agent) Hooking java.lang.Runtime.exec() — blocks su execution check

# iOS jailbreak detection bypass
ios jailbreak disable
```

```bash
# Identify which detection method the app is using
# Watch for these patterns in app behavior:
# - App crashes immediately on launch → early native check
# - App shows popup "rooted device detected" → Java-layer check
# - App behaves normally but logs show checks → monitoring check

# Hook all file existence checks to see what root files the app checks
android hooking watch class_method java.io.File.exists --dump-args
```

---

# PHASE 4: APP EXPLORATION & ENUMERATION

---

## 4.1 Class & Method Enumeration

```bash
# List all loaded classes
android hooking list classes

# Filter by keyword
android hooking list classes | grep -i "login\|auth\|crypto\|ssl\|token\|session"

# List all methods of a specific class
android hooking list class_methods com.example.app.LoginManager

# Search for methods containing a keyword across all classes
android hooking search methods login
android hooking search methods decrypt
android hooking search methods verify
```

## 4.2 Live Method Hooking

```bash
# Watch a method — prints call args and return value every time it's called
android hooking watch class_method com.example.app.LoginManager.authenticate \
  --dump-args --dump-return --dump-backtrace

# Watch all methods in a class
android hooking watch class com.example.app.Crypto

# Hook and replace return value (override to return true/success)
android hooking set return_value com.example.app.RootChecker.isRooted false
```

## 4.3 Intent Interception

```bash
# Watch for broadcast intents being sent/received
android intents launch_activity com.example.app.HiddenActivity
# Launches an Activity that isn't in the main navigation flow

# Dump all registered receivers
android hooking list receivers
```

---

# PHASE 5: MEMORY & RUNTIME ANALYSIS

---

```bash
# Dump memory of a specific heap object
memory dump all /tmp/memdump.bin

# List memory regions
memory list modules

# Search memory for strings
memory search --string "password"
memory search --string "api_key"
memory search --string "token"

# Dump a specific memory region
memory dump from_base ADDR SIZE /tmp/region.bin

# Find class instances in heap (find live objects in memory)
android heap search instances com.example.app.SessionManager
# Then interact with a found instance:
android heap execute INSTANCE_HANDLE getAuthToken
```

---

# PHASE 6: FILE SYSTEM & DATA STORAGE ANALYSIS

---

```bash
# Show app's file system paths (data directories, databases, shared prefs)
env

# Output:
# Files Directory: /data/data/com.target.app/files
# Cache Directory: /data/data/com.target.app/cache
# External Files: /sdcard/Android/data/com.target.app/files

# List files in app's private directory
ls /data/data/com.target.app/

# Download files from device to local machine
file download /data/data/com.target.app/shared_prefs/prefs.xml ./prefs.xml
file download /data/data/com.target.app/databases/app.db ./app.db

# Read a SQLite database (look for stored tokens, passwords, session data)
sqlite connect /data/data/com.target.app/databases/app.db
sqlite execute query "SELECT * FROM users"
sqlite execute query "SELECT * FROM sessions"

# View SharedPreferences (key-value storage)
android keystore list    # List Android Keystore entries (encrypted storage)
```

## 6.2 SharedPreferences Live Monitoring

```bash
# Hook SharedPreferences to see all reads/writes in real time
android hooking watch class_method android.content.SharedPreferences.Editor.putString \
  --dump-args
# Every time the app writes a string to SharedPreferences, you see the key + value
```

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — Rapid App Assessment:** Install InsecureBankv2 or DIVA Android on your emulator. Launch Objection, run `android hooking list classes`, and identify at least 5 security-relevant class names (authentication, crypto, network). Hook one method in each class and document what data it processes.

- [ ] **Lab 2 — SSL Pinning Bypass (Phase 5 Exit Gate):** Find an app with certificate pinning (try TikTok, Snapchat, or any banking app in an emulator). Without Objection, confirm Burp Suite fails to intercept (SSL handshake failure). Launch Objection, run `android sslpinning disable`, and confirm Burp Suite now intercepts HTTPS traffic successfully.

- [ ] **Lab 3 — Data Storage Audit:** Using a banking/shopping app in your emulator, run all data storage commands (`file download` of SharedPrefs, SQLite query of databases, `memory search` for "token" and "password"). Document every piece of sensitive data stored insecurely (unencrypted tokens, passwords in SharedPreferences, credit card data in SQLite).

- [ ] **Lab 4 — Hidden Functionality:** Use `android hooking list classes` and `android intents launch_activity` on a target app to find and launch at least one Activity that isn't accessible through the normal UI. Document how you found it and what it does.

---

## 📝 Operational Notes

- **Objection is a Frida wrapper:** All Objection commands ultimately run Frida scripts under the hood. When Objection's pre-built commands fail, the fallback is always raw Frida (see Frida.md). Know how to use both.
- **App detection of Objection:** Objection and Frida share the same detection surface. Apps that detect Frida will also detect Objection. Advanced evasion requires custom Frida server builds with obfuscated thread/module names.
- **Job persistence:** Hooks you set in Objection persist only for the current session. When Objection disconnects (or the app is killed), all hooks are removed. For persistent monitoring, run hooks as background jobs (`--foreground` flag or use `jobs list`).
- **`--startup-command`:** The most important Objection flag for timing-sensitive hooks. Apps that check for root or pin certificates before any UI renders require the hook to be active before the first line of Java code runs. Always use `--startup-command "android sslpinning disable"` as your default launch pattern for any app with network traffic.
- **iOS `ssl-kill-switch`:** For iOS, a more reliable alternative to Objection's iOS pinning bypass is the `ssl-kill-switch2` Cydia tweak, which hooks at the native TLS layer and bypasses all certificate validation globally. Objection's iOS pinning bypass covers the Objective-C layer only.
