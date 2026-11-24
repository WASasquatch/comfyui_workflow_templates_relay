# Video Restyle

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_shane_video_restyle)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_shane_video_restyle-1.webp" width="360" alt="Video Restyle templates_shane_video_restyle-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_shane_video_restyle-2.webp" width="360" alt="Video Restyle templates_shane_video_restyle-2.webp">

> Use a base video + a stylized reference image to create the stylized video using WAN 2.1 VACE

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_shane_video_restyle.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_shane_video_restyle.json)

## Details

| | |
|---|---|
| Name | `templates_shane_video_restyle` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.1 VACE |
| Tags | Video, Video to Video |
| Type | open source |
| Date | 2026-03-03 |
| Author | shane |
| Download size | 20.0 GB |
| Min ComfyUI version | 0.3.30 |
| Usage | 16 |
| Nodes | 25 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #134 | image | shane_video_restyle_ref_frame.png |
| input | `VHS_LoadVideo` #154 | video | flower.mp4 |

## Custom nodes required

- [comfyui-depthanythingv2](https://registry.comfy.org/nodes/comfyui-depthanythingv2)
- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [ComfyUI-WanVideoWrapper](https://registry.comfy.org/nodes/ComfyUI-WanVideoWrapper)
- [comfyui_controlnet_aux](https://registry.comfy.org/nodes/comfyui_controlnet_aux)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `wan2.1_vace_14B_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_vace_14B_fp16.safetensors) |
| `Wan2_1-VACE_module_14B_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2_1-VACE_module_14B_bf16.safetensors?download=true) |
| `Wan21_CausVid_14B_T2V_lora_rank32.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan21_CausVid_14B_T2V_lora_rank32.safetensors) |
| `umt5-xxl-enc-bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/umt5-xxl-enc-bf16.safetensors?download=true) |
| `Wan2_1_VAE_bf16.safetensors` | `vae` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2_1_VAE_bf16.safetensors?download=true) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `INTConstant` | 3 | comfyui-kjnodes |
| `ImageResizeKJv2` | 2 | comfyui-kjnodes |
| `CannyEdgePreprocessor` | 1 | comfyui_controlnet_aux |
| `DepthAnything_V2` | 1 | comfyui-depthanythingv2 |
| `DownloadAndLoadDepthAnythingV2Model` | 1 | comfyui-depthanythingv2 |
| `LoadImage` | 1 | comfy-core |
| `LoadWanVideoT5TextEncoder` | 1 | ComfyUI-WanVideoWrapper |
| `MarkdownNote` | 1 |  |
| `VHS_LoadVideo` | 1 | comfyui-videohelpersuite |
| `VHS_VideoCombine` | 1 | comfyui-videohelpersuite |
| `WanVideoDecode` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoEncode` | 1 |  |
| `WanVideoExperimentalArgs` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoLoraSelect` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoModelLoader` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoSampler` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoSLG` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoTextEncode` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoTorchCompileSettings` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoVACEEncode` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoVACEModelSelect` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoVAELoader` | 1 | ComfyUI-WanVideoWrapper |

## Notes embedded in the workflow

<details><summary>Preprocessor Settings</summary>

Experiment between Depth vs Canny. Plug either into the reroute node here

</details>
