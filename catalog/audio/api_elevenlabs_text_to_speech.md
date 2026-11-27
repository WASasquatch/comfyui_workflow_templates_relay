# ElevenLabs: Text to Speech

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_elevenlabs_text_to_speech)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_elevenlabs_text_to_speech-1.webp" width="360" alt="ElevenLabs: Text to Speech api_elevenlabs_text_to_speech-1.webp">

> Input text to generate speech with ultra-realistic voices, or upload a voice sample to clone it for synthesis.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_elevenlabs_text_to_speech.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_elevenlabs_text_to_speech.json)

## Details

| | |
|---|---|
| Name | `api_elevenlabs_text_to_speech` |
| Category | Foundation › Audio |
| Output | audio |
| Models | ElevenLabs |
| Tags | Text to Speech, Audio, API |
| Type | API |
| Date | 2026-02-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.25.0 |
| Usage | 60 |
| Nodes | 8 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #210 | audio | chatterbox_input_gettysburg.wav |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ElevenLabsInstantVoiceClone` | 1 | comfy-core |
| `ElevenLabsTextToSpeech` | 1 | comfy-core |
| `ElevenLabsVoiceSelector` | 1 | comfy-core |
| `LoadAudio` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `Note` | 1 |  |
| `RecordAudio` | 1 | comfy-core |
| `SaveAudioAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>How to enable bypassed nodes</summary>

```text
Please select and use Ctrl-B to enable the bypassed nodes.
```

</details>

<details><summary>MarkdownNote</summary>

## Input Asset

- [chatterbox_input_gettysburg.wav](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/chatterbox_input_gettysburg.wav)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
