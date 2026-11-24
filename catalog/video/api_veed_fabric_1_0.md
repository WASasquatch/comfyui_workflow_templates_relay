# VEED Fabric 1.0: Talking Photo

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_veed_fabric_1_0)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_fabric_1_0-1.webp" width="360" alt="VEED Fabric 1.0: Talking Photo api_veed_fabric_1_0-1.webp">

> Turn a still photo and a speech track into a talking, lip-synced video with VEED Fabric 1.0. The face in the image speaks the audio, the clip keeps the image's aspect ratio and runs as long as the audio, up to 300 seconds at 480p or 720p. Ideal for avatars, mascots and localized spokesperson clips driven by your own voice recording or a TTS node.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_veed_fabric_1_0.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_veed_fabric_1_0.json)

## Details

| | |
|---|---|
| Name | `api_veed_fabric_1_0` |
| Category | Foundation › Video |
| Output | video |
| Models | VEED |
| Tags | API, Image to Video, Lip Sync |
| Type | API |
| Date | 2026-10-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.43.0 |
| Usage | 15 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | black_fashion_portrait.png |
| input | `LoadAudio` #5 | audio | audio_see_beyond_the_light.mp3 |
| output | `SaveVideo` #3 | video | api_veed_fabric_1_0.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadAudio` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |
| `VeedFabricNode` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Workflow Guide</summary>

## VEED Fabric 1.0: Talking Photo — Workflow Guide

## Input Assets
- [black_fashion_portrait.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/black_fashion_portrait.png)
- [audio_see_beyond_the_light.mp3](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/audio_see_beyond_the_light.mp3)

## How to Use
1. Load a photo with one clear, front-facing face.
2. Load the speech: it sets lip movement and clip length.
3. Pick 720p (default) or 480p.

## Limits
- Audio up to 300 seconds; output length equals the audio.
- 480p is 864x480 at 16:9; 720p is 1312x736.
- One speaker per run; the clearest front-facing face speaks.

</details>
