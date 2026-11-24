# Seedance 2.0 Mini: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_seedance2_0_mini_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_mini_t2v-1.webp" width="360" alt="Seedance 2.0 Mini: Text to Video api_seedance2_0_mini_t2v-1.webp">

> Generate cinematic videos from text prompts with Dreamina’s Seedance 2.0 Mini, supporting AI camera controls and consistent character generation across scenes. This workflow takes only prompt input and produces 1 video output. Ideal for AI filmmaking, branded content creation, and multi-shot storytelling projects.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_mini_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_0_mini_t2v.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_0_mini_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Seedance 2.0 |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-06-25 |
| Author | ComfyUI |
| Min ComfyUI version | 0.26.2 |
| Usage | 32 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #2 | video | api_seedance2_0_mini_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDance2TextToVideoNode` | 1 |  |
| `SaveVideo` | 1 |  |
