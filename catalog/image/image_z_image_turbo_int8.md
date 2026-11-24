# Z-Image-Turbo Int8: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_z_image_turbo_int8-1.webp" width="360" alt="Z-Image-Turbo Int8: Text to Image image_z_image_turbo_int8-1.webp">

> Generate photorealistic images using the Z-Image-Turbo int8 model, a distilled 6B-parameter variant optimized for sub-second inference through efficient 8-step sampling. The workflow takes a text prompt as input and outputs a single high-quality image. Ideal for rapid creative iteration, realistic concept art, and production-ready visual prototyping.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_z_image_turbo_int8.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_z_image_turbo_int8.json)

## Details

| | |
|---|---|
| Name | `image_z_image_turbo_int8` |
| Category | Foundation › Image |
| Media type | image |
| Models | Z-Image-Turbo |
| Tags | Text to Image, Int8 |
| Type | open source |
| Date | 2026-07-04 |
| Author | ComfyUI |
| Download size | 11.3 GB |
| Min ComfyUI version | 0.11.0 |
| Usage | 141 |
| Nodes | 11 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #9 | image | image_z_image_turbo_int8.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `z_image_turbo_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_int8_convrot.safetensors) |
| `qwen_3_4b_fp8_mixed.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b_fp8_mixed.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Text to Image (Z-Image-Turbo)** (9 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPLoader` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model link</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo)

### Alternative Repos

- [ModelScope:Comfy-Org/z_image_turbo](https://modelscope.cn/models/Comfy-Org/z_image_turbo)

**text_encoders**

- [qwen_3_4b_fp8_mixed.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b_fp8_mixed.safetensors) (5.25 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

**diffusion_models**

- [z_image_turbo_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_int8_convrot.safetensors) (5.78 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   └── qwen_3_4b_fp8_mixed.safetensors
│   ├── 📂 vae/
│   │   └── ae.safetensors
│   └── 📂 diffusion_models/
│       └── z_image_turbo_int8_convrot.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
