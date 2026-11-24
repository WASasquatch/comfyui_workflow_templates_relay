# Layer Decomposition: Qwen-Image-Layered

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_qwen_image_layered)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_layered-1.webp" width="360" alt="Layer Decomposition: Qwen-Image-Layered image_qwen_image_layered-1.webp">

> Decompose an image into editable RGBA layers for high-fidelity recolor, replace, resize, and reposition workflows using Qwen-Image-Layered.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_layered.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_qwen_image_layered.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image-layered)

## Details

| | |
|---|---|
| Name | `image_qwen_image_layered` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | Qwen-Image-Layered |
| Tags | Layer Decompose |
| Type | open source |
| Date | 2025-12-22 |
| Author | ComfyUI |
| Download size | 47.0 GB |
| Min ComfyUI version | 0.6.0 |
| Usage | 74 |
| Nodes | 33 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #74 | image | coastal_smiling_woman.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_layered_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-Layered_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_layered_bf16.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_layered_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-Layered_ComfyUI/resolve/main/split_files/vae/qwen_image_layered_vae.safetensors) |

## Subgraphs

- **Image to Layers (Qwen-Image-Layered)** (15 nodes)
- **Text to Layers (Qwen-Image-Layered)** (11 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 4 | comfy-core |
| `CLIPLoader` | 2 | comfy-core |
| `EmptyQwenImageLayeredLatentImage` | 2 | comfy-core |
| `KSampler` | 2 | comfy-core |
| `LatentCut` | 2 | comfy-core |
| `LatentCutToBatch` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `ModelSamplingAuraFlow` | 2 | comfy-core |
| `ReferenceLatent` | 2 | comfy-core |
| `SaveImage` | 2 | comfy-core |
| `UNETLoader` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageScaleToMaxDimension` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model links (for local user)</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Report issue

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

## Model Links

- [Hugging Face:Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged)
- [Hugging Face:Comfy-Org/Qwen-Image-Layered_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image-Layered_ComfyUI)

### Alternative Repos

- [ModelScope:Comfy-Org/HunyuanVideo_1.5_repackaged](https://modelscope.cn/models/Comfy-Org/HunyuanVideo_1.5_repackaged)
- [ModelScope:Comfy-Org/Qwen-Image-Layered_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image-Layered_ComfyUI)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**diffusion_models**

- [qwen_image_layered_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Layered_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_layered_bf16.safetensors) (38.05 GB)

**vae**

- [qwen_image_layered_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Layered_ComfyUI/resolve/main/split_files/vae/qwen_image_layered_vae.safetensors) (242.1 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   ├── 📂 diffusion_models/
│   │      └── qwen_image_layered_bf16.safetensors
│   └── 📂 vae/
│          └── qwen_image_layered_vae.safetensors
```

## FP8 

By default we are using bf16, it will require high VRAM, for fp8 please visit [qwen_image_layered_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Layered_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_layered_fp8mixed.safetensors)

Then update the **Load Diffusion model** node inside the [Subgraph](https://docs.comfy.org/interface/features/subgraph) to use it.

</details>

<details><summary>Note: Settings</summary>

## Sampler settings

This model is slow. The original sampling settings are steps: 50 and CFG: 4.0. It will at least double the generated time.

## Input size

For input size, 640px is recommended, 1024px for high-res

## Prompt(Optional)

The text prompt is intended to describe the overall content of the input image—including elements that may be partially occluded (e.g., you may specify the text hidden behind a foreground object). It is not designed to control the semantic content of individual layers explicitly.

</details>
