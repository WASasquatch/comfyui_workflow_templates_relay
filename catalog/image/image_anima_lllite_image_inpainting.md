# Anima Lllite: Image Inpainting

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_anima_lllite_image_inpainting)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_anima_lllite_image_inpainting-1.webp" width="360" alt="Anima Lllite: Image Inpainting image_anima_lllite_image_inpainting-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_anima_lllite_image_inpainting-2.webp" width="360" alt="Anima Lllite: Image Inpainting image_anima_lllite_image_inpainting-2.webp">

> Inpaint anime images with Anima LLLite, a lightweight ControlNet variant that applies low-rank corrections for precise mask-based editing. Input 1 image and receive 1 inpainted output plus a comparison view. Ideal for fixing character details, removing unwanted objects from anime scenes, and seamless background restoration.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_anima_lllite_image_inpainting.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_anima_lllite_image_inpainting.json)

## Details

| | |
|---|---|
| Name | `image_anima_lllite_image_inpainting` |
| Category | Foundation › Image |
| Output | image |
| Models | Anima |
| Tags | Anime, Inpainting |
| Type | open source |
| Date | 2026-07-21 |
| Author | ComfyUI |
| Download size | 5.4 GB |
| Min ComfyUI version | 0.29.0 |
| Usage | 101 |
| Nodes | 28 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #91 | image | goat_horned_spirit_girl.png |
| output | `SaveImage` #46 | image | image_anima_lllite_image_inpainting.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `anima-base-v1.0.safetensors` | `diffusion_models` | [link](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/diffusion_models/anima-base-v1.0.safetensors) |
| `anima-turbo-lora-v0.2.safetensors` | `loras` | [link](https://huggingface.co/circlestone-labs/Anima-Official-LoRAs/resolve/main/anima-turbo-lora-v0.2.safetensors) |
| `anima-lllite-inpainting-v2.safetensors` | `model_patches` | [link](https://huggingface.co/Comfy-Org/Anima-LLLite/resolve/main/model_patches/anima-lllite-inpainting-v2.safetensors) |
| `qwen_3_06b_base.safetensors` | `text_encoders` | [link](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/text_encoders/qwen_3_06b_base.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Control to Image (Anima LLLite )** (19 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 |  |
| `MarkdownNote` | 3 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `PrimitiveFloat` | 2 |  |
| `PrimitiveInt` | 2 |  |
| `AnimaLLLiteApply` | 1 |  |
| `CLIPLoader` | 1 | comfy-core |
| `EmptyLatentImage` | 1 | comfy-core |
| `ImageCompare` | 1 |  |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 |  |
| `LoraLoaderModelOnly` | 1 |  |
| `MaskPreview` | 1 |  |
| `ModelPatchLoader` | 1 |  |
| `Painter` | 1 |  |
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

**text_encoders**

- [qwen_3_06b_base.safetensors](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/text_encoders/qwen_3_06b_base.safetensors) (1.11 GB)

**vae**

- [qwen_image_vae.safetensors](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

**diffusion_models**

- [anima-base-v1.0.safetensors](https://huggingface.co/circlestone-labs/Anima/resolve/main/split_files/diffusion_models/anima-base-v1.0.safetensors) (3.89 GB)

**model_patches**

- [anima-lllite-inpainting-v2.safetensors](https://huggingface.co/Comfy-Org/Anima-LLLite/resolve/main/model_patches/anima-lllite-inpainting-v2.safetensors) (62.7 MB)

**loras**

- [anima-turbo-lora-v0.2.safetensors](https://huggingface.co/circlestone-labs/Anima-Official-LoRAs/resolve/main/anima-turbo-lora-v0.2.safetensors) (142 MB)


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
│   │   └── anima-lllite-inpainting-v2.safetensors
│   └── 📂 loras/
│       └── anima-turbo-lora-v0.2.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: Draw Mask</summary>

Use the Painter node to draw mask

</details>

<details><summary>MarkdownNote</summary>

Resize the input image if it's oversized (like over 1024*1024)

</details>
