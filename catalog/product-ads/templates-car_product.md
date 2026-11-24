# 1 Image to Car Product Shots

[← Product & Ads](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-car_product-1.webp" width="360" alt="1 Image to Car Product Shots templates-car_product-1.webp">

> Upload a photo of your vehicle and generate a studio quality video of the vehicle from multiple angles.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-car_product.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-car_product.json)

## Details

| | |
|---|---|
| Name | `templates-car_product` |
| Category | Applied › Product & Ads |
| Media type | image |
| Models | Kling, Seedream |
| Tags | API, FLF2V, Image to Video |
| Type | API |
| Date | 2025-12-18 |
| Author | hellorob |
| Min ComfyUI version | 0.35.2 |
| Usage | 26 |
| Nodes | 38 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #10 | image | product_car.jpg |

## Subgraphs

- **Generate Video** (6 nodes)
- **Generate Video** (6 nodes)
- **Generate Video** (6 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewAny` | 6 | comfy-core |
| `RegexExtract` | 6 | comfy-core |
| `ByteDanceSeedreamNodeV3` | 4 |  |
| `SaveImage` | 4 | comfy-core |
| `SaveVideo` | 4 | comfy-core |
| `GeminiNodeV3` | 3 |  |
| `GetVideoComponents` | 3 | comfy-core |
| `KlingFirstLastFrameNode` | 3 |  |
| `Reroute` | 2 |  |
| `BatchImagesNode` | 1 |  |
| `CreateVideo` | 1 |  |
| `LoadImage` | 1 | comfy-core |
