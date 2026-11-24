# LTXV Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/ltxv_image_to_video-1.webp" width="360" alt="LTXV Image to Video ltxv_image_to_video-1.webp">

> Generate videos from still images.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/ltxv_image_to_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/ltxv_image_to_video.json)
- [Tutorial](https://docs.comfy.org/tutorials/video/ltxv)

## Details

| | |
|---|---|
| Name | `ltxv_image_to_video` |
| Category | Foundation › Video |
| Media type | image |
| Models | LTX-0.9.5 |
| Tags | Image to Video, Video |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 17.8 GB |
| Min ComfyUI version | 0.3.31 |
| Usage | 15 |
| Nodes | 15 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #78 | image | ltxv_image_to_video_input_image.jpg |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-video-2b-v0.9.5.safetensors` | `checkpoints` | [link](https://huggingface.co/Lightricks/LTX-Video/resolve/main/ltx-video-2b-v0.9.5.safetensors) |
| `t5xxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LTXVConditioning` | 1 | comfy-core |
| `LTXVImgToVideo` | 1 | comfy-core |
| `LTXVScheduler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `Note` | 1 |  |
| `SamplerCustom` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
This model needs long descriptive prompts, if the prompt is too short the quality will suffer greatly.
```

</details>

<details><summary>MarkdownNote</summary>

## Model links

**checkpoints**

- [ltx-video-2b-v0.9.5.safetensors](https://huggingface.co/Lightricks/LTX-Video/resolve/main/ltx-video-2b-v0.9.5.safetensors) (5.91 GB)

**text_encoders**

- [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) (9.12 GB)


Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │      └── ltx-video-2b-v0.9.5.safetensors
│   └── 📂 text_encoders/
│          └── t5xxl_fp16.safetensors
```

</details>
