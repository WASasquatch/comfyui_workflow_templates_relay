# GPT-5.6 Terra

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_openrouter_gpt5_6_terra)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_gpt5_6_terra-1.webp" width="360" alt="GPT-5.6 Terra api_openrouter_gpt5_6_terra-1.webp">

> Describe a scene or world using GPT-5.6 Terra, a balanced multimodal model that interprets one uploaded image to guide visual storytelling and style consistency. Ideal for worldbuilding, mood board creation, and maintaining cohesive aesthetics across a series of works.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_gpt5_6_terra.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openrouter_gpt5_6_terra.json)

## Details

| | |
|---|---|
| Name | `api_openrouter_gpt5_6_terra` |
| Category | Foundation › LLM |
| Output | llm |
| Models | ChatGPT |
| Tags | API, Text Generation |
| Type | API |
| Date | 2026-07-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.28.0 |
| Usage | 12 |
| Nodes | 8 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | blue_poppies_field.png |

## Subgraphs

- **Format Output** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `StringConcatenate` | 3 |  |
| `LoadImage` | 1 |  |
| `OpenRouterLLMNode` | 1 |  |
| `PreviewAny` | 1 |  |
| `PrimitiveStringMultiline` | 1 |  |
| `SaveText` | 1 |  |
