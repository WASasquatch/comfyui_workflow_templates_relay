# Qwen Image: Gummy Animals LoRA

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_sugar_coated_gummy_style_qwen-1.webp" width="360" alt="Qwen Image: Gummy Animals LoRA template_sugar_coated_gummy_style_qwen-1.webp">

> Apply a Qwen Image LoRA to transform any subject into a sour gummy candy-style character. Enter an animal name in the prompt to generate a stylized, edible-looking creature.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_sugar_coated_gummy_style_qwen.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_sugar_coated_gummy_style_qwen.json)

## Details

| | |
|---|---|
| Name | `template_sugar_coated_gummy_style_qwen` |
| Category | Foundation › Image |
| Media type | image |
| Models | Qwen-Image |
| Tags | Text to Image, Image, LoRA |
| Type | open source |
| Date | 2026-03-30 |
| Author | enigmatic_e |
| Download size | 28.6 GB |
| Min ComfyUI version | 0.3.49 |
| Usage | 12 |
| Nodes | 15 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #60 | image | template_sugar_coated_gummy_style_qwen.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) |
| `gummycandy_qwen.safetensors` | `loras` | [link](https://huggingface.co/enigmatic/gummycandy_qwen/resolve/main/gummycandy_qwen.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Text to Image (Qwen-Image)** (12 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `Note` | 1 |  |
| `PreviewAny` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `StringConcatenate` | 1 |  |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
Enter a subject (e.g., dog, cat, horse) in the prompt field to generate a sour gummy candy–style character.
```

</details>

<details><summary>Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)
- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)

**vae**

- [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**diffusion_models**

- [qwen_image_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) (19.03 GB)

**loras**

- [gummycandy_qwen.safetensors](https://huggingface.co/enigmatic/gummycandy_qwen/resolve/main/gummycandy_qwen.safetensors) (562.8 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   ├── 📂 diffusion_models/
│   │   └── qwen_image_fp8_e4m3fn.safetensors
│   └── 📂 loras/
│       └── gummycandy_qwen.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
