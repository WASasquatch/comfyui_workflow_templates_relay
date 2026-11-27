# HY 3D 2.0 MV

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=3d_hunyuan3d_multiview_to_model)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_hunyuan3d_multiview_to_model-1.webp" width="360" alt="HY 3D 2.0 MV 3d_hunyuan3d_multiview_to_model-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_hunyuan3d_multiview_to_model-2.webp" width="360" alt="HY 3D 2.0 MV 3d_hunyuan3d_multiview_to_model-2.webp">

> Generate 3D models from multiple views using Hunyuan3D 2.0 MV.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_hunyuan3d_multiview_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/3d_hunyuan3d_multiview_to_model.json)

## Details

| | |
|---|---|
| Name | `3d_hunyuan3d_multiview_to_model` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Hunyuan3D, Tencent |
| Tags | 3D, Image to 3D |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 4.6 GB |
| Min ComfyUI version | 0.3.28 |
| Usage | 67 |
| Nodes | 18 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #56 | image | 3d_hunyuan3d_multiview_to_model_front_image.png |
| input | `LoadImage` #78 | image | 3d_hunyuan3d_multiview_to_model_left_image.png |
| input | `LoadImage` #80 | image | 3d_hunyuan3d_multiview_to_model_back_image.png |
| input | `LoadImage` #87 | image | 3d_hunyuan3d_multiview_to_model_right_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `hunyuan3d-dit-v2-mv_fp16.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/hunyuan3D_2.0_repackaged/resolve/main/split_files/hunyuan3d-dit-v2-mv_fp16.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPVisionEncode` | 4 | comfy-core |
| `LoadImage` | 4 | comfy-core |
| `MarkdownNote` | 2 |  |
| `EmptyLatentHunyuan3Dv2` | 1 | comfy-core |
| `Hunyuan3Dv2ConditioningMultiView` | 1 | comfy-core |
| `ImageOnlyCheckpointLoader` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `SaveGLB` | 1 | comfy-core |
| `VAEDecodeHunyuan3D` | 1 | comfy-core |
| `VoxelToMesh` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>CFG setting</summary>

Try adjusting the CFG settings to get better output.

</details>

<details><summary>MarkdownNote</summary>

[Tutorial](https://docs.comfy.org/tutorials/3d/hunyuan3D-2)


## Model link

- [Hugging Face:Comfy-Org/hunyuan3D_2.0_repackaged](https://huggingface.co/Comfy-Org/hunyuan3D_2.0_repackaged)
- [ModelScope:Comfy-Org/hunyuan3D_2.0_repackaged](https://modelscope.cn/models/Comfy-Org/hunyuan3D_2.0_repackaged)

**checkpoints**

- [hunyuan3d-dit-v2-mv_fp16.safetensors](https://huggingface.co/Comfy-Org/hunyuan3D_2.0_repackaged/resolve/main/split_files/hunyuan3d-dit-v2-mv_fp16.safetensors) (4.59 GB)


Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 checkpoints/
│          └── hunyuan3d-dit-v2-mv_fp16.safetensors
```

</details>
