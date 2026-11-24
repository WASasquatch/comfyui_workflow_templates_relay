# Ideogram 4.5 Precise Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_ideogram_v4_5_precise_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_5_precise_image_edit-1.webp" width="360" alt="Ideogram 4.5 Precise Edit api_ideogram_v4_5_precise_image_edit-1.webp">

> Generate a precisely edited image from a text prompt and up to five input images using Ideogram 4.5, where image 1 is the image to edit and images 2-5 are optional references. Only what the prompt asks for changes, so untouched pixels stay identical and the output keeps the size of image 1, with a choice of quality tiers. Ideal for product recolours and material swaps, replacing one element of a photo without disturbing its lighting, background, or framing, and touch-ups that must leave the rest of the image alone.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_v4_5_precise_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_ideogram_v4_5_precise_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_ideogram_v4_5_precise_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | Ideogram |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-09-30 |
| Author | ComfyUI |
| Download size | 102.4 MB |
| Min ComfyUI version | 0.43.2 |
| Usage | 156 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | redhair_girl_portrait.png |

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

- [redhair_girl_portrait.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/redhair_girl_portrait.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: context window</summary>

# Ideogram 4.5 Precise Edit — `context_window`

Edits **only one region of image 1** at its native resolution. Without it the whole image is capped at ~4 MP (2048×2048), so anything bigger comes back downscaled. With a region, only the region changes, the rest is copied through, and the output keeps the source's exact size.

| Option | Uses | Effect |
|---|---|---|
| `none` | — | Whole image, downscaled above ~4 MP. Default. |
| `auto` | `context_window_mask` | Fits a region around the white mask area. Mask > 4 MP falls back to `none`. |
| `custom` | `context_window_bboxes` | Region = union of your boxes. Sides under 256 px are padded to 256. |

Region must be 256–4608 px per side, ≤ 4 MP, ≤ 6:1, inside image 1. Max 4 reference images, 3 with a mask. Price is unchanged — one image at the chosen `quality`.

</details>
