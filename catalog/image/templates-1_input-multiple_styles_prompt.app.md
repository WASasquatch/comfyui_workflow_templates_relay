# 1 input multiple styles from prompt

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-1_input-multiple_styles_prompt.app-1.webp" width="360" alt="1 input multiple styles from prompt templates-1_input-multiple_styles_prompt.app-1.webp">

> Upload an image and generate 12 stylized variations in under 15 seconds.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-1_input-multiple_styles_prompt.app.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-1_input-multiple_styles_prompt.app.json)

## Details

| | |
|---|---|
| Name | `templates-1_input-multiple_styles_prompt.app` |
| Category | Foundation › Image |
| Media type | image |
| Models | Grok |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-02-19 |
| Author | hellorob |
| Min ComfyUI version | 0.21.1 |
| Usage | 4 |
| Nodes | 26 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | lightning_man.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GrokImageEditNodeV2` | 12 |  |
| `SaveImage` | 12 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [lightning_man.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/lightning_man.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
