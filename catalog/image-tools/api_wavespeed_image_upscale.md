# Image Upscale: WaveSpeed

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wavespeed_image_upscale-1.webp" width="360" alt="Image Upscale: WaveSpeed api_wavespeed_image_upscale-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wavespeed_image_upscale-2.webp" width="360" alt="Image Upscale: WaveSpeed api_wavespeed_image_upscale-2.webp">

> Upload an image to upscale its resolution. Generate an enhanced 2K, 4K, or 8K output that preserves details and reduces artifacts in JPEG, PNG, or WEBP format.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wavespeed_image_upscale.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_wavespeed_image_upscale.json)

## Details

| | |
|---|---|
| Name | `api_wavespeed_image_upscale` |
| Category | Foundation › Image Tools |
| Media type | image |
| Models | WaveSpeed |
| Tags | API, Image Upscale |
| Type | API |
| Date | 2026-01-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.11.0 |
| Usage | 28 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #9 | image | woman_behind_veil.png |
| output | `SaveImage` #3 | image | api_wavespeed_image_upscale.png |

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
