# Krea-2 Int8: Image Style Reference

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_krea2_turbo_int8_image_style_reference)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_krea2_turbo_int8_image_style_reference-1.webp" width="360" alt="Krea-2 Int8: Image Style Reference image_krea2_turbo_int8_image_style_reference-1.webp">

> Generate images with the Krea-2 Turbo model while referencing the style of 1–2 uploaded images, using the high-performance Int8 Convrot format for faster, higher-quality inference. This workflow accepts up to two reference image inputs and produces a single stylized output, with optional LoRA support for further creative control. Ideal for matching a specific artistic style in concept art, producing consistent brand visuals, and exploring rapid style transfer for iterative design.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_krea2_turbo_int8_image_style_reference.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_krea2_turbo_int8_image_style_reference.json)

## Details

| | |
|---|---|
| Name | `image_krea2_turbo_int8_image_style_reference` |
| Category | Foundation › Image |
| Output | image |
| Models | Krea 2 |
| Tags | Style Reference, Image, Int8 |
| Type | open source |
| Date | 2026-07-20 |
| Author | ComfyUI |
| Download size | 18.1 GB |
| Min ComfyUI version | 0.44.0 |
| Usage | 520 |
| Nodes | 28 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #69 | image | krea2_reference_image.png |
| output | `SaveImage` #29 | image | image_krea2_turbo_int8_image_style_reference.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `krea2_turbo_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/diffusion_models/krea2_turbo_int8_convrot.safetensors) |
| `krea2_style_reference.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/loras/krea2_style_reference.safetensors) |
| `qwen3vl_4b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/text_encoders/qwen3vl_4b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Image Style Reference (Krea-2 Turbo)** (23 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `EmptyLatentImage` | 2 | comfy-core |
| `PrimitiveStringMultiline` | 2 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `CFGGuider` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `ComfySwitchNode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `FluxKontextMultiReferenceLatentMethod` | 1 | comfy-core |
| `GetImageSize` | 1 |  |
| `KSamplerSelect` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingFlux` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `ResolutionSelector` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `StringConcatenate` | 1 | comfy-core |
| `TextEncodeQwenImageEditPlus` | 1 | comfy-core |
| `TextGenerateV2` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2)
- [ModelScope:Comfy-Org/Krea-2](https://modelscope.cn/models/Comfy-Org/Krea-2)

- [ostris/krea2_turbo_style_reference](https://huggingface.co/ostris/krea2_turbo_style_reference)

**diffusion_models**

- [krea2_turbo_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/diffusion_models/krea2_turbo_int8_convrot.safetensors) (12.57 GB)

**text_encoders**

- [qwen3vl_4b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/text_encoders/qwen3vl_4b_fp8_scaled.safetensors) (4.88 GB)

**vae**

- [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/vae/qwen_image_vae.safetensors) (242 MB)

**loras**

- [krea2_style_reference.safetensors](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/loras/krea2_style_reference.safetensors) (435.9 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── krea2_turbo_int8_convrot.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen3vl_4b_fp8_scaled.safetensors
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   └── 📂 loras/
│       └── krea2_style_reference.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
