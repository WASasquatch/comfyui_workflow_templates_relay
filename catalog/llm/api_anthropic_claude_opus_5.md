# Claude: Opus 5

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_anthropic_claude_opus_5)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_anthropic_claude_opus_5-1.webp" width="360" alt="Claude: Opus 5 api_anthropic_claude_opus_5-1.webp">

> Load an image and enter a prompt to interact with Claude Opus 5, a highly capable and cost-efficient AI model that excels at coding, knowledge work, and problem-solving. Ideal for software engineering tasks, scientific research requiring visual analysis, and everyday productivity with a thoughtful, proactive assistant.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_anthropic_claude_opus_5.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_anthropic_claude_opus_5.json)

## Details

| | |
|---|---|
| Name | `api_anthropic_claude_opus_5` |
| Category | Foundation › LLM |
| Output | llm |
| Models | Claude |
| Tags | API, Text Generation |
| Type | API |
| Date | 2026-07-28 |
| Author | ComfyUI |
| Min ComfyUI version | 0.29.0 |
| Usage | 24 |
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
