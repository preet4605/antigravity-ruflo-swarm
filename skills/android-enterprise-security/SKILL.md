---
name: android-enterprise-security
description: "Deep-dive skills for banking and healthcare apps."
category: security
risk: high
source: community
date_added: "2026-04-07"
metadata:
  triggers:
    - "@security"
    - "proguard"
    - "root detection"
---

# Android Enterprise Security 🛡️

Hardening Android apps against reverse engineering and runtime modifications.

## ⚡ When to Use
- When requested to implement banking-grade security, obfuscation, or tamper-detection.

## 🏗️ Core Rules / Pillars

### 1. ProGuard / R8 Rules
- **Pattern**: Always explicitly keep domains, GSON/Moshi models, and JNI bridges. Use `-keepattributes *Annotation*`.

### 2. Root & Tamper Detection
- **Pattern**: Use Google Play Integrity API instead of hand-written root-checking scripts that look for `su` binaries.

## 🚧 Critical Anti-Hallucination Guards
- **Trap**: Do NOT use outdated SafetyNet APIs. SafetyNet is deprecated. Use Play Integrity API.
