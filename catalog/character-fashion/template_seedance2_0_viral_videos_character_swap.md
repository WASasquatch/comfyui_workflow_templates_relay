# Seedance 2.0: Viral Videos Character Swap

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_seedance2_0_viral_videos_character_swap)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_seedance2_0_viral_videos_character_swap-1.webp" width="360" alt="Seedance 2.0: Viral Videos Character Swap template_seedance2_0_viral_videos_character_swap-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_seedance2_0_viral_videos_character_swap-2.webp" width="360" alt="Seedance 2.0: Viral Videos Character Swap template_seedance2_0_viral_videos_character_swap-2.webp">

> A one click workflow to recreate an input video with your character. All you need to do is upload the video and your character. This workflow uses Google Gemini LLM to analyze the input video and reverse engineer a prompt. You can prompt for specific details to inject into this analysis. The workflow extracts the first frame of the video and swaps your character into it, sends this into Seedance 2.0 Reference-to-Video and generates

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_seedance2_0_viral_videos_character_swap.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_seedance2_0_viral_videos_character_swap.json)

## Details

| | |
|---|---|
| Name | `template_seedance2_0_viral_videos_character_swap` |
| Category | Applied › Character & Fashion |
| Output | image |
| Models | GPT Image 2, Google Gemini, Seedance 2.0 |
| Tags | API, Character Replacement, Image to Video |
| Type | API |
| Date | 2026-05-19 |
| Author | hellorob |
| Min ComfyUI version | 0.35.2 |
| Usage | 21 |
| Nodes | 12 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #18 | video | source_ref_video.mp4 |
| input | `LoadImage` #29 | image | virtual_character_ref.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDance2ReferenceNodeV2` | 1 |  |
| `GeminiNodeV3` | 1 |  |
| `GetVideoComponents` | 1 | comfy-core |
| `ImageFromBatch` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `OpenAIGPTImageNodeV2` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `StringConcatenate` | 1 | comfy-core |
| `Video Slice` | 1 | comfy-core |
