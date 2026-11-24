# Tripo P2: Multiview to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p2_multiview_to_model-1.webp" width="360" alt="Tripo P2: Multiview to Model api_tripo_p2_multiview_to_model-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p2_multiview_to_model-2.webp" width="360" alt="Tripo P2: Multiview to Model api_tripo_p2_multiview_to_model-2.webp">

> Generate production-ready 3D models from up to four reference views using Tripo P2.0 Preview, which reconstructs geometry with native quad topology and triangle meshes up to 50,000 faces. Ideal for game characters and props ready for rigging, hard-surface mechanical assets, and high-volume real-time pipelines.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p2_multiview_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_tripo_p2_multiview_to_model.json)

## Details

| | |
|---|---|
| Name | `api_tripo_p2_multiview_to_model` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Tripo P2 |
| Tags | 3D, API |
| Type | API |
| Date | 2026-09-18 |
| Author | ComfyUI |
| Download size | 102.4 MB |
| Min ComfyUI version | 0.36.0 |
| Usage | 129 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #16 | image | worker_doll_front.png |
| input | `LoadImage` #19 | image | worker_doll_back.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `MarkdownNote` | 1 |  |
| `Save3DAdvanced` | 1 |  |
| `TripoConversionNode` | 1 | comfy-core |
| `TripoPSeriesMultiviewToModelNode` | 1 |  |
| `TripoRetargetNode` | 1 | comfy-core |
| `TripoRigNode` | 1 | comfy-core |
| `TripoTextureNodeV2` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [worker_doll_front.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/worker_doll_front.png)
- [worker_doll_back.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/worker_doll_back.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
