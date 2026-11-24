# SenseNova U1.6: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_sensenova_u16_image_edit-1.webp" width="360" alt="SenseNova U1.6: Image Edit image_sensenova_u16_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_sensenova_u16_image_edit-2.webp" width="360" alt="SenseNova U1.6: Image Edit image_sensenova_u16_image_edit-2.webp">

> Edit a photo with SenseNova-U1.6 by attaching it as a reference and describing the change; the same 8B multimodal backbone reads the source, reworks it and returns the edit at the source's own resolution, with a self-correction pass that re-checks the result against the prompt before returning it.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_sensenova_u16_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_sensenova_u16_image_edit.json)

## Details

| | |
|---|---|
| Name | `image_sensenova_u16_image_edit` |
| Category | Foundation › Image |
| Media type | image |
| Models | SenseNova U1.6 |
| Tags | Image Edit, Int8 |
| Type | open source |
| Date | 2026-11-23 |
| Author | ComfyUI |
| Download size | 27.4 GB |
| Min ComfyUI version | 0.46.0 |
| Usage | 0 |
| Nodes | 51 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #79 | image | sensenova_u16_edit_women_in_car.png |
| output | `SaveImage` #24 | image | image_sensenova_u16_image_edit.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sensenova_u1.6_8b_mot_int8_convrot.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/SenseNova-U1/resolve/main/checkpoints/sensenova_u1.6_8b_mot_int8_convrot.safetensors) |
| `sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/SenseNova-U1/resolve/main/loras/sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors) |
| `qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 7 |  |
| `GetItemFromList` | 5 |  |
| `PrimitiveBoolean` | 3 |  |
| `PrimitiveInt` | 3 |  |
| `CLIPTextEncode` | 2 |  |
| `CreateList` | 2 |  |
| `KSampler` | 2 |  |
| `MarkdownNote` | 2 |  |
| `PreviewAny` | 2 |  |
| `PrimitiveFloat` | 2 |  |
| `PrimitiveStringMultiline` | 2 |  |
| `ResizeImageMaskNode` | 2 |  |
| `SenseNovaConditioning` | 2 |  |
| `CheckpointLoaderSimple` | 1 |  |
| `CLIPLoader` | 1 |  |
| `ComfyMathExpression` | 1 |  |
| `EmptyHiDreamO1LatentImage` | 1 |  |
| `EndLoop` | 1 |  |
| `GetImageSize` | 1 |  |
| `HiDreamO1ReferenceImages` | 1 |  |
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `LoraLoaderModelOnly` | 1 |  |
| `SaveImage` | 1 |  |
| `SenseNovaInterleaveDecode` | 1 |  |
| `StartLoop` | 1 |  |
| `TextGenerateV2` | 1 |  |
| `VAEDecode` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [sensenova_u16_edit_women_in_car.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/sensenova_u16_edit_women_in_car.png)

## Model Links

- [Hugging Face:Comfy-Org/SenseNova-U1](https://huggingface.co/Comfy-Org/SenseNova-U1)
- PE model: [Hugging Face:Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1)

**checkpoints**

- [sensenova_u1.6_8b_mot_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/SenseNova-U1/resolve/main/checkpoints/sensenova_u1.6_8b_mot_int8_convrot.safetensors)

**loras**

- [sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors](https://huggingface.co/Comfy-Org/SenseNova-U1/resolve/main/loras/sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors)

**text_encoders**

- [qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors) (8.82 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │   └── sensenova_u1.6_8b_mot_int8_convrot.safetensors
│   ├── 📂 loras/
│   │   └── sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors
│   └── 📂 text_encoders/
│       └── qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>MarkdownNote</summary>

# SenseNova-U1.6 · Image to Image

SenseNova-U1.6 is a unified multimodal model that combines visual understanding with image generation in a single 8B `mot` backbone. It targets the work where accuracy and beauty both matter — portraits, posters, illustrations and infographics — and it can review its own output and fix text errors before returning the final image.

In this workflow the model works from a reference image: your source image is attached as a reference, and the prompt describes the change you want. Because understanding and generation live in one model, it reads the source, reworks it, and outputs an edit at the source's own resolution.

## Highlights

- **Refined aesthetics** — genre-specific aesthetic reward models drive feedback for portraits and photoreal scenes (realism, texture, lighting), artistic work (creativity, style) and infographics (text, layout, composition). **+10% overall aesthetic quality over U1.5** in subjective user evaluations.
- **Autonomous self-correction** — after the first pass the model checks the image against the prompt, flags blurred or garbled text, typos, misspellings and wrong numbering, then regenerates from the original prompt plus the current image as context. **+7% average relative improvement over single-pass generation** on dense infographic tasks (UltraTextBench).
- **Scaled multi-expert RL** — aesthetic reward models, interleaved self-correction and multiple reward signals across content-specific experts, consolidated into one model through multi-expert on-policy distillation (MOPD).

## Reference images

- **Load Source Image** feeds the reference. It is scaled to **4 megapixels** (the range the model was trained at), then padded to a multiple of 32.
- **Output size follows the source**, so the edit keeps the original aspect ratio and framing.
- The reference node exposes **up to 100 image sockets** (`image_1 … image_100`), used in numeric order and split per image if you pass a batch. **1–4 references** is the useful range in practice; each one costs vision tokens and memory.
- **ImageCompare** shows the source and the result side by side.

## Two pipelines in this workflow

| Pipeline | What it does | Best for |
| --- | --- | --- |
| **Option 1 · Base pipeline** | Single edit pass over the reference image. | Lighting, time of day, mood, material and color changes |
| **Option 2 · Self-correction pipeline** | Edit → review → refine loop (up to 5 passes), then decode. | Editing infographics, posters and layouts that carry text |

## Sampling settings

| Mode | Steps | CFG |
| --- | --- | --- |
| **Turbo** (8-step LoRA) | 8 | 1.0 |
| **Quality** (no LoRA) | 50 | 4.0 |

- **Turbo Mode?** — toggles the 8-step LoRA. Keep it on while you iterate; turn it off for maximum text fidelity and fine detail.
- **Self-Correction** — adds the review/refine loop. On by default here; turn it off for plain lighting or colour edits to save passes.
- **Enable PE** — prompt rewriter for editing: a Qwen3.5-9B PE text encoder reads the source image together with your short instruction and expands it into an executable edit prompt.

</details>
