# Seedance 2.5: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_seedance2_5_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_t2v-1.webp" width="360" alt="Seedance 2.5: Text to Video api_seedance2_5_t2v-1.webp">

> Generate 30-second cinematic videos from text prompts with Seedance 2.5, producing synchronized sound and music alongside the footage. Input a single text prompt to create one video with precise camera control and multi-shot storytelling. Ideal for brand films, episodic series, and e-commerce content where quality matters more than budget.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_seedance2_5_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_seedance2_5_t2v.json)

## Details

| | |
|---|---|
| Name | `api_seedance2_5_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Seedance 2.5 |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-08-07 |
| Author | ComfyUI |
| Min ComfyUI version | 0.31.0 |
| Usage | 181 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #2 | video | api_seedance2_5_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDance2TextToVideoNode` | 1 |  |
| `SaveVideo` | 1 |  |
