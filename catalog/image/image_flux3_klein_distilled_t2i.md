# FLUX 3 Image Klein Distilled: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_flux3_klein_distilled_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux3_klein_distilled_t2i-1.webp" width="360" alt="FLUX 3 Image Klein Distilled: Text to Image image_flux3_klein_distilled_t2i-1.webp">

> Generate images from text prompts using the distilled FLUX 3 Image Klein model, which runs efficiently in 15 sampling steps with no classifier-free guidance. Just describe what you want and receive one finished image. Ideal for rapid concept art, marketing visuals, and everyday creative ideation where speed matters.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux3_klein_distilled_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_flux3_klein_distilled_t2i.json)

## Details

| | |
|---|---|
| Name | `image_flux3_klein_distilled_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX 3 Image |
| Tags | Text to Image |
| Type | open source |
| Date | 2026-10-15 |
| Author | ComfyUI |
| Download size | 20.7 GB |
| Min ComfyUI version | 0.44.0 |
| Usage | 61 |
| Nodes | 21 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #9 | image | image_flux3_klein_distilled_t2i.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux3-image-klein-int8-convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/diffusion_models/flux3-image-klein-int8-convrot.safetensors) |
| `qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors` | `text_encoders` | [link](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/text_encoders/qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors) |
| `qwen3vl_4b_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/text_encoders/qwen3vl_4b_int8_convrot.safetensors) |
| `flux2-vae.safetensors` | `vae` | [link](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/vae/flux2-vae.safetensors) |

## Subgraphs

- **Text to Image (FLUX 3 Image Klein SD)** (14 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPLoader` | 2 |  |
| `CLIPTextEncode` | 2 |  |
| `MarkdownNote` | 2 |  |
| `PreviewAny` | 2 |  |
| `PrimitiveStringMultiline` | 2 |  |
| `ComfySwitchNode` | 1 |  |
| `CreateBoundingBoxes` | 1 |  |
| `EmptyFlux2LatentImage` | 1 |  |
| `Flux3LayoutPrompt` | 1 |  |
| `KSampler` | 1 |  |
| `ResolutionSelector` | 1 |  |
| `SaveImage` | 1 |  |
| `TextGenerateV2` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:black-forest-labs/flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy)

**text_encoders**

- [qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/blob/main/text_encoders/qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors)
- [qwen3vl_4b_int8_convrot.safetensors](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/text_encoders/qwen3vl_4b_int8_convrot.safetensors)

> **VRAM tip** — this template ships the quantised distilled checkpoint to keep the footprint small. With more than 24 GB of VRAM, use the bf16 weights instead: [`flux3-image-klein-bf16.safetensors`](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/diffusion_models/flux3-image-klein-bf16.safetensors).

**diffusion_models**

- [flux3-image-klein-int8-convrot.safetensors](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/diffusion_models/flux3-image-klein-int8-convrot.safetensors)

**vae**

- [flux2-vae.safetensors](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/vae/flux2-vae.safetensors)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   ├── qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors
│   │   └── qwen3vl_4b_int8_convrot.safetensors
│   ├── 📂 diffusion_models/
│   │   └── flux3-image-klein-int8-convrot.safetensors
│   └── 📂 vae/
│       └── flux2-vae.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>MarkdownNote</summary>

Plug the `STRING` output into the `prompt` input of the `Text to Image (FLUX 3 Image Klein SD)` node when you want to use bounding box

</details>
