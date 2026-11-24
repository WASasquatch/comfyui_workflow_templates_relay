# GPT Image 2.6 Flare: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_26_flare_image_edit-1.webp" width="360" alt="GPT Image 2.6 Flare: Image Edit api_openai_gpt_image_26_flare_image_edit-1.webp">

> Edit one detail of a photo and leave the rest alone: keep the face, pose, framing and lighting, then change the outfit, hair or a single object. Built on GPT Image 2.6 Flare, so drafts come back in seconds and the identity holds well enough to iterate on.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_26_flare_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_gpt_image_26_flare_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_openai_gpt_image_26_flare_image_edit` |
| Category | Foundation › Image |
| Media type | image |
| Models | GPT Image 2.6 |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-11-05 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.1 |
| Usage | 493 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #360 | image | young_man_windblown.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `OpenAIGPTImageNodeV2` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [young_man_windblown.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/young_man_windblown.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
