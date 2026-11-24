# Apply Texture + Elements to Logo

[← Brand & Design](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-textured_logo_elements-1.webp" width="360" alt="Apply Texture + Elements to Logo templates-textured_logo_elements-1.webp">

> Upload your logo, texture and elements. Generate a video of the textured logo for an on brand asset.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-textured_logo_elements.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-textured_logo_elements.json)

## Details

| | |
|---|---|
| Name | `templates-textured_logo_elements` |
| Category | Applied › Brand & Design |
| Media type | image |
| Models | Gemini3 Pro Image Preview, Nano Banana Pro, Google, ByteDance, Seedance |
| Tags | API, Brand Design, Image to Video |
| Type | API |
| Date | 2025-12-11 |
| Author | hellorob |
| Min ComfyUI version | 0.8.0 |
| Usage | 6 |
| Nodes | 11 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #4 | image | comfy_logo_b.png |
| input | `LoadImage` #17 | image | furry_ball.png |
| input | `LoadImage` #18 | image | furry_tech.png |

## Subgraphs

- **Batch Images** (4 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 3 | comfy-core |
| `ResizeAndPadImage` | 2 |  |
| `BatchImagesNode` | 1 |  |
| `ByteDanceImageToVideoNode` | 1 |  |
| `GeminiImage2Node` | 1 | comfy-core |
| `GetImageSize` | 1 |  |
| `SaveImage` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
