# Qwen Image 2.1 Turbo: Image edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_qwen_image_2_1_turbo_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_2_1_turbo_image_edit-1.webp" width="360" alt="Qwen Image 2.1 Turbo: Image edit image_qwen_image_2_1_turbo_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_2_1_turbo_image_edit-2.webp" width="360" alt="Qwen Image 2.1 Turbo: Image edit image_qwen_image_2_1_turbo_image_edit-2.webp">

> Edit images with Qwen-Image-2.1 by feeding two reference images through a single checkpoint that handles both generation and editing, then comparing the result against the original. Ideal for character-consistent edits, product cutout compositing with real transparency, and style-transfer passes at native 2K

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_2_1_turbo_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_qwen_image_2_1_turbo_image_edit.json)

## Details

| | |
|---|---|
| Name | `image_qwen_image_2_1_turbo_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | Qwen Image 2.1 |
| Tags | Image Edit |
| Type | open source |
| Date | 2026-10-13 |
| Author | ComfyUI |
| Download size | 38.2 GB |
| Min ComfyUI version | 0.44.0 |
| Usage | 2000 |
| Nodes | 25 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #470 | image | ballet_dancer_photography_minimalist_architecture.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_2.1_turbo_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_turbo_int8_convrot.safetensors) |
| `qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors) |
| `qwen3vl_8b_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors) |
| `qwen_image_2.1_vae_bf16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/vae/qwen_image_2.1_vae_bf16.safetensors) |

## Subgraphs

- **Image Edit (Qwen Image 2.1 Turbo)** (19 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `CLIPLoader` | 2 |  |
| `ComfySwitchNode` | 2 |  |
| `BatchImagesNode` | 1 |  |
| `CFGGuider` | 1 |  |
| `EmptyLatentImage` | 1 |  |
| `ImageCompare` | 1 |  |
| `KSamplerSelect` | 1 |  |
| `LoadImage` | 1 |  |
| `ManualSigmas` | 1 |  |
| `PreviewAny` | 1 |  |
| `PrimitiveStringMultiline` | 1 |  |
| `QwenImage21Cache` | 1 |  |
| `RandomNoise` | 1 |  |
| `SamplerCustomAdvanced` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
| `TextEncodeQwenImage21` | 1 |  |
| `TextGenerateV2` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Usage</summary>

## Size
Qwen Image 2.1 has native 2K (2048*2048) support for direct output.

- resolution is a total pixel budget (not width or height). Aspect ratio is preserved.
- Official default is 1024. The model supports up to 2048.
- This template starts at 0: no resize beyond a multiple of 32.
- Output follows image_1. Extra refs can differ in size or aspect.
- custom_size off: canvas comes from the encode latent (image_1).
- custom_size on: use ResolutionSelector width/height. Keep it close to the resized image_1 size, or the edit can shift.

## Reference images
- Up to 10 reference images (image_1 to image_10).
- Mention them in the prompt as `<image1>`, `<image2>`, ...
- image_1 is the edit target. The rest are references.

## Custom settings
If you need custom settings, enter or unpack the subgraph to edit it. See the [Subgraph](https://docs.comfy.org/interface/features/subgraph) guide.

## Parameters
- prompt: edit instruction. Use `<image1>` ... `<image10>`.
- negative_prompt: unused while cfg is 1.
- cfg: keep 1 for the Qwen Image 2.1 official path. Raise it only if you use a negative prompt.
- steps: Qwen Image 2.1 official pipeline uses about 40-50 with euler. This template starts at 25. More advanced samplers need fewer steps.

</details>

<details><summary>Note: Model links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Input Asset

- [ballet_dancer_photography_minimalist_architecture.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/ballet_dancer_photography_minimalist_architecture.png)

## Model Links

- [Hugging Face:Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1)
- [ModelScope:Comfy-Org/Qwen-Image-2.1](https://modelscope.cn/models/Comfy-Org/Qwen-Image-2.1)

**diffusion_models**

- [qwen_image_2.1_turbo_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_turbo_bf16.safetensors) (13.25 GB)
- [qwen_image_2.1_turbo_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_turbo_int8_convrot.safetensors) (6.76 GB)

**text_encoders**

- [qwen3vl_8b_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_bf16.safetensors) (16.33 GB)
- [qwen3vl_8b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors) (8.71 GB) 
- [qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors) (8.82 GB)

**vae**

- [qwen_image_2.1_vae_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/vae/qwen_image_2.1_vae_bf16.safetensors) (644.2 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   ├── qwen_image_2.1_turbo_bf16.safetensors
│   │   └── qwen_image_2.1_turbo_int8_convrot.safetensors
│   ├── 📂 text_encoders/
│   │   ├── qwen3vl_8b_bf16.safetensors
│   │   ├── qwen3vl_8b_int8_convrot.safetensors
│   │   └── qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors│   └── 📂 vae/
│       └── qwen_image_2.1_vae_bf16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: PE</summary>

## Prompt Enhancer

The prompt enhancer rewrites your instruction with the Qwen 3.5 prompt enhancer model before the edit model sees it. These settings follow the official prompt enhancer release, and the ones you are most likely to change are exposed on the node.

- `refine_prompt`: on runs the rewrite and feeds it to the edit model, off passes your instruction through as written. On gives the edit model a fuller prompt and usually better results; off skips the rewrite pass and the run finishes faster. This template starts with it off.
- `thinking`: turn this on together with the enhancer. The checkpoint was trained with a reasoning block and loses quality without it.
- `max_length`: the token budget for the reasoning block plus the rewritten prompt, 4096 here. The official setting is 24000; this template caps it lower so a single rewrite cannot run for many minutes.
- `sampling_mode`: the sampling values live inside the subgraph. They follow the official ones: `temperature` 1.0, `top_p` 0.95, `top_k` 20, `min_p` 0, `presence_penalty` 0, `repetition_penalty` 1.0.

The enhancer checkpoint and its system prompt live inside the subgraph.

</details>
