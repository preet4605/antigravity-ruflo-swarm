---
name: android-hardware-testing
description: "Automated UIAutomator tests and Hardware mocking setup."
category: testing
risk: medium
source: community
date_added: "2026-04-07"
metadata:
  triggers:
    - "@uiautomator"
    - "hardware test"
    - "e2e"
---

# Android UIAutomator & System Testing 🤖

Testing that extends beyond a single application boundary into the OS itself.

## ⚡ When to Use
- When writing tests spanning multiple apps, interacting with system notifications, or performing Home button interactions.

## 🏗️ Core Rules / Pillars

### 1. UIAutomator Fundamentals
- **Pattern**: Espresso / Compose Rule testing CANNOT interact with System Dialogs (like Permission Popups). You MUST use UIAutomator to click system buttons.
- **Implementation**: Use `UiDevice.getInstance(InstrumentationRegistry.getInstrumentation())` to find notification shades, click permission "Allow" buttons, and press the physical hardware back button.

### 2. Mocking Hardware Sensors
- **Pattern**: End-to-end tests relying on BLE, GPS, or NFC will randomly flake on CI servers.
- **Implementation**: Introduce a Fake/Mock layer behind an interface (e.g., `LocationProvider`) to stub out sensor values during test variants instead of simulating complex location spoofing over ADB.

## 🚧 Critical Anti-Hallucination Guards
- **Trap**: Never use `Thread.sleep()` to wait for a system animation. Always use `UiDevice.wait(Until.hasObject(By.text("Welcome")), 5000)` to ensure tests don't flake on slow emulators.
