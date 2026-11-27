# SAM 3D Body: 3D Human Mesh Extraction From Video

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_sam3d_body)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_sam3d_body-1.webp" width="360" alt="SAM 3D Body: 3D Human Mesh Extraction From Video utility_sam3d_body-1.webp">

> Extract a full-body 3D human mesh from a single video frame using SAM 3D Body, guided by a text prompt to refine pose and shape estimation. The workflow loads one video and one text prompt, then outputs a reconstructed video showing the recovered human rig. Ideal for motion capture prototyping, biomechanics analysis, and character animation previsualization.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_sam3d_body.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_sam3d_body.json)

## Details

| | |
|---|---|
| Name | `utility_sam3d_body` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | SAM 3D Body |
| Tags | 3D |
| Type | open source |
| Date | 2026-08-25 |
| Author | ComfyUI |
| Download size | 5.1 GB |
| Min ComfyUI version | 0.34.0 |
| Usage | 168 |
| Nodes | 25 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #85 | video | woman_holding_water_glass.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sam3.1_multiplex_fp16.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors) |
| `sam_3d_body_dinov3_bf16.safetensors` | `detection` | [link](https://huggingface.co/Comfy-Org/sam-3d-body/resolve/main/detection/sam_3d_body_dinov3_bf16.safetensors) |
| `rt_detr_v4-x-hgnet_fp32.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/SDPose/resolve/main/diffusion_models/rt_detr_v4-x-hgnet_fp32.safetensors) |
| `moge_2_vitl_normal_fp16.safetensors` | `geometry_estimation` | [link](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_2_vitl_normal_fp16.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Note` | 4 |  |
| `BuildPoseFile` | 1 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `LoadMoGeModel` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `MoGeGeometryToFOV` | 1 | comfy-core |
| `MoGeInference` | 1 | comfy-core |
| `RTDETR_detect` | 1 | comfy-core |
| `SAM3_VideoTrack` | 1 | comfy-core |
| `SAM3DBody_FaceExpression` | 1 | comfy-core |
| `SAM3DBody_Loader` | 1 | comfy-core |
| `SAM3DBody_Predict` | 1 | comfy-core |
| `SAM3DBody_Render` | 1 | comfy-core |
| `SAM3DBody_Smooth` | 1 | comfy-core |
| `Save3DAdvanced` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `Video Slice` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
MoGe can be optionally used to detect FoV for more accurate alignment with source video.
```

</details>

<details><summary>Note</summary>

```text
For multiple people in same clip SAM3 is practically required, otherwise optional but can improve detection
```

</details>

<details><summary>Note</summary>

```text
While bounding boxes are technically optional, depending on clip will improve detection accuracy drastically.
```

</details>

<details><summary>Note</summary>

```text
Sam3d-body does not detect face expressions, this node adds them through MediaPipe face detection.
```

</details>

<details><summary>Note: Model Link and Input Asset</summary>

**Input Asset**

- [woman_holding_water_glass.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/woman_holding_water_glass.mp4) — required workflow input (`input/woman_holding_water_glass.mp4`)


## Model Links

- [Hugging Face:Comfy-Org/sam3.1](https://huggingface.co/Comfy-Org/sam3.1)
- [ModelScope:Comfy-Org/sam3.1](https://modelscope.cn/models/Comfy-Org/sam3.1)
- [Hugging Face:Comfy-Org/sam-3d-body](https://huggingface.co/Comfy-Org/sam-3d-body)
- [ModelScope:Comfy-Org/sam-3d-body](https://modelscope.cn/models/Comfy-Org/sam-3d-body)
- [Hugging Face:Comfy-Org/MoGe](https://huggingface.co/Comfy-Org/MoGe)
- [ModelScope:Comfy-Org/MoGe](https://modelscope.cn/models/Comfy-Org/MoGe)
- [Hugging Face:Comfy-Org/SDPose](https://huggingface.co/Comfy-Org/SDPose)
- [ModelScope:Comfy-Org/SDPose](https://modelscope.cn/models/Comfy-Org/SDPose)

**checkpoints**

- [sam3.1_multiplex_fp16.safetensors](https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors) (1.63 GB)

**detection**

- [sam_3d_body_dinov3_bf16.safetensors](https://huggingface.co/Comfy-Org/sam-3d-body/resolve/main/detection/sam_3d_body_dinov3_bf16.safetensors) (2.64 GB)

**geometry_estimation**

- [moge_2_vitl_normal_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_2_vitl_normal_fp16.safetensors) (631.2 MB)

**diffusion_models**

- [rt_detr_v4-x-hgnet_fp32.safetensors](https://huggingface.co/Comfy-Org/SDPose/resolve/main/diffusion_models/rt_detr_v4-x-hgnet_fp32.safetensors) (236.3 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │   └── sam3.1_multiplex_fp16.safetensors
│   ├── 📂 detection/
│   │   └── sam_3d_body_dinov3_bf16.safetensors
│   ├── 📂 geometry_estimation/
│   │   └── moge_2_vitl_normal_fp16.safetensors
│   └── 📂 diffusion_models/
│       └── rt_detr_v4-x-hgnet_fp32.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
