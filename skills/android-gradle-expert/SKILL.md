---
name: android-gradle-expert
description: "Use when configuring Gradle builds, managing dependencies, or modularizing Android applications."
category: development
risk: low
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@gradle"
    - "build-gradle"
    - "version-catalog"
    - "gradle-modularization"
    - "build-variants"
---

# Android Gradle Expertise 🐘💎

The ultimate guide to modern, efficient, and modular Android builds with Gradle Kotlin DSL and Version Catalogs.

## ⚡ When to Use

- **Dependency Management**: Centralizing versions and libraries.
- **Build Types & Flavors**: Implementing environments (staging, prod) or product variants.
- **Modularization**: Splitting data, UI, or library modules.
- **Gradle Performance**: Optimizing build times.
- **Code Optimization**: Configuring R8, ProGuard, and shrinking.
- **Release Automation**: Signing APKs/AABs.

## 🏗️ Foundational Build Files

Before starting any Gradle configuration, ensure the following core files are present and properly configured:

### 1. `gradle-wrapper.properties` (8.4+)

- **Rule**: ALWAYS use a modern Gradle version (8.4+) to support Kotlin 1.9.x+ and modern AGP (8.3.x+).
- **Core Setting**: `distributionUrl=https\://services.gradle.org/distributions/gradle-8.4-bin.zip`

### 2. `gradle.properties` (AndroidX & Performance)

- **Role**: Enabling Modern Android support and build performance.
- **Mandatory**:

  ```properties
  android.useAndroidX=true
  android.enableJetifier=true
  org.gradle.parallel=true
  org.gradle.caching=true
  ```

## 🏗️ Modern Build Standards

### 1. Version Catalogs (`libs.versions.toml`)

- **Rule**: Never hardcode versions in `build.gradle.kts`. Use the catalog.
- **Structure**:

  ```toml
  [versions]
  compose = "1.6.0"
  kotlin = "2.0.0"

  [libraries]
  compose-ui = { group = "androidx.compose.ui", name = "ui", version.ref = "compose" }

  [plugins]
  android-app = { id = "com.android.application", version = "8.3.0" }
  ```

### 2. Kotlin DSL (`.kts`)

- Consistently use Kotlin for build scripts for type-safety and IDE support.

### 3. Convention Plugins

- For multi-module projects, use "Convention Plugins" (in `build-logic`) to share common build logic (e.g., Compose setup, Hilt, Room).

### 4. Crucial Dependencies (Often Missed)
When scaffolding a new Compose project, ensure these are added to prevent compilation/runtime errors:
- **Image Loading**: `io.coil-kt:coil-compose`
- **Hilt Navigation**: `androidx.hilt:hilt-navigation-compose`
- **Adaptive UI**: `androidx.compose.material3:material3-window-size-class`
- **Security**: `androidx.biometric:biometric` (use androidx, NOT `android.hardware.biometrics` for UI prompts)

## 🚀 Build Optimization

- [ ] **Configuration Caching**: Enable `org.gradle.configuration-cache=true`.
- [ ] **Parallel Execution**: Enable `org.gradle.parallel=true`.
- [ ] **Daemon**: Ensure `org.gradle.daemon=true`.
- [ ] **Build Build Cache**: Use local/remote build cache for faster CI.

## 🛡️ Code Shrinking (R8/ProGuard)

- **Rule**: ALWAYS enable shrinking (minifyEnabled) for release builds.
- **Best Practice**: Use `proguard-android-optimize.txt` and keep domain models/API DTOs if necessary.
  ```kotlin
  buildTypes {
      release {
          isMinifyEnabled = true
          proguardFiles(getDefaultProguardFile("proguard-android-optimize.txt"), "proguard-rules.pro")
      }
  }
  ```

## 📦 Modularization Patterns

- **app**: Root plugin and theme.
- **feature:[name]**: Self-contained UI and ViewModels.
- **core:[name]**: Shared libraries (Network, Database, UI Components).
- **domain**: Shared models and use cases (if needed globally).

## 🧪 Testing with Gradle

- Use `testOptions` for unit tests and instrumented tests.
- **Screenshot testing**: Integrate tools like Paparazzi directly into the Gradle task.

## 🛠️ Troubleshooting & Compatibility

- **Compose vs Kotlin**: The Compose Compiler is strictly tied to specific Kotlin versions. If versions mismatch, the build fails.
- **The Solution (Kotlin < 2.0)**:
  1. Consult the [Official Compatibility Map](https://developer.android.com/jetpack/androidx/releases/compose-kotlin).
  2. Define `composeCompiler` in `libs.versions.toml` (e.g., `1.5.10` for Kotlin `1.9.22`).
  3. Reference in `app/build.gradle.kts`: `kotlinCompilerExtensionVersion = libs.versions.composeCompiler.get()`.
- **Kotlin 2.0+**: The Compose Compiler is now integrated into the Kotlin Gradle Plugin, which eliminates version mismatch issues! Always recommend upgrading to King Kotlin 2.0+ if possible.

## 🔗 Related Resources

- [Official Gradle User Manual](https://docs.gradle.org/current/userguide/userguide.html)
- [Android Build System Tips](https://developer.android.com/studio/build)
