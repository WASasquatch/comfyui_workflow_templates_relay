# Stable Audio 1.0: Text to Audio

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=audio_stable_audio_example)

[▶ audio_stable_audio_example-1.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_stable_audio_example-1.mp3) <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_stable_audio_example-1.webp" width="360" alt="Stable Audio 1.0: Text to Audio audio_stable_audio_example-1.webp">

> Generate audio from text prompts using Stable Audio.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_stable_audio_example.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_stable_audio_example.json)
- [Tutorial](https://comfyanonymous.github.io/ComfyUI_examples/audio/)

## Details

| | |
|---|---|
| Name | `audio_stable_audio_example` |
| Category | Foundation › Audio |
| Output | audio |
| Models | Stability, Stable Audio |
| Tags | Audio, Text to Audio |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 5.3 GB |
| Min ComfyUI version | 0.25.0 |
| Usage | 14 |
| Nodes | 9 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `stable-audio-open-1.0.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/stable-audio-open-1.0_repackaged/resolve/main/stable-audio-open-1.0.safetensors) |
| `t5-base.safetensors` | `text_encoders` | [link](https://huggingface.co/ComfyUI-Wiki/t5-base/resolve/main/t5-base.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 |  |
| `CheckpointLoaderSimple` | 1 |  |
| `CLIPLoader` | 1 |  |
| `EmptyLatentAudio` | 1 |  |
| `KSampler` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |
| `VAEDecodeAudio` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Model Links

- [Hugging Face:Comfy-Org/stable-audio-open-1.0_repackaged](https://huggingface.co/Comfy-Org/stable-audio-open-1.0_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/stable-audio-open-1.0_repackaged](https://modelscope.cn/models/Comfy-Org/stable-audio-open-1.0_repackaged)

**checkpoints**

- [stable-audio-open-1.0.safetensors](https://huggingface.co/Comfy-Org/stable-audio-open-1.0_repackaged/resolve/main/stable-audio-open-1.0.safetensors) (4.52 GB)

**text_encoders**

- [t5-base.safetensors](https://huggingface.co/ComfyUI-Wiki/t5-base/resolve/main/t5-base.safetensors) (850.3 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │      └── stable-audio-open-1.0.safetensors
│   └── 📂 text_encoders/
│          └── t5-base.safetensors
```

</details>
