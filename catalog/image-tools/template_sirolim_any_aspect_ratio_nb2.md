# Any Image → Any Aspect Ratio

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_sirolim_any_aspect_ratio_nb2-1.webp" width="360" alt="Any Image → Any Aspect Ratio template_sirolim_any_aspect_ratio_nb2-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_sirolim_any_aspect_ratio_nb2-2.webp" width="360" alt="Any Image → Any Aspect Ratio template_sirolim_any_aspect_ratio_nb2-2.webp">

> Upload any image and input your desired aspect ratio. Generate an outpainted version of your image to perfectly fit the new dimensions.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_sirolim_any_aspect_ratio_nb2.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_sirolim_any_aspect_ratio_nb2.json)

## Details

| | |
|---|---|
| Name | `template_sirolim_any_aspect_ratio_nb2` |
| Category | Foundation › Image Tools |
| Media type | image |
| Models | Nano Banana 2 |
| Tags | API, Image, Outpainting, Image Edit |
| Type | API |
| Date | 2026-03-08 |
| Author | sirolim |
| Min ComfyUI version | 0.20.3 |
| Usage | 19 |
| Nodes | 22 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #130 | image | input-aspect-ratio-converter |

## Custom nodes required

- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)
- [controlaltai-nodes](https://registry.comfy.org/nodes/controlaltai-nodes)
- [masquerade-nodes-comfyui](https://registry.comfy.org/nodes/masquerade-nodes-comfyui)

## Subgraphs

- **Image Extender** (16 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewImage` | 5 |  |
| `LayerUtility: ColorImage V2` | 3 |  |
| `ImageToMask` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `Paste By Mask` | 2 | masquerade-nodes-comfyui |
| `FluxResolutionNode` | 1 | controlaltai-nodes |
| `GeminiNanoBanana2` | 1 |  |
| `Get Image Size` | 1 | masquerade-nodes-comfyui |
| `ImageCompositeMasked` | 1 | comfy-core |
| `ImageRemoveAlpha+` | 1 | comfyui_essentials |
| `InvertMask` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MaskComposite` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>🖼️ Any Image → Any Aspect Ratio</summary>

Turn a **single image** into an animated GIF + WebM.

## How It Works

1. **Upload a image**
2. Choose the target aspect ratio
(e.g. “16:9”, “9:16”, “1:1”, “4:5”, etc.)

3. The system:
   - Adapts your image to the target aspect ratio
   - Fills in the gaps with Nano Banana 2

## Tips

- If your image doesn't have enough contrast to the empty area, change the background color in the Image Extender.

That’s it.  
Single image → any aspect ratio.

</details>

<details><summary>Change Fill Color</summary>

## Tips

- If your image doesn't have enough contrast to the empty area, change the background color here 👉

</details>
