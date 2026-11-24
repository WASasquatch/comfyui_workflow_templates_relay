# PixVerse V6 Max: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pixverse_v6_max_i2v-1.webp" width="360" alt="PixVerse V6 Max: Image to Video api_pixverse_v6_max_i2v-1.webp">

> Animate a still image with PixVerse V6 Max, keeping the aspect ratio of the input image and generating up to 15 seconds at up to 1080p with an optional native audio track. Ideal for bringing product shots, character art and keyframes to life for social and advertising use.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pixverse_v6_max_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_pixverse_v6_max_i2v.json)

## Details

| | |
|---|---|
| Name | `api_pixverse_v6_max_i2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | PixVerse |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-10-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.42.5 |
| Usage | 25 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | pixverse_v6max_i2v_input_image.png |
| output | `SaveVideo` #4 | video | api_pixverse_v6_max_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PixverseV6ImageToVideoNode` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [pixverse_v6max_i2v_input_image.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/pixverse_v6max_i2v_input_image.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
