# LED Billboard Message

[← Brand & Design](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-led_billboard-1.webp" width="360" alt="LED Billboard Message templates-led_billboard-1.webp">

> Upload a blank billboard and overlay text. Generate a smooth zoom in shot revealing your message.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-led_billboard.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-led_billboard.json)

## Details

| | |
|---|---|
| Name | `templates-led_billboard` |
| Category | Applied › Brand & Design |
| Media type | image |
| Models | Gemini3 Pro Image Preview, Google, Kling, Nano Banana Pro |
| Tags | API, Brand Design |
| Type | API |
| Date | 2026-01-19 |
| Author | hellorob |
| Min ComfyUI version | 0.13.0 |
| Usage | 1 |
| Nodes | 22 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #10 | image | billboard.png |
| input | `LoadImage` #12 | image | comfyorg_logo.png |

## Custom nodes required

- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)

## Subgraphs

- **Image to Outpaint** (7 nodes)
- **Batch Images** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SimpleMath+` | 3 | comfyui_essentials |
| `GeminiImage2Node` | 2 | comfy-core |
| `GetImageSize` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `PrimitiveStringMultiline` | 2 | comfy-core |
| `SaveImage` | 2 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `ImagePadForOutpaint` | 1 | comfy-core |
| `ImageScaleToTotalPixels` | 1 | comfy-core |
| `KlingFirstLastFrameNode` | 1 |  |
| `PreviewImage` | 1 | comfy-core |
| `PrimitiveInt` | 1 | comfy-core |
| `RegexReplace` | 1 | comfy-core |
| `ResizeAndPadImage` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
