# Vidu Q3 Image-to-Video with Audio

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_q3_image_to_video-1.webp" width="360" alt="Vidu Q3 Image-to-Video with Audio api_vidu_q3_image_to_video-1.webp">

> Upload an image and provide a text prompt to generate a 1-16 second video with synchronized audio and intelligent scene transitions.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_q3_image_to_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_vidu_q3_image_to_video.json)

## Details

| | |
|---|---|
| Name | `api_vidu_q3_image_to_video` |
| Category | Foundation › Video |
| Media type | image |
| Models | Vidu, Vidu Q3 |
| Tags | API, Image to Video, Video |
| Type | API |
| Date | 2026-02-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.12.0 |
| Usage | 7 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #16 | image | two_characters.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `Vidu3ImageToVideoNode` | 1 | comfy-core |
