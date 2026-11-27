# Single Image to Animated Sprite Sheet

[← Brand & Design](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_purz_nb2_single_image_sprite_sheet)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_purz_nb2_single_image_sprite_sheet-1.webp" width="360" alt="Single Image to Animated Sprite Sheet template_purz_nb2_single_image_sprite_sheet-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_purz_nb2_single_image_sprite_sheet-2.webp" width="360" alt="Single Image to Animated Sprite Sheet template_purz_nb2_single_image_sprite_sheet-2.webp">

> Upload a single image to generate an animated sequence. The workflow creates a sprite sheet with multiple frames for use in games or animations.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_purz_nb2_single_image_sprite_sheet.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_purz_nb2_single_image_sprite_sheet.json)

## Details

| | |
|---|---|
| Name | `template_purz_nb2_single_image_sprite_sheet` |
| Category | Applied › Brand & Design |
| Output | image |
| Models | Nano Banana 2 |
| Tags | API, Game |
| Type | API |
| Date | 2026-03-08 |
| Author | PurzBeats |
| Min ComfyUI version | 0.20.3 |
| Usage | 15 |
| Nodes | 43 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #14 | image | nb2-single_image_sprite_sheet-input |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui-rmbg](https://registry.comfy.org/nodes/comfyui-rmbg)
- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)
- [was-ns](https://registry.comfy.org/nodes/was-ns)

## Subgraphs

- **Animated Sprite Sheet** (28 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveImage` | 9 | comfy-core |
| `Image Crop Location` | 8 | was-ns |
| `Reroute` | 7 |  |
| `SimpleMath+` | 5 | comfyui_essentials |
| `PreviewAny` | 4 | comfy-core |
| `VHS_VideoCombine` | 2 | comfyui-videohelpersuite |
| `BatchImagesNode` | 1 | comfy-core |
| `BiRefNetRMBG` | 1 | comfyui-rmbg |
| `GeminiImage2Node` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImageWithAlpha` | 1 | comfyui-kjnodes |
| `SplitImageWithAlpha` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>🍌 Single Image -> Animated Sprite Sheet</summary>

Turn a **single image** into an animated GIF + WebM.

## How It Works

1. **Upload one image**
2. **Describe the animation** in the prompt box  
   (e.g. “8-frame looping idle, subtle breathing, soft blink”)
3. The system:
   - Calls **Nano Banana 2**
   - Generates a sprite sheet
   - Removes background
   - Slices frames automatically
   - Exports an **animated GIF + WebM**

## Tips

- Say “looping” if you want to try for a seamless loop  
- Specify frame rate in Video Combine node (8, 12, 16, etc.)  
- Mention style constraints (pixel art, no blur, smooth motion)

That’s it.  
Single image → structured sprite sheet → ready-to-use animation.

</details>
