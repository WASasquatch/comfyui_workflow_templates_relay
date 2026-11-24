# Image Upscale: Z-Image-Turbo 2K

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_z_image_turbo_2k_upscaler.app)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_z_image_turbo_2k_upscaler.app-1.webp" width="360" alt="Image Upscale: Z-Image-Turbo 2K utility_z_image_turbo_2k_upscaler.app-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_z_image_turbo_2k_upscaler.app-2.webp" width="360" alt="Image Upscale: Z-Image-Turbo 2K utility_z_image_turbo_2k_upscaler.app-2.webp">

> Upload an image to upscale it to 2K resolution using the Z-Image-Turbo model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_z_image_turbo_2k_upscaler.app.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_z_image_turbo_2k_upscaler.app.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/image-upscale)

## Details

| | |
|---|---|
| Name | `utility_z_image_turbo_2k_upscaler.app` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | Z-Image-Turbo |
| Tags | Image Upscale |
| Type | open source |
| Date | 2026-02-19 |
| Author | hellorob |
| Download size | 19.3 GB |
| Min ComfyUI version | 0.9.0 |
| Usage | 291 |
| Nodes | 19 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #77 | image | fighter_jet.png |
| output | `SaveImage` #9 | image | utility_z_image_turbo_2k_upscaler.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `z_image_turbo_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) |
| `qwen_3_4b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) |
| `RealESRGAN_x4plus.safetensors` | `upscale_models` | [link](https://huggingface.co/Comfy-Org/Real-ESRGAN_repackaged/resolve/main/RealESRGAN_x4plus.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Image Upscale(Z-image-Turbo)** (13 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `ImageCompare` | 1 | comfy-core |
| `ImageScaleBy` | 1 | comfy-core |
| `ImageScaleToTotalPixels` | 1 | comfy-core |
| `ImageUpscaleWithModel` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `UpscaleModelLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>About Denoise Setting</summary>

### Denoise Parameter Explained
The denoise value controls the creative freedom of the sampler. Lower values keep outputs closer to the input; higher values allow the model to reinterpret and add more details.

| Style | Value Range | Effect |
|------|-------------|--------|
| Subtle Creativity | 0.15 – 0.25 | Output stays close to input |
| High Creativity | 0.25 – 0.35 | More reinterpretation & details |

---

## Note
Denoise values above `0.35` may introduce artifacts. To maintain coherence at high denoise, use a **detailed image caption** as your prompt to provide the model with more context.

**Comparison example at `0.5` denoise:**  
- **Prompt A (minimal):** `masterpiece, 8k`  
- **Prompt B (detailed caption):** `A low-angle head-on view of an F-22 Raptor... masterpiece, 8k`

Using a detailed prompt will result in significantly more stable and coherent outputs.

</details>

<details><summary>Model Links</summary>

## Model Links

- [Hugging Face:Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo)
- [ModelScope:Comfy-Org/z_image_turbo](https://modelscope.cn/models/Comfy-Org/z_image_turbo)
- [Hugging Face:Comfy-Org/Real-ESRGAN_repackaged](https://huggingface.co/Comfy-Org/Real-ESRGAN_repackaged)
- [ModelScope:Comfy-Org/Real-ESRGAN_repackaged](https://modelscope.cn/models/Comfy-Org/Real-ESRGAN_repackaged)

**diffusion_models**

- [z_image_turbo_bf16.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) (11.46 GB)

**text_encoders**

- [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) (7.49 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

**upscale_models**

- [RealESRGAN_x4plus.safetensors](https://huggingface.co/Comfy-Org/Real-ESRGAN_repackaged/resolve/main/RealESRGAN_x4plus.safetensors) (63.8 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── z_image_turbo_bf16.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen_3_4b.safetensors
│   ├── 📂 vae/
│   │   └── ae.safetensors
│   └── 📂 upscale_models/
│       └── RealESRGAN_x4plus.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note</summary>

Image Compare is now only available under Nodes 2.0. Open menu -> Nodes 2.0 to switch

</details>
