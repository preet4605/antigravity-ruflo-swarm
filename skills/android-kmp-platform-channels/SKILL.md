---
name: android-kmp-platform-channels
description: "Bridging Native iOS and Desktop APIs back into KMP."
category: cross-platform
risk: high
source: community
date_added: "2026-04-07"
metadata:
  triggers:
    - "@kmp-native"
    - "expect actual"
    - "cinterop"
---

# Kotlin Multiplatform Native Bridging 🌉

When the common Kotlin standard library falls short, you must write native platform bridges to access raw iOS Foundation or Android Context APIs.

## ⚡ When to Use
- When integrating platform-specific hardware, Push Notifications, or third-party proprietary SDKs that lack a KMP wrapper.

## 🏗️ Core Rules / Pillars

### 1. The Expect/Actual Paradigm
- **Pattern**: Avoid trying to pass `Context` (Android) or `UIViewController` (iOS) around in common code via generic `Any` types.
- **Implementation**: Define an `expect` class or interface in `commonMain`, and provide `actual` implementations within `androidMain` and `iosMain`. Use constructor injection for dependencies if using Koin or Kotlin-Inject.

### 2. Bridging Coroutines to Swift (iOS)
- **Pattern**: By default, Kotlin `StateFlow` and `suspend` functions compile to Swift with generic clunky `Skie` or `CompletionHandler` signatures.
- **Implementation**: Rely on libraries like Touchlab's SKIE to seamlessly map Kotlin Coroutines into native Swift Async/Await to provide iOS developers a world-class API.

## 🚧 Critical Anti-Hallucination Guards
- **Trap**: Do not attempt to use `java.util.UUID` or `java.time` anywhere in `commonMain`! Native Java libraries simply DO NOT compile to iOS and will immediately break the KMP build. Instead use `kotlinx.datetime` and `uuid` libraries.
