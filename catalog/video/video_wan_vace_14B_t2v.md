# Wan2.1 VACE Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_vace_14B_t2v-1.webp" width="360" alt="Wan2.1 VACE Text to Video video_wan_vace_14B_t2v-1.webp">

> Transform text descriptions into high-quality videos. Supports both 480p and 720p with VACE-14B model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_vace_14B_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan_vace_14B_t2v.json)
- [Tutorial](https://docs.comfy.org/tutorials/video/wan/vace)

## Details

| | |
|---|---|
| Name | `video_wan_vace_14B_t2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | Wan2.1, Wan |
| Tags | Text to Video, Video |
| Type | open source |
| Date | 2025-05-21 |
| Author | ComfyUI |
| Download size | 53.8 GB |
| Min ComfyUI version | 0.3.31 |
| Usage | 10 |
| Nodes | 22 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `wan2.1_vace_1.3B_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_vace_1.3B_fp16.safetensors) |
| `wan2.1_vace_14B_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_vace_14B_fp16.safetensors) |
| `Wan21_CausVid_14B_T2V_lora_rank32.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan21_CausVid_14B_T2V_lora_rank32.safetensors) |
| `Wan21_CausVid_bidirect2_T2V_1_3B_lora_rank32.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan21_CausVid_bidirect2_T2V_1_3B_lora_rank32.safetensors) |
| `umt5_xxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp16.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 5 |  |
| `CLIPLoader` | 2 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `LoraLoader` | 2 | comfy-core |
| `UNETLoader` | 2 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `ModelSamplingSD3` | 1 | comfy-core |
| `SaveAnimatedWEBP` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `TrimVideoLatent` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `WanVaceToVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>About Video Size</summary>

| Model                                                         | 480P | 720P |
| ------------------------------------------------------------ | ---- | ---- |
| [VACE-1.3B](https://huggingface.co/Wan-AI/Wan2.1-VACE-1.3B) | ✅   | ❌   |
| [VACE-14B](https://huggingface.co/Wan-AI/Wan2.1-VACE-14B)   | ✅   | ✅   |

</details>

<details><summary>KSampler Setting</summary>

## Default

- steps:20
- cfg:6.0

## For CausVid LoRA

- steps: 2-4
- cfg: 1.0

</details>

<details><summary>About CausVid LoRA</summary>

We have added CausVid LoRA by default to achieve acceleration. However, in some cases, the video may shake and become blurry. You might need to test different LoRA intensities to get the best results, which should be between 0.3 and 0.7. If you don't need it, you can use the bypass mode to disable it, and then restore the settings of `KSampler` to the default ones.

</details>

<details><summary>Note</summary>

The generation quality of the 14B model is better, but it takes longer to generate. If you have already downloaded the model, you can choose to directly use the nodes above, or just modify the model loaded by the loader node.

The corresponding LoRA should match the Diffusion Model. For example, the LoRA corresponding to the 14B diffusion model is the 14B LoRA.

</details>

<details><summary>MarkdownNote</summary>

[Tutorial](https://docs.comfy.org/tutorials/video/wan/vace) | [教程](https://docs.comfy.org/zh-CN/tutorials/video/wan/vace)

##  14B Support 480P 720P

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

**Diffusion Model**
- [wan2.1_vace_14B_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_vace_14B_fp16.safetensors) (32.29 GB)

**LoRA**
- [Wan21_CausVid_14B_T2V_lora_rank32.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_14B_T2V_lora_rank32.safetensors)

It takes about 40 minutes to complete at 81 frames 720P resolution with the RTX 4090 .  
After using Wan21_CausVid_14B_T2V_lora_rank32.safetensors, it only takes about 4 minutes.

## 1.3B Support 480P only

**Diffusion Model**
- [wan2.1_vace_1.3B_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_vace_1.3B_fp16.safetensors) (4.01 GB)

**LoRA**
- [Wan21_CausVid_bidirect2_T2V_1_3B_lora_rank32.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan21_CausVid_bidirect2_T2V_1_3B_lora_rank32.safetensors)
 
## Other Models

* You may already have these models if you use Wan workflow before.

**VAE**
- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors?download=true) (242.1 MB)

**Text encoders**   Chose one of following model
- [umt5_xxl_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp16.safetensors?download=true) (10.59 GB)
- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true) (6.27 GB)

> You can choose between fp16 of fp8; I used fp16 to match what kijai's wrapper is compatible with.

File save location

```
ComfyUI/
├── models/
│   ├── diffusion_models/
│   │   ├-── wan2.1_vace_14B_fp16.safetensors
│   │   └─── wan2.1_vace_1.3B_fp16.safetensors 
│   ├── text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors # or fp16
│   ├── loras/
│   │   ├── Wan21_CausVid_14B_T2V_lora_rank32.safetensors
│   │   └── Wan21_CausVid_bidirect2_T2V_1_3B_lora_rank32.safetensors
│   └── vae/
│       └──  wan_2.1_vae.safetensors
```

</details>
