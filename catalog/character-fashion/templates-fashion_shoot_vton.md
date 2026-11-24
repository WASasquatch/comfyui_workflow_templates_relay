# Character + Clothing (OOTD) Flat Lay to Studio Photoshoot

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates-fashion_shoot_vton)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-fashion_shoot_vton-1.webp" width="360" alt="Character + Clothing (OOTD) Flat Lay to Studio Photoshoot templates-fashion_shoot_vton-1.webp">

> Upload an image of your character and a flatlay image of your clothing items. Generate 4 fashion editorial photographs of your character in the outfit. Select which image to upscale and add back details.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-fashion_shoot_vton.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-fashion_shoot_vton.json)

## Details

| | |
|---|---|
| Name | `templates-fashion_shoot_vton` |
| Category | Applied › Character & Fashion |
| Output | image |
| Models | Google Gemini Image, Nano Banana Pro, Google, Gemini3 Pro Image Preview |
| Tags | API, Image Edit |
| Type | API |
| Date | 2025-12-15 |
| Author | hellorob |
| Min ComfyUI version | 0.15.0 |
| Usage | 62 |
| Nodes | 46 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | subject.png |
| input | `LoadImage` #35 | image | outfit.png |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)

## Subgraphs

- **Crop Images** (20 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SimpleMath+` | 8 | comfyui_essentials |
| `Reroute` | 7 |  |
| `PreviewImage` | 6 | comfy-core |
| `SaveImage` | 6 | comfy-core |
| `ImageCrop` | 4 | comfy-core |
| `GeminiImage2Node` | 2 | comfy-core |
| `GetImageSize` | 2 | comfy-core |
| `ImageBatch` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `ImageBatchMulti` | 1 | comfyui-kjnodes |
| `ImageFromBatch` | 1 | comfy-core |
| `ImageResizeKJv2` | 1 | comfyui-kjnodes |
| `Note` | 1 |  |
| `PrimitiveInt` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |
| `ResizeAndPadImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
Change batch_index to select which image you want to outpaint.

(first image is index 0)
```

</details>
