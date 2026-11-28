# Flux.1 Outpaint

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=flux_fill_outpaint_example)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_fill_outpaint_example-1.webp" width="360" alt="Flux.1 Outpaint flux_fill_outpaint_example-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_fill_outpaint_example-2.webp" width="360" alt="Flux.1 Outpaint flux_fill_outpaint_example-2.webp">

> Extend images beyond boundaries using Flux.1 outpainting.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_fill_outpaint_example.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/flux_fill_outpaint_example.json)
- [Tutorial](https://docs.comfy.org/tutorials/flux/flux-1-fill-dev)

## Details

| | |
|---|---|
| Name | `flux_fill_outpaint_example` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX.1, FLUX |
| Tags | Outpainting, Image |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 9.7 GB |
| Min ComfyUI version | 0.0.4 |
| Usage | 76 |
| Nodes | 14 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #17 | image | flux_fill_outpaint_example_input_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux1-fill-dev.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/split_files/diffusion_models/flux1-fill-dev.safetensors) |
| `clip_l.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true) |
| `t5xxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `DifferentialDiffusion` | 1 | comfy-core |
| `DualCLIPLoader` | 1 | comfy-core |
| `FluxGuidance` | 1 | comfy-core |
| `ImagePadForOutpaint` | 1 | comfy-core |
| `InpaintModelConditioning` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Model links</summary>

[Tutorial](https://docs.comfy.org/tutorials/flux/flux-1-fill-dev)

## Model Links

- [Hugging Face:Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev)
- [Hugging Face:Comfy-Org/Lumina_Image_2.0_Repackaged](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/flux1-dev](https://modelscope.cn/models/Comfy-Org/flux1-dev)
- [ModelScope:Comfy-Org/Lumina_Image_2.0_Repackaged](https://modelscope.cn/models/Comfy-Org/Lumina_Image_2.0_Repackaged)

**text_encoders**

- [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true) (234.7 MB)
- [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true) (9.12 GB)

**diffusion_models**

- [flux1-fill-dev.safetensors](https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/split_files/diffusion_models/flux1-fill-dev.safetensors) (22.17 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      ├── clip_l.safetensors
│   │      └── t5xxl_fp16.safetensors
│   ├── 📂 diffusion_models/
│   │      └── flux1-fill-dev.safetensors
│   └── 📂 vae/
│          └── ae.safetensors
```

</details>
