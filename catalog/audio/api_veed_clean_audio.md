# VEED Clean Audio: Speech Cleanup

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_veed_clean_audio)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_clean_audio-1.webp" width="360" alt="VEED Clean Audio: Speech Cleanup api_veed_clean_audio-1.webp">

> Remove background noise from a speech recording with VEED Clean Audio: music and effects go with the noise, pauses are cleaned completely, and the voice comes back as 48 kHz mono audio, optionally normalized to a target loudness. Audio up to 1799 seconds.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_clean_audio.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_veed_clean_audio.json)

## Details

| | |
|---|---|
| Name | `api_veed_clean_audio` |
| Category | Foundation › Audio |
| Output | audio |
| Models | VEED |
| Tags | API, Audio, Audio Editing |
| Type | API |
| Date | 2026-10-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.43.0 |
| Usage | 21 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #13 | audio | veed_clean_audio_noisy_input.wav |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadAudio` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveAudioAdvanced` | 1 |  |
| `VeedCleanAudioNode` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Workflow Guide</summary>

## VEED Clean Audio: Speech Cleanup — Workflow Guide

## Input Asset
- [veed_clean_audio_noisy_input.wav](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/veed_clean_audio_noisy_input.wav)

## How to Use
1. Load the speech recording in Load Audio.
2. Keep strength at 0.874, or lower it to keep more room tone under the voice.
3. Pick normalize (target -19 LUFS) or keep input level.

## Limits
- Up to 1799 seconds per run.
- Returns 48 kHz mono; music and effects are removed with the noise.
- Pauses are cleaned fully; peaks cap at -1.1 dBTP, so loud targets settle near -15 LUFS.

</details>
