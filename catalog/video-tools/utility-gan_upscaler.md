# Video Upscale: Real-ESRGAN

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility-gan_upscaler)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-gan_upscaler-1.webp" width="360" alt="Video Upscale: Real-ESRGAN utility-gan_upscaler-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-gan_upscaler-2.webp" width="360" alt="Video Upscale: Real-ESRGAN utility-gan_upscaler-2.webp">

> Upload a video to upscale it using a fast GAN model. The output resolution is determined by your chosen model (e.g., 2x or 4x). For best results, upscale first, then resize to your target resolution.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility-gan_upscaler.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility-gan_upscaler.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/image-upscale)

## Details

| | |
|---|---|
| Name | `utility-gan_upscaler` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | Real-ESRGAN |
| Tags | Video Upscale, API |
| Type | open source |
| Date | 2026-01-26 |
| Author | ComfyUI |
| Min ComfyUI version | 0.3.31 |
| Usage | 43 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #9 | video | gan_input.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `RealESRGAN_x4plus.safetensors` | `upscale_models` | [link](https://huggingface.co/Comfy-Org/Real-ESRGAN_repackaged/resolve/main/RealESRGAN_x4plus.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CreateVideo` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `ImageUpscaleWithModel` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
| `UpscaleModelLoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# GAN Upscaler Workflow

A fast approach for upscaling videos using GAN models. It can't create new detail like diffusion can, but it's much faster.

- **Model determines output size** — 2x models upscale 2x, 4x models upscale 4x
- **Tip:** Upscale 4x first, then use a resize node to bring it down to your target resolution

## Model Links

- [Hugging Face:Comfy-Org/Real-ESRGAN_repackaged](https://huggingface.co/Comfy-Org/Real-ESRGAN_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Real-ESRGAN_repackaged](https://modelscope.cn/models/Comfy-Org/Real-ESRGAN_repackaged)

**upscale_models**

- [RealESRGAN_x4plus.safetensors](https://huggingface.co/Comfy-Org/Real-ESRGAN_repackaged/resolve/main/RealESRGAN_x4plus.safetensors) (63.8 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 upscale_models/
│   │   ├── RealESRGAN_x4plus.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
