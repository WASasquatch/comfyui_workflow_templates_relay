# ElevenLabs: Text to Dialogue

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_elevenlabs_text_to_dialogue)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_elevenlabs_text_to_dialogue-1.webp" width="360" alt="ElevenLabs: Text to Dialogue api_elevenlabs_text_to_dialogue-1.webp">

> Input text and select a voice profile to generate a high-quality, emotionally expressive audio dialogue.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_elevenlabs_text_to_dialogue.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_elevenlabs_text_to_dialogue.json)

## Details

| | |
|---|---|
| Name | `api_elevenlabs_text_to_dialogue` |
| Category | Foundation › Audio |
| Output | audio |
| Models | ElevenLabs |
| Tags | API, Text to Speech |
| Type | API |
| Date | 2026-02-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.25.0 |
| Usage | 30 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #210 | audio | long_demo.mp3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ElevenLabsVoiceSelector` | 2 | comfy-core |
| `ElevenLabsInstantVoiceClone` | 1 | comfy-core |
| `ElevenLabsTextToDialogue` | 1 | comfy-core |
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

- [long_demo.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/long_demo.mp3)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
