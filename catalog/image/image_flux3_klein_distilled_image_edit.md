# FLUX 3 Image Klein Distilled: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_flux3_klein_distilled_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux3_klein_distilled_image_edit-1.webp" width="360" alt="FLUX 3 Image Klein Distilled: Image Edit image_flux3_klein_distilled_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux3_klein_distilled_image_edit-2.webp" width="360" alt="FLUX 3 Image Klein Distilled: Image Edit image_flux3_klein_distilled_image_edit-2.webp">

> Edit an existing image with FLUX 3 Image Klein by pairing one input image with one text prompt, producing a single edited result and a side-by-side comparison view. Ideal for targeted retouching, restyling a photo, or swapping details while keeping the rest of the scene intact.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux3_klein_distilled_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_flux3_klein_distilled_image_edit.json)

## Details

| | |
|---|---|
| Name | `image_flux3_klein_distilled_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX 3 Image |
| Tags | Image Edit |
| Type | open source |
| Date | 2026-10-15 |
| Author | ComfyUI |
| Download size | 20.0 GB |
| Min ComfyUI version | 0.44.0 |
| Usage | 274 |
| Nodes | 24 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #11 | image | woman_gold_earring_teal_top_portrait.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux3-image-klein-int8-convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/diffusion_models/flux3-image-klein-int8-convrot.safetensors) |
| `qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors` | `text_encoders` | [link](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/text_encoders/qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors) |
| `qwen3vl_4b_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/text_encoders/qwen3vl_4b_int8_convrot.safetensors) |
| `flux2-vae.safetensors` | `vae` | [link](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/vae/flux2-vae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `CLIPLoader` | 2 |  |
| `PreviewAny` | 2 |  |
| `BatchImagesNode` | 1 |  |
| `CLIPTextEncode` | 1 |  |
| `ComfySwitchNode` | 1 |  |
| `ConditioningZeroOut` | 1 |  |
| `CreateBoundingBoxes` | 1 |  |
| `EmptyFlux2LatentImage` | 1 |  |
| `Flux3LayoutPrompt` | 1 |  |
| `ImageCompare` | 1 |  |
| `KSampler` | 1 |  |
| `LoadImage` | 1 |  |
| `PrimitiveStringMultiline` | 1 |  |
| `ReferenceMultiLatent` | 1 |  |
| `SaveImage` | 1 |  |
| `TextGenerateV2` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>Notes</summary>

## FLUX 3 Image Klein: editing

Same files and sampler settings as text-to-image (50 steps, cfg 3.5, euler / simple).

**References**: plug more input image to the `Set Reference Multi Latent` node, the first one is `<ref_image_0>` in the prompt, the next `<ref_image_1>`, and so on. Add every reference to **both** the positive and the negative, as the reference pipeline does.

**Size**: the reference is scaled to ~1 MP here and the output latent takes its size. BFL's pipeline keeps references at native size (up to ~16 MP): raise the megapixels for more reference detail at a higher cost.

**Prompting**: write a full caption of the result, with the edit folded in.

</details>

<details><summary>MarkdownNote</summary>

## Input Asset

- [woman_gold_earring_teal_top_portrait.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/woman_gold_earring_teal_top_portrait.png)

## Model Links

- [Hugging Face:black-forest-labs/flux-3-image-klein-comfy](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy)

> **VRAM tip** — this template ships the quantised distilled checkpoint to keep the footprint small. With more than 24 GB of VRAM, use the bf16 weights instead: [`flux3-image-klein-bf16.safetensors`](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/diffusion_models/flux3-image-klein-bf16.safetensors).

**diffusion_models**

- [flux3-image-klein-int8-convrot.safetensors](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/diffusion_models/flux3-image-klein-int8-convrot.safetensors)

**text_encoders**

- [qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/blob/main/text_encoders/qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors)
- [qwen3vl_4b_int8_convrot.safetensors](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/text_encoders/qwen3vl_4b_int8_convrot.safetensors)

**vae**

- [flux2-vae.safetensors](https://huggingface.co/black-forest-labs/flux-3-image-klein-comfy/resolve/main/vae/flux2-vae.safetensors)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── flux3-image-klein-int8-convrot.safetensors
│   ├── 📂 text_encoders/
│   │   ├── qwen3.5_9b_flux3_prompt_upsampler_w4a8.safetensors
│   │   └── qwen3vl_4b_int8_convrot.safetensors
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

Use `Empty Flux 2 Latent` node to customize image size

`Create Bounding Boxes` node for node for creating prompts for precise editing

</details>
