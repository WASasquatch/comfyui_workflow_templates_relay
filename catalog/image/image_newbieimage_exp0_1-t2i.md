# NewBie Exp0.1: Anime Generation

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_newbieimage_exp0_1-t2i-1.webp" width="360" alt="NewBie Exp0.1: Anime Generation image_newbieimage_exp0_1-t2i-1.webp">

> Generate detailed anime-style images with NewBie Exp0.1's Next-DiT architecture. Supports XML structured prompts for better multi-character scenes and attribute control.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_newbieimage_exp0_1-t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_newbieimage_exp0_1-t2i.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/newbie-image/newbie-image-exp-0-1)

## Details

| | |
|---|---|
| Name | `image_newbieimage_exp0_1-t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | NewBie |
| Tags | Anime, Image, Text to Image |
| Type | open source |
| Date | 2025-12-19 |
| Author | ComfyUI |
| Download size | 15.1 GB |
| Min ComfyUI version | 0.6.0 |
| Usage | 28 |
| Nodes | 17 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #9 | image | image_newbieimage_exp0_1-t2i.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `NewBie-Image-Exp0.1-bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/NewBie-image-Exp0.1_repackaged/resolve/main/split_files/diffusion_models/NewBie-Image-Exp0.1-bf16.safetensors) |
| `gemma_3_4b_it_bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/NewBie-image-Exp0.1_repackaged/resolve/main/split_files/text_encoders/gemma_3_4b_it_bf16.safetensors) |
| `jina_clip_v2_bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/NewBie-image-Exp0.1_repackaged/resolve/main/split_files/text_encoders/jina_clip_v2_bf16.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **NewBie Image Exp0.1** (9 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveStringMultiline` | 3 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `StringReplace` | 2 | comfy-core |
| `DualCLIPLoader` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>For Local User</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Report issue

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

## Model Links

- [Hugging Face:Comfy-Org/NewBie-image-Exp0.1_repackaged](https://huggingface.co/Comfy-Org/NewBie-image-Exp0.1_repackaged)
- [Hugging Face:Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo)

### Alternative Repos

- [ModelScope:Comfy-Org/NewBie-image-Exp0.1_repackaged](https://modelscope.cn/models/Comfy-Org/NewBie-image-Exp0.1_repackaged)
- [ModelScope:Comfy-Org/z_image_turbo](https://modelscope.cn/models/Comfy-Org/z_image_turbo)

**text_encoders**

- [gemma_3_4b_it_bf16.safetensors](https://huggingface.co/Comfy-Org/NewBie-image-Exp0.1_repackaged/resolve/main/split_files/text_encoders/gemma_3_4b_it_bf16.safetensors) (7.23 GB)
- [jina_clip_v2_bf16.safetensors](https://huggingface.co/Comfy-Org/NewBie-image-Exp0.1_repackaged/resolve/main/split_files/text_encoders/jina_clip_v2_bf16.safetensors) (1.04 GB)

**diffusion_models**

- [NewBie-Image-Exp0.1-bf16.safetensors](https://huggingface.co/Comfy-Org/NewBie-image-Exp0.1_repackaged/resolve/main/split_files/diffusion_models/NewBie-Image-Exp0.1-bf16.safetensors) (6.49 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      ├── gemma_3_4b_it_bf16.safetensors
│   │      └── jina_clip_v2_bf16.safetensors
│   ├── 📂 diffusion_models/
│   │      └── NewBie-Image-Exp0.1-bf16.safetensors
│   └── 📂 vae/
│          └── ae.safetensors
```

</details>

<details><summary>About NewBie Exp0.1</summary>

NewBie-image is an anime-style text-to-image generation model developed by NewBieAI Lab, built for creating high-quality anime and second-generation (ACG) images.

- Huggingface: [NewBie-AI/NewBie-image-Exp0.1](https://huggingface.co/NewBie-AI/NewBie-image-Exp0.1)
- [Getting Started Guide](https://ai.feishu.cn/wiki/NZl9wm7V1iuNzmkRKCUcb1USnsh)
- [LoRa Trainer](https://www.notion.so/Newbie-AI-lora-training-tutorial-English-2c2e4ae984ab8177b312e318827657e6?source=copy_link)

</details>
