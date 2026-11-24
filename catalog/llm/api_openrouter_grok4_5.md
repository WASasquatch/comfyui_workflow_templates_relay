# Grok: Grok 4.5

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_grok4_5-1.webp" width="360" alt="Grok: Grok 4.5 api_openrouter_grok4_5-1.webp">

> Grok 4.5 is a flagship multimodal model designed for complex engineering and creative tasks, with native visual parsing and high-speed inference. It takes creative briefs and generated images as inputs, producing standardized scene descriptions and iterative visual analysis. Ideal for multi-shot storyboarding, batch image description generation, and feedback-driven creative refinement.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_grok4_5.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openrouter_grok4_5.json)

## Details

| | |
|---|---|
| Name | `api_openrouter_grok4_5` |
| Category | Foundation › LLM |
| Media type | image |
| Models | Grok |
| Tags | API, Text Generation |
| Type | API |
| Date | 2026-07-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.28.0 |
| Usage | 144 |
| Nodes | 8 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #12 | image | blue_poppies_field.png |

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
