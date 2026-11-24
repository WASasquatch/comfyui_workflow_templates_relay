# Sprite Sheet Generator

[← Brand & Design](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates-sprite_sheet)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-sprite_sheet-1.webp" width="360" alt="Sprite Sheet Generator templates-sprite_sheet-1.webp">

> Upload an image of your sprite and receive individual frames of idle, attack, walk and jump animations.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-sprite_sheet.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-sprite_sheet.json)

## Details

| | |
|---|---|
| Name | `templates-sprite_sheet` |
| Category | Applied › Brand & Design |
| Output | image |
| Models | Google, Nano Banana Pro |
| Tags | API, Video, Image Edit |
| Type | API |
| Date | 2026-02-05 |
| Author | hellorob |
| Min ComfyUI version | 0.15.0 |
| Usage | 13 |
| Nodes | 575 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | input-sprite-1.png |
| input | `LoadImage` #76 | image | 2x2_grid_image.png |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)
- [comfyui_layerstyle](https://registry.comfy.org/nodes/comfyui_layerstyle)

## Subgraphs

- **Create Animation** (6 nodes)
- **Crop Images** (28 nodes)
- **Create Composites** (4 nodes)
- **Crop+Composite** (24 nodes)
- **Crop+Composite** (25 nodes)
- **Crop+Composite** (25 nodes)
- **Crop+Composite** (25 nodes)
- **Create Animation** (6 nodes)
- **Crop Images** (28 nodes)
- **Create Composites** (4 nodes)
- **Crop+Composite** (24 nodes)
- **Crop+Composite** (25 nodes)
- **Crop+Composite** (25 nodes)
- **Crop+Composite** (25 nodes)
- **Create Animation** (6 nodes)
- **Crop Images** (28 nodes)
- **Create Composites** (4 nodes)
- **Crop+Composite** (24 nodes)
- **Crop+Composite** (25 nodes)
- **Crop+Composite** (25 nodes)
- **Crop+Composite** (25 nodes)
- **Create Animation** (6 nodes)
- **Crop Images** (28 nodes)
- **Create Composites** (4 nodes)
- **Crop+Composite** (24 nodes)
- **Crop+Composite** (25 nodes)
- **Crop+Composite** (25 nodes)
- **Crop+Composite** (25 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewImage` | 116 | comfy-core |
| `GetImageSize` | 64 | comfy-core |
| `SimpleMath+` | 64 | comfyui_essentials |
| `ImageCompositeMasked` | 32 | comfy-core |
| `ImageCrop` | 32 | comfy-core |
| `MaskPreview+` | 32 | comfyui_essentials |
| `ImageResizeKJv2` | 20 | comfyui-kjnodes |
| `SaveImage` | 20 | comfy-core |
| `ColorToMask` | 16 | comfyui-kjnodes |
| `CropMask` | 16 | comfy-core |
| `ImageFromBatch` | 16 | comfy-core |
| `ImagePadForOutpaintMasked` | 16 | comfyui-kjnodes |
| `InvertMask` | 16 | comfy-core |
| `LayerUtility: ColorImage V2` | 16 | comfyui_layerstyle |
| `MaskBoundingBox+` | 16 | comfyui_essentials |
| `RepeatImageBatch` | 16 | comfy-core |
| `Reroute` | 16 |  |
| `SplitImageWithAlpha` | 16 | comfy-core |
| `PrimitiveNode` | 8 |  |
| `BatchImagesNode` | 5 | comfy-core |
| `CreateVideo` | 4 | comfy-core |
| `GeminiImage2Node` | 4 | comfy-core |
| `ImageBatchMulti` | 4 | comfyui-kjnodes |
| `PrimitiveInt` | 4 | comfy-core |
| `SaveVideo` | 4 | comfy-core |
| `LoadImage` | 2 | comfy-core |
