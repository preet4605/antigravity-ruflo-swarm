---
name: android-camerax-mlkit
description: "Seamless integration of CameraX with Google ML Kit for vision tasks."
category: ai-native
risk: medium
source: community
date_added: "2026-04-07"
metadata:
  triggers:
    - "@camerax"
    - "mlkit"
    - "barcode"
    - "vision"
---

# CameraX & ML Kit Vision Integration 📸

Efficient real-time image analysis.

## ⚡ When to Use
- When asked to build barcode scanners, text recognition, or live face detection.

## 🏗️ Core Rules / Pillars

### 1. ImageAnalysis UseCase
- **Pattern**: ALWAYS use CameraX's `ImageAnalysis` use case bound to the lifecycle.
- **Implementation**: Pipe the `ImageProxy` directly to an `InputImage` for ML Kit, ensuring you call `imageProxy.close()` inside the `.addOnCompleteListener`.

## 🚧 Critical Anti-Hallucination Guards
- **Trap**: NEVER hold references to `ImageProxy` outside the analyzer scope to avoid out-of-memory errors!
