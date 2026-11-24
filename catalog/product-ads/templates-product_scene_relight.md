# Composite your Product + Scene and Relight

[← Product & Ads](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-product_scene_relight-1.webp" width="360" alt="Composite your Product + Scene and Relight templates-product_scene_relight-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-product_scene_relight-2.webp" width="360" alt="Composite your Product + Scene and Relight templates-product_scene_relight-2.webp">

> Upload an image of your product and background. Composite them and seamlessly relight and fuse together using Seedream 4.5.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-product_scene_relight.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-product_scene_relight.json)

## Details

| | |
|---|---|
| Name | `templates-product_scene_relight` |
| Category | Applied › Product & Ads |
| Media type | image |
| Models | ByteDance, Seedream |
| Tags | API, Image Edit, Relight |
| Type | API |
| Date | 2025-12-15 |
| Author | hellorob |
| Min ComfyUI version | 0.33.3 |
| Usage | 13 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | comfy_shampoo.png |
| input | `LoadImage` #2 | image | flower_sea.png |
| output | `SaveImage` #23 | image | templates-product_scene_relight.png |

## Subgraphs

- **Batch Images** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `PrimitiveStringMultiline` | 2 |  |
| `BatchImagesNode` | 1 |  |
| `ByteDanceSeedreamNode` | 1 |  |
| `GetImageSize` | 1 |  |
| `RegexReplace` | 1 |  |
| `ResizeAndPadImage` | 1 |  |
| `SaveImage` | 1 |  |
