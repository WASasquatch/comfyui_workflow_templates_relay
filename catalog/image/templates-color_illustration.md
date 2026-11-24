# Add Color to Line Art Illustration

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-color_illustration-1.webp" width="360" alt="Add Color to Line Art Illustration templates-color_illustration-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-color_illustration-2.webp" width="360" alt="Add Color to Line Art Illustration templates-color_illustration-2.webp">

> Input a black and white illustration and generate a colored output.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-color_illustration.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-color_illustration.json)

## Details

| | |
|---|---|
| Name | `templates-color_illustration` |
| Category | Foundation › Image |
| Media type | image |
| Models | Gemini3 Pro Image Preview, Google, Nano Banana Pro |
| Tags | API, Image Edit |
| Type | API |
| Date | 2025-12-20 |
| Author | hellorob |
| Min ComfyUI version | 0.3.71 |
| Usage | 12 |
| Nodes | 3 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #10 | image | illustration_bw.png |
| output | `SaveImage` #11 | image | templates-color_illustration.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiImage2Node` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
