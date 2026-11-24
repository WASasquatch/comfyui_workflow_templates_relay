# Step 3: Contact Sheet Workflow

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_contact_sheet-step_3.app)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_contact_sheet-step_3.app-1.webp" width="360" alt="Step 3: Contact Sheet Workflow template_contact_sheet-step_3.app-1.webp">

> Upload 8 images (in order) to be used as keyframes for 7 Kling 3.0 FLF2V videos.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_contact_sheet-step_3.app.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_contact_sheet-step_3.app.json)

## Details

| | |
|---|---|
| Name | `template_contact_sheet-step_3.app` |
| Category | Applied › Character & Fashion |
| Output | image |
| Models | Gemini-3.1-flash-lite, Kling 3.0 |
| Tags | API, FLF2V, Video |
| Type | API |
| Date | 2026-03-30 |
| Author | hellorob |
| Min ComfyUI version | 0.35.2 |
| Usage | 9 |
| Nodes | 61 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #224 | image | contact_sheet_app_input_1.png |
| input | `LoadImage` #226 | image | contact_sheet_app_input_2.png |
| input | `LoadImage` #227 | image | contact_sheet_app_input_3.png |
| input | `LoadImage` #228 | image | contact_sheet_app_input_4.png |
| input | `LoadImage` #232 | image | contact_sheet_app_input_5.png |
| input | `LoadImage` #233 | image | contact_sheet_app_input_6.png |
| input | `LoadImage` #234 | image | contact_sheet_app_input_7.png |

## Subgraphs

- **Generate Video 1** (6 nodes)
- **Generate Video 2** (6 nodes)
- **Generate Video 3** (6 nodes)
- **Generate Video 4** (6 nodes)
- **Generate Video 5** (6 nodes)
- **Generate Video 6** (6 nodes)
- **Generate Video 7** (6 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ImageFromBatch` | 14 | comfy-core |
| `BatchImagesNode` | 8 |  |
| `GeminiNode` | 7 | comfy-core |
| `KlingFirstLastFrameNode` | 7 |  |
| `LoadImage` | 7 |  |
| `PreviewAny` | 7 | comfy-core |
| `SaveVideo` | 7 | comfy-core |
| `PrimitiveNode` | 2 |  |
| `Reroute` | 2 |  |
