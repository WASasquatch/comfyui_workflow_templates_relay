# HY 3D 2.0 MV Turbo

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=3d_hunyuan3d_multiview_to_model_turbo)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_hunyuan3d_multiview_to_model_turbo-1.webp" width="360" alt="HY 3D 2.0 MV Turbo 3d_hunyuan3d_multiview_to_model_turbo-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_hunyuan3d_multiview_to_model_turbo-2.webp" width="360" alt="HY 3D 2.0 MV Turbo 3d_hunyuan3d_multiview_to_model_turbo-2.webp">

> Generate 3D models from multiple views using Hunyuan3D 2.0 MV Turbo.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_hunyuan3d_multiview_to_model_turbo.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/3d_hunyuan3d_multiview_to_model_turbo.json)

## Details

| | |
|---|---|
| Name | `3d_hunyuan3d_multiview_to_model_turbo` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Hunyuan3D, Tencent |
| Tags | Image to 3D, 3D |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 4.6 GB |
| Min ComfyUI version | 0.3.28 |
| Usage | 22 |
| Nodes | 19 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #56 | image | 3d_hunyuan3d_multiview_to_model_turbo_front_view.png |
| input | `LoadImage` #82 | image | 3d_hunyuan3d_multiview_to_model_turbo_back_view.png |
| input | `LoadImage` #85 | image | 3d_hunyuan3d_multiview_to_model_turbo_left_view.png |
| input | `LoadImage` #87 | image | 3d_hunyuan3d_multiview_to_model_turbo_right_view.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `hunyuan3d-dit-v2-mv-turbo_fp16.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/hunyuan3D_2.0_repackaged/resolve/main/split_files/hunyuan3d-dit-v2-mv-turbo_fp16.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPVisionEncode` | 4 | comfy-core |
| `LoadImage` | 4 | comfy-core |
| `MarkdownNote` | 2 |  |
| `EmptyLatentHunyuan3Dv2` | 1 | comfy-core |
| `FluxGuidance` | 1 | comfy-core |
| `Hunyuan3Dv2ConditioningMultiView` | 1 | comfy-core |
| `ImageOnlyCheckpointLoader` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `SaveGLB` | 1 | comfy-core |
| `VAEDecodeHunyuan3D` | 1 | comfy-core |
| `VoxelToMesh` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>CFG setting</summary>

Try adjusting the cfg settings to get the best results. It should be between 4 and 8. Thanks for the feedback from Manifold.

</details>

<details><summary>MarkdownNote</summary>

[Tutorial](https://docs.comfy.org/tutorials/3d/hunyuan3D-2)


## Model link

- [Hugging Face:Comfy-Org/hunyuan3D_2.0_repackaged](https://huggingface.co/Comfy-Org/hunyuan3D_2.0_repackaged)
- [ModelScope:Comfy-Org/hunyuan3D_2.0_repackaged](https://modelscope.cn/models/Comfy-Org/hunyuan3D_2.0_repackaged)

**checkpoints**

- [hunyuan3d-dit-v2-mv-turbo_fp16.safetensors](https://huggingface.co/Comfy-Org/hunyuan3D_2.0_repackaged/resolve/main/split_files/hunyuan3d-dit-v2-mv-turbo_fp16.safetensors) (4.59 GB)


Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 checkpoints/
│          └── hunyuan3d-dit-v2-mv-turbo_fp16.safetensors
```

</details>
