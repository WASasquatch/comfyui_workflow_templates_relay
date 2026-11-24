# Seedance 2.0: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_t2v-1.webp" width="360" alt="Seedance 2.0: Text to Video api_seedance2_0_t2v-1.webp">

> Generate cinematic videos from text prompts with synchronized audio, controlled camera motion, and stable visuals. Input text descriptions to output high-quality video sequences.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_0_t2v.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_0_t2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | Seedance 2.0 |
| Tags | API, Text to Video, Video |
| Type | API |
| Date | 2026-05-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.26.2 |
| Usage | 29 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #344 | video | api_seedance2_0_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDance2TextToVideoNode` | 1 |  |
| `SaveVideo` | 1 |  |
