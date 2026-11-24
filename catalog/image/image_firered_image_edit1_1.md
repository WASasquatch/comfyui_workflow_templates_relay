# FireRed Image Edit 1.1: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_firered_image_edit1_1-1.webp" width="360" alt="FireRed Image Edit 1.1: Image Edit image_firered_image_edit1_1-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_firered_image_edit1_1-2.webp" width="360" alt="FireRed Image Edit 1.1: Image Edit image_firered_image_edit1_1-2.webp">

> Upload an image and a text prompt to edit it. Generate a modified image with enhanced identity consistency, multi-element fusion, or professional photo restoration.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_firered_image_edit1_1.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_firered_image_edit1_1.json)

## Details

| | |
|---|---|
| Name | `image_firered_image_edit1_1` |
| Category | Foundation › Image |
| Media type | image |
| Models | FireRed Image Edit 1.1 |
| Tags | Image Edit |
| Type | open source |
| Date | 2026-03-06 |
| Author | ComfyUI |
| Download size | 47.8 GB |
| Min ComfyUI version | 0.8.0 |
| Usage | 435 |
| Nodes | 23 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #143 | image | future_portrait.png |
| output | `SaveImage` #9 | image | image_firered_image_edit1_1.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `FireRed-Image-Edit-1.1-transformer.safetensors` | `diffusion_models` | [link](https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.1-ComfyUI/resolve/main/FireRed-Image-Edit-1.1-transformer.safetensors) |
| `FireRed-Image-Edit-1.0-Lightning-8steps-v1.0.safetensors` | `loras` | [link](https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.0-ComfyUI/resolve/main/FireRed-Image-Edit-1.0-Lightning-8steps-v1.0.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.0-ComfyUI/resolve/main/qwen_image_vae.safetensors) |

## Subgraphs

- **Image Edit (FireRed Image Edit 1.1)** (20 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 | comfy-core |
| `PrimitiveFloat` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `TextEncodeQwenImageEditPlus` | 2 | comfy-core |
| `CFGNorm` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `ResizeImageMaskNode` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Model Links

- [Hugging Face:Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/HunyuanVideo_1.5_repackaged](https://modelscope.cn/models/Comfy-Org/HunyuanVideo_1.5_repackaged)

**vae**

- [qwen_image_vae.safetensors](https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.0-ComfyUI/resolve/main/qwen_image_vae.safetensors) (242 MB)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**loras**

- [FireRed-Image-Edit-1.0-Lightning-8steps-v1.0.safetensors](https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.0-ComfyUI/resolve/main/FireRed-Image-Edit-1.0-Lightning-8steps-v1.0.safetensors) (810.2 MB)

**diffusion_models**

- [FireRed-Image-Edit-1.1-transformer.safetensors](https://huggingface.co/FireRedTeam/FireRed-Image-Edit-1.1-ComfyUI/resolve/main/FireRed-Image-Edit-1.1-transformer.safetensors) (38.05 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   ├── 📂 loras/
│   │   └── FireRed-Image-Edit-1.0-Lightning-8steps-v1.0.safetensors
│   └── 📂 diffusion_models/
│       └── FireRed-Image-Edit-1.1-transformer.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
