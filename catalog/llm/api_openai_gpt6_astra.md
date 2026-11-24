# GPT-6 Astra

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_openai_gpt6_astra)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt6_astra-1.webp" width="360" alt="GPT-6 Astra api_openai_gpt6_astra-1.webp">

> Generate polished visual assets and optimize image-analysis prompts with GPT-6 Astra, an AI model that excels at computer vision tasks while adapting to your preferred style and reference images. Input your source visuals and creative direction to receive refined, immediately usable outputs with accurate detail and concise messaging. Ideal for enhancing prompt engineering workflows, preparing image datasets for analysis, and producing presentation-ready visual content that meets professional standards.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_gpt6_astra.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_gpt6_astra.json)

## Details

| | |
|---|---|
| Name | `api_openai_gpt6_astra` |
| Category | Foundation › LLM |
| Output | llm |
| Models | ChatGPT |
| Tags | API, LLM |
| Type | API |
| Date | 2026-09-05 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.6 |
| Usage | 33 |
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
| `OpenAIChatNode` | 1 |  |
| `PreviewAny` | 1 |  |
| `PrimitiveStringMultiline` | 1 |  |
| `SaveText` | 1 |  |
