# Fish Audio: Speech to Text

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_fishaudio_speech_to_text-1.webp" width="360" alt="Fish Audio: Speech to Text api_fishaudio_speech_to_text-1.webp">

> Transcribe audio to text with Fish Audio ASR. Language is detected automatically across 80+ languages, with optional word-level timestamps returned as JSON segments. Use it to create subtitles, transcribe recordings, or generate text prompts from audio clips. A sample audio is pre-loaded so you can test it right away.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_fishaudio_speech_to_text.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_fishaudio_speech_to_text.json)

## Details

| | |
|---|---|
| Name | `api_fishaudio_speech_to_text` |
| Category | Foundation › Audio |
| Media type | image |
| Models | Fish Audio |
| Tags | API, Speech to Text |
| Type | API |
| Date | 2026-08-31 |
| Author | ComfyUI |
| Download size | 102.4 MB |
| Min ComfyUI version | 0.34.0 |
| Usage | 9 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #11 | audio | fish_audio_example.mp3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveText` | 2 |  |
| `FishAudioSpeechToText` | 1 |  |
| `LoadAudio` | 1 |  |
| `MarkdownNote` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [fish_audio_example.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/fish_audio_example.mp3)

## Guide

- `segments_json` is always output, but it is empty unless `precise_timestamps` is enabled. Turn it on to get per-segment text with start/end times for subtitles.
- `language` is optional. The model auto-detects the language regardless of what you type; a two-letter code (e.g. `en`, `zh`) only acts as a hint for mixed-language audio.

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
