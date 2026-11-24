# Video Upscale: SeedVR2

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_seedvr2_video_upscale-1.webp" width="360" alt="Video Upscale: SeedVR2 utility_seedvr2_video_upscale-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_seedvr2_video_upscale-2.webp" width="360" alt="Video Upscale: SeedVR2 utility_seedvr2_video_upscale-2.webp">

> Upload a video to upscale and enhance its resolution using the SeedVR2 model for high-definition output.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_seedvr2_video_upscale.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_seedvr2_video_upscale.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/video-upscale)

## Details

| | |
|---|---|
| Name | `utility_seedvr2_video_upscale` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | SeedVR2 |
| Tags | Video Upscale |
| Type | open source |
| Date | 2026-02-06 |
| Author | ComfyUI |
| Min ComfyUI version | 0.28.0 |
| Usage | 223 |
| Nodes | 11 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #18 | video | input_3d.mp4 |

## Custom nodes required

- [seedvr2_videoupscaler](https://registry.comfy.org/nodes/seedvr2_videoupscaler)

## Subgraphs

- **SeedVR2 Upscaler** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `CreateVideo` | 1 |  |
| `GetVideoComponents` | 1 |  |
| `ImageFromBatch` | 1 |  |
| `ImageScale` | 1 |  |
| `LoadVideo` | 1 |  |
| `SaveVideo` | 1 |  |
| `SeedVR2LoadDiTModel` | 1 |  |
| `SeedVR2LoadVAEModel` | 1 |  |
| `SeedVR2VideoUpscaler` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# About SeedVR2 Video Upscale

## How Resolution Works

The **Resolution** setting in the `SeedVR2_VideoUpscaler` node is based on the **height** of your output video. Think of it the same way you'd refer to standard video resolutions:

| Resolution Setting | Output Example (16:9) |
|----|-----|
| 1080 | 1920×1080 (1080p) |
| 1440 | 2560×1440 (1440p) |
| 2160 | 3840×2160 (4K) |

So if your source is 1280×720 and you set Resolution to `1080`, the output will be **1920×1080**.

## Preparing Your Input

Use the **Image Scale** node before the upscaler to downscale your input to the correct starting size. The upscaler node will **center-crop** the input to ensure the final output lands on the correct aspect ratio, so getting your input dimensions right beforehand avoids unexpected cropping.

## Performance Note

Higher target resolutions require significantly more processing time. If you're experimenting or iterating, start at a lower resolution to dial in your settings before committing to a full 2160p render.

</details>

<details><summary>Video length</summary>

`ImageFromBatch` clips video frames. Select the node and press **Ctrl-B** to disable it for full video.

</details>
