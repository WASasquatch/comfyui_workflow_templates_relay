# HY 3D 2.0

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_hunyuan3d_image_to_model-1.webp" width="360" alt="HY 3D 2.0 3d_hunyuan3d_image_to_model-1.webp">

> Generate a textured-ready 3D mesh from a single image using Hunyuan3D 2.0's shape diffusion pipeline, which aligns geometry to the given image and outputs an untextured white mesh. Ideal for 3D asset prototyping, game and AR content prep, and as a base for later texture painting or handcrafted detailing.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_hunyuan3d_image_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/3d_hunyuan3d_image_to_model.json)

## Details

| | |
|---|---|
| Name | `3d_hunyuan3d_image_to_model` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Hunyuan3D, Tencent |
| Tags | Image to 3D, 3D |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 4.6 GB |
| Min ComfyUI version | 0.36.0 |
| Usage | 55 |
| Nodes | 12 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #56 | image | 3d_hunyuan3d_image_to_model_input_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `hunyuan3d-dit-v2_fp16.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/hunyuan3D_2.0_repackaged/resolve/main/split_files/hunyuan3d-dit-v2_fp16.safetensors) |

## Subgraphs

- **Image to Model (Hunyuan3D 2.0)** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `CLIPVisionEncode` | 1 | comfy-core |
| `EmptyLatentHunyuan3Dv2` | 1 | comfy-core |
| `Hunyuan3Dv2Conditioning` | 1 | comfy-core |
| `ImageOnlyCheckpointLoader` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `SaveGLB` | 1 | comfy-core |
| `VAEDecodeHunyuan3D` | 1 | comfy-core |
| `VoxelToMesh` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>CFG setting</summary>

Set the cfg value between 4 and 8. Thanks for the feedback from Manifold.

</details>

<details><summary>Note: Model link</summary>

## Input Asset

- [3d_hunyuan3d_image_to_model_input_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/3d_hunyuan3d_image_to_model_input_image.png)

## Model Link

- [Hugging Face:Comfy-Org/hunyuan3D_2.0_repackaged](https://huggingface.co/Comfy-Org/hunyuan3D_2.0_repackaged)
- [ModelScope:Comfy-Org/hunyuan3D_2.0_repackaged](https://modelscope.cn/models/Comfy-Org/hunyuan3D_2.0_repackaged)

**checkpoints**

- [hunyuan3d-dit-v2_fp16.safetensors](https://huggingface.co/Comfy-Org/hunyuan3D_2.0_repackaged/resolve/main/split_files/hunyuan3d-dit-v2_fp16.safetensors) (4.59 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 checkpoints/
│       └── hunyuan3d-dit-v2_fp16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
