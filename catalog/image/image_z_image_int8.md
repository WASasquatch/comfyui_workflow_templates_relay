# Z-Image Int8: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_z_image_int8-1.webp" width="360" alt="Z-Image Int8: Text to Image image_z_image_int8-1.webp">

> Generate high-quality, diverse images from text prompts using the Z-Image Int8 model, which leverages an undistilled transformer for precise prompt adherence and broad stylistic coverage. The workflow takes no file inputs and produces 1 image output through a standard text-to-image pipeline. Ideal for professional creative projects, LoRA training and model development, and scenarios requiring robust negative control and high compositional diversity.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_z_image_int8.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_z_image_int8.json)

## Details

| | |
|---|---|
| Name | `image_z_image_int8` |
| Category | Foundation › Image |
| Media type | image |
| Models | Z-Image |
| Tags | Text to Image, Int8 |
| Type | open source |
| Date | 2026-07-10 |
| Author | ComfyUI |
| Download size | 13.6 GB |
| Min ComfyUI version | 0.23.0 |
| Usage | 59 |
| Nodes | 14 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImageAdvanced` #95 | image | image_z_image_int8.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `z_image_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/z_image/resolve/main/split_files/diffusion_models/z_image_int8_convrot.safetensors) |
| `qwen_3_4b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Text to Image(Z-Image-Base Int8)** (10 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `ResolutionSelector` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo)
- [Hugging Face:Comfy-Org/z_image](https://huggingface.co/Comfy-Org/z_image)

### Alternative Repos

- [ModelScope:Comfy-Org/z_image_turbo](https://modelscope.cn/models/Comfy-Org/z_image_turbo)
- [ModelScope:Comfy-Org/z_image](https://modelscope.cn/models/Comfy-Org/z_image)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

**text_encoders**

- [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) (7.49 GB)

**diffusion_models**

- [z_image_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/z_image/resolve/main/split_files/diffusion_models/z_image_int8_convrot.safetensors) (5.78 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   └── ae.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen_3_4b.safetensors
│   └── 📂 diffusion_models/
│       └── z_image_int8_convrot.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Original Settings</summary>

- Steps: 30～50
- cfg:  3～5

</details>

<details><summary>Original Settings</summary>

- Steps: 30～50
- cfg:  3～5

</details>
