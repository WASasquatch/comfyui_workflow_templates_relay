# ACE-Step 1.5 Music Generation (4B LLM )

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=audio_ace_step_1_5_split_4b)

[▶ audio_ace_step_1_5_split_4b-1.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_ace_step_1_5_split_4b-1.mp3)

> Input a text prompt to generate music. This 4B model version offers stronger audio understanding and composition capabilities compared to smaller variants.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_ace_step_1_5_split_4b.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_ace_step_1_5_split_4b.json)

## Details

| | |
|---|---|
| Name | `audio_ace_step_1_5_split_4b` |
| Category | Foundation › Audio |
| Output | audio |
| Models | ACE-Step |
| Tags | Audio, Music, Text to Audio |
| Type | open source |
| Date | 2026-02-05 |
| Author | ComfyUI |
| Download size | 13.7 GB |
| Min ComfyUI version | 0.25.0 |
| Usage | 24 |
| Nodes | 13 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `acestep_v1.5_turbo.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/diffusion_models/acestep_v1.5_turbo.safetensors) |
| `qwen_0.6b_ace15.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_0.6b_ace15.safetensors) |
| `qwen_4b_ace15.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_4b_ace15.safetensors) |
| `ace_1.5_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/vae/ace_1.5_vae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveNode` | 2 |  |
| `ConditioningZeroOut` | 1 | comfy-core |
| `DualCLIPLoader` | 1 | comfy-core |
| `EmptyAceStep1.5LatentAudio` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `SaveAudioMP3` | 1 | comfy-core |
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

**diffusion_models**

- [acestep_v1.5_turbo.safetensors](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/diffusion_models/acestep_v1.5_turbo.safetensors) (4.46 GB)

**vae**

- [ace_1.5_vae.safetensors](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/vae/ace_1.5_vae.safetensors) (321.8 MB)

**text_encoders**

- [qwen_0.6b_ace15.safetensors](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_0.6b_ace15.safetensors) (1.11 GB)
- [qwen_4b_ace15.safetensors](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_4b_ace15.safetensors) (7.8 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── acestep_v1.5_turbo.safetensors
│   ├── 📂 vae/
│   │   └── ace_1.5_vae.safetensors
│   └── 📂 text_encoders/
│       ├── qwen_0.6b_ace15.safetensors
│       └── qwen_4b_ace15.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
