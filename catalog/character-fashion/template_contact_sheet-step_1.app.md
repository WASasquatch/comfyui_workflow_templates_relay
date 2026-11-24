# Step 1: Contact Sheet Workflow

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_contact_sheet-step_1.app-1.webp" width="360" alt="Step 1: Contact Sheet Workflow template_contact_sheet-step_1.app-1.webp">

> Upload your character, scene and product. Integrates all images into a fashion editorial style photograph.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_contact_sheet-step_1.app.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_contact_sheet-step_1.app.json)

## Details

| | |
|---|---|
| Name | `template_contact_sheet-step_1.app` |
| Category | Applied › Character & Fashion |
| Media type | image |
| Models | Nano Banana Pro |
| Tags | API, Image, Image Edit |
| Type | API |
| Date | 2026-03-30 |
| Author | hellorob |
| Min ComfyUI version | 0.8.0 |
| Usage | 41 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | snake_on_jacket.jpg |
| input | `LoadImage` #2 | image | forest_background.jpg |
| input | `LoadImage` #5 | image | brown_moisturizer_bottle.jpg |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 3 | comfy-core |
| `BatchImagesNode` | 1 |  |
| `GeminiImage2Node` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 |  |
| `SaveImage` | 1 | comfy-core |
