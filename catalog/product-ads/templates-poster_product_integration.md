# Generate Poster/Ad Asset with your Product

[← Product & Ads](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates-poster_product_integration)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-poster_product_integration-1.webp" width="360" alt="Generate Poster/Ad Asset with your Product templates-poster_product_integration-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-poster_product_integration-2.webp" width="360" alt="Generate Poster/Ad Asset with your Product templates-poster_product_integration-2.webp">

> Upload your product and a simple text prompt for the poster or ad design. Iterate on the look before swapping the product into the generated layout.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-poster_product_integration.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-poster_product_integration.json)

## Details

| | |
|---|---|
| Name | `templates-poster_product_integration` |
| Category | Applied › Product & Ads |
| Output | image |
| Models | ByteDance, Google Gemini, Seedream |
| Tags | API, Image Edit |
| Type | API |
| Date | 2025-12-15 |
| Author | hellorob |
| Min ComfyUI version | 0.36.0 |
| Usage | 16 |
| Nodes | 16 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #15 | image | comfy_cloud_water_can.jpg |
| output | `SaveImage` #10 | image | templates-poster_product_integration-1.png |
| output | `SaveImage` #13 | image | templates-poster_product_integration-2.png |

## Custom nodes required

- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)

## Subgraphs

- **Batch Images** (7 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDanceSeedreamNodeV3` | 2 | comfy-core |
| `PreviewImage` | 2 | comfy-core |
| `Reroute` | 2 |  |
| `SaveImage` | 2 | comfy-core |
| `BatchImagesNode` | 1 |  |
| `GeminiNodeV3` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageRemoveBackground+` | 1 | comfyui_essentials |
| `LoadImage` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `RemBGSession+` | 1 | comfyui_essentials |
| `ResizeAndPadImage` | 1 | comfy-core |
