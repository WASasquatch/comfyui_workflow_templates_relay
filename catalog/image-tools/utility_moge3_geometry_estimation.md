# Geometry Estimation: MoGe 3

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_moge3_geometry_estimation-1.webp" width="360" alt="Geometry Estimation: MoGe 3 utility_moge3_geometry_estimation-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_moge3_geometry_estimation-2.webp" width="360" alt="Geometry Estimation: MoGe 3 utility_moge3_geometry_estimation-2.webp">

> Estimate fine-detailed geometry from a single image with MoGe 3, the sparse-volumetric refinement version of MoGe. It lifts a coarse point map onto a sparse voxel shell and refines depth with lightweight sparse 3D convolutions, keeping thin structures and depth discontinuities that image-space decoders blur. Ships with the ViT-L checkpoint; the ViT-G file is selectable in the same Load MoGe Model dropdown for higher fine-detail accuracy. Takes 1 image input and outputs 1 depth map and 1 normal map.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_moge3_geometry_estimation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_moge3_geometry_estimation.json)

## Details

| | |
|---|---|
| Name | `utility_moge3_geometry_estimation` |
| Category | Foundation › Image Tools |
| Media type | image |
| Models | MoGe |
| Tags | Depth Estimation, Normal Estimation |
| Type | open source |
| Date | 2026-09-18 |
| Author | ComfyUI |
| Download size | 2.3 GB |
| Min ComfyUI version | 0.37.0 |
| Usage | 34 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | cosmic_suitcase.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `moge_3_vitg_fp16.safetensors` | `geometry_estimation` | [link](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_3_vitg_fp16.safetensors) |

## Subgraphs

- **Geometry Estimation (MoGe 3)** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `LoadMoGeModel` | 1 |  |
| `MarkdownNote` | 1 |  |
| `MoGeInference` | 1 |  |
| `MoGeRender` | 1 |  |
| `PreviewImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Input Asset

- [cosmic_suitcase.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/cosmic_suitcase.png)

## Model Links

- [Hugging Face:Comfy-Org/MoGe](https://huggingface.co/Comfy-Org/MoGe)

### Alternative Repos

- [ModelScope:Comfy-Org/MoGe](https://modelscope.cn/models/Comfy-Org/MoGe)

**geometry_estimation** (one of the models below)

- [moge_3_vitg_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_3_vitg_fp16.safetensors) (2.33 GB)
- [moge_3_vitl_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_3_vitl_fp16.safetensors) (706.3 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 geometry_estimation/
│       ├── moge_3_vitl_fp16.safetensors
│       └── moge_3_vitg_fp16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
