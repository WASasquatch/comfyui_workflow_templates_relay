# HeyGen: Avatar Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_heygen_avatar_video)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_avatar_video-1.webp" width="360" alt="HeyGen: Avatar Video api_heygen_avatar_video-1.webp">

> Create an AI avatar video from a text prompt or uploaded image using HeyGen's avatar generation technology, outputting a single talking-head video. You can save the avatar ID for reuse in future videos. Ideal for personalized digital presenters, social media content creation, and multilingual video production without recording talent.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_avatar_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_heygen_avatar_video.json)

## Details

| | |
|---|---|
| Name | `api_heygen_avatar_video` |
| Category | Foundation › Video |
| Output | video |
| Models | HeyGen |
| Tags | API, Lip Sync, Video |
| Type | API |
| Date | 2026-07-21 |
| Author | ComfyUI |
| Min ComfyUI version | 0.28.1 |
| Usage | 11 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #21 | video | api_heygen_avatar_video.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewAny` | 2 | comfy-core |
| `ColorToRGBInt` | 1 | comfy-core |
| `HeyGenAvatarVideoNode` | 1 | comfy-core |
| `HeyGenCreateAvatarNode` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveText` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `StringConcatenate` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Create Avatar</summary>

You can use prompt or input image to create your own avatar, please save the avatar ID for reuse

</details>
