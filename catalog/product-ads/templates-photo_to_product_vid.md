# Phone Image to Product Video: Shoe

[← Product & Ads](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-photo_to_product_vid-1.webp" width="360" alt="Phone Image to Product Video: Shoe templates-photo_to_product_vid-1.webp">

> Take a picture with your phone, upload it and generate a studio grade product video.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-photo_to_product_vid.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-photo_to_product_vid.json)

## Details

| | |
|---|---|
| Name | `templates-photo_to_product_vid` |
| Category | Applied › Product & Ads |
| Media type | image |
| Models | Seedream, MiniMax |
| Tags | Image to Video, API |
| Type | API |
| Date | 2025-12-18 |
| Author | hellorob |
| Min ComfyUI version | 0.33.3 |
| Usage | 29 |
| Nodes | 16 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | product_shoe.jpeg |

## Subgraphs

- **Combine Video** (6 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveVideo` | 4 | comfy-core |
| `GetVideoComponents` | 3 | comfy-core |
| `MinimaxHailuoVideoNode` | 3 | comfy-core |
| `ImageBatch` | 2 | comfy-core |
| `ByteDanceSeedreamNode` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
