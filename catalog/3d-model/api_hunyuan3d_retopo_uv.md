# Hunyuan3D: Model Retopology and UV Unwrapping

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_retopo_uv-1.webp" width="360" alt="Hunyuan3D: Model Retopology and UV Unwrapping api_hunyuan3d_retopo_uv-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_retopo_uv-2.webp" width="360" alt="Hunyuan3D: Model Retopology and UV Unwrapping api_hunyuan3d_retopo_uv-2.webp">

> Input a dense mesh (from AI generation or photogrammetry scans) and create a lightweight model with good topology and unwrapped UV. Great for 3D game asset optimization.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_retopo_uv.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_hunyuan3d_retopo_uv.json)

## Details

| | |
|---|---|
| Name | `api_hunyuan3d_retopo_uv` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Hunyuan3D |
| Tags | API, 3D |
| Type | API |
| Date | 2026-03-07 |
| Author | shane |
| Min ComfyUI version | 0.16.4 |
| Usage | 12 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `Load3D` #265 | 3d | toy.glb |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveGLB` | 2 | comfy-core |
| `Load3D` | 1 | comfy-core |
| `TencentModelTo3DUVNode` | 1 | comfy-core |
| `TencentSmartTopologyNode` | 1 | comfy-core |
