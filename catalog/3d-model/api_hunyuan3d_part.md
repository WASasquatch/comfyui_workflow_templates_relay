# HY 3D: 3D Parts Decomposition

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_hunyuan3d_part)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_part-1.webp" width="360" alt="HY 3D: 3D Parts Decomposition api_hunyuan3d_part-1.webp">

> Upload a 3D model to automatically segment it into its constituent parts, generating a fully decomposed 3D asset for reuse and editing.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_hunyuan3d_part.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_hunyuan3d_part.json)

## Details

| | |
|---|---|
| Name | `api_hunyuan3d_part` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Hunyuan3D |
| Tags | 3D, API |
| Type | API |
| Date | 2026-02-13 |
| Author | ComfyUI |
| Min ComfyUI version | 0.14.0 |
| Usage | 12 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `Load3D` #36 | 3d | motor_cycle.fbx |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Load3D` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveGLB` | 1 | comfy-core |
| `Tencent3DPartNode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

- Recommended file size not greater than 100MB
- Face count not greater than 30,000
- Only supports FBX format

</details>
