---
name: android-lint-and-quality
description: "Use when setting up static analysis, enforcing coding standards, or configuring Detekt/KtLint for Android."
category: quality
risk: low
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@lint-quality"
    - "detekt"
    - "ktlint"
    - "custom-lint-rules"
    - "coding-standards"
---

# Android Code Quality & Linting 🧹🛡️

Professional strategies for enforcing team standards and preventing technical debt through automated static analysis.

## ⚡ When to Use
- **Code Review Readiness**: Automatically checking Pull Requests for common errors.
- **Enforcing Style**: Ensuring all developers follow the same Kotlin formatting.
- **Complex Bug Prevention**: Using custom Lint rules to catch project-specific issues.
- **CI/CD Automation**: Failing builds on logic or style violations.
- **Gradual Refactoring**: Deprecating legacy methods and encouraging migration.

## 🏗️ The 3 Layers of Analysis

### 1. Android Lint (Built-in)
- **Rules**: Catch memory leaks, missing accessibility labels, and incorrect resource usages.
- **Customization**: Use `lint-rules` module to write your own rules specific to your app architecture.

### 2. Detekt (Core Logic Static Analysis)
- **Benefit**: Checks for code smells (Long methods, deep nested loops, cognitive complexity).
- **Gradle Task**: `./gradlew detekt`

### 3. KtLint (Formatting)
- **Benefit**: Focuses purely on coding style (Indentation, line length, spacing).
- **Rule**: Follow the **Official Android Kotlin Style Guide**.
- **Gradle Task**: `./gradlew ktlintCheck` / `./gradlew ktlintFormat`

## 🚀 Quality Enforcement Checklist

- [ ] **Fail Fast**: Set `abortOnError = true` in Gradle to ensure bad code never stays in the repo.
- [ ] **Custom Rules**: For example: "No `Log.d` allowed in production" or "All ViewModels must inherit from `BaseViewModel`".
- [ ] **Baseline Files**: Use `baseline.xml` to ignore existing issues in older code and only enforce rules on new changes.

## 🛠️ Configuration Example

```kotlin
// build.gradle.kts
lint {
    isWarningsAsErrors = true
    isAbortOnError = true
    xmlReport = true
    htmlReport = true
}

detekt {
    buildUponDefaultConfig = true
    allRules = false
    config = files("$projectDir/config/detekt.yml")
}
```

## 📐 Team Policy Best Practices

- **Pre-commit Hooks**: Use `Git Hooks` to run KtLint locally before pushing.
- **CI Report Annotation**: Configure CI (e.g., GitHub Actions) to comment directly on PR lines with Lint/Detekt findings.
- **Quality Gates**: Maintain a score using tools like **SonarQube** or **Codecov**.

## 🧪 Testing Your Quality Setup

- **Lint Tests**: Use `LintDetectorTest` to verify that your custom rules actually catch what they should.
- **Baseline Evolution**: Regularly review and clean up baseline files to pay down technical debt.

## 🔗 Related Resources
- [Android Lint Official Guide](https://developer.android.com/studio/write/lint)
- [Detekt Documentation](https://detekt.dev)
- [KtLint Documentation](https://pinterest.github.io/ktlint)
