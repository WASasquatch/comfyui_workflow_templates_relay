# GPT Image 2.6 Sunburst: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_openai_gpt_image_26_sunburst_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_26_sunburst_t2i-1.webp" width="360" alt="GPT Image 2.6 Sunburst: Text to Image api_openai_gpt_image_26_sunburst_t2i-1.webp">

> GPT Image 2.6 Sunburst is the detail-first half of GPT Image 2.6: it spends more of the render on fine texture, small type and materials, and keeps subjects and lighting consistent from one pass to the next. Use it for finished visuals, product shots and dense layouts where detail has to hold up.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt_image_26_sunburst_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_gpt_image_26_sunburst_t2i.json)

## Details

| | |
|---|---|
| Name | `api_openai_gpt_image_26_sunburst_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | GPT Image 2.6 |
| Tags | API, Text to Image |
| Type | API |
| Date | 2026-11-05 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.1 |
| Usage | 1466 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #269 | image | api_openai_gpt_image_26_sunburst_t2i.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `OpenAIGPTImageNodeV2` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
