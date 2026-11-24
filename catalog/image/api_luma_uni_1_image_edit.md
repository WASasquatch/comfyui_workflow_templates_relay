# Luma UNI-1: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_luma_uni_1_image_edit-1.webp" width="360" alt="Luma UNI-1: Image Edit api_luma_uni_1_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_luma_uni_1_image_edit-2.webp" width="360" alt="Luma UNI-1: Image Edit api_luma_uni_1_image_edit-2.webp">

> Edit existing images with Uni-1's Image Edit mode, preserving composition and core elements. Supports targeted adjustments like lighting and color using prompts and reference images.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_luma_uni_1_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_luma_uni_1_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_luma_uni_1_image_edit` |
| Category | Foundation › Image |
| Media type | image |
| Models | Luma UNI-1 |
| Tags | Image Edit, API |
| Type | API |
| Date | 2026-05-05 |
| Author | ComfyUI |
| Min ComfyUI version | 0.20.3 |
| Usage | 22 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #33 | image | the_leap.png |
| output | `SaveImage` #34 | image | api_luma_uni_1_image_edit.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `LumaImageEditNode2` | 1 |  |
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
