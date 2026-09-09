# 🔬 Frida: Complete Mastery Checklist

> **What is Frida?** Frida is an open-source dynamic instrumentation framework that lets you inject JavaScript (or Python) scripts into running processes on Android, iOS, Windows, macOS, and Linux — without modifying or recompiling the target application. At runtime, Frida can intercept function calls, modify arguments and return values, hook into memory, bypass security checks, and extract sensitive data from any running process. It is the primary tool for mobile application security testing and reverse engineering.
>
> **Why does it exist?** Static analysis (reading decompiled code) tells you what an app *can* do. Dynamic instrumentation tells you what it *actually does* at runtime, with real data. Frida bridges this gap — you can observe, intercept, and modify an application's behavior while it's running, without having the source code.
>
> **When to use it:** SSL/certificate pinning bypass (Phase 5 exit gate), bypassing root/jailbreak detection on mobile apps, hooking Android/iOS API calls to extract secrets (API keys, session tokens, decrypted data), runtime analysis of obfuscated apps, and any scenario where static analysis hits a wall.
>
> **When to avoid it:** When you need static analysis (use jadx/Ghidra instead). When the app has advanced Frida detection (some banking apps detect Frida's presence via thread inspection — need advanced evasion techniques). Frida requires a rooted Android device or jailbroken iOS device for most attack scenarios.
>
> **What mastering Frida unlocks:** SSL pinning bypass (the Phase 5 exit requirement), runtime secret extraction from mobile apps, ability to patch any mobile application's logic at runtime, foundation for all dynamic mobile app security testing, and the skill that makes mobile pentesting dramatically more powerful than static analysis alone.
>
> **Roadmap Stage / Module:** Shelf: Module S02 (Mobile Security)

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| Mobile Security | Android Analysis | iOS Analysis | Network |
|:---------------|:----------------|:-------------|:--------|
| **🔬 Frida** (you are here) | [📦 jadx](jadx.md) | [📱 Objection](Objection.md) | [🕷️ Burp Suite](Burp_Suite.md) |
| [🔨 APKTool](APKTool.md) | [📡 Aircrack-ng](Aircrack-ng.md) | | |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & Setup | 5 | 2–3 hours |
| 2 | Frida Basics & Script Structure | 7 | 3–4 hours |
| 3 | Intercepting Android API Calls | 8 | 4–6 hours |
| 4 | SSL Pinning Bypass | 6 | 3–5 hours |
| 5 | Root/Jailbreak Detection Bypass | 5 | 3–4 hours |
| 6 | iOS Instrumentation | 5 | 3–4 hours |
| 7 | Practical Labs | 4 | 5–8 hours |
| | **Total** | **40** | **~23–34 hours** |

**Prerequisites:** Phase 1 complete (Python basics). A rooted Android device or emulator (Genymotion, Android Studio AVD with rooted image). Basic understanding of Android app architecture (Activity, APK structure). Phase 4 Burp Suite basics helpful.

---

# PHASE 1: INSTALLATION & SETUP

---

## 1.1 Install Frida on Kali/Attack Machine

```bash
# Install Frida tools (Python-based CLI)
pip3 install frida frida-tools

# Verify
frida --version
frida-ps --version   # List processes
frida-trace --version
```

## 1.2 Set Up Frida Server on Android Device

The Frida server runs on the Android device (requires root). Your host machine communicates with it over ADB.

```bash
# Check your device's architecture
adb shell getprop ro.product.cpu.abi
# Common values: arm64-v8a (most modern phones), armeabi-v7a (32-bit), x86_64 (emulators)

# Download the correct Frida server binary from:
# https://github.com/frida/frida/releases
# Filename format: frida-server-<version>-android-<arch>.xz

# Example: arm64 device
wget https://github.com/frida/frida/releases/download/16.2.1/frida-server-16.2.1-android-arm64.xz
xz -d frida-server-16.2.1-android-arm64.xz

# Push to device and make executable
adb push frida-server-16.2.1-android-arm64 /data/local/tmp/frida-server
adb shell chmod 755 /data/local/tmp/frida-server

# Start the Frida server (as root on device)
adb shell su -c "/data/local/tmp/frida-server &"

# Verify connection from host
frida-ps -U          # -U = USB device
# Should list running Android processes
```

## 1.3 Using an Android Emulator

```bash
# Genymotion (recommended — easiest rooted emulator)
# Download from genymotion.com, create a virtual device, start it

# Android Studio AVD with rooted image
# Use Google APIs arm64 image, then root with Magisk in the emulator

# Connect via ADB
adb connect 127.0.0.1:5555   # Genymotion default port
frida-ps -U                   # Verify Frida sees the emulator
```

---

# PHASE 2: FRIDA BASICS & SCRIPT STRUCTURE

---

## 2.1 Frida CLI Commands

```bash
# List all running processes on connected device
frida-ps -U

# Attach to a running process by name
frida -U -n com.target.app

# Spawn (launch) an app and attach immediately
frida -U -f com.target.app --no-pause

# Run a Frida script against an app
frida -U -f com.target.app -l my_script.js --no-pause

# Frida REPL (interactive JavaScript console attached to process)
frida -U -n com.target.app
# Then type JavaScript in the console
```

## 2.2 Frida JavaScript API Core Concepts

```javascript
// === Basic Hooks ===

// Hook a Java method (Android)
Java.perform(function() {
    // Get reference to a class
    var TargetClass = Java.use("com.example.app.ClassName");

    // Override a method
    TargetClass.methodName.implementation = function(arg1, arg2) {
        console.log("[*] methodName called with arg1=" + arg1 + " arg2=" + arg2);

        // Call the original method and capture return value
        var retval = this.methodName(arg1, arg2);
        console.log("[*] methodName returned: " + retval);

        // Return original value, modified value, or hardcoded value
        return retval;
        // return true;   // Override return value
    };
});
```

```javascript
// === Overloaded Methods ===
Java.perform(function() {
    var String = Java.use("java.lang.String");

    // Method with overloads — specify argument types
    String.equals.overload("java.lang.Object").implementation = function(other) {
        console.log("[*] String.equals called: " + this.toString() + " vs " + other);
        return this.equals(other);
    };
});
```

```javascript
// === Hook Native Functions (C/C++ layer) ===
// Find function address
var funcAddr = Module.getExportByName("libssl.so", "SSL_get_verify_result");

// Intercept calls
Interceptor.attach(funcAddr, {
    onEnter: function(args) {
        console.log("[*] SSL_get_verify_result called, SSL* = " + args[0]);
    },
    onLeave: function(retval) {
        console.log("[*] SSL_get_verify_result returned: " + retval);
        // Force return 0 (X509_V_OK — certificate is valid)
        retval.replace(0);
    }
});
```

## 2.3 Useful Built-in Helpers

```javascript
// Print Java stack trace (where was this method called from?)
Java.perform(function() {
    var TargetClass = Java.use("com.example.app.Crypto");
    TargetClass.encrypt.implementation = function(data) {
        // Print call stack
        console.log(Java.use("android.util.Log").getStackTraceString(
            Java.use("java.lang.Exception").$new()
        ));
        return this.encrypt(data);
    };
});

// Enumerate all loaded classes matching a pattern
Java.perform(function() {
    Java.enumerateLoadedClasses({
        onMatch: function(className) {
            if (className.includes("SSL") || className.includes("Trust")) {
                console.log("[*] Found: " + className);
            }
        },
        onComplete: function() {}
    });
});

// Find all instances of a class currently in memory
Java.perform(function() {
    Java.choose("com.example.app.SessionManager", {
        onMatch: function(instance) {
            console.log("[*] Found instance, token = " + instance.getAuthToken());
        },
        onComplete: function() {}
    });
});
```

---

# PHASE 3: INTERCEPTING ANDROID API CALLS

---

## 3.1 Intercept Cryptographic Operations

```javascript
// Hook AES encryption — extract key and plaintext
Java.perform(function() {
    var Cipher = Java.use("javax.crypto.Cipher");

    Cipher.doFinal.overload("[B").implementation = function(input) {
        console.log("[*] Cipher.doFinal called");
        console.log("[*] Algorithm: " + this.getAlgorithm());
        console.log("[*] Input (plaintext/ciphertext): " + bytesToHex(input));

        var result = this.doFinal(input);
        console.log("[*] Output: " + bytesToHex(result));
        return result;
    };

    function bytesToHex(bytes) {
        var hex = "";
        for (var i = 0; i < bytes.length; i++) {
            hex += ("0" + (bytes[i] & 0xFF).toString(16)).slice(-2);
        }
        return hex;
    }
});
```

## 3.2 Extract SharedPreferences (Stored Secrets)

```javascript
// Hook SharedPreferences to extract all stored key-value pairs
Java.perform(function() {
    var SharedPreferencesImpl = Java.use("android.app.SharedPreferencesImpl");

    SharedPreferencesImpl.getString.implementation = function(key, defValue) {
        var value = this.getString(key, defValue);
        console.log("[*] SharedPreferences.getString key=" + key + " value=" + value);
        return value;
    };
});
```

## 3.3 Intercept HTTP Requests (Before SSL Layer)

```javascript
// Hook OkHttp3 — most popular Android HTTP library
Java.perform(function() {
    var OkHttpClient = Java.use("okhttp3.OkHttpClient");
    var Request = Java.use("okhttp3.Request");
    var RealCall = Java.use("okhttp3.RealCall");

    RealCall.execute.implementation = function() {
        var request = this.request();
        console.log("[*] OkHttp Request: " + request.method() + " " + request.url());
        var headers = request.headers();
        for (var i = 0; i < headers.size(); i++) {
            console.log("[*] Header: " + headers.name(i) + ": " + headers.value(i));
        }
        return this.execute();
    };
});
```

---

# PHASE 4: SSL PINNING BYPASS

---

SSL Certificate Pinning is when an app validates that the server's TLS certificate matches a hardcoded expected value — preventing Burp Suite's intercepting certificate from working.

## 4.1 Generic SSL Pinning Bypass (TrustManager)

```javascript
// Bypass Android TrustManager — makes app accept ALL certificates
Java.perform(function() {
    var X509TrustManager = Java.use("javax.net.ssl.X509TrustManager");
    var SSLContext = Java.use("javax.net.ssl.SSLContext");

    // Create a permissive TrustManager
    var TrustManager = Java.registerClass({
        name: "com.example.frida.TrustManager",
        implements: [X509TrustManager],
        methods: {
            checkClientTrusted: function(chain, authType) {},
            checkServerTrusted: function(chain, authType) {},  // Do nothing = accept all
            getAcceptedIssuers: function() { return []; }
        }
    });

    // Install it in SSLContext
    var trustManagers = [TrustManager.$new()];
    var SSLContextInit = SSLContext.init.overload(
        "[Ljavax.net.ssl.KeyManager;",
        "[Ljavax.net.ssl.TrustManager;",
        "java.security.SecureRandom"
    );

    SSLContextInit.implementation = function(keyManager, trustManager, secureRandom) {
        console.log("[*] SSLContext.init hooked — installing permissive TrustManager");
        SSLContextInit.call(this, keyManager, trustManagers, secureRandom);
    };
});
```

## 4.2 OkHttp3 Certificate Pinner Bypass

```javascript
// Bypass OkHttp3's CertificatePinner
Java.perform(function() {
    var CertificatePinner = Java.use("okhttp3.CertificatePinner");

    CertificatePinner.check.overload(
        "java.lang.String",
        "java.util.List"
    ).implementation = function(hostname, peerCertificates) {
        console.log("[*] CertificatePinner.check bypassed for: " + hostname);
        // Do nothing — skip the pinning check entirely
    };

    CertificatePinner.check.overload(
        "java.lang.String",
        "[Ljava.security.cert.Certificate;"
    ).implementation = function(hostname, peerCertificates) {
        console.log("[*] CertificatePinner.check (v2) bypassed for: " + hostname);
    };
});
```

## 4.3 Using Objection for Automated Pinning Bypass

```bash
# Objection's built-in SSL pinning bypass (covers most cases automatically)
# See Objection.md for full instructions
objection -g com.target.app explore
# Then in objection REPL:
android sslpinning disable
```

## 4.4 Native-Layer SSL Bypass

```javascript
// Bypass at the native libssl level — works when pinning is in C/C++ code
var libssl = Process.getModuleByName("libssl.so");
var funcVerify = libssl.getExportByName("SSL_get_verify_result");

Interceptor.attach(funcVerify, {
    onLeave: function(retval) {
        // X509_V_OK = 0 — force return success regardless of actual result
        retval.replace(ptr(0));
        console.log("[*] SSL_get_verify_result forced to X509_V_OK");
    }
});
```

---

# PHASE 5: ROOT/JAILBREAK DETECTION BYPASS

---

```javascript
// Bypass common Android root detection checks
Java.perform(function() {

    // 1. File existence checks (common root files)
    var File = Java.use("java.io.File");
    File.exists.implementation = function() {
        var filePath = this.getAbsolutePath();
        var rootFiles = ["/su", "/system/bin/su", "/sbin/su", "/system/xbin/su",
                         "/data/local/tmp/su", "/system/app/Superuser.apk",
                         "/.magisk", "/data/adb/magisk"];
        for (var i = 0; i < rootFiles.length; i++) {
            if (filePath.indexOf(rootFiles[i]) !== -1) {
                console.log("[*] Root file check bypassed: " + filePath);
                return false;
            }
        }
        return this.exists();
    };

    // 2. Build tag checks (test-keys = rooted ROM)
    var Build = Java.use("android.os.Build");
    Build.TAGS.value = "release-keys";

    // 3. System property checks
    var SystemProperties = Java.use("android.os.SystemProperties");
    SystemProperties.get.overload("java.lang.String").implementation = function(key) {
        if (key === "ro.debuggable") return "0";
        if (key === "ro.secure") return "1";
        return this.get(key);
    };
});
```

---

# PHASE 6: iOS INSTRUMENTATION

---

```bash
# iOS requires a jailbroken device (Palera1n, Checkra1n, Unc0ver)
# Install Frida on iOS via Cydia/Sileo: add repo https://build.frida.re

# Connect via USB
iproxy 27042 27042 &    # Forward USB port to localhost
frida-ps -U             # List iOS processes

# Attach to an app
frida -U -n com.example.app
```

```javascript
// iOS Objective-C hooking
ObjC.schedule(ObjC.mainQueue, function() {
    // Hook NSURLSession for network interception
    var NSURLSession = ObjC.classes.NSURLSession;
    var dataTaskMethod = NSURLSession["- dataTaskWithRequest:completionHandler:"];

    Interceptor.attach(dataTaskMethod.implementation, {
        onEnter: function(args) {
            var request = ObjC.Object(args[2]);
            console.log("[*] NSURLSession request: " + request.URL().absoluteString());
        }
    });
});
```

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — First Hook:** Using any rooted Android emulator, install a simple test app (e.g., InsecureBankv2 from GitHub). Attach Frida and write a script that prints the arguments and return value of any login method. Confirm your hook fires when you tap "Login" in the app.

- [ ] **Lab 2 — SSL Pinning Bypass (Phase 5 Exit Gate):** Install an app with certificate pinning (TikTok, Snapchat, any banking app in an emulator). Configure Burp Suite as proxy. Observe that HTTPS traffic fails due to pinning. Apply the generic TrustManager bypass or OkHttp3 bypass script. Confirm traffic now flows through Burp Suite with intercepted requests visible.

- [ ] **Lab 3 — Secret Extraction:** Using DIVA Android (Deliberately Insecure and Vulnerable Application), hook `SharedPreferences.getString` and `Cipher.doFinal`. Navigate through the app's challenges. Document every secret value (hardcoded keys, stored passwords) captured by your hooks.

- [ ] **Lab 4 — Root Detection Bypass:** Find an app with root detection (many banking apps or security challenge apps like RootBeer). Apply the root detection bypass script. Verify the app proceeds past the root check in a rooted emulator where it previously blocked.

---

## 📝 Operational Notes

- **Frida detection by apps:** Banking apps, DRM-protected apps, and some games actively detect Frida's presence (by scanning process names, thread names, memory patterns, and `/proc/` entries). Bypassing Frida detection requires advanced evasion: custom server builds, process name obfuscation, or using `frida-gadget` embedded directly in the APK.
- **`--no-pause` flag:** When spawning an app with `-f`, always use `--no-pause` unless you need to hook something in the very first milliseconds of app startup. Without it, the app pauses at entry point waiting for your signal.
- **Script loading order:** For early-stage hooks (before `onCreate`), use `frida -U -f com.app --no-pause -l script.js`. The script is injected before the app's first line of code runs.
- **Gadget mode:** When a rooted device isn't available, embed `frida-gadget` as a native library in the APK using APKTool. The gadget starts a Frida server automatically on app launch. Works on non-rooted devices but requires app repackaging.
- **Frida vs Xposed:** Xposed Framework is an alternative hooking framework for Android (requires a custom recovery). Frida is preferred for pentesting because it doesn't require modifying the device persistently — sessions are temporary.
