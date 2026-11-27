# Qwen3.5: Text Generation

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=llm_qwen3_5_text_gen)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/llm_qwen3_5_text_gen-1.webp" width="360" alt="Qwen3.5: Text Generation llm_qwen3_5_text_gen-1.webp">

> Use the Qwen3.5 model to analyze an input image and generate descriptive text prompts. This workflow performs image captioning and reverse prompt engineering.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/llm_qwen3_5_text_gen.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/llm_qwen3_5_text_gen.json)
- [Tutorial](https://docs.comfy.org/tutorials/llm/qwen/qwen3_5)

## Details

| | |
|---|---|
| Name | `llm_qwen3_5_text_gen` |
| Category | Foundation › LLM |
| Output | llm |
| Models | Qwen3.5 |
| Tags | Text Generation |
| Type | open source |
| Date | 2026-03-27 |
| Author | ComfyUI |
| Download size | 6.8 GB |
| Min ComfyUI version | 0.44.0 |
| Usage | 226 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | man_with_red_hat.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen3.5_9b_w4a8_gptq.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen3.5/resolve/main/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPLoader` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `PreviewAny` | 1 | comfy-core |
| `TextGenerateV2` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Related PR: https://github.com/Comfy-Org/ComfyUI/pull/12771
## Model Links

- [Hugging Face:Comfy-Org/Qwen3.5](https://huggingface.co/Comfy-Org/Qwen3.5)
- [ModelScope:Comfy-Org/Qwen3.5](https://modelscope.cn/models/Comfy-Org/Qwen3.5)

**text_encoders**

- [qwen3.5_9b_w4a8_gptq.safetensors](https://huggingface.co/Comfy-Org/Qwen3.5/resolve/main/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors) (7.34 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 text_encoders/
│       └── qwen3.5_9b_w4a8_gptq.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
