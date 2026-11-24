# HiDream E1.1 Image Editing

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/hidream_e1_1-1.webp" width="360" alt="HiDream E1.1 Image Editing hidream_e1_1-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/hidream_e1_1-2.webp" width="360" alt="HiDream E1.1 Image Editing hidream_e1_1-2.webp">

> Edit images with HiDream E1.1—superior image quality and editing accuracy compared to HiDream-E1-Full.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/hidream_e1_1.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/hidream_e1_1.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/hidream/hidream-e1)

## Details

| | |
|---|---|
| Name | `hidream_e1_1` |
| Category | Foundation › Image |
| Media type | image |
| Models | HiDream |
| Tags | Image, Image Edit |
| Type | open source |
| Date | 2025-07-21 |
| Author | ComfyUI |
| Download size | 47.0 GB |
| Min ComfyUI version | 0.3.45 |
| Usage | 26 |
| Nodes | 20 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #13 | image | hidream_e1_1_input_image.jpg |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `hidream_e1_1_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_e1_1_bf16.safetensors) |
| `clip_g_hidream.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/text_encoders/clip_g_hidream.safetensors) |
| `clip_l_hidream.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/text_encoders/clip_l_hidream.safetensors) |
| `llama_3.1_8b_instruct_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/text_encoders/llama_3.1_8b_instruct_fp8_scaled.safetensors) |
| `t5xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/text_encoders/t5xxl_fp8_e4m3fn_scaled.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/vae/ae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `PrimitiveNode` | 2 |  |
| `BasicScheduler` | 1 | comfy-core |
| `CFGNorm` | 1 | comfy-core |
| `DualCFGGuider` | 1 | comfy-core |
| `ImageScaleToTotalPixels` | 1 | comfy-core |
| `InstructPixToPixConditioning` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `QuadrupleCLIPLoader` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `Reroute` | 1 |  |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Model Links

- [Hugging Face:Comfy-Org/HiDream-I1_ComfyUI](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI)
- [ModelScope:Comfy-Org/HiDream-I1_ComfyUI](https://modelscope.cn/models/Comfy-Org/HiDream-I1_ComfyUI)

[Tutorial](https://docs.comfy.org/tutorials/image/hidream/hidream-e1)

**Diffusion Model**
- [hidream_e1_1_bf16.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/diffusion_models/hidream_e1_1_bf16.safetensors) (31.86 GB)

**Text Encoder**：

- [clip_l_hidream.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/clip_l_hidream.safetensors)
- [clip_g_hidream.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/clip_g_hidream.safetensors)
- [t5xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/t5xxl_fp8_e4m3fn_scaled.safetensors) 
- [llama_3.1_8b_instruct_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/text_encoders/llama_3.1_8b_instruct_fp8_scaled.safetensors)

**VAE**
-  [ae.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/blob/main/split_files/vae/ae.safetensors)

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   ├─── clip_l_hidream.safetensors
│   │   ├─── clip_g_hidream.safetensors
│   │   ├─── t5xxl_fp8_e4m3fn_scaled.safetensors
│   │   └─── llama_3.1_8b_instruct_fp8_scaled.safetensors
│   └── 📂 vae/
│   │   └── ae.safetensors
│   └── 📂 diffusion_models/
│       └── hidream_e1_1_bf16.safetensors   
```

</details>
