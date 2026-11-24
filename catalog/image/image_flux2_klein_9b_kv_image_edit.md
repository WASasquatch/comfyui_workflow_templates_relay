# FLUX.2 Klein KV: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_flux2_klein_9b_kv_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_9b_kv_image_edit-1.webp" width="360" alt="FLUX.2 Klein KV: Image Edit image_flux2_klein_9b_kv_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_9b_kv_image_edit-2.webp" width="360" alt="FLUX.2 Klein KV: Image Edit image_flux2_klein_9b_kv_image_edit-2.webp">

> Upload reference images and a text prompt. Generate multiple edited images using cached image data for faster processing.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_9b_kv_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_flux2_klein_9b_kv_image_edit.json)

## Details

| | |
|---|---|
| Name | `image_flux2_klein_9b_kv_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX.2 Klein |
| Tags | Image, Image Edit |
| Type | open source |
| Date | 2026-03-12 |
| Author | ComfyUI |
| Download size | 17.5 GB |
| Min ComfyUI version | 0.17.0 |
| Distributions | local |
| Usage | 16 |
| Nodes | 27 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #76 | image | man_in_street.png |
| input | `LoadImage` #81 | image | safari_outfit.png |
| output | `SaveImage` #94 | image | image_flux2_klein_9b_kv_image_edit.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux-2-klein-9b-kv-fp8.safetensors` | `diffusion_models` | [link](https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-kv-fp8/resolve/main/flux-2-klein-9b-kv-fp8.safetensors) |
| `qwen_3_8b_fp8mixed.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/flux2-klein-9B/resolve/main/split_files/text_encoders/qwen_3_8b_fp8mixed.safetensors) |
| `flux2-vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) |

## Subgraphs

- **Reference Conditioning** (3 nodes)
- **Reference Conditioning** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ReferenceLatent` | 4 | comfy-core |
| `ImageScaleToTotalPixels` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `VAEEncode` | 2 | comfy-core |
| `CFGGuider` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `EmptyFlux2LatentImage` | 1 | comfy-core |
| `Flux2Scheduler` | 1 | comfy-core |
| `FluxKVCache` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

[black-forest-labs/FLUX.2-klein-9b-kv-fp8](https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-kv-fp8)

## Model Links

- [Hugging Face:Comfy-Org/flux2-klein-9B](https://huggingface.co/Comfy-Org/flux2-klein-9B)
- [Hugging Face:Comfy-Org/flux2-dev](https://huggingface.co/Comfy-Org/flux2-dev)

### Alternative Repos

- [ModelScope:Comfy-Org/flux2-klein-9B](https://modelscope.cn/models/Comfy-Org/flux2-klein-9B)
- [ModelScope:Comfy-Org/flux2-dev](https://modelscope.cn/models/Comfy-Org/flux2-dev)

**diffusion_models**

- [flux-2-klein-9b-kv-fp8.safetensors](https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-kv-fp8/resolve/main/flux-2-klein-9b-kv-fp8.safetensors) (9.14 GB)

**text_encoders**

- [qwen_3_8b_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/flux2-klein-9B/resolve/main/split_files/text_encoders/qwen_3_8b_fp8mixed.safetensors) (8.07 GB)

**vae**

- [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) (320.6 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │      └── flux-2-klein-9b-kv-fp8.safetensors
│   ├── 📂 text_encoders/
│   │      └── qwen_3_8b_fp8mixed.safetensors
│   └── 📂 vae/
│          └── flux2-vae.safetensors
```
## Report issue

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>More reference images</summary>

You can follow this pattern to add more reference images.

</details>
