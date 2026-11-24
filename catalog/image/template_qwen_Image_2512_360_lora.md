# Qwen Image 2512: 360 Panorama Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_qwen_Image_2512_360_lora)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_qwen_Image_2512_360_lora-1.webp" width="360" alt="Qwen Image 2512: 360 Panorama Image template_qwen_Image_2512_360_lora-1.webp">

> Generate 360-degree equirectangular projection images from text descriptions using a rank 128 LoRA on the 20B MMDiT model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_qwen_Image_2512_360_lora.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_qwen_Image_2512_360_lora.json)

## Details

| | |
|---|---|
| Name | `template_qwen_Image_2512_360_lora` |
| Category | Foundation › Image |
| Output | image |
| Models | Qwen-Image 2512 |
| Tags | Text to Image, LoRA |
| Type | open source |
| Date | 2026-05-19 |
| Author | ComfyUI |
| Download size | 30.3 GB |
| Min ComfyUI version | 0.4.0 |
| Usage | 15 |
| Nodes | 26 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_2512_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors) |
| `qwen-360-diffusion-2512-int8-bf16-v2.safetensors` | `loras` | [link](https://huggingface.co/ProGamerGov/qwen-360-diffusion/resolve/main/qwen-360-diffusion-2512-int8-bf16-v2.safetensors) |
| `Qwen-Image-2512-Lightning-4steps-V1.0-fp32.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Qwen-Image-2512-Lightning/resolve/main/Qwen-Image-2512-Lightning-4steps-V1.0-fp32.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Text to Image (Qwen-Image 2512 with LoRA)** (19 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 | comfy-core |
| `MarkdownNote` | 3 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `PrimitiveFloat` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `PrimitiveStringMultiline` | 2 |  |
| `CLIPLoader` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `StringConcatenate` | 1 |  |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)

### Alternative Repos

- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**vae**

- [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

**diffusion_models**

- [qwen_image_2512_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors) (19.03 GB)

**loras**

- [Qwen-Image-2512-Lightning-4steps-V1.0-fp32.safetensors](https://huggingface.co/lightx2v/Qwen-Image-2512-Lightning/resolve/main/Qwen-Image-2512-Lightning-4steps-V1.0-fp32.safetensors) (1.58 GB)
- [qwen-360-diffusion-2512-int8-bf16-v2.safetensors](https://huggingface.co/ProGamerGov/qwen-360-diffusion/resolve/main/qwen-360-diffusion-2512-int8-bf16-v2.safetensors) (720.1 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   ├── 📂 diffusion_models/
│   │   └── qwen_image_2512_fp8_e4m3fn.safetensors
│   └── 📂 loras/
│       ├── Qwen-Image-2512-Lightning-4steps-V1.0-fp32.safetensors
│       └── qwen-360-diffusion-2512-int8-bf16-v2.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: LoRA Trigger Words</summary>

"equirectangular", "360 image", "360 panorama", or "360 degree panorama with equirectangular projection"

</details>

<details><summary>Qwen 360 LoRA</summary>

## [Qwen 360 Diffusion LoRA](https://huggingface.co/ProGamerGov/qwen-360-diffusion/)

Rank-128 LoRA on **Qwen-Image-2512** for **equirectangular 360°** text-to-image. Trained on tens of thousands of 2:1 panoramas (landscapes, interiors, people, objects).

### How it fits this graph

| Subgraph control | Role |
|------------------|------|
| **`lora_model`** | Qwen 360 Diffusion (default strength **1.0**) |
| **`lightning_lora`** + **`enable_turbo_mode`** | Optional 4-step Lightning LoRA — speed only, not 360-specific |

Connect your prompt via the trigger prefix + main text. Trigger phrases → **Note: LoRA Trigger Words** (next to prompt).

### Recommended settings

- **Size:** **2048×1024** (2:1, workflow default). Smaller 2:1 (e.g. 1024×512) can work but horizons may be less stable.
- **Prompt:** Add medium/style (photograph, illustration, etc.). Image **wraps left↔right**; top/bottom are sphere poles.
- **People:** For full-body shots, describe head/face and shoes/boots to reduce limb distortion.

### FP8 base model note

This template uses `qwen_image_2512_fp8_e4m3fn`. With the **int8-trained** 360 LoRA, rare patch/grid artifacts may appear — try slightly lower LoRA strength or prompt tweaks; see the [model card](https://huggingface.co/ProGamerGov/qwen-360-diffusion) for int4 LoRA variants on FP8 quants.

### Next steps

Try to load the output as a background image in the Load 3D node in ComfyUI, it supports panoramic images as the background

</details>
