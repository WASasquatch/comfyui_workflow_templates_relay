# Qwen Image: Illustration LoRA

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_qwen_image_illustration_lora)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_qwen_image_illustration_lora-1.webp" width="360" alt="Qwen Image: Illustration LoRA template_qwen_image_illustration_lora-1.webp">

> A t2v workflows for a style LoRA built on Qwen-Image. Produces images spanning cute anime character design, European bande dessinee, indie risograph prints, storybook watercolor, retro shoujo manga, and graphic novel illustration.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_qwen_image_illustration_lora.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_qwen_image_illustration_lora.json)

## Details

| | |
|---|---|
| Name | `template_qwen_image_illustration_lora` |
| Category | Foundation › Image |
| Output | image |
| Models | Qwen-Image |
| Tags | Text to Image, LoRA |
| Type | open source |
| Date | 2026-03-30 |
| Author | ComfyUI |
| Download size | 28.7 GB |
| Min ComfyUI version | 0.3.49 |
| Usage | 70 |
| Nodes | 12 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #60 | image | template_qwen_image_illustration_lora.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) |
| `illustration-1.0-qwen-image.safetensors` | `loras` | [link](https://huggingface.co/alvdansen/illustration-1.0-qwen-image/resolve/main/illustration-1.0-qwen-image.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Text to Image (Qwen-Image with LoRA)** (10 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

- [About Qwen-Image](https://docs.comfy.org/tutorials/image/qwen/qwen-image) 

## Alvdansen Illustration v1.0 (Qwen Images)

- [Alvdansen Illustration 1.0 -- Qwen-Image](https://huggingface.co/alvdansen/illustration-1.0-qwen-image)

A style LoRA for Qwen-Image trained on 244 curated illustration and anime reference images across diverse visual styles. Produces images spanning cute anime character design, European bande dessinee, indie risograph prints, storybook watercolor, retro shoujo manga, and graphic novel illustration.

---

**Recommended Inference Settings**

```
Sampler: euler
Scheduler: simple
CFG: 3.5
Steps: 45 (30-60 works well)
LoRA strength: 0.8-1.0

```
---

## Model Links

- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)

### Alternative Repos

- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)

**vae**

- [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**diffusion_models**

- [qwen_image_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) (19.03 GB)

**loras**

- [illustration-1.0-qwen-image.safetensors](https://huggingface.co/alvdansen/illustration-1.0-qwen-image/resolve/main/illustration-1.0-qwen-image.safetensors) (738.5 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   ├── 📂 diffusion_models/
│   │   └── qwen_image_fp8_e4m3fn.safetensors
│   └── 📂 loras/
│       └── illustration-1.0-qwen-image.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
