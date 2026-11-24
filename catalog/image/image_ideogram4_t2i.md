# Ideogram v4: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_ideogram4_t2i-1.webp" width="360" alt="Ideogram v4: Text to Image image_ideogram4_t2i-1.webp">

> Input a text prompt or structured JSON description. Generate an image with precise layout, color, and style control using Ideogram 4.0.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_ideogram4_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_ideogram4_t2i.json)

## Details

| | |
|---|---|
| Name | `image_ideogram4_t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | Ideogram |
| Tags | Text to Image |
| Type | open source |
| Date | 2026-06-03 |
| Author | ComfyUI |
| Download size | 24.7 GB |
| Min ComfyUI version | 0.24.0 |
| Usage | 34 |
| Nodes | 42 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #158 | image | image_ideogram4_t2i.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ideogram4_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Ideogram-4/resolve/main/diffusion_models/ideogram4_fp8_scaled.safetensors) |
| `ideogram4_unconditional_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Ideogram-4/resolve/main/diffusion_models/ideogram4_unconditional_fp8_scaled.safetensors) |
| `qwen3vl_8b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen3-VL/resolve/main/text_encoders/qwen3vl_8b_fp8_scaled.safetensors) |
| `flux2-vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) |

## Subgraphs

- **Text to Image (Ideogram v4)** (27 nodes)
- **Ideogram4 Caption Prompt Template** (9 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfyMathExpression` | 4 | comfy-core |
| `JsonExtractString` | 4 | comfy-core |
| `StringReplace` | 4 | comfy-core |
| `ComfyNumberConvert` | 3 | comfy-core |
| `MarkdownNote` | 3 |  |
| `PreviewAny` | 3 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `PrimitiveStringMultiline` | 2 | comfy-core |
| `UNETLoader` | 2 | comfy-core |
| `CFGOverride` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `CustomCombo` | 1 | comfy-core |
| `DualModelGuider` | 1 | comfy-core |
| `EmptyFlux2LatentImage` | 1 | comfy-core |
| `Ideogram4Scheduler` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `ResolutionSelector` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Model link</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/flux2-dev](https://huggingface.co/Comfy-Org/flux2-dev)
- [ModelScope:Comfy-Org/flux2-dev](https://modelscope.cn/models/Comfy-Org/flux2-dev)
- [Hugging Face:Comfy-Org/Ideogram-4](https://huggingface.co/Comfy-Org/Ideogram-4)
- [ModelScope:Comfy-Org/Ideogram-4](https://modelscope.cn/models/Comfy-Org/Ideogram-4)
- [Hugging Face:Comfy-Org/Qwen3-VL](https://huggingface.co/Comfy-Org/Qwen3-VL)
- [ModelScope:Comfy-Org/Qwen3-VL](https://modelscope.cn/models/Comfy-Org/Qwen3-VL)
- [Hugging Face:Comfy-Org/gemma-4](https://huggingface.co/Comfy-Org/gemma-4)
- [ModelScope:Comfy-Org/gemma-4](https://modelscope.cn/models/Comfy-Org/gemma-4)

**vae**

- [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) (320.6 MB)

**diffusion_models**

- [ideogram4_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Ideogram-4/resolve/main/diffusion_models/ideogram4_fp8_scaled.safetensors) (8.64 GB)
- [ideogram4_unconditional_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Ideogram-4/resolve/main/diffusion_models/ideogram4_unconditional_fp8_scaled.safetensors) (8.64 GB)

**text_encoders**

- [qwen3vl_8b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen3-VL/resolve/main/text_encoders/qwen3vl_8b_fp8_scaled.safetensors) (9.86 GB)
- [gemma4_e4b_it_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/gemma-4/resolve/main/text_encoders/gemma4_e4b_it_fp8_scaled.safetensors) (8.44 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   └── flux2-vae.safetensors
│   ├── 📂 diffusion_models/
│   │   ├── ideogram4_fp8_scaled.safetensors
│   │   └── ideogram4_unconditional_fp8_scaled.safetensors
│   └── 📂 text_encoders/
│       ├── qwen3vl_8b_fp8_scaled.safetensors
│       └── gemma4_e4b_it_fp8_scaled.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: Ideogram 4.0</summary>

### About the model

The model is trained on **structured JSON captions** (scene summary, style block, background, and optional per-object descriptions with bounding boxes and hex color palettes). Official inference validates prompts against that schema. Guidance uses **flow-matching** with **asymmetric classifier-free guidance** (the unconditional pass drops text tokens)—not a separate negative prompt string.

**NOTE:**  If you see "Image blocked by safety filter", this is Ideogram 4.0's built-in safety filter. Non-JSON (plain-text) prompts have a higher false-positive rate. Using structured JSON prompts reduces the chance of your prompt being blocked. See the [official prompting guide](https://github.com/ideogram-oss/ideogram4/blob/main/docs/prompting.md#safety-filter) for details.

---

### How to build prompts here

**(a) Raw input**: Paste or type directly into the subgraph. You may use plain natural language, but **structured JSON** (as in the subgraph default) gives the most predictable layout and style control.

**(b) Model-assisted (LLM):** Use the **Ideogram4 Caption Prompt Template** output with any LLM tools to obtain the JSON format prompt

</details>

<details><summary>MarkdownNote</summary>

This is a prompt construction template. You can copy its input into any LLM to generate matching prompts.

---
You may try installing or updating [KJNodes](https://github.com/kijai/ComfyUI-KJNodes) and use the **Ideogram 4 Prompt Builder KJ** node to achieve visual control over prompts.

</details>
