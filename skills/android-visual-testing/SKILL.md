---
name: "android-visual-testing"
description: "Use when implementing visual regression tests, verifying UI layouts, or using Paparazzi/Roborazzi for Android."
category: testing
risk: low
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@screenshot-testing"
    - "paparazzi-testing"
    - "roborazzi-testing"
    - "visual-regression"
    - "ui-verification"
---

# Android Screenshot Testing 📸🛡️

Expert techniques for implementing visual regression testing to ensure UI consistency and catch unintended layout changes automatically.

## ⚡ When to Use
- **UI Consistency**: Verifying complex layouts across screen sizes.
- **Visual Regression**: Catching pixel-level changes in CI/CD.
- **Design System Audit**: Verifying components against design specs.
- **Screenshot Automation**: Generating millions of UI variants (Dark mode, RTL, Font scales).
- **Test-Driven Design**: Testing UI before deploying to devices.

## 🏗️ Core Tools

### 1. Paparazzi (Cash App)
- **Benefit**: Runs entirely on the JVM (Host). NO DEVICE/EMULATOR REQUIRED.
- **Use Case**: Testing Jetpack Compose components fast and frequently.
- **Gradle Task**: `./gradlew recordPaparazziDebug` / `./gradlew verifyPaparazziDebug`

### 2. Roborazzi (Droidkaigi)
- **Benefit**: Works with Robolectric and provides screenshots in standard unit tests.
- **Use Case**: Testing with existing Robolectric mocks and complex native view hierarchies.

### 3. Showkase (Airbnb)
- **Benefit**: Auto-generates a library of previews for your app's design system.
- **Use Case**: Creating a "living design system" documentation.

## 📐 Screenshot Strategy

### 1. The "Base" Screenshot
- Record a "Golden Screenshot" that represents the correct state.
- **Rule**: Commit these screenshots to your repository.

### 2. Verification (The Diff)
- The test compares the current output with the "Golden" version.
- Any pixel difference (even 1px) will cause the test to fail.
- Use **Redline** or **Side-by-side** views to inspect failures.

## 🚀 Modern Screenshot Workflow

- [ ] **Multi-config Previews**: Test every component in:
  - Light vs. Dark mode.
  - Large font scales (Accessibility).
  - RTL (Right-to-Left) languages.
  - Different screen densities (ldpi to xxxhdpi).
- [ ] **Data Mocking**: Use hardcoded, stable mocks for screenshots (Avoid dynamic dates or network data).
- [ ] **Stable Animations**: Disable animations or use `FixedTime` during screenshot capture to avoid timing issues.

## 📦 Gradle Configuration

```kotlin
plugins {
    id("app.cash.paparazzi") version "1.3.1"
}

paparazzi {
    // Optional: customize screen size or theme
    deviceConfig = DeviceConfig.PIXEL_5
}
```

## 🧪 Testing Best Practices

- **Atomic Components**: Favor testing individual atoms (e.g., buttons, chips) over full screens.
- **CI/CD Integration**: Automatically run `./gradlew verifyPaparazziDebug` on every Pull Request.
- **Review Workflow**: Use tools like **GitHub PR comments** to display screenshot diffs directly to reviewers.

## 🔗 Related Resources
- [Paparazzi Documentation](https://github.com/cashapp/paparazzi)
- [Roborazzi Documentation](https://github.com/takahirom/roborazzi)
- [Unit Testing Skill](../android-unit-testing/SKILL.md)
