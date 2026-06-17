---
name: design-website
description: (Meta-Orchestrator) Triggers on requests to "design a xyz website". Coordinates and applies the 10 premium web design skills and other styling/motion skills to build luxury-grade frontend interfaces.
risk: medium
source: custom-orchestrator
date_added: 2026-06-10
---

# Design Website (Meta-Orchestrator)

Use this skill whenever the user requests to **"design a [XYZ] website"** or asks you to build/design a web interface **"using web design skills"**. This meta-skill forces the agent to activate, orchestrate, and apply the 10 premium design skills in unison.

## Trigger Phrase
Matches: `design a [XYZ] website` or `design a [XYZ] site` or `using web design skills`.

---

## The 10 Premium Web Design Skills Checklist

When designing any website, you MUST systematically apply the following 10 capabilities:

1. **`midjourney-vision`**: Align visual layouts with glassmorphism layers, custom border shapes, and clean wrapper boundaries.
2. **`magic-ui-components`**: Inject glowing grids, typography reveal states, bento layouts, border beams, and neon text reveals into dark-mode containers.
3. **`fluid-theme`**: Restrict all sizing (typography, padding) to fluid `clamp()` scales. Maintain a strict luxury dark-mode scale (base surface `#0B0B0C`, alt surface `#141416`, low-opacity thin border `rgba(255,255,255,0.06)`).
4. **`motion-timeline`**: Configure layout entry physics using Framer Motion or GSAP. Apply staggered viewport entrance transitions with cubic-bezier easing curves.
5. **`smooth-scroll`**: Wrap containers with Lenis or Locomotive scroll to achieve inertia-based smooth scroll. Ensure hardware-accelerated animations.
6. **`threejs-canvas`**: Integrate floating particle fields, interactive meshes, or light-warping webGL layers behind hero copy when appropriate.
7. **`figma-connect`**: Match spacing and typography ratios to professional design coordinate layouts.
8. **`vector-icons`**: Restrict all icons to crisp SVG vector layouts or Lucide icons, enforcing a locked thin-line 1.5px stroke width.
9. **`lighthouse-optimize`**: Audit build states for layout shifts (CLS), load elements lazily, and compress assets using WebP/AVIF.
10. **`tailwind-variants`**: Build irregular, advanced grid variations using dynamic container query syntax, clipping masks, and parent box container queries.

---

## Step-by-Step Implementation Workflow

To execute a website design task, structure your planning and coding phases as follows:

### Step 1: Foundation & Theme Setup
- **Action**: Create/modify `index.css` or the styling tokens.
- **Skills**: `[fluid-theme, figma-connect]`
- **Requirements**: Enforce the luxury dark-mode palette and set up the fluid typography and spacing scale using `clamp()`.

### Step 2: Main Layout & Structural Bento
- **Action**: Define the core layout grid (asymmetrical/bento style).
- **Skills**: `[tailwind-variants, midjourney-vision]`
- **Requirements**: Establish structural wrapper boundaries and irregular grid layouts.

### Step 3: Core UI Elements & SVGs
- **Action**: Build luxury headers, heroes, feature cards, and footers.
- **Skills**: `[magic-ui-components, vector-icons]`
- **Requirements**: Embed border beams, glowing marquee grids, and SVG icons with 1.5px strokes.

### Step 4: Motion, Scroll, and 3D Canvas
- **Action**: Add entry animations, smooth inertia scrolling, and background 3D canvas mesh layers.
- **Skills**: `[motion-timeline, smooth-scroll, threejs-canvas]`
- **Requirements**: Connect GSAP/Framer Motion, Lenis scroll, and floating canvas meshes.

### Step 5: Auditing & Performance Optimizations
- **Action**: Check page load times, lazy loading, and layout shifts.
- **Skills**: `[lighthouse-optimize]`
- **Requirements**: Optimize images and assets to maintain high initial load performance.
