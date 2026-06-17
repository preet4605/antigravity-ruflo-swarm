---
name: android-design-to-code
description: "Use when translating Figma, Sketch, or Adobe XD designs into Jetpack Compose code for Android."
category: ui-ux
risk: low
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@design-to-code"
    - "figma-translation"
    - "design-handover"
    - "ui-specs"
    - "pixel-perfect"
---

# Android Design to Code (The Bridge) 📐🌉

Professional strategies for translating high-fidelity design specifications into clean, semantic, and pixel-perfect Jetpack Compose code.

## ⚡ When to Use
- **UI Handover**: Implementing a new screen from Figma/Sketch.
- **Micro-Copy**: Translating exact text styles and case formatting.
- **Grid Alignment**: Replicating specific spacing and layout grids.
- **Component Building**: Creating atoms/molecules from design symbols.
- **Pixel Perfection**: Verifying accuracy through developer tools.

## 🏗️ The 4 Principles of High-Fidelity Translation

1.  **Semantic Match**: Use MaterialTheme tokens (Primary, BodyLarge) instead of raw hex/pixel values.
2.  **Structural Accuracy**: Replicate Flexbox (Row, Column) and Constraint systems as intended.
3.  **Interaction Fidelity**: Add the correct hover, press, and click ripple effects.
4.  **Responsive Layouts**: Handle how the design should shrink or grow beyond the mock's dimensions.

## 🛠️ Translation Workflow

### 1. Spacing & Grids (The 8dp Rule)
- **Rule**: Most modern Android designs use an **8dp grid**.
- Use `8.dp`, `16.dp`, `24.dp`, etc.
- In Compose: `Spacer(Modifier.height(16.dp))` or `PaddingValues(16.dp)`.

### 2. Colors & Typography
- Don't just copy the `0xFFAABBCC`. Check if it's already in the `colorScheme.primary` or `surface`.
- Use the M3 **Typography scale** (HeadlineLarge, BodyMedium) to match the designer's intent.

### 3. Shadows & Elevation
- Designs often have custom "Soft Shadows".
- **Rule**: In Android, use `Modifier.shadow()` with a high `elevation` for M2, or use `MaterialTheme.colorScheme.surfaceColorAtElevation()` for modern M3 designs.

## 🚀 Speeding Up Implementation

- [ ] **Figma Plugins**: Use "Relay" or "Copy as Compose" plugins to generate base code.
- [ ] **Lottie/Rive**: Export complex animations as JSON or RIV files for pixel-perfect motion.
- [ ] **Vector Assets**: Export as SVG or VectorDrawable (AVD) for sharp rendering.

## 📐 Interaction Best Practices

- **Ripple Effects**: Ensure all `clickable` modifiers have the standard ripple or custom `Indication`.
- **States**: Implement all design states (Enabled, Disabled, Pressed, Hovered).
- **Haptics**: Add `LocalHapticFeedback` for tactile confirmation on success/error.

## 🧪 Verification & Checklist

- [ ] **The "Overlay" Test**: Use a semi-transparent screen capture of the design overlaid on the running app.
- [ ] **Layout Inspector**: Verify all margins, paddings, and alignment match the specs.
- [ ] **Dynamic Font Scales**: Does the design survive a 200% font size increase?
- [ ] **Localization**: Does the layout break with long German or Russian strings?

## 📜 Key Terms for Designers

- **dp**: Density-independent pixels (The standard).
- **sp**: Scalable pixels (For text only).
- **Material 3**: The framework we use to build.
- **Composable**: The UI function we are creating.

## 🔗 Related Resources
- [Android Adaptive Layouts](../android-adaptive-layouts/SKILL.md)
- [Design System (M3) Skill](../android-design-system-m3/SKILL.md)
- [Accessibility Skill](../android-accessibility/SKILL.md)
