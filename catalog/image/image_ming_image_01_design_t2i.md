# Ming Image 0.1 Design: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_ming_image_01_design_t2i-1.webp" width="360" alt="Ming Image 0.1 Design: Text to Image image_ming_image_01_design_t2i-1.webp">

> Generate text-heavy design compositions from text prompts using Ming Image 0.1 Design, a 6B model tuned for UI screens, infographics, and posters. It takes no file inputs and produces one image, supporting transparent backgrounds for easy layering. Ideal for interface mockups, marketing posters, and data-rich infographic drafts.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_ming_image_01_design_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_ming_image_01_design_t2i.json)

## Details

| | |
|---|---|
| Name | `image_ming_image_01_design_t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | Ming Image |
| Tags | Int8, Text to Image |
| Type | open source |
| Date | 2026-09-25 |
| Author | ComfyUI |
| Download size | 40.3 GB |
| Min ComfyUI version | 0.44.0 |
| Usage | 20 |
| Nodes | 25 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImageAdvanced` #84 | image | image_ming_image_01_design_t2i.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ming_image_0.1_design_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Ming-Image/resolve/main/diffusion_models/ming_image_0.1_design_int8_convrot.safetensors) |
| `ming_image_0.1_ling_mini_2.0_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Ming-Image/resolve/main/text_encoders/ming_image_0.1_ling_mini_2.0_int8_convrot.safetensors) |
| `qwen3.8_27b_w4a8.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen3.8-27B/resolve/main/text_encoders/qwen3.8_27b_w4a8.safetensors) |
| `ming_image_vae_bf16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Ming-Image/resolve/main/vae/ming_image_vae_bf16.safetensors) |

## Subgraphs

- **Text to Image (Ming Image 0.1 Design)** (21 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPLoader` | 2 |  |
| `MarkdownNote` | 2 |  |
| `PrimitiveInt` | 2 |  |
| `PrimitiveStringMultiline` | 2 |  |
| `BasicGuider` | 1 |  |
| `BasicScheduler` | 1 |  |
| `CLIPTextEncode` | 1 |  |
| `ComfySwitchNode` | 1 |  |
| `EmptyLatentImage` | 1 |  |
| `KSamplerSelect` | 1 |  |
| `ModelAttentionBackend` | 1 |  |
| `ModelSamplingFlux` | 1 |  |
| `PreviewAny` | 1 |  |
| `RandomNoise` | 1 |  |
| `ResolutionSelector` | 1 |  |
| `SamplerCustomAdvanced` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
| `TextGenerateV2` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links
- [Hugging Face:Comfy-Org/Ming-Image](https://huggingface.co/Comfy-Org/Ming-Image)
- [ModelScope:Comfy-Org/Ming-Image](https://modelscope.cn/models/Comfy-Org/Ming-Image)
- [Hugging Face:Comfy-Org/Qwen3.8-27B](https://huggingface.co/Comfy-Org/Qwen3.8-27B)
- [ModelScope:Comfy-Org/Qwen3.8-27B](https://modelscope.cn/models/Comfy-Org/Qwen3.8-27B)


**text_encoders**

- [qwen3.8_27b_w4a8.safetensors](https://huggingface.co/Comfy-Org/Qwen3.8-27B/resolve/main/text_encoders/qwen3.8_27b_w4a8.safetensors) (16.1 GB)
- [ming_image_0.1_ling_mini_2.0_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Ming-Image/resolve/main/text_encoders/ming_image_0.1_ling_mini_2.0_int8_convrot.safetensors) (18.17 GB)

**diffusion_models**

- [ming_image_0.1_design_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Ming-Image/resolve/main/diffusion_models/ming_image_0.1_design_int8_convrot.safetensors) (5.75 GB)

**vae**

- [ming_image_vae_bf16.safetensors](https://huggingface.co/Comfy-Org/Ming-Image/resolve/main/vae/ming_image_vae_bf16.safetensors) (242.1 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   ├── qwen3.8_27b_w4a8.safetensors
│   │   └── ming_image_0.1_ling_mini_2.0_int8_convrot.safetensors
│   ├── 📂 diffusion_models/
│   │   └── ming_image_0.1_design_int8_convrot.safetensors
│   └── 📂 vae/
│       └── ming_image_vae_bf16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: Ming Image 0.1 Design</summary>

## Ming Image 0.1 Design

Ming Image 0.1 Design is a 6B text-to-image model from inclusionAI (Ant Group), built for design work: UI screens, infographics, posters and other text-heavy layouts. It outputs RGBA images with a real alpha channel, so a result can be dropped straight into a design file. Released under the MIT license.

What it is good at:

- Long, structured layouts: pages, posters and infographics with many sections, written section by section.
- Text rendering: strings quoted in the prompt are followed closely, so labels, prices and headings stay legible.
- Transparent output: transparent backgrounds and isolated elements for compositing.
- Prompt rewriting: an instruction-following VLM turns a short idea into a detailed layout caption before sampling.

The checkpoints this workflow needs, and where to put them, are listed in the **Model Links** note next to this one.

## How to use this workflow

1. Enter the **Text to Image (Ming Image 0.1 Design)** subgraph with the **Enter subgraph** button at the bottom of the node.
2. Write your prompt in the `prompt` field, describing the layout section by section and putting any copy you want rendered in quotes.
3. Choose the canvas with the `ResolutionSelector` node: 2048 x 2048 gives the best quality, 1024 x 1024 is faster.
4. Keep the prompt enhancer on to let Qwen3.8-27B expand your prompt, or switch `enable_PE` off to send your text exactly as typed. The enhancer runs the rewriter system prompt released by the model authors, see below.
5. Queue the prompt: the decoded image appears in the `PreviewImage` node.
6. For a transparent background, prepend one RGBA phrase to your prompt, for example `RGBA, 4-channel, transparent background`.

## Prompt guide

- [Text-to-image prompt rewriting](https://github.com/inclusionAI/Ming-Image#text-to-image-prompt-rewriting): the official prompt structure and the [rewriter system prompt](https://github.com/inclusionAI/Ming-Image/blob/main/assets/t2i_rewriter_system_prompt.txt) that this workflow's prompt enhancer runs.
- [Transparent-background generation tip](https://github.com/inclusionAI/Ming-Image#transparent-background-generation-tip): the fixed RGBA phrases to prepend.

</details>
