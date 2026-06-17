---
name: "android_ui_verification"
description: "MANDATORY verification skill to run after EVERY file change. Automatically triggers an Android build (assembledDebug) to check for compilation or schema errors."
category: quality
risk: medium
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@build-verify"
    - "verify-changes"
    - "changed-files"
    - "build-broken"
    - "compile-check"
---

# Android Build Verification 🛠️🔍

A foundational quality guard for Android AI Agents that ensures no code is committed or merged without a successful compilation.

## ⚡ When to Use

- **After EVERY edit**: After you modify more than 2 files or 20 lines of code.
- **Dependency Changes**: After updating `libs.versions.toml` or `build.gradle.kts`.
- **DI/Schema Changes**: After adding a new `@HiltAndroidApp`, `@Entity`, or `@Dao`.
- **Resource Changes**: If you add new icons or strings to `res/`.

## 🏗️ The Build Workflow

### 1. Fast Compilation Check

- **Command**: `./gradlew assembleDebug --parallel --build-cache`
- **Purpose**: Verify that the entire project compiles.

### 2. Unit Verification

- **Command**: `./gradlew testDebugUnitTest`
- **Purpose**: Ensure that logic didn't regress after the build script was changed.

### 3. Manifest & Resource Consistency (Critical)
- **Hilt Entry Point**: Verify that the `Application` class (annotated with `@HiltAndroidApp`) is registered in `AndroidManifest.xml` under `android:name`.
- **Theme Bridge**: If using Material 3 XML themes, ensure `com.google.android.material:material` is present in dependencies.
- **Icon Resources**: Check that `res/mipmap-anydpi-v26` and `res/drawable` contain valid XML vectors for adaptive icons to avoid AAPT linking errors.

## 🛑 Scaffolding / Empty Project Guardrails

When explicitly tasked to **create a project** or **scaffold a new feature** from scratch, agents MUST verify these items before claiming completion:
1. **Complete Theme Implementation**: Did you actually create `Theme.kt`, `Color.kt`, and `Type.kt`? (Prevents `Theme not found` errors).
2. **Compose Compiler Symmetry**: Did you double-check that the `composeCompiler` version explicitly matches the `kotlin` plugin version in `libs.versions.toml`?
3. **Auxiliary Dependencies**: Did you add the required libraries you referenced? (e.g. `coil-compose`, `hilt-navigation-compose`, `windowsizeclass`).
4. **End-to-End Hookup**: Are all UI buttons calling actual ViewModel methods that hit a Repository, or did you accidentally leave an empty `{ /* TODO */ }` block? Do not leave disconnected UIs.

## 🚀 Performance Strategies

- [ ] **Daemon Speed**: Keep the Gradle daemon warm by running consecutive tasks.
- [ ] **Offline Mode**: If building frequently without dependency changes, use `--offline` to skip network checks.
- [ ] **Task Selection**: If only one module changed (e.g., `:feature:auth`), only build that module: `./gradlew :feature:auth:assembleDebug`.

## 🧪 Error & Symptom Checker

- **"Unresolved Reference"**: Check imports or if the target module is missing from `settings.gradle.kts`.
- **"Duplicate Class"**: Check for version conflicts in `libs.versions.toml`.
- **"Hilt Error"**: Ensure the `@AndroidEntryPoint` or `@Module` classes have the correct annotations and that `kapt` is active.
- **"Room Schema Export"**: Verify if you moved database versioning without updating the `exportSchema` config.

## 📐 Continuous Verification Workflow (For Agents)

- **Step 1**: Make the intended change.
- **Step 2**: Run `./gradlew assembleDebug`.
- **Step 3**: If it fails, fix the code immediately.
- **Step 4**: Report "Build Successful" alongside the code changes to the user.

## 📜 Checklist for Reliability

- [ ] **Local Build**: Did it pass locally before saying "I'm done"?
- [ ] **Syncing**: Did you run `git add .` and commit the new files for the user?
- [ ] **Lint**: Are there no critical lint errors that would prevent a release?

## 🔗 Related Resources
- [Detekt Expert Skill](../android-detekt-expert/SKILL.md)
- [Unit Testing Skill](../android-unit-testing/SKILL.md)
- [Gradle Expert Skill](../android-gradle-expert/SKILL.md)
