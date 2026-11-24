# Krea 2: Style Reference

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_krea2_style_reference)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_krea2_style_reference-1.webp" width="360" alt="Krea 2: Style Reference api_krea2_style_reference-1.webp">

> Upload a style reference image and input a text prompt. Generate an image matching the prompt while applying the aesthetic style from your reference.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_krea2_style_reference.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_krea2_style_reference.json)

## Details

| | |
|---|---|
| Name | `api_krea2_style_reference` |
| Category | Foundation › Image |
| Output | image |
| Models | Krea 2 |
| Tags | API, Style Reference |
| Type | API |
| Date | 2026-05-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.24.1 |
| Usage | 16 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #11 | image | krea_style_reference_image1.png |
| input | `LoadImage` #12 | image | krea_style_reference_image2.png |
| output | `SaveImage` #2 | image | api_krea2_style_reference.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Krea2StyleReferenceNode` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `Krea2ImageNode` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Chain multiple input images for style reference

</details>
