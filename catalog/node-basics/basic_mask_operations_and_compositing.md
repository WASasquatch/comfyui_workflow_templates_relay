# Mask Operations, Combining & Compositing

[← Node Basics](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=basic_mask_operations_and_compositing)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/basic_mask_operations_and_compositing-1.webp" width="360" alt="Mask Operations, Combining & Compositing basic_mask_operations_and_compositing-1.webp">

> Interactive walkthrough of core image and mask nodes — create and refine masks, combine overlapping masks with different operations, and composite images using feathered masks. No models required.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/basic_mask_operations_and_compositing.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/basic_mask_operations_and_compositing.json)

## Details

| | |
|---|---|
| Name | `basic_mask_operations_and_compositing` |
| Category | Foundation › Node Basics |
| Output | image |
| Models | None |
| Tags | Node Basics |
| Type | open source |
| Date | 2026-03-24 |
| Author | ComfyUI |
| Min ComfyUI version | 0.3.30 |
| Usage | 16 |
| Nodes | 41 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #374 | image | example.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MaskPreview` | 14 | comfy-core |
| `MaskComposite` | 7 | comfy-core |
| `MarkdownNote` | 4 |  |
| `PreviewImage` | 4 | comfy-core |
| `EmptyImage` | 2 | comfy-core |
| `FeatherMask` | 2 | comfy-core |
| `SolidMask` | 2 | comfy-core |
| `ImageCompositeMasked` | 1 | comfy-core |
| `ImageToMask` | 1 | comfy-core |
| `InvertMask` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MaskToImage` | 1 | comfy-core |
| `ThresholdMask` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Image & Mask Compositing</summary>

Paste one image onto another — the **mask** decides where the overlay appears.

**Empty Image** creates a quick test image (set width, height, and color).

**Image Composite Masked** blends the source onto the destination at position x/y. Only the white area of the mask shows the overlay. Toggle *resize source* to stretch the source to match the destination size.

The mask here comes from the **Combine Masks** section below, passed through **Feather Mask** first — check the mask preview on the right to see the softened edges before compositing.

Run the workflow and check the large **Preview Image** for the final result.

</details>

<details><summary>Note: Mask Operations</summary>

Masks are grayscale maps — **white** = active, **black** = inactive. They control *where* an effect applies.

This section walks through common mask tools:

- **Image to Mask** — pull a mask from an image channel (red / green / blue / alpha)
- **Mask to Image** — turn a mask into a visible grayscale image
- **Invert Mask** — swap active and inactive areas
- **Threshold Mask** — snap soft values to hard black/white using a cutoff
- **Feather Mask** — fade the edges (set fade amount per side: left, top, right, bottom)

Use **Preview Mask** nodes along the chain to inspect each step. Queue the workflow and follow left to right to see how a mask is built and refined.

</details>

<details><summary>Note: Combine Masks</summary>

Two masks are built on a gray canvas, then merged with different operations to show how each mode behaves.

**Setup:** A gray **Solid Mask** (0.5) acts as the canvas. Two white squares are placed at different positions using **Combine Masks** with *add* — preview these first to see each shape.

**Compare operations** on the overlapping pair (same x/y offset on each row):

- **multiply** — keeps only where both masks overlap
- **add** — brightens the overlapping area
- **and** — white only where both are active
- **or** — merges both shapes together
- **xor** — keeps areas that don't overlap

Each row has a **Preview Mask** — compare them side by side to see the difference.

</details>

<details><summary>MarkdownNote</summary>

## Try It Yourself

Replace **Empty Image** with **Load Image** to use your own file. Open the **[Mask Editor](https://docs.comfy.org/interface/maskeditor)** on the Load Image node to draw a mask directly on your image.

Connect the image and mask outputs into any section above to see how the nodes respond to real data — this is the fastest way to learn.

</details>
