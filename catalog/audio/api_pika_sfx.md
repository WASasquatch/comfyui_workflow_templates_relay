# Pika: Text to Sound Effects

[← Audio](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_pika_sfx)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pika_sfx-1.webp" width="360" alt="Pika: Text to Sound Effects api_pika_sfx-1.webp">

> Describe a single sound and get it back as a finished audio clip with Pika SFX through the partner API. Name the material, the action, the space and the intensity in one line, set a length between 1 and 20 seconds, and the node returns a mono sound effect that drops straight into a timeline. Ideal for foley, game UI blips, trailer hits and ambience beds that are faster to generate than to record.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pika_sfx.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_pika_sfx.json)

## Details

| | |
|---|---|
| Name | `api_pika_sfx` |
| Category | Foundation › Audio |
| Output | audio |
| Models | Pika |
| Tags | API, Audio, Text to Audio |
| Type | API |
| Date | 2026-11-09 |
| Author | ComfyUI |
| Min ComfyUI version | 0.44.1 |
| Usage | 76 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveAudioAdvanced` #2 | audio | api_pika_sfx.mp3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PikaSFXNode` | 1 | comfy-core |
| `SaveAudioAdvanced` | 1 | comfy-core |
