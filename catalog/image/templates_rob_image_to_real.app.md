# Illustration to Realism

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_rob_image_to_real.app)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_rob_image_to_real.app-1.webp" width="360" alt="Illustration to Realism templates_rob_image_to_real.app-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_rob_image_to_real.app-2.webp" width="360" alt="Illustration to Realism templates_rob_image_to_real.app-2.webp">

> Input an illustration and generate a realistic version using Qwen Image Edit 2509 with Anything2Real LoRA.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_rob_image_to_real.app.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_rob_image_to_real.app.json)

## Details

| | |
|---|---|
| Name | `templates_rob_image_to_real.app` |
| Category | Foundation › Image |
| Output | image |
| Models | Qwen-Image-Edit |
| Tags | Image, Image Edit, LoRA |
| Type | open source |
| Date | 2026-03-09 |
| Author | hellorob |
| Download size | 29.4 GB |
| Min ComfyUI version | 0.9.0 |
| Distributions | cloud |
| Usage | 76 |
| Nodes | 26 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #14 | image | templates_rob_image_to_real-input.png |
| output | `SaveImage` #18 | image | templates_rob_image_to_real.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_edit_2509_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2509_fp8_e4m3fn.safetensors) |
| `Qwen-Image-Edit-2509-Anything2RealAlpha.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/loras/Qwen-Image-Edit-2509-Anything2RealAlpha.safetensors) |
| `Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Image Edit (Qwen 2509 with LoRA)** (22 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 | comfy-core |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `PrimitiveFloat` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `TextEncodeQwenImageEditPlus` | 2 | comfy-core |
| `CFGNorm` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `FluxKontextImageScale` | 1 | comfy-core |
| `ImageCompare` | 1 |  |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>For local User</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model links

- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)
- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)
- [Hugging Face:Comfy-Org/Qwen-Image-Edit_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI)
- [ModelScope:Comfy-Org/Qwen-Image-Edit_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image-Edit_ComfyUI)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**loras**

- [Qwen-Image-Edit-2509-Anything2RealAlpha.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/loras/Qwen-Image-Edit-2509-Anything2RealAlpha.safetensors) (581.4 MB)
- [Qwen-Image-Edit-2509-Lightning-8steps-V1.0-bf16.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-8steps-V1.0-bf16.safetensors) (810.2 MB)

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
│   │      ├── Qwen-Image-Edit-2509-Anything2RealAlpha.safetensors
│   │      └── Qwen-Image-Edit-2509-Lightning-8steps-V1.0-bf16.safetensors
│   ├── 📂 diffusion_models/
│   │      └── qwen_image_edit_2509_fp8_e4m3fn.safetensors
│   └── 📂 vae/
│          └── qwen_image_vae.safetensors
```
## Report issue

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: KSampler settings</summary>

You can test and find the best setting by yourself. The following table is for reference.
| Parameters   | Qwen Team | Comfy Original | with 4steps LoRA |
|--------|---------|------------|---------------------------|
| Steps  | 50      | 20         | 4                         |
| CFG    | 4.0     | 2.5        | 1.0                       |

</details>
