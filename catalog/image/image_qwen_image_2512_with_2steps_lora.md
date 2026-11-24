# Qwen-Image 2512 Turbo

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_2512_with_2steps_lora-1.webp" width="360" alt="Qwen-Image 2512 Turbo image_qwen_image_2512_with_2steps_lora-1.webp">

> Qwen-Image 2512 Image generation with 2-steps Turbo LoRA. Input your text prompt to quickly produce a result, though some quality is sacrificed for speed.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_2512_with_2steps_lora.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_qwen_image_2512_with_2steps_lora.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image-2512)

## Details

| | |
|---|---|
| Name | `image_qwen_image_2512_with_2steps_lora` |
| Category | Foundation › Image |
| Media type | image |
| Models | Qwen-Image 2512 |
| Tags | Image, Text to Image, Turbo |
| Type | open source |
| Date | 2026-01-30 |
| Author | ComfyUI |
| Download size | 30.2 GB |
| Min ComfyUI version | 0.3.49 |
| Usage | 51 |
| Nodes | 13 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #123 | image | image_qwen_image_2512_with_2steps_lora.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_2512_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors) |
| `Wuli-Qwen-Image-2512-Turbo-LoRA-2steps-V1.0-bf16.safetensors` | `loras` | [link](https://huggingface.co/Wuli-art/Qwen-Image-2512-Turbo-LoRA-2-Steps/resolve/main/Wuli-Qwen-Image-2512-Turbo-LoRA-2steps-V1.0-bf16.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Aspect Ratios</summary>

- 1:1 : 1328x1328
- 16:9 : 1664x928
- 9:16 : 928x1664
- 4:3 : 1472x1104
- 3:4 : 1104x1472
- 3:2 : 1584x1056
- 2:3 : 1056x1584

</details>

<details><summary>Model links</summary>

## Model Links

- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)

### Alternative Repos

- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**diffusion_models**

- [qwen_image_2512_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors) (19.03 GB)

**vae**

- [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

**loras**

- [Wuli-Qwen-Image-2512-Turbo-LoRA-2steps-V1.0-bf16.safetensors](https://huggingface.co/Wuli-art/Qwen-Image-2512-Turbo-LoRA-2-Steps/resolve/main/Wuli-Qwen-Image-2512-Turbo-LoRA-2steps-V1.0-bf16.safetensors) (2.2 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   ├── 📂 diffusion_models/
│   │   └── qwen_image_2512_fp8_e4m3fn.safetensors
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   └── 📂 loras/
│       └── Wuli-Qwen-Image-2512-Turbo-LoRA-2steps-V1.0-bf16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
