# MOSS-Image: Layout-Guided Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_moss_image_t2i_bboxes)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_moss_image_t2i_bboxes-1.webp" width="360" alt="MOSS-Image: Layout-Guided Text to Image image_moss_image_t2i_bboxes-1.webp">

> Generate an image from a text prompt plus a layout drawn in Create Bounding Boxes. Each box carries its own caption, and text boxes also render their text, so MOSS-Image places every element where you put it. Useful for posters, packaging shots, and any composition where placement matters.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_moss_image_t2i_bboxes.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_moss_image_t2i_bboxes.json)

## Details

| | |
|---|---|
| Name | `image_moss_image_t2i_bboxes` |
| Category | Foundation › Image |
| Output | image |
| Models | MOSS-Image |
| Tags | Layout, Text to Image |
| Type | open source |
| Date | 2026-10-17 |
| Author | ComfyUI |
| Download size | 14.4 GB |
| Min ComfyUI version | 0.44.0 |
| Usage | 56 |
| Nodes | 24 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #9 | image | image_moss_image_t2i_bboxes.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `moss_image_sft_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/diffusion_models/moss_image_sft_int8_convrot.safetensors) |
| `qwen3.5_9b_w4a8_gptq.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors) |
| `flux2-vae_small.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/vae/flux2-vae_small.safetensors) |

## Subgraphs

- **Text to Image (MOSS-Image)** (15 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 4 |  |
| `CLIPTextEncode` | 2 |  |
| `ComfySwitchNode` | 2 |  |
| `PreviewAny` | 2 |  |
| `PrimitiveStringMultiline` | 2 |  |
| `CLIPLoader` | 1 |  |
| `CreateBoundingBoxes` | 1 |  |
| `EmptyFlux2LatentImage` | 1 |  |
| `KSampler` | 1 |  |
| `MOSSImageLayoutPrompt` | 1 |  |
| `ResolutionSelector` | 1 |  |
| `SaveImage` | 1 |  |
| `SkipLayerGuidanceDiTSimple` | 1 |  |
| `TextGenerateV2` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/MOSS-Image](https://huggingface.co/Comfy-Org/MOSS-Image)
- [ModelScope:Comfy-Org/MOSS-Image](https://modelscope.cn/models/Comfy-Org/MOSS-Image)

**diffusion_models**

- [moss_image_sft_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/diffusion_models/moss_image_sft_int8_convrot.safetensors) (5.04 GB)

**text_encoders**

- [qwen3.5_9b_w4a8_gptq.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors) (9.08 GB)

**vae**

- [flux2-vae_small.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/vae/flux2-vae_small.safetensors) (249.5 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── moss_image_sft_int8_convrot.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen3.5_9b_w4a8_gptq.safetensors
│   └── 📂 vae/
│       └── flux2-vae_small.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>MarkdownNote</summary>

## Layout / bounding-box flow

`CreateBoundingBoxes` is where the layout is drawn: it outputs the boxes as `BOUNDING_BOX` plus an element list → `MOSS-Image Layout Prompt` turns those elements into the Layout prompt → that `prompt` is wired into `positive_prompt` of the **Text to Image (MOSS-Image)** subgraph. Remove the link to fall back to a plain text prompt.

Prompt upsampler is **on** in this template, so it can rewrite the prompt and drop the layout — set `enable_prompt_upsampler` to `false` (inside the subgraph) when the boxes must survive verbatim.

</details>

<details><summary>MarkdownNote</summary>

## MOSS-Image capabilities and limits

Sources: [USERGUIDE](https://github.com/OpenMOSS/MOSS-Image/blob/main/USERGUIDE.md), README, HF Base/SFT cards; cross-checked against community benchmark notes.

### Resolution

| Item | Official |
|------|----------|
| Recommended total pixels | **1M, 1.5M, or 2M** |
| Extrapolation range | **0.25M (512×512) to 4M (~2K)** |
| Aspect ratio | Arbitrary; width/height must be positive multiples of **16** |
| This template default | 1024×1024 (~1M) |

### Strengths

- ~**5B** single-stream DiT (Muon); FLUX.2 small VAE; Qwen-family text encoder.
- Strong bilingual English and Chinese text rendering and auto layout; JSON Layout control for text/objects; long prompts (~**4K** tokens); anime and photorealistic.
- **SFT** clearer text grouping/layouts; **Base** has no post-training / CFG distillation (better for community LoRAs).
- Inputs: natural language, tag sequences, JSON layout (layout is experimental). Prefer English (most training data); Chinese supported.

### Limits / notes

- Auto line breaks may not match intent — use `\n` or real newlines for precise text.
- Turning off SLG looks more realistic but can collapse details; official negative-branch skip layer **22** (24/26 also help). kijai notes SLG can overblow anime styles.
- Recommended negative prompt: `nsfw, worst quality, bad anatomy, watermark, jpeg artifact`
- If VRAM is tight, lower resolution or use Sequential / CPU offload.
- When training LoRA yourself, **freeze the text encoder**.
- License: Apache 2.0.

---

## Sampling settings vs. official defaults

| Setting | This template | OpenMOSS official |
|---------|---------------|-------------------|
| Steps | 25 | 50 |
| CFG | 2.5 | 3 |
| Sampler | er_sde | Euler |
| Scheduler | simple | default |
| Denoise | 1 | 1 |
| Shift | 5 (model default) | 5 (same) |

This template follows the faster settings from kijai's ComfyUI MOSS-Image PR [#17095](https://github.com/comfyanonymous/ComfyUI/pull/17095). That is a speed trade-off, not a bug. For results closer to the official ones, try 50 steps and CFG 3.

### Community notes

- **Skip layer guidance:** can overblow anime styles; no alternative values were suggested (template keeps official layer 22). You can check the detail settings inside the subgraph
- **Shift:** adjust with ModelSamplingAuraFlow or ModelSamplingFlux — ModelSamplingSD3 uses a completely different scale. You can enter the subgraph to adjust it
- **SFT banding:** experimental LoRA at about −0.5 strength: [moss_image_sft_lora_blocks_21_to_49…](https://huggingface.co/Kijai/MOSS-image_experimental/blob/main/loras/moss_image_sft_lora_blocks_21_to_49_rank_512_bf16.safetensors)


## Prompt skill

The system prompt driving the upsampler is written from the official [MOSS-Image Prompt Enhancer skill](https://github.com/OpenMOSS/MOSS-Image/blob/main/skills/moss-image-prompt-enhancer/SKILL.md). The same skill turns an idea into a caption or a Layout prompt outside ComfyUI, and it is the reference for the caption style this model was trained on.

</details>

<details><summary>Note: ref_image and PE</summary>

The `ref_image` is fed to the LLM only for prompt enhancement and cannot be used directly by the model. Enable the prompt enhancer if you wish to use it. The model itself doesn't support `ref_image`.

When using the bboxes, enabling PE will rewrite the json input totally, so it's disabled by default in the current workflow.

</details>
