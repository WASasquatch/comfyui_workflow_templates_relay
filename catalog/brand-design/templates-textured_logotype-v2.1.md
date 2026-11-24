# Apply Texture to Logo

[← Brand & Design](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-textured_logotype-v2.1-1.webp" width="360" alt="Apply Texture to Logo templates-textured_logotype-v2.1-1.webp">

> Upload your logotype and apply a texture + elements for on brand asset

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-textured_logotype-v2.1.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-textured_logotype-v2.1.json)

## Details

| | |
|---|---|
| Name | `templates-textured_logotype-v2.1` |
| Category | Applied › Brand & Design |
| Media type | image |
| Models | Gemini3 Pro Image Preview, Nano Banana Pro, Google, ByteDance, Seedance |
| Tags | API, Brand Design, Image to Video, FLF2V |
| Type | API |
| Date | 2025-12-03 |
| Author | hellorob |
| Min ComfyUI version | 0.8.0 |
| Usage | 13 |
| Nodes | 11 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #4 | image | comfy_logo_b.png |
| input | `LoadImage` #17 | image | logotype_texture.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `SaveImage` | 2 | comfy-core |
| `ByteDanceFirstLastFrameNode` | 1 | comfy-core |
| `GeminiImage2Node` | 1 | comfy-core |
| `GeminiImageNode` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageBatch` | 1 | comfy-core |
| `ResizeAndPadImage` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
