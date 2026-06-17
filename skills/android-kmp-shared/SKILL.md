---
name: android-kmp-shared
description: "Use when building Kotlin Multiplatform (KMP) shared modules, integrating with iOS, or sharing business logic across platforms."
category: architecture
risk: low
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@kmp"
    - "kotlin-multiplatform"
    - "common-main"
    - "shared-module"
    - "expect-actual"
---

# Android Kotlin Multiplatform (KMP) 🌍🤝

Professional patterns for sharing code between Android and iOS using the next-generation Kotlin Multiplatform technology.

## ⚡ When to Use
- **Shared Business Logic**: Centralizing ViewModels, Use Cases, and Domain Models.
- **Data Layer Sharing**: Using Ktor (Network) and SQLDelight (Database) across platforms.
- **Modularization**: Creating a cross-platform library module.
- **Migration**: Moving from 100% native to shared logic.
- **Validation**: Building one logic for both apps (e.g., Auth, Calculations).

## 🏗️ The Multiplatform Architecture

- **`commonMain`**: The heart of the app. Pure Kotlin code shared by all platforms.
- **`androidMain`**: Platform-specific implementation for Android.
- **`iosMain`**: Platform-specific implementation for iOS (via Kotlin/Native).

## 🛠️ Essential Shared Tools

### 1. Ktor (Networking)
- **Benefit**: Async, multiplatform HTTP client.
- Use `ContentNegotiation` and `Serialization` for shared DTOs.

### 2. SQLDelight (Local Persistence)
- **Benefit**: Type-safe SQL queries that generate Kotlin code.
- Shared schema, platform-specific drivers (SQLite for Android, Native for iOS).

### 3. Koin (Dependency Injection)
- **Benefit**: Simple and lightweight DI that works across `commonMain`.

### 4. kotlinx-datetime
- Use for consistent date/time logic without platform-specific issues (java.time vs NSDate).

## 🚀 The `expect` / `actual` Pattern

- Use for platform-specific APIs when no shared library exists.
- **Rule**: Avoid `expect`/`actual` if a shared library is available.
- **Bad**: `expect fun getPlatformName(): String`
- **Good**: Use **interfaces** and **DI** to provide platform-specific implementations.

## 🏁 Shared Logic Workflow

- [ ] **ViewModel Sharing**: Use `multiplatform-viewmodel` library for consistent lifecycle mapping.
- [ ] **State Management**: Use `StateFlow` in `commonMain` to expose UI state.
- [ ] **iOS Interoperability**: Be aware of Swift/Kotlin memory management and `@ObjCName` for clean iOS APIs.

## 📦 Gradle Configuration

```kotlin
kotlin {
    androidTarget()
    iosX64()
    iosArm64()
    iosSimulatorArm64()

    sourceSets {
        commonMain.dependencies {
            implementation("io.ktor:ktor-client-core:2.3.0")
        }
    }
}
```

## 🧪 Testing with KMP

- Tests in `commonTest` run on both Android and iOS targets.
- Use `kotlin.test` for standard assertions (`assertTrue`, `assertEquals`).
- Mocking: Use libraries like **Mockative** or **KMock** for multiplatform mocking.

## 🔗 Related Resources
- [KMP Official Guide](https://kotlinlang.org/docs/multiplatform.html)
- [KMP Samples (By JetBrains)](https://github.com/Kotlin/kmp-samples)
- [Clean Architecture Skill](../android-clean-architecture/SKILL.md)
