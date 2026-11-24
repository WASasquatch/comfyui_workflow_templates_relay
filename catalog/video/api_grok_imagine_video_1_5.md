# Grok Imagine Video 1.5: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_grok_imagine_video_1_5)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_video_1_5-1.webp" width="360" alt="Grok Imagine Video 1.5: Image to Video api_grok_imagine_video_1_5-1.webp">

> Upload an image and optional text prompt to generate a video with native audio, realistic motion, and high-quality output up to 720p resolution.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_video_1_5.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_grok_imagine_video_1_5.json)

## Details

| | |
|---|---|
| Name | `api_grok_imagine_video_1_5` |
| Category | Foundation › Video |
| Output | video |
| Models | Grok |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-06-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.30.0 |
| Usage | 138 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #6 | image | robot_nun_pray.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GrokVideoNode` | 1 |  |
| `LoadImage` | 1 |  |
| `SaveVideo` | 1 |  |
