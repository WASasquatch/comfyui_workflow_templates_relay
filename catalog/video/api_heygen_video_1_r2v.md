# HeyGen Video 1.0: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_video_1_r2v-1.webp" width="360" alt="HeyGen Video 1.0: Reference to Video api_heygen_video_1_r2v-1.webp">

> Generate a 5-15 second video with dialogue and sound from a prompt plus up to nine images, three videos and three audio clips using HeyGen Video 1.0, addressed in the prompt as @Image1, @Video1 and @Audio1. One video is output, with the people, products and places you supply driving the shot. Ideal for product demos, UGC-style clips that keep one presenter or product consistent, and placing your product into a scene of your own.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_heygen_video_1_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_heygen_video_1_r2v.json)

## Details

| | |
|---|---|
| Name | `api_heygen_video_1_r2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | HeyGen |
| Tags | API, Reference to Video |
| Type | API |
| Date | 2026-09-30 |
| Author | ComfyUI |
| Min ComfyUI version | 0.38.1 |
| Usage | 158 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #5 | image | model_black_blazer_red_earrings.png |
| input | `LoadImage` #6 | image | cognac_leather_handbag.png |
| output | `SaveVideo` #3 | video | api_heygen_video_1_r2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `HeyGenReferenceToVideoNode` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [model_black_blazer_red_earrings.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/model_black_blazer_red_earrings.png)
- [cognac_leather_handbag.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/cognac_leather_handbag.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
