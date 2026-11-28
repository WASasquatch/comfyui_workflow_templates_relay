# Qwen-Image: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_qwen_image)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image-1.webp" width="360" alt="Qwen-Image: Text to Image image_qwen_image-1.webp">

> Generate images with exceptional multilingual text rendering and editing capabilities using Qwen-Image's 20B MMDiT model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_qwen_image.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image)

## Details

| | |
|---|---|
| Name | `image_qwen_image` |
| Category | Foundation › Image |
| Output | image |
| Models | Qwen-Image |
| Tags | Image, Text to Image |
| Type | open source |
| Date | 2025-08-05 |
| Author | ComfyUI |
| Download size | 29.6 GB |
| Min ComfyUI version | 0.4.0 |
| Usage | 64 |
| Nodes | 23 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #60 | image | image_qwen_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) |
| `Qwen-Image-Lightning-8steps-V1.0.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-8steps-V1.0.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Text to Image (Qwen-Image)** (19 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 4 |  |
| `ComfySwitchNode` | 3 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `PrimitiveFloat` | 2 |  |
| `PrimitiveInt` | 2 |  |
| `CLIPLoader` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>VRAM Usage</summary>

## GPU:RTX4090D 24GB

| Configuration            | VRAM Usage | 1st Generation | 2nd Generation |
|---------------------|---------------|---------------|-----------------|
| Fp8_e4m3fn             | 86%                | ≈ 94s               | ≈ 71s                   |
| With 8steps LoRA    | 86%                | ≈ 55s               | ≈ 34s                  |
| Distill fp8_e4m3fn   | 86%                | ≈ 69s               | ≈ 36s                  |

</details>

<details><summary>Model links</summary>

[Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image) 

## Model Links

- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)

### Alternative Repos

- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)

You can find all the models on [Huggingface](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/tree/main) or [Modelscope](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI/files)

**Diffusion model**

- [qwen_image_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) (19.03 GB)

Qwen_image_distill

- [qwen_image_distill_full_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/non_official/diffusion_models/qwen_image_distill_full_fp8_e4m3fn.safetensors) (19.03 GB)
- [qwen_image_distill_full_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/non_official/diffusion_models/qwen_image_distill_full_bf16.safetensors) (38.05 GB)

**LoRA**

- [Qwen-Image-Lightning-8steps-V1.0.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-8steps-V1.0.safetensors) (1.58 GB)

**Text encoder**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**VAE**

- [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   ├── qwen_image_fp8_e4m3fn.safetensors
│   │   └── qwen_image_distill_full_fp8_e4m3fn.safetensors
│   ├── 📂 loras/
│   │   └── Qwen-Image-Lightning-8steps-V1.0.safetensors
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   └── 📂 text_encoders/
│       └── qwen_2.5_vl_7b_fp8_scaled.safetensors
```

</details>

<details><summary>Aspect Ratio Resolutions</summary>

| Aspect Ratio | Resolution (Width, Height) |
|--------------|-----------------------------|
| 1:1          | (1328, 1328)                |
| 16:9         | (1664, 928)                 |
| 9:16         | (928, 1664)                 |
| 4:3          | (1472, 1140)                |
| 3:4          | (1140, 1472)                |
| 3:2          | (1584, 1056)                |
| 2:3          | (1056, 1584)                |

</details>

<details><summary>MarkdownNote</summary>

Try 50 steps, if you want original the [qwen image](https://huggingface.co/Qwen/Qwen-Image)'s setting, but it will takes longer

</details>
