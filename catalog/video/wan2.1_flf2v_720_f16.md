# Wan 2.1 FLF2V 720p F16

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/wan2.1_flf2v_720_f16-1.webp" width="360" alt="Wan 2.1 FLF2V 720p F16 wan2.1_flf2v_720_f16-1.webp">

> Generate videos by controlling first and last frames using Wan 2.1 FLF2V.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/wan2.1_flf2v_720_f16.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/wan2.1_flf2v_720_f16.json)
- [Tutorial](https://docs.comfy.org/tutorials/video/wan/wan-flf)

## Details

| | |
|---|---|
| Name | `wan2.1_flf2v_720_f16` |
| Category | Foundation › Video |
| Media type | image |
| Models | Wan2.1, Wan |
| Tags | FLF2V, Video |
| Type | open source |
| Date | 2025-04-15 |
| Author | ComfyUI |
| Download size | 38.2 GB |
| Min ComfyUI version | 0.3.31 |
| Usage | 9 |
| Nodes | 17 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #52 | image | wan2.1_flf2v_720_f16_start_image.png |
| input | `LoadImage` #72 | image | wan2.1_flf2v_720_f16_end_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `clip_vision_h.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors?download=true) |
| `wan2.1_flf2v_720p_14B_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_flf2v_720p_14B_fp16.safetensors?download=true) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors?download=true) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `CLIPVisionEncode` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingSD3` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `WanFirstLastFrameToVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

[Tutorial here](https://docs.comfy.org/tutorials/video/wan/wan-flf) 

You can find the following files in the [Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/tree/main/split_files).

Download the following files, and put them in right directory

**Diffusion models**

- [wan2.1_flf2v_720p_14B_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_flf2v_720p_14B_fp16.safetensors?download=true) (30.54 GB)

**Text encoders**
- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true) (6.27 GB)

**VAE**
- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors?download=true) (242.1 MB)

**CLIP Vision**
- [clip_vision_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors?download=true) (1.18 GB)

File Storage Location

```
ComfyUI/
├── models/
│   ├── diffusion_models/
│   │   └─── wan2.1_flf2v_720p_14B_fp16.safetensors  
│   ├── text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors  
│   ├── vae/
│   │   └──  wan_2.1_vae.safetensors
│   └── clip_vision/
│       └──  clip_vision_h.safetensors   
```

</details>
