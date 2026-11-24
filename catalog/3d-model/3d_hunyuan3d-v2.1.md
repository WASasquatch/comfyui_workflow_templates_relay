# HY 3D 2.1: Single View to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_hunyuan3d-v2.1-1.webp" width="360" alt="HY 3D 2.1: Single View to Model 3d_hunyuan3d-v2.1-1.webp">

> Reconstruct a 3D model from a single photo using Hunyuan3D 2.1, converting one input image into a raw white-mesh geometry without textures or materials. Ideal for rapid 3D concepting, blockout prototyping, and asset preparation before texturing or retopology.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_hunyuan3d-v2.1.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/3d_hunyuan3d-v2.1.json)

## Details

| | |
|---|---|
| Name | `3d_hunyuan3d-v2.1` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Hunyuan3D, Tencent |
| Tags | Image to 3D, 3D |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 4.6 GB |
| Min ComfyUI version | 0.36.0 |
| Usage | 205 |
| Nodes | 11 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | 3d_hunyuan3d-v2.1_input_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `hunyuan_3d_v2.1.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/hunyuan3D_2.1_repackaged/resolve/main/hunyuan_3d_v2.1.safetensors) |

## Subgraphs

- **Image to 3D (Hunyun3D 2.1)** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPVisionEncode` | 1 | comfy-core |
| `EmptyLatentHunyuan3Dv2` | 1 | comfy-core |
| `Hunyuan3Dv2Conditioning` | 1 | comfy-core |
| `ImageOnlyCheckpointLoader` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `SaveGLB` | 1 | comfy-core |
| `VAEDecodeHunyuan3D` | 1 | comfy-core |
| `VoxelToMesh` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Input Asset

- [3d_hunyuan3d-v2.1_input_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/3d_hunyuan3d-v2.1_input_image.png)

## Model Link

- [Hugging Face:Comfy-Org/hunyuan3D_2.1_repackaged](https://huggingface.co/Comfy-Org/hunyuan3D_2.1_repackaged)
- [ModelScope:Comfy-Org/hunyuan3D_2.1_repackaged](https://modelscope.cn/models/Comfy-Org/hunyuan3D_2.1_repackaged)

**checkpoints**

- [hunyuan_3d_v2.1.safetensors](https://huggingface.co/Comfy-Org/hunyuan3D_2.1_repackaged/resolve/main/hunyuan_3d_v2.1.safetensors) (6.86 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 checkpoints/
│       └── hunyuan_3d_v2.1.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
