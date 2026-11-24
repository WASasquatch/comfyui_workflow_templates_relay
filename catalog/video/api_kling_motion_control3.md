# Kling 3.0: Motion Control

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_motion_control3-1.webp" width="360" alt="Kling 3.0: Motion Control api_kling_motion_control3-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_motion_control3-2.webp" width="360" alt="Kling 3.0: Motion Control api_kling_motion_control3-2.webp">

> Upload a character image and a motion reference video. Generate a new video where your character performs the actions from the reference, with enhanced facial consistency using optional element binding.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_motion_control3.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_motion_control3.json)

## Details

| | |
|---|---|
| Name | `api_kling_motion_control3` |
| Category | Foundation › Video |
| Media type | image |
| Models | Kling 3.0 |
| Tags | API, Motion Control |
| Type | API |
| Date | 2026-03-06 |
| Author | ComfyUI |
| Min ComfyUI version | 0.16.1 |
| Usage | 93 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | future_robot.png |
| input | `LoadVideo` #3 | video | boxing_man.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `KlingMotionControl` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
