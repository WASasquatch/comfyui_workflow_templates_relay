# Higgsfield Genjutsu: Motion Transfer

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_higgsfield_genjutsu_motion_transfer)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_higgsfield_genjutsu_motion_transfer-1.webp" width="360" alt="Higgsfield Genjutsu: Motion Transfer api_higgsfield_genjutsu_motion_transfer-1.webp">

> Recast an existing video with Higgsfield Genjutsu: the source clip keeps its motion, camera movement, timing and audio, while the cast, location and style are rebuilt from 1 to 8 reference images. Describe which reference replaces what in the optional prompt. Output length follows the source clip. Ideal for restyling footage, swapping the cast of a shot, and building scenes a shoot never covered.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_higgsfield_genjutsu_motion_transfer.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_higgsfield_genjutsu_motion_transfer.json)

## Details

| | |
|---|---|
| Name | `api_higgsfield_genjutsu_motion_transfer` |
| Category | Foundation › Video |
| Output | video |
| Models | Genjutsu 1.0 |
| Tags | Character Replacement, Motion Control, Video, Video Edit |
| Type | API |
| Date | 2026-10-12 |
| Author | ComfyUI |
| Min ComfyUI version | 0.40.0 |
| Usage | 235 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #13 | video | rooftop_dancer.mp4 |
| input | `LoadImage` #14 | image | snow_queen_ref.png |
| input | `LoadImage` #15 | image | ice_palace_ref.png |
| output | `SaveVideo` #10 | video | api_higgsfield_genjutsu_motion_transfer.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `HiggsfieldMotionTransferNode` | 1 |  |
| `LoadVideo` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>Higgsfield Genjutsu Motion Transfer</summary>

## Higgsfield Genjutsu Motion Transfer

Recast a video: the source clip keeps its motion, camera movement, timing and audio, while the cast, location and style are rebuilt from 1 to 8 reference images.

This example turns a rooftop dancer into a snow queen, first with a character reference, then with an optional scene reference.

## Input Assets

- [rooftop_dancer.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/rooftop_dancer.mp4)
- [snow_queen_ref.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/snow_queen_ref.png)
- [ice_palace_ref.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/ice_palace_ref.png)

**Inputs:**

- `video`: source motion clip. At least 4 seconds, only the first 30 seconds are used.
- `reference_images`: 1 to 8 images of the characters, locations or styles to use. Click **+** on the input to add more references.
- `prompt`: optional. Describe which reference replaces what, for example which person it should replace.
- `resolution`: 480p, 720p (default) or 1080p.

**Notes:**

- Output length follows the source clip, and the model is billed per output second.
- One partner job runs at a time.
- The seed only controls whether the node re-runs: results are non-deterministic either way.

</details>
