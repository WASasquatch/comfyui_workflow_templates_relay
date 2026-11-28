# FLUX.2 [Klein] 9B: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_flux2_klein_image_edit_9b_base)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_9b_base-1.webp" width="360" alt="FLUX.2 [Klein] 9B: Image Edit image_flux2_klein_image_edit_9b_base-1.webp">

> BFL undistilled foundation model. Maximum flexibility and control. Great for fine-tuning.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_9b_base.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_flux2_klein_image_edit_9b_base.json)
- [Tutorial](https://docs.comfy.org/tutorials/flux/flux-2-klein)

## Details

| | |
|---|---|
| Name | `image_flux2_klein_image_edit_9b_base` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX, FLUX.2 Klein |
| Tags | Image, Text to Image |
| Type | open source |
| Date | 2026-01-16 |
| Author | ComfyUI |
| Download size | 18.0 GB |
| Min ComfyUI version | 0.9.2 |
| Usage | 425 |
| Nodes | 43 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #76 | image | car_interior_white.jpeg |
| input | `LoadImage` #81 | image | comfy_logo_blue.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux-2-klein-base-9b-fp8.safetensors` | `diffusion_models` | [link](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9b-fp8/resolve/main/flux-2-klein-base-9b-fp8.safetensors) |
| `qwen_3_8b_fp8mixed.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/flux2-klein-9B/resolve/main/split_files/text_encoders/qwen_3_8b_fp8mixed.safetensors) |
| `full_encoder_small_decoder.safetensors` | `vae` | [link](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder/resolve/main/full_encoder_small_decoder.safetensors) |

## Subgraphs

- **Image Edit (FLUX.2 Klein 9B)** (17 nodes)
- **Image Edit (FLUX.2 Klein 9B)** (21 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ReferenceLatent` | 6 | comfy-core |
| `CLIPTextEncode` | 4 | comfy-core |
| `ImageScaleToTotalPixels` | 3 | comfy-core |
| `VAEEncode` | 3 | comfy-core |
| `CFGGuider` | 2 | comfy-core |
| `CLIPLoader` | 2 | comfy-core |
| `EmptyFlux2LatentImage` | 2 | comfy-core |
| `Flux2Scheduler` | 2 | comfy-core |
| `GetImageSize` | 2 | comfy-core |
| `KSamplerSelect` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `RandomNoise` | 2 | comfy-core |
| `SamplerCustomAdvanced` | 2 | comfy-core |
| `SaveImage` | 2 | comfy-core |
| `UNETLoader` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `MarkdownNote` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Model Links

- [Hugging Face:Comfy-Org/flux2-klein-9B](https://huggingface.co/Comfy-Org/flux2-klein-9B)

### Alternative Repos

- [ModelScope:Comfy-Org/flux2-klein-9B](https://modelscope.cn/models/Comfy-Org/flux2-klein-9B)

**diffusion_models**

- [flux-2-klein-base-9b-fp8.safetensors](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9b-fp8)

> Please visit BFL's repo, accept the agreement in the repo, and then download the fp8 model.

**text_encoders**

- [qwen_3_8b_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/flux2-klein-9B/resolve/main/split_files/text_encoders/qwen_3_8b_fp8mixed.safetensors) (8.07 GB)

**vae**

- [full_encoder_small_decoder.safetensors](https://huggingface.co/black-forest-labs/FLUX.2-small-decoder/resolve/main/full_encoder_small_decoder.safetensors) (238 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── flux-2-klein-base-9b-fp8.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen_3_8b_fp8mixed.safetensors
│   └── 📂 vae/
│       └── full_encoder_small_decoder.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
