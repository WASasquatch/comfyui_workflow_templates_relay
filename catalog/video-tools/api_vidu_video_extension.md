# Video Extend: Vidu Q2

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_vidu_video_extension)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_video_extension-1.webp" width="360" alt="Video Extend: Vidu Q2 api_vidu_video_extension-1.webp">

> Upload a video and use the Vidu Q2 model to extend it up to 7 seconds and enhance the resolution to 1080p.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_video_extension.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_vidu_video_extension.json)

## Details

| | |
|---|---|
| Name | `api_vidu_video_extension` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | Vidu Q2, Vidu |
| Tags | Video, Video Extend, API |
| Type | API |
| Date | 2026-02-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.12.0 |
| Usage | 13 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #2 | video | lawyer.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GetImageSize` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `ImageFromBatch` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `Note` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
| `ViduExtendVideoNode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
The extended video will not retain the original audio.
```

</details>
