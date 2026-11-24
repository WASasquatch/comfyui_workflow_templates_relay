# Ideogram 4.6 Precise Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_ideogram_v4_6_precise_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_6_precise_image_edit-1.webp" width="360" alt="Ideogram 4.6 Precise Edit api_ideogram_v4_6_precise_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_6_precise_image_edit-2.webp" width="360" alt="Ideogram 4.6 Precise Edit api_ideogram_v4_6_precise_image_edit-2.webp">

> Change one part of an image with Ideogram 4.6 and keep everything else as it was: send image 1 with an instruction, optionally paint a mask and add up to four references, and the result comes back at the source's exact size. Use the context window controls to edit a region of a large picture at native resolution. Ideal for swapping a product's material or colour, correcting one detail in a photo, and repeating the same edit without the rest of the frame drifting.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_6_precise_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_ideogram_v4_6_precise_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_ideogram_v4_6_precise_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | Ideogram |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-11-19 |
| Author | ComfyUI |
| Min ComfyUI version | 0.46.1 |
| Usage | 0 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | carbon_fibre_controller.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `BuildJsonPromptIdeogram` | 1 |  |
| `CreateBoundingBoxes` | 1 |  |
| `IdeogramPreciseEditApi` | 1 |  |
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

- [carbon_fibre_controller.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/carbon_fibre_controller.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: context window</summary>

# Ideogram 4.6 Precise Edit — `context_window`

Edits **only one region of image 1** at its native resolution. Without it the whole image is capped at ~4 MP (2048×2048), so anything bigger comes back downscaled. With a region, only the region changes, the rest is copied through, and the output keeps the source's exact size.

| Option | Uses | Effect |
|---|---|---|
| `none` | — | Whole image, downscaled above ~4 MP. Default. |
| `auto` | `context_window_mask` | Fits a region around the white mask area. Mask > 4 MP falls back to `none`. |
| `custom` | `context_window_bboxes` | Region = union of your boxes. Sides under 256 px are padded to 256. |

Region must be 256–4608 px per side, ≤ 4 MP, ≤ 6:1, inside image 1. Max 4 reference images, 3 with a mask. Price is unchanged — one image at the chosen `quality`.

</details>
