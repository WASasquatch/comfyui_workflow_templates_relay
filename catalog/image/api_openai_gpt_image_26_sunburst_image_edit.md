# GPT Image 2.6 Sunburst: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_openai_gpt_image_26_sunburst_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_26_sunburst_image_edit-1.webp" width="360" alt="GPT Image 2.6 Sunburst: Image Edit api_openai_gpt_image_26_sunburst_image_edit-1.webp">

> Edit one thing in a photo and keep the rest identical: the same camera angle, framing, subject position and light, with only the requested element changed. GPT Image 2.6 Sunburst renders fine texture and small type, so posters and dense scenes hold up better on the second or third pass.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_26_sunburst_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_gpt_image_26_sunburst_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_openai_gpt_image_26_sunburst_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | GPT Image 2.6 |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-11-05 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.1 |
| Usage | 629 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #376 | image | api_openai_gpt_image_26_sunburst_image_edit_input.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `OpenAIGPTImageNodeV2` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [api_openai_gpt_image_26_sunburst_image_edit_input.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_openai_gpt_image_26_sunburst_image_edit_input.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
