# Gemini Omni Flash: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_t2v-1.webp" width="360" alt="Gemini Omni Flash: Text to Video api_google_gemini_omni_flash_t2v-1.webp">

> Generate cinematic video from natural language prompts using Gemini Omni Flash, transforming text descriptions into a single video output with world-aware motion, lighting, and sound. Ideal for social media content creation, rapid video prototyping, and iterative visual storytelling with conversational editing.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_gemini_omni_flash_t2v.json)

## Details

| | |
|---|---|
| Name | `api_google_gemini_omni_flash_t2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | Gemini Omni |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-06-30 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.2 |
| Usage | 16 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #2 | video | api_google_gemini_omni_flash_t2i.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiVideoOmniV2` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
