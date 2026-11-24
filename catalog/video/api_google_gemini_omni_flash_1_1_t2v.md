# Gemini Omni 1.1 Flash: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_google_gemini_omni_flash_1_1_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_t2v-1.webp" width="360" alt="Gemini Omni 1.1 Flash: Text to Video api_google_gemini_omni_flash_1_1_t2v-1.webp">

> Generate cinematic videos with audio from text prompts or reference images using Gemini Omni 1.1 Flash, supporting aspect ratio, resolution, and keyframe interpolation controls. Ideal for text-to-video storytelling, animating product shots or illustrations, and iterative conversational video editing.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_gemini_omni_flash_1_1_t2v.json)

## Details

| | |
|---|---|
| Name | `api_google_gemini_omni_flash_1_1_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Gemini Omni 1.1 Flash |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-08-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.2 |
| Usage | 46 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #25 | video | api_google_gemini_omni_flash_1_1_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiVideoOmniV2` | 1 |  |
| `SaveVideo` | 1 |  |
