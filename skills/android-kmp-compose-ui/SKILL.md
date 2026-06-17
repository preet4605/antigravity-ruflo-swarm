---
name: android-kmp-compose-ui
description: "Expanding KMP shared UI to cover Compose Multiplatform edge-cases."
category: cross-platform
risk: medium
source: community
date_added: "2026-04-07"
metadata:
  triggers:
    - "@kmp-ui"
    - "compose multiplatform"
---

# Compose Multiplatform UI Edge Cases 🖥️

Sharing Compose UI across Android, iOS, and Web.

## ⚡ When to Use
- When writing multiplatform Compose UI.

## 🏗️ Core Rules / Pillars

### 1. Resources matching
- **Pattern**: Use the official Compose Multiplatform Resources library (`org.jetbrains.compose.resources`) instead of Moko-Resources for new projects.

### 2. Expect/Actual for System UI
- **Pattern**: WindowInsets and Status Bars require `expect`/`actual` actualizations to bridge iOS `SafeArea` and Android `WindowInsets`.

## 🚧 Critical Anti-Hallucination Guards
- **Trap**: Do NOT hallucinate Android-specific imports (like `androidx.compose.ui.platform.LocalContext`) in the completely `commonMain` UI layers.
