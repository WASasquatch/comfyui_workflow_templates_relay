# Virtual Try On with Character - 4 in 1

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_rob_fashion_shoot_vton-4in1.app-1.webp" width="360" alt="Virtual Try On with Character - 4 in 1 templates_rob_fashion_shoot_vton-4in1.app-1.webp">

> Upload an image of your character and a flatlay of an outfit to be tried on. Generate 4 images in 1 Nano Banana prompt.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_rob_fashion_shoot_vton-4in1.app.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_rob_fashion_shoot_vton-4in1.app.json)

## Details

| | |
|---|---|
| Name | `templates_rob_fashion_shoot_vton-4in1.app` |
| Category | Applied › Character & Fashion |
| Media type | image |
| Models | Nano Banana Pro |
| Tags | API, Image Edit, Virtual Try-On |
| Type | API |
| Date | 2026-03-09 |
| Author | hellorob |
| Min ComfyUI version | 0.15.0 |
| Distributions | cloud |
| Usage | 39 |
| Nodes | 28 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | subject-templates_rob_fashion_shoot_vton-4in1.png |
| input | `LoadImage` #35 | image | outfit-templates_rob_fashion_shoot_vton-4in1.png |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)

## Subgraphs

- **Crop Images** (15 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SimpleMath+` | 8 | comfyui_essentials |
| `SaveImage` | 5 | comfy-core |
| `ImageCrop` | 4 | comfy-core |
| `GetImageSize` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `BatchImagesNode` | 1 |  |
| `GeminiImage2Node` | 1 | comfy-core |
| `ImageBatchMulti` | 1 | comfyui-kjnodes |
| `ImageResizeKJv2` | 1 | comfyui-kjnodes |
| `PrimitiveInt` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |
| `ResizeAndPadImage` | 1 | comfy-core |
