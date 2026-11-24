# Seedream 5.0 Pro: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_0_pro_image_edit-1.webp" width="360" alt="Seedream 5.0 Pro: Image Edit api_bytedance_seedream_5_0_pro_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_0_pro_image_edit-2.webp" width="360" alt="Seedream 5.0 Pro: Image Edit api_bytedance_seedream_5_0_pro_image_edit-2.webp">

> Edit images with precision using Seedream 5.0 Pro, targeting specific regions while preserving lighting, depth, and texture. The workflow takes 1 input image and produces 1 output image. Ideal for product photography edits, portrait consistency adjustments, and creating structured layouts with multilingual text.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedream_5_0_pro_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bytedance_seedream_5_0_pro_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_bytedance_seedream_5_0_pro_image_edit` |
| Category | Foundation › Image |
| Media type | image |
| Models | Seedream 5.0 Pro |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-07-08 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.3 |
| Usage | 4128 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | interior_college.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `ByteDanceSeedreamNodeV3` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `Painter` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `SaveImageAdvanced` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Enable Node 2.0. If you can’t use the Painter node, use the [Partial Execution](https://docs.comfy.org/interface/features/partial-execution) feature on the Preview Image node. This way, you won’t need to run the entire workflow just to get the Painter preview working. With future updates, the preview can support live use.

You can run this workflow without updating it; if you want, you can use it to draw some marks on the input image.

</details>

<details><summary>MarkdownNote</summary>

## Input Asset

- [interior_college.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/interior_college.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
