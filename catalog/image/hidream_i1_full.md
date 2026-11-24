# HiDream I1 Full

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/hidream_i1_full-1.webp" width="360" alt="HiDream I1 Full hidream_i1_full-1.webp">

> Generate images with HiDream I1 Full - Complete version with 50 inference steps for highest quality output.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/hidream_i1_full.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/hidream_i1_full.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/hidream/hidream-i1)

## Details

| | |
|---|---|
| Name | `hidream_i1_full` |
| Category | Foundation › Image |
| Media type | image |
| Models | HiDream |
| Tags | Text to Image, Image |
| Type | open source |
| Date | 2025-04-17 |
| Author | ComfyUI |
| Download size | 22.6 GB |
| Min ComfyUI version | 0.3.29 |
| Usage | 13 |
| Nodes | 12 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #90 | image | hidream_i1_full.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `hidream_i1_full_fp8.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_i1_full_fp8.safetensors?download=true) |
| `clip_g_hidream.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/text_encoders/clip_g_hidream.safetensors) |
| `clip_l_hidream.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/text_encoders/clip_l_hidream.safetensors) |
| `llama_3.1_8b_instruct_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/text_encoders/llama_3.1_8b_instruct_fp8_scaled.safetensors) |
| `t5xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/text_encoders/t5xxl_fp8_e4m3fn_scaled.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/vae/ae.safetensors?download=true) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `ModelSamplingSD3` | 1 | comfy-core |
| `QuadrupleCLIPLoader` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>KSampler Settings</summary>

## Official sampling settings

Provided for reference, my workflows may have slightly different settings.

### HiDream Full

* hidream_i1_full_fp16.safetensors
* shift: 3.0
* steps: 50
* sampler: uni_pc
* scheduler: simple
* cfg: 5.0

### HiDream Dev

* hidream_i1_dev_bf16.safetensors
* shift: 6.0
* steps: 28
* sampler: lcm
* scheduler: normal
* cfg: 1.0 (no negative prompt)

### HiDream Fast

* hidream_i1_fast_bf16.safetensors
* shift: 3.0
* steps: 16
* sampler: lcm
* scheduler: normal
* cfg: 1.0 (no negative prompt)

</details>

<details><summary>Model links</summary>

## Model Links

- [Hugging Face:Comfy-Org/HiDream-I1_ComfyUI](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI)

### Alternative Repos

- [ModelScope:Comfy-Org/HiDream-I1_ComfyUI](https://modelscope.cn/models/Comfy-Org/HiDream-I1_ComfyUI)

[Tutorial](https://docs.comfy.org/tutorials/image/hidream/hidream-i1) 

**diffusion models**
- [hidream_i1_full_fp8.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_i1_full_fp8.safetensors) (15.93 GB)

**text_encoders**：

- [clip_l_hidream.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/text_encoders/clip_l_hidream.safetensors) (236.1 MB)
- [clip_g_hidream.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/text_encoders/clip_g_hidream.safetensors) (1.29 GB)
- [t5xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/text_encoders/t5xxl_fp8_e4m3fn_scaled.safetensors) (4.8 GB) 
- [llama_3.1_8b_instruct_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/text_encoders/llama_3.1_8b_instruct_fp8_scaled.safetensors) (8.46 GB)

**VAE**
-  [ae.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/vae/ae.safetensors) (319.8 MB) 

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── hidream_i1_full_fp8.safetensors
│   ├── 📂 text_encoders/
│   │   ├─── clip_l_hidream.safetensors
│   │   ├─── clip_g_hidream.safetensors
│   │   ├─── t5xxl_fp8_e4m3fn_scaled.safetensors
│   │   └───llama_3.1_8b_instruct_fp8_scaled.safetensors
│   ├── 📂 vae/
│   │   └── ae.safetensors
           
```

</details>
