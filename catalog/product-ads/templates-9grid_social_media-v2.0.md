# 3x3 Grid For Product Ads

[← Product & Ads](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates-9grid_social_media-v2.0)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-9grid_social_media-v2.0-1.webp" width="360" alt="3x3 Grid For Product Ads templates-9grid_social_media-v2.0-1.webp">

> Upload your product and enter a brief prompt for each grid position in a 3x3 grid. Generates 9 distinct images. Select the images you like and upscale to 4k using your product as reference.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-9grid_social_media-v2.0.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-9grid_social_media-v2.0.json)

## Details

| | |
|---|---|
| Name | `templates-9grid_social_media-v2.0` |
| Category | Applied › Product & Ads |
| Output | image |
| Models | Nano Banana Pro, Google |
| Tags | API, Image Edit, Image |
| Type | API |
| Date | 2025-12-06 |
| Author | hellorob |
| Min ComfyUI version | 0.15.0 |
| Usage | 31 |
| Nodes | 71 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #11 | image | template-3x3_Grid_For_Product_Ads Assets.png |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)

## Subgraphs

- **Crop Images** (39 nodes)
- **Select and Batch** (5 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveImage` | 11 | comfy-core |
| `PreviewImage` | 10 | comfy-core |
| `SimpleMath+` | 10 | comfyui_essentials |
| `ImageCropV2` | 9 | comfy-core |
| `PrimitiveBoundingBox` | 9 |  |
| `Reroute` | 9 |  |
| `GeminiImage2Node` | 2 | comfy-core |
| `GetImageSize` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `ImageBatchMulti` | 1 | comfyui-kjnodes |
| `ImageFromBatch` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `Note` | 1 |  |
| `ResizeAndPadImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
Nano Banana Pro may generate with borders between grid images.

Increase this value to crop out the borders.
```

</details>

<details><summary>Required Custom Nodes (For local user)</summary>

[How to install custom nodes](https://docs.comfy.org/installation/install_custom_node)

Custom nodes in this workflow
- [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes)
- [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials)

</details>
