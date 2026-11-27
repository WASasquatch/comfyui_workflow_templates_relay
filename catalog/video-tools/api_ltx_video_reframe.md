# Reframe: LTX VFX

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_ltx_video_reframe)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ltx_video_reframe-1.webp" width="360" alt="Reframe: LTX VFX api_ltx_video_reframe-1.webp">

> Reframe a finished clip to a different aspect ratio with LTX VFX through the partner API. Pick a target preset such as 720p 16:9 and the crop anchor, and the model rebuilds the framing inside the new canvas instead of simply cutting the edges, so the action stays in shot. Ideal for turning a vertical clip into a widescreen cut or reshaping footage for another platform.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ltx_video_reframe.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_ltx_video_reframe.json)

## Details

| | |
|---|---|
| Name | `api_ltx_video_reframe` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | LTX-2.5 |
| Tags | API, Outpainting, Video |
| Type | API |
| Date | 2026-11-10 |
| Author | ComfyUI |
| Min ComfyUI version | 0.45.1 |
| Usage | 56 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #3 | video | man_black_horse_surreal.mp4 |
| output | `SaveVideo` #4 | video | api_ltx_video_reframe.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadVideo` | 1 |  |
| `LtxApiVideoReframe` | 1 |  |
| `Note` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
## Input Asset

- [man_black_horse_surreal.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/man_black_horse_surreal.mp4)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)
```

</details>
