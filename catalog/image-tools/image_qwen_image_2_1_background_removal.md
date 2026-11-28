# Remove Background: Qwen Image 2.1

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_qwen_image_2_1_background_removal)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_2_1_background_removal-1.webp" width="360" alt="Remove Background: Qwen Image 2.1 image_qwen_image_2_1_background_removal-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_2_1_background_removal-2.webp" width="360" alt="Remove Background: Qwen Image 2.1 image_qwen_image_2_1_background_removal-2.webp">

> Remove image backgrounds with Qwen Image 2.1, which natively supports 2K output and RGBA transparency for direct transparent results. It takes 1 input image and returns 1 background-free image plus a comparison view showing the before and after. Ideal for e-commerce product photos, profile pictures, and marketing graphics needing clean cutouts.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_2_1_background_removal.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_qwen_image_2_1_background_removal.json)

## Details

| | |
|---|---|
| Name | `image_qwen_image_2_1_background_removal` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | Qwen Image 2.1 |
| Tags | Remove Background, Int8 |
| Type | open source |
| Date | 2026-09-20 |
| Author | ComfyUI |
| Download size | 19.9 GB |
| Min ComfyUI version | 0.37.0 |
| Usage | 156 |
| Nodes | 14 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #470 | image | angry_broccoli.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_2.1_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_int8_convrot.safetensors) |
| `qwen3vl_8b_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors) |
| `qwen_image_2.1_vae_bf16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/vae/qwen_image_2.1_vae_bf16.safetensors) |

## Subgraphs

- **Image Edit (Qwen Image 2.1)** (9 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `CLIPLoader` | 1 |  |
| `ComfySwitchNode` | 1 |  |
| `EmptyLatentImage` | 1 |  |
| `ImageCompare` | 1 |  |
| `KSampler` | 1 |  |
| `LoadImage` | 1 |  |
| `QwenImage21Cache` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
| `TextEncodeQwenImage21` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Usage</summary>

## Size
Qwen Image 2.1 has native 2K (2048*2048) support for direct output.

- resolution is a total pixel budget (not width or height). Aspect ratio is preserved.
- Official default is 1024. The model supports up to 2048.
- This template starts at 0: no resize beyond a multiple of 32.
- Output follows image_1. Extra refs can differ in size or aspect.
- custom_size off: canvas comes from the encode latent (image_1).
- custom_size on: use ResolutionSelector width/height. Keep it close to the resized image_1 size, or the edit can shift.

## Reference images
- Up to 10 reference images (image_1 to image_10).
- Mention them in the prompt as `<image1>`, `<image2>`, ...
- image_1 is the edit target. The rest are references.

## Custom settings
If you need custom settings, enter or unpack the subgraph to edit it. See the [Subgraph](https://docs.comfy.org/interface/features/subgraph) guide.

## Parameters
- prompt: edit instruction. Use `<image1>` ... `<image10>`.
- negative_prompt: unused while cfg is 1.
- cfg: keep 1 for the Qwen Image 2.1 official path. Raise it only if you use a negative prompt.
- steps: Qwen Image 2.1 official pipeline uses about 40-50 with euler. This template starts at 25. More advanced samplers need fewer steps.

</details>

<details><summary>Note: Model links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Input Assets

- [angry_broccoli.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/angry_broccoli.png)


## Model Links

- [Hugging Face:Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1)
- [ModelScope:Comfy-Org/Qwen-Image-2.1](https://modelscope.cn/models/Comfy-Org/Qwen-Image-2.1)

**diffusion_models**

- [qwen_image_2.1_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_bf16.safetensors) (13.25 GB)
- [qwen_image_2.1_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_int8_convrot.safetensors) (6.76 GB)

**text_encoders**

- [qwen3vl_8b_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_bf16.safetensors) (16.33 GB)
- [qwen3vl_8b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors) (8.71 GB) 

**vae**

- [qwen_image_2.1_vae_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/vae/qwen_image_2.1_vae_bf16.safetensors) (644.2 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   ├── qwen_image_2.1_bf16.safetensors
│   │   └── qwen_image_2.1_int8_convrot.safetensors
│   ├── 📂 text_encoders/
│   │   ├── qwen3vl_8b_bf16.safetensors
│   │   └── qwen3vl_8b_int8_convrot.safetensors
│   └── 📂 vae/
│       └── qwen_image_2.1_vae_bf16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
