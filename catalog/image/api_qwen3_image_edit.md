# Qwen Image 3.0 Pro: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_qwen3_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_qwen3_image_edit-1.webp" width="360" alt="Qwen Image 3.0 Pro: Image Edit api_qwen3_image_edit-1.webp">

> Qwen Image 3.0 Pro performs advanced image editing with rich multi-image input, generating complex layouts like newspapers, storyboards, menus, and exam papers in a single pass while preserving fine details down to 10px text, micro-expressions, and individual hairs. Supports native rendering across 12 languages with realistic simulation of web pages, games, and live streams. Ideal for professional content production, interface mockups, and high-fidelity commercial imagery requiring authentic detail.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_qwen3_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_qwen3_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_qwen3_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | Qwen Image 3.0 Pro |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-08-06 |
| Author | ComfyUI |
| Min ComfyUI version | 0.32.0 |
| Usage | 109 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #14 | image | wasteland_merchant.png |
| output | `SaveImage` #2 | image | api_qwen3_image_edit.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `QwenImageEditApi` | 1 |  |
| `SaveImage` | 1 |  |
