# FLUX.2 [Klein] 4B: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_flux2_klein_text_to_image)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_text_to_image-1.webp" width="360" alt="FLUX.2 [Klein] 4B: Text to Image image_flux2_klein_text_to_image-1.webp">

> BFL distilled model. Outstanding quality at sub-second speed. Great for real-time generation while retaining quality. Marketing launch will focus on this model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux2_klein_text_to_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_flux2_klein_text_to_image.json)
- [Tutorial](https://docs.comfy.org/tutorials/flux/flux-2-klein)

## Details

| | |
|---|---|
| Name | `image_flux2_klein_text_to_image` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX, FLUX.2 Klein |
| Tags | Image, Text to Image |
| Type | open source |
| Date | 2026-01-16 |
| Author | ComfyUI |
| Download size | 15.9 GB |
| Min ComfyUI version | 0.9.2 |
| Usage | 78 |
| Nodes | 32 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux-2-klein-4b.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/flux2-klein/resolve/main/split_files/diffusion_models/flux-2-klein-4b.safetensors) |
| `flux-2-klein-base-4b.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/flux2-klein/resolve/main/split_files/diffusion_models/flux-2-klein-base-4b.safetensors) |
| `qwen_3_4b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/flux2-klein/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) |
| `flux2-vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) |

## Subgraphs

- **Text to Image (FLUX.2 Klein 4B)** (14 nodes)
- **Text to Image (FLUX.2 Klein 4B Distilled)** (14 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveInt` | 4 | comfy-core |
| `CLIPTextEncode` | 3 | comfy-core |
| `CFGGuider` | 2 | comfy-core |
| `CLIPLoader` | 2 | comfy-core |
| `EmptyFlux2LatentImage` | 2 | comfy-core |
| `Flux2Scheduler` | 2 | comfy-core |
| `KSamplerSelect` | 2 | comfy-core |
| `RandomNoise` | 2 | comfy-core |
| `SamplerCustomAdvanced` | 2 | comfy-core |
| `SaveImage` | 2 | comfy-core |
| `UNETLoader` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `PrimitiveStringMultiline` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/flux2-klein-4B](https://huggingface.co/Comfy-Org/flux2-klein-4B)
- [Hugging Face:Comfy-Org/flux2-dev](https://huggingface.co/Comfy-Org/flux2-dev)

### Alternative Repos

- [ModelScope:Comfy-Org/flux2-klein-4B](https://modelscope.cn/models/Comfy-Org/flux2-klein-4B)
- [ModelScope:Comfy-Org/flux2-dev](https://modelscope.cn/models/Comfy-Org/flux2-dev)

**text_encoders**

- [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/flux2-klein/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) (7.49 GB)

**diffusion_models**

- [flux-2-klein-base-4b.safetensors](https://huggingface.co/Comfy-Org/flux2-klein/resolve/main/split_files/diffusion_models/flux-2-klein-base-4b.safetensors) (7.22 GB)
- [flux-2-klein-4b.safetensors](https://huggingface.co/Comfy-Org/flux2-klein/resolve/main/split_files/diffusion_models/flux-2-klein-4b.safetensors) (7.22 GB)

**vae**

- [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) (320.6 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── qwen_3_4b.safetensors
│   ├── 📂 diffusion_models/
│   │      ├── flux-2-klein-base-4b.safetensors
│   │      └── flux-2-klein-4b.safetensors
│   └── 📂 vae/
│          └── flux2-vae.safetensors
```

## Report issue

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare the required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
