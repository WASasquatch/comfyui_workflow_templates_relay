# Pruna P-Video 2: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_pruna_p_video_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pruna_p_video_i2v-1.webp" width="360" alt="Pruna P-Video 2: Image to Video api_pruna_p_video_i2v-1.webp">

> Turn a single image into video with Pruna P-Video-2. As Pruna's quality-focused video model, its image-to-video mode excels at identity consistency and subtle, natural motion — 720p/1080p, 1-20s duration, plus Draft mode for fast previews. Ideal for image animation, product motion, and poster cinemagraphs.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pruna_p_video_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_pruna_p_video_i2v.json)

## Details

| | |
|---|---|
| Name | `api_pruna_p_video_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | P-Video-2 |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-09-16 |
| Author | ComfyUI |
| Min ComfyUI version | 0.36.0 |
| Usage | 56 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #18 | image | alien_mothership_foggy_megacity.png |
| output | `SaveVideo` #19 | video | api_pruna_p_video_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PrunaImageToVideoNode` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [alien_mothership_foggy_megacity.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/alien_mothership_foggy_megacity.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
