# Clarity AI: Crystal Upscaler

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_clarity_ai_crystal_upscale)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_clarity_ai_crystal_upscale-1.webp" width="360" alt="Clarity AI: Crystal Upscaler api_clarity_ai_crystal_upscale-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_clarity_ai_crystal_upscale-2.webp" width="360" alt="Clarity AI: Crystal Upscaler api_clarity_ai_crystal_upscale-2.webp">

> Upscale and enhance images with the precision-focused Crystal model, preserving real detail while adding resolution. Takes one image in and returns one upscaled image plus a side-by-side comparison view. Ideal for portraits, product shots, and print-ready enlargements where faithful detail matters.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_clarity_ai_crystal_upscale.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_clarity_ai_crystal_upscale.json)

## Details

| | |
|---|---|
| Name | `api_clarity_ai_crystal_upscale` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | Crystal Upscaler |
| Tags | Image Upscale |
| Type | API |
| Date | 2026-10-07 |
| Author | ComfyUI |
| Min ComfyUI version | 0.39.2 |
| Usage | 172 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | watch_spa_black.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ClarityCrystalUpscaleNode` | 1 |  |
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [watch_spa_black.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/watch_spa_black.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
