# Kling O1: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_kling_omni_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_omni_i2v-1.webp" width="360" alt="Kling O1: Image to Video api_kling_omni_i2v-1.webp">

> Transform static images into dynamic videos with Kling O1. Add motion, camera movements, and life to your images using text prompts.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_omni_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_omni_i2v.json)

## Details

| | |
|---|---|
| Name | `api_kling_omni_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Kling O1 |
| Tags | API, Video, Character Reference |
| Type | API |
| Date | 2026-01-12 |
| Author | ComfyUI |
| Min ComfyUI version | 0.8.0 |
| Usage | 17 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | sheep_knit.jpg |
| input | `LoadImage` #5 | image | quokka_bath.jpg |
| input | `LoadImage` #6 | image | quokka_relax.jpg |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 3 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `KlingOmniProImageToVideoNode` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
