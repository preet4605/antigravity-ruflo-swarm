---
name: "android-performance-polish"
description: "Use when profiling Android apps, debugging memory leaks, optimizing Compose UI, or improving app startup time."
category: performance
risk: low
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@performance"
    - "memory-leak"
    - "profiling"
    - "startup-time"
    - "recomposition-tracking"
---

# Android Performance Auditing 🚀⏱️

Expert strategies for profiling and optimizing Android applications to ensure smooth, responsive, and efficient user experiences.

## ⚡ When to Use
- **UI Lag**: Fixing jank in lists or complex Compose layouts.
- **Memory Issues**: Debugging `OutOfMemoryError` or high memory growth.
- **App Startup**: Reducing the time from icon tap to first usable frame.
- **Battery Drain**: Identifying excessive network calls or background work.
- **Leak Detection**: Investigating persistent objects after activity destruction.

## 🛠️ Main Tools

### 1. Android Studio Profiler
- **CPU Profiler**: Inspect call stacks and thread activity.
- **Memory Profiler**: Capture heap dumps and track allocations.
- **Network Profiler**: Analyze traffic and payload sizes.
- **Energy Profiler**: Monitor battery impact.

### 2. LeakCanary
- **Rule**: ALWAYS include LeakCanary in debug builds.
- Use it to detect memory leaks automatically during development.

## 🎥 Compose Optimization

- [ ] **Recomposition Tracking**: Use the "Layout Inspector" in Android Studio to count recompositions.
- [ ] **Stability Rules**: Use `@Stable` or `@Immutable` on domain models to help the Compose compiler.
- [ ] **Lambda Stability**: Avoid pass-through lambdas that capture unstable variables; use method references where possible.
- [ ] **remember & derivedStateOf**: Minimize expensive calculations within the composition loop.

## 🏁 App Startup Optimization

- **Baseline Profiles**: Use Baseline Profiles to pre-compile critical code paths (AOT) to improve startup by up to 30%.
- **Lazy Initialization**: Use `Lazy` or `Hilt` entry points to avoid unnecessary object creation during `Application.onCreate`.
- **App Startup Library**: Utilize `androidx.startup` for organized component initialization.

## 📦 Memory Management Checklist

- [ ] **Context Leaks**: Ensure no long-lived references to `Activity` context (use `ApplicationContext` if possible).
- [ ] **Bitmap Scaling**: Never load full-resolution bitmaps into small `Image` views. Use **Coil** with `size()` transformations.
- [ ] **Flow/Coroutine Cleanup**: Use `viewModelScope` to ensure background tasks are canceled with the UI.

## 🧪 Benchmarking

- **Macrobenchmark**: Measure high-level user interactions (Startup, Scrolling).
- **Microbenchmark**: Measure isolated code loops or CPU-intensive algorithms.

## 🔗 Related Resources
- [Android Performance Documentation](https://developer.android.com/topic/performance)
- [Baseline Profiles Guide](https://developer.android.com/topic/performance/baselineprofiles/overview)
