# Stable Audio 3.0 Medium Base

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=audio_stable_audio_3_medium_base)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_stable_audio_3_medium_base-1.webp" width="360" alt="Stable Audio 3.0 Medium Base audio_stable_audio_3_medium_base-1.webp">

> Input a short text description of a sound, music, or effect. The workflow expands your prompt with Qwen and generates a stereo audio clip from Stable Audio 3.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_stable_audio_3_medium_base.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_stable_audio_3_medium_base.json)

## Details

| | |
|---|---|
| Name | `audio_stable_audio_3_medium_base` |
| Category | Foundation › Audio |
| Output | audio |
| Models | Stable Audio |
| Tags | Text to Audio |
| Type | open source |
| Date | 2026-05-20 |
| Author | ComfyUI |
| Download size | 14.8 GB |
| Min ComfyUI version | 0.44.0 |
| Usage | 112 |
| Nodes | 24 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `stable_audio_3_medium_base.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/stable-audio-3/resolve/main/checkpoints/stable_audio_3_medium_base.safetensors) |
| `qwen3.5_2b_bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen3.5/resolve/main/text_encoders/qwen3.5_2b_bf16.safetensors) |
| `t5gemma_b_b_ul2.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/stable-audio-3/resolve/main/text_encoders/t5gemma_b_b_ul2.safetensors) |

## Subgraphs

- **Audio Generation (Stable Audio 3 Medium Base)** (21 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `StringReplace` | 3 |  |
| `CLIPLoader` | 2 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `PreviewAny` | 2 |  |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `ComfyMathExpression` | 1 |  |
| `ComfySwitchNode` | 1 |  |
| `CustomCombo` | 1 |  |
| `EmptyLatentAudio` | 1 | comfy-core |
| `JsonExtractString` | 1 |  |
| `KSampler` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 |  |
| `PrimitiveFloat` | 1 |  |
| `PrimitiveStringMultiline` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |
| `TextGenerateV2` | 1 | comfy-core |
| `VAEDecodeAudio` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: About Stable Audio 3</summary>

## Stable Audio 3

**Stable Audio 3** turns a **text description** into **stereo audio**: music, instruments, SFX, short one-shots, and similar material, guided by what you write (style, instruments, energy, length, and so on).

**What this graph does:** you supply a **short idea**. The workflow can **expand it with Qwen** using a **category-aware** reprompt template (Music / Instrument / SFX / One-shot), then runs the **Stable Audio** checkpoint so the expanded text becomes a **full clip**. The subgraph returns **`AUDIO`** (decoded waveform).

---

## About the Audio Generation (Stable Audio 3 Base)  subgraph

**Inputs** (same order as pins on the subgraph node)

- `user_input` — short text fed into the reprompt template.
- `duration` — clip length in seconds.
- `seed` — KSampler seed.
- `use_reprompt` — enables the reprompt / text-switch path.
- `category` — reprompt preset (Music, Instrument, SFX, One-shot).
- `ckpt_name` — Stable Audio checkpoint.
- `sa_clip` — text encoder for Stable Audio conditioning.
- `qwen_clip` — text encoder for Qwen TextGenerate.

**Output:** `AUDIO`

</details>

<details><summary>Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Qwen3.5](https://huggingface.co/Comfy-Org/Qwen3.5)
- [ModelScope:Comfy-Org/Qwen3.5](https://modelscope.cn/models/Comfy-Org/Qwen3.5)

-  [Comfy-Org/stable-audio-3](https://huggingface.co/Comfy-Org/stable-audio-3)
- [ModelScope:Comfy-Org/stable-audio-3](https://modelscope.cn/models/Comfy-Org/stable-audio-3)

**text_encoders**

- [qwen3.5_2b_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen3.5/resolve/main/text_encoders/qwen3.5_2b_bf16.safetensors) (4.24 GB)
- [t5gemma_b_b_ul2.safetensors](https://huggingface.co/Comfy-Org/stable-audio-3/resolve/main/text_encoders/t5gemma_b_b_ul2.safetensors) (1.11 GB)

**checkpoints**

- [stable_audio_3_medium_base.safetensors](https://huggingface.co/Comfy-Org/stable-audio-3/resolve/main/checkpoints/stable_audio_3_medium_base.safetensors) (8.59 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   ├── qwen3.5_2b_bf16.safetensors
│   │   └── t5gemma_b_b_ul2.safetensors
│   └── 📂 checkpoints/
│       └── stable_audio_3_medium_base.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
