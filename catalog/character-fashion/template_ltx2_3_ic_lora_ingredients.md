# LTX-2.3 IC-LoRA: Reference Sheet Control

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_ltx2_3_ic_lora_ingredients)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_ic_lora_ingredients-1.webp" width="360" alt="LTX-2.3 IC-LoRA: Reference Sheet Control template_ltx2_3_ic_lora_ingredients-1.webp">

> Generate short video clips that stay visually consistent with a reference sheet inventorying characters, props, and locations. Input a composite reference image and a split prompt describing the action, outputting a single video clip. Ideal for character-driven animation, consistent prop visualization, and location-specific scene generation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_ic_lora_ingredients.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_ltx2_3_ic_lora_ingredients.json)

## Details

| | |
|---|---|
| Name | `template_ltx2_3_ic_lora_ingredients` |
| Category | Applied › Character & Fashion |
| Output | video |
| Models | LTX-2.3 |
| Tags | Reference to Video |
| Type | open source |
| Date | 2026-07-13 |
| Author | ComfyUI |
| Download size | 36.9 GB |
| Min ComfyUI version | 0.22.0 |
| Usage | 103 |
| Nodes | 42 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #724 | image | german_shepherd_news_anchor_ref.png |
| output | `SaveVideo` #68 | video | template_ltx2_3_ic_lora_ingredients.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-2.3-22b-distilled-fp8.safetensors` | `checkpoints` | [link](https://huggingface.co/Lightricks/LTX-2.3-fp8/resolve/main/ltx-2.3-22b-distilled-fp8.safetensors) |
| `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/loras/gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors) |
| `ltx-2.3-22b-ic-lora-ingredients-0.9.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/ltx-2.3/resolve/main/split_files/loras/ltx-2.3-22b-ic-lora-ingredients-0.9.safetensors) |
| `gemma_3_12B_it_fp4_mixed.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) |

## Subgraphs

- **LTX-2.3 IC-LoRA Video Generation** (30 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveInt` | 5 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `ComfyMathExpression` | 2 | comfy-core |
| `GetImageSize` | 2 |  |
| `MarkdownNote` | 2 |  |
| `PrimitiveBoolean` | 2 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `ComfySwitchNode` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `EmptyImage` | 1 |  |
| `EmptyLTXVLatentVideo` | 1 | comfy-core |
| `GetICLoRAParameters` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 |  |
| `LoraLoader` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `LTXAVTextEncoderLoader` | 1 | comfy-core |
| `LTXVAddGuide` | 1 | comfy-core |
| `LTXVAudioVAEDecode` | 1 | comfy-core |
| `LTXVAudioVAELoader` | 1 | comfy-core |
| `LTXVConcatAVLatent` | 1 | comfy-core |
| `LTXVConditioning` | 1 | comfy-core |
| `LTXVCropGuides` | 1 | comfy-core |
| `LTXVEmptyLatentAudio` | 1 | comfy-core |
| `LTXVImgToVideoInplace` | 1 | comfy-core |
| `LTXVSeparateAVLatent` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `PreviewImage` | 1 |  |
| `RepeatImageBatch` | 1 |  |
| `ResizeAndPadImage` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
| `TextGenerateLTX2Prompt` | 1 | comfy-core |
| `VAEDecodeTiled` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model Links</summary>

- Hugging Face (base): [Lightricks/LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3/)
- Hugging Face (Ingredients IC-LoRA): [Lightricks/LTX-2.3-22b-IC-LoRA-Ingredients](https://huggingface.co/Comfy-Org/ltx-2.3/resolve/main/split_files/loras/ltx-2.3-22b-ic-lora-ingredients-0.9.safetensors) (1.22 GB)
- [gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/loras/gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors) (599.1 MB)


## Model Storage Location

- [Hugging Face:Comfy-Org/ltx-2.3](https://huggingface.co/Comfy-Org/ltx-2.3)
- [ModelScope:Comfy-Org/ltx-2.3](https://modelscope.cn/models/Comfy-Org/ltx-2.3)
- [Hugging Face:Comfy-Org/ltx-2](https://huggingface.co/Comfy-Org/ltx-2)
- [ModelScope:Comfy-Org/ltx-2](https://modelscope.cn/models/Comfy-Org/ltx-2)

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │   └── ltx-2.3-22b-distilled-fp8.safetensors
│   ├── 📂 text_encoders/
│   │   └── gemma_3_12B_it_fp4_mixed.safetensors
│   └── 📂 loras/
│       ├── ltx-2.3-22b-ic-lora-ingredients-0.9.safetensors
│       └── gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: IC-LoRA</summary>

## IC-LoRA Ingredients

Sources (official only):
- Model card: [Lightricks/LTX-2.3-22b-IC-LoRA-Ingredients](https://huggingface.co/Lightricks/LTX-2.3-22b-IC-LoRA-Ingredients)
- IC-LoRA docs: [docs.ltx.video — IC-LoRA usage guide](https://docs.ltx.video/open-source-model/usage-guides/ic-lo-ra)

### What This Model Is
From the model card:

> This is an IC-LoRA trained on top of LTX-2.3-22B, which conditions video generation on a reference sheet — a single composite image inventorying the characters, props, and location of a scene — so that generated videos keep those elements visually consistent.


**Model details (model card):**
- Base Model: LTX-2.3-22B (dev)
- Training Type: IC-LoRA (in-context LoRA)
- Control Type: Reference-sheet conditioning — character / prop / location identity carried into the generated video
- Reference Downscale Factor: `1` (the reference is provided at the same resolution as the output)
- Pipeline: the reference sheet is supplied as a static video (the still sheet looped to the output's length and frame rate). Trained with a `video_to_video` strategy over reference latents; no extra color/space transforms are applied at inference.

### Intended Use & Out-of-Scope
From the model card:

- **Intended use:** Generating short video clips that stay faithful to a supplied reference sheet — keeping recurring characters (face and costume), handled props, and the set/location consistent with the sheet while following an action described in the prompt.
- **Out of scope:** This is not a general text-to-video model — it expects a reference sheet as conditioning. It was trained at a single resolution / length bucket (**768×448**, **121 frames**, **24 fps**); other resolutions, much longer clips, or use without a reference sheet are out of distribution. It does not reproduce identities that are absent from the supplied sheet.

### Control Signal Requirements
From the model card:

- **Control signal type:** Reference sheet — a single composite image with one clean panel per distinct visual element (each character as a face close-up + body turnaround, each prop as a product-style render, and one clean location panel), laid out on a **black background with no text**.
- **Expected input:** A static video built from the reference sheet, looped to match the output clip's length and frame rate, at the output resolution (downscale factor 1).
- **Preprocessing:** Author the reference sheet, then loop the still into a static video. Frame count must be **≥ 121** so the reference-encoding / 121-frame read bucket is satisfied; all targets in training were ≥ 121 frames.
- **Alignment:** The reference video should match the output resolution and frame rate; its frame count must be at least the output length (clamped to ≥ 121).

### Prompt Format
From the model card — the prompt is split into two labeled parts, matching how the model was trained:

```text
Reference sheet: <description of the panels in the sheet — characters, props, location>

Generated video: <description of the action / shot you want generated>
```

At inference, the reference sheet (as a static video) supplies *what things look like*, and the `Generated video:` portion supplies *what happens*. The model reads the reference latents in-context and renders a new clip whose characters, props, and setting match the sheet.

Model-card gallery examples also show prompts labeled as `### Reference Sheet Description` / `### Target Description`.

### ComfyUI Usage
From the model card:

1. Copy the LoRA weights into `models/loras`.
2. Load the LTX-2.3-22B base model and add the Ingredients LoRA.
3. Start at strength `1.0` and adjust to taste.
4. Use an IC-LoRA / reference workflow from the LTX-2 ComfyUI repository, which already wires the reference (control) input. Connect the reference-sheet static video as the control/reference input; a generic LoRA loader that ignores the reference path will not apply the conditioning.

### Recommended Settings
From the model card:

- LoRA strength / weight: **1.4**
- Inference steps: **30**
- Guidance scale: **4.0**
- Resolution & frames: **768×448**, **121 frames**, **24 fps** (the trained bucket — best results here)
- Prompting: use the two-part `Reference sheet: … / Generated video: …` structure. The `Reference sheet:` text should describe the panels present; the `Generated video:` text drives the action.
- Suggested negative prompt: `worst quality, inconsistent motion, blurry, jittery, distorted`
- Validation used spatiotemporal guidance (STG, mode `stg_v`, block 29, scale 1.0), which can help motion stability.

### Tips & Troubleshooting
From the model card only:

- **Bigger panels carry over better:** The more space an element takes up in the reference image, the more faithfully it carries over into the generated video. Give important characters/props larger, more prominent panels rather than small or crowded ones.
- **Identity drift:** If a character's face or costume drifts, make sure the reference sheet has a clean, front-facing close-up and full turnaround for that character, and that its panel isn't cluttered or text-laden.
- **Element not appearing:** The model only reproduces elements present on the sheet — add a dedicated panel for any prop/character you need to persist, and describe it in the `Reference sheet:` portion of the prompt.
- **Reference too short:** The reference static video must be ≥ 121 frames; shorter references break the reference-encoding bucket.

</details>
