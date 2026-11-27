# Character Portrait Relighting

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_character_portrait_relighting)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_character_portrait_relighting-1.webp" width="360" alt="Character Portrait Relighting template_character_portrait_relighting-1.webp">

> Upload a portrait of your character and create multiple cinematic lighting conditions while maintaining character consistency.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_character_portrait_relighting.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_character_portrait_relighting.json)

## Details

| | |
|---|---|
| Name | `template_character_portrait_relighting` |
| Category | Applied › Character & Fashion |
| Output | image |
| Models | Nano Banana Pro |
| Tags | Relight, Portrait, API |
| Type | API |
| Date | 2026-04-06 |
| Author | hellorob |
| Min ComfyUI version | 0.16.0 |
| Usage | 23 |
| Nodes | 11 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #124 | image | silver_hand.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiImage2Node` | 5 |  |
| `SaveImage` | 5 | comfy-core |
| `LoadImage` | 1 | comfy-core |
