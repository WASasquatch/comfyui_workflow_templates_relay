# Boogu Turbo: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_boogu_image_0_1_turbo_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_boogu_image_0_1_turbo_t2i-1.webp" width="360" alt="Boogu Turbo: Text to Image image_boogu_image_0_1_turbo_t2i-1.webp">

> Generate high-quality images from text prompts using the Boogu Turbo model, a distilled 10B-parameter text-to-image pipeline that produces photorealistic outputs in just 4 steps. The workflow accepts one text prompt and outputs a single 1024x1024 image. Ideal for rapid prototyping of photorealistic concepts, generating marketing visuals, and creating bilingual text-rendered images with strong prompt adherence.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_boogu_image_0_1_turbo_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_boogu_image_0_1_turbo_t2i.json)

## Details

| | |
|---|---|
| Name | `image_boogu_image_0_1_turbo_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | Boogu |
| Tags | Image, Text to Image |
| Type | open source |
| Date | 2026-06-23 |
| Author | ComfyUI |
| Download size | 19.8 GB |
| Min ComfyUI version | 0.26.0 |
| Usage | 24 |
| Nodes | 11 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #33 | image | image_boogu_image_0_1_turbo_t2i.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `boogu_image_turbo_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Boogu-Image/resolve/main/diffusion_models/boogu_image_turbo_fp8_scaled.safetensors) |
| `qwen3vl_8b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Boogu-Image/resolve/main/text_encoders/qwen3vl_8b_fp8_scaled.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/vae/ae.safetensors?download=true) |

## Subgraphs

- **Text to Image (Boogu Turbo)** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPLoader` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `EmptyLatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ResolutionSelector` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Boogu-Image](https://huggingface.co/Comfy-Org/Boogu-Image)
- [Hugging Face:Comfy-Org/HiDream-I1_ComfyUI](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI)

### Alternative Repos

- [ModelScope:Comfy-Org/Boogu-Image](https://modelscope.cn/models/Comfy-Org/Boogu-Image)
- [ModelScope:Comfy-Org/HiDream-I1_ComfyUI](https://modelscope.cn/models/Comfy-Org/HiDream-I1_ComfyUI)

**text_encoders**

- [qwen3vl_8b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Boogu-Image/resolve/main/text_encoders/qwen3vl_8b_fp8_scaled.safetensors) (9.86 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/vae/ae.safetensors?download=true) (319.8 MB)

**diffusion_models**

- [boogu_image_turbo_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Boogu-Image/resolve/main/diffusion_models/boogu_image_turbo_fp8_scaled.safetensors) (9.61 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   └── qwen3vl_8b_fp8_scaled.safetensors
│   ├── 📂 vae/
│   │   └── ae.safetensors
│   └── 📂 diffusion_models/
│       └── boogu_image_turbo_fp8_scaled.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
