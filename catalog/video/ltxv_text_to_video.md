# LTXV Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=ltxv_text_to_video)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/ltxv_text_to_video-1.webp" width="360" alt="LTXV Text to Video ltxv_text_to_video-1.webp">

> Generate videos from text prompts.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/ltxv_text_to_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/ltxv_text_to_video.json)
- [Tutorial](https://docs.comfy.org/tutorials/video/ltxv)

## Details

| | |
|---|---|
| Name | `ltxv_text_to_video` |
| Category | Foundation › Video |
| Output | video |
| Models | LTX-0.9.5 |
| Tags | Text to Video, Video |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 17.8 GB |
| Min ComfyUI version | 0.3.31 |
| Usage | 16 |
| Nodes | 14 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-video-2b-v0.9.safetensors` | `checkpoints` | [link](https://huggingface.co/Lightricks/LTX-Video/resolve/main/ltx-video-2b-v0.9.safetensors?download=true) |
| `t5xxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 |  |
| `CheckpointLoaderSimple` | 1 |  |
| `CLIPLoader` | 1 |  |
| `CreateVideo` | 1 |  |
| `EmptyLTXVLatentVideo` | 1 |  |
| `KSamplerSelect` | 1 |  |
| `LTXVConditioning` | 1 |  |
| `LTXVScheduler` | 1 |  |
| `MarkdownNote` | 1 |  |
| `Note` | 1 |  |
| `SamplerCustom` | 1 |  |
| `SaveVideo` | 1 |  |
| `VAEDecode` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
This model needs long descriptive prompts, if the prompt is too short the quality will suffer greatly.
```

</details>

<details><summary>MarkdownNote</summary>

🛈 [Learn more about this workflow](https://comfyanonymous.github.io/ComfyUI_examples/ltxv/)

</details>
