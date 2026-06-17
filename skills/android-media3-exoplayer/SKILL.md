---
name: android-media3-exoplayer
description: "Background playing, Audio focus, and PiP mode using Media3."
category: core-android
risk: medium
source: community
date_added: "2026-04-07"
metadata:
  triggers:
    - "@media3"
    - "exoplayer"
    - "video player"
    - "pip"
---

# Android Media3 & ExoPlayer 🎬

Handling streaming audio, video playback, and Picture-in-Picture.

## ⚡ When to Use
- When asked to build video players, music streaming services, or complex media apps.

## 🏗️ Core Rules / Pillars

### 1. Migrating to Media3
- **Pattern**: `com.google.android.exoplayer2` is fully deprecated. You MUST use `androidx.media3:media3-exoplayer`.
- **Implementation**: Instantiate the `ExoPlayer.Builder(context).build()` and strictly manage its lifecycle, hooking it to Compose's `DisposableEffect` to trigger `player.release()` when leaving the screen.

### 2. Audio Focus & Background Playback
- **Pattern**: If building a music app, you MUST use `MediaSession` connected to a Foreground Service.
- **Implementation**: Request Audio Focus automatically using Media3's `player.setAudioAttributes(..., handleAudioFocus = true)` so the player pauses gracefully when a phone call comes in.

## 🚧 Critical Anti-Hallucination Guards
- **Trap**: Do not hallucinate `MediaBrowserServiceCompat`. Media3 replaces the entire legacy MediaSessionCompat stack with a unified `MediaSessionService`.
