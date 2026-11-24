# ElevenLabs: Speech to Speech

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_elevenlabs_speech_to_speech-1.webp" width="360" alt="ElevenLabs: Speech to Speech api_elevenlabs_speech_to_speech-1.webp">

> Upload a source audio file to apply a new voice tone or clone a different voice, generating a modified audio output.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_elevenlabs_speech_to_speech.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_elevenlabs_speech_to_speech.json)

## Details

| | |
|---|---|
| Name | `api_elevenlabs_speech_to_speech` |
| Category | Foundation › Audio |
| Media type | image |
| Models | ElevenLabs |
| Tags | Voice Cloning, API |
| Type | API |
| Date | 2026-02-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.25.0 |
| Usage | 50 |
| Nodes | 8 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #210 | audio | long_demo.mp3 |
| input | `LoadAudio` #221 | audio | api_elevenlabs_speech_to_speech.mp3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadAudio` | 2 | comfy-core |
| `ElevenLabsInstantVoiceClone` | 1 | comfy-core |
| `ElevenLabsSpeechToSpeech` | 1 | comfy-core |
| `ElevenLabsVoiceSelector` | 1 | comfy-core |
| `Note` | 1 |  |
| `RecordAudio` | 1 | comfy-core |
| `SaveAudioAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>How to enable bypassed nodes</summary>

```text
Please select and use Ctrl-B to enable the bypassed nodes.
```

</details>
