# P-H3-Image: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_p_h3_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_p_h3_t2i-1.webp" width="360" alt="P-H3-Image: Text to Image image_p_h3_t2i-1.webp">

> Pruna AI's few-step image model built on MiniMax-H3: write a plain-language request and a local prompt upsampler expands it into a detailed scene before an 8-step sample. Pick the aspect ratio and megapixel target on the Resolution Selector to move between square, 4:3, 16:9 and portrait canvases.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_p_h3_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_p_h3_t2i.json)

## Details

| | |
|---|---|
| Name | `image_p_h3_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | P-H3-Image, MiniMax H3 |
| Tags | Text to Image, Int8 |
| Type | open source |
| Date | 2026-11-03 |
| Author | ComfyUI |
| Download size | 35.3 GB |
| Min ComfyUI version | 0.44.0 |
| Usage | 1474 |
| Nodes | 22 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #16 | image | image_p_h3_t2i.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `minimax_h3_fl2va_pruned_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) |
| `p-image-oss_lora_bf16.safetensors` | `loras` | [link](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy/resolve/main/loras/p-image-oss_lora_bf16.safetensors) |
| `p-image-oss_prompt_upsampler_w4a8.safetensors` | `text_encoders` | [link](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy/resolve/main/text_encoders/p-image-oss_prompt_upsampler_w4a8.safetensors) |
| `p-image-oss_text_encoder_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy/resolve/main/text_encoders/p-image-oss_text_encoder_int8_convrot.safetensors) |
| `p-image-oss_vae_int8_convrot.safetensors` | `vae` | [link](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy/resolve/main/vae/p-image-oss_vae_int8_convrot.safetensors) |

## Subgraphs

- **New Subgraph** (17 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `CLIPLoader` | 2 | comfy-core |
| `BasicGuider` | 1 | comfy-core |
| `ComfySwitchNode` | 1 |  |
| `KSamplerSelect` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 |  |
| `ManualSigmas` | 1 | comfy-core |
| `MiniMaxH3SigmaShift` | 1 | comfy-core |
| `PH3ImageConditioning` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 |  |
| `RandomNoise` | 1 | comfy-core |
| `ResolutionSelector` | 1 |  |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `TextGenerateV2` | 1 |  |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>How to use</summary>

## p-h3-image

**Text to image:** write your request after `Request:` in the prompt box. The prompt upsampler expands it before sampling.

**Size:** the Resolution Selector sets the canvas — pick the aspect ratio, a megapixel target and a rounding multiple (8.0 MP with multiple 32 lands on 3360×2496 for 4:3). Keep the `Aspect ratio:` line in the request in sync with the selector, otherwise the prompt asks for one shape and the latent produces another.

| Selector ratio | Size at 8.0 MP, multiple 32 |
| --- | --- |
| 1:1 (Square) | 2912×2912 |
| 4:3 (Standard) | 3360×2496 |
| 3:2 (Photo) | 3552×2368 |
| 16:9 (Widescreen) | 3872×2176 |
| 3:4 (Portrait Standard) | 2496×3360 |
| 2:3 (Portrait Photo) | 2368×3552 |
| 9:16 (Portrait Widescreen) | 2176×3872 |

Sampling is an 8-step distilled schedule (`ManualSigmas` + `er_sde`, CFG 1) — more steps do not help. Set seed control to `randomize` for new images and back to `fixed` to reproduce the shipped example.

</details>

<details><summary>MarkdownNote</summary>

## Model Links

- [Hugging Face:Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)
- [Hugging Face:PrunaAI/P-Image-OSS-Comfy](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy)

### Alternative Repos

- [ModelScope:Comfy-Org/MiniMax-H3](https://modelscope.cn/models/Comfy-Org/MiniMax-H3)

**diffusion_models**

- [minimax_h3_fl2va_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) (19.53 GB)

**text_encoders**

- [p-image-oss_text_encoder_int8_convrot.safetensors](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy/resolve/main/text_encoders/p-image-oss_text_encoder_int8_convrot.safetensors) (4.77 GB)
- [p-image-oss_prompt_upsampler_w4a8.safetensors](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy/resolve/main/text_encoders/p-image-oss_prompt_upsampler_w4a8.safetensors) (6.26 GB)

**vae**

- [p-image-oss_vae_int8_convrot.safetensors](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy/resolve/main/vae/p-image-oss_vae_int8_convrot.safetensors) (2.93 GB)

**loras**

- [p-image-oss_lora_bf16.safetensors](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy/resolve/main/loras/p-image-oss_lora_bf16.safetensors) (1.82 GB)

**Total**: 35.31 GB

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── minimax_h3_fl2va_pruned_int8_convrot.safetensors
│   ├── 📂 text_encoders/
│   │   ├── p-image-oss_text_encoder_int8_convrot.safetensors
│   │   └── p-image-oss_prompt_upsampler_w4a8.safetensors
│   ├── 📂 vae/
│   │   └── p-image-oss_vae_int8_convrot.safetensors
│   └── 📂 loras/
│       └── p-image-oss_lora_bf16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>MarkdownNote</summary>

You can try to set `megapixels` to `8`

</details>
