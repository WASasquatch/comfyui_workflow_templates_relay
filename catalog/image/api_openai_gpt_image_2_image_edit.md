# GPT Image 2: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_2_image_edit-1.webp" width="360" alt="GPT Image 2: Image Edit api_openai_gpt_image_2_image_edit-1.webp">

> Upload a reference image and write a prompt to create campaign-ready posters, product shots, and multilingual signage. The model renders clean text and photorealistic outputs suitable for commercial work.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_2_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_gpt_image_2_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_openai_gpt_image_2_image_edit` |
| Category | Foundation › Image |
| Media type | image |
| Models | GPT Image 2 |
| Tags | Image Edit, API |
| Type | API |
| Date | 2026-04-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.21.1 |
| Usage | 128 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #271 | image | product_shoe.png |
| output | `SaveImage` #269 | image | api_openai_gpt_image_2_image_edit.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 | comfy-core |
| `OpenAIGPTImageNodeV2` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
