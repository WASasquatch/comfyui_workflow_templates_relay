# HY 3D: UV Unwrapping

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_hunyuan3d_model2uv)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_model2uv-1.webp" width="360" alt="HY 3D: UV Unwrapping api_hunyuan3d_model2uv-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_model2uv-2.webp" width="360" alt="HY 3D: UV Unwrapping api_hunyuan3d_model2uv-2.webp">

> Upload a 3D model to perform UV unwrapping. Generate a processed model with optimized UV layout for texturing.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_model2uv.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_hunyuan3d_model2uv.json)

## Details

| | |
|---|---|
| Name | `api_hunyuan3d_model2uv` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Hunyuan3D |
| Tags | API, 3D |
| Type | API |
| Date | 2026-03-07 |
| Author | ComfyUI |
| Min ComfyUI version | 0.14.0 |
| Usage | 8 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `Load3D` #13 | 3d | toy.glb |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveGLB` | 2 | comfy-core |
| `Load3D` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `TencentModelTo3DUVNode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Input limits</summary>

- Supported formats: FBX, OBJ, GLB
- 3D model limit: less than 30,000 faces

</details>
