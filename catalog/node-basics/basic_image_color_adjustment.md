# Color Adjustment Blueprints Showcase

[← Node Basics](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=basic_image_color_adjustment)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/basic_image_color_adjustment-1.webp" width="360" alt="Color Adjustment Blueprints Showcase basic_image_color_adjustment-1.webp">

> Side-by-side demo of built-in blueprint color-grading subgraphs.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/basic_image_color_adjustment.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/basic_image_color_adjustment.json)

## Details

| | |
|---|---|
| Name | `basic_image_color_adjustment` |
| Category | Foundation › Node Basics |
| Output | image |
| Models | None |
| Tags | Node Basics |
| Type | open source |
| Date | 2026-04-24 |
| Author | ComfyUI |
| Min ComfyUI version | 0.19.0 |
| Usage | 9 |
| Nodes | 78 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #180 | image | example.png |

## Subgraphs

- **Color Curves** (6 nodes)
- **Image Channels** (1 nodes)
- **Brightness and Contrast** (3 nodes)
- **Glow** (6 nodes)
- **Film Grain** (6 nodes)
- **Color Balance** (11 nodes)
- **Chromatic Aberration** (3 nodes)
- **Hue and Saturation** (7 nodes)
- **Color Adjustment** (5 nodes)
- **Image Levels** (7 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveFloat` | 32 | comfy-core |
| `PreviewImage` | 13 | comfy-core |
| `GLSLShader` | 10 | comfy-core |
| `MarkdownNote` | 9 |  |
| `CustomCombo` | 6 | comfy-core |
| `CurveEditor` | 4 | comfy-core |
| `ColorToRGBInt` | 1 | comfy-core |
| `ImageHistogram` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Color Balance</summary>

## Color Balance

**Purpose**: Adjust RGB color balance separately in **shadows, midtones, and highlights**.

**Highlights**: Real-time GPU fragment shader; independent sliders for precise color grading.

**Use when**: Fixing color casts, matching tone across the image, or cinematic split-toning without crushing contrast.

</details>

<details><summary>Brightness and Contrast</summary>

## Brightness and Contrast

**Purpose**: Change overall image **brightness** and **contrast**.

**Highlights**: GPU shader; simple controls with fast preview for exposure tweaks.

**Use when**: Brightening underexposed shots, taming highlights, or boosting/separating subject from background.

</details>

<details><summary>Image Levels</summary>

## Image Levels

**Purpose**: Set **black point, white point, and gamma** to control tonal distribution.

**Highlights**: Familiar Levels-style workflow; GPU shader with live preview.

**Use when**: Expanding dynamic range, fixing flat or crushed blacks, before other color passes.

</details>

<details><summary>Glow</summary>

## Glow

**Purpose**: Add **bloom / glow** around bright areas of the image.

**Highlights**: GPU shader; adjustable strength, radius, blend mode, and tint color.

**Use when**: Dreamy, neon, or cinematic halation around lights and specular highlights.

</details>

<details><summary>Chromatic Aberration</summary>

## Chromatic Aberration

**Purpose**: Simulate lens **color fringing** (e.g. red/cyan edges).

**Highlights**: GPU real-time; adjustable strength and direction for strong stylization.

**Use when**: Vintage, film, or lo-fi lens character; subtle edge accent effects.

</details>

<details><summary>Film Grain</summary>

## Film Grain

**Purpose**: Overlay procedural **film grain** texture.

**Highlights**: GPU shader; control grain size, amount, and related parameters.

**Use when**: Reducing overly clean digital look; adding cinematic texture and depth.

</details>

<details><summary>Color Adjustment</summary>

## Color Adjustment

**Purpose**: Tune global **saturation, temperature, tint, and vibrance**.

**Highlights**: GPU real-time; broad global grade that complements zone-based Color Balance.

**Use when**: Quick warm/cool shifts or overall saturation changes for mood.

</details>

<details><summary>Hue and Saturation</summary>

## Hue and Saturation

**Purpose**: Shift **hue**, **saturation**, and **lightness**.

**Highlights**: GPU shader; channel or global modes depending on subgraph controls.

**Use when**: Creative recoloring, desaturation, or pushing a specific color palette.

</details>

<details><summary>About this workflow</summary>

## Built-in Color Adjustment Blueprints Demo

This workflow demonstrates built-in image color and tone **subgraphs** from ComfyUI **blueprints**. **Load Image** on the left feeds every branch; **Preview Image** on the right shows each result side by side.

### Tips
- Drag any subgraph from the Comfy Subgraph in the Node library into your own graphs, or keep this layout for comparison.
- All color subgraphs use **GPU fragment shaders** for low-latency preview and export.

### Strongly recommended
Enable **[Nodes 2.0](https://docs.comfy.org/interface/nodes-2)** in ComfyUI settings for proxied subgraph widgets, canvas previews, and a smoother editing experience.

</details>
