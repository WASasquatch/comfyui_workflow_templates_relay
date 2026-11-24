# Google Gemini

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini-1.webp" width="360" alt="Google Gemini api_google_gemini-1.webp">

> Experience Google's multimodal AI with Gemini's reasoning capabilities.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_gemini.json)

## Details

| | |
|---|---|
| Name | `api_google_gemini` |
| Category | Foundation › LLM |
| Media type | image |
| Models | Google, Google Gemini |
| Tags | API, Text Generation |
| Type | API |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.35.2 |
| Usage | 14 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | example.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiNodeV3` | 1 |  |
| `LoadImage` | 1 | comfy-core |
| `SaveText` | 1 |  |
