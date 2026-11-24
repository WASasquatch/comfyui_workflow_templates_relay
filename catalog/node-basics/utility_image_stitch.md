# Image Stitch 2x2 Grid

[← Node Basics](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_image_stitch-1.webp" width="360" alt="Image Stitch 2x2 Grid utility_image_stitch-1.webp">

> Combine four input images into a 2x2 grid. Automatically resizes mismatched images and outputs a single 2048x2048 image.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_image_stitch.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_image_stitch.json)

## Details

| | |
|---|---|
| Name | `utility_image_stitch` |
| Category | Foundation › Node Basics |
| Media type | image |
| Models | None |
| Tags | Image, Image Edit |
| Type | open source |
| Date | 2026-03-19 |
| Author | ComfyUI |
| Min ComfyUI version | 0.8.0 |
| Usage | 20 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #12 | image | angle_1.png |
| input | `LoadImage` #13 | image | angle_2.png |
| input | `LoadImage` #14 | image | angle_3.png |
| input | `LoadImage` #15 | image | angle_4.png |
| output | `SaveImage` #19 | image | utility_image_stitch.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 4 | comfy-core |
| `ImageStitch` | 3 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ResizeImageMaskNode` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# Image Stitch Grid Workflow

4 images → 2×2 grid → saved at 2048×2048.

**How it chains:**
1. `Image Stitch (right)` — joins top-left + top-right into a row
2. `Image Stitch (right)` — joins bottom-left + bottom-right into a row
3. `Image Stitch (down)` — stacks both rows into the final grid

**Key settings:**
- `direction` — `right` for horizontal, `down` for vertical
- `match_image_size: ON` — auto-resizes mismatched inputs

</details>
