# ACE-Step 1.5 Music Generation Workflow

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md)

[▶ audio_ace_step_1_5_split-1.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_ace_step_1_5_split-1.mp3)

> Input a text prompt describing the music style and optional lyrics. Generate a full, high-quality audio song in under 10 seconds on consumer hardware.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_ace_step_1_5_split.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_ace_step_1_5_split.json)

## Details

| | |
|---|---|
| Name | `audio_ace_step_1_5_split` |
| Category | Foundation › Audio |
| Media type | audio |
| Models | ACE-Step |
| Tags | Audio, Text to Audio, Music |
| Type | open source |
| Date | 2026-02-02 |
| Author | ComfyUI |
| Download size | 10.0 GB |
| Min ComfyUI version | 0.25.0 |
| Usage | 40 |
| Nodes | 13 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `acestep_v1.5_turbo.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/diffusion_models/acestep_v1.5_turbo.safetensors) |
| `qwen_0.6b_ace15.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_0.6b_ace15.safetensors) |
| `qwen_1.7b_ace15.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_1.7b_ace15.safetensors) |
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
| `SaveAudioAdvanced` | 1 | comfy-core |
| `TextEncodeAceStepAudio1.5` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecodeAudio` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Model Links

- [Hugging Face:Comfy-Org/ace_step_1.5_ComfyUI_files](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files)

### Alternative Repos

- [ModelScope:Comfy-Org/ace_step_1.5_ComfyUI_files](https://modelscope.cn/models/Comfy-Org/ace_step_1.5_ComfyUI_files)

**diffusion_models**

- [acestep_v1.5_turbo.safetensors](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/diffusion_models/acestep_v1.5_turbo.safetensors) (4.46 GB)

**text_encoders**

- [qwen_0.6b_ace15.safetensors](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_0.6b_ace15.safetensors) (1.11 GB)
- [qwen_1.7b_ace15.safetensors](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_1.7b_ace15.safetensors) (3.45 GB)

**vae**

- [ace_1.5_vae.safetensors](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/vae/ace_1.5_vae.safetensors) (321.8 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── acestep_v1.5_turbo.safetensors
│   ├── 📂 text_encoders/
│   │   ├── qwen_0.6b_ace15.safetensors
│   │   └── qwen_1.7b_ace15.safetensors
│   └── 📂 vae/
│       └── ace_1.5_vae.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
