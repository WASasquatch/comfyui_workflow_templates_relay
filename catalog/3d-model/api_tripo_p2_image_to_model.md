# Tripo P2: Image to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p2_image_to_model-1.webp" width="360" alt="Tripo P2: Image to Model api_tripo_p2_image_to_model-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p2_image_to_model-2.webp" width="360" alt="Tripo P2: Image to Model api_tripo_p2_image_to_model-2.webp">

> Generate a production-ready 3D model from a single reference image using Tripo P2.0 Preview, which builds native quad topology with clean edge flow suited for rigging and animation. It takes 1 input image, with optional multi-view references for better side and back accuracy. Ideal for game characters and props, hard-surface mechanical assets, and high-volume real-time pipelines.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p2_image_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_tripo_p2_image_to_model.json)

## Details

| | |
|---|---|
| Name | `api_tripo_p2_image_to_model` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Tripo P2 |
| Tags | 3D, API, Image to 3D |
| Type | API |
| Date | 2026-09-16 |
| Author | ComfyUI |
| Min ComfyUI version | 0.36.0 |
| Usage | 130 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #16 | image | designer_toy_3d.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `LoadImage` | 1 |  |
| `Save3DAdvanced` | 1 |  |
| `TripoConversionNode` | 1 | comfy-core |
| `TripoPSeriesImageToModelNode` | 1 |  |
| `TripoRetargetNode` | 1 | comfy-core |
| `TripoRigNode` | 1 | comfy-core |
| `TripoTextureNodeV2` | 1 |  |

## Notes embedded in the workflow

<details><summary>⚠️ Output format</summary>

Please plug the Save 3D to the right slot when you have enabled the `quad` option
| Condition | Output Format |
| --------- | ------------- |
| `quad` enabled | FBX |
| `quad` disabled | GLB |

</details>

<details><summary>MarkdownNote</summary>

## Input Asset

- [designer_toy_3d.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/designer_toy_3d.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
