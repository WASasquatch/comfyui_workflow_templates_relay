# Selfie + Text Prompt to Studio Photoshoot Doodle

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates-fashion_shoot_prompt_doodle)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-fashion_shoot_prompt_doodle-1.webp" width="360" alt="Selfie + Text Prompt to Studio Photoshoot Doodle templates-fashion_shoot_prompt_doodle-1.webp">

> Upload a selfie and describe your outfit in the prompt. Generate 4 fashion editorial photographs with fun doodle illustrations. Select which image to upscale and add back face details.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-fashion_shoot_prompt_doodle.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-fashion_shoot_prompt_doodle.json)

## Details

| | |
|---|---|
| Name | `templates-fashion_shoot_prompt_doodle` |
| Category | Applied › Character & Fashion |
| Output | image |
| Models | Google Gemini Image, Nano Banana Pro, Google, Gemini3 Pro Image Preview |
| Tags | API, Image Edit |
| Type | API |
| Date | 2025-12-15 |
| Author | hellorob |
| Min ComfyUI version | 0.15.0 |
| Usage | 2 |
| Nodes | 46 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | character-1.png |

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
| `SaveImage` | 7 | comfy-core |
| `PreviewImage` | 6 | comfy-core |
| `ImageCrop` | 4 | comfy-core |
| `GeminiImage2Node` | 3 | comfy-core |
| `PrimitiveStringMultiline` | 2 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageBatch` | 1 | comfy-core |
| `ImageBatchMulti` | 1 | comfyui-kjnodes |
| `ImageFromBatch` | 1 | comfy-core |
| `ImageResizeKJv2` | 1 | comfyui-kjnodes |
| `LoadImage` | 1 | comfy-core |
| `Note` | 1 |  |
| `PrimitiveInt` | 1 | comfy-core |
| `RegexReplace` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
Change batch_index to select which image you want to outpaint.

(first image is index 0)
```

</details>
