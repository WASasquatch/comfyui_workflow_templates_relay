# Dynamic 3D Logo Animations

[← Brand & Design](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-3D_logo_texture_animation-1.webp" width="360" alt="Dynamic 3D Logo Animations templates-3D_logo_texture_animation-1.webp">

> Upload a vector image of your logo, and prompt your desired texture. Generate a textured 3D first and last frame with automated prompting for the final animation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-3D_logo_texture_animation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-3D_logo_texture_animation.json)

## Details

| | |
|---|---|
| Name | `templates-3D_logo_texture_animation` |
| Category | Applied › Brand & Design |
| Media type | image |
| Models | ByteDance, Seedream, Google Gemini, Nano Banana Pro |
| Tags | API, Brand Design, FLF2V |
| Type | API |
| Date | 2025-12-15 |
| Author | hellorob |
| Min ComfyUI version | 0.35.2 |
| Usage | 15 |
| Nodes | 12 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | comfy_logo_c.png |

## Subgraphs

- **Automatic Transition Prompt** (2 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiImage2Node` | 3 | comfy-core |
| `SaveImage` | 3 | comfy-core |
| `BatchImagesNode` | 1 |  |
| `ByteDanceFirstLastFrameNode` | 1 | comfy-core |
| `GeminiNode` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
