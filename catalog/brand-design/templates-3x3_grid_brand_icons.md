# 3x3 Brand Icon Assets Grid

[← Brand & Design](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates-3x3_grid_brand_icons)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-3x3_grid_brand_icons-1.webp" width="360" alt="3x3 Brand Icon Assets Grid templates-3x3_grid_brand_icons-1.webp">

> Upload a reference image of an icon, enter your brand information in the prompt and generate 9 unique on brand stylized icon assets.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-3x3_grid_brand_icons.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-3x3_grid_brand_icons.json)

## Details

| | |
|---|---|
| Name | `templates-3x3_grid_brand_icons` |
| Category | Applied › Brand & Design |
| Output | image |
| Models | Gemini3 Pro Image Preview, Google, Nano Banana Pro |
| Tags | API, Brand Design, Image Edit |
| Type | API |
| Date | 2026-01-13 |
| Author | hellorob |
| Min ComfyUI version | 0.15.0 |
| Usage | 16 |
| Nodes | 55 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | input_reference_icon.png |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)

## Subgraphs

- **Crop Images** (30 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewImage` | 10 | comfy-core |
| `SaveImage` | 10 | comfy-core |
| `ImageCrop` | 9 | comfy-core |
| `Reroute` | 9 |  |
| `SimpleMath+` | 9 | comfyui_essentials |
| `PrimitiveStringMultiline` | 2 | comfy-core |
| `GeminiImage2Node` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageBatchMulti` | 1 | comfyui-kjnodes |
| `LoadImage` | 1 | comfy-core |
| `PrimitiveInt` | 1 | comfy-core |
| `RegexReplace` | 1 | comfy-core |
