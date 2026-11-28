# Generate Brand Packaging from Dieline

[← Product & Ads](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates-assemble_dieline)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-assemble_dieline-1.webp" width="360" alt="Generate Brand Packaging from Dieline templates-assemble_dieline-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-assemble_dieline-2.webp" width="360" alt="Generate Brand Packaging from Dieline templates-assemble_dieline-2.webp">

> Upload a dieline of your product and assemble into a 3D package.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-assemble_dieline.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-assemble_dieline.json)

## Details

| | |
|---|---|
| Name | `templates-assemble_dieline` |
| Category | Applied › Product & Ads |
| Output | image |
| Models | Google, Google Gemini Image, Nano Banana Pro |
| Tags | API, Image Edit |
| Type | API |
| Date | 2025-12-15 |
| Author | hellorob |
| Min ComfyUI version | 0.3.71 |
| Usage | 23 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | dieline.jpg |
| output | `SaveImage` #6 | image | templates-assemble_dieline.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiImage2Node` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
