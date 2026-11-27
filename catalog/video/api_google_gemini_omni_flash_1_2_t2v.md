# Gemini Omni 1.2 Flash: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_google_gemini_omni_flash_1_2_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_t2v-1.webp" width="360" alt="Gemini Omni 1.2 Flash: Text to Video api_google_gemini_omni_flash_1_2_t2v-1.webp">

> Write the shot and get a 5-second 16:9 clip with synchronized audio: ambience, footsteps and UI clicks come out of the same pass. Gemini Omni 1.2 Flash keeps a fixed cast and layout across the clip, so game-lobby key art, product beats and menu shots hold together.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_2_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_gemini_omni_flash_1_2_t2v.json)

## Details

| | |
|---|---|
| Name | `api_google_gemini_omni_flash_1_2_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Gemini Omni 1.2 Flash |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-11-06 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.1 |
| Usage | 88 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #4 | video | api_google_gemini_omni_flash_1_2_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiVideoOmniV2` | 1 |  |
| `SaveVideo` | 1 |  |
