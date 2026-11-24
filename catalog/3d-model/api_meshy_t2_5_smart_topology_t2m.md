# Meshy T2.5: Text to Model (Smart Topology)

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_t2_5_smart_topology_t2m-1.webp" width="360" alt="Meshy T2.5: Text to Model (Smart Topology) api_meshy_t2_5_smart_topology_t2m-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_t2_5_smart_topology_t2m-2.webp" width="360" alt="Meshy T2.5: Text to Model (Smart Topology) api_meshy_t2_5_smart_topology_t2m-2.webp">

> Generate a game-ready 3D model from a text prompt with Meshy T2.5. Meshy T2.5 builds the mesh at the triangle budget you set instead of generating a dense mesh and retopologizing it afterwards, so the result drops straight into a game engine. No input files required. Ideal for props, environment dressing and low-poly game assets that need a predictable triangle count.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_t2_5_smart_topology_t2m.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_meshy_t2_5_smart_topology_t2m.json)

## Details

| | |
|---|---|
| Name | `api_meshy_t2_5_smart_topology_t2m` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Meshy |
| Tags | API, Text to 3D |
| Type | API |
| Date | 2026-10-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.42.5 |
| Usage | 15 |
| Nodes | 3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 1 |  |
| `MeshyTextToModelSmartTopologyNode` | 1 |  |
| `SaveGLB` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# Meshy T2.5: Text to Model (Smart Topology)

Describe the object you want and Meshy T2.5 returns a game-ready mesh built directly at the triangle budget you ask for, so there is no separate retopology step before it goes into an engine.

## Parameters

- `target_polycount` is the approximate triangle count of the result, from 100 to 30000.
- `pose_mode` stays empty for props; pick A-pose or T-pose for characters that must land in a fixed stance.
- `seed` only controls whether the node re-runs. Meshy output is non-deterministic regardless of the seed.

Save GLB writes the mesh from the node's GLB output, not the task id or the FBX output.

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
