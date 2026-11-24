# Sync 3: Video Lip-Sync

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_sync_so_lip_sync_video-1.webp" width="360" alt="Sync 3: Video Lip-Sync api_sync_so_lip_sync_video-1.webp">

> Synchronize a video's lip movements with a new audio track using the Sync Labs sync-3 model, which automatically adjusts the speaker’s mouth to match your uploaded audio. This workflow takes 1 video and 1 audio input to produce 1 synced video output. Ideal for dubbing foreign-language content, correcting mismatched dialogue in video production, or animating a static portrait to speak.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_sync_so_lip_sync_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_sync_so_lip_sync_video.json)

## Details

| | |
|---|---|
| Name | `api_sync_so_lip_sync_video` |
| Category | Foundation › Video |
| Media type | image |
| Models | Sync 3 |
| Tags | API, Lip Sync |
| Type | API |
| Date | 2026-07-15 |
| Author | ComfyUI |
| Min ComfyUI version | 0.28.0 |
| Usage | 53 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #9 | video | girl_looking_at_photo.mp4 |
| input | `LoadAudio` #11 | audio | sync3_reference_audio.mp3 |
| output | `SaveVideo` #13 | video | api_sync_so_lip_sync_video.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadAudio` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `RecordAudio` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `SyncLipSyncNode` | 1 | comfy-core |
