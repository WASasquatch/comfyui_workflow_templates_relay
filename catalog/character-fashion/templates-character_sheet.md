# 360 Full-body Turnaround

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates-character_sheet)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-character_sheet-1.webp" width="360" alt="360 Full-body Turnaround templates-character_sheet-1.webp">

> Upload your character and generate 360 turnaround views for full body and close ups.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-character_sheet.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-character_sheet.json)

## Details

| | |
|---|---|
| Name | `templates-character_sheet` |
| Category | Applied › Character & Fashion |
| Output | image |
| Models | Gemini3 Pro Image Preview, Google, Nano Banana Pro |
| Tags | API, Character Reference |
| Type | API |
| Date | 2026-01-13 |
| Author | hellorob |
| Min ComfyUI version | 0.3.71 |
| Usage | 118 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | templates-character_sheet_pink_silver_outfit.jpg |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveImage` | 3 | comfy-core |
| `GeminiImage2Node` | 2 | comfy-core |
| `Reroute` | 2 |  |
| `ImageStitch` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
