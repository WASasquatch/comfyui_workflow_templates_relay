# Rodin: Image to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_rodin_image_to_model-1.webp" width="360" alt="Rodin: Image to Model api_rodin_image_to_model-1.webp">

> Generate detailed 3D models from single photos using Rodin AI.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_rodin_image_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_rodin_image_to_model.json)

## Details

| | |
|---|---|
| Name | `api_rodin_image_to_model` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Rodin |
| Tags | Image to 3D, 3D, API |
| Type | API |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.23.0 |
| Usage | 4 |
| Nodes | 11 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #49 | image | api_rodin_image_to_model_input_image.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Preview3D` | 4 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `Note` | 1 |  |
| `Rodin3D_Detail` | 1 | comfy-core |
| `Rodin3D_Regular` | 1 | comfy-core |
| `Rodin3D_Sketch` | 1 | comfy-core |
| `Rodin3D_Smooth` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Tips</summary>

```text
Try to provide the following types of images:
- Provide images from multiple angles.
- Images with a solid color background.

This helps to generate a model that better meets the requirements. Of course, thanks to Rodin's excellent product capabilities, the subject in the unprocessed image can also achieve a good model output.
```

</details>
