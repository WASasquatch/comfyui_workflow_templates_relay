# Claude: Opus 5.5

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_anthropic_claude_opus_5_5)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_anthropic_claude_opus_5_5-1.webp" width="360" alt="Claude: Opus 5.5 api_anthropic_claude_opus_5_5-1.webp">

> This workflow pairs a single uploaded image with a text prompt, sending both to Claude Opus 5.5 for multimodal reasoning and response generation. Ideal for image captioning, visual question answering, and prompt-driven image analysis.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_anthropic_claude_opus_5_5.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_anthropic_claude_opus_5_5.json)

## Details

| | |
|---|---|
| Name | `api_anthropic_claude_opus_5_5` |
| Category | Foundation › LLM |
| Output | llm |
| Models | Claude |
| Tags | API, LLM |
| Type | API |
| Date | 2026-09-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.37.2 |
| Usage | 12 |
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
| `ClaudeNode` | 1 |  |
| `LoadImage` | 1 |  |
| `PreviewAny` | 1 |  |
| `PrimitiveStringMultiline` | 1 |  |
| `SaveText` | 1 |  |
