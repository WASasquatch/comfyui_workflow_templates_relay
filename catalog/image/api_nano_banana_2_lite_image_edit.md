# Nano Banana 2 Lite: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_nano_banana_2_lite_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_nano_banana_2_lite_image_edit-1.webp" width="360" alt="Nano Banana 2 Lite: Image Edit api_nano_banana_2_lite_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_nano_banana_2_lite_image_edit-2.webp" width="360" alt="Nano Banana 2 Lite: Image Edit api_nano_banana_2_lite_image_edit-2.webp">

> Edit an image using Nano Banana 2 Lite, the fastest image generation model from Google’s Gemini series, producing a side-by-side comparison of the original and edited result. I

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_nano_banana_2_lite_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_nano_banana_2_lite_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_nano_banana_2_lite_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | Nano Banana 2 |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-06-30 |
| Author | ComfyUI |
| Min ComfyUI version | 0.27.0 |
| Usage | 47 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #8 | image | red_f1_track_car.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiNanoBanana2V2` | 1 |  |
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
