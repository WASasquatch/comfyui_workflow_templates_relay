# VEED Clean Audio: Video Speech Cleanup

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_clean_audio_video-1.webp" width="360" alt="VEED Clean Audio: Video Speech Cleanup api_veed_clean_audio_video-1.webp">

> Clean the speech inside a video with VEED Clean Audio: background noise, music and effects are stripped from the soundtrack, pauses are cleaned completely, and the clip comes back with 48 kHz mono speech, optionally normalized to a target loudness while the picture stays as shot. Video up to 1799 seconds.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_clean_audio_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_veed_clean_audio_video.json)

## Details

| | |
|---|---|
| Name | `api_veed_clean_audio_video` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | VEED |
| Tags | API, Audio, Video Edit |
| Type | API |
| Date | 2026-10-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.43.0 |
| Usage | 0 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #2 | video | veed_clean_audio_input_h3_omniref_person_dialogue_plus_noise.mp4 |
| output | `SaveVideo` #3 | video | api_veed_clean_audio_video.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadVideo` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |
| `VeedCleanVideoAudioNode` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Workflow Guide</summary>

## VEED Clean Audio (in Video): Speech Cleanup — Workflow Guide

## Input Asset
- [veed_clean_audio_input_h3_omniref_person_dialogue_plus_noise.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/veed_clean_audio_input_h3_omniref_person_dialogue_plus_noise.mp4)

## How to Use
1. Load a clip with an audio track.
2. Keep strength at 0.874: how much noise is removed.
3. Choose normalize (target -19 LUFS) or keep input level.

## Limits
- Up to 1799 seconds (just under 30 minutes) per run.
- Audio returns 48 kHz mono; stereo is folded down.
- A clip with no audio track stops with an error.
- Peaks are capped at -1.1 dBTP, so loud targets settle near -15 LUFS.

</details>
