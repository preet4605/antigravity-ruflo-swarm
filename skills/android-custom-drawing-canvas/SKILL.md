---
name: android-custom-drawing-canvas
description: "Use when creating custom UI components, charts, shaders, or hardware-accelerated drawing in Android with Jetpack Compose Canvas."
category: ui-ux
risk: low
source: community
date_added: "2026-03-31"
metadata:
  triggers:
    - "@android-canvas"
    - "draw-behind"
    - "custom-charts"
    - "agsl-shaders"
    - "graphics-layer"
---

# Android Custom Drawing & Canvas ✏️🎨

Advanced strategies for high-performance, pixel-level custom UI components, data visualization, and creative graphics in Jetpack Compose.

## ⚡ When to Use
- **Custom Charts**: Drawing pie, bar, or line charts with precise control.
- **Complex UI Elements**: Building circular progress bars or custom sliders.
- **Graphic Effects**: Applying shaders (AGSL), gradients, or masks.
- **Dynamic Graphics**: Hand-drawn signatures or interactive shapes.
- **Particle Systems**: Drawing lightweight, dynamic visual effects.

## 🏗️ Drawing with `Canvas`

- **Rule**: Use `Modifier.drawBehind { ... }` or `Canvas(modifier = ...) { ... }`.
- **Coordinate System**: (0,0) is TOP-LEFT.
- **Draw Scope**: Access built-in methods like `drawRect`, `drawCircle`, `drawPath`.

### 1. Drawing a Circular Progress Bar
```kotlin
Canvas(modifier = Modifier.size(100.dp)) {
    val strokeWidth = 8.dp.toPx()
    drawArc(
        color = Color.LightGray,
        startAngle = 0f,
        sweepAngle = 360f,
        useCenter = false,
        style = Stroke(width = strokeWidth)
    )
    drawArc(
        color = Color.Blue,
        startAngle = -90f,
        sweepAngle = progress * 360f,
        useCenter = false,
        style = Stroke(width = strokeWidth, cap = StrokeCap.Round)
    )
}
```

### 2. The `Path` API
- Use for complex shapes (Stars, Polygons, Waves).
- Use `Path()` and methods like `moveTo`, `lineTo`, `cubicTo`.
- **Rule**: Reuse the `Path` object if possible to avoid allocations in the drawing loop.

## 🚀 Performance & Tips

- [ ] **Avoid Object Allocation**: Never create `Paint`, `Path`, or `Brush` objects inside `drawBehind`. Create them with `remember` outside.
- [ ] **Use `graphicsLayer`**: Move drawing into a separate layer for better hardware acceleration and cacheability.
- [ ] **Pixel Conversion**: Use `toPx()` carefully within the `DrawScope`. Keep dimensions consistent.
- [ ] **AGSL Shaders**: For Android 13+, use `RuntimeShader` for professional-grade effects (Blur, Wave, Noise).

## 📐 Chart Design Best Practices

- **Labels**: Don't draw complex text with `drawText` if you can use `Text` composables with `Layout`.
- **Interactivity**: Use `detectDragGestures` or `detectTapGestures` to make your custom drawings interactive.
- **Smoothness**: Use `animateFloatAsState` to animate chart values during transitions.

## 🧪 Testing and Verification

- **Screenshot Testing**: ALWAYS use screenshot tests for custom Canvas components to catch pixel-level regressions.
- **Layout Inspector**: Verify that your Canvas component isn't causing excessive recompositions.
- **Hardware Profile**: Ensure the "GPU rendering" bar doesn't cross the threshold during complex animations.

## 📜 Checklist for Canvas Components

- [ ] **Accessibility**: Does the canvas component have a `clearAndSetSemantics` entry with a proper description?
- [ ] **Theming**: Does the drawing use `MaterialTheme.colorScheme` colors?
- [ ] **Density Independence**: Does it look correct on both low and high-density screens?
- [ ] **Performance**: Are expensive path calculations cached?

## 🔗 Related Resources
- [Compose Graphics Documentation](https://developer.android.com/jetpack/compose/graphics)
- [AGSL Shaders Guide](https://developer.android.com/develop/ui/views/graphics/agsl)
- [Screenshot Testing Skill](../android-screenshot-testing/SKILL.md)
