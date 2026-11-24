# Meshy T2.5: Image to Model (Smart Topology)

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_t2_5_smart_topology_i2m-1.webp" width="360" alt="Meshy T2.5: Image to Model (Smart Topology) api_meshy_t2_5_smart_topology_i2m-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_t2_5_smart_topology_i2m-2.webp" width="360" alt="Meshy T2.5: Image to Model (Smart Topology) api_meshy_t2_5_smart_topology_i2m-2.webp">

> Generate a game-ready 3D model from a single image with Meshy T2.5. Meshy T2.5 builds the mesh at the triangle budget you set instead of generating a dense mesh and retopologizing it afterwards, so the result drops straight into a game engine. Texturing with PBR maps is optional and runs at 2k, 4k or 8k. Ideal for turning concept art, product photos and sculpts into engine-ready props.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_t2_5_smart_topology_i2m.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_meshy_t2_5_smart_topology_i2m.json)

## Details

| | |
|---|---|
| Name | `api_meshy_t2_5_smart_topology_i2m` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Meshy |
| Tags | API, Image to 3D |
| Type | API |
| Date | 2026-10-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.42.5 |
| Usage | 57 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | abstract_3d_toy_van_game_asset.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `MeshyImageToModelSmartTopologyNode` | 1 |  |
| `SaveGLB` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [abstract_3d_toy_van_game_asset.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/abstract_3d_toy_van_game_asset.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
