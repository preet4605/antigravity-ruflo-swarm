---
name: android-code-review-expert
description: "Use when performing a code review for Android pull requests, focusing on architecture, memory safety, and UI excellence."
category: quality
risk: low
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@code-review"
    - "review-pr"
    - "diff-analysis"
    - "security-check"
    - "performance-check"
---

# Android Code Review Excellence 🧐🛡️

A rigorous framework for AI agents and developers to perform high-quality, professional Android code reviews.

## ⚡ When to Use

- **PR Review**: Analyzing a Pull Request for logic, style, and regressions.
- **Pre-commit Audit**: Self-checking code before pushing.
- **Architectural Check**: Ensuring new features follow the established team patterns.
- **Security Audit**: Spotting sensitive data exposure or insecure networking.
- **Performance Audit**: Detecting potential memory leaks or UI jank.

## 🏗️ Review Checklist

### 1. Architecture & Design

- [ ] **Clean Architecture**: Is logic properly separated into Domain/Data/Presentation?
- [ ] **State Flow**: Does the ViewModel expose `StateFlow`? Is state properly hoisted?
- [ ] **Dependency Injection**: Are dependencies injected via Hilt/Koin? No manual `new Class()` for dependencies.
- [ ] **Manifest Scaffolding**: Are required permissions (like `INTERNET` for Coil/Retrofit) actually defined? Is the `@HiltAndroidApp` class correctly designated in `AndroidManifest.xml` via `android:name`?
- [ ] **Type-Safe Navigation**: Is the app using Compose `NavHost` with Kotlin Serialization (type-safe routes) instead of anti-pattern manual state swapping?
- [ ] **Modularity**: Is the code placed in the correct module?

### 2. Jetpack Compose (UI)

- [ ] **Recomposition**: Are there expensive calculations inside `@Composable`? Use `remember`.
- [ ] **Previews**: Does the new component have `@Preview` for light/dark mode and accessibility?
- [ ] **Stability**: Are domain models marked `@Stable` or `@Immutable`?
- [ ] **Material 3**: Is the code using the theme's `MaterialTheme.colorScheme` instead of hardcoded hex values?
- [ ] **Theme Bridge**: If XML resources are used (e.g. `res/`), is the **Material Components XML Bridge** correctly set up in themes?

### 3. Stability & Networking

- [ ] **Error Handling**: Are network calls wrapped in `Result` or `try/catch` with proper UI feedback?
- [ ] **Coroutine Scopes**: Use `viewModelScope` for ViewModels and `lifecycleScope` for Fragments/Activities.
- [ ] **Flow Lifecycle**: Is `collectAsStateWithLifecycle()` used instead of base `collectAsState()`? (Critical for avoiding resource leaks when the app goes into the background).
- [ ] **Room TypeConverters**: If caching domain models with complex definitions (e.g. `LocalDateTime`, `List<String>`), did you verify a `@TypeConverter` is written and registered on the Database? ROOM WILL CRASH without this.

### 4. Performance & Memory

- [ ] **Memory Leaks**: Are there references to `Context` held in long-lived objects?
- [ ] **Lazy Lists**: Are `key` parameters provided for `items()` in `LazyColumn`/`LazyRow`?
- [ ] **Heavy Work**: Is heavy computation moved to `Dispatchers.Default`?

### 5. Security & Privacy

- [ ] **Sensitive Data**: Ensure NO passwords, keys, or PII are logged or stored in plain text.
- [ ] **Networking**: Is all communication over HTTPS? No `cleartextTraffic` allowed.
- [ ] **Permissions**: Is the app requesting minimum necessary permissions?

## 📜 Reviewer Best Practices

- **The "Why", Not Just the "What"**: Explain the reasoning behind a request (e.g., "Use `remember` here to prevent re-calculating on every frame").
- **Prioritize**: Distinguish between "Critical" (security, crashes) and "Nitpick" (formatting, naming).
- **Compliment**: Acknowledge good code, elegant solutions, and clear documentation.

## 🧪 Verification Commands (For Agents)

### Check Lint

  ```bash
  ./gradlew lintDebug
  ```

### Check Style

  ```bash
  ./gradlew ktlintCheck
  ```

### Run Logic Tests

  ```bash
  ./gradlew testDebugUnitTest
  ```

## 🔗 Related Resources
- [Google Official Review Guide](https://google.github.io/eng-practices/review/)
- [Lint & Quality Skill](../android-lint-and-quality/SKILL.md)
