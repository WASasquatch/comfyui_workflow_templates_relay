# PixVerse 6.0: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pixverse6_r2v-1.webp" width="360" alt="PixVerse 6.0: Reference to Video api_pixverse6_r2v-1.webp">

> Create reference-driven videos with PixVerse V6, generating clips that follow the style, motion, and subject traits of your uploaded reference footage. Ideal for matching a specific visual identity across variations, extending a character or scene’s look to new actions, and producing consistent branded content from a single source clip.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pixverse6_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_pixverse6_r2v.json)

## Details

| | |
|---|---|
| Name | `api_pixverse6_r2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | PixVerse |
| Tags | API, Reference to Video |
| Type | API |
| Date | 2026-08-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.0 |
| Usage | 10 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #7 | image | street_rider.png |
| input | `LoadImage` #8 | image | futuristic_urban_editorial.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `MarkdownNote` | 1 |  |
| `PixverseV6FusionVideoNode` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [street_rider.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/street_rider.png)
- [futuristic_urban_editorial.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/futuristic_urban_editorial.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
