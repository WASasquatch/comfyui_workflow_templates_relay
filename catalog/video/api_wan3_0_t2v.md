# Wan3.0: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_wan3_0_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan3_0_t2v-1.webp" width="360" alt="Wan3.0: Text to Video api_wan3_0_t2v-1.webp">

> Generate videos up to 30 seconds directly from text prompts using Wan3.0-Video, producing a single video output with lifelike visuals and synchronized sound. This workflow transforms written descriptions into immersive, production-ready footage with strong character consistency and cinematic quality. Ideal for cinematic storytelling, character-driven animations, and quick multimedia content creation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan3_0_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_wan3_0_t2v.json)

## Details

| | |
|---|---|
| Name | `api_wan3_0_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan3.0 |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-08-24 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.4 |
| Usage | 90 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #4 | video | api_wan3_0_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveVideo` | 1 | comfy-core |
| `Wan3ReferenceToVideoApi` | 1 | comfy-core |
