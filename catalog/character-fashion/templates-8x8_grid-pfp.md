# Profile Picture Stylized Variations

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates-8x8_grid-pfp)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-8x8_grid-pfp-1.webp" width="360" alt="Profile Picture Stylized Variations templates-8x8_grid-pfp-1.webp">

> Upload your profile picture, enter a theme and generate 64 variations.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-8x8_grid-pfp.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-8x8_grid-pfp.json)

## Details

| | |
|---|---|
| Name | `templates-8x8_grid-pfp` |
| Category | Applied › Character & Fashion |
| Output | image |
| Models | Nano Banana Pro, Google, Gemini3 Pro Image Preview |
| Tags | API, Image Edit |
| Type | API |
| Date | 2025-12-18 |
| Author | hellorob |
| Min ComfyUI version | 0.15.0 |
| Usage | 1 |
| Nodes | 273 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #10 | image | subject-profile.png |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)

## Subgraphs

- **Crop Images** (259 nodes)
- **Select and Batch** (5 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewImage` | 73 | comfy-core |
| `ImageCropV2` | 64 | comfy-core |
| `PrimitiveBoundingBox` | 64 |  |
| `Reroute` | 34 |  |
| `SimpleMath+` | 17 | comfyui_essentials |
| `ImageBatchMulti` | 9 | comfyui-kjnodes |
| `SaveImage` | 3 | comfy-core |
| `GeminiImage2Node` | 2 | comfy-core |
| `GetImageSize` | 2 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `ImageFromBatch` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `PrimitiveInt` | 1 | comfy-core |
| `ResizeAndPadImage` | 1 | comfy-core |
