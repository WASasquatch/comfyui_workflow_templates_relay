# OpenAI: ChatGPT

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_chat-1.webp" width="360" alt="OpenAI: ChatGPT api_openai_chat-1.webp">

> Engage with OpenAI's advanced language models for intelligent conversations.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_openai_chat.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_openai_chat.json)

## Details

| | |
|---|---|
| Name | `api_openai_chat` |
| Category | Foundation › LLM |
| Media type | image |
| Models | ChatGPT |
| Tags | API, Text Generation |
| Type | API |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.28.1 |
| Usage | 24 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #5 | image | example.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 | comfy-core |
| `OpenAIChatConfig` | 1 | comfy-core |
| `OpenAIChatNode` | 1 | comfy-core |
| `SaveText` | 1 |  |
