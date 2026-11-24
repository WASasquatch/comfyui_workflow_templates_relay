# GPT-5.6 Luna

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_gpt5_6_luna-1.webp" width="360" alt="GPT-5.6 Luna api_openrouter_gpt5_6_luna-1.webp">

> GPT-5.6 Luna streamlines visual pre-production by analyzing a single reference image and generating structured creative text from a user prompt. It takes 1 input image and produces no explicit visual outputs, focusing instead on rapid, standardized copywriting. Ideal for batch scene description expansion, shot list organization, and high-volume creative ideation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_gpt5_6_luna.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openrouter_gpt5_6_luna.json)

## Details

| | |
|---|---|
| Name | `api_openrouter_gpt5_6_luna` |
| Category | Foundation › LLM |
| Media type | image |
| Models | ChatGPT |
| Tags | API, Text Generation |
| Type | API |
| Date | 2026-07-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.28.0 |
| Usage | 21 |
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
