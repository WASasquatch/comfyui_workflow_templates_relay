# SDXL1.0: Text to Image (Simple)

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_sdxl_simple-1.webp" width="360" alt="SDXL1.0: Text to Image (Simple) image_sdxl_simple-1.webp">

> Generate high-quality images from text prompts using the SDXL 1.0 model, offering a straightforward text-to-image generation workflow. Ideal for quick concept visualization, creative brainstorming, and rapid prototyping of visual ideas.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_sdxl_simple.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_sdxl_simple.json)

## Details

| | |
|---|---|
| Name | `image_sdxl_simple` |
| Category | Foundation › Image |
| Media type | image |
| Models | SDXL |
| Tags | Image, Text to Image |
| Type | open source |
| Date | 2024-02-22 |
| Author | ComfyUI |
| Download size | 6.5 GB |
| Min ComfyUI version | 0.0.1 |
| Usage | 350 |
| Nodes | 8 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #7 | image | image_sdxl_simple.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sd_xl_base_1.0.safetensors` | `checkpoints` | [link](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors?download=true) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `EmptyLatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Model Link</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Link

**checkpoints**

- [sd_xl_base_1.0.safetensors](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors?download=true) (6.46 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 checkpoints/
│       └── sd_xl_base_1.0.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
