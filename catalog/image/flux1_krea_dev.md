# Flux.1 Krea Dev

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=flux1_krea_dev)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux1_krea_dev-1.webp" width="360" alt="Flux.1 Krea Dev flux1_krea_dev-1.webp">

> A fine-tuned FLUX model pushing photorealism to the max

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux1_krea_dev.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/flux1_krea_dev.json)
- [Tutorial](https://docs.comfy.org/tutorials/flux/flux1-krea-dev)

## Details

| | |
|---|---|
| Name | `flux1_krea_dev` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX, FLUX.1 Krea |
| Tags | Image, Text to Image |
| Type | open source |
| Date | 2025-07-31 |
| Author | ComfyUI |
| Download size | 20.7 GB |
| Min ComfyUI version | 0.3.42 |
| Usage | 87 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #9 | image | flux1_krea_dev.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux1-krea-dev_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/FLUX.1-Krea-dev_ComfyUI/resolve/main/split_files/diffusion_models/flux1-krea-dev_fp8_scaled.safetensors) |
| `clip_l.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors) |
| `t5xxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Text to Image (Flux.1 Krea Dev)** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `DualCLIPLoader` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model links</summary>

- Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/FLUX.1-Krea-dev_ComfyUI](https://huggingface.co/Comfy-Org/FLUX.1-Krea-dev_ComfyUI)
- [Hugging Face:Comfy-Org/Lumina_Image_2.0_Repackaged](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/FLUX.1-Krea-dev_ComfyUI](https://modelscope.cn/models/Comfy-Org/FLUX.1-Krea-dev_ComfyUI)
- [ModelScope:Comfy-Org/Lumina_Image_2.0_Repackaged](https://modelscope.cn/models/Comfy-Org/Lumina_Image_2.0_Repackaged)

**text_encoders**

- [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors) (234.7 MB)
- [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) (9.12 GB)

**diffusion_models**

- [flux1-krea-dev_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/FLUX.1-Krea-dev_ComfyUI/resolve/main/split_files/diffusion_models/flux1-krea-dev_fp8_scaled.safetensors) (11.09 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      ├── clip_l.safetensors
│   │      └── t5xxl_fp16.safetensors
│   ├── 📂 diffusion_models/
│   │      └── flux1-krea-dev_fp8_scaled.safetensors
│   └── 📂 vae/
│          └── ae.safetensors
```

## Report issue

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
