# Sync 3: Talking Image

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_sync_so_talking_image)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_sync_so_talking_image-1.webp" width="360" alt="Sync 3: Talking Image api_sync_so_talking_image-1.webp">

> Generate a talking-head video from a single face photo and an audio clip, with lips and lower-face motion precisely synchronized to the speech. This process outputs one video from one image and one audio input, keeping hands, products, and background completely unchanged. Ideal for product demos, e-commerce introductions, and marketing videos where a static product-holding photo is paired with a voiceover.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_sync_so_talking_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_sync_so_talking_image.json)

## Details

| | |
|---|---|
| Name | `api_sync_so_talking_image` |
| Category | Foundation › Video |
| Output | video |
| Models | Sync 3 |
| Tags | API, Lip Sync |
| Type | API |
| Date | 2026-07-15 |
| Author | ComfyUI |
| Min ComfyUI version | 0.28.0 |
| Usage | 12 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #11 | audio | gel_cream_ad_voice.mp3 |
| input | `LoadImage` #15 | image | girl_holding_gel_cream.png |
| output | `SaveVideo` #13 | video | api_sync_so_talking_image.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadAudio` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `RecordAudio` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `SyncTalkingImageNode` | 1 | comfy-core |
