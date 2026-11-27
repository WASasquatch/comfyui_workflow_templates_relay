# Poster Scene Mockups

[← Brand & Design](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates-poster_to_2x2_mockups-v2.0)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-poster_to_2x2_mockups-v2.0-1.webp" width="360" alt="Poster Scene Mockups templates-poster_to_2x2_mockups-v2.0-1.webp">

> Upload a poster/ad design and with a short input about your brand, generate 4 mockups in multiple scenes.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-poster_to_2x2_mockups-v2.0.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-poster_to_2x2_mockups-v2.0.json)

## Details

| | |
|---|---|
| Name | `templates-poster_to_2x2_mockups-v2.0` |
| Category | Applied › Brand & Design |
| Output | image |
| Models | Nano Banana Pro, Google |
| Tags | API, Image Edit |
| Type | API |
| Date | 2025-12-06 |
| Author | hellorob |
| Min ComfyUI version | 0.15.0 |
| Usage | 14 |
| Nodes | 43 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | template_Poster_Scene_Mockups.jpg |

## Custom nodes required

- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)

## Subgraphs

- **Crop Images** (19 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveImage` | 6 | comfy-core |
| `SimpleMath+` | 6 | comfyui_essentials |
| `ImageCropV2` | 4 | comfy-core |
| `PreviewImage` | 4 | comfy-core |
| `PrimitiveBoundingBox` | 4 |  |
| `PrimitiveStringMultiline` | 4 |  |
| `RegexReplace` | 3 |  |
| `GeminiImage2Node` | 2 | comfy-core |
| `GetImageSize` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `ImageBatchMulti` | 1 |  |
| `ImageFromBatch` | 1 | comfy-core |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `ResizeAndPadImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Required Custom Nodes (For local user)</summary>

[Guide: Install custom node](https://docs.comfy.org/installation/install_custom_node)

- [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes)
- [ComfyUI_essentials](https://github.com/cubiq/ComfyUI_essentials)

</details>
