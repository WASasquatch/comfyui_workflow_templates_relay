# PixVerse 6.0: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pixverse6_t2v-1.webp" width="360" alt="PixVerse 6.0: Text to Video api_pixverse6_t2v-1.webp">

> Generate videos up to 15 seconds at 1080p from text prompts with PixVerse V6, supporting multiple aspect ratios, optional integrated audio, and multi-shot scene direction in a single generation. Ideal for social media ads, product concept testing, and short-form storytelling where narrative continuity and distribution-ready framing matter.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pixverse6_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_pixverse6_t2v.json)

## Details

| | |
|---|---|
| Name | `api_pixverse6_t2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | PixVerse |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-08-30 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.0 |
| Usage | 21 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #14 | video | api_pixverse6_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PixverseV6TextToVideoNode` | 1 |  |
| `SaveVideo` | 1 |  |
