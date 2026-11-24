# Recraft v4: Text to Vector

[← Vector](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_text_to_vector-1.webp" width="360" alt="Recraft v4: Text to Vector api_recraft_v4_text_to_vector-1.webp">

> Input text prompts to generate clean, editable vector SVG graphics. Create logos, icons, or illustrations with structured paths suitable for design tools.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_text_to_vector.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_recraft_v4_text_to_vector.json)

## Details

| | |
|---|---|
| Name | `api_recraft_v4_text_to_vector` |
| Category | Foundation › Vector |
| Media type | image |
| Models | Recraft |
| Tags | API, Image, Vector |
| Type | API |
| Date | 2026-02-17 |
| Author | ComfyUI |
| Min ComfyUI version | 0.14.1 |
| Usage | 17 |
| Nodes | 6 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `RecraftColorRGB` | 2 |  |
| `MarkdownNote` | 1 |  |
| `RecraftControls` | 1 |  |
| `RecraftV4TextToVectorNode` | 1 |  |
| `SaveSVGNode` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

If you want more precise control over the image:
- Use the `Recraft Controls` node for more precise color control.
- You can chain multiple `Recraft Color RGB` nodes to provide multiple control colors.

</details>
