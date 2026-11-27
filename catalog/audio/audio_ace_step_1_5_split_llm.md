# ACE-Step 1.5 AI Lyric Song Generation

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=audio_ace_step_1_5_split_llm)

[▶ audio_ace_step_1_5_split_llm-1.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_ace_step_1_5_split_llm-1.mp3)

> Input a music style and optional lyrics. Generate a full song with AI-created lyrics and audio.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_ace_step_1_5_split_llm.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_ace_step_1_5_split_llm.json)

## Details

| | |
|---|---|
| Name | `audio_ace_step_1_5_split_llm` |
| Category | Foundation › Audio |
| Output | audio |
| Models | ACE-Step, Google Gemini |
| Tags | API, Text to Audio |
| Type | API |
| Date | 2026-02-09 |
| Author | ComfyUI |
| Download size | 9.3 GB |
| Min ComfyUI version | 0.36.0 |
| Usage | 19 |
| Nodes | 17 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveAudioAdvanced` #111 | audio | audio_ace_step_1_5_split_llm.flac |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `acestep_v1.5_turbo.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/diffusion_models/acestep_v1.5_turbo.safetensors) |
| `qwen_0.6b_ace15.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_0.6b_ace15.safetensors) |
| `qwen_4b_ace15.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_4b_ace15.safetensors) |
| `ace_1.5_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/vae/ace_1.5_vae.safetensors) |

## Subgraphs

- **Text to Audio (ACE-Step 1.5)** (11 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `RegexExtract` | 2 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `DualCLIPLoader` | 1 | comfy-core |
| `EmptyAceStep1.5LatentAudio` | 1 | comfy-core |
| `GeminiNodeV3` | 1 |  |
| `KSampler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `PrimitiveFloat` | 1 | comfy-core |
| `SaveAudioAdvanced` | 1 |  |
| `SeedNode` | 1 |  |
| `TextEncodeAceStepAudio1.5` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecodeAudio` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/ace_step_1.5_ComfyUI_files](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files)

### Alternative Repos

- [ModelScope:Comfy-Org/ace_step_1.5_ComfyUI_files](https://modelscope.cn/models/Comfy-Org/ace_step_1.5_ComfyUI_files)

**text_encoders**

- [qwen_0.6b_ace15.safetensors](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_0.6b_ace15.safetensors) (1.11 GB)
- [qwen_4b_ace15.safetensors](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_4b_ace15.safetensors) (7.8 GB)

**vae**

- [ace_1.5_vae.safetensors](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/vae/ace_1.5_vae.safetensors) (321.8 MB)

**diffusion_models**

- [acestep_v1.5_turbo.safetensors](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/diffusion_models/acestep_v1.5_turbo.safetensors) (4.46 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   ├── qwen_0.6b_ace15.safetensors
│   │   └── qwen_4b_ace15.safetensors
│   ├── 📂 vae/
│   │   └── ace_1.5_vae.safetensors
│   └── 📂 diffusion_models/
│       └── acestep_v1.5_turbo.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
