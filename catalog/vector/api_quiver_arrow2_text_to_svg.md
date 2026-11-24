# Arrow2: Text to SVG

[← Vector](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_quiver_arrow2_text_to_svg-1.webp" width="360" alt="Arrow2: Text to SVG api_quiver_arrow2_text_to_svg-1.webp">

> Generate editable SVG vector graphics directly from text prompts using Arrow 2, producing one image output with no file inputs required. Ideal for illustrations, technical diagrams, logo design, and turning written briefs into clean, scalable vector assets.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_quiver_arrow2_text_to_svg.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_quiver_arrow2_text_to_svg.json)

## Details

| | |
|---|---|
| Name | `api_quiver_arrow2_text_to_svg` |
| Category | Foundation › Vector |
| Media type | image |
| Models | Quiver |
| Tags | API, Vector |
| Type | API |
| Date | 2026-09-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.39.2 |
| Usage | 13 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveSVGNode` #5 | image | api_quiver_arrow2_text_to_svg.svg |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `QuiverTextToSVGNodeV2` | 1 |  |
| `SaveSVGNode` | 1 | comfy-core |
