# Kling 4.0: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_kling4_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_i2v-1.webp" width="360" alt="Kling 4.0: Image to Video api_kling4_i2v-1.webp">

> Animate a single still into a five-second clip with Kling 4.0, cutting three times inside one generation. The source image locks the subject and styling while the default prompt drives the camera moves and a beat-timed edit, and the model also produces stereo audio. Ideal for fashion, editorial, and product motion where the input frame defines the look.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling4_i2v.json)

## Details

| | |
|---|---|
| Name | `api_kling4_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Kling 4.0 |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-10-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.43.0 |
| Usage | 571 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | kling4_editorial_portrait.png |
| output | `SaveVideo` #3 | video | api_kling4_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Kling4ImageToVideoNode` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Input Asset</summary>

## Input Asset

- [kling4_editorial_portrait.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/kling4_editorial_portrait.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
