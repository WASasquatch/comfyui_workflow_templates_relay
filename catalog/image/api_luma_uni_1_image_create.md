# Luma UNI-1: Image Creation

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_luma_uni_1_image_create-1.webp" width="360" alt="Luma UNI-1: Image Creation api_luma_uni_1_image_create-1.webp">

> Generate brand-new original images using the Luma UNI-1 node with up to 9 reference images for style, character, color, lighting, and composition. Create unique compositions with detailed prompts, adjustable aspect ratios, and seed control.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_luma_uni_1_image_create.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_luma_uni_1_image_create.json)

## Details

| | |
|---|---|
| Name | `api_luma_uni_1_image_create` |
| Category | Foundation › Image |
| Media type | image |
| Models | Luma UNI-1 |
| Tags | API, Image, Style Reference |
| Type | API |
| Date | 2026-05-05 |
| Author | ComfyUI |
| Min ComfyUI version | 0.20.3 |
| Usage | 15 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #33 | image | uni_1_style_ref.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `LumaImageNode2` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Luma UNI-1 Image</summary>

Luma UNI-1 Image node is use for create new images
1. Create Mode generates **brand-new original images and compositions**, not limited to existing visuals.
2. It supports up to 9 reference images with defined roles (style, character, color, lighting, composition, etc.) for style or element inspiration.
3. Works with detailed prompts, adjustable aspect ratios and seed control to customize visuals.
4. Ideal for making new scenes, original artworks, or content inspired by reference materials without copying the original image structure.

</details>
