# Recraft 4.1: Text to Vector

[← Vector](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_recraft_v4_1_text_to_vector)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_1_text_to_vector-1.webp" width="360" alt="Recraft 4.1: Text to Vector api_recraft_v4_1_text_to_vector-1.webp">

> Generate a clean, flat vector logo from a text prompt using Recraft V4.1, producing one scalable SVG output with no file input required. Ideal for branding and logo design, vector illustration projects, and creating consistent flat-color graphics for presentations or merchandise.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_v4_1_text_to_vector.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_recraft_v4_1_text_to_vector.json)

## Details

| | |
|---|---|
| Name | `api_recraft_v4_1_text_to_vector` |
| Category | Foundation › Vector |
| Output | image |
| Models | Recraft |
| Tags | Vector, API |
| Type | API |
| Date | 2026-07-28 |
| Author | ComfyUI |
| Min ComfyUI version | 0.29.0 |
| Usage | 44 |
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
