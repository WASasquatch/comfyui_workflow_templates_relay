# Graphic Design Recomposer

[← Brand & Design](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_graphic_design_recomposer)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_graphic_design_recomposer-1.webp" width="360" alt="Graphic Design Recomposer templates_graphic_design_recomposer-1.webp">

> Upload a graphic design and select your desired aspect ratio. Generates and recomposes the graphic to fit the new aspect ratio.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_graphic_design_recomposer.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_graphic_design_recomposer.json)

## Details

| | |
|---|---|
| Name | `templates_graphic_design_recomposer` |
| Category | Applied › Brand & Design |
| Output | image |
| Models | Nano Banana 2, Nano Banana Pro |
| Tags | API, Brand Design |
| Type | API |
| Date | 2026-03-30 |
| Author | hellorob |
| Min ComfyUI version | 0.20.3 |
| Usage | 79 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #125 | image | latent_space_clud.png |
| output | `SaveImage` #131 | image | templates_graphic_design_recomposer.png |

## Subgraphs

- **Recompose Image** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveNode` | 2 |  |
| `ComfySwitchNode` | 1 |  |
| `CustomCombo` | 1 |  |
| `GeminiImage2Node` | 1 |  |
| `GeminiNanoBanana2V2` | 1 |  |
| `LoadImage` | 1 |  |
| `PrimitiveStringMultiline` | 1 |  |
| `SaveImage` | 1 |  |
| `StringCompare` | 1 |  |
