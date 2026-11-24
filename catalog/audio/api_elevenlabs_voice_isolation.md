# ElevenLabs: Voice Isolation

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_elevenlabs_voice_isolation)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_elevenlabs_voice_isolation-1.webp" width="360" alt="ElevenLabs: Voice Isolation api_elevenlabs_voice_isolation-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_elevenlabs_voice_isolation-2.webp" width="360" alt="ElevenLabs: Voice Isolation api_elevenlabs_voice_isolation-2.webp">

> Upload an audio file containing background noise. Use the ElevenLabs API to isolate and output a clean voice track.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_elevenlabs_voice_isolation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_elevenlabs_voice_isolation.json)

## Details

| | |
|---|---|
| Name | `api_elevenlabs_voice_isolation` |
| Category | Foundation › Audio |
| Output | audio |
| Models | ElevenLabs |
| Tags | API, Audio Editing |
| Type | API |
| Date | 2026-02-21 |
| Author | ComfyUI |
| Min ComfyUI version | 0.25.0 |
| Usage | 13 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #131 | audio | noisy_background.mp3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ElevenLabsAudioIsolation` | 1 | comfy-core |
| `LoadAudio` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [noisy_background.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/noisy_background.mp3)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
