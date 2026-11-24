# Pose Detection: SDPose Multi-Person

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_sdpose_multi_person_video-1.webp" width="360" alt="Pose Detection: SDPose Multi-Person utility_sdpose_multi_person_video-1.webp">

> Upload a video to detect human poses. Supports detection for both single individuals and multiple people within the same scene

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_sdpose_multi_person_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_sdpose_multi_person_video.json)

## Details

| | |
|---|---|
| Name | `utility_sdpose_multi_person_video` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | SDPose-OOD |
| Tags | Pose Map |
| Type | open source |
| Date | 2026-03-31 |
| Author | ComfyUI |
| Download size | 1.9 GB |
| Min ComfyUI version | 0.19.0 |
| Usage | 11 |
| Nodes | 18 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #694 | video | man_playing_violin.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sdpose_wholebody_fp16.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/SDPose/resolve/main/checkpoints/sdpose_wholebody_fp16.safetensors) |
| `rt_detr_v4-x-hgnet_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/SDPose/resolve/main/diffusion_models/rt_detr_v4-x-hgnet_fp16.safetensors) |

## Subgraphs

- **Video to Pose Map (SDPose Multi-Person)** (7 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GetVideoComponents` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `ResizeImageMaskNode` | 2 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `DrawBBoxes` | 1 | comfy-core |
| `ImageBlend` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `PrimitiveInt` | 1 | comfy-core |
| `RTDETR_detect` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `SDPoseDrawKeypoints` | 1 | comfy-core |
| `SDPoseKeypointExtractor` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Related PR: [#12748](https://github.com/Comfy-Org/ComfyUI/pull/12748)

## Model Links

- [Hugging Face:Comfy-Org/SDPose](https://huggingface.co/Comfy-Org/SDPose)

### Alternative Repos

- [ModelScope:Comfy-Org/SDPose](https://modelscope.cn/models/Comfy-Org/SDPose)

**checkpoints**

- [sdpose_wholebody_fp16.safetensors](https://huggingface.co/Comfy-Org/SDPose/resolve/main/checkpoints/sdpose_wholebody_fp16.safetensors) (1.79 GB)

**diffusion_models**

- [rt_detr_v4-x-hgnet_fp16.safetensors](https://huggingface.co/Comfy-Org/SDPose/resolve/main/diffusion_models/rt_detr_v4-x-hgnet_fp16.safetensors) (118.2 MB)
- [rt_detr_v4-x-hgnet_fp32.safetensors](https://huggingface.co/Comfy-Org/SDPose/resolve/main/diffusion_models/rt_detr_v4-x-hgnet_fp32.safetensors) (236.3 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │   └── sdpose_wholebody_fp16.safetensors
│   └── 📂 diffusion_models/
│       ├── rt_detr_v4-x-hgnet_fp32.safetensors
│       └── rt_detr_v4-x-hgnet_fp16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>MarkdownNote</summary>

Upload an image with multiple people, then change the `max_detections` to see how it works.

</details>
