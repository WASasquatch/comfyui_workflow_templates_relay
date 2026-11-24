# GPT Image 2: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_openai_gpt_image_2_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_2_t2i-1.webp" width="360" alt="GPT Image 2: Text to Image api_openai_gpt_image_2_t2i-1.webp">

> Create campaign-ready posters, product shots, and multilingual signage using OpenAI's latest model. Upload an optional reference image, write a detailed prompt, and generate high-quality, photorealistic outputs.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_2_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_gpt_image_2_t2i.json)

## Details

| | |
|---|---|
| Name | `api_openai_gpt_image_2_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | GPT Image 2 |
| Tags | API, Text to Image |
| Type | API |
| Date | 2026-04-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.21.1 |
| Usage | 95 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #269 | image | api_openai_gpt_image_2_t2i.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `OpenAIGPTImageNodeV2` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
