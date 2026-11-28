# Tripo P2: Text to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_tripo_p2_text_to_model)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p2_text_to_model-1.webp" width="360" alt="Tripo P2: Text to Model api_tripo_p2_text_to_model-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p2_text_to_model-2.webp" width="360" alt="Tripo P2: Text to Model api_tripo_p2_text_to_model-2.webp">

> Generate production-ready 3D meshes from text prompts with Tripo P2, featuring native quad topology and mesh budgets up to 50,000 triangles or 25,000 quads. Ideal for game characters and props, hard-surface assets, and high-volume pipelines needing clean, rig-ready geometry.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_p2_text_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_tripo_p2_text_to_model.json)

## Details

| | |
|---|---|
| Name | `api_tripo_p2_text_to_model` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Tripo, Tripo P2 |
| Tags | API, Text to 3D |
| Type | API |
| Date | 2026-09-16 |
| Author | ComfyUI |
| Min ComfyUI version | 0.36.0 |
| Usage | 13 |
| Nodes | 7 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 1 |  |
| `Save3DAdvanced` | 1 |  |
| `TripoConversionNode` | 1 | comfy-core |
| `TripoPSeriesTextToModelNode` | 1 |  |
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
