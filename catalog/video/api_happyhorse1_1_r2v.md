# HappyHorse 1.1: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_happyhorse1_1_r2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_1_r2v-1.webp" width="360" alt="HappyHorse 1.1: Reference to Video api_happyhorse1_1_r2v-1.webp">

> Generate video from reference images using HappyHorse 1.1, locking character and scene appearance while following a text prompt for motion. This workflow takes 2 input images (character reference and scene reference) and produces 1 video output. Ideal for short films, advertising, and game cutscenes requiring consistent character design and controllable narrative.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_happyhorse1_1_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_happyhorse1_1_r2v.json)

## Details

| | |
|---|---|
| Name | `api_happyhorse1_1_r2v` |
| Category | Foundation › Video |
| Output | video |
| Models | HappyHorse 1.1 |
| Tags | API, Reference to Video |
| Type | API |
| Date | 2026-06-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.26.1 |
| Usage | 9 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | wooden_doll_2_views.png |
| input | `LoadImage` #3 | image | cave_ocean_living_room.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `HappyHorseReferenceVideoApi` | 1 |  |
| `SaveVideo` | 1 |  |
