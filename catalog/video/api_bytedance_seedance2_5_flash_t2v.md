# Seedance 2.5 Flash: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bytedance_seedance2_5_flash_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedance2_5_flash_t2v-1.webp" width="360" alt="Seedance 2.5 Flash: Text to Video api_bytedance_seedance2_5_flash_t2v-1.webp">

> Generate videos from a text prompt with Seedance 2.5 Flash, the faster, lower-cost tier of Seedance 2.5: one prompt produces a multi-shot clip with synchronized sound, at 480p or 720p and up to 30 seconds. Ideal for iterating on a shot list before committing to a full-quality render.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_seedance2_5_flash_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bytedance_seedance2_5_flash_t2v.json)

## Details

| | |
|---|---|
| Name | `api_bytedance_seedance2_5_flash_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Seedance 2.5 |
| Tags | API, Text to Video |
| Type | API |
| Date | 2026-11-15 |
| Author | ComfyUI |
| Min ComfyUI version | 0.45.4 |
| Usage | 249 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #2 | video | api_bytedance_seedance2_5_flash_t2v.mp4 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDance2TextToVideoNode` | 1 |  |
| `SaveVideo` | 1 |  |
