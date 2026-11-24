# HeyGen Voice 1.0 Turbo: Voice Clone to Speech

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_heygen_voice_1_turbo)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_voice_1_turbo-1.webp" width="360" alt="HeyGen Voice 1.0 Turbo: Voice Clone to Speech api_heygen_voice_1_turbo-1.webp">

> Clone a voice from a short recording with HeyGen Voice 1.0 Turbo, then speak any script in that voice. It is the same instant clone as Voice 1.0, run through the turbo model, which renders faster for quick drafts and iteration. Connect one audio clip to Instant Clone and the resulting voice_id feeds straight into text to speech, while SaveText keeps the ID on disk for the next session. Ideal for narration in your own voice, character dialogue, and multilingual voiceover.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_voice_1_turbo.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_heygen_voice_1_turbo.json)

## Details

| | |
|---|---|
| Name | `api_heygen_voice_1_turbo` |
| Category | Foundation › Audio |
| Output | audio |
| Models | HeyGen |
| Tags | API, Text to Speech, Voice Cloning |
| Type | API |
| Date | 2026-10-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.42.3 |
| Usage | 29 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #2 | audio | long_demo.mp3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `HeyGenVoiceCloneNode` | 1 |  |
| `HeyGenVoiceTextToSpeechNode` | 1 |  |
| `LoadAudio` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |
| `SaveText` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## HeyGen Voice 1.0 Turbo: Voice Clone to Speech — Workflow Guide

## Input Asset
- [long_demo.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/long_demo.mp3)

## How to Use
1. Load one speaker, 10 seconds+: Instant Clone returns a `voice_id`, which SaveText writes to `output/`.
2. Text to Speech already uses `heygen-voice-1-turbo`, the faster model: link `voice_id`, write the script in `text`.
3. Queue the prompt; `expressiveness_boost` 0.5 stays near the recording. SaveAudioAdvanced writes the mp3.

## Limits
- First 3 minutes of the recording are used.
- Script: plain prose, 1 to 5000 characters.
- Instant voices ignore seed, speed and pitch.

</details>
