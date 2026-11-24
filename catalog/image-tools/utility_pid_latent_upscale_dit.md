# Image Upscale: PiD Latent Decode

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_pid_latent_upscale_dit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_pid_latent_upscale_dit-1.webp" width="360" alt="Image Upscale: PiD Latent Decode utility_pid_latent_upscale_dit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_pid_latent_upscale_dit-2.webp" width="360" alt="Image Upscale: PiD Latent Decode utility_pid_latent_upscale_dit-2.webp">

> Input a latent image from a diffusion model and select a PiD checkpoint. Generate a high-resolution decoded image with 4x or 8x upscaling in a single pass.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_pid_latent_upscale_dit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_pid_latent_upscale_dit.json)

## Details

| | |
|---|---|
| Name | `utility_pid_latent_upscale_dit` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | PiD |
| Tags | Image Upscale |
| Type | open source |
| Date | 2026-05-19 |
| Author | ComfyUI |
| Download size | 24.2 GB |
| Min ComfyUI version | 0.23.0 |
| Distributions | local |
| Usage | 2 |
| Nodes | 26 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `pid_flux1_1024_to_4096_4step_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_flux1_1024_to_4096_4step_bf16.safetensors) |
| `z_image_turbo_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) |
| `gemma_2_2b_it_elm_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/text_encoders/gemma_2_2b_it_elm_fp8_scaled.safetensors) |
| `qwen_3_4b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Latent Upscale Decode (PiD)** (11 nodes)
- **Text to Image (Z-Image-Turbo)** (9 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPLoader` | 2 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `ConditioningZeroOut` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `UNETLoader` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `EmptyChromaRadianceLatentImage` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `ImageCompare` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PiDConditioning` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |
| `SamplerCustom` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: PiD</summary>

## PiD — Latent Upscale & Decode

PiD (Pixel Diffusion Decoder) turns a diffusion **latent** into a **4× super-resolved image** in 4 distilled pixel-space steps — no separate VAE decode.

PiD matches checkpoints by the **VAE / latent space** of the upstream model (the encoder side), not the diffusion model name alone.

**This workflow** uses **Z-Image-Turbo** (1024 px latent → 4096 px output). You can also find **Flux.1** and **FLUX.2** workflows in the template library — generate a latent with the matching VAE, then feed it into the PiD subgraph with the corresponding checkpoint below.

### Checkpoints

Download from [Comfy-Org/PixelDiT](https://huggingface.co/Comfy-Org/PixelDiT) → `models/diffusion_models/`. Set PiD output size to **4×** the input latent resolution.

| Checkpoint | Input → Output | Compatible latent (VAE backbone) |
| --- | --- | --- |
| `pid_flux1_512_to_2048_4step_bf16` | 512 → 2048 | Flux1-dev 16-ch VAE (Flux.1, Z-Image) |
| `pid_flux1_1024_to_4096_4step_bf16` | 1024 → 4096 | Flux1-dev 16-ch VAE (Flux.1, Z-Image) *(this workflow)* |
| `pid_flux2_512_to_2048_4step_bf16` | 512 → 2048 | Flux2-dev 128-ch VAE (FLUX.2) |
| `pid_flux2_1024_to_4096_4step_bf16` | 1024 → 4096 | Flux2-dev 128-ch VAE (FLUX.2) |
| `pid_sd3_512_to_2048_4step_bf16` | 512 → 2048 | SD3 medium 16-ch VAE |
| `pid_sd3_1024_to_4096_4step_bf16` | 1024 → 4096 | SD3 medium 16-ch VAE |

Z-Image shares Flux1's VAE — no separate PiD checkpoint; use the **flux1** rows above.

### Settings ([subgraph](https://docs.comfy.org/interface/features/subgraph))

Configure these on the **Latent Upscale Decode (PiD)** subgraph:

**latent_format:** `flux` for Flux1 / Flux2 / Z-Image (`sd3` for SD3; Flux2 auto-detected by 128 ch)

### degrade_sigma

How "finished" the input latent is — which point in diffusion PiD should start decoding from.

| Value | Latent state | When to use |
| --- | --- | --- |
| **0.0** (default) | Fully denoised, clean | Normal KSampler output — keep default |
| **0.1 – 0.8** | Partially denoised, still blurry | Early-stopped or noisy upstream latent |
| **1.0** | Pure noise | No prior generation; decode from scratch |

</details>

<details><summary>Note: Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [ModelScope:Comfy-Org/PixelDiT](https://modelscope.cn/models/Comfy-Org/PixelDiT)
- [Hugging Face:Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo)
- [ModelScope:Comfy-Org/z_image_turbo](https://modelscope.cn/models/Comfy-Org/z_image_turbo)

Repacks: [Comfy-Org/PixelDiT](https://huggingface.co/Comfy-Org/PixelDiT)

### Z Image Turbo
**text_encoders**

- [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) (7.49 GB)

**diffusion_models**

- [z_image_turbo_bf16.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) (11.46 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

### PiD

**diffusion_models** (512→2048 / 2k variant)

- [pid_flux1_512_to_2048_4step_bf16.safetensors](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_flux1_512_to_2048_4step_bf16.safetensors) (2.54 GB)
- [pid_flux2_512_to_2048_4step_bf16.safetensors](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_flux2_512_to_2048_4step_bf16.safetensors) (2.54 GB)
- [pid_sd3_512_to_2048_4step_bf16.safetensors](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_sd3_512_to_2048_4step_bf16.safetensors) (2.54 GB)

**diffusion_models** (1024→4096 / 2kto4k variant — used in this workflow)

- [pid_flux1_1024_to_4096_4step_bf16.safetensors](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_flux1_1024_to_4096_4step_bf16.safetensors) (2.54 GB)
- [pid_flux2_1024_to_4096_4step_bf16.safetensors](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_flux2_1024_to_4096_4step_bf16.safetensors) (2.54 GB)
- [pid_sd3_1024_to_4096_4step_bf16.safetensors](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/diffusion_models/pid_sd3_1024_to_4096_4step_bf16.safetensors) (2.54 GB)

**text_encoders** (load with `pixeldit` type)

- [gemma_2_2b_it_elm_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/text_encoders/gemma_2_2b_it_elm_fp8_scaled.safetensors) (2.44 GB)
- [gemma_2_2b_it_elm_bf16.safetensors](https://huggingface.co/Comfy-Org/PixelDiT/resolve/main/text_encoders/gemma_2_2b_it_elm_bf16.safetensors) (4.87 GB)

PiD uses built-in **pixel_space** VAE — no separate VAE file needed.

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   ├── gemma_2_2b_it_elm_fp8_scaled.safetensors
│   │   └── qwen_3_4b.safetensors
│   ├── 📂 diffusion_models/
│   │   ├── pid_flux1_1024_to_4096_4step_bf16.safetensors
│   │   └── z_image_turbo_bf16.safetensors
│   └── 📂 vae/
│       └── ae.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
