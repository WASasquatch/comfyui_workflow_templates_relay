# Image Upscale: Topaz Illustration

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_topaz_illustration_upscale)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_topaz_illustration_upscale-1.webp" width="360" alt="Image Upscale: Topaz Illustration utility_topaz_illustration_upscale-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_topaz_illustration_upscale-2.webp" width="360" alt="Image Upscale: Topaz Illustration utility_topaz_illustration_upscale-2.webp">

> Upload an illustration to upscale using Topaz. Generate a smooth, stylized image with accurate colors, though some artifacts may appear.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_topaz_illustration_upscale.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_topaz_illustration_upscale.json)

## Details

| | |
|---|---|
| Name | `utility_topaz_illustration_upscale` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | Topaz |
| Tags | API, Image Upscale |
| Type | API |
| Date | 2026-02-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.30.2 |
| Usage | 14 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #5 | image | silent_sanctuary.jpg |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `GetImageSize` | 1 | comfy-core |
| `ImageCompare` | 1 | comfy-core |
| `ImageScaleBy` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `PrimitiveNode` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `TopazImageEnhanceV2` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

Image Compare is now only available under Nodes 2.0. Open menu -> Nodes 2.0 to switch

</details>

<details><summary>MarkdownNote</summary>

## Input Asset

- [silent_sanctuary.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/silent_sanctuary.jpg)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
