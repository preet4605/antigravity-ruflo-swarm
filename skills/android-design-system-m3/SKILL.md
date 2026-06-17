---
name: android-design-system-m3
description: "Use when creating Material 3 design systems, custom themes, or dynamic color implementations in Android apps with Jetpack Compose."
category: ui-ux
risk: low
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@design-system"
    - "material-3"
    - "custom-theme"
    - "dynamic-color"
    - "design-tokens"
---

# Android Design Systems (Material 3) 🎨🛠️

Advanced strategies for building scalable, cohesive, and professional design systems for modern Android applications using the Material 3 (M3) framework.

## ⚡ When to Use

- **Branding Architecture**: Defining custom color tokens, typography, and shapes.
- **Dark Mode Support**: Implementing unified themes that swap automatically.
- **Dynamic Color**: Using `DynamicColor` for personalized system-wide tinting.
- **Component Libraries**: Building reusable Atom/Molecule components.
- **Multi-Brand Support**: Creating one app code for multiple visual identities.

## 🏗️ The 3 Pillars of M3 Design Systems

1. **Color Scheme**: Light/Dark palettes, surface variations, and semantic tokens (Primary, Error, OnPrimary).
2. **Typography**: Defined scales (HeadlineLarge, BodyMedium, LabelSmall) based on modern fonts.
3. **Shapes**: Corner radii for cards, buttons, and surfaces.

## 🧱 Creating Your Theme

- **Rule**: NEVER use hex codes in your UI code. ALWAYS use semantic tokens from your theme.
- **Bad**: `color = Color(0xFFAA44CC)`
- **Good**: `color = MaterialTheme.colorScheme.primary`

### 1. The Theme Composable

  ```kotlin
  @Composable
  fun AppTheme(
      darkTheme: Boolean = isSystemInDarkTheme(),
      dynamicColor: Boolean = true,
      content: @Composable () -> Unit
  ) {
      val colorScheme = when {
          dynamicColor && Build.VERSION.SDK_INT >= Build.VERSION_CODES.S -> {
              if (darkTheme) dynamicDarkColorScheme(context) else dynamicLightColorScheme(context)
          }
          darkTheme -> DarkColorScheme
          else -> LightColorScheme
      }

      MaterialTheme(colorScheme = colorScheme, typography = Typography, shapes = Shapes, content = content)
  ```

### 2. Mandatory Scaffold Files
When a user asks to "create a new project" or "set up a screen", ALWAYS ensure these three files are explicitly created in the `ui/theme` package to prevent `Theme not found` errors:
1. `Theme.kt` (containing the main Theme composable)
2. `Color.kt` (containing hex colors and M3 ColorSchemes)
3. `Type.kt` (containing Compose Typography)
- Provide these files outright if they are missing.

### 2. Custom Color Extensions
Use `CompositionLocal` or `colorScheme` extensions to add extra colors not in M3 (e.g., "SuccessGreen").

### 3. XML Theme Interoperability (Mandatory Bridge)

- **Role**: If using XML themes or resources alongside Compose, you MUST use the **Material Components for Android** XML bridge.
- **Dependency**: Add `com.google.android.material:material` to the project.
- **Standard Parent**: Use `Theme.Material3.DayNight.NoActionBar` (or variations) as the base parent for your XML themes.
- **Attribute Matching**: Ensure your XML `colorPrimary` matches your Compose `theme.colorScheme.primary`.

## 🚀 Premium Implementation Best Practices

- [ ] **Design Tokens**: Match your variable names exactly with Figma tokens (e.g., `md_sys_color_primary`).
- [ ] **Material 3 Shapes**: Use RoundedCornerShape(8dp) for cards but (32dp) for buttons for modern hierarchy.
- [ ] **Elevation**: Use `Surface` or `MaterialTheme.colorScheme.surfaceColorAtElevation()` instead of shadow modifiers for modern translucent effects.
- [ ] **Icons**: Use the Material Symbols official icons with uniform sizes (typically 24dp).

## 📐 Typography Rules

- **Display**: For landing pages or large hero text.
- **Headline**: For navigation or section headers.
- **Title**: For list items or subtitles.
- **Body**: For main readable content.
- **Label**: For metadata or button text.

## 🧪 Testing Your Design System

- **`@PreviewLightDark`**: See both light and dark themes at a glance.
- **Contrast Check**: Verify your color pairs using accessibility tools.
- **Component Preview**: Create a "Kitchen Sink" screen (via Showkase) to see all variations in one place.

## 📜 Checklist for Consistency

- [ ] **Surface Tones**: Are secondary surfaces (e.g., Background vs Surface) distinct?
- [ ] **Focus States**: Do interactive elements have clear focus states for keyboard/stylus users?
- [ ] **Loading States**: Are shimmer and progress indicators consistent with the theme?
- [ ] **Empty States**: Do all screens have a themed "No data" or "Error" state?

## 🔗 Related Resources
- [Official Material 3 Guide](https://m3.material.io)
- [Design to Code Skill](../android-design-to-code/SKILL.md)
- [Accessibility Skill](../android-accessibility/SKILL.md)
