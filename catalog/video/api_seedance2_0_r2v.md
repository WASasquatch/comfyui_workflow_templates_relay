# Seedance 2.0: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_seedance2_0_r2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_r2v-1.webp" width="360" alt="Seedance 2.0: Reference to Video api_seedance2_0_r2v-1.webp">

> Generate cinematic videos from reference images and text prompts. Preserve subject identity and composition while adding expressive motion with synchronized audio. Control camera movement and lighting through detailed prompts.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_0_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_0_r2v.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_0_r2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Seedance 2.0 |
| Tags | API, Image to Video, Video |
| Type | API |
| Date | 2026-05-25 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.2 |
| Usage | 396 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #356 | image | selfie_cartoon_style.png |
| output | `SaveVideo` #344 | video | Seedance2.0_r2v_00006_.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDance2ReferenceNodeV2` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Input Asset</summary>

## Input Asset

- [selfie_cartoon_style.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/selfie_cartoon_style.png)

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
