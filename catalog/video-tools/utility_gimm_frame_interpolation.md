# Frame Interpolation: GIMM-VFI

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_gimm_frame_interpolation)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_gimm_frame_interpolation-1.webp" width="360" alt="Frame Interpolation: GIMM-VFI utility_gimm_frame_interpolation-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_gimm_frame_interpolation-2.webp" width="360" alt="Frame Interpolation: GIMM-VFI utility_gimm_frame_interpolation-2.webp">

> Generate intermediate frames between existing video frames to create smoother motion. Input a video and receive a fluid, higher-frame-rate output without changing the total duration.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_gimm_frame_interpolation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_gimm_frame_interpolation.json)

## Details

| | |
|---|---|
| Name | `utility_gimm_frame_interpolation` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | None |
| Tags | Frame Interpolation, Video |
| Type | open source |
| Date | 2026-03-30 |
| Author | PurzBeats |
| Download size | 10.0 GB |
| Min ComfyUI version | 0.16.4 |
| Usage | 14 |
| Nodes | 8 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `VHS_LoadVideo` #8 | video | gimm-input.mp4 |

## Custom nodes required

- [comfyui-gimm-vfi](https://registry.comfy.org/nodes/comfyui-gimm-vfi)
- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)

## Subgraphs

- **GIMM Frame Interpolation** (5 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfyMathExpression` | 1 |  |
| `DownloadAndLoadGIMMVFIModel` | 1 |  |
| `GIMMVFI_interpolate` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PrimitiveInt` | 1 |  |
| `VHS_LoadVideo` | 1 |  |
| `VHS_VideoCombine` | 1 |  |
| `VHS_VideoInfo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# GIMM Frame Interpolation

Inserts synthetic frames between existing frames to increase frame density without changing video duration. Output FPS is multiplied so playback time stays identical.

```
output_fps = input_fps × interpolation_factor
// e.g. 30 fps × 3 = 90 fps, same length
```

---

## GIMM Interpolation Node

| Setting | Notes |
|---|---|
| `interpolation_factor` | Multiplier — `3` inserts 2 new frames per gap |
| `output_frame_rate` | feeds directly into Video Combine's | 
| `frame_rate`  | **don't hardcode it** or duration breaks.  |
---
## Tips

- Higher factors = smoother but slower and more prone to artifacts on fast motion
- Test on a short clip before running a full video


---
 
> **In plain English:** Videos are made of still images played rapidly one after another. This workflow uses AI to generate *extra* images and slip them in between the originals — making motion look silkier and more fluid. Your video stays the exact same length, it just has more "steps" between each moment.

</details>
