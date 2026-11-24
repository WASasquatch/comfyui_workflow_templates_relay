# Relight: Magnific

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magnific_image_relight-1.webp" width="360" alt="Relight: Magnific api_magnific_image_relight-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magnific_image_relight-2.webp" width="360" alt="Relight: Magnific api_magnific_image_relight-2.webp">

> Upload a source image and a reference lighting image. Generate a relit version of your source image, applying the lighting conditions from the reference.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magnific_image_relight.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_magnific_image_relight.json)

## Details

| | |
|---|---|
| Name | `api_magnific_image_relight` |
| Category | Foundation › Image Tools |
| Media type | image |
| Models | Magnific |
| Tags | API, Relight |
| Type | API |
| Date | 2026-01-26 |
| Author | ComfyUI |
| Min ComfyUI version | 0.11.0 |
| Usage | 22 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #11 | image | magical-portrait.png |
| input | `LoadImage` #13 | image | vintage-girl.png |
| output | `SaveImage` #14 | image | api_magnific_image_relight.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `MagnificImageRelightNode` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
