# Wan 2.2 14B Fun Control

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_fun_control-1.webp" width="360" alt="Wan 2.2 14B Fun Control video_wan2_2_14B_fun_control-1.webp">

> Generate videos guided by pose, depth, and edge controls using Wan 2.2 Fun Control.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_fun_control.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan2_2_14B_fun_control.json)
- [Tutorial](https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-control)

## Details

| | |
|---|---|
| Name | `video_wan2_2_14B_fun_control` |
| Category | Foundation › Video |
| Media type | image |
| Models | Wan2.2, Wan |
| Tags | Video to Video, Video, ControlNet |
| Type | open source |
| Date | 2025-08-12 |
| Author | ComfyUI |
| Download size | 35.4 GB |
| Min ComfyUI version | 0.3.50 |
| Usage | 82 |
| Nodes | 44 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #145 | image | video_wan2_2_14B_fun_control_start_image.jpg |
| input | `LoadVideo` #158 | video | video_wan2_2_14B_fun_control_start_image_control_video.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors) |
| `wan2.2_fun_control_low_noise_14B_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_fun_control_low_noise_14B_fp8_scaled.safetensors) |
| `wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors) |
| `wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 4 | comfy-core |
| `KSamplerAdvanced` | 4 | comfy-core |
| `ModelSamplingSD3` | 4 | comfy-core |
| `UNETLoader` | 4 | comfy-core |
| `MarkdownNote` | 3 |  |
| `Canny` | 2 | comfy-core |
| `CLIPLoader` | 2 | comfy-core |
| `CreateVideo` | 2 | comfy-core |
| `GetVideoComponents` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `LoadVideo` | 2 | comfy-core |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `PreviewImage` | 2 | comfy-core |
| `SaveVideo` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `Wan22FunControlToVideo` | 2 | comfy-core |
| `Note` | 1 |  |

## Notes embedded in the workflow

<details><summary>About Control Video</summary>

You may need the following custom nodes to preprocess the  control video:
1.  [comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux)
2. [ComfyUI-DepthAnythingV2](https://github.com/kijai/ComfyUI-DepthAnythingV2)

You can find the control video we use [here](https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-control).

This model supports multiple control conditions such as Canny, Depth, Pose, and trajectory control.

</details>

<details><summary>Note</summary>

```text
Using the Wan2.2 Lighting LoRA will result in the loss of video dynamics, but it will reduce the generation time. This template provides two workflows, and you can enable one as needed.
```

</details>

<details><summary>MarkdownNote</summary>

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)
- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)
- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

[Tutorial](https://docs.comfy.org/tutorials/video/wan/wan2-2-fun-control
) 

**Diffusion Model**
- [wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors) (13.31 GB)
- [wan2.2_fun_control_low_noise_14B_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_fun_control_low_noise_14B_fp8_scaled.safetensors) (13.31 GB)

**LoRA**
- [wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors) (1.14 GB)
- [wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors) (1.14 GB)

**VAE**
- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) (242.1 MB)

**Text Encoder**   
- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) (6.27 GB)

File save location

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   ├─── wan2.2_fun_control_low_noise_14B_fp8_scaled.safetensors
│   │   └─── wan2.2_fun_control_high_noise_14B_fp8_scaled.safetensors
│   ├───📂 loras/
│   │   ├─── wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors
│   │   └─── wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   └───📂 vae/
│       └── wan_2.1_vae.safetensors
```

</details>

<details><summary>Note: About Wan2.2 Fun Control</summary>

Wan2.2-Fun-Control is a 14B-parameter video generation model launched by Alibaba PAI, supporting multiple control conditions such as Canny, Depth, Pose and trajectory control. 

It enables multi-resolution (512/768/1024) video prediction, trained with 81 frames and 16 FPS, and supports multilingual generation.

</details>
