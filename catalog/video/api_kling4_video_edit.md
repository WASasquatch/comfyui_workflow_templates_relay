# Kling 4.0: Video Edit

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_kling4_video_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_video_edit-1.webp" width="360" alt="Kling 4.0: Video Edit api_kling4_video_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_video_edit-2.webp" width="360" alt="Kling 4.0: Video Edit api_kling4_video_edit-2.webp">

> Edit an existing clip in one pass with Kling 4.0: name the change and list what must survive, and the model rewrites only that part while keeping the subject, costume, shot count, camera work and timing intact. Output inherits the input's length and aspect ratio, and stereo audio is regenerated to match the new scene. Ideal for swapping environments, wardrobe or style on footage that is already cut.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling4_video_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling4_video_edit.json)

## Details

| | |
|---|---|
| Name | `api_kling4_video_edit` |
| Category | Foundation › Video |
| Output | video |
| Models | Kling 4.0 |
| Tags | Video Edit, API |
| Type | API |
| Date | 2026-10-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.43.0 |
| Usage | 273 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #1 | video | kling4_gown_input.mp4 |
| output | `SaveVideo` #3 | video | api_kling4_video_edit.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Kling4EditVideoNode` | 1 |  |
| `LoadVideo` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Input Asset & Editing</summary>

**Input Asset**

- [kling4_gown_input.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/kling4_gown_input.mp4) — required workflow input (`input/kling4_gown_input.mp4`, 5 s)

## How to edit

The prompt must open with `Edit @Video1:` and then name the change; everything after that is your keep-list. Listing what must survive — subject, costume, movement, shot count, camera work, light direction — is what stops the model from quietly redesigning the person or re-staging the camera.

The output inherits the input: same length, same aspect ratio (`adaptive`), same three shots. Input clips must be 3–30 s. Extra `reference_images` / `reference_videos` inputs can be connected when the new element has to look like something specific (a garment, a product, a location).

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
