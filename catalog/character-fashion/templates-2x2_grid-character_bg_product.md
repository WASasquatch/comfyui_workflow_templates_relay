# Fashion Editorial Shots

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates-2x2_grid-character_bg_product)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-2x2_grid-character_bg_product-1.webp" width="360" alt="Fashion Editorial Shots templates-2x2_grid-character_bg_product-1.webp">

> Upload your character, background scene and product. Generate a 2x2 grid, select your desired image and upscale

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-2x2_grid-character_bg_product.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-2x2_grid-character_bg_product.json)

## Details

| | |
|---|---|
| Name | `templates-2x2_grid-character_bg_product` |
| Category | Applied › Character & Fashion |
| Output | image |
| Models | Nano Banana Pro, Google, Google Gemini Image |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-01-13 |
| Author | hellorob |
| Min ComfyUI version | 0.15.0 |
| Usage | 2 |
| Nodes | 50 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | snake_on_jacket.jpg |
| input | `LoadImage` #2 | image | forest_background.jpg |
| input | `LoadImage` #5 | image | brown_moisturizer_bottle.jpg |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)

## Subgraphs

- **Batch Images** (4 nodes)
- **Crop Images** (20 nodes)
- **Batch Images** (3 nodes)
- **Select Image Number #** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SimpleMath+` | 9 | comfyui_essentials |
| `Reroute` | 7 |  |
| `PreviewImage` | 6 | comfy-core |
| `SaveImage` | 6 | comfy-core |
| `ImageCrop` | 4 | comfy-core |
| `GetImageSize` | 3 | comfy-core |
| `LoadImage` | 3 | comfy-core |
| `ResizeAndPadImage` | 3 | comfy-core |
| `BatchImagesNode` | 2 |  |
| `GeminiImage2Node` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `ImageBatchMulti` | 1 | comfyui-kjnodes |
| `ImageFromBatch` | 1 | comfy-core |
| `ImageResizeKJv2` | 1 | comfyui-kjnodes |
