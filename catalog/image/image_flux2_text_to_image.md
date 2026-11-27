# FLUX.2 Dev Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_flux2_text_to_image)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_text_to_image-1.webp" width="360" alt="FLUX.2 Dev Text to Image image_flux2_text_to_image-1.webp">

> Text-to-image with enhanced lighting, materials, and realistic details.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_text_to_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_flux2_text_to_image.json)
- [Tutorial](https://docs.comfy.org/tutorials/flux/flux-2-dev)

## Details

| | |
|---|---|
| Name | `image_flux2_text_to_image` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX, FLUX.2 Dev |
| Tags | Image, Text to Image |
| Type | open source |
| Date | 2025-11-26 |
| Author | ComfyUI |
| Download size | 66.5 GB |
| Min ComfyUI version | 0.4.0 |
| Usage | 260 |
| Nodes | 20 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #9 | image | image_flux2_text_to_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux2_dev_fp8mixed.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/diffusion_models/flux2_dev_fp8mixed.safetensors) |
| `Flux_2-Turbo-LoRA_comfyui.safetensors` | `loras` | [link](https://huggingface.co/ByteZSzn/Flux.2-Turbo-ComfyUI/resolve/main/Flux_2-Turbo-LoRA_comfyui.safetensors) |
| `mistral_3_small_flux2_bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/text_encoders/mistral_3_small_flux2_bf16.safetensors) |
| `full_encoder_small_decoder.safetensors` | `vae` | [link](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder/resolve/main/full_encoder_small_decoder.safetensors) |

## Subgraphs

- **Text to Image (FLUX.2 Dev)** (18 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `BasicGuider` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `EmptyFlux2LatentImage` | 1 | comfy-core |
| `Flux2Scheduler` | 1 | comfy-core |
| `FluxGuidance` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `PrimitiveBoolean` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/flux2-dev](https://huggingface.co/Comfy-Org/flux2-dev)

### Alternative Repos

- [ModelScope:Comfy-Org/flux2-dev](https://modelscope.cn/models/Comfy-Org/flux2-dev)

**vae**

- [full_encoder_small_decoder.safetensors](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder/resolve/main/full_encoder_small_decoder.safetensors) (238 MB)

**text_encoders**

- [mistral_3_small_flux2_bf16.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/text_encoders/mistral_3_small_flux2_bf16.safetensors) (33.14 GB)

**loras**

- [Flux_2-Turbo-LoRA_comfyui.safetensors](https://huggingface.co/ByteZSzn/Flux.2-Turbo-ComfyUI/resolve/main/Flux_2-Turbo-LoRA_comfyui.safetensors) (2.57 GB)

**diffusion_models**

- [flux2_dev_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/diffusion_models/flux2_dev_fp8mixed.safetensors) (33.02 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   └── full_encoder_small_decoder.safetensors
│   ├── 📂 text_encoders/
│   │   └── mistral_3_small_flux2_bf16.safetensors
│   ├── 📂 loras/
│   │   └── Flux_2-Turbo-LoRA_comfyui.safetensors
│   └── 📂 diffusion_models/
│       └── flux2_dev_fp8mixed.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
