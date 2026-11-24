# Lens Turbo: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_lens_turbo_t2i-1.webp" width="360" alt="Lens Turbo: Text to Image image_lens_turbo_t2i-1.webp">

> Input a text prompt and select resolution, aspect ratio, and inference steps. Generate a high-quality image using the Lens text-to-image model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_lens_turbo_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_lens_turbo_t2i.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/lens/lens)

## Details

| | |
|---|---|
| Name | `image_lens_turbo_t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | Lens |
| Tags | Text to Image |
| Type | open source |
| Date | 2026-05-26 |
| Author | ComfyUI |
| Download size | 20.3 GB |
| Min ComfyUI version | 0.23.0 |
| Distributions | local |
| Usage | 27 |
| Nodes | 20 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #43 | image | image_lens_turbo_t2i.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `lens_turbo_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Lens/resolve/main/diffusion_models/lens_turbo_bf16.safetensors) |
| `gpt_oss_20b_nvfp4.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Lens/resolve/main/text_encoders/gpt_oss_20b_nvfp4.safetensors) |
| `flux2-vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Lens/resolve/main/vae/flux2-vae.safetensors) |

## Subgraphs

- **Text to Image (Lens Turbo)** (16 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `ComfyMathExpression` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `PrimitiveInt` | 2 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `CFGNorm` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `EmptyLatentImage` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `ModelSamplingFlux` | 1 | comfy-core |
| `ResolutionSelector` | 1 | comfy-core |
| `SamplerCustom` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Lens Turbo</summary>

# Lens Turbo

Lens-Turbo is the distilled fast variant of Microsoft's 3.8B Lens text-to-image model family. This workflow is the ComfyUI text-to-image turbo version and is configured around the official 4-step setup.

## Key Traits

- Fast 4-step generation for quick iteration.
- Generates up to `1440x1440` base resolution.
- Uses GPT-OSS text features and the FLUX.2 semantic VAE for strong prompt following.
- Distilled from the RL-tuned Lens model to keep strong quality at much lower sampling cost.


## Repository Info

- ComfyUI model files: [Comfy-Org/Lens](https://huggingface.co/Comfy-Org/Lens) (includes `lens_turbo_bf16.safetensors`)
- Paper: [Lens: Rethinking Training Efficiency for Foundational Text-to-Image Models](https://arxiv.org/abs/2605.21573)

</details>

<details><summary>Note: Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Required Model Repositories

- Model repo: [Comfy-Org/Lens](https://huggingface.co/Comfy-Org/Lens) (includes `lens_turbo_bf16.safetensors`)
- [ModelScope:Comfy-Org/Lens](https://modelscope.cn/models/Comfy-Org/Lens)

## Model Links

**vae**

- [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/Lens/resolve/main/vae/flux2-vae.safetensors) (320.6 MB)

**text_encoders**

- [gpt_oss_20b_nvfp4.safetensors](https://huggingface.co/Comfy-Org/Lens/resolve/main/text_encoders/gpt_oss_20b_nvfp4.safetensors) (12.33 GB)

**diffusion_models**

- [lens_turbo_bf16.safetensors](https://huggingface.co/Comfy-Org/Lens/resolve/main/diffusion_models/lens_turbo_bf16.safetensors) (7.64 GB)

## Recommended Turbo Settings

- Steps: `4`
- CFG: `1.0`
- Sampler: `euler`
- Aspect ratios from `1:2` to `2:1`
- Designed for the Lens `1440` base-resolution workflow family

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   └── flux2-vae.safetensors
│   ├── 📂 text_encoders/
│   │   └── gpt_oss_20b_nvfp4.safetensors
│   └── 📂 diffusion_models/
│       └── lens_turbo_bf16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
