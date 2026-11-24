# Portrait Enhancement: Magnific

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_magnific_skin_enhancer)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magnific_skin_enhancer-1.webp" width="360" alt="Portrait Enhancement: Magnific api_magnific_skin_enhancer-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magnific_skin_enhancer-2.webp" width="360" alt="Portrait Enhancement: Magnific api_magnific_skin_enhancer-2.webp">

> Enhance skin and overall image quality by uploading your image and selecting a preset to adjust lighting, color grading, and realism.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_magnific_skin_enhancer.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_magnific_skin_enhancer.json)

## Details

| | |
|---|---|
| Name | `api_magnific_skin_enhancer` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | Magnific |
| Tags | API, Portrait |
| Type | API |
| Date | 2026-01-26 |
| Author | ComfyUI |
| Min ComfyUI version | 0.11.0 |
| Usage | 134 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #4 | image | close_up_girl_skin.png |
| output | `SaveImage` #5 | image | api_magnific_skin_enhancer.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ImageCompare` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MagnificImageSkinEnhancerNode` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
