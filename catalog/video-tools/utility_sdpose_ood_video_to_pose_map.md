# Pose Map: SDPose-OOD

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_sdpose_ood_video_to_pose_map)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_sdpose_ood_video_to_pose_map-1.webp" width="360" alt="Pose Map: SDPose-OOD utility_sdpose_ood_video_to_pose_map-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_sdpose_ood_video_to_pose_map-2.webp" width="360" alt="Pose Map: SDPose-OOD utility_sdpose_ood_video_to_pose_map-2.webp">

> Upload a video to extract pose keypoints and generate a pose map. The workflow supports multiple person detection and uses an enhanced SDPose model for accurate whole-body feature extraction.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_sdpose_ood_video_to_pose_map.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_sdpose_ood_video_to_pose_map.json)

## Details

| | |
|---|---|
| Name | `utility_sdpose_ood_video_to_pose_map` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | SDPose-OOD |
| Tags | Pose Map |
| Type | open source |
| Date | 2026-03-02 |
| Author | ComfyUI |
| Download size | 1.8 GB |
| Min ComfyUI version | 0.16.0 |
| Usage | 22 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #679 | video | man_in_the_rain.mp4 |
| output | `SaveVideo` #680 | video | utility_sdpose_ood_video_to_pose_map.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sdpose_wholebody_fp16.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/SDPose/resolve/main/checkpoints/sdpose_wholebody_fp16.safetensors) |

## Subgraphs

- **Video to Pose Map (SDPose-OOD)** (5 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ResizeImageMaskNode` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `SDPoseDrawKeypoints` | 1 | comfy-core |
| `SDPoseKeypointExtractor` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Model Links

- [Hugging Face:Comfy-Org/SDPose](https://huggingface.co/Comfy-Org/SDPose)
- [ModelScope:Comfy-Org/SDPose](https://modelscope.cn/models/Comfy-Org/SDPose)

**checkpoints**

- [sdpose_wholebody_fp16.safetensors](https://huggingface.co/Comfy-Org/SDPose/resolve/main/checkpoints/sdpose_wholebody_fp16.safetensors) (1.79 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 checkpoints/
│       └── sdpose_wholebody_fp16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
