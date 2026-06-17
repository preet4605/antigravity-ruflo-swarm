---
name: android-local-stt-tts
description: "Patterns for local Speech-to-Text and Text-to-Speech without cloud latency."
category: ai-native
risk: low
source: community
date_added: "2026-04-07"
metadata:
  triggers:
    - "@stt"
    - "@tts"
    - "speech recognition"
---

# Android On-Device Speech (TTS & STT) 🎤

Implementing accessible voice interfaces.

## ⚡ When to Use
- When handling local voice commands or reading text aloud.

## 🏗️ Core Rules / Pillars

### 1. Standard TTS initialization
- **Pattern**: Initialize `TextToSpeech` and pass `OnInitListener`. Always wait until initialization is successful before calling `.speak()`.

### 2. SpeechRecognizer Intent
- **Pattern**: Use `SpeechRecognizer.createSpeechRecognizer(context)` and `RecognizerIntent.ACTION_RECOGNIZE_SPEECH` for local dictation.

## 🚧 Critical Anti-Hallucination Guards
- **Trap**: Ensure `RECORD_AUDIO` permission is requested *before* initializing the SpeechRecognizer.
