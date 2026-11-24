# Apply Glitch And Distortion Effects

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_purz_image_glitch-1.webp" width="360" alt="Apply Glitch And Distortion Effects templates_purz_image_glitch-1.webp">

> Adds customizable glitch and tearing effects to images. Control distortion intensity, chromatic aberration, and pattern randomness. Outputs a stylistically distorted image.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_purz_image_glitch.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_purz_image_glitch.json)

## Details

| | |
|---|---|
| Name | `templates_purz_image_glitch` |
| Category | Foundation › Image |
| Media type | image |
| Models | None |
| Tags | Image, Image Edit |
| Type | open source |
| Date | 2026-03-19 |
| Author | PurzBeats |
| Min ComfyUI version | 0.0.1 |
| Usage | 2 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | comfy_cat.png |
| output | `SaveImage` #3 | image | templates_purz_image_glitch.png |

## Custom nodes required

- [comfyui_fill-nodes](https://registry.comfy.org/nodes/comfyui_fill-nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `FL_Glitch` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# FL Glitch

Applies glitch/distortion effects to images.

## Parameters

| Parameter | Default | Notes |
|---|---|---|
| `envelope_json` | — | Leave blank. |
| `blend_intensity` | 1.00 | Mask blend strength. Only active when a mask is connected. |
| `invert` | Off | Inverts the mask area. |
| `glitch_amount` | 4.00 | Main distortion intensity. Higher = more tearing. |
| `color_offset` | Disable | Adds chromatic aberration. |
| `seed` | 61 | Controls glitch pattern randomness. |

</details>
