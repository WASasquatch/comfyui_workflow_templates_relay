# Anima Lllite: Depth Control to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_anima_lllite_depth_control_to_image-1.webp" width="360" alt="Anima Lllite: Depth Control to Image image_anima_lllite_depth_control_to_image-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_anima_lllite_depth_control_to_image-2.webp" width="360" alt="Anima Lllite: Depth Control to Image image_anima_lllite_depth_control_to_image-2.webp">

> Generate anime-style illustrations from a depth map using the Anima LLLite model, which applies a lightweight ControlNet correction for precise spatial control. Input 1 image to produce 2 image outputs plus a comparison view. Ideal for 3D scene reconstruction, VFX depth passes, and AR asset preparation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_anima_lllite_depth_control_to_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_anima_lllite_depth_control_to_image.json)

## Details

| | |
|---|---|
| Name | `image_anima_lllite_depth_control_to_image` |
| Category | Foundation › Image |
| Media type | image |
| Models | Anima |
| Tags | Anime |
| Type | open source |
| Date | 2026-07-21 |
| Author | ComfyUI |
| Download size | 6.6 GB |
| Min ComfyUI version | 0.29.0 |
| Usage | 27 |
| Nodes | 29 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #91 | image | anima_depth_ref.png |
| output | `SaveImage` #46 | image | image_anima_lllite_depth_control_to_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `anima-base-v1.0.safetensors` | `diffusion_models` | [link](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/diffusion_models/anima-base-v1.0.safetensors) |
| `depth_anything_3_mono_large.safetensors` | `geometry_estimation` | [link](https://huggingface.co/Comfy-Org/Depth-Anything-3/resolve/main/geometry_estimation/depth_anything_3_mono_large.safetensors) |
| `anima-turbo-lora-v0.2.safetensors` | `loras` | [link](https://huggingface.co/circlestone-labs/Anima-Official-LoRAs/resolve/main/anima-turbo-lora-v0.2.safetensors) |
| `anima-lllite-depth-1.safetensors` | `model_patches` | [link](https://huggingface.co/Comfy-Org/Anima-LLLite/resolve/main/model_patches/anima-lllite-depth-1.safetensors) |
| `qwen_3_06b_base.safetensors` | `text_encoders` | [link](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/text_encoders/qwen_3_06b_base.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Control to Image (Anima LLLite )** (19 nodes)
- **Image Depth Estimation (Depth Anything 3)** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `PrimitiveFloat` | 2 |  |
| `PrimitiveInt` | 2 |  |
| `AnimaLLLiteApply` | 1 |  |
| `CLIPLoader` | 1 | comfy-core |
| `DA3Inference` | 1 | comfy-core |
| `DA3Render` | 1 | comfy-core |
| `EmptyLatentImage` | 1 | comfy-core |
| `GetImageSize` | 1 |  |
| `ImageCompare` | 1 |  |
| `KSampler` | 1 | comfy-core |
| `LoadDA3Model` | 1 | comfy-core |
| `LoadImage` | 1 |  |
| `LoraLoaderModelOnly` | 1 |  |
| `MarkdownNote` | 1 |  |
| `ModelPatchLoader` | 1 |  |
| `PreviewImage` | 1 |  |
| `PrimitiveBoolean` | 1 |  |
| `ResizeImageMaskNode` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Anima-LLLite](https://huggingface.co/Comfy-Org/Anima-LLLite)
- [ModelScope:Comfy-Org/Anima-LLLite](https://modelscope.cn/models/Comfy-Org/Anima-LLLite)
- [Hugging Face:Comfy-Org/Depth-Anything-3](https://huggingface.co/Comfy-Org/Depth-Anything-3)
- [ModelScope:Comfy-Org/Depth-Anything-3](https://modelscope.cn/models/Comfy-Org/Depth-Anything-3)

**text_encoders**

- [qwen_3_06b_base.safetensors](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/text_encoders/qwen_3_06b_base.safetensors) (1.11 GB)

**vae**

- [qwen_image_vae.safetensors](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

**diffusion_models**

- [anima-base-v1.0.safetensors](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/diffusion_models/anima-base-v1.0.safetensors) (3.89 GB)

**model_patches**

- [anima-lllite-depth-1.safetensors](https://huggingface.co/Comfy-Org/Anima-LLLite/resolve/main/model_patches/anima-lllite-depth-1.safetensors) (7.5 MB)

**loras**

- [anima-turbo-lora-v0.2.safetensors](https://huggingface.co/circlestone-labs/Anima-Official-LoRAs/resolve/main/anima-turbo-lora-v0.2.safetensors) (142 MB)

**geometry_estimation**

- [depth_anything_3_mono_large.safetensors](https://huggingface.co/Comfy-Org/Depth-Anything-3/resolve/main/geometry_estimation/depth_anything_3_mono_large.safetensors) (1.24 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   └── qwen_3_06b_base.safetensors
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   ├── 📂 diffusion_models/
│   │   └── anima-base-v1.0.safetensors
│   ├── 📂 model_patches/
│   │   └── anima-lllite-depth-1.safetensors
│   ├── 📂 loras/
│   │   └── anima-turbo-lora-v0.2.safetensors
│   └── 📂 geometry_estimation/
│       └── depth_anything_3_mono_large.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
