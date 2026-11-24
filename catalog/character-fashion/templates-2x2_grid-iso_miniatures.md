# Isometric Miniatures from a Selfie

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-2x2_grid-iso_miniatures-1.webp" width="360" alt="Isometric Miniatures from a Selfie templates-2x2_grid-iso_miniatures-1.webp">

> Upload a character or selfie and prompt the outfit/scene. Generate a 2x2 grid of isometric figurines of your character.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-2x2_grid-iso_miniatures.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-2x2_grid-iso_miniatures.json)

## Details

| | |
|---|---|
| Name | `templates-2x2_grid-iso_miniatures` |
| Category | Applied › Character & Fashion |
| Media type | image |
| Models | Nano Banana Pro, Gemini3 Pro Image Preview, Google |
| Tags | API, Portrait |
| Type | API |
| Date | 2026-01-19 |
| Author | hellorob |
| Min ComfyUI version | 0.15.0 |
| Usage | 4 |
| Nodes | 35 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | character_in_red_jacket.png |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)

## Subgraphs

- **Crop Images** (20 nodes)
- **Prompt Template** (4 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SimpleMath+` | 8 | comfyui_essentials |
| `PreviewImage` | 5 | comfy-core |
| `SaveImage` | 5 | comfy-core |
| `ImageCrop` | 4 | comfy-core |
| `PrimitiveStringMultiline` | 3 | comfy-core |
| `RegexReplace` | 2 | comfy-core |
| `GeminiImage2Node` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageBatchMulti` | 1 | comfyui-kjnodes |
| `ImageResizeKJv2` | 1 | comfyui-kjnodes |
| `LoadImage` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `PrimitiveInt` | 1 | comfy-core |
| `StringConcatenate` | 1 | comfy-core |
