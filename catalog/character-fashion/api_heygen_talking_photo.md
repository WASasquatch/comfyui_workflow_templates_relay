# HeyGen: Talking Photo

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_heygen_talking_photo)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_talking_photo-1.webp" width="360" alt="HeyGen: Talking Photo api_heygen_talking_photo-1.webp">

> Generate a talking-head video from a single photograph using HeyGen's Avatar IV engine, which produces a fully animated video with lip-synced speech, facial expressions, head movements, and automatic gestures. Ideal for creating digital avatars for presentations, virtual characters for interactive content, and personalized video messages from a single image.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_talking_photo.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_heygen_talking_photo.json)

## Details

| | |
|---|---|
| Name | `api_heygen_talking_photo` |
| Category | Applied › Character & Fashion |
| Output | video |
| Models | HeyGen |
| Tags | API, Image to Video, Lip Sync |
| Type | API |
| Date | 2026-07-21 |
| Author | ComfyUI |
| Min ComfyUI version | 0.28.1 |
| Usage | 30 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #14 | image | yellow_lens_girl.png |
| output | `SaveVideo` #15 | video | api_heygen_talking_photo.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `HeyGenTalkingPhotoNode` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
