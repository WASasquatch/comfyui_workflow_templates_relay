# Graphic Design Recomposer

[← Brand & Design](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_graphic_color_remixer-1.webp" width="360" alt="Graphic Design Recomposer template_graphic_color_remixer-1.webp">

> Upload a graphic design and select your desired aspect ratio. Generates and recomposes the graphic to fit the new aspect ratio.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_graphic_color_remixer.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_graphic_color_remixer.json)

## Details

| | |
|---|---|
| Name | `template_graphic_color_remixer` |
| Category | Applied › Brand & Design |
| Media type | image |
| Models | Nano Banana Pro |
| Tags | API, Image Edit, Image |
| Type | API |
| Date | 2026-03-30 |
| Author | hellorob |
| Min ComfyUI version | 0.16.0 |
| Usage | 4 |
| Nodes | 97 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #5001 | image | input_graphic-1x1.png |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)

## Subgraphs

- **Stitch 2x2** (3 nodes)
- **Stitch 3x3** (8 nodes)
- **Stitch 4x4** (15 nodes)
- **Crop 2x2** (10 nodes)
- **Crop 3x3** (17 nodes)
- **Crop 4x4** (26 nodes)
- **Prompt + Select Grid Size** (15 nodes)
- **Crop Tiles** (5 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ImageCrop` | 29 | comfy-core |
| `ImageStitch` | 26 | comfy-core |
| `SimpleMath+` | 18 | comfyui_essentials |
| `ComfySwitchNode` | 4 | comfy-core |
| `GetImageSize` | 3 | comfy-core |
| `ImageBatchMulti` | 3 | comfyui-kjnodes |
| `PrimitiveNode` | 3 |  |
| `RegexReplace` | 2 | comfy-core |
| `SaveImage` | 2 | comfy-core |
| `StringCompare` | 2 | comfy-core |
| `CustomCombo` | 1 | comfy-core |
| `GeminiImage2Node` | 1 | comfy-core |
| `ImageScaleToTotalPixels` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `ResizeImageMaskNode` | 1 | comfy-core |
