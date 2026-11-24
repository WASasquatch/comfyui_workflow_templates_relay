# Qwen3.0: Text Generation

[← LLM](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=llm_qwen3_text_gen)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/llm_qwen3_text_gen-1.webp" width="360" alt="Qwen3.0: Text Generation llm_qwen3_text_gen-1.webp">

> Input a text prompt to generate detailed, reasoned responses using the Qwen3-4B-Thinking model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/llm_qwen3_text_gen.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/llm_qwen3_text_gen.json)
- [Tutorial](https://docs.comfy.org/tutorials/llm/qwen/qwen3)

## Details

| | |
|---|---|
| Name | `llm_qwen3_text_gen` |
| Category | Foundation › LLM |
| Output | llm |
| Models | Qwen 3.0 |
| Tags | Text Generation |
| Type | open source |
| Date | 2026-02-23 |
| Author | ComfyUI |
| Download size | 7.5 GB |
| Min ComfyUI version | 0.15.0 |
| Usage | 30 |
| Nodes | 5 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_3_4b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/flux2-klein/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `CLIPLoader` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `TextGenerate` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Related PR: [#12392](https://github.com/Comfy-Org/ComfyUI/pull/12392), [#12537](https://github.com/Comfy-Org/ComfyUI/pull/12537)
## Model Links

**text_encoders**

- [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/flux2-klein/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) (7.49 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 text_encoders/
│       └── qwen_3_4b.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Supported Model</summary>

For Qwen 3.0, ComfyUI only supports the 4B model at the moment (2026/3).

</details>
