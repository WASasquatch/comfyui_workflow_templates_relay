# MAGI-2: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_magi2_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magi2_i2v-1.webp" width="360" alt="MAGI-2: Image to Video api_magi2_i2v-1.webp">

> Animate a first frame, or a first and last frame, into a 1080p video of 4 to 30 seconds with native audio using MAGI-2, Sand.ai's 480B video model. Keeps a supplied composition exactly where you put it while the camera, subject motion and sound all follow the prompt.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magi2_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_magi2_i2v.json)

## Details

| | |
|---|---|
| Name | `api_magi2_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | MAGI-2 |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-11-28 |
| Author | ComfyUI |
| Min ComfyUI version | 0.46.4 |
| Usage | 0 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | forest_rhino_ukiyoe.png |
| output | `SaveVideo` #2 | video | api_magi2_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `Magi2ImageToVideoApi` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [forest_rhino_ukiyoe.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/forest_rhino_ukiyoe.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
