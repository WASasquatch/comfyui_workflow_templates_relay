# OmniGen2: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_omnigen2_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_omnigen2_t2i-1.webp" width="360" alt="OmniGen2: Text to Image image_omnigen2_t2i-1.webp">

> Generate high-quality images from text prompts using OmniGen2's unified 7B multimodal model with dual-path architecture.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_omnigen2_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_omnigen2_t2i.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/omnigen/omnigen2)

## Details

| | |
|---|---|
| Name | `image_omnigen2_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | OmniGen |
| Tags | Image, Text to Image |
| Type | open source |
| Date | 2025-06-30 |
| Author | ComfyUI |
| Download size | 14.7 GB |
| Min ComfyUI version | 0.3.42 |
| Usage | 15 |
| Nodes | 14 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #9 | image | image_omnigen2_t2i.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `omnigen2_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/omnigen2_fp16.safetensors) |
| `qwen_2.5_vl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_fp16.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Omnigen2 Text to Image** (12 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `DualCFGGuider` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `RandomNoise` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>For Local User</summary>

[Docs](https://docs.comfy.org/tutorials/image/omnigen/omnigen2)

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Omnigen2_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged)
- [Hugging Face:Comfy-Org/Lumina_Image_2.0_Repackaged](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Omnigen2_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Omnigen2_ComfyUI_repackaged)
- [ModelScope:Comfy-Org/Lumina_Image_2.0_Repackaged](https://modelscope.cn/models/Comfy-Org/Lumina_Image_2.0_Repackaged)

**text_encoders**

- [qwen_2.5_vl_fp16.safetensors](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_fp16.safetensors) (6.99 GB)

**diffusion_models**

- [omnigen2_fp16.safetensors](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/omnigen2_fp16.safetensors) (7.39 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── qwen_2.5_vl_fp16.safetensors
│   ├── 📂 diffusion_models/
│   │      └── omnigen2_fp16.safetensors
│   └── 📂 vae/
│          └── ae.safetensors
```

## Report issue

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
