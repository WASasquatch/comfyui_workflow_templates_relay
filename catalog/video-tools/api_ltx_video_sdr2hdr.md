# SDR to HDR: LTX VFX

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_ltx_video_sdr2hdr)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ltx_video_sdr2hdr-1.webp" width="360" alt="SDR to HDR: LTX VFX api_ltx_video_sdr2hdr-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ltx_video_sdr2hdr-2.webp" width="360" alt="SDR to HDR: LTX VFX api_ltx_video_sdr2hdr-2.webp">

> Convert a standard-dynamic-range clip to HDR with LTX VFX through the partner API. Load the finished shot, run it once and the model rebuilds the highlights, shadows and colour volume in an HDR deliverable instead of applying a LUT. Ideal for finishing broadcast and streaming masters, or for matching an SDR shot to an HDR timeline.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ltx_video_sdr2hdr.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_ltx_video_sdr2hdr.json)

## Details

| | |
|---|---|
| Name | `api_ltx_video_sdr2hdr` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | LTX-2.5 |
| Tags | API, Color, Video |
| Type | API |
| Date | 2026-11-10 |
| Author | ComfyUI |
| Min ComfyUI version | 0.45.1 |
| Usage | 28 |
| Nodes | 8 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #3 | video | sky_citadel_ring_collapse.mp4 |
| output | `SaveVideo` #12 | video | api_ltx_video_sdr2hdr.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GetVideoComponents` | 2 |  |
| `ComfySwitchNode` | 1 |  |
| `CreateVideo` | 1 |  |
| `LoadVideo` | 1 |  |
| `LtxApiVideoSdrToHdr` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [sky_citadel_ring_collapse.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/sky_citadel_ring_collapse.mp4)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
