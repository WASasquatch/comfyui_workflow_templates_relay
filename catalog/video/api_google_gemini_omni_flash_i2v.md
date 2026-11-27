# Gemini Omni Flash: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_google_gemini_omni_flash_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_i2v-1.webp" width="360" alt="Gemini Omni Flash: Image to Video api_google_gemini_omni_flash_i2v-1.webp">

> Generate a video from two images using Gemini Omni Flash, which interprets natural language prompts to control duration and aspect ratio. The workflow accepts 2 input images and produces 1 video output. Ideal for creating short brand clips, dynamic social media content, and iterative video edits through conversational prompting.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_gemini_omni_flash_i2v.json)

## Details

| | |
|---|---|
| Name | `api_google_gemini_omni_flash_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Gemini Omni |
| Tags | API, Image to Video |
| Type | API |
| Date | 2026-06-30 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.2 |
| Usage | 23 |
| Nodes | 13 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #5 | image | clay_toy_shop_old_man.png |
| input | `LoadImage` #6 | image | comic_toy_store_strips.png |
| output | `SaveVideo` #2 | video | api_google_gemini_omni_flash_i2v.mp4 |

## Subgraphs

- **Prompt Constructor** (7 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `StringConcatenate` | 4 | comfy-core |
| `CustomCombo` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `GeminiVideoOmniV2` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PreviewAny` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Duration and Aspect Ratio</summary>

The Google Gemini Omni Video requires you to specify the `duration` and `aspect ratio` in the prompt. The `Prompt Constructor` subgraph  helps you quickly construct the prompt with `duration` and `aspect ratio`.

</details>
