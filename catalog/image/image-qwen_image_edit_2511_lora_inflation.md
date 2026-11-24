# Image Inflation Effect with INFL8 LoRA

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image-qwen_image_edit_2511_lora_inflation)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image-qwen_image_edit_2511_lora_inflation-1.webp" width="360" alt="Image Inflation Effect with INFL8 LoRA image-qwen_image_edit_2511_lora_inflation-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image-qwen_image_edit_2511_lora_inflation-2.webp" width="360" alt="Image Inflation Effect with INFL8 LoRA image-qwen_image_edit_2511_lora_inflation-2.webp">

> Upload an image and specify a subject. Generate an inflated version of that subject using the INFL8 LoRA for Qwen Image Edit.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image-qwen_image_edit_2511_lora_inflation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image-qwen_image_edit_2511_lora_inflation.json)

## Details

| | |
|---|---|
| Name | `image-qwen_image_edit_2511_lora_inflation` |
| Category | Foundation › Image |
| Output | image |
| Models | Qwen-Image-Edit |
| Tags | Image, Image Edit |
| Type | open source |
| Date | 2026-01-30 |
| Author | PurzBeats |
| Download size | 47.3 GB |
| Min ComfyUI version | 0.5.0 |
| Usage | 19 |
| Nodes | 19 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #41 | image | inflation_lora_input.png |
| output | `SaveImage` #9 | image | image-qwen_image_edit_2511_lora_inflation.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_edit_2511_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2511_bf16.safetensors) |
| `Qwen_Image_Edit_2511-SYSTMS_INFL8.safetensors` | `loras` | [link](https://huggingface.co/systms/SYSTMS-INFL8-LoRA-Qwen-Image-Edit-2511/resolve/main/SYSTMS_INFL8_LoRA_Qwen_Image_Edit_2511.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Image Edit (Qwen 2511)** (16 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `FluxKontextMultiReferenceLatentMethod` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `TextEncodeQwenImageEditPlus` | 2 | comfy-core |
| `CFGNorm` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `FluxKontextImageScale` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `Note` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## About INFL8 LoRA
Note: INFL8 is a LoRA for Qwen Image Edit 2511 that lets you inflate elements within an image, using the prompt "inflate the [insert subject]"

- Source: [systms/SYSTMS-INFL8-LoRA-Qwen-Image-Edit-2511](https://huggingface.co/systms/SYSTMS-INFL8-LoRA-Qwen-Image-Edit-2511)

## Model Links

- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)
- [Hugging Face:Comfy-Org/Qwen-Image-Edit_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI)
- [Hugging Face:Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)
- [ModelScope:Comfy-Org/Qwen-Image-Edit_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image-Edit_ComfyUI)
- [ModelScope:Comfy-Org/HunyuanVideo_1.5_repackaged](https://modelscope.cn/models/Comfy-Org/HunyuanVideo_1.5_repackaged)

**vae**

- [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

**diffusion_models**

- [qwen_image_edit_2511_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2511_bf16.safetensors) (38.05 GB)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**loras**

- [Qwen_Image_Edit_2511-SYSTMS_INFL8.safetensors(renamed)](https://huggingface.co/systms/SYSTMS-INFL8-LoRA-Qwen-Image-Edit-2511/resolve/main/SYSTMS_INFL8_LoRA_Qwen_Image_Edit_2511.safetensors) (281.5 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   ├── 📂 diffusion_models/
│   │   └── qwen_image_edit_2511_bf16.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   └── 📂 loras/
│       └── Qwen_Image_Edit_2511-SYSTMS_INFL8.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>KSampler settings</summary>

You can test and find the best setting by yourself. The following table is for reference.
|   | Qwen | Comfy | lightning LoRA |
|--------|---------|------------|---------------------------|
| Steps  | 40      | 20         | 4                         |
| CFG    | 4.0     | 4.0       | 1.0                       |

By default, we use 20 steps as we just don't want it to take too long. Try 40 if you want a better result, but it will take longer.

</details>

<details><summary>Note</summary>

```text
The "Edit Model Reference Method" nodes above are not needed if you use Comfy files, but may be needed if you use repackaged ones from other people.
```

</details>
