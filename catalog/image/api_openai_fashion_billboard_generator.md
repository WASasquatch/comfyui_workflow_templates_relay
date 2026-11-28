# Fashion Billboard Generator

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_openai_fashion_billboard_generator)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_fashion_billboard_generator-1.webp" width="360" alt="Fashion Billboard Generator api_openai_fashion_billboard_generator-1.webp">

> Transform clothing photos into professional mall billboard advertisements featuring realistic fashion models.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_fashion_billboard_generator.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_fashion_billboard_generator.json)

## Details

| | |
|---|---|
| Name | `api_openai_fashion_billboard_generator` |
| Category | Foundation › Image |
| Output | image |
| Models | GPT Image 2.6, OpenAI |
| Tags | Image Edit, Image, API |
| Type | API |
| Date | 2025-12-18 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.1 |
| Usage | 9 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | outfit-streetwear.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `OpenAIGPTImageNodeV2` | 2 | comfy-core |
| `SaveImage` | 2 | comfy-core |
| `LoadImage` | 1 | comfy-core |
