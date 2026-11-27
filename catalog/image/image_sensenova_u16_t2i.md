# SenseNova U1.6: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_sensenova_u16_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_sensenova_u16_t2i-1.webp" width="360" alt="SenseNova U1.6: Text to Image image_sensenova_u16_t2i-1.webp">

> Turn a written scene into a finished image with SenseNova-U1.6, an 8B multimodal model that understands and generates in one backbone. It reads the prompt, fills in the visual detail and returns a 4-megapixel image at the aspect ratio you pick, with a self-correction pass that re-checks the result against the prompt before it comes back.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_sensenova_u16_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_sensenova_u16_t2i.json)

## Details

| | |
|---|---|
| Name | `image_sensenova_u16_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | SenseNova U1.6 |
| Tags | Text to Image, Int8 |
| Type | open source |
| Date | 2026-11-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.46.0 |
| Usage | 249 |
| Nodes | 46 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #24 | image | image_sensenova_u16_t2i.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sensenova_u1.6_8b_mot_int8_convrot.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/SenseNova-U1/resolve/main/checkpoints/sensenova_u1.6_8b_mot_int8_convrot.safetensors) |
| `sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/SenseNova-U1/resolve/main/loras/sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors) |
| `qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors) |

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
| `CheckpointLoaderSimple` | 1 |  |
| `CLIPLoader` | 1 |  |
| `ComfyMathExpression` | 1 |  |
| `EmptyHiDreamO1LatentImage` | 1 |  |
| `EndLoop` | 1 |  |
| `HiDreamO1ReferenceImages` | 1 |  |
| `LoraLoaderModelOnly` | 1 |  |
| `ResolutionSelector` | 1 |  |
| `SaveImage` | 1 |  |
| `SenseNovaConditioning` | 1 |  |
| `SenseNovaInterleaveDecode` | 1 |  |
| `StartLoop` | 1 |  |
| `TextGenerateV2` | 1 |  |
| `VAEDecode` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Model Links

- [Hugging Face:Comfy-Org/SenseNova-U1](https://huggingface.co/Comfy-Org/SenseNova-U1)
- [Hugging Face:Comfy-Org/Qwen-Image-2.1](https://huggingface.co/Comfy-Org/Qwen-Image-2.1) PE Model

**checkpoints**

- [sensenova_u1.6_8b_mot_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/SenseNova-U1/resolve/main/checkpoints/sensenova_u1.6_8b_mot_int8_convrot.safetensors)

**loras**

- [sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors](https://huggingface.co/Comfy-Org/SenseNova-U1/resolve/main/loras/sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors)

**text_encoders**

- PE Model: [qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors) (8.82 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │   └── sensenova_u1.6_8b_mot_int8_convrot.safetensors
│   ├── 📂 loras/
│   │   └── sensenova_u1.6_8b_mot_8step_lora_bf16.safetensors
│   └── 📂 text_encoders/
│       └── qwen3.5_9b_qwen_image_2.1_pe_t2i.int8_convrot.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>MarkdownNote</summary>

# SenseNova-U1.6 · Text to Image

SenseNova-U1.6 is a unified multimodal model that combines visual understanding with image generation in a single 8B `mot` backbone. It targets the work where accuracy and beauty both matter — portraits, posters, illustrations and infographics — and it can review its own output and fix text errors before returning the final image.

## Highlights

- **Refined aesthetics** — genre-specific aesthetic reward models drive feedback for portraits and photoreal scenes (realism, texture, lighting), artistic work (creativity, style) and infographics (text, layout, composition). **+10% overall aesthetic quality over U1.5** in subjective user evaluations.
- **Autonomous self-correction** — after the first pass the model checks the image against the prompt, flags blurred or garbled text, typos, misspellings and wrong numbering, then regenerates from the original prompt plus the current image as context. **+7% average relative improvement over single-pass generation** on dense infographic tasks (UltraTextBench).
- **Scaled multi-expert RL** — aesthetic reward models, interleaved self-correction and multiple reward signals across content-specific experts, consolidated into one model through multi-expert on-policy distillation (MOPD).

## Two pipelines in this workflow

| Pipeline | What it does | Best for |
| --- | --- | --- |
| **Option 1 · Base pipeline** | Single generation pass. | Portraits, photography, posters, general illustration |
| **Option 2 · Self-correction pipeline** | Generate → review → refine loop (up to 5 passes), then decode. | Infographics, dense text, charts, step diagrams, numbering |

## Sampling settings

| Mode | Steps | CFG |
| --- | --- | --- |
| **Turbo** (8-step LoRA) | 8 | 1.0 |
| **Quality** (no LoRA) | 50 | 4.0 |

- **Turbo Mode?** — toggles the 8-step LoRA. Keep it on for iteration speed; turn it off for maximum text fidelity and fine detail.
- **Self-Correction** — adds the review/refine loop. On for text-heavy layouts, off for portraits and photoreal work, since every pass is another sampling run.
- **Enable PE** — optional prompt rewriter: a Qwen3.5-9B PE text encoder expands short prompts into full visual descriptions and fills in the exact on-image copy.
- **Resolution** — presets from 1:1 to 21:9, default **4:3 (Standard) at 4 megapixels (2368 × 1760)**.

## Prompting tips

- Quote every word that should appear in the image — quoted copy is rendered verbatim, and unquoted text is where errors come from.
- Self-correction was trained on infographics but generalizes to some other image types; it pays off most on dense layouts with numbers, labels and small type.
- With PE off, write the full visual description yourself. A one-line prompt will not reach the model's typography and layout strengths.

</details>
