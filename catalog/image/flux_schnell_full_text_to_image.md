# Flux.1 Schnell Full: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_schnell_full_text_to_image-1.webp" width="360" alt="Flux.1 Schnell Full: Text to Image flux_schnell_full_text_to_image-1.webp">

> Generate images quickly with Flux.1 Schnell full version. Uses Apache2.0 license, requires only 4 steps to generate images while maintaining good image quality.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_schnell_full_text_to_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/flux_schnell_full_text_to_image.json)
- [Tutorial](https://docs.comfy.org/tutorials/flux/flux-1-text-to-image)

## Details

| | |
|---|---|
| Name | `flux_schnell_full_text_to_image` |
| Category | Foundation › Image |
| Media type | image |
| Models | FLUX.1, FLUX |
| Tags | Text to Image, Image |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 31.8 GB |
| Min ComfyUI version | 0.0.4 |
| Usage | 52 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #9 | image | flux_schnell_full_text_to_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux1-schnell.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/flux1-schnell/resolve/main/flux1-schnell.safetensors) |
| `clip_l.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors) |
| `t5xxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncodeFlux` | 1 | comfy-core |
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

- [Hugging Face:Comfy-Org/flux1-schnell](https://huggingface.co/Comfy-Org/flux1-schnell)
- [Hugging Face:Comfy-Org/Lumina_Image_2.0_Repackaged](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/flux1-schnell](https://modelscope.cn/models/Comfy-Org/flux1-schnell)
- [ModelScope:Comfy-Org/Lumina_Image_2.0_Repackaged](https://modelscope.cn/models/Comfy-Org/Lumina_Image_2.0_Repackaged)

**Diffusion Model**

- [flux1-schnell.safetensors](https://huggingface.co/Comfy-Org/flux1-schnell/resolve/main/flux1-schnell.safetensors) (22.15 GB)

**Text Encoder**

- [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors)

- [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) (9.12 GB) or [t5xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn_scaled.safetensors) (4.8 GB)

**VAE**

- [ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

```
ComfyUI/
├── models/
│   ├── diffusion_models/
│   │   └─── flux1-schnell.safetensors
│   ├── text_encoders/
│   │   ├── clip_l.safetensors
│   │   └─── t5xxl_fp16.safetensors # or t5xxl_fp8_e4m3fn_scaled.safetensors
│   └── vae/
│       └── ae.safetensors
```

</details>
