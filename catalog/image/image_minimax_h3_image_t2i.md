# MiniMax-H3-Image: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_minimax_h3_image_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_minimax_h3_image_t2i-1.webp" width="360" alt="MiniMax-H3-Image: Text to Image image_minimax_h3_image_t2i-1.webp">

> Generate a photoreal or graphic image from a text prompt with MiniMax-H3-Image, an open-weights model whose single checkpoint handles both text-to-image and image editing. Generation is distilled to 6 steps with no CFG and outputs about 16 MP natively, and an optional prompt expander turns a short request into the detailed caption the model reads best.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_minimax_h3_image_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_minimax_h3_image_t2i.json)

## Details

| | |
|---|---|
| Name | `image_minimax_h3_image_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | MiniMax H3 Image |
| Tags | Text to Image |
| Type | open source |
| Date | 2026-11-10 |
| Author | ComfyUI |
| Download size | 62.0 GB |
| Min ComfyUI version | 0.45.0 |
| Usage | 3357 |
| Nodes | 20 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #9 | image | image_minimax_h3_image_t2i.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `minimax_h3_image_pruned_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/diffusion_models/minimax_h3_image_pruned_int8_convrot.safetensors) |
| `qwen3.5_9b_w4a8_gptq.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen3.5/resolve/main/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors) |
| `qwen3vl_32b_minimax_h3_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_int8_convrot.safetensors) |
| `minimax_h3_image_vae_fp16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/vae/minimax_h3_image_vae_fp16.safetensors) |

## Subgraphs

- **Text to Image (MiniMax H3 Image)** (16 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveStringMultiline` | 3 |  |
| `CLIPLoader` | 2 |  |
| `MarkdownNote` | 2 |  |
| `ComfySwitchNode` | 1 |  |
| `ConditioningZeroOut` | 1 |  |
| `JsonExtractString` | 1 |  |
| `KSampler` | 1 |  |
| `MiniMaxH3ImageConditioning` | 1 |  |
| `PreviewAny` | 1 |  |
| `ResolutionSelector` | 1 |  |
| `SaveImage` | 1 |  |
| `StringReplace` | 1 |  |
| `TextGenerateV2` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: size</summary>

MiniMax H3 Image is native at about 16 MP, so this workflow defaults to 16 MP (4096x4096 at 1:1). Effective range is about 4 MP to 20 MP: lower `megapixels` to 4 MP on a small GPU or for faster runs, going higher gains nothing.

**Settings** - 6 steps, CFG 1.0, `euler` + `simple`, fixed by the CFG-distilled checkpoint. The negative is a `Conditioning Zero Out` and is never read. `switch` on the subgraph is **on**, so `Generate Text` (Qwen3.5 9B) rewrites your prompt first.

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

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

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
