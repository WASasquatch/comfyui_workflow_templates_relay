# Fibo 2.0 Dev: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_fibo2_edit_dev_pe)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_fibo2_edit_dev_pe-1.webp" width="360" alt="Fibo 2.0 Dev: Image Edit image_fibo2_edit_dev_pe-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_fibo2_edit_dev_pe-2.webp" width="360" alt="Fibo 2.0 Dev: Image Edit image_fibo2_edit_dev_pe-2.webp">

> Same graph as the Turbo template loaded with the full non-distilled Fibo 2.0 Dev weights: 50 steps at CFG 5 with Bria's structured negative, for the cleanest edits when sampling time is not the constraint. The optional prompt enhancer rewrites the instruction into a structured caption; switch it off to sample the raw prompt.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_fibo2_edit_dev_pe.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_fibo2_edit_dev_pe.json)

## Details

| | |
|---|---|
| Name | `image_fibo2_edit_dev_pe` |
| Category | Foundation › Image |
| Output | image |
| Models | Fibo 2.0 |
| Tags | Image Edit, Int8 |
| Type | open source |
| Date | 2026-10-26 |
| Author | ComfyUI |
| Download size | 25.1 GB |
| Min ComfyUI version | 0.44.0 |
| Usage | 152 |
| Nodes | 19 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #10 | image | red_bowler_hat_portrait.png |
| output | `SaveImage` #7 | image | image_fibo2_edit_dev_pe.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `fibo2_dev_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/diffusion_models/fibo2_dev_int8_convrot.safetensors) |
| `qwen3vl_4b_bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/text_encoders/qwen3vl_4b_bf16.safetensors) |
| `qwen3vl_8b_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen3-VL/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors) |
| `flux2-vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/vae/flux2-vae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `CLIPLoader` | 2 |  |
| `PrimitiveStringMultiline` | 2 |  |
| `BatchImagesNode` | 1 |  |
| `ComfySwitchNode` | 1 |  |
| `ImageCompare` | 1 |  |
| `KSampler` | 1 |  |
| `LoadImage` | 1 |  |
| `PreviewAny` | 1 |  |
| `SaveImage` | 1 |  |
| `TextEncodeFibo2` | 1 |  |
| `TextGenerateV2` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Fibo 2.0 Edit (Dev, int8)</summary>

## Fibo 2.0: Image Edit (Dev, int8)

**Input Assets**
- [red_bowler_hat_portrait.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/red_bowler_hat_portrait.png) — required workflow input (`input/red_bowler_hat_portrait.png`)

One 8B flow-matching model does both editing and text-to-image, in the FLUX.2 VAE latent space, with prompts encoded by Qwen3-VL-4B. `fibo2_edit_turbo` is the step + CFG distillation of `fibo2_dev`.

Defaults here: **50 steps**, **CFG 5**, euler / simple, the settings Bria publishes for Dev. CFG is on, so `negative_prompt` carries Bria's structured VGL negative.

- Trained at ~1 MP. Stay near 1 MP: above that the coordinate origin stays top-left, so the prompt text leaks into the corner and adherence collapses.
- This is the full non-distilled base: the cleanest result, at roughly 12 times the sampling time. For quick direction tests load `fibo2_edit_turbo_int8_convrot` with **4 steps / CFG 1**.
- Fibo 2.0 reads structured VGL captions. Describe the **final** state of the target region and stop — writing "keep X unchanged" makes the model re-render the whole frame and invent props (measured: extra moon, extra signage).

## Result size (`TextEncodeFibo2` width / height)

These two widgets size the **result**, not the reference image:

- `0` = let the node pick Fibo 2.0's trained bucket for the first image's aspect ratio (about 1 MP; `1024 x 1024` when no image is connected).
- Any other value is floored to a multiple of 16 and becomes the output latent size `128 x (height/16) x (width/16)`, so the saved image is exactly `width x height`.
- With **one** reference image, that image is scaled and centre-cropped (lanczos) to exactly `width x height` first, because the edit lines up with the reference pixel for pixel. That crop is why a source at a non-bucket aspect ratio loses frame area: set `width`/`height` to the source size (floored to /16) to keep every pixel of the reference.
- With **several** reference images each one is resized to its own trained bucket instead, and `width`/`height` only size the result.
- Stay near 1 MP: above that the coordinate origin stays at the top-left, so prompt content leaks into the corner and adherence drops.
- `batch_size` is the latent batch and is independent of how many references are connected.

## Project Links

- [Fibo 2.0 Dev: model card](https://huggingface.co/briaai/Fibo-2.0-dev): full non-distilled base, 50 steps / guidance 5.0
- [Fibo 2.0 Edit Turbo: model card](https://huggingface.co/briaai/Fibo-2.0-edit-turbo): step + cfg distillation of Dev, 4 steps / guidance 1.0
- [Fibo 2 Scene Analyzer](https://huggingface.co/briaai/fibo-scene-analyzer): Bria's own model for VGL expansion and edit rewriting (the `<edit>` task is what the Prompt Enhancer imitates)
- [Bria VGL docs](https://docs.bria.ai/vgl) · [Bria-AI/vgl on GitHub](https://github.com/Bria-AI/vgl): the structured caption format this model reads
- [Fibo 2 release notes](https://docs.bria.ai/whats-new/fibo-2)
- [Tech paper (arXiv 2511.06876)](https://arxiv.org/abs/2511.06876)
- [Comfy-Org/Fibo-2.0](https://huggingface.co/Comfy-Org/Fibo-2.0): the repack this workflow loads · [Comfy-Org/Qwen3-VL](https://huggingface.co/Comfy-Org/Qwen3-VL): text encoder (and the optional 8B enhancer)

</details>

<details><summary>Note: Prompt Enhancer (PE)</summary>

## Prompt Enhancer (optional)

Fibo 2.0 reads structured VGL captions, so the enhancer turns a one-line instruction into a full scene description before it reaches `TextEncodeFibo2`.

- `TextGenerate` runs on `qwen3vl_8b_int8_convrot` (CLIPLoader type = fibo2). It needs the reference image, so `LoadImage` feeds **both** the enhancer and `TextEncodeFibo2`.
- `TextGenerate.system_prompt` is a **forceInput** (must be linked) and only takes effect while `use_default_template = true`. Paste Bria's edit rewrite prompt there — it is the same spec the API uses: preserve everything by default, describe the final image only, and put the single change into one imperative `edit_instruction`.
- `ComfySwitchNode` picks the enhanced text (`on_true`) or your raw prompt (`on_false`). Set `switch = false` to bypass. `PreviewAny` shows what the enhancer produced.
- Bria's own implementation of this step is [`briaai/fibo-scene-analyzer`](https://huggingface.co/briaai/fibo-scene-analyzer) (the `<edit>` task: 1-5 images + instruction → scene description); a local VLM plus the same system prompt is the cheap stand-in. Format reference: [Bria VGL docs](https://docs.bria.ai/vgl).

Shipped sampling (`TextGenerate`): `temperature 0.3`, `top_k 20`, `top_p 0.95`, `min_p 0.05`, `repetition_penalty 1.05`, `presence_penalty 0`, `max_length 3000`, `thinking off`, `mtp off`, seed `1234`. Low temperature and a small `top_k` keep the JSON stable; `max_length 3000` fits a full VGL caption (the schema default of 512 truncates it); `mtp off` keeps the same seed reproducible.

Measured on a reference image (same seed): prose with "keep X unchanged" made the model invent a moon, extra signage and a chest-pocket zip, while the VGL rewrite kept only the one requested front zip. Dev at 50 steps gave the finest embroidery and no invented hardware.

</details>

<details><summary>Note: Models</summary>

## Model Links

- [Hugging Face:Comfy-Org/Qwen3-VL](https://huggingface.co/Comfy-Org/Qwen3-VL)
- [ModelScope:Comfy-Org/Qwen3-VL](https://modelscope.cn/models/Comfy-Org/Qwen3-VL)
- [Hugging Face:Comfy-Org/Fibo-2.0](https://huggingface.co/Comfy-Org/Fibo-2.0)
- [ModelScope:Comfy-Org/Fibo-2.0](https://modelscope.cn/models/Comfy-Org/Fibo-2.0)

**diffusion_models**

- [fibo2_edit_turbo_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/diffusion_models/fibo2_edit_turbo_int8_convrot.safetensors)
- [fibo2_edit_turbo_bf16.safetensors](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/diffusion_models/fibo2_edit_turbo_bf16.safetensors) (full quality, 2× size)
- [fibo2_dev_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/diffusion_models/fibo2_dev_int8_convrot.safetensors) (non-distilled, 50 steps / CFG 5)
- [fibo_2.0_turbo_lora_avg_rank_270_bf16.safetensors](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/loras/fibo_2.0_turbo_lora_avg_rank_270_bf16.safetensors) (optional turbo LoRA for dev)

**text_encoders** — load with CLIPLoader **type = fibo2**

- [qwen3vl_4b_bf16.safetensors](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/text_encoders/qwen3vl_4b_bf16.safetensors)
- [qwen3vl_4b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/text_encoders/qwen3vl_4b_int8_convrot.safetensors) (int8_convrot alternative)
- [qwen3vl_8b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen3-VL/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors) — optional, only for the Prompt Enhancer

**vae**

- [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/Fibo-2.0/resolve/main/vae/flux2-vae.safetensors)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   ├── fibo2_edit_turbo_int8_convrot.safetensors
│   │   ├── fibo2_edit_turbo_bf16.safetensors
│   │   └── fibo2_dev_int8_convrot.safetensors
│   ├── 📂 text_encoders/
│   │   ├── qwen3vl_4b_bf16.safetensors
│   │   └── qwen3vl_8b_int8_convrot.safetensors
│   ├── 📂 loras/
│   │   └── fibo_2.0_turbo_lora_avg_rank_270_bf16.safetensors
│   └── 📂 vae/
│       └── flux2-vae.safetensors
```

## License

Weights © BRIA AI, [CC BY-NC 4.0](https://creativecommons.org/licenses/by-nc/4.0/). Non-commercial use only unless you have a separate BRIA agreement.

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
