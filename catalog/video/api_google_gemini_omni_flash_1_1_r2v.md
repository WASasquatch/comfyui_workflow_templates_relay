# Gemini Omni 1.1 Flash: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_r2v-1.webp" width="360" alt="Gemini Omni 1.1 Flash: Reference to Video api_google_gemini_omni_flash_1_1_r2v-1.webp">

> Generate video that incorporates specific subjects from multiple reference images using Gemini Omni 1.1 Flash's reference mode: characters, products, and objects from your images appear in the scene while the image itself is never shown as a frame. Bind each image to a role with tags like <IMAGE_REF_0>, combine character references with style references, and direct the scene in plain language with native audio. Ideal for character-driven stories, product placement, and brand-consistent content.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_1_1_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_gemini_omni_flash_1_1_r2v.json)

## Details

| | |
|---|---|
| Name | `api_google_gemini_omni_flash_1_1_r2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | Gemini Omni 1.1 Flash |
| Tags | API, Reference to Video |
| Type | API |
| Date | 2026-08-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.2 |
| Usage | 52 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #11 | image | terracotta_eyeshadow_palette.png |
| input | `LoadImage` #15 | image | asian_female_model_beige_suit.png |
| output | `SaveVideo` #8 | video | api_google_gemini_omni_flash_1_1_r2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `GeminiVideoOmniV2` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Assets

- [terracotta_eyeshadow_palette.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/terracotta_eyeshadow_palette.png) — required workflow input (`input/terracotta_eyeshadow_palette.png`)
- [asian_female_model_beige_suit.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/asian_female_model_beige_suit.png) — required workflow input (`input/asian_female_model_beige_suit.png`)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
