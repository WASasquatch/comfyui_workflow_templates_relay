# Step 2: Contact Sheet Workflow

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_contact_sheet-step_2.app-1.webp" width="360" alt="Step 2: Contact Sheet Workflow template_contact_sheet-step_2.app-1.webp">

> Upload the fashion editorial and product image. Generate 8 distinct angle variations with product consistency from only 2 Nano Banana generations.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_contact_sheet-step_2.app.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_contact_sheet-step_2.app.json)

## Details

| | |
|---|---|
| Name | `template_contact_sheet-step_2.app` |
| Category | Applied › Character & Fashion |
| Media type | image |
| Models | Nano Banana Pro |
| Tags | API, Video, Image Edit |
| Type | API |
| Date | 2026-03-30 |
| Author | hellorob |
| Min ComfyUI version | 0.8.0 |
| Usage | 8 |
| Nodes | 39 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #16 | image | contact_sheet_app_input_1.png |
| input | `LoadImage` #26 | image | brown_moisturizer_bottle.jpg |

## Custom nodes required

- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)

## Subgraphs

- **Crop Images** (8 nodes)
- **Crop Images** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ImageCrop+` | 8 |  |
| `SaveImage` | 8 | comfy-core |
| `SimpleMath+` | 6 | comfyui_essentials |
| `PrimitiveStringMultiline` | 4 | comfy-core |
| `PrimitiveNode` | 3 |  |
| `BatchImagesNode` | 2 |  |
| `GeminiImage2Node` | 2 | comfy-core |
| `GetImageSize` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `RegexReplace` | 2 |  |
