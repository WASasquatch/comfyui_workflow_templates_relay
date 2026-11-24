# Anima Base v1: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_anima_base_v1)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_anima_base_v1-1.webp" width="360" alt="Anima Base v1: Text to Image image_anima_base_v1-1.webp">

> Input a text prompt describing an anime or artistic illustration. Generate a non-photorealistic image focused on anime concepts, characters, or styles.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_anima_base_v1.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_anima_base_v1.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/anima/anima)

## Details

| | |
|---|---|
| Name | `image_anima_base_v1` |
| Category | Foundation › Image |
| Output | image |
| Models | Anima |
| Tags | Anime, Text to Image |
| Type | open source |
| Date | 2026-05-23 |
| Author | ComfyUI |
| Download size | 5.4 GB |
| Min ComfyUI version | 0.16.0 |
| Usage | 410 |
| Nodes | 20 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #46 | image | image_anima_base_v1.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `anima-base-v1.0.safetensors` | `diffusion_models` | [link](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/diffusion_models/anima-base-v1.0.safetensors) |
| `anima-turbo-lora-v0.2.safetensors` | `loras` | [link](https://huggingface.co/circlestone-labs/Anima-Official-LoRAs/resolve/main/anima-turbo-lora-v0.2.safetensors) |
| `qwen_3_06b_base.safetensors` | `text_encoders` | [link](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/text_encoders/qwen_3_06b_base.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Text to Image (Anima Base v1.0)** (17 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `PrimitiveFloat` | 2 |  |
| `PrimitiveInt` | 2 |  |
| `CLIPLoader` | 1 | comfy-core |
| `EmptyLatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PrimitiveBoolean` | 1 |  |
| `ResolutionSelector` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

- Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)
- Repository: [circlestone-labs/Anima](https://huggingface.co/circlestone-labs/Anima)
## Model Links

**text_encoders**

- [qwen_3_06b_base.safetensors](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/text_encoders/qwen_3_06b_base.safetensors) (1.11 GB)

**vae**

- [qwen_image_vae.safetensors](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

**diffusion_models**

- [anima-base-v1.0.safetensors](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/diffusion_models/anima-base-v1.0.safetensors) (3.89 GB)

**loras**

- [anima-turbo-lora-v0.2.safetensors](https://huggingface.co/circlestone-labs/Anima-Official-LoRAs/resolve/main/anima-turbo-lora-v0.2.safetensors) (142 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   └── qwen_3_06b_base.safetensors
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   ├── 📂 diffusion_models/
│   │   └── anima-base-v1.0.safetensors
│   └── 📂 loras/
│       └── anima-turbo-lora-v0.2.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
