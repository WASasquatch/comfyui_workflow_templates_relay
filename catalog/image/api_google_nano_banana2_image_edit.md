# Nano Banana 2: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_google_nano_banana2_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_nano_banana2_image_edit-1.webp" width="360" alt="Nano Banana 2: Image Edit api_google_nano_banana2_image_edit-1.webp">

> Upload an image and a text prompt to edit it. Generate a new image that modifies the original based on your instructions, maintaining subject consistency and high visual fidelity.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_nano_banana2_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_nano_banana2_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_google_nano_banana2_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | Google, Nano Banana 2 |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-02-26 |
| Author | ComfyUI |
| Min ComfyUI version | 0.20.3 |
| Usage | 1323 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #16 | image | man_with_dog.png |
| output | `SaveImage` #9 | image | api_google_nano_banana2_image_edit.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiNanoBanana2V2` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
