# 📦 jadx: Complete Mastery Checklist

> **What is jadx?** jadx is an open-source command-line and GUI tool for decompiling Android APK and DEX (Dalvik Executable) files back into readable Java source code. It takes the compiled bytecode of an Android app and reconstructs the original Java classes, methods, and logic — allowing you to read an app's code without having the source. jadx-gui provides a graphical interface with syntax highlighting, class browser, search, and cross-reference navigation.
>
> **Why does it exist?** Android apps ship as compiled DEX bytecode, not source code. Static analysis of mobile apps requires reading this code. While tools like `apktool` decompile to Smali (assembly-like bytecode), jadx decompiles all the way to Java — dramatically more readable and analyzable. jadx is the fastest way to understand what an Android application is doing.
>
> **When to use it:** Finding hardcoded API keys, credentials, and encryption keys in app code; understanding authentication logic and business logic flaws; identifying certificate pinning implementation details (to know how to bypass them); finding hidden functionality, debug endpoints, and admin features; and reverse engineering obfuscated Android malware.
>
> **When to avoid it:** When the app uses aggressive obfuscation (ProGuard/R8/DexGuard) that makes Java output unreadable — use dynamic analysis (Frida) instead. For native (C/C++) library analysis within APKs, use Ghidra instead of jadx. For repackaging/patching APKs, use APKTool instead.
>
> **What mastering jadx unlocks:** Static analysis of any Android app without source code, ability to find hardcoded secrets (Phase 5 OWASP M9), understanding of app security mechanisms that dynamic analysis will then target, and foundation for Android malware analysis in Phase 7.
>
> **Roadmap Stage / Module:** Shelf: Module S02 (Mobile Security)

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| Mobile Static Analysis | Mobile Dynamic Analysis | Binary Analysis |
|:----------------------|:------------------------|:----------------|
| **📦 jadx** (you are here) | [🔬 Frida](Frida.md) | [🔭 Ghidra](Ghidra.md) |
| [🔨 APKTool](APKTool.md) | [📱 Objection](Objection.md) | [🐛 x64dbg](x64dbg.md) |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & First Decompile | 4 | 1–2 hours |
| 2 | jadx-gui Navigation | 6 | 2–3 hours |
| 3 | Finding Hardcoded Secrets | 7 | 3–4 hours |
| 4 | Authentication & Crypto Logic Analysis | 7 | 4–5 hours |
| 5 | Certificate Pinning Analysis | 5 | 3–4 hours |
| 6 | Dealing with Obfuscation | 5 | 3–4 hours |
| 7 | Practical Labs | 4 | 4–6 hours |
| | **Total** | **38** | **~20–28 hours** |

**Prerequisites:** Phase 1 complete. Basic Java reading ability (you don't need to write Java, just read and understand it). Phase 5 APK structure knowledge helpful.

---

# PHASE 1: INSTALLATION & FIRST DECOMPILE

---

## 1.1 Installation

```bash
# Option 1: Package manager (may not be latest)
sudo apt install jadx

# Option 2: Download latest release (recommended)
wget https://github.com/skylot/jadx/releases/latest/download/jadx-1.5.0.zip
unzip jadx-1.5.0.zip -d jadx/
export PATH="$PATH:$(pwd)/jadx/bin"

# Verify
jadx --version

# GUI version (requires Java)
jadx-gui
```

## 1.2 Getting APKs to Analyze

```bash
# Method 1: Pull APK from a connected device
adb shell pm list packages | grep target      # Find package name
adb shell pm path com.target.app              # Get APK path
adb pull /data/app/~~.../com.target.app.../base.apk ./target.apk

# Method 2: Download from APKPure, APKMirror, or APK extraction apps (on device)

# Method 3: Extract split APKs (modern apps use AAB format producing split APKs)
adb pull /data/app/~~.../com.target.app.../base.apk
adb pull /data/app/~~.../com.target.app.../split_config.arm64_v8a.apk
# Pass all splits to jadx
```

## 1.3 First Decompile

```bash
# Decompile APK to Java source (CLI)
jadx -d output_dir/ target.apk

# Output structure:
# output_dir/
# ├── sources/        — Decompiled Java source files
# └── resources/      — APK resources (XML layouts, strings, images)

# Decompile with all features enabled (recommended)
jadx -d output_dir/ --show-bad-code --no-res-decode target.apk

# Open in GUI
jadx-gui target.apk
```

---

# PHASE 2: JADX-GUI NAVIGATION

---

## 2.1 GUI Layout

- **Left panel — Package tree:** All Java classes organized by package structure. Navigate like a file explorer.
- **Center — Source viewer:** Decompiled Java code with syntax highlighting.
- **Search bar (Ctrl+F):** Search within the current file.
- **Global Search (Ctrl+Shift+F):** Search across ALL decompiled files — this is your primary reconnaissance tool.
- **Code navigation:** Click any class/method reference to jump to its definition (Ctrl+click).
- **Cross-references (X):** Right-click any method/field → "Find usage" — shows everywhere it's called from. Critical for following data flow.

## 2.2 Navigation Workflow

```
1. Open APK in jadx-gui
2. Browse the package tree — look for:
   - Main app package (e.g., com.target.app.*)
   - Authentication packages (auth/, login/, account/)
   - Network packages (network/, api/, http/)
   - Crypto packages (crypto/, security/, utils/)
3. Use global search (Ctrl+Shift+F) for specific strings:
   - "http://" / "https://"          — Find hardcoded URLs
   - "api_key" / "apikey" / "key"    — Find API keys
   - "password" / "passwd" / "pwd"   — Find password references
   - "secret" / "token" / "Bearer"   — Find secrets/tokens
   - "BuildConfig"                   — Find build-time constants
4. Follow code flows using cross-references
```

---

# PHASE 3: FINDING HARDCODED SECRETS

---

## 3.1 Command-Line Secret Hunting

```bash
# After decompiling to output_dir/, search the source
# API keys and tokens (high-entropy strings)
grep -r "api_key\|apikey\|API_KEY\|api-key" output_dir/sources/ --include="*.java"
grep -r "secret\|SECRET\|client_secret" output_dir/sources/
grep -r "token\|TOKEN\|Bearer\|bearer" output_dir/sources/
grep -r "password\|PASSWORD\|passwd" output_dir/sources/

# Hardcoded URLs and endpoints
grep -r "http[s]*://" output_dir/sources/ | grep -v "//.*http"

# AWS credentials pattern
grep -r "AKIA[0-9A-Z]{16}" output_dir/sources/   # AWS Access Key ID
grep -r "wJalrXUtnFEMI\|[A-Za-z0-9/+=]{40}" output_dir/sources/  # AWS Secret

# Google API keys
grep -r "AIza[0-9A-Za-z-_]{35}" output_dir/sources/

# Check resources/strings.xml for string constants
grep -r "api\|key\|secret\|token\|password\|url\|endpoint" output_dir/resources/
```

## 3.2 BuildConfig — Developer Constants

```bash
# BuildConfig.java contains constants set at build time
find output_dir/ -name "BuildConfig.java" -exec cat {} \;

# Typical contents:
# public static final String BASE_URL = "https://api.target.com";
# public static final String API_KEY = "abc123xyz";
# public static final boolean DEBUG = false;
# public static final int VERSION_CODE = 42;
```

## 3.3 res/values/strings.xml — String Resources

```bash
# Android string resources — often contains URLs, endpoints, keys
cat output_dir/resources/res/values/strings.xml | grep -i "key\|url\|api\|secret\|token"

# Examine all XML files in resources
find output_dir/resources/ -name "*.xml" -exec grep -l "http\|key\|secret\|token" {} \;
```

---

# PHASE 4: AUTHENTICATION & CRYPTO LOGIC ANALYSIS

---

## 4.1 Tracing Authentication Flow

```bash
# In jadx-gui: Search for login/authentication entry points
# Common class names to look for:
# LoginActivity, AuthManager, AccountManager, UserRepository, SessionManager

# Find the login button click handler:
# In the XML layout: find the login Button's android:onClick attribute
# Then search that method name in sources

# Typical authentication flow in decompiled code:
# 1. User inputs username/password
# 2. App constructs HTTP request with credentials
# 3. Server responds with token/session cookie
# 4. App stores token in SharedPreferences/database
```

## 4.2 Understanding Crypto Usage

```java
// What to look for in decompiled crypto code:

// WEAK: Hardcoded key (critical vulnerability)
SecretKeySpec key = new SecretKeySpec("hardcodedkey1234".getBytes(), "AES");

// WEAK: ECB mode (no IV, pattern-preserving)
Cipher cipher = Cipher.getInstance("AES/ECB/PKCS5Padding");

// WEAK: Static IV (same IV every time)
byte[] iv = "1234567890123456".getBytes();

// BETTER: GCM mode with random IV (look for SecureRandom)
SecureRandom random = new SecureRandom();
byte[] iv = new byte[12];
random.nextBytes(iv);
Cipher cipher = Cipher.getInstance("AES/GCM/NoPadding");
```

## 4.3 Finding JWT Implementation

```bash
# Search for JWT handling
grep -r "JWT\|JsonWebToken\|jjwt\|jose4j\|nimbus" output_dir/sources/
grep -r "parseClaimsJws\|getBody\|getClaims" output_dir/sources/

# If you find JWT verification code, check:
# 1. Is the algorithm validated? (alg:none attack)
# 2. Is the signature actually verified?
# 3. Is the secret key hardcoded?
```

---

# PHASE 5: CERTIFICATE PINNING ANALYSIS

---

```bash
# Find where pinning is implemented — to know what to bypass
grep -r "CertificatePinner\|TrustManager\|checkServerTrusted\|X509Certificate" \
  output_dir/sources/ --include="*.java"

grep -r "ssl\|SSL\|certificate\|Certificate\|pinning\|Pinning" \
  output_dir/sources/ -l
```

```java
// Common pinning patterns to identify:

// Pattern 1: OkHttp3 CertificatePinner (most common)
CertificatePinner pinner = new CertificatePinner.Builder()
    .add("api.target.com", "sha256/AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=")
    .build();

// Pattern 2: Custom TrustManager
public void checkServerTrusted(X509Certificate[] chain, String authType) {
    // Custom validation logic here
    String certHash = getCertHash(chain[0]);
    if (!certHash.equals(EXPECTED_HASH)) throw new CertificateException("Pinning failed");
}

// Pattern 3: Network Security Config (XML-based, Android 7+)
// Check res/xml/network_security_config.xml
// <pin-set> entries contain expected certificate hashes
```

```bash
# Check for Network Security Config (XML-based pinning)
find output_dir/resources/ -name "network_security_config.xml"
cat output_dir/resources/res/xml/network_security_config.xml
```

---

# PHASE 6: DEALING WITH OBFUSCATION

---

```bash
# Signs of obfuscation:
# Class names: a.b.c, A, B, C (single-letter names)
# Method names: a(), b(), c()
# String constants encrypted/obfuscated
# Control flow flattening (switch statements everywhere)

# Decompile with more aggressive renaming detection
jadx --deobf --deobf-min-len 2 --deobf-max-len 64 -d output/ target.apk

# Rename classes as you understand them in jadx-gui:
# Right-click class → Rename → Give meaningful name
# These renames persist as comments in the code view
```

```bash
# String obfuscation — strings are decrypted at runtime
# Technique: Hook the decryption method with Frida to get plaintext
# 1. Find the decryption method in jadx (look for Base64 + XOR patterns)
# 2. Hook it with Frida to print decrypted strings as app runs
# See Frida.md for hooking technique

# ProGuard mapping file: if you can find the mapping.txt (sometimes leaked
# in the APK or accessible via the app's error reporting), load it in jadx:
# jadx --proguard-map mapping.txt -d output/ target.apk
```

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — OWASP Benchmark APK:** Download the OWASP MASTG (Mobile Application Security Testing Guide) benchmark APK or DIVA Android. Decompile with jadx. Find all OWASP M1–M10 vulnerabilities using only static analysis. Document the vulnerable class name, method name, and line number for each finding.

- [ ] **Lab 2 — Hardcoded Secret Hunt:** Decompile any free app from APKPure (choose a random productivity or utility app). Run the full secret-hunting grep commands from Phase 3. Document any hardcoded URLs, keys, or credentials found. This is exactly what bug bounty hunters do at scale.

- [ ] **Lab 3 — Pinning Prep:** Decompile an app that uses SSL pinning. Locate the pinning implementation in the decompiled source (OkHttp CertificatePinner, custom TrustManager, or network_security_config.xml). Document the exact class and method. Then use Frida/Objection to bypass it. Confirm the bypass targets the exact mechanism you identified statically.

- [ ] **Lab 4 — Malware APK Analysis:** Download a known Android malware sample from MalwareBazaar (look for tag "android"). Decompile with jadx. Identify: hardcoded C2 URLs, permission abuse (what permissions does it request?), persistence mechanism, and any obfuscation techniques used. Write a 1-page technical analysis.

---

## 📝 Operational Notes

- **jadx vs apktool:** jadx decompiles to Java (human-readable). apktool decompiles to Smali (Android bytecode — assembly-like). Use jadx for reading/understanding logic. Use apktool for patching/modifying the APK.
- **Decompilation accuracy:** jadx's Java output is a *reconstruction*, not the original source. Some constructs (lambdas, generics, annotations) may be imperfectly reconstructed. If the Java doesn't make sense, check the apktool Smali output for reference.
- **Large APKs:** Some apps (Facebook, Instagram) are 100MB+ APKs with thousands of classes. jadx-gui can take minutes to open these. Increase jadx's JVM heap: set `JAVA_OPTS=-Xmx4g` before running jadx-gui.
- **`--show-bad-code`:** When jadx can't perfectly decompile a method, it shows a placeholder comment by default. The `--show-bad-code` flag shows its best (possibly incorrect) attempt at the code — often still useful for understanding the structure.
- **Cross-reference navigation:** The most underused jadx-gui feature. "Find usage" on any method/field shows you the entire call graph. Start from a sensitive operation (e.g., `checkServerTrusted`) and trace backwards to understand when and how it's invoked.
