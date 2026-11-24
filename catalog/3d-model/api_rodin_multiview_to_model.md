# Rodin: Multiview to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_rodin_multiview_to_model)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_rodin_multiview_to_model-1.webp" width="360" alt="Rodin: Multiview to Model api_rodin_multiview_to_model-1.webp">

> Sculpt comprehensive 3D models using Rodin's multi-angle reconstruction.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_rodin_multiview_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_rodin_multiview_to_model.json)

## Details

| | |
|---|---|
| Name | `api_rodin_multiview_to_model` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Rodin |
| Tags | Image to 3D, 3D, API |
| Type | API |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.23.0 |
| Usage | 13 |
| Nodes | 14 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #40 | image | api_rodin_multiview_to_model_left.jpg |
| input | `LoadImage` #41 | image | api_rodin_multiview_to_model_front.jpg |
| input | `LoadImage` #56 | image | api_rodin_multiview_to_model_back.jpg |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Preview3D` | 4 | comfy-core |
| `LoadImage` | 3 | comfy-core |
| `MarkdownNote` | 2 |  |
| `BatchImagesNode` | 1 | comfy-core |
| `Rodin3D_Detail` | 1 | comfy-core |
| `Rodin3D_Regular` | 1 | comfy-core |
| `Rodin3D_Sketch` | 1 | comfy-core |
| `Rodin3D_Smooth` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Rodin provides model generation APIs with different levels of precision. You can set the corresponding nodes to the "always" mode according to your requirements.

</details>

<details><summary>File location</summary>

Output model will be auto saved to "ComfyUI/output/Rodin3D"

Or you can use the export function in the preview 3D node to download it.

</details>
