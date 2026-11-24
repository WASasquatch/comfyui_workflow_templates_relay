# Video Upscale: Topaz Astra 2 Creative

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_topaz_astra2)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_astra2-1.webp" width="360" alt="Video Upscale: Topaz Astra 2 Creative api_topaz_astra2-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_astra2-2.webp" width="360" alt="Video Upscale: Topaz Astra 2 Creative api_topaz_astra2-2.webp">

> Upscale GenAI video footage with Astra 2's creative diffusion, adding dynamic detail and texture. Adjust creativity, sharpness, and prompt-based guidance for precise stylization of AI-generated content.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_topaz_astra2.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_topaz_astra2.json)

## Details

| | |
|---|---|
| Name | `api_topaz_astra2` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | Topaz |
| Tags | API, Video Upscale |
| Type | API |
| Date | 2026-05-03 |
| Author | ComfyUI |
| Min ComfyUI version | 0.20.2 |
| Usage | 88 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #1 | video | cyber_fight.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadVideo` | 1 |  |
| `SaveVideo` | 1 |  |
| `TopazVideoEnhanceV2` | 1 |  |
