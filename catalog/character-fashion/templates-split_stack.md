# Character × 4 Scene Explorer

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-split_stack-1.webp" width="360" alt="Character × 4 Scene Explorer templates-split_stack-1.webp">

> Upload a reference image and generate a 1x4 grid. Select desired image and upscale/refine with Nano Banana Pro.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-split_stack.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-split_stack.json)

## Details

| | |
|---|---|
| Name | `templates-split_stack` |
| Category | Applied › Character & Fashion |
| Media type | image |
| Models | Google Gemini Image, Nano Banana Pro |
| Tags | API, Image Edit, Character Reference |
| Type | API |
| Date | 2026-01-13 |
| Author | hellorob |
| Min ComfyUI version | 0.15.0 |
| Usage | 12 |
| Nodes | 54 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | cube_robot.jpg |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)

## Subgraphs

- **Crop Images** (33 nodes)
- **Select and Batch** (5 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Reroute` | 18 |  |
| `SaveImage` | 7 | comfy-core |
| `SimpleMath+` | 7 | comfyui_essentials |
| `PreviewImage` | 5 | comfy-core |
| `ImageCrop` | 4 | comfy-core |
| `GeminiImage2Node` | 2 | comfy-core |
| `GetImageSize` | 2 | comfy-core |
| `PrimitiveStringMultiline` | 2 | comfy-core |
| `ImageBatch` | 1 | comfy-core |
| `ImageBatchMulti` | 1 | comfyui-kjnodes |
| `ImageFromBatch` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `PrimitiveInt` | 1 | comfy-core |
| `RegexReplace` | 1 | comfy-core |
| `ResizeAndPadImage` | 1 | comfy-core |
