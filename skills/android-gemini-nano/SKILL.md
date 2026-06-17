---
name: android-gemini-nano
description: "Use when integrating Google Gemini Nano via AICore for on-device ML."
category: ai-native
risk: medium
source: community
date_added: "2026-04-07"
metadata:
  triggers:
    - "@gemini-nano"
    - "aicore"
    - "on-device ai"
---

# Android Gemini Nano On-Device Integration 🧠

Gemini Nano allows for powerful, completely on-device AI generation. Because it runs locally via the AICore Android system service, careful life-cycle and asynchronous resource management is required.

## ⚡ When to Use

- When building chat interfaces, generating summaries, or drafting text without cloud latency.
- When the user asks to integrate "Gemini Nano" or "AICore".

## 🏗️ Core Rules / Pillars

### 1. AICore Dependency and Availability Check

- **Pattern**: AICore might not be downloaded or fully initialized. Always check availability before starting a session.
- **Implementation**:
  ```kotlin
  val generativeModel = GenerativeModel("gemini-nano")
  
  // ALWAYS verify availability first
  val isAvailable = generativeModel.isAvailable()
  if (!isAvailable) {
      // Request download or show fallback UI
  }
  ```

### 2. Streaming Responses with Flow
- **Pattern**: Because generation can take time on low-end devices, always use `generateContentStream` to stream the UI update instead of waiting for the full response.
- **Anti-Pattern**: NEVER block the main thread.
- **Implementation**:
  ```kotlin
  viewModelScope.launch {
      generativeModel.generateContentStream(prompt)
          .catch { e -> handleError(e) }
          .collect { chunk ->
              _uiState.update { it.copy(text = it.text + chunk.text) }
          }
  }
  ```

## 🚧 Critical Anti-Hallucination Guards

- **Trap**: `GenerativeModel` is part of the `com.google.ai.client.generativeai` SDK. Do NOT hallucinate custom `AICoreManager` wrapper singletons.

## 🔗 Related Resources
- [Google AI Edge / AICore SDK](https://developer.android.com/ai/custom/aicore)
