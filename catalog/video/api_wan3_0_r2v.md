# Wan3.0: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_wan3_0_r2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan3_0_r2v-1.webp" width="360" alt="Wan3.0: Reference to Video api_wan3_0_r2v-1.webp">

> Generate a video from two reference images using Wan3.0's reference-to-video capability, which produces up to 30 seconds of footage with character consistency and lifelike visuals. Ideal for creating consistent character animations, scene replication from visual references, and producing audiovisual content from static imagery.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan3_0_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_wan3_0_r2v.json)

## Details

| | |
|---|---|
| Name | `api_wan3_0_r2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan3.0 |
| Tags | API, Reference to Video |
| Type | API |
| Date | 2026-08-24 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.4 |
| Usage | 5000 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #6 | image | vortex_shoe.png |
| input | `LoadImage` #18 | image | psss_character.png |
| output | `SaveVideo` #17 | video | api_wan3_0_r2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
| `Wan3ReferenceToVideoApi` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Input Asset</summary>

**Input Asset** 


- [vortex_shoe.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/vortex_shoe.png) — required workflow input (`input/vortex_shoe.png`)
- [psss_character.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/psss_character.png) — required workflow input (`input/psss_character.png`)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
