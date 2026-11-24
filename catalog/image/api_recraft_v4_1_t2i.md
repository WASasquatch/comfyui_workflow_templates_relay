# Recraft 4.1: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_1_t2i-1.webp" width="360" alt="Recraft 4.1: Text to Image api_recraft_v4_1_t2i-1.webp">

> Generate photorealistic and illustrative images from text prompts using Recraft V4.1, producing one high-quality image per generation. This model excels at interpreting short prompts with creative flair, delivering natural photorealism, expressive vectors, and clean illustrations. Ideal for concept art, logo and typography design, and lifestyle product mockups.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_1_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_recraft_v4_1_t2i.json)

## Details

| | |
|---|---|
| Name | `api_recraft_v4_1_t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | Recraft |
| Tags | API, Image, Text to Image |
| Type | API |
| Date | 2026-07-28 |
| Author | ComfyUI |
| Min ComfyUI version | 0.29.0 |
| Usage | 39 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #5 | image | api_recraft_v4_1_t2i.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `RecraftColorRGB` | 2 |  |
| `MarkdownNote` | 1 |  |
| `RecraftControls` | 1 |  |
| `RecraftV4TextToImageNode` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

If you want more precise control over the image:
- Use the `Recraft Controls' node for more precise color control.

</details>
