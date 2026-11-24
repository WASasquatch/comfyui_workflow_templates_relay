# Seedance 2.5 Flash: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bytedance_seedance2_5_flash_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedance2_5_flash_i2v-1.webp" width="360" alt="Seedance 2.5 Flash: Image to Video api_bytedance_seedance2_5_flash_i2v-1.webp">

> Animate a still image with Seedance 2.5 Flash, the faster tier of Seedance 2.5: load a start image, describe the action in the prompt and it returns a multi-shot clip at 480p or 720p, up to 30 seconds, with synchronized sound. Ideal for turning stills, key art and product shots into motion.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedance2_5_flash_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bytedance_seedance2_5_flash_i2v.json)

## Details

| | |
|---|---|
| Name | `api_bytedance_seedance2_5_flash_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Seedance 2.5 |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-11-15 |
| Author | ComfyUI |
| Min ComfyUI version | 0.45.4 |
| Usage | 54 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | api_bytedance_seedance2_5_flash_i2v_input.png |
| output | `SaveVideo` #3 | video | api_bytedance_seedance2_5_flash_i2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDance2ReferenceNodeV2` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [api_bytedance_seedance2_5_flash_i2v_input.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_bytedance_seedance2_5_flash_i2v_input.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
