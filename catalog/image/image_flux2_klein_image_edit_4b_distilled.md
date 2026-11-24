# FLUX.2 [Klein] 4B Distilled: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_flux2_klein_image_edit_4b_distilled)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_4b_distilled-1.webp" width="360" alt="FLUX.2 [Klein] 4B Distilled: Image Edit image_flux2_klein_image_edit_4b_distilled-1.webp">

> The fastest variant in the Klein family. Built for interactive applications, real-time previews, and latency-critical production use cases.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_image_edit_4b_distilled.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_flux2_klein_image_edit_4b_distilled.json)
- [Tutorial](https://docs.comfy.org/tutorials/flux/flux-2-klein)

## Details

| | |
|---|---|
| Name | `image_flux2_klein_image_edit_4b_distilled` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX, FLUX.2 Klein |
| Tags | Image, Image Edit |
| Type | open source |
| Date | 2026-01-16 |
| Author | ComfyUI |
| Download size | 11.6 GB |
| Min ComfyUI version | 0.9.2 |
| Usage | 780 |
| Nodes | 43 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #76 | image | handbag_white.png |
| input | `LoadImage` #81 | image | comfy_logo_blue.png |
| output | `SaveImage` #94 | image | image_flux2_klein_image_edit_4b_distilled.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux-2-klein-4b-fp8.safetensors` | `diffusion_models` | [link](https://huggingface.co/black-forest-labs/FLUX.2-klein-4b-fp8/resolve/main/flux-2-klein-4b-fp8.safetensors) |
| `qwen_3_4b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) |
| `flux2-vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) |

## Subgraphs

- **Image Edit (FLUX.2 Klein 4B Distilled)** (17 nodes)
- **Image Edit (FLUX.2 Klein 4B Distilled)** (17 nodes)
- **Reference Conditioning** (3 nodes)
- **Reference Conditioning** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ReferenceLatent` | 6 | comfy-core |
| `ImageScaleToTotalPixels` | 3 | comfy-core |
| `VAEEncode` | 3 | comfy-core |
| `CFGGuider` | 2 | comfy-core |
| `CLIPLoader` | 2 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `ConditioningZeroOut` | 2 | comfy-core |
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

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo)
- [Hugging Face:Comfy-Org/flux2-dev](https://huggingface.co/Comfy-Org/flux2-dev)

### Alternative Repos

- [ModelScope:Comfy-Org/z_image_turbo](https://modelscope.cn/models/Comfy-Org/z_image_turbo)
- [ModelScope:Comfy-Org/flux2-dev](https://modelscope.cn/models/Comfy-Org/flux2-dev)

**text_encoders**

- [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) (7.49 GB)

**diffusion_models**

- [flux-2-klein-4b-fp8.safetensors](https://huggingface.co/black-forest-labs/FLUX.2-klein-4b-fp8/resolve/main/flux-2-klein-4b-fp8.safetensors) (3.79 GB)

**vae**

- [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) (320.6 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── qwen_3_4b.safetensors
│   ├── 📂 diffusion_models/
│   │      └── flux-2-klein-4b-fp8.safetensors
│   └── 📂 vae/
│          └── flux2-vae.safetensors
```

## Report issues

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
