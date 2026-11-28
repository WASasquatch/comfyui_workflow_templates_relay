# Wan 2.2 5B Fun Control

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_wan2_2_5B_fun_control)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_5B_fun_control-1.webp" width="360" alt="Wan 2.2 5B Fun Control video_wan2_2_5B_fun_control-1.webp">

> Multi-condition video control with pose, depth, and edge guidance. Compact 5B size for experimental development.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_5B_fun_control.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan2_2_5B_fun_control.json)

## Details

| | |
|---|---|
| Name | `video_wan2_2_5B_fun_control` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.2, Wan |
| Tags | Text to Video, Video, ControlNet |
| Type | open source |
| Date | 2025-07-29 |
| Author | ComfyUI |
| Download size | 16.9 GB |
| Min ComfyUI version | 0.3.50 |
| Usage | 26 |
| Nodes | 18 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #66 | video | video_wan2_2_5B_fun_control_control_video.mp4 |
| input | `LoadImage` #70 | image | video_wan2_2_5B_fun_control_start_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `wan2.2_fun_control_5B_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_fun_control_5B_bf16.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `wan2.2_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan2.2_vae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `Canny` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `ModelSamplingSD3` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `Wan22FunControlToVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model Links</summary>

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)
- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)
- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

[Tutorial](https://docs.comfy.org/tutorials/video/wan/wan2_2
) 

**Diffusion Model**
- [wan2.2_fun_control_5B_bf16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_fun_control_5B_bf16.safetensors) (9.32 GB)

**VAE**
- [wan2.2_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan2.2_vae.safetensors) (1.31 GB)

**Text Encoder**   
- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) (6.27 GB)

File save location

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   └───wan2.2_fun_control_5B_bf16.safetensors)
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   └───📂 vae/
│       └── wan2.2_vae.safetensors
```

</details>

<details><summary>Note: About Wan2.2 fun control 5B</summary>

Since this model only has 5B parameters, the result most of the time will not be very good.

Wan2.2-Fun-5B-Control is a multi-language video generation model trained with 121 frames at 24 FPS, supporting various control conditions like Canny, Depth, Pose, and trajectory control for image-to-video tasks.

</details>
