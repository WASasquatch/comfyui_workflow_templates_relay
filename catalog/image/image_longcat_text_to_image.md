# LongCat Image: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_longcat_text_to_image-1.webp" width="360" alt="LongCat Image: Text to Image image_longcat_text_to_image-1.webp">

> Generate an image from a text prompt. Input your desired scene description in English or Chinese. Output a photorealistic image with accurate text rendering.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_longcat_text_to_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_longcat_text_to_image.json)

## Details

| | |
|---|---|
| Name | `image_longcat_text_to_image` |
| Category | Foundation › Image |
| Media type | image |
| Models | LongCat |
| Tags | Image, Text to Image |
| Type | open source |
| Date | 2026-03-02 |
| Author | ComfyUI |
| Download size | 20.7 GB |
| Min ComfyUI version | 0.16.0 |
| Usage | 22 |
| Nodes | 14 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #9 | image | image_longcat_text_to_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `longcat_image_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/LongCat-Image/resolve/main/split_files/diffusion_models/longcat_image_bf16.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **New Subgraph** (11 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `FluxGuidance` | 2 | comfy-core |
| `CFGNorm` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ResolutionSelector` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

[meituan-longcat/LongCat-Image](https://huggingface.co/meituan-longcat/LongCat-Image)

## Model Links

- [Hugging Face:Comfy-Org/LongCat-Image](https://huggingface.co/Comfy-Org/LongCat-Image)
- [Hugging Face:Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged)
- [Hugging Face:Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo)

### Alternative Repos

- [ModelScope:Comfy-Org/LongCat-Image](https://modelscope.cn/models/Comfy-Org/LongCat-Image)
- [ModelScope:Comfy-Org/HunyuanVideo_1.5_repackaged](https://modelscope.cn/models/Comfy-Org/HunyuanVideo_1.5_repackaged)
- [ModelScope:Comfy-Org/z_image_turbo](https://modelscope.cn/models/Comfy-Org/z_image_turbo)

**diffusion_models**

- [longcat_image_bf16.safetensors](https://huggingface.co/Comfy-Org/LongCat-Image/resolve/main/split_files/diffusion_models/longcat_image_bf16.safetensors) (11.68 GB)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── longcat_image_bf16.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   └── 📂 vae/
│       └── ae.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
