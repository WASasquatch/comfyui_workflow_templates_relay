# Kling2.6: Motion Control

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_kling_motion_control)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_motion_control-1.webp" width="360" alt="Kling2.6: Motion Control api_kling_motion_control-1.webp">

> Apply precise character actions and expressions from a reference video to your character image with synchronized motion control.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_motion_control.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_motion_control.json)

## Details

| | |
|---|---|
| Name | `api_kling_motion_control` |
| Category | Foundation › Video |
| Output | video |
| Models | Kling 2.6, Kling |
| Tags | Video, Motion Control, API |
| Type | API |
| Date | 2026-01-12 |
| Author | ComfyUI |
| Min ComfyUI version | 0.16.1 |
| Usage | 45 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #2 | video | street_dancer.mp4 |
| input | `LoadImage` #11 | image | streetwear_fox.jpg |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `KlingMotionControl` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

If possible, keep the image and video at a similar ratio.

</details>
