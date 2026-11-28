# Ideogram 4.5: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_ideogram_v4_5_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_5_image_edit-1.webp" width="360" alt="Ideogram 4.5: Image Edit api_ideogram_v4_5_image_edit-1.webp">

> Generate edited or combined images from a text prompt and up to five input images using Ideogram 4.5, where image 1 is the image to edit and images 2-5 are references for design, material, or colour. Canvas size, quality level, and seed are adjustable, and one image is output. Ideal for product and outfit swaps, applying a reference design or palette to an existing photo, and recomposing a shot into a different aspect ratio.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_5_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_ideogram_v4_5_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_ideogram_v4_5_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | Ideogram |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-09-30 |
| Author | ComfyUI |
| Min ComfyUI version | 0.38.1 |
| Usage | 53 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | interior_orange_sofa.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `BuildJsonPromptIdeogram` | 1 |  |
| `CreateBoundingBoxes` | 1 |  |
| `IdeogramEditApi` | 1 |  |
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `PreviewAny` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

- Enable [Nodes2.0](https://docs.comfy.org/interface/nodes-2) if you can't see the editor above
- Load an image and draw BBox captions on it, like "remove it", to edit the image.

</details>

<details><summary>MarkdownNote</summary>

## Input Asset

- [interior_orange_sofa.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/interior_orange_sofa.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
