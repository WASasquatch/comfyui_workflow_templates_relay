# Style Transfer - Recraft Text-to-Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template-recraft_create_style)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template-recraft_create_style-1.webp" width="360" alt="Style Transfer - Recraft Text-to-Image template-recraft_create_style-1.webp">

> Upload 1-5 style references and create a style ID to generate consistent, on brand images.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template-recraft_create_style.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template-recraft_create_style.json)

## Details

| | |
|---|---|
| Name | `template-recraft_create_style` |
| Category | Foundation › Image |
| Output | image |
| Models | Recraft |
| Tags | API, Style Transfer |
| Type | API |
| Date | 2026-02-11 |
| Author | hellorob |
| Min ComfyUI version | 0.12.0 |
| Usage | 23 |
| Nodes | 15 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | input_style_1.png |
| input | `LoadImage` #23 | image | input_style_2.png |
| input | `LoadImage` #24 | image | input_style_3.png |
| input | `LoadImage` #25 | image | input_style_4.png |
| input | `LoadImage` #26 | image | input_style_5.png |
| output | `SaveImage` #37 | image | template-recraft_create_style.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 5 | comfy-core |
| `MarkdownNote` | 2 |  |
| `PrimitiveNode` | 2 |  |
| `RecraftStyleV3InfiniteStyleLibrary` | 2 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `RecraftCreateStyleNode` | 1 | comfy-core |
| `RecraftTextToImageNode` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Load **up to** 5 style reference images to create your Recraft style ID.

If you do not have 5 style images, bypass unused 'Load Style Image' nodes with `CTRL/CMD + B`

</details>

<details><summary>MarkdownNote</summary>

After running the workflow once, you can view your ID in the "Preview Recraft Style ID" node.

To avoid creating a new style ID on each job, copy/paste the ID into the "Recraft - Infinite Style Library (Manual)". Connect the output into the Recraft Text to Image input.

Then, bypass `CTRL/CMD + B` the 'Recraft Create Style' API node.

</details>
