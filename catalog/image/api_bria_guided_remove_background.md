# Bria: Guided Background Removal

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bria_guided_remove_background)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_guided_remove_background-1.webp" width="360" alt="Bria: Guided Background Removal api_bria_guided_remove_background-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_guided_remove_background-2.webp" width="360" alt="Bria: Guided Background Removal api_bria_guided_remove_background-2.webp">

> Remove the background from an image with Bria while keeping whatever a text prompt describes, so one subject can be cut out of a busy scene instead of losing everything that is not background. The original pixels come back at full resolution with a new alpha channel. Ideal for product cutouts, portrait isolation and compositing prep.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_guided_remove_background.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bria_guided_remove_background.json)

## Details

| | |
|---|---|
| Name | `api_bria_guided_remove_background` |
| Category | Foundation › Image |
| Output | image |
| Models | BRIA |
| Tags | API, Image, Remove Background |
| Type | API |
| Date | 2026-10-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.42.5 |
| Usage | 14 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #3 | image | bria_guided_person.png |
| output | `SaveImage` #4 | image | api_bria_guided_remove_background.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BriaGuidedRemoveBackground` | 1 |  |
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# Bria: Guided Background Removal

Describe what to keep and Bria removes everything else, so a cutout can keep one subject out of a busy scene instead of losing whatever is not background. The original pixels come back at full resolution with a new alpha channel.

## Input Asset

- [bria_guided_person.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/bria_guided_person.png)

## Parameters

- The prompt names what stays: `the man in the blue shirt`, `only the shoes`. A prompt that matches nothing returns a fully transparent image.
- Naming what to drop as well as what to keep is the most reliable way to get a clean edge around hair and thin clothing.
- `moderation` on exposes separate visual input and output moderation toggles; off skips them.
- For a plain cutout with no guidance, Bria Remove Image Background is the simpler node.

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
