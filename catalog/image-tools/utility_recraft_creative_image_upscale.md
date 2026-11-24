# Image Upscale: Recraft Creative

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_recraft_creative_image_upscale-1.webp" width="360" alt="Image Upscale: Recraft Creative utility_recraft_creative_image_upscale-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_recraft_creative_image_upscale-2.webp" width="360" alt="Image Upscale: Recraft Creative utility_recraft_creative_image_upscale-2.webp">

> Upload an image to enhance and upscale it. Recraft's AI reconstructs details and improves textures, outputting a higher-quality image with a natural appearance.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_recraft_creative_image_upscale.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_recraft_creative_image_upscale.json)

## Details

| | |
|---|---|
| Name | `utility_recraft_creative_image_upscale` |
| Category | Foundation › Image Tools |
| Media type | image |
| Models | Recraft |
| Tags | API, Image Upscale |
| Type | API |
| Date | 2026-02-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.9.0 |
| Usage | 13 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | butterfly_girl.png |
| output | `SaveImage` #3 | image | utility_recraft_creative_image_upscale.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `ImageCompare` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `RecraftCreativeUpscaleNode` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Image Compare is now only available under Nodes 2.0. Open menu -> Nodes 2.0 to switch

</details>

<details><summary>Input Size</summary>

- image size should be no more than 5MB
- image resolution should be no more than 2048×2048

</details>
