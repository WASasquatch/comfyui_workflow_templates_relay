# Wan2.1 Alpha T2V

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_wan2.1_alpha_t2v_14B)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2.1_alpha_t2v_14B-1.webp" width="360" alt="Wan2.1 Alpha T2V video_wan2.1_alpha_t2v_14B-1.webp">

> Generate text-to-video with alpha channel support for transparent backgrounds and semi-transparent objects.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2.1_alpha_t2v_14B.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan2.1_alpha_t2v_14B.json)

## Details

| | |
|---|---|
| Name | `video_wan2.1_alpha_t2v_14B` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.1, Wan |
| Tags | Text to Video, Video |
| Type | open source |
| Date | 2025-10-06 |
| Author | ComfyUI |
| Download size | 21.0 GB |
| Min ComfyUI version | 0.3.16 |
| Usage | 18 |
| Nodes | 19 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `wan2.1_t2v_14B_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_t2v_14B_fp8_scaled.safetensors) |
| `lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors) |
| `wan_alpha_2.1_rgba_lora.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/loras/wan_alpha_2.1_rgba_lora.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `wan_alpha_2.1_vae_alpha_channel.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_alpha_2.1_vae_alpha_channel.safetensors) |
| `wan_alpha_2.1_vae_rgb_channel.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_alpha_2.1_vae_rgb_channel.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `VAEDecode` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `EmptyHunyuanLatentVideo` | 1 | comfy-core |
| `ImageToMask` | 1 | comfy-core |
| `InvertMask` | 1 | comfy-core |
| `JoinImageWithAlpha` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `ModelSamplingSD3` | 1 | comfy-core |
| `SaveAnimatedWEBP` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>KSampler Setting</summary>

| Parameter | Default  | with 4steps lightning |
|-----------|--------------------------------|------------------|
| steps     | 20                             | 4              |
| cfg       | 6.0                            | 1.0              |

</details>

<details><summary>Note: Model links</summary>

**Diffusion Model**
- [wan2.1_t2v_14B_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_t2v_14B_fp8_scaled.safetensors) (13.31 GB)
- [wan2.1_t2v_14B_bf16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_t2v_14B_bf16.safetensors) (26.61 GB) if you need the original model weights, download this one.

**LoRA**
- [lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors) (601.5 MB)
- [wan_alpha_2.1_rgba_lora.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/loras/wan_alpha_2.1_rgba_lora.safetensors) (297.2 MB)

**VAE**
- [wan_alpha_2.1_vae_rgb_channel.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_alpha_2.1_vae_rgb_channel.safetensors) (242 MB)
-[wan_alpha_2.1_vae_alpha_channel.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_alpha_2.1_vae_alpha_channel.safetensors) (242 MB)

**Text Encoder**   
- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) (6.27 GB)

File save location

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   ├── wan2.1_t2v_14B_bf16.safetensors
│   │   └── wan2.1_t2v_14B_fp8_scaled.safetensors
│   ├───📂 loras/
│   │   ├───lightx2v_T2V_14B_cfg_step_distill_v2_lora_rank64_bf16.safetensors
│   │   └─── wan_alpha_2.1_rgba_lora.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   └───📂 vae/
│   │   ├── wan_alpha_2.1_vae_rgb_channel.safetensors
│       └── wan_alpha_2.1_vae_alpha_channel.safetensors
```
# Report issue

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

If you have any problems while using this workflow, please report template-related issues via this link: [report the template issue here](https://github.com/Comfy-Org/workflow_templates/issues).

</details>
