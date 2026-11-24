# Claude: Fable 5.1

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_anthropic_claude_fable5_1-1.webp" width="360" alt="Claude: Fable 5.1 api_anthropic_claude_fable5_1-1.webp">

> Run Claude Fable 5.1, Anthropic's frontier coding and agentic research model, directly in your workflow to tackle long-running, multi-step problems with state-of-the-art reasoning. This template provides access to the model's full capabilities, from root-cause software debugging and complex code generation to scientific analysis and knowledge work, with adjustable effort levels to balance cost and performance. Ideal for autonomous coding agents, deep technical investigations, and extended research tasks that require sustained, high-quality output.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_anthropic_claude_fable5_1.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_anthropic_claude_fable5_1.json)

## Details

| | |
|---|---|
| Name | `api_anthropic_claude_fable5_1` |
| Category | Foundation › LLM |
| Media type | image |
| Models | Claude |
| Tags | API, LLM |
| Type | API |
| Date | 2026-09-04 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.4 |
| Usage | 31 |
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
