# Anima Anime Text-to-Image Generation

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_anima_preview)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_anima_preview-1.webp" width="360" alt="Anima Anime Text-to-Image Generation image_anima_preview-1.webp">

> Input a text prompt to generate an anime-style image using the Anima model. Configure settings like steps and CFG scale to control the output. The workflow produces a non-photorealistic illustration based on your description.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_anima_preview.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_anima_preview.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/anima/anima)

## Details

| | |
|---|---|
| Name | `image_anima_preview` |
| Category | Foundation › Image |
| Output | image |
| Models | Anima |
| Tags | Anime, Text to Image |
| Type | open source |
| Date | 2025-05-07 |
| Author | ComfyUI |
| Download size | 5.2 GB |
| Min ComfyUI version | 0.11.0 |
| Usage | 209 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #46 | image | image_anima_preview.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `anima-preview3-base.safetensors` | `diffusion_models` | [link](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/diffusion_models/anima-preview3-base.safetensors) |
| `qwen_3_06b_base.safetensors` | `text_encoders` | [link](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/text_encoders/qwen_3_06b_base.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Text to Image (Anima)** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `EmptyLatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## About Anima

[Anima](https://huggingface.co/circlestone-labs/Anima) (2B-parameter, CircleStone/Comfy Org): Anime/non-photorealistic text-to-image model (no realism). Preview version trained on anime; final version to improve details.

Limitations: poor realism (intentional), weak high-res/text, plain style.

## Model Links

**text_encoders**

- [qwen_3_06b_base.safetensors](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/text_encoders/qwen_3_06b_base.safetensors) (1.11 GB)

**vae**

- [qwen_image_vae.safetensors](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

**diffusion_models**

- [anima-preview3-base.safetensors](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/diffusion_models/anima-preview3-base.safetensors) (3.89 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   └── qwen_3_06b_base.safetensors
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   └── 📂 diffusion_models/
│       └── anima-preview3-base.safetensors)
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
