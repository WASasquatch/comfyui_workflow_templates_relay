# ACE-Step 1.5 Music Generation AIO

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=audio_ace_step_1_5_checkpoint)

[▶ audio_ace_step_1_5_checkpoint-1.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_ace_step_1_5_checkpoint-1.mp3)

> Input style tags and lyrics to generate a full song. The workflow uses the ACE-Step 1.5 model to produce commercial-grade music in under 10 seconds on consumer hardware.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_ace_step_1_5_checkpoint.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_ace_step_1_5_checkpoint.json)

## Details

| | |
|---|---|
| Name | `audio_ace_step_1_5_checkpoint` |
| Category | Foundation › Audio |
| Output | audio |
| Models | ACE-Step |
| Tags | Audio, Music, Text to Audio |
| Type | open source |
| Date | 2026-02-03 |
| Author | ComfyUI |
| Download size | 10.0 GB |
| Min ComfyUI version | 0.25.0 |
| Usage | 74 |
| Nodes | 11 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ace_step_1.5_turbo_aio.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/checkpoints/ace_step_1.5_turbo_aio.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveNode` | 2 |  |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `EmptyAceStep1.5LatentAudio` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `SaveAudioAdvanced` | 1 |  |
| `TextEncodeAceStepAudio1.5` | 1 | comfy-core |
| `VAEDecodeAudio` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Model Links

- [Hugging Face:Comfy-Org/ace_step_1.5_ComfyUI_files](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files)

### Alternative Repos

- [ModelScope:Comfy-Org/ace_step_1.5_ComfyUI_files](https://modelscope.cn/models/Comfy-Org/ace_step_1.5_ComfyUI_files)

**checkpoints**

- [ace_step_1.5_turbo_aio.safetensors](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/checkpoints/ace_step_1.5_turbo_aio.safetensors) (9.34 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 checkpoints/
│       └── ace_step_1.5_turbo_aio.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
