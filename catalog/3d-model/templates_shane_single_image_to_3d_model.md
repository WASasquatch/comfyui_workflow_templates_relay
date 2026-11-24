# Single Image to 3D model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_shane_single_image_to_3d_model)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_shane_single_image_to_3d_model-1.webp" width="360" alt="Single Image to 3D model templates_shane_single_image_to_3d_model-1.webp">

> Use one frontal image to generate a consistent and highly detailed 3D model. Model used: Multiangle QWEN Edit + Hunyuan 3D

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_shane_single_image_to_3d_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_shane_single_image_to_3d_model.json)

## Details

| | |
|---|---|
| Name | `templates_shane_single_image_to_3d_model` |
| Category | Foundation › 3D Model |
| Output | image |
| Models | Hunyuan3D, Qwen-Image-Edit |
| Tags | API, 3D, Image to 3D |
| Type | API |
| Date | 2026-03-04 |
| Author | shane |
| Download size | 54.8 GB |
| Min ComfyUI version | 0.23.0 |
| Usage | 17 |
| Nodes | 21 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #119 | image | lucky_cat_sculpture_front.png |
| output | `SaveImage` #118 | image | lucky_cat_sculpture_back.png |

## Custom nodes required

- [comfyui-qwenmultiangle](https://registry.comfy.org/nodes/comfyui-qwenmultiangle)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_edit_2511_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2511_bf16.safetensors) |
| `Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning/resolve/main/Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors) |
| `qwen-image-edit-2511-multiple-angles-lora.safetensors` | `loras` | [link](https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA/resolve/main/qwen-image-edit-2511-multiple-angles-lora.safetensors) |
| `qwen_2.5_vl_7b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanImage_2.1_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Image Edit(Qwen Image 2511 with LoRA)** (16 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `FluxKontextMultiReferenceLatentMethod` | 2 | comfy-core |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `TextEncodeQwenImageEditPlus` | 2 | comfy-core |
| `CFGNorm` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `FluxKontextImageScale` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `Preview3D` | 1 | comfy-core |
| `QwenMultiangleCameraNode` | 1 | comfyui-qwenmultiangle |
| `SaveImage` | 1 | comfy-core |
| `TencentImageToModelNode` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>KSampler settings</summary>

You can test and find the best setting by yourself. The following table is for reference.
|   | Qwen | Comfy | lightning LoRA |
|--------|---------|------------|---------------------------|
| Steps  | 40      | 20         | 4                         |
| CFG    | 4.0     | 4.0       | 1.0                       |

By default, we use 20 steps as we just don't want it to take too long. Try 40 if you want a better result, but it will take longer.

</details>
