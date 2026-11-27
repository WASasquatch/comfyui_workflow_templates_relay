# Gemini Omni Flash: Video Edit

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_google_gemini_omni_flash_video_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_video_edit-1.webp" width="360" alt="Gemini Omni Flash: Video Edit api_google_gemini_omni_flash_video_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_video_edit-2.webp" width="360" alt="Gemini Omni Flash: Video Edit api_google_gemini_omni_flash_video_edit-2.webp">

> Edit videos with natural language using Gemini Omni Flash, transforming a single input video into one edited output based on your descriptive instructions. Specify the duration and aspect ratio in your prompt, and leverage Omni's world knowledge for intuitive edits like changing backgrounds or adding atmosphere. Ideal for quick social media remixes, cinematic scene adjustments, and iterative video refinements without technical prompts.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_google_gemini_omni_flash_video_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_gemini_omni_flash_video_edit.json)

## Details

| | |
|---|---|
| Name | `api_google_gemini_omni_flash_video_edit` |
| Category | Foundation › Video |
| Output | video |
| Models | Gemini Omni |
| Tags | API, Video Edit |
| Type | API |
| Date | 2026-06-30 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.2 |
| Usage | 13 |
| Nodes | 12 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #8 | video | space_horse_rider.mp4 |
| output | `SaveVideo` #2 | video | api_google_gemini_omni_flash_video_edit.mp4 |

## Subgraphs

- **Prompt Constructor** (7 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `StringConcatenate` | 4 | comfy-core |
| `CustomCombo` | 2 | comfy-core |
| `GeminiVideoOmniV2` | 1 |  |
| `LoadVideo` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `PreviewAny` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Duration and Aspect Ratio</summary>

The Google Gemini Omni Video requires you to specify the `duration` and `aspect ratio` in the prompt. The `Prompt Constructor` subgraph  helps you quickly construct the prompt with `duration` and `aspect ratio`.

</details>
