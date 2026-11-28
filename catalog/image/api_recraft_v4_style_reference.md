# Recraft V4: Style-Reference Image Generation

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_recraft_v4_style_reference)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_style_reference-1.webp" width="360" alt="Recraft V4: Style-Reference Image Generation api_recraft_v4_style_reference-1.webp">

> Generate images in the style of one or more reference images using Recraft V4 Styles, capturing texture, composition, and rendering without any training or fine-tuning. Feed in multiple reference images to sharpen or broaden the style match, and receive a single styled output. Ideal for brand-consistent asset creation, matching a client's existing campaign look, or adapting styles from any external image source.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_style_reference.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_recraft_v4_style_reference.json)

## Details

| | |
|---|---|
| Name | `api_recraft_v4_style_reference` |
| Category | Foundation › Image |
| Output | image |
| Models | Recraft |
| Tags | API, Style Reference |
| Type | API |
| Date | 2026-09-04 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.1 |
| Usage | 65 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #8 | image | recraft_v4_style_ref_2.png |
| input | `LoadImage` #9 | image | recraft_v4_style_ref_4.png |
| input | `LoadImage` #11 | image | recraft_v4_style_ref_3.png |
| input | `LoadImage` #12 | image | recraft_v4_style_ref_1.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 4 |  |
| `MarkdownNote` | 2 |  |
| `RecraftV4CreateStyleNode` | 1 |  |
| `RecraftV4TextToImageNode` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
| `SaveText` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [recraft_v4_style_ref_1.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/recraft_v4_style_ref_1.png)
- [recraft_v4_style_ref_2.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/recraft_v4_style_ref_2.png)
- [recraft_v4_style_ref_3.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/recraft_v4_style_ref_3.png)
- [recraft_v4_style_ref_4.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/recraft_v4_style_ref_4.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>MarkdownNote</summary>

The style ID will be saved to the `ComfyUI/output/Recraft_Style_v4/`; you can also update the filename_prefix to customize the output file name.

You can reuse the same style ID for future use

</details>
