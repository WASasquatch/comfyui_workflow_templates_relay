# Claude: Fable 5

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_anthropic_claude_fable5-1.webp" width="360" alt="Claude: Fable 5 api_anthropic_claude_fable5-1.webp">

> Claude Fable 5, Anthropic's first public Mythos-class frontier model, powers end-to-end creative workflows in ComfyUI. It takes 1 text prompt and generates 1 structured output including storyboard breakdowns, precise prompts for SD models and ControlNet, and custom node scripts. Ideal for concept artists refining visual narratives, AI filmmakers maintaining style consistency across series, and digital creators automating their entire rendering pipeline.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_anthropic_claude_fable5.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_anthropic_claude_fable5.json)

## Details

| | |
|---|---|
| Name | `api_anthropic_claude_fable5` |
| Category | Foundation › LLM |
| Media type | image |
| Models | Claude |
| Tags | API, Text Generation |
| Type | API |
| Date | 2026-07-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.28.3 |
| Usage | 15 |
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
