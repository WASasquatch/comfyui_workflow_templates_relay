# Qwen Image 2.1: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_qwen_image_2_1_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_2_1_t2i-1.webp" width="360" alt="Qwen Image 2.1: Text to Image image_qwen_image_2_1_t2i-1.webp">

> Generate images from text prompts with Qwen Image 2.1, the latest open-weight Qwen-Image model, producing a single 1024×1024 image over 25 sampling steps. Generation and instruction-based editing share one model with native 2K output, professional typography, and alpha-channel support. Ideal for poster and layout design, transparent asset creation, and rapid concept visualization.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_2_1_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_qwen_image_2_1_t2i.json)

## Details

| | |
|---|---|
| Name | `image_qwen_image_2_1_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | Qwen Image 2.1 |
| Tags | Text to Image, Int8 |
| Type | open source |
| Date | 2026-09-20 |
| Author | ComfyUI |
| Download size | 24.9 GB |
| Min ComfyUI version | 0.44.0 |
| Usage | 1534 |
| Nodes | 18 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImageAdvanced` #461 | image | image_qwen_image_2_1_t2i.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_2.1_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_int8_convrot.safetensors) |
| `qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors) |
| `qwen3vl_8b_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors) |
| `qwen_image_2.1_vae_bf16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/vae/qwen_image_2.1_vae_bf16.safetensors) |

## Subgraphs

- **Text to Image (Qwen Image 2.1)** (13 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `CLIPLoader` | 2 |  |
| `ComfySwitchNode` | 1 |  |
| `EmptyLatentImage` | 1 |  |
| `KSampler` | 1 |  |
| `PreviewAny` | 1 |  |
| `PrimitiveStringMultiline` | 1 |  |
| `QwenImage21Cache` | 1 |  |
| `ResolutionSelector` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
| `TextEncodeQwenImage21` | 1 |  |
| `TextGenerateV2` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Model links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1)
- [ModelScope:Comfy-Org/Qwen-Image-2.1](https://modelscope.cn/models/Comfy-Org/Qwen-Image-2.1)

**diffusion_models**

- [qwen_image_2.1_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_int8_convrot.safetensors) (6.76 GB)

**text_encoders**

- [qwen3vl_8b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors) (8.71 GB)
- [qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors) (8.82 GB)

**vae**

- [qwen_image_2.1_vae_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/vae/qwen_image_2.1_vae_bf16.safetensors) (644.2 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── qwen_image_2.1_int8_convrot.safetensors
│   ├── 📂 text_encoders/
│   │   ├── qwen3vl_8b_int8_convrot.safetensors
│   │   └── qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors
│   └── 📂 vae/
│       └── qwen_image_2.1_vae_bf16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: Usage</summary>

## Size
Qwen Image 2.1 has native 2K (2048*2048) support for direct output.

Output size comes from ResolutionSelector (width/height). Default is 1 megapixel (1024*1024). For native 2K, set 1:1 and 4 megapixels (2048*2048). Prefer multiples of 32.

## Transparent Image

To generate a transparent image, wrap the prompt like this and replace the middle with the subject:

---
This is an RGBA format image with transparency. `[your description]`. The image has an alpha channel and a transparent background.

---
Save as PNG to keep the alpha channel.

## Parameters

- prompt: what to generate. For RGBA, see Note: transparent.
- negative_prompt: unused while cfg is 1.
- cfg: keep 1 for the Qwen Image 2.1 official path. Raise it only if you use a negative prompt.
- steps: Qwen Image 2.1 official  pipeline uses about 40-50 with euler. This template starts at 25. More advanced samplers need fewer steps.

</details>

<details><summary>Note: PE</summary>

## Prompt Enhancer

The prompt enhancer rewrites your prompt with the Qwen 3.5 prompt enhancer model before the image model sees it. These settings follow the official prompt enhancer release, and the ones you are most likely to change are exposed on the node.

- `refine_prompt`: on runs the rewrite and feeds it to the image model, off passes your prompt through as written. On gives the image model a fuller prompt and usually better results; off skips the rewrite pass and the run finishes faster. This template starts with it off.
- `thinking_mode`: turn this on together with the enhancer. The checkpoint was trained with a reasoning block and loses quality without it.
- `max_length`: the token budget for the reasoning block plus the rewritten prompt, 4096 here. The official setting is 16256; this template caps it lower so a single rewrite cannot run for many minutes.
- `sampling_mode`: the sampling values live inside the subgraph. They follow the official ones: `temperature` 1.0, `top_p` 0.95, `top_k` 20, `min_p` 0, `presence_penalty` 1.5, `repetition_penalty` 1.0.

The enhancer checkpoint and its system prompt live inside the subgraph.

</details>
