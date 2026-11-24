# Recraft Style Reference Generation

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_style_reference-1.webp" width="360" alt="Recraft Style Reference Generation api_recraft_style_reference-1.webp">

> Upload multiple images to create a consistent style reference. Generate new images using this reference to maintain visual coherence across outputs.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_style_reference.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_recraft_style_reference.json)

## Details

| | |
|---|---|
| Name | `api_recraft_style_reference` |
| Category | Foundation › Image |
| Media type | image |
| Models | Recraft |
| Tags | API, Image, Style Reference |
| Type | API |
| Date | 2026-02-05 |
| Author | ComfyUI |
| Min ComfyUI version | 0.12.0 |
| Usage | 22 |
| Nodes | 11 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #29 | image | recraft_style_ref-1.png |
| input | `LoadImage` #36 | image | recraft_style_ref-3.png |
| input | `LoadImage` #38 | image | recraft_style_ref-2.png |
| input | `LoadImage` #39 | image | recraft_style_ref-4.png |
| output | `SaveImage` #34 | image | api_recraft_style_reference.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 4 | comfy-core |
| `RecraftStyleV3InfiniteStyleLibrary` | 2 | comfy-core |
| `MarkdownNote` | 1 |  |
| `PreviewAny` | 1 | comfy-core |
| `RecraftCreateStyleNode` | 1 | comfy-core |
| `RecraftTextToImageNode` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

After running the workflow once, you can see your style ID in the "Preview as Text" node.

To avoid creating a new style ID for each job, copy and paste the ID into the "Recraft - Infinite Style Library (Manual)" and connect the output to the Recraft Text to Image input.

Then, bypass `CTRL/CMD + B` the 'Recraft Create Style' API node.

</details>
