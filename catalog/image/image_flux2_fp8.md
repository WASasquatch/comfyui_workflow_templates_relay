# Product Mockup(FLUX.2 Dev FP8)

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_flux2_fp8)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_fp8-1.webp" width="360" alt="Product Mockup(FLUX.2 Dev FP8) image_flux2_fp8-1.webp">

> Create product mockups by applying design patterns to packaging, mugs, and other products using multi-reference consistency.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_fp8.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_flux2_fp8.json)
- [Tutorial](https://docs.comfy.org/tutorials/flux/flux-2-dev)

## Details

| | |
|---|---|
| Name | `image_flux2_fp8` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX.2 Dev, FLUX |
| Tags | Text to Image, Image, Image Edit |
| Type | open source |
| Date | 2025-11-26 |
| Author | ComfyUI |
| Download size | 52.7 GB |
| Min ComfyUI version | 0.4.0 |
| Usage | 34 |
| Nodes | 29 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #42 | image | image_flux2_input_ref_image.png |
| input | `LoadImage` #46 | image | image_flux2_input_Illustration.png |
| output | `SaveImage` #9 | image | image_flux2_fp8.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux2_dev_fp8mixed.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/diffusion_models/flux2_dev_fp8mixed.safetensors) |
| `Flux2TurboComfyv2.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/loras/Flux2TurboComfyv2.safetensors) |
| `mistral_3_small_flux2_fp8.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/text_encoders/mistral_3_small_flux2_fp8.safetensors) |
| `flux2-vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) |

## Subgraphs

- **Image Edit (FLUX.2 Dev)** (25 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 2 |  |
| `ImageScaleToTotalPixels` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `PrimitiveInt` | 2 |  |
| `ReferenceLatent` | 2 | comfy-core |
| `VAEEncode` | 2 | comfy-core |
| `BasicGuider` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `EmptyFlux2LatentImage` | 1 | comfy-core |
| `Flux2Scheduler` | 1 | comfy-core |
| `FluxGuidance` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `PrimitiveBoolean` | 1 |  |
| `RandomNoise` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model links</summary>

We are using quantized weights in this workflow, the original FLUX.2 repo is [here](https://huggingface.co/black-forest-labs/FLUX.2-dev/)

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/flux2-dev](https://huggingface.co/Comfy-Org/flux2-dev)

### Alternative Repos

- [ModelScope:Comfy-Org/flux2-dev](https://modelscope.cn/models/Comfy-Org/flux2-dev)

**text_encoders**

- [mistral_3_small_flux2_fp8.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/text_encoders/mistral_3_small_flux2_fp8.safetensors) (16.8 GB)

**loras**

- [Flux2TurboComfyv2.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/loras/Flux2TurboComfyv2.safetensors) (2.57 GB)

**diffusion_models**

- [flux2_dev_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/diffusion_models/flux2_dev_fp8mixed.safetensors) (33.02 GB)

**vae**

- [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) (320.6 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── mistral_3_small_flux2_fp8.safetensors
│   ├── 📂 loras/
│   │      └── Flux2TurboComfyv2.safetensors
│   ├── 📂 diffusion_models/
│   │      └── flux2_dev_fp8mixed.safetensors
│   └── 📂 vae/
│          └── flux2-vae.safetensors
```

## Report issue

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
