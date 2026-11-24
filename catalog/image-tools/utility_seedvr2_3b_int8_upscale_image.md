# Image Upscale: SeedVR2 3B Int8

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_seedvr2_3b_int8_upscale_image)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_seedvr2_3b_int8_upscale_image-1.webp" width="360" alt="Image Upscale: SeedVR2 3B Int8 utility_seedvr2_3b_int8_upscale_image-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_seedvr2_3b_int8_upscale_image-2.webp" width="360" alt="Image Upscale: SeedVR2 3B Int8 utility_seedvr2_3b_int8_upscale_image-2.webp">

> Upscale images using SeedVR2 3B Int8, a one-step diffusion-based video restoration model that produces high-quality results with improved temporal consistency. Ideal for restoring degraded footage, upscaling low-resolution videos, and enhancing archival media.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_seedvr2_3b_int8_upscale_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_seedvr2_3b_int8_upscale_image.json)

## Details

| | |
|---|---|
| Name | `utility_seedvr2_3b_int8_upscale_image` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | SeedVR2 |
| Tags | Image Upscale, Int8 |
| Type | open source |
| Date | 2026-07-13 |
| Author | ComfyUI |
| Download size | 3.7 GB |
| Min ComfyUI version | 0.28.0 |
| Usage | 122 |
| Nodes | 14 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | watch_macro_shot.png |
| output | `SaveImage` #9 | image | utility_seedvr2_3b_int8_upscale_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `seedvr2_3b_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/SeedVR2/resolve/main/diffusion_models/seedvr2_3b_int8_convrot.safetensors) |
| `seedvr2_ema_vae_fp16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/SeedVR2/resolve/main/vae/seedvr2_ema_vae_fp16.safetensors) |

## Subgraphs

- **Upscale Image (SeedVR2 3B Int8)** (10 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ImageCompare` | 1 | comfy-core |
| `JoinImageWithAlpha` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ResizeImageMaskNode` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `SeedVR2Conditioning` | 1 | comfy-core |
| `SeedVR2PostProcessing` | 1 | comfy-core |
| `SeedVR2Preprocess` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecodeTiled` | 1 | comfy-core |
| `VAEEncodeTiled` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/SeedVR2](https://huggingface.co/Comfy-Org/SeedVR2)
- [ModelScope:Comfy-Org/SeedVR2](https://modelscope.cn/models/Comfy-Org/SeedVR2)

**vae**

- [seedvr2_ema_vae_fp16.safetensors](https://huggingface.co/Comfy-Org/SeedVR2/resolve/main/vae/seedvr2_ema_vae_fp16.safetensors) (478.1 MB)

**diffusion_models**

- [seedvr2_3b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/SeedVR2/resolve/main/diffusion_models/seedvr2_3b_int8_convrot.safetensors) (3.22 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   └── seedvr2_ema_vae_fp16.safetensors
│   └── 📂 diffusion_models/
│       └── seedvr2_3b_int8_convrot.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
