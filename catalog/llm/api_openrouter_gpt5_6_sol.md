# GPT-5.6: Sol

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_openrouter_gpt5_6_sol)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_gpt5_6_sol-1.webp" width="360" alt="GPT-5.6: Sol api_openrouter_gpt5_6_sol-1.webp">

> GPT-5.6 Sol is a multimodal model workflow for visual storytelling, taking 1 input image and a user prompt to generate detailed scene descriptions and narrative sequences. Ideal for world-building, multi-shot storyboarding, and maintaining consistent art style across long-form illustration or video projects.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_gpt5_6_sol.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openrouter_gpt5_6_sol.json)

## Details

| | |
|---|---|
| Name | `api_openrouter_gpt5_6_sol` |
| Category | Foundation › LLM |
| Output | llm |
| Models | ChatGPT |
| Tags | API, Text Generation |
| Type | API |
| Date | 2026-07-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.28.0 |
| Usage | 38 |
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
