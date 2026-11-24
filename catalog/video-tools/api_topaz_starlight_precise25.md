# Video Upscale: Topaz Starlight Precise 2.5

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_starlight_precise25-1.webp" width="360" alt="Video Upscale: Topaz Starlight Precise 2.5 api_topaz_starlight_precise25-1.webp">

> Upload a video to enhance its resolution using the Topaz Starlight Precise 2.5 model. This workflow produces sharper 4K output with reduced artifacts compared to previous versions.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_starlight_precise25.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_topaz_starlight_precise25.json)

## Details

| | |
|---|---|
| Name | `api_topaz_starlight_precise25` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | Topaz |
| Tags | Video Upscale, API |
| Type | API |
| Date | 2026-03-26 |
| Author | ComfyUI |
| Min ComfyUI version | 0.20.2 |
| Usage | 276 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #3 | video | running_horse.mp4 |
| output | `SaveVideo` #4 | video | running_horse.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadVideo` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `TopazVideoEnhanceV2` | 1 |  |
