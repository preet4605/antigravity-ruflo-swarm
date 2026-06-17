---
name: android-jetpack-compose
description: "Use when creating, refactoring, or optimizing Android UI components using Jetpack Compose."
category: development
risk: low
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@jetpack-compose"
    - "compose-ui"
    - "build-screen"
    - "material-3"
    - "composable"
---

# Android Jetpack Compose Excellence 🎨

Expert guidance for building modern, high-performance Android UI with Jetpack Compose.

## ⚡ When to Use

- **New Feature UI**: Starting a new screen or custom component.
- **UI Refactoring**: Moving from XML to Compose or legacy Compose to modern patterns.
- **Theming**: Implementing Material 3, Dark Mode, or Custom Design Systems.
- **Performance Fixes**: Debugging recomposition issues or laggy lists.
- **Animations**: Adding smooth transitions and micro-interactions.

## 🏗️ Core Principles

### 1. State Management (Hoisting)

- **Rule**: Composables should be stateless where possible. Hoist state to the caller.
- **Bad**:
  ```kotlin
  @Composable
  fun SearchBar() {
      val text = remember { mutableStateOf("") } // Local state in reusable component
      TextField(value = text.value, onValueChange = { text.value = it })
  }
  ```
- **Good**:
  ```kotlin
  @Composable
  fun SearchBar(
      query: String,
      onQueryChange: (String) -> Unit
  ) {
      TextField(value = query, onValueChange = onQueryChange)
  }
  ```

### 2. Slot API Pattern

- For complex components, use "Slots" (content parameters) to increase flexibility.
  ```kotlin
  @Composable
  fun AppHeader(
      title: @Composable () -> Unit,
      actions: @Composable RowScope.() -> Unit = {}
  ) { ... }
  ```

### 3. Material 3 (M3)

- Always prefer `androidx.compose.material3` components.
- Use `ColorScheme`, `Typography`, and `Shapes` from the theme.

## 🚀 Performance Checklist

- [ ] **Lambda Stability**: Method references (`::onAction`) or bound lambdas `(val -> action(val))` are safer for stability than capturing unstable variables.
- [ ] **derivedStateOf**: Use when a state depends on another state that changes frequently (e.g., scroll position).
- [ ] **remember(key)**: Correctly keying `remember` blocks to avoid stale data.
- [ ] **Lists**: Use `LazyColumn` / `LazyRow` and ALWAYS provide a `key` to `items`.

## 🎨 Animations

- `AnimatedVisibility`: For simple appear/disappear.
- `animateColorAsState`: For smooth color changes.
- `Transition`: For complex, multi-state animations.
- `Lottie`: Use `lottie-compose` for complex vector animations.

## 🧪 Testing and Previews

- **Previews**: Use `@Preview(showBackground = true, uiMode = Configuration.UI_MODE_NIGHT_YES)` for dark mode testing.
- **Multi-device Previews**: Use `@PreviewScreenSizes` and `@PreviewFontScales`.
- **UI Testing**: Use `createComposeRule()` and `onNodeWithTag()`.

## 🔗 Related Resources

- [Google Official Compose Samples](https://github.com/android/nowinandroid)
- [Clean Architecture Skill](../android-clean-architecture/SKILL.md)
