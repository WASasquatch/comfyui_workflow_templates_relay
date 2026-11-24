# Anthropic Claude

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_anthropic_claude-1.webp" width="360" alt="Anthropic Claude api_anthropic_claude-1.webp">

> Input your query or image for analysis. Generate a natural language response powered by Anthropic Claude, supporting both text conversation and image understanding.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_anthropic_claude.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_anthropic_claude.json)

## Details

| | |
|---|---|
| Name | `api_anthropic_claude` |
| Category | Foundation › LLM |
| Media type | image |
| Models | Claude |
| Tags | API, Text Generation |
| Type | API |
| Date | 2026-05-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.21.1 |
| Usage | 14 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | ice_cold_pup.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ClaudeNode` | 1 |  |
| `LoadImage` | 1 |  |
| `PreviewAny` | 1 |  |
