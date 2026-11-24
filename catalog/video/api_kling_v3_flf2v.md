# Kling 3.0: First Last Frame to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_kling_v3_flf2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_v3_flf2v-1.webp" width="360" alt="Kling 3.0: First Last Frame to Video api_kling_v3_flf2v-1.webp">

> Input a first and last frame image to generate a continuous video sequence with multi-shot generation, precise element control, and support for multilingual prompts.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_kling_v3_flf2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_kling_v3_flf2v.json)

## Details

| | |
|---|---|
| Name | `api_kling_v3_flf2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Kling 3.0 |
| Tags | API, Video, FLF2V |
| Type | API |
| Date | 2026-02-10 |
| Author | ComfyUI |
| Min ComfyUI version | 0.13.0 |
| Usage | 298 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | goldenfish_in_bag.png |
| input | `LoadImage` #13 | image | man_in_daydream.png |
| output | `SaveVideo` #2 | video | Kling_v3_flf2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `KlingFirstLastFrameNode` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
