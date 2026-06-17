---
name: android-development
description: (Meta-Orchestrator) Triggers on requests to "build using android development skills". Coordinates and applies the 9 Android development, performance, and UI polish skills to construct production-ready Android apps.
risk: medium
source: custom-orchestrator
date_added: 2026-06-10
---

# Android Development (Meta-Orchestrator)

Use this skill whenever the user requests to **"build using android development skills"** or asks you to construct, refactor, or polish an Android application. This meta-skill forces the agent to activate, coordinate, and apply the 9 specialized Android skills in unison.

## Trigger Phrase
Matches: `build using android development skills` or `build an android app` or `android development skills`.

---

## The 9 Android Development Skills Checklist

When building or modifying any Android application, you MUST systematically apply the following 9 capabilities:

1. **`android-clean-architecture`**: Separate Presentation, Domain, and Data layers. Use unidirectional data flows via ViewModels with StateFlow.
2. **`android-design-system-m3`**: Enforce Material 3 token-based styling. Implement dynamic Material You overrides; reject raw hex constants.
3. **`android-jetpack-compose`**: Build interfaces exclusively using Jetpack Compose. Implement Edge-to-Edge window structures and Navigation 3 component trees.
4. **`android-responsive-layouts`**: Set layout sizes relative to `WindowSizeClass` brackets to support foldables and tablets.
5. **`android-motion-animations`**: Implement Shared Element transitions, physics-based springs (`spring()`), and custom Canvas drawing via graphicsLayer to maintain 120 FPS.
6. **`android-offline-first`**: Query UI data solely from the local database (Room/SQLDelight). Setup background WorkManager sync updates.
7. **`android-performance-polish`**: Check Compose compiler stability metrics, optimize recompositions, and create Baseline Profiles.
8. **`android-visual-testing`**: Deploy Compose test rules and Roborazzi/Paparazzi screenshot tests.
9. **`design-polish`**: Audits components iteratively against spacing parameters, touch target scales, and contrasts.

---

## Step-by-Step Implementation Workflow

To execute any Android development task, structure your planning and coding phases as follows:

### Step 1: Core Architecture & Cache Setup
- **Action**: Scaffold folders, repositories, local databases, and preferences.
- **Skills**: `[android-clean-architecture, android-offline-first]`
- **Requirements**: Define Room tables, DAO methods, Repository syncing, and StateFlow ViewModels.

### Step 2: UI Drafting & Navigation
- **Action**: Build Compose screens and link Navigation 3.
- **Skills**: `[android-jetpack-compose, android-responsive-layouts]`
- **Requirements**: Enforce Edge-to-Edge layout styling and adaptive column configurations.

### Step 3: Material 3 Theme & Motion
- **Action**: Connect themes and dynamic transitions.
- **Skills**: `[android-design-system-m3, android-motion-animations]`
- **Requirements**: setup dynamic color overrides, shared elements, and custom spring animations.

### Step 4: Optimization & Profiling
- **Action**: Minimize recompositions and compile Baseline Profiles.
- **Skills**: `[android-performance-polish]`
- **Requirements**: Annotate parameter stability and compile initial cold-start optimizations.

### Step 5: Auditing, Tests, & Verification
- **Action**: Verify layout dimensions, contrasts, and screenshot checks.
- **Skills**: `[design-polish, android-visual-testing]`
- **Requirements**: Run compose tests, capture regression screenshots, and check touch target compliance.
