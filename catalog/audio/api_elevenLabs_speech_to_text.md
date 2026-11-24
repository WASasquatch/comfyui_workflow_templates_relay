# ElevenLabs: Speech to text

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_elevenLabs_speech_to_text)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_elevenLabs_speech_to_text-1.webp" width="360" alt="ElevenLabs: Speech to text api_elevenLabs_speech_to_text-1.webp">

> Upload an audio or video file to transcribe its speech into accurate, editable text.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_elevenLabs_speech_to_text.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_elevenLabs_speech_to_text.json)

## Details

| | |
|---|---|
| Name | `api_elevenLabs_speech_to_text` |
| Category | Foundation › Audio |
| Output | audio |
| Models | ElevenLabs |
| Tags | API, Speech to Text |
| Type | API |
| Date | 2026-02-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.15.0 |
| Usage | 8 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #219 | audio | long_demo.mp3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewAny` | 2 | comfy-core |
| `ElevenLabsSpeechToText` | 1 | comfy-core |
| `LoadAudio` | 1 | comfy-core |
| `RecordAudio` | 1 | comfy-core |
