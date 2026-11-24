# ByteDance: Seed 2.0

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seed-1.webp" width="360" alt="ByteDance: Seed 2.0 api_bytedance_seed-1.webp">

> Input an image or video for analysis. Receive detailed text output describing visual content, reasoning, and structured information extraction.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seed.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bytedance_seed.json)

## Details

| | |
|---|---|
| Name | `api_bytedance_seed` |
| Category | Foundation › LLM |
| Media type | image |
| Models | Seed 2.0 |
| Tags | API, Text Generation |
| Type | API |
| Date | 2026-05-19 |
| Author | ComfyUI |
| Min ComfyUI version | 0.22.0 |
| Usage | 35 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | angle_3.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewAny` | 3 |  |
| `JsonExtractString` | 2 | comfy-core |
| `RegexReplace` | 2 | comfy-core |
| `ByteDanceSeedNode` | 1 |  |
| `LoadImage` | 1 |  |
