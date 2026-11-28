# Qwen Image Edit 2509

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_qwen_image_edit_2509)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_edit_2509-1.webp" width="360" alt="Qwen Image Edit 2509 image_qwen_image_edit_2509-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_edit_2509-2.webp" width="360" alt="Qwen Image Edit 2509 image_qwen_image_edit_2509-2.webp">

> Advanced image editing with multi-image support, improved consistency, and ControlNet integration.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_edit_2509.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_qwen_image_edit_2509.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit)

## Details

| | |
|---|---|
| Name | `image_qwen_image_edit_2509` |
| Category | Foundation › Image |
| Output | image |
| Models | Qwen-Image |
| Tags | ControlNet, Image Edit |
| Type | open source |
| Date | 2025-09-25 |
| Author | ComfyUI |
| Download size | 29.6 GB |
| Min ComfyUI version | 0.23.0 |
| Usage | 1550 |
| Nodes | 24 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #78 | image | image_qwen_image_edit_2509_input_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_edit_2509_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2509_fp8_e4m3fn.safetensors) |
| `Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Image Edit (Qwen 2509)** (21 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 |  |
| `MarkdownNote` | 2 |  |
| `PrimitiveFloat` | 2 |  |
| `PrimitiveInt` | 2 |  |
| `TextEncodeQwenImageEditPlus` | 2 | comfy-core |
| `CFGNorm` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `FluxKontextImageScale` | 1 |  |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model links</summary>

**Input Assets**
- [image_qwen_image_edit_2509_input_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/image_qwen_image_edit_2509_input_image.png) — required workflow input (`input/image_qwen_image_edit_2509_input_image.png`)

[Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit)

## Model Links

- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)
- [Hugging Face:Comfy-Org/Qwen-Image-Edit_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI)

### Alternative Repos

- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)
- [ModelScope:Comfy-Org/Qwen-Image-Edit_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image-Edit_ComfyUI)

You can find all the models on [Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/tree/main) and  [Comfy-Org/Qwen-Image-Edit_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI) 

**Diffusion model**

- [qwen_image_edit_2509_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2509_fp8_e4m3fn.safetensors) (19.03 GB)

**LoRA**

- [Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors) (810.2 MB)

**Text encoder**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**VAE**

- [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── qwen_image_edit_2509_fp8_e4m3fn.safetensors
│   ├── 📂 loras/
│   │   └── Qwen-Image-Lightning-4steps-V1.0.safetensors
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   └── 📂 text_encoders/
│       └── qwen_2.5_vl_7b_fp8_scaled.safetensors
```

## Report issue
If you have any problems running this workflow, please report template-related issues via this link: [report the template issue here](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: KSampler settings</summary>

You can test and find the best setting by yourself. The following table is for reference.
| Parameters   | Qwen Team | Comfy Original | with 4steps LoRA |
|--------|---------|------------|---------------------------|
| Steps  | 50      | 20         | 4                         |
| CFG    | 4.0     | 2.5        | 1.0                       |

</details>
