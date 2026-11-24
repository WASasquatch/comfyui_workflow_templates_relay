# FLUX 3 Max: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_flux3_max_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_flux3_max_i2v-1.webp" width="360" alt="FLUX 3 Max: Image to Video api_flux3_max_i2v-1.webp">

> Animate a single still image into a short video clip using FLUX 3 Max, taking one input image and producing one video output. Ideal for bringing product shots, portraits, and concept art to life, generating social media motion content, and rapid prototyping of animated scenes.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_flux3_max_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_flux3_max_i2v.json)

## Details

| | |
|---|---|
| Name | `api_flux3_max_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | FLUX 3 Video |
| Tags | Image to Video, API |
| Type | API |
| Date | 2026-10-19 |
| Author | ComfyUI |
| Min ComfyUI version | 0.42.2 |
| Usage | 169 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #17 | image | hovering_spaceship.png |
| output | `SaveVideo` #5 | video | api_flux3_max_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Flux3MaxImageToVideoNode` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [hovering_spaceship.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/hovering_spaceship.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
