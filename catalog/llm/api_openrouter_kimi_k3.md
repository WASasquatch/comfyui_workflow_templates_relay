# Kimi: K3

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_kimi_k3-1.webp" width="360" alt="Kimi: K3 api_openrouter_kimi_k3-1.webp">

> Generate detailed image descriptions and creative briefs using Kimi K3, a multimodal model with million-token context windows for unified text and image understanding. Input one image and a text prompt to produce nuanced visual analyses or batch descriptions. Ideal for streamlining multi-shot visual series, generating automated script prompts for node-based workflows, and iteratively refining creative concepts through image feedback.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openrouter_kimi_k3.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openrouter_kimi_k3.json)

## Details

| | |
|---|---|
| Name | `api_openrouter_kimi_k3` |
| Category | Foundation › LLM |
| Media type | image |
| Models | Kimi K3 |
| Tags | API, Text Generation |
| Type | API |
| Date | 2026-07-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.28.3 |
| Usage | 17 |
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
