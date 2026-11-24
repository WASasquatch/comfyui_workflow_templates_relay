# LongCat Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_longcat_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_longcat_image_edit-1.webp" width="360" alt="LongCat Image Edit image_longcat_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_longcat_image_edit-2.webp" width="360" alt="LongCat Image Edit image_longcat_image_edit-2.webp">

> Edit images using the LongCat-Image-Edit model. Supports bilingual instructions for global, local, text, and reference-guided editing while preserving visual consistency.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_longcat_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_longcat_image_edit.json)

## Details

| | |
|---|---|
| Name | `image_longcat_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | LongCat Image Edit |
| Tags | Image, Image Edit |
| Type | open source |
| Date | 2026-03-23 |
| Author | ComfyUI |
| Download size | 20.7 GB |
| Min ComfyUI version | 0.16.0 |
| Distributions | local |
| Usage | 36 |
| Nodes | 18 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #13 | image | steel_in_the_mist.png |
| output | `SaveImage` #9 | image | image_longcat_image_edit.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `longcat_image_edit_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/TalmajM/LongCat-Image-Edit_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/longcat_image_edit_bf16.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Image Edit (LongCat Image Edit)** (13 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `FluxGuidance` | 2 | comfy-core |
| `FluxKontextMultiReferenceLatentMethod` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `TextEncodeQwenImageEdit` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `ImageCompare` | 1 |  |
| `ImageScaleToTotalPixels` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>About Settings</summary>

Try 50 steps to get better quality, but it will take longer.

</details>

<details><summary>MarkdownNote</summary>

## Model Links

- [Hugging Face:Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo)
- [ModelScope:Comfy-Org/z_image_turbo](https://modelscope.cn/models/Comfy-Org/z_image_turbo)
- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)
- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

**diffusion_models**

- [longcat_image_edit_bf16.safetensors](https://huggingface.co/TalmajM/LongCat-Image-Edit_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/longcat_image_edit_bf16.safetensors) (11.68 GB)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   └── ae.safetensors
│   ├── 📂 diffusion_models/
│   │   └── longcat_image_edit_bf16.safetensors
│   └── 📂 text_encoders/
│       └── qwen_2.5_vl_7b_fp8_scaled.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
