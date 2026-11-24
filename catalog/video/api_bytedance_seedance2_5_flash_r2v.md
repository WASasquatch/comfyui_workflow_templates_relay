# Seedance 2.5 Flash: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedance2_5_flash_r2v-1.webp" width="360" alt="Seedance 2.5 Flash: Reference to Video api_bytedance_seedance2_5_flash_r2v-1.webp">

> Generate a reference-driven fight scene with Seedance 2.5 Flash: load two character images plus the location, describe the blocking and cuts in the prompt, and it returns a multi-shot clip at 480p or 720p, up to 30 seconds, with synchronized sound. The references hold faces, costumes and set across every shot.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedance2_5_flash_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bytedance_seedance2_5_flash_r2v.json)

## Details

| | |
|---|---|
| Name | `api_bytedance_seedance2_5_flash_r2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | Seedance 2.5 |
| Tags | API, Reference to Video |
| Type | API |
| Date | 2026-11-15 |
| Author | ComfyUI |
| Min ComfyUI version | 0.45.4 |
| Usage | 15 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | api_bytedance_seedance2_5_flash_r2v_input_image_1.jpeg |
| input | `LoadImage` #5 | image | api_bytedance_seedance2_5_flash_r2v_input_image_2.jpeg |
| input | `LoadImage` #6 | image | api_bytedance_seedance2_5_flash_r2v_input_image_3.jpeg |
| output | `SaveVideo` #3 | video | api_bytedance_seedance2_5_flash_r2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 3 |  |
| `ByteDance2ReferenceNodeV2` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [api_bytedance_seedance2_5_flash_r2v_input_image_1.jpeg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_bytedance_seedance2_5_flash_r2v_input_image_1.jpeg) — bandaged monk in a fight stance (the ash prophet)
- [api_bytedance_seedance2_5_flash_r2v_input_image_2.jpeg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_bytedance_seedance2_5_flash_r2v_input_image_2.jpeg) — fur-and-brass armoured brawler, bandaged head and arms (the half-giant porter)
- [api_bytedance_seedance2_5_flash_r2v_input_image_3.jpeg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_bytedance_seedance2_5_flash_r2v_input_image_3.jpeg) — empty temple colonnade with a broken-roof light shaft (the location)

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
