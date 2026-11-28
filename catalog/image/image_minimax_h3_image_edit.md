# MiniMax-H3-Image: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_minimax_h3_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_minimax_h3_image_edit-1.webp" width="360" alt="MiniMax-H3-Image: Image Edit image_minimax_h3_image_edit-1.webp">

> Edit a picture by describing the change. MiniMax-H3-Image reads the source as <Picture 1> and rewrites only what the instruction asks for, keeping the rest of the frame intact, so one checkpoint handles both text-to-image and reference-guided edits at about 16 MP. Ideal for swapping products, props or vehicles in a shot, changing a material, or restyling a still frame.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_minimax_h3_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_minimax_h3_image_edit.json)

## Details

| | |
|---|---|
| Name | `image_minimax_h3_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | MiniMax H3 Image |
| Tags | Image, Image Edit |
| Type | open source |
| Date | 2026-11-10 |
| Author | ComfyUI |
| Download size | 62.0 GB |
| Min ComfyUI version | 0.45.0 |
| Usage | 6553 |
| Nodes | 27 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #45 | image | vintage_yellow_taxi.png |
| output | `SaveImage` #9 | image | image_minimax_h3_image_edit.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `minimax_h3_image_pruned_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/diffusion_models/minimax_h3_image_pruned_int8_convrot.safetensors) |
| `qwen3.5_9b_w4a8_gptq.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen3.5/resolve/main/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors) |
| `qwen3vl_32b_minimax_h3_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_int8_convrot.safetensors) |
| `minimax_h3_image_vae_fp16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/vae/minimax_h3_image_vae_fp16.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 4 |  |
| `PrimitiveStringMultiline` | 3 |  |
| `CLIPLoader` | 2 |  |
| `ResizeImageMaskNode` | 2 |  |
| `ComfySwitchNode` | 1 |  |
| `ConditioningZeroOut` | 1 |  |
| `GetImageSize` | 1 |  |
| `ImageCompare` | 1 |  |
| `JsonExtractString` | 1 |  |
| `KSampler` | 1 |  |
| `LoadImage` | 1 |  |
| `MiniMaxH3ImageConditioning` | 1 |  |
| `PreviewAny` | 1 |  |
| `PrimitiveBoolean` | 1 |  |
| `SaveImage` | 1 |  |
| `StringReplace` | 1 |  |
| `TextGenerateV2` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: size and Referencen Images</summary>

MiniMax H3 Image is native at about 16 MP, so this workflow edits at 16 MP: the megapixel value sets the canvas, the output size and the reference latent, and the input picture is upscaled to it first. Effective range is about 4 MP to 20 MP; drop `scale total pixels` to 4 MP for a faster, smaller run.

**Settings** - 6 steps, CFG 1.0, `euler` + `simple`, fixed by the CFG-distilled checkpoint. The negative is a `Conditioning Zero Out` and is never read. `Boolean (Enable PE?)` is **on**, so `Generate Text` (Qwen3.5 9B) rewrites your instruction first. For more references, add `Load Image` nodes and name them `<Picture 2>`, `<Picture 3>`, ...

## Recommended sizes (16MP)

| Aspect ratio | Size (width x height) |
| --- | --- |
| 1:1 | 4096x4096 |
| 4:3 / 3:4 | 4736x3552 / 3552x4736 |
| 3:2 / 2:3 | 5024x3360 / 3360x5024 |
| 16:9 / 9:16 | 5472x3072 / 3072x5472 |
| 21:9 | 6272x2688 |

</details>

<details><summary>Model Links</summary>

## Input Asset

- [vintage_yellow_taxi.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/vintage_yellow_taxi.png)

## Model Links

- [Hugging Face:Comfy-Org/MiniMax-H3-Image](https://huggingface.co/Comfy-Org/MiniMax-H3-Image)
- [Hugging Face:Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)
- [Hugging Face:Comfy-Org/Qwen3.5](https://huggingface.co/Comfy-Org/Qwen3.5)

**diffusion_models**

- [minimax_h3_image_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/diffusion_models/minimax_h3_image_pruned_int8_convrot.safetensors) (21 GB)

**text_encoders**

- [qwen3vl_32b_minimax_h3_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_int8_convrot.safetensors) (25.28 GB)
- [qwen3.5_9b_w4a8_gptq.safetensors](https://huggingface.co/Comfy-Org/Qwen3.5/resolve/main/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors) (6.84 GB)

**vae**

- [minimax_h3_image_vae_fp16.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/vae/minimax_h3_image_vae_fp16.safetensors) (1.17 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── minimax_h3_image_pruned_int8_convrot.safetensors
│   ├── 📂 text_encoders/
│   │   ├── qwen3vl_32b_minimax_h3_int8_convrot.safetensors
│   │   └── qwen3.5_9b_w4a8_gptq.safetensors
│   └── 📂 vae/
│       └── minimax_h3_image_vae_fp16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: PE model</summary>

For MiniMax H3 Image's PE model it’s not tied to any specific model

[MiniMax H3 Image PE](https://huggingface.co/MiniMaxAI/MiniMax-H3-Image-PE) repo is using `Qwen3.8-27B, FP4` and we are using Qwen3.5 9B in this workflow

</details>

<details><summary>Note</summary>

Hover on the `prompt output` or `right click -> show link` to restore the link

</details>
