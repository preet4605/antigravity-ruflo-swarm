---
name: "android-responsive-layouts"
description: "Use when supporting tablets, foldables, and different screen sizes in Android apps with Jetpack Compose."
category: ui-ux
risk: low
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@adaptive-layout"
    - "tablet-support"
    - "foldable-devices"
    - "window-size-class"
    - "canonical-layouts"
---

# Android Adaptive Layouts 📱💻💻

Professional strategies for building flexible, responsive Android applications that scale beautifully from phones to tablets and foldables.

## ⚡ When to Use
- **Multi-Device Support**: Designing a UI that works on all screen sizes.
- **Foldable Support**: Adapting layout based on hinge position (Tabletop mode).
- **Tablet Optimization**: Using extra screen space for "List-Detail" or complex dashboards.
- **ChromeOS Support**: Adapting for resizable desktop-style windows.
- **Dynamic Orientation**: Handling rotations without losing state.

## 🏗️ The 3 Window Size Classes

1.  **Compact (Phone)**: 0-599dp width. Single column.
2.  **Medium (Small Tablet/Large Phone)**: 600-839dp width. Navigation rail or multi-pane.
3.  **Expanded (Large Tablet/Desktop)**: 840dp+ width. Fixed navigation drawer or complex dashboards.

## 🛠️ Canonical Layouts (Google Standard)

### 1. List-Detail
- **Compact**: Shows list, then navigate to detail screen.
- **Expanded**: Side-by-side list and detail (always visible).

### 2. Supporting Pane
- **Expanded**: Central work area with a persistent tool or info pane beside it.

### 3. Feed/Grid
- **Compact**: 1-2 columns.
- **Expanded**: 4-6 columns with responsive grid margins.

## 🚀 Adaptive Layout Tools

### 1. `WindowSizeClass` (Material 3)
- **Benefit**: Automatically categorizes the current window size.
- **Use Case**: Decide which UI to show based on `calculateWindowSizeClass()`.

### 2. `TwoPaneLayout` (Foldable Support)
- **Benefit**: Automatically handles display on single-screen vs dual-screen/foldable devices.
- **Rule**: Give content weights (e.g., list = 1, detail = 2).

## 📐 Layout Execution Best Practices

- [ ] **Responsive Grid**: Use `FlowRow` and `FlowColumn` for wrapping content automatically.
- [ ] **Dynamic Margins**: Use larger horizontal margins (e.g., 24dp or 32dp) for wider screens.
- [ ] **Modal Bottom Sheets**: Convert `ModalBottomSheet` (Phone) into `NavigationDrawer` or `ModalNavigationDrawer` (Tablet).
- [ ] **Fixed Content Width**: For text content, avoid full-screen width on tablets (Keep it between 400dp and 600dp for readability).

## 🧪 Testing and Previews

- **`@PreviewScreenSizes`**: Use this annotation to see your UI on every standard device.
- **`@PreviewFontScales`**: Check how your responsive layout handles large accessibility fonts.
- **Physical Foldables**: If no device is available, use the "Foldable" emulator in Android Studio.

## 📜 Checklist for Adaptive Design

- [ ] **Touch Targets**: Ensure targets are easy to hit even when scaled up.
- [ ] **Continuity**: Does the app state persist when the device is unfolded or rotated?
- [ ] **Input Methods**: Is the UI easy to use with a mouse, keyboard, or stylus (not just touch)?
- [ ] **Aspect Ratios**: Does the UI handle ultra-wide or ultra-narrow (split-screen) windows?

## 🔗 Related Resources
- [Android Adaptive Layouts Guide](https://developer.android.com/guide/topics/ui/adaptive)
- [Canonical Layout Patterns](https://developer.android.com/guide/topics/ui/layout/canonical-layouts)
- [Window Size Classes Documentation](https://developer.android.com/guide/topics/ui/layout/window-size-classes)
