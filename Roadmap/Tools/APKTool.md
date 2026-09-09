# 🔨 APKTool: Complete Mastery Checklist

> **What is APKTool?** APKTool is an open-source reverse engineering tool for Android APK files. Unlike jadx (which decompiles to Java), APKTool disassembles the compiled DEX bytecode to Smali — a human-readable assembly language for Android's Dalvik Virtual Machine. APKTool also decodes binary XML resources (AndroidManifest.xml, layouts, strings) back to readable text, and crucially allows you to **rebuild and repackage** modified APKs. This bidirectional capability (disassemble → modify → reassemble) is what makes APKTool unique.
>
> **Why does it exist?** jadx gives you readable Java code but you can't easily modify and rebuild it. APKTool operates at the Smali layer — closer to the actual bytecode — enabling precise modifications that survive recompilation. It's the tool for patching APKs: removing security checks, modifying behavior, injecting code, and rebuilding for testing.
>
> **When to use it:** Patching APKs to disable root/SSL checks when Frida isn't viable, injecting Frida Gadget for non-rooted device testing, modifying app behavior for testing edge cases, extracting and analyzing all resources (including encrypted assets), and repackaging modified apps for static + dynamic combined analysis.
>
> **When to avoid it:** For reading/understanding code logic, jadx (Java output) is far more readable than APKTool's Smali. For dynamic analysis, Frida/Objection is cleaner. Use APKTool specifically when you need to **permanently modify** an APK.
>
> **What mastering APKTool unlocks:** Ability to patch any Android app without source code (removing checks, injecting Frida gadget), deep understanding of Android's Smali bytecode layer, capability to modify app behavior for edge case testing, and the technical foundation for Android malware modification analysis.
>
> **Roadmap Stage / Module:** Shelf: Module S02 (Mobile Security)

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| Mobile Static Analysis | Mobile Dynamic Analysis | Resources |
|:----------------------|:------------------------|:---------|
| [📦 jadx](jadx.md) | [🔬 Frida](Frida.md) | |
| **🔨 APKTool** (you are here) | [📱 Objection](Objection.md) | |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & First Decompile | 4 | 1–2 hours |
| 2 | APK Structure & Smali Basics | 7 | 3–4 hours |
| 3 | AndroidManifest & Resource Analysis | 5 | 2–3 hours |
| 4 | Patching APKs (Disabling Checks) | 8 | 4–6 hours |
| 5 | Injecting Frida Gadget | 5 | 3–4 hours |
| 6 | Signing & Installing Modified APKs | 4 | 1–2 hours |
| 7 | Practical Labs | 4 | 4–6 hours |
| | **Total** | **37** | **~18–27 hours** |

**Prerequisites:** Basic Android understanding (what an APK is, activity lifecycle). Phase 1 Linux CLI. jadx basics (Phase 5) helpful for understanding code before patching.

---

# PHASE 1: INSTALLATION & FIRST DECOMPILE

---

## 1.1 Installation

```bash
# Option 1: Package manager
sudo apt install apktool

# Option 2: Latest version (recommended)
wget https://bitbucket.org/iBotPeaches/apktool/downloads/apktool_2.9.3.jar -O apktool.jar
wget https://raw.githubusercontent.com/iBotPeaches/Apktool/master/scripts/linux/apktool -O apktool
chmod +x apktool
sudo mv apktool apktool.jar /usr/local/bin/

# Verify
apktool --version

# Also install tools needed for signing
sudo apt install zipalign apksigner
# Or use the Android SDK build tools
```

## 1.2 Disassemble an APK

```bash
# Basic disassembly
apktool d target.apk

# Output directory structure:
# target/
# ├── AndroidManifest.xml   — Decoded (human-readable XML)
# ├── apktool.yml           — APKTool metadata
# ├── smali/                — Disassembled bytecode (one .smali file per class)
# ├── smali_classes2/       — Multi-dex secondary DEX files
# ├── res/                  — Decoded resources (XML layouts, strings, drawables)
# └── assets/               — Raw assets (raw files, certificates, databases)

# Disassemble with specific options
apktool d target.apk -o output_dir/   # Specify output directory
apktool d target.apk --no-res         # Skip resource decoding (faster)
apktool d target.apk --only-main-classes  # Only decode main classes DEX
```

---

# PHASE 2: APK STRUCTURE & SMALI BASICS

---

## 2.1 APK File Structure

```
target.apk (it's a ZIP file)
├── AndroidManifest.xml        — Binary XML (APKTool decodes it)
├── classes.dex                — Compiled Dalvik bytecode (main DEX)
├── classes2.dex               — Multi-dex overflow (large apps)
├── resources.arsc             — Compiled resource table (APKTool decodes it)
├── res/                       — Resource files (images, XML)
├── assets/                    — Raw assets (databases, certs, config)
├── lib/                       — Native libraries (.so files for ARM/x86)
│   ├── arm64-v8a/
│   └── armeabi-v7a/
└── META-INF/                  — APK signature files
    ├── MANIFEST.MF
    ├── CERT.RSA
    └── CERT.SF
```

## 2.2 Smali Basics (Read This Before Patching)

Smali is the assembly language of the Dalvik VM. Every Java class becomes a `.smali` file.

```smali
# Java:
# public class com.example.RootChecker {
#     public boolean isRooted() {
#         return false;
#     }
# }

# Smali equivalent:
.class public Lcom/example/RootChecker;  # Class declaration (L = class type, ; = end)
.super Ljava/lang/Object;

.method public isRooted()Z               # Method: name(params)ReturnType
    .registers 2                          # Number of registers used (v0, v1, ...)

    const/4 v0, 0x0                       # v0 = 0 (false)
    return v0                             # Return v0

.end method
```

**Critical Smali type descriptors:**

| Smali | Java Type |
|:------|:---------|
| `Z` | boolean |
| `I` | int |
| `J` | long |
| `F` | float |
| `D` | double |
| `B` | byte |
| `C` | char |
| `S` | short |
| `V` | void |
| `Ljava/lang/String;` | String (object types start with L, end with ;) |
| `[I` | int[] (array) |

**Key Smali instructions:**

```smali
const/4 v0, 0x1         # v0 = 1 (true)
const/4 v0, 0x0         # v0 = 0 (false)
return-void             # return (void method)
return v0               # return boolean/int/etc
return-object v0        # return object reference

invoke-virtual {v0, v1}, Lsome/Class;->method(Ljava/lang/String;)Z
# Call v0.method(v1) [virtual dispatch]
move-result v0          # Store return value of last invoke in v0

if-eqz v0, :cond_0     # if v0 == 0 goto :cond_0
if-nez v0, :cond_0     # if v0 != 0 goto :cond_0

:cond_0                 # Label (jump target)
```

---

# PHASE 3: ANDROIDMANIFEST & RESOURCE ANALYSIS

---

## 3.1 AndroidManifest.xml Analysis

```bash
# After apktool d, the manifest is decoded to readable XML
cat output_dir/AndroidManifest.xml

# Critical sections to examine:
# 1. Permissions requested
grep "uses-permission" output_dir/AndroidManifest.xml

# 2. Exported components (accessible without authentication)
grep "exported=\"true\"" output_dir/AndroidManifest.xml
# Any exported Activity, Service, or BroadcastReceiver is an attack surface

# 3. Debug flag (should be false in production)
grep "debuggable" output_dir/AndroidManifest.xml

# 4. Backup flag (allows adb backup of app data if true)
grep "allowBackup" output_dir/AndroidManifest.xml

# 5. Network security config reference
grep "networkSecurityConfig" output_dir/AndroidManifest.xml
```

## 3.2 Resource Analysis

```bash
# strings.xml — app string constants (often contains URLs, keys)
cat output_dir/res/values/strings.xml | grep -i "api\|key\|url\|secret\|token\|password"

# Network security config (certificate pinning in XML)
cat output_dir/res/xml/network_security_config.xml

# Check for raw embedded certificates
ls output_dir/assets/
file output_dir/assets/*       # Identify file types

# Check for embedded SQLite databases
find output_dir/assets/ -name "*.db" -o -name "*.sqlite"
```

---

# PHASE 4: PATCHING APKs (DISABLING CHECKS)

---

## 4.1 Patching Root Detection

```bash
# 1. Find the root check method using jadx (get class + method name)
# 2. Open the corresponding Smali file
# Example: com.example.security.RootChecker → smali/com/example/security/RootChecker.smali

# 3. Find the isRooted() method in the Smali file
grep -n "isRooted" output_dir/smali/ -r

# 4. Edit the method to always return false
```

```smali
# BEFORE (returns actual root check result):
.method public isRooted()Z
    .registers 3
    # ... complex root detection logic ...
    return v0    # Returns true if rooted

# AFTER (patched to always return false):
.method public isRooted()Z
    .registers 2
    const/4 v0, 0x0    # v0 = false
    return v0          # Always return false
.end method
```

## 4.2 Patching Certificate Pinning (Smali-Level)

```bash
# Find the checkServerTrusted method (custom TrustManager)
grep -r "checkServerTrusted" output_dir/smali/ -l
```

```smali
# BEFORE (validates certificate):
.method public checkServerTrusted([Ljava/security/cert/X509Certificate;Ljava/lang/String;)V
    .registers 5
    # ... validation logic that throws CertificateException ...
    invoke-virtual {v1}, Ljava/security/cert/CertificateException;->...

# AFTER (empty method — accepts all certificates):
.method public checkServerTrusted([Ljava/security/cert/X509Certificate;Ljava/lang/String;)V
    .registers 1
    return-void    # Do nothing — accept everything
.end method
```

## 4.3 Modifying Network Security Config

```bash
# Simpler alternative to Smali patching for basic pinning:
# Edit the network_security_config.xml to remove pin-set entries

# BEFORE:
# <domain-config cleartextTrafficPermitted="false">
#     <domain includeSubdomains="true">api.target.com</domain>
#     <pin-set>
#         <pin digest="SHA-256">AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA==</pin>
#     </pin-set>
# </domain-config>

# AFTER (remove the pin-set section entirely):
sed -i '/<pin-set>/,/<\/pin-set>/d' output_dir/res/xml/network_security_config.xml

# Also add cleartextTrafficPermitted for Burp HTTPS interception
# Add to AndroidManifest.xml's application tag:
# android:networkSecurityConfig="@xml/network_security_config"
# And in network_security_config.xml:
# <base-config cleartextTrafficPermitted="true">
#     <trust-anchors>
#         <certificates src="user"/>   <!-- Trust user-installed CAs = Burp cert -->
#         <certificates src="system"/>
#     </trust-anchors>
# </base-config>
```

---

# PHASE 5: INJECTING FRIDA GADGET

---

Frida Gadget allows Frida instrumentation **without a rooted device** by embedding the Frida server as a native library directly in the APK.

```bash
# 1. Download Frida Gadget for target architecture
# https://github.com/frida/frida/releases
wget https://github.com/frida/frida/releases/download/16.2.1/frida-gadget-16.2.1-android-arm64.so.xz
xz -d frida-gadget-16.2.1-android-arm64.so.xz
mv frida-gadget-16.2.1-android-arm64.so libgadget.so

# 2. Disassemble the APK
apktool d target.apk -o target_patched/

# 3. Copy Gadget library to APK's lib directory
cp libgadget.so target_patched/lib/arm64-v8a/libgadget.so

# 4. Find the app's main Activity's Smali file (check AndroidManifest for LAUNCHER activity)
# 5. Add Gadget load instruction at the start of the Activity's static initializer
#    or in the onCreate method:
```

```smali
# Add this at the beginning of the target Smali method:
const-string v0, "gadget"
invoke-static {v0}, Ljava/lang/System;->loadLibrary(Ljava/lang/String;)V
# This calls System.loadLibrary("gadget") which loads libgadget.so
```

```bash
# 6. Rebuild, sign, and install (see Phase 6)
# 7. Launch the app — it pauses waiting for Frida to connect
# 8. Connect with Frida from your machine:
frida -U -n Gadget
```

---

# PHASE 6: SIGNING & INSTALLING MODIFIED APKs

---

```bash
# Every APK must be signed before Android will install it

# Step 1: Rebuild the APK with APKTool
apktool b target_patched/ -o target_modified.apk

# Step 2: Generate a signing keystore (do once, reuse)
keytool -genkey -v -keystore test_key.jks -alias test -keyalg RSA \
  -keysize 2048 -validity 3650 -storepass android -keypass android \
  -dname "CN=Test, OU=Test, O=Test, L=Test, S=Test, C=US"

# Step 3: Align the APK (required before signing)
zipalign -p -f -v 4 target_modified.apk target_aligned.apk

# Step 4: Sign with apksigner
apksigner sign --ks test_key.jks --ks-key-alias test \
  --ks-pass pass:android --key-pass pass:android \
  --out target_signed.apk target_aligned.apk

# Step 5: Verify the signature
apksigner verify --verbose target_signed.apk

# Step 6: Install on device
adb install target_signed.apk
# If app already installed:
adb install -r target_signed.apk   # Replace existing
```

> [!IMPORTANT]
> You CANNOT install a modified APK alongside the original if the signatures differ. You must uninstall the original first: `adb uninstall com.target.app`. This means you lose any data stored by the app.

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — Resource Extraction:** Take any APK (your own phone's APKs are fine). Disassemble with APKTool. Extract and document: all permissions, all exported components, all string resource values containing URLs or keys, and the network security config if present.

- [ ] **Lab 2 — Root Check Bypass via Patching:** Install InsecureBankv2 or a RootBeer demo app. Use jadx to find the root check method. Open the corresponding Smali in APKTool output. Patch it to always return `false`. Rebuild, sign, and install. Confirm the app no longer detects root.

- [ ] **Lab 3 — Frida Gadget Injection:** Take any APK. Inject Frida Gadget into it using the Phase 5 process. Rebuild, sign, and install on a non-rooted device or standard emulator. Connect with `frida -U -n Gadget` and confirm you can run hooks. This proves you can instrument any app even without device root.

- [ ] **Lab 4 — Full Mobile Pentest Chain:** Using DIVA Android: (a) disassemble with APKTool, (b) find hardcoded credentials in resources/Smali, (c) patch a security check, (d) rebuild and install, (e) use Frida/Objection for runtime analysis. Write a 2-page finding report in professional pentest format.

---

## 📝 Operational Notes

- **APKTool vs jadx for patching:** APKTool works at Smali (bytecode) level — accurate but verbose. You can theoretically decompile to Java with jadx, edit, then recompile with a Java compiler, but this almost never works cleanly. Stick to Smali edits via APKTool for patching.
- **Multi-dex apps:** Large apps split code across multiple DEX files (classes.dex, classes2.dex, etc.). APKTool creates `smali/`, `smali_classes2/`, `smali_classes3/` directories. Search across all of them.
- **`apktool.yml`:** The metadata file APKTool creates tracks the APK's original structure. Do not delete it — APKTool uses it during rebuild. The `targetSdkVersion` in this file affects behavior during rebuild.
- **V2/V3 signatures:** Modern APKs use APK Signature Scheme v2/v3. `apksigner` handles these. The older `jarsigner` tool only creates v1 signatures — don't use it for modern apps.
- **App bundle (AAB) vs APK:** The Google Play Store distributes App Bundles (.aab), but devices receive split APKs. APKTool works on APKs, not AABs. Get the APK directly from the device using `adb pull`.
