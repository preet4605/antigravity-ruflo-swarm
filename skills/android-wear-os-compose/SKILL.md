---
name: android-wear-os-compose
description: "Jetpack Compose for Wear OS, rotary input, and ambient modes."
category: hardware-form-factors
risk: medium
source: community
date_added: "2026-04-07"
metadata:
  triggers:
    - "@wearos"
    - "watch app"
    - "wear compose"
---

# Wear OS Compose & Hardware Inputs ⌚

Building for the wrist comes with entirely new constraints regarding battery life, input mechanisms, and screen real estate.

## ⚡ When to Use
- When asked to build a Wear OS companion app or standalone watch app.

## 🏗️ Core Rules / Pillars

### 1. Wear Compose Dependencies
- **Pattern**: Standard compose material will look incorrect and tiny on Wear OS. ALWAYS use `androidx.wear.compose:compose-material` or `compose-material3` specifically meant for watches.
- **Implementation**: Instead of `Scaffold`, use `Scaffold` from the Wear OS library which includes a `TimeText` and `PositionIndicator`.

### 2. Rotary Input (Crown support)
- **Pattern**: Scrolling lists MUST support the physical rotating crown on the watch.
- **Implementation**: Combine `ScalingLazyColumn` with `.rotaryScrollable()` modifier to capture hardware scroll events continuously.

## 🚧 Critical Anti-Hallucination Guards
- **Trap**: Do not hallucinate massive long-running background workers for Wear OS! Always use Google Play Services `DataClient` or `MessageClient` to safely proxy network requests to the attached phone to save watch battery life.
