# Nano Banana

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_google_gemini_image)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_image-1.webp" width="360" alt="Nano Banana api_google_gemini_image-1.webp">

> Nano-banana (Gemini-2.5-Flash Image) - image editing with consistency.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_gemini_image.json)

## Details

| | |
|---|---|
| Name | `api_google_gemini_image` |
| Category | Foundation › Image |
| Output | image |
| Models | Gemini-2.5-Flash, Nano Banana, Google |
| Tags | Image Edit, Image, API, Text to Image |
| Type | API |
| Date | 2025-08-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.8.0 |
| Usage | 22 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | comfyui_logo.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiInputFiles` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `BatchImagesNode` | 1 |  |
| `GeminiImageNode` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>About Gemini Input Files</summary>

The files need to be in the "ComfyUI/input" folder first. This node still needs updating to let you upload directly in the node.

</details>

<details><summary>MarkdownNote</summary>

Select `Batch Images` node and press Ctrl-B to enable multiple inputs.

</details>
