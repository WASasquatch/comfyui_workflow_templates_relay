# ACE-Step 1.5XL SFT: Text to Music

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=audio_ace_step1_5_xl_sft)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_ace_step1_5_xl_sft-1.webp" width="360" alt="ACE-Step 1.5XL SFT: Text to Music audio_ace_step1_5_xl_sft-1.webp">

> Generate high-quality music from text prompts using a 4B parameter SFT model. Control output with CFG for precise prompt adherence.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/audio_ace_step1_5_xl_sft.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/audio_ace_step1_5_xl_sft.json)

## Details

| | |
|---|---|
| Name | `audio_ace_step1_5_xl_sft` |
| Category | Foundation › Audio |
| Output | audio |
| Models | ACE-Step |
| Tags | Text to Music |
| Type | open source |
| Date | 2026-04-10 |
| Author | ComfyUI |
| Download size | 18.5 GB |
| Min ComfyUI version | 0.25.0 |
| Usage | 76 |
| Nodes | 12 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `acestep_v1.5_xl_sft_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/diffusion_models/acestep_v1.5_xl_sft_bf16.safetensors) |
| `qwen_0.6b_ace15.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_0.6b_ace15.safetensors) |
| `qwen_4b_ace15.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_4b_ace15.safetensors) |
| `ace_1.5_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/vae/ace_1.5_vae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ConditioningZeroOut` | 1 | comfy-core |
| `DualCLIPLoader` | 1 | comfy-core |
| `EmptyAceStep1.5LatentAudio` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PrimitiveInt` | 1 | comfy-core |
| `PrimitiveNode` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |
| `TextEncodeAceStepAudio1.5` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecodeAudio` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
