# FLUX.2 [max]: Object Swap

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux2_max_sofa_swap-1.webp" width="360" alt="FLUX.2 [max]: Object Swap api_bfl_flux2_max_sofa_swap-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux2_max_sofa_swap-2.webp" width="360" alt="FLUX.2 [max]: Object Swap api_bfl_flux2_max_sofa_swap-2.webp">

> Replace objects in images with unmatched quality using FLUX.2 [max]. Perfect for product photography, furniture swaps, and maintaining scene consistency with highest editing precision.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux2_max_sofa_swap.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bfl_flux2_max_sofa_swap.json)

## Details

| | |
|---|---|
| Name | `api_bfl_flux2_max_sofa_swap` |
| Category | Foundation › Image |
| Media type | image |
| Models | FLUX, FLUX.2 |
| Tags | API, Image, Image Edit |
| Type | API |
| Date | 2025-12-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.21.1 |
| Usage | 77 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | minimalist_wooden_sofa_living_room.png |
| input | `LoadImage` #3 | image | fluffy_beige_sofa.png |
| input | `LoadImage` #10 | image | black_coat_model.png |
| output | `SaveImage` #6 | image | api_bfl_flux2_max_sofa_swap.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 3 | comfy-core |
| `Flux2ImageNode` | 1 |  |
| `GetImageSize` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [black_coat_model.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/black_coat_model.png)
- [fluffy_beige_sofa.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/fluffy_beige_sofa.png)
- [minimalist_wooden_sofa_living_room.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/minimalist_wooden_sofa_living_room.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
