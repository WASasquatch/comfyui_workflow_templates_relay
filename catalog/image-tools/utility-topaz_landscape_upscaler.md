# Image Upscale: Topaz Reimagine Landscape

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-topaz_landscape_upscaler-1.webp" width="360" alt="Image Upscale: Topaz Reimagine Landscape utility-topaz_landscape_upscaler-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-topaz_landscape_upscaler-2.webp" width="360" alt="Image Upscale: Topaz Reimagine Landscape utility-topaz_landscape_upscaler-2.webp">

> Upload a landscape image to upscale and enhance details. Generate a high-resolution output optimized for natural scenery using Topaz Reimagine.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-topaz_landscape_upscaler.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility-topaz_landscape_upscaler.json)

## Details

| | |
|---|---|
| Name | `utility-topaz_landscape_upscaler` |
| Category | Foundation › Image Tools |
| Media type | image |
| Models | Topaz |
| Tags | API, Image Upscale |
| Type | API |
| Date | 2026-02-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.30.2 |
| Usage | 22 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | moonlit_cliff_house.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GetImageSize` | 1 | comfy-core |
| `ImageCompare` | 1 |  |
| `ImageScaleBy` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `TopazImageEnhanceV2` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [moonlit_cliff_house.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/moonlit_cliff_house.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
