# Image Upscale: HitPaw Portrait

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_hitpaw_general_image_enhance)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_hitpaw_general_image_enhance-1.webp" width="360" alt="Image Upscale: HitPaw Portrait utility_hitpaw_general_image_enhance-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_hitpaw_general_image_enhance-2.webp" width="360" alt="Image Upscale: HitPaw Portrait utility_hitpaw_general_image_enhance-2.webp">

> Upload a low-quality portrait image and adjust the upscaling factor. Generate a high-fidelity, detailed portrait with enhanced skin textures and facial features.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_hitpaw_general_image_enhance.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_hitpaw_general_image_enhance.json)

## Details

| | |
|---|---|
| Name | `utility_hitpaw_general_image_enhance` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | HitPaw |
| Tags | API, Image Upscale |
| Type | API |
| Date | 2026-02-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.12.0 |
| Usage | 15 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | sunlit_girl_portrait.png |
| output | `SaveImage` #3 | image | utility_hitpaw_general_image_enhance.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `HitPawGeneralImageEnhance` | 1 | comfy-core |
| `ImageCompare` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Image Compare is now only available under Nodes 2.0. Open menu -> Nodes 2.0 to switch

</details>
