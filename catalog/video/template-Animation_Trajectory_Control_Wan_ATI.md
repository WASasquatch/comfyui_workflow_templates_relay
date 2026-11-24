# Animation Trajectory Control

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template-Animation_Trajectory_Control_Wan_ATI)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template-Animation_Trajectory_Control_Wan_ATI-1.webp" width="360" alt="Animation Trajectory Control template-Animation_Trajectory_Control_Wan_ATI-1.webp">

> Draw the movement trajectory you want for the input image.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template-Animation_Trajectory_Control_Wan_ATI.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template-Animation_Trajectory_Control_Wan_ATI.json)

## Details

| | |
|---|---|
| Name | `template-Animation_Trajectory_Control_Wan_ATI` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.1 |
| Tags | Image to Video |
| Type | open source |
| Date | 2025-12-11 |
| Author | ComfyUI |
| Download size | 29.4 GB |
| Min ComfyUI version | 0.3.42 |
| Usage | 15 |
| Nodes | 19 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #58 | image | hk_scene.png |
| output | `SaveVideo` #96 | video | template-Animation_Trajectory_Control_Wan_ATI.mp4 |

## Custom nodes required

- [ComfyUI-WanVideoWrapper](https://registry.comfy.org/nodes/ComfyUI-WanVideoWrapper)
- [comfyui_fill-nodes](https://registry.comfy.org/nodes/comfyui_fill-nodes)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/CLIP-ViT-H-14-laion2B-s32B-b79K_repackaged/resolve/main/split_files/clip_vision/CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors) |
| `Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors) |
| `Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors) |
| `umt5-xxl-enc-bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/umt5-xxl-enc-bf16.safetensors) |
| `Wan2_1_VAE_bf16.safetensors` | `vae` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2_1_VAE_bf16.safetensors) |

## Subgraphs

- **Wan ATI** (12 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveInt` | 2 |  |
| `CLIPVisionLoader` | 1 | comfy-core |
| `CreateVideo` | 1 |  |
| `FL_PathAnimator` | 1 | comfyui_fill-nodes |
| `ImageScale` | 1 |  |
| `LoadImage` | 1 | comfy-core |
| `LoadWanVideoT5TextEncoder` | 1 | ComfyUI-WanVideoWrapper |
| `SaveVideo` | 1 |  |
| `WanVideoATITracks` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoATITracksVisualize` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoClipVisionEncode` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoDecode` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoImageToVideoEncode` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoLoraSelect` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoModelLoader` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoSampler` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoTextEncode` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoVAELoader` | 1 | ComfyUI-WanVideoWrapper |
