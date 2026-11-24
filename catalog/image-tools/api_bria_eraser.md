# Object Removal: Bria Eraser

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_eraser-1.webp" width="360" alt="Object Removal: Bria Eraser api_bria_eraser-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_eraser-2.webp" width="360" alt="Object Removal: Bria Eraser api_bria_eraser-2.webp">

> Remove unwanted objects or regions from images with Bria's Eraser, which fills the masked area with surrounding context while leaving the rest of the image pixel-perfect. Upload 1 image, paint over the target object with a brush mask, and receive 1 cleaned output alongside a before-and-after comparison. Ideal for cleaning up photobombs, removing watermarks or text, and decluttering product or real-estate photos.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_eraser.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bria_eraser.json)

## Details

| | |
|---|---|
| Name | `api_bria_eraser` |
| Category | Foundation › Image Tools |
| Media type | image |
| Models | BRIA |
| Tags | API, Inpainting |
| Type | API |
| Date | 2026-08-16 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.0 |
| Usage | 20 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | vintage_girl_yellow_apple.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BriaEraser` | 1 |  |
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `Painter` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Bria Eraser</summary>

# Bria Eraser Template

Use this template to **remove a specific object or region from an image** with Bria's Eraser API. The masked area is erased and filled with surrounding context; everything outside the mask stays pixel-perfect unchanged.

## Input Assets

- [vintage_girl_yellow_apple.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/vintage_girl_yellow_apple.png)

## How to use

1. **Load an image**: Upload your image in `LoadImage`. The Painter canvas and compare view auto-update.
2. **Paint a mask**: Use the `Painter` node to brush over the object or region you want to remove. Tip: paint slightly beyond the object's edge (hair, glass, fabric, contact points) so the model has room to blend cleanly.
3. **Run `BriaEraser`**: No prompt needed. The node erases the masked area and inpaints the background. Enter your `api_key` if it is not already set.
4. **Compare and save**: `ImageCompare` shows before/after, `SaveImageAdvanced` exports the result.

## Notes

- The masked area is **fully regenerated from its surroundings**: Eraser erases the object and inpaints the region with the surrounding background, so the result blends seamlessly. Keep the mask slightly larger than the object's edge for clean blending.
- The mask is **binary**: white (255) marks the region to erase, black (0) everywhere else, and it must match the image's aspect ratio.
- For more precise results, use an automatic segmentation mask (SAM-style) if available: the API's `mask_type` distinguishes `manual` (brush-drawn) from `automatic` (algorithm-generated) masks.
- The `Painter` node is only available under **Nodes 2.0**. The canvas auto-updates when you upload a new image. If you only see "Painter: Node 2.0 only": enable Nodes 2.0 via **Menu -> Nodes2.0**, or remove the Painter node and use the [Mask Editor](https://docs.comfy.org/interface/maskeditor) to create the mask.

</details>
