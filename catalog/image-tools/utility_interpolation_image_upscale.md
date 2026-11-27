# Image Upscale: Traditional Interpolation

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_interpolation_image_upscale)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_interpolation_image_upscale-1.webp" width="360" alt="Image Upscale: Traditional Interpolation utility_interpolation_image_upscale-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_interpolation_image_upscale-2.webp" width="360" alt="Image Upscale: Traditional Interpolation utility_interpolation_image_upscale-2.webp">

> Upload an image and select an interpolation method. Upscale the image using traditional algorithms for faster processing with minimal detail changes.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_interpolation_image_upscale.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_interpolation_image_upscale.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/image-upscale)

## Details

| | |
|---|---|
| Name | `utility_interpolation_image_upscale` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | None |
| Tags | Image Upscale |
| Type | open source |
| Date | 2026-02-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.9.0 |
| Usage | 20 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | pray.png |
| output | `SaveImage` #5 | image | utility_interpolation_image_upscale.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ImageCompare` | 1 |  |
| `ImageScaleBy` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Image Compare is now only available under Nodes 2.0. Open menu -> Nodes 2.0 to switch

</details>
