# Image Relight

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_qwen_image_edit_2509_relight)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_edit_2509_relight-1.webp" width="360" alt="Image Relight image_qwen_image_edit_2509_relight-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_edit_2509_relight-2.webp" width="360" alt="Image Relight image_qwen_image_edit_2509_relight-2.webp">

> Relight images using Qwen-Image-Edit with LoRA support.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_edit_2509_relight.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_qwen_image_edit_2509_relight.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit)

## Details

| | |
|---|---|
| Name | `image_qwen_image_edit_2509_relight` |
| Category | Foundation › Image |
| Output | image |
| Models | Qwen-Image-Edit |
| Tags | Image Edit, Relight |
| Type | open source |
| Date | 2025-12-15 |
| Author | ComfyUI |
| Download size | 29.6 GB |
| Min ComfyUI version | 0.3.60 |
| Usage | 56 |
| Nodes | 18 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #11 | image | warm_living_room.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_edit_2509_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2509_fp8_e4m3fn.safetensors) |
| `Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors) |
| `Qwen-Image-Edit-2509-Relight.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/loras/Qwen-Image-Edit-2509-Relight.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Image Edit (Qwen 2509 with LoRA)** (13 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `TextEncodeQwenImageEditPlus` | 2 | comfy-core |
| `CFGNorm` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `FluxKontextImageScale` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `StringConcatenate` | 1 |  |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>For Local User</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Report issue

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

## Model Links

- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)
- [Hugging Face:Comfy-Org/Qwen-Image-Edit_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI)

### Alternative Repos

- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)
- [ModelScope:Comfy-Org/Qwen-Image-Edit_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image-Edit_ComfyUI)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**loras**

- [Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors) (810.2 MB)
- [Qwen-Image-Edit-2509-Relight.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/loras/Qwen-Image-Edit-2509-Relight.safetensors) (225.2 MB)

**diffusion_models**

- [qwen_image_edit_2509_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2509_fp8_e4m3fn.safetensors) (19.03 GB)

**vae**

- [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   ├── 📂 loras/
│   │      ├── Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors
│   │      └── Qwen-Image-Edit-2509-Relight.safetensors
│   ├── 📂 diffusion_models/
│   │      └── qwen_image_edit_2509_fp8_e4m3fn.safetensors
│   └── 📂 vae/
│          └── qwen_image_vae.safetensors
```

</details>
