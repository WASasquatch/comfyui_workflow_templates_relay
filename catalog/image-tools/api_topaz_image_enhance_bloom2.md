# Image Upscale: Topaz Bloom 2

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_topaz_image_enhance_bloom2)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_image_enhance_bloom2-1.webp" width="360" alt="Image Upscale: Topaz Bloom 2 api_topaz_image_enhance_bloom2-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_image_enhance_bloom2-2.webp" width="360" alt="Image Upscale: Topaz Bloom 2 api_topaz_image_enhance_bloom2-2.webp">

> Enhance AI-generated images with Bloom 2, a creative upscaling model that adds new detail, texture, and visual elements while offering a Creativity control from 1–9 for subtle refinement or bold reinterpretation. It accepts 1 input image and produces 1 enhanced output, with optional Face Recovery, Color Preservation, and grain settings for fine-tuned results. Ideal for improving AI artwork and illustrations, adding realism to CG renders, and refining facial detail in generated portraits.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_image_enhance_bloom2.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_topaz_image_enhance_bloom2.json)

## Details

| | |
|---|---|
| Name | `api_topaz_image_enhance_bloom2` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | Topaz |
| Tags | API, Image Upscale |
| Type | API |
| Date | 2026-08-04 |
| Author | ComfyUI |
| Min ComfyUI version | 0.30.2 |
| Usage | 26 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | digital_bloom.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
| `TopazImageEnhanceV2` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

If the prompt is empty, the model will auto create one for you

</details>
