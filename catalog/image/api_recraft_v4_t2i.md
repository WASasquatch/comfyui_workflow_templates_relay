# Recraft v4: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_t2i-1.webp" width="360" alt="Recraft v4: Text to Image api_recraft_v4_t2i-1.webp">

> Input a text prompt to generate a high-resolution image. Use the Recraft V4 model for enhanced realism, text accuracy, and detailed vector graphics. Output a 1024x1024 or 2048x2048 image based on your selected version.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_recraft_v4_t2i.json)

## Details

| | |
|---|---|
| Name | `api_recraft_v4_t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | Recraft |
| Tags | API, Image, Text to Image |
| Type | API |
| Date | 2026-02-17 |
| Author | ComfyUI |
| Min ComfyUI version | 0.14.1 |
| Usage | 9 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #5 | image | api_recraft_v4_t2i.png |

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
