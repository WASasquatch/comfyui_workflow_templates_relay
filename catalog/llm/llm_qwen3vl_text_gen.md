# Qwen3-VL: Text Generation

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/llm_qwen3vl_text_gen-1.webp" width="360" alt="Qwen3-VL: Text Generation llm_qwen3vl_text_gen-1.webp">

> Generate text with visual understanding using Qwen3-VL models, processing one input image to produce contextual text responses. Ideal for image captioning, visual question answering, and multimodal content generation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/llm_qwen3vl_text_gen.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/llm_qwen3vl_text_gen.json)

## Details

| | |
|---|---|
| Name | `llm_qwen3vl_text_gen` |
| Category | Foundation › LLM |
| Media type | image |
| Models | Qwen 3.0 |
| Tags | Text Generation |
| Type | open source |
| Date | 2026-06-23 |
| Author | ComfyUI |
| Download size | 4.9 GB |
| Min ComfyUI version | 0.44.0 |
| Usage | 99 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #8 | image | example.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen3vl_4b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen3-VL/resolve/main/text_encoders/qwen3vl_4b_fp8_scaled.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPLoader` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `PreviewAny` | 1 | comfy-core |
| `TextGenerateV2` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

**Input Assets**
- [example.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/example.png) — required workflow input (`input/example.png`)

- [#14298](https://github.com/Comfy-Org/ComfyUI/pull/14298)

## Model Links

- [Hugging Face:Comfy-Org/Qwen3-VL](https://huggingface.co/Comfy-Org/Qwen3-VL)

**ModelScope mirrors** (alternative repo location)

- [ModelScope:Comfy-Org/Qwen3-VL](https://modelscope.cn/models/Comfy-Org/Qwen3-VL)

**text_encoders**

- [qwen3vl_4b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen3-VL/resolve/main/text_encoders/qwen3vl_4b_fp8_scaled.safetensors) (4.88 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 text_encoders/
│       └── qwen3vl_4b_fp8_scaled.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
