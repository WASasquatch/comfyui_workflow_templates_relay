# PixelDiT: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_pixeldit_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_pixeldit_t2i-1.webp" width="360" alt="PixelDiT: Text to Image image_pixeldit_t2i-1.webp">

> Input a text prompt and optional negative prompt. Generate a 1024px image using PixelDiT's VAE-free pixel diffusion transformer.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_pixeldit_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_pixeldit_t2i.json)

## Details

| | |
|---|---|
| Name | `image_pixeldit_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | PixelDiT |
| Tags | Text to Image |
| Type | open source |
| Date | 2026-04-29 |
| Author | ComfyUI |
| Download size | 7.3 GB |
| Min ComfyUI version | 0.23.0 |
| Usage | 16 |
| Nodes | 12 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #43 | image | image_pixeldit_t2i.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `pixeldit_1300m_1024px_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pixeldit_1300m_1024px_bf16.safetensors) |
| `gemma_2_2b_it_elm_bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/text_encoders/gemma_2_2b_it_elm_bf16.safetensors) |

## Subgraphs

- **Text to Image (PixelDiT)** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `CLIPLoader` | 1 | comfy-core |
| `EmptyChromaRadianceLatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `ResolutionSelector` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: PixelDiT</summary>

## PixelDiT Text-to-Image

NVIDIA's **PixelDiT** is a pixel-space diffusion transformer for 1024px text-to-image generation.

### Links

- **ComfyUI support PR:** [Comfy-Org/ComfyUI#14103](https://github.com/Comfy-Org/ComfyUI/pull/14103) — merged 2026-05-27; adds PixelDiT T2I and PiD support
- **Official model:** [nvidia/PixelDiT-1300M-1024px](https://huggingface.co/nvidia/PixelDiT-1300M-1024px)
- **ComfyUI weights:** [Comfy-Org/PixelDiT](https://huggingface.co/Comfy-Org/PixelDiT)
- **Subgraph:** [docs.comfy.org — Subgraph](https://docs.comfy.org/interface/features/subgraph)

### Model highlights

- **VAE-free** — generates directly in pixel space; no traditional VAE encode/decode
- **Dual-level DiT** — patch-level DiT + pixel-level DiT
- **MM-DiT fusion** — joint attention between text and image tokens
- **Text encoder** — Gemma-2-2B-IT
- **Multi aspect ratio** — 1024px base resolution; supports several aspect ratios
- **Parameters** — ~1.3B
- **License** — NSCLv1 (non-commercial research/evaluation only)

### Workflow layout

`ResolutionSelector` → [subgraph](https://docs.comfy.org/interface/features/subgraph) **Text to Image (PixelDiT)** → `SaveImage`

Most generation settings live inside the [subgraph](https://docs.comfy.org/interface/features/subgraph). On the main canvas you mainly adjust resolution outside the [subgraph](https://docs.comfy.org/interface/features/subgraph) and the exposed [subgraph](https://docs.comfy.org/interface/features/subgraph) widgets below.

</details>

<details><summary>Note: Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/PixelDiT](https://huggingface.co/Comfy-Org/PixelDiT)
- [ModelScope:Comfy-Org/PixelDiT](https://modelscope.cn/models/Comfy-Org/PixelDiT)

**text_encoders**

- [gemma_2_2b_it_elm_bf16.safetensors](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/text_encoders/gemma_2_2b_it_elm_bf16.safetensors) (4.87 GB)

**diffusion_models**

- [pixeldit_1300m_1024px_bf16.safetensors](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pixeldit_1300m_1024px_bf16.safetensors) (2.43 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   └── gemma_2_2b_it_elm_bf16.safetensors
│   └── 📂 diffusion_models/
│       └── pixeldit_1300m_1024px_bf16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
