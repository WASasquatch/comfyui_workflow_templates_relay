# Flux.1 Dev: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_dev_full_text_to_image-1.webp" width="360" alt="Flux.1 Dev: Text to Image flux_dev_full_text_to_image-1.webp">

> Generate high-quality images with Flux Dev full version. Requires larger VRAM and multiple model files, but provides the best prompt following capability and image quality.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_dev_full_text_to_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/flux_dev_full_text_to_image.json)
- [Tutorial](https://docs.comfy.org/tutorials/flux/flux-1-text-to-image)

## Details

| | |
|---|---|
| Name | `flux_dev_full_text_to_image` |
| Category | Foundation › Image |
| Media type | image |
| Models | FLUX, FLUX.1 |
| Tags | Image, Text to Image |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 31.8 GB |
| Min ComfyUI version | 0.3.42 |
| Usage | 229 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #9 | image | flux_dev_full_text_to_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux1-dev.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev.safetensors) |
| `clip_l.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors) |
| `t5xxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Text to Image (Flux.1 Dev)** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `DualCLIPLoader` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Model Links

- [Hugging Face:Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev)
- [Hugging Face:Comfy-Org/Lumina_Image_2.0_Repackaged](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/flux1-dev](https://modelscope.cn/models/Comfy-Org/flux1-dev)
- [ModelScope:Comfy-Org/Lumina_Image_2.0_Repackaged](https://modelscope.cn/models/Comfy-Org/Lumina_Image_2.0_Repackaged)

**Diffusion Model**

- [flux1-dev.safetensors](https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev.safetensors) (22.17 GB)

**Text Encoder**

- [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors)

- [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) (9.12 GB) or [t5xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn_scaled.safetensors) (4.8 GB)

**VAE**

- [ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

```
ComfyUI/
├── models/
│   ├── diffusion_models/
│   │   └─── flux1-dev.safetensors 
│   ├── text_encoders/
│   │   ├── clip_l.safetensors
│   │   └─── t5xxl_fp16.safetensors # or t5xxl_fp8_e4m3fn_scaled.safetensors
│   └── vae/
│       └── ae.safetensors
```

</details>
