# Kling O3: FLF2V

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_o3_flf2v-1.webp" width="360" alt="Kling O3: FLF2V api_kling_o3_flf2v-1.webp">

> Upload reference images or specify start and end frames. Generate a video with precise semantic control, longer duration, and improved narrative coherence.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_o3_flf2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_o3_flf2v.json)

## Details

| | |
|---|---|
| Name | `api_kling_o3_flf2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | Kling O3 |
| Tags | API, FLF2V |
| Type | API |
| Date | 2026-02-10 |
| Author | ComfyUI |
| Min ComfyUI version | 0.13.0 |
| Usage | 10 |
| Nodes | 8 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #17 | image | ivory_rider_right_front_view.png |
| input | `LoadImage` #34 | image | ivory_rider.png |
| input | `LoadImage` #35 | image | ivory_rider_left_side_view.png |
| input | `LoadImage` #36 | image | ivory_rider_right_side_view.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 4 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `KlingOmniProFirstLastFrameNode` | 1 | comfy-core |
| `Note` | 1 |  |
| `SaveVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
Reference images can be used for the context of the video, but cannot be used simultaneously with end_frame.
```

</details>
