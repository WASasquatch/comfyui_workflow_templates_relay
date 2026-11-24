# Claude: Sonnet 5

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_anthropic_claude_sonnet5)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_anthropic_claude_sonnet5-1.webp" width="360" alt="Claude: Sonnet 5 api_anthropic_claude_sonnet5-1.webp">

> Leverage Claude Sonnet 5 for high-value autonomous task execution, bridging the gap to flagship performance at a lower cost. Input any text prompt or script to generate precise image descriptions, automated workflow scripts, shot sequence logs, or node logic corrections. Ideal for batch production tasks, debugging ComfyUI node logic, and maintaining consistent output quality across repetitive generation workflows.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_anthropic_claude_sonnet5.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_anthropic_claude_sonnet5.json)

## Details

| | |
|---|---|
| Name | `api_anthropic_claude_sonnet5` |
| Category | Foundation › LLM |
| Output | llm |
| Models | Claude |
| Tags | API, Text Generation |
| Type | API |
| Date | 2026-07-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.28.3 |
| Usage | 30 |
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
| `ClaudeNode` | 1 |  |
| `LoadImage` | 1 |  |
| `PreviewAny` | 1 |  |
| `PrimitiveStringMultiline` | 1 |  |
| `SaveText` | 1 |  |
