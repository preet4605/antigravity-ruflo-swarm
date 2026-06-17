---
name: android-macrobenchmark
description: "Use when evaluating App Startup Time, frame timing, and writing Baseline Profiles."
category: performance
risk: medium
source: community
date_added: "2026-04-07"
metadata:
  triggers:
    - "@macrobenchmark"
    - "baseline profile"
    - "app startup time"
---

# Android Macrobenchmark & Baseline Profiles 🏎️

App Startup Time and UI performance are crucial. Macrobenchmark allows us to write standard JUnit 4 tests to measure end-to-end user journeys (like app startup or scrolling a list) and automatically generate Baseline Profiles that Android's ART uses to pre-compile critical code.

## ⚡ When to Use

- When the prompt mentions "speeding up app startup time"
- When writing a Macrobenchmark module
- When generating or applying Baseline Profiles (`baseline-prof.txt`)

## 🏗️ Core Rules / Pillars

### 1. Separate Macrobenchmark Module

- **Pattern**: Macrobenchmarks MUST be in a separate `com.android.test` module. They launch your application by its `applicationId` externally.
- **Anti-Pattern**: Do NOT attempt to run Macrobenchmark tests inside the standard `app/src/androidTest` directory.

### 2. Writing a Scrolling Benchmark

- **Implementation**:
  ```kotlin
  @RunWith(AndroidJUnit4::class)
  class ScrollBenchmark {
      @get:Rule
      val benchmarkRule = MacrobenchmarkRule()

      @Test
      fun scrollTimeline() = benchmarkRule.measureRepeated(
          packageName = "com.example.app",
          metrics = listOf(FrameTimingMetric()),
          iterations = 5,
          startupMode = StartupMode.COLD
      ) {
          pressHome()
          startActivityAndWait()
          
          // Using UIAutomator to find the scrollable list and scroll
          val list = device.findObject(By.res("com.example.app", "timeline_list"))
          list.setGestureMargin(device.displayWidth / 5)
          list.fling(Direction.DOWN)
      }
  }
  ```

## 🚧 Critical Anti-Hallucination Guards

- **Trap**: Baseline Profiles generation requires a rooted device OR a device running **Android 13 (API 33)**+. 

## 🔗 Related Resources
- [Macrobenchmark Documentation](https://developer.android.com/topic/performance/benchmarking/macrobenchmark-overview)
