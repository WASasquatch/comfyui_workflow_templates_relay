# Boogu image 0.1 Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_boogu_image_0_1_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_boogu_image_0_1_edit-1.webp" width="360" alt="Boogu image 0.1 Edit image_boogu_image_0_1_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_boogu_image_0_1_edit-2.webp" width="360" alt="Boogu image 0.1 Edit image_boogu_image_0_1_edit-2.webp">

> Edit images using Boogu's instruction-driven model, taking one input image and generating an edited output alongside a side-by-side comparison view.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_boogu_image_0_1_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_boogu_image_0_1_edit.json)

## Details

| | |
|---|---|
| Name | `image_boogu_image_0_1_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | Boogu |
| Tags | Image Edit |
| Type | open source |
| Date | 2026-06-23 |
| Author | ComfyUI |
| Download size | 19.8 GB |
| Min ComfyUI version | 0.26.0 |
| Usage | 44 |
| Nodes | 18 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #32 | image | tech_cowboy.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `boogu_image_edit_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Boogu-Image/resolve/main/diffusion_models/boogu_image_edit_fp8_scaled.safetensors) |
| `qwen3vl_8b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen3-VL/resolve/main/text_encoders/qwen3vl_8b_fp8_scaled.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/vae/ae.safetensors?download=true) |

## Subgraphs

- **Image Edit (Boogu Image Edit)** (10 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `BasicScheduler` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `EmptyLatentImage` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageCompare` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `ResizeImageMaskNode` | 1 | comfy-core |
| `SamplerCustom` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `TextEncodeBooguEdit` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Image Size</summary>

You can bypass the Resize Image/Mask node if you don't want to resize the input image.

Or you can update megapixels to `4` for high resolution; it depends on your hardware

</details>

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Boogu-Image](https://huggingface.co/Comfy-Org/Boogu-Image)
- [ModelScope:Comfy-Org/Boogu-Image](https://modelscope.cn/models/Comfy-Org/Boogu-Image)
- [Hugging Face:Comfy-Org/HiDream-I1_ComfyUI](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI)
- [ModelScope:Comfy-Org/HiDream-I1_ComfyUI](https://modelscope.cn/models/Comfy-Org/HiDream-I1_ComfyUI)
- [Hugging Face:Comfy-Org/Qwen3-VL](https://huggingface.co/Comfy-Org/Qwen3-VL)
- [ModelScope:Comfy-Org/Qwen3-VL](https://modelscope.cn/models/Comfy-Org/Qwen3-VL)

**diffusion_models**

- [boogu_image_edit_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Boogu-Image/resolve/main/diffusion_models/boogu_image_edit_fp8_scaled.safetensors) (9.61 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/HiDream-I1_ComfyUI/resolve/main/split_files/vae/ae.safetensors?download=true) (319.8 MB)

**text_encoders**

- [qwen3vl_8b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen3-VL/resolve/main/text_encoders/qwen3vl_8b_fp8_scaled.safetensors) (9.86 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── boogu_image_edit_fp8_scaled.safetensors
│   ├── 📂 vae/
│   │   └── ae.safetensors
│   └── 📂 text_encoders/
│       └── qwen3vl_8b_fp8_scaled.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: Boogu Image Edit</summary>

## Boogu-Image-0.1-Edit

[Boogu/Boogu-Image-0.1-Edit](https://huggingface.co/Boogu/Boogu-Image-0.1-Edit) — a 10B Apache-2.0 unified image editing model (TI2I). Describe the change you want in natural language; the model keeps the subject coherent while editing backgrounds, objects, styles, text, and more.

**Model page:** 
- [huggingface.co/Boogu/Boogu-Image-0.1-Edit](https://huggingface.co/Boogu/Boogu-Image-0.1-Edit)
- [Comfy-Org/Boogu-Image](https://huggingface.co/Comfy-Org/Boogu-Image)

## How to Use

1. Load a reference image in **Load Image** (one image only for now).
2. Write an editing instruction in the subgraph prompt, e.g. *"Keep the character unchanged, replace the desert background and scene. The model is on the dune."*
3. Run the workflow. Use **Image Compare** to check before/after.

## Resolution

Supported: **1K, 1.5K, 2K**. Results are most stable at **1K**; use the Resize node megapixels setting for higher res (up to ~4 MP depending on VRAM). 
## What It Can Do

- Object insert / replace / remove
- Attribute & material changes
- Background & scene replacement
- Style transfer (e.g. *"Change the style to a colored pencil drawing."*)
- Bilingual (CN/EN) in-image text editing

## Faster Alternative

Need speed? Try Boogu-Image-0.1-Edit-Turbo** — 4-step distilled variant (~1K res).

## Limitations

- Single reference image only (multi-image coming later)
- Strict identity/layout preservation can be unstable on hard edits
- Long or dense text edits may drift; small faces/limbs can artifact (FLUX VAE)

</details>
