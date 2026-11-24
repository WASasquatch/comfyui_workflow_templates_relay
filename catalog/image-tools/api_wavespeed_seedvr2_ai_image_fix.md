# Image Upscale: WaveSpeed SeedVR2

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_wavespeed_seedvr2_ai_image_fix)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wavespeed_seedvr2_ai_image_fix-1.webp" width="360" alt="Image Upscale: WaveSpeed SeedVR2 api_wavespeed_seedvr2_ai_image_fix-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wavespeed_seedvr2_ai_image_fix-2.webp" width="360" alt="Image Upscale: WaveSpeed SeedVR2 api_wavespeed_seedvr2_ai_image_fix-2.webp">

> Upload an AI-generated image to restore details and upscale. The workflow preserves colors and sharpness while minimizing artifacts. Output is a high-quality, enlarged version of your input.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wavespeed_seedvr2_ai_image_fix.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_wavespeed_seedvr2_ai_image_fix.json)

## Details

| | |
|---|---|
| Name | `api_wavespeed_seedvr2_ai_image_fix` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | SeedVR2, WaveSpeed |
| Tags | API, Image Upscale |
| Type | API |
| Date | 2026-02-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.28.0 |
| Usage | 16 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #9 | image | midnight_coastal.png |
| output | `SaveImage` #3 | image | api_wavespeed_seedvr2_ai_image_fix.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ImageCompare` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `WavespeedImageUpscaleNode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Image Compare is now only available under Nodes 2.0. Open menu -> Nodes 2.0 to switch

</details>
