# Pixel Sort Glitch Effect Image Transformation

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_purz_pixel_sort_image)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_purz_pixel_sort_image-1.webp" width="360" alt="Pixel Sort Glitch Effect Image Transformation templates_purz_pixel_sort_image-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_purz_pixel_sort_image-2.webp" width="360" alt="Pixel Sort Glitch Effect Image Transformation templates_purz_pixel_sort_image-2.webp">

> Apply a pixel sorting algorithm to create glitch art. Control the effect direction, threshold, and blending with the original image. Outputs a stylized, smeared version of the input.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_purz_pixel_sort_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_purz_pixel_sort_image.json)

## Details

| | |
|---|---|
| Name | `templates_purz_pixel_sort_image` |
| Category | Foundation › Image |
| Output | image |
| Models | None |
| Tags | Image, Style Transfer |
| Type | open source |
| Date | 2026-03-21 |
| Author | PurzBeats |
| Min ComfyUI version | 0.0.1 |
| Distributions | cloud |
| Usage | 9 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | wireframe_dancer.png |
| output | `SaveImage` #3 | image | templates_purz_pixel_sort_image.png |

## Custom nodes required

- [comfyui_fill-nodes](https://registry.comfy.org/nodes/comfyui_fill-nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `FL_PixelSort` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# FL PixelSort

Sorts pixels along a direction to create a glitch/smear effect.

## Parameters

| Parameter | Default | Notes |
|---|---|---|
| `direction` | Horizontal | UI only — does nothing. Direction is controlled by `rotation`. |
| `threshold` | 0.25 | Brightness cutoff that determines which pixels get sorted. |
| `smoothing` | 0.10 | Blends the sorted result with the original. |
| `rotation` | 1 | `0` = horizontal, `1` = vertical, `2` = diagonal. |

</details>
