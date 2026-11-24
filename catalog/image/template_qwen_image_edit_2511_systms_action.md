# Qwen Image Edit 2511: SYSTMS ACTION LoRA

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_qwen_image_edit_2511_systms_action-1.webp" width="360" alt="Qwen Image Edit 2511: SYSTMS ACTION LoRA template_qwen_image_edit_2511_systms_action-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_qwen_image_edit_2511_systms_action-2.webp" width="360" alt="Qwen Image Edit 2511: SYSTMS ACTION LoRA template_qwen_image_edit_2511_systms_action-2.webp">

> Upload your target image and use the trigger phrase "action the [thing]" (e.g., "action the scene"). Generate a toy or action figure version of your subject with articulated joints, plastic materials, and painted details.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_qwen_image_edit_2511_systms_action.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_qwen_image_edit_2511_systms_action.json)

## Details

| | |
|---|---|
| Name | `template_qwen_image_edit_2511_systms_action` |
| Category | Foundation › Image |
| Media type | image |
| Models | Qwen Image Edit 2511 |
| Tags | Image Edit, LoRA |
| Type | open source |
| Date | 2026-05-10 |
| Author | ingi |
| Download size | 48.1 GB |
| Min ComfyUI version | 0.5.0 |
| Distributions | local |
| Usage | 0 |
| Nodes | 27 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #223 | image | western_rider.png |
| output | `SaveImage` #9 | image | template_qwen_image_edit_2511_systms_action.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_edit_2511_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2511_bf16.safetensors) |
| `Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning/resolve/main/Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors) |
| `QWEN_EDIT_ACTION_V1.safetensors` | `loras` | [link](https://huggingface.co/systms/SYSTMS-ACTION-LoRA-Qwen-Image-Edit-2511/resolve/main/QWEN_EDIT_ACTION_V1.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Image Edit (Qwen-Image 2511 with LoRA)** (24 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 | comfy-core |
| `FluxKontextMultiReferenceLatentMethod` | 2 | comfy-core |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `PrimitiveFloat` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `TextEncodeQwenImageEditPlus` | 2 | comfy-core |
| `CFGNorm` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `FluxKontextImageScale` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `Note` | 1 |  |
| `PrimitiveBoolean` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

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

**loras**

- [Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning/resolve/main/Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors) (810.2 MB)
- [QWEN_EDIT_ACTION_V1.safetensors](https://huggingface.co/systms/SYSTMS-ACTION-LoRA-Qwen-Image-Edit-2511/resolve/main/QWEN_EDIT_ACTION_V1.safetensors) (281.5 MB)

**diffusion_models**

- [qwen_image_edit_2511_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2511_bf16.safetensors) (38.05 GB)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   ├── 📂 loras/
│   │   ├── Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors
│   │   └── QWEN_EDIT_ACTION_V1.safetensors
│   ├── 📂 diffusion_models/
│   │   └── qwen_image_edit_2511_bf16.safetensors
│   └── 📂 text_encoders/
│       └── qwen_2.5_vl_7b_fp8_scaled.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note</summary>

```text
The "Edit Model Reference Method" nodes above are not needed if you use Comfy files, but may be needed if you use repackaged ones from other people.
```

</details>
