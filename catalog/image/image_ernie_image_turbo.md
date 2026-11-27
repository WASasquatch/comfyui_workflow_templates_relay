# Ernie Image Turbo: Text To Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_ernie_image_turbo)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_ernie_image_turbo-1.webp" width="360" alt="Ernie Image Turbo: Text To Image image_ernie_image_turbo-1.webp">

> Generate images from text prompts using the ERNIE-Image turbo model. Input a text description and receive a high-quality image with precise text rendering and structured layouts.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_ernie_image_turbo.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_ernie_image_turbo.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/ernie-image/ernie-image)

## Details

| | |
|---|---|
| Name | `image_ernie_image_turbo` |
| Category | Foundation › Image |
| Output | image |
| Models | ERNIE-Image |
| Tags | Text to Image, Turbo |
| Type | open source |
| Date | 2026-04-14 |
| Author | ComfyUI |
| Download size | 24.2 GB |
| Min ComfyUI version | 0.44.0 |
| Usage | 76 |
| Nodes | 21 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #73 | image | image_ernie_image_turbo.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ernie-image-turbo.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/ERNIE-Image/resolve/main/diffusion_models/ernie-image-turbo.safetensors) |
| `ernie-image-prompt-enhancer.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ERNIE-Image/resolve/main/text_encoders/ernie-image-prompt-enhancer.safetensors) |
| `ministral-3-3b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ERNIE-Image/resolve/main/text_encoders/ministral-3-3b.safetensors) |
| `flux2-vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/ERNIE-Image/resolve/main/vae/flux2-vae.safetensors) |

## Subgraphs

- **Text to Image (Ernie Image Turbo)** (19 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewAny` | 3 | comfy-core |
| `StringReplace` | 3 | comfy-core |
| `CLIPLoader` | 2 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `ComfySwitchNode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `EmptyFlux2LatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `PrimitiveBoolean` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `TextGenerateV2` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/ERNIE-Image](https://huggingface.co/Comfy-Org/ERNIE-Image)
- [ModelScope:Comfy-Org/ERNIE-Image](https://modelscope.cn/models/Comfy-Org/ERNIE-Image)

**diffusion_models**

- [ernie-image-turbo.safetensors](https://huggingface.co/Comfy-Org/ERNIE-Image/resolve/main/diffusion_models/ernie-image-turbo.safetensors) (14.96 GB)

**text_encoders**

- [ministral-3-3b.safetensors](https://huggingface.co/Comfy-Org/ERNIE-Image/resolve/main/text_encoders/ministral-3-3b.safetensors) (7.19 GB)
- [ernie-image-prompt-enhancer.safetensors](https://huggingface.co/Comfy-Org/ERNIE-Image/resolve/main/text_encoders/ernie-image-prompt-enhancer.safetensors) (6.41 GB)

**vae**

- [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/ERNIE-Image/resolve/main/vae/flux2-vae.safetensors) (320.6 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── ernie-image-turbo.safetensors
│   ├── 📂 text_encoders/
│   │   ├── ministral-3-3b.safetensors
│   │   └── ernie-image-prompt-enhancer.safetensors
│   └── 📂 vae/
│       └── flux2-vae.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
