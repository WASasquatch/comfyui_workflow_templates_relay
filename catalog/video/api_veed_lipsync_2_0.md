# VEED Lipsync 2.0: Lip Sync

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_lipsync_2_0-1.webp" width="360" alt="VEED Lipsync 2.0: Lip Sync api_veed_lipsync_2_0-1.webp">

> Re-sync a speaker's mouth in footage you already shot to a new speech track with VEED Lipsync 2.0. The person on camera speaks the new audio while the rest of the shot stays as recorded; the output keeps the video's resolution at 25 fps and runs as long as the audio, up to 600 seconds. If the clip is shorter than the speech it plays forward and backward until the audio ends. Ideal for dubbing a line, swapping a script without re-shooting, or making localized versions of existing footage.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_lipsync_2_0.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_veed_lipsync_2_0.json)

## Details

| | |
|---|---|
| Name | `api_veed_lipsync_2_0` |
| Category | Foundation › Video |
| Media type | image |
| Models | VEED |
| Tags | API, Lip Sync, Video Edit |
| Type | API |
| Date | 2026-10-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.43.0 |
| Usage | 107 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #8 | video | rainbow_face_portrait_prism_video.mp4 |
| input | `LoadAudio` #9 | audio | veed_lipsync_rainbow_night_speech.wav |
| output | `SaveVideo` #10 | video | api_veed_lipsync_2_0.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadAudio` | 1 |  |
| `LoadVideo` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |
| `VeedLipsyncNode` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Workflow Guide</summary>

## VEED Lipsync 2.0: Video Lip Sync — Workflow Guide

## Input Assets
- [rainbow_face_portrait_prism_video.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/rainbow_face_portrait_prism_video.mp4)
- [veed_lipsync_rainbow_night_speech.wav](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/veed_lipsync_rainbow_night_speech.wav)

## How to Use
1. Load footage of one front-facing speaker.
2. Load the new speech; it sets the clip length.
3. Run; Save Video writes the result.

## Limits
- Audio up to 600 seconds; output length matches it.
- Output keeps the source resolution at 25 fps.
- Shorter video than audio plays forward then backward until it ends.

</details>
