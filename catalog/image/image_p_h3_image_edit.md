# P-H3-Image: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_p_h3_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_p_h3_image_edit-1.webp" width="360" alt="P-H3-Image: Image Edit image_p_h3_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_p_h3_image_edit-2.webp" width="360" alt="P-H3-Image: Image Edit image_p_h3_image_edit-2.webp">

> Pruna AI's few-step image model built on MiniMax-H3: edit the source image with a short instruction, up to 9 reference images, 8-step sampling.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_p_h3_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_p_h3_image_edit.json)

## Details

| | |
|---|---|
| Name | `image_p_h3_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | P-H3-Image, MiniMax H3 |
| Tags | Image Edit, Int8 |
| Type | open source |
| Date | 2026-11-03 |
| Author | ComfyUI |
| Download size | 37.6 GB |
| Min ComfyUI version | 0.44.0 |
| Usage | 1315 |
| Nodes | 24 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #26 | image | image_p_h3_image_edit_atrium_day.png |
| output | `SaveImage` #16 | image | image_p_h3_image_edit.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `minimax_h3_fl2va_pruned_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) |
| `p-image-oss_lora_bf16.safetensors` | `loras` | [link](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy/resolve/main/loras/p-image-oss_lora_bf16.safetensors) |
| `p-image-oss_prompt_upsampler_w4a8.safetensors` | `text_encoders` | [link](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy/resolve/main/text_encoders/p-image-oss_prompt_upsampler_w4a8.safetensors) |
| `p-image-oss_text_encoder_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy/resolve/main/text_encoders/p-image-oss_text_encoder_int8_convrot.safetensors) |
| `p-image-oss_vae_int8_convrot.safetensors` | `vae` | [link](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy/resolve/main/vae/p-image-oss_vae_int8_convrot.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPLoader` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `BasicGuider` | 1 | comfy-core |
| `ComfySwitchNode` | 1 |  |
| `GetImageSize` | 1 |  |
| `ImageCompare` | 1 |  |
| `ImageScaleToTotalPixels` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `LoadImage` | 1 |  |
| `LoraLoaderModelOnly` | 1 |  |
| `ManualSigmas` | 1 | comfy-core |
| `MiniMaxH3SigmaShift` | 1 | comfy-core |
| `PH3ImageConditioning` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 |  |
| `RandomNoise` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `TextGenerateV2` | 1 |  |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>How to use</summary>

## p-h3-image

**Text to image:** write your request after `Request:` in the Prompt upsampler. Width and height 0 give 2912x2912.

**Image edit:** the source image goes into `Load Image`; the result matches its shape, so `width`/`height` on the conditioning follow the image automatically.

**Prompt format:** write `Aspect ratio: <ratio>` then `Request: <what to change>`. The model keeps the composition when the request is one short sentence.

Other shapes: set width and height on p-h3-image Conditioning and change `Aspect ratio:` to match.

| Ratio | Size |
| --- | --- |
| 4:3 | 3360x2496 |
| 3:2 | 3552x2368 |
| 16:9 | 3872x2176 |

Swap the sides for portrait, for example `Aspect ratio: 3:4` with 2496x3360.

</details>

<details><summary>MarkdownNote</summary>

## Input Asset

- [image_p_h3_image_edit_atrium_day.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/image_p_h3_image_edit_atrium_day.png)

## Model Links

- [Hugging Face:Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)
- [Hugging Face:PrunaAI/P-Image-OSS-Comfy](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy)

### Alternative Repos

- [ModelScope:Comfy-Org/MiniMax-H3](https://modelscope.cn/models/Comfy-Org/MiniMax-H3)

**diffusion_models**

- [minimax_h3_fl2va_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) (19.53 GB)

**text_encoders**

- [p-image-oss_text_encoder_int8_convrot.safetensors](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy/resolve/main/text_encoders/p-image-oss_text_encoder_int8_convrot.safetensors)
- [p-image-oss_prompt_upsampler_w4a8.safetensors](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy/resolve/main/text_encoders/p-image-oss_prompt_upsampler_w4a8.safetensors)

**vae**

- [p-image-oss_vae_int8_convrot.safetensors](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy/resolve/main/vae/p-image-oss_vae_int8_convrot.safetensors)

**loras**

- [p-image-oss_lora_bf16.safetensors](https://huggingface.co/PrunaAI/P-Image-OSS-Comfy/resolve/main/loras/p-image-oss_lora_bf16.safetensors)

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
