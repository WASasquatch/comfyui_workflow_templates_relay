# Aspect Ratio Extend: Kling O3

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_horizontal_vertical_extension)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_horizontal_vertical_extension-1.webp" width="360" alt="Aspect Ratio Extend: Kling O3 template_horizontal_vertical_extension-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_horizontal_vertical_extension-2.webp" width="360" alt="Aspect Ratio Extend: Kling O3 template_horizontal_vertical_extension-2.webp">

> Extend any video to a custom aspect ratio. Convert vertical videos to horizontal format and vice versa. Includes an application mode for easy use.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_horizontal_vertical_extension.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_horizontal_vertical_extension.json)

## Details

| | |
|---|---|
| Name | `template_horizontal_vertical_extension` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | Kling O3 |
| Tags | API, Video, Video Edit, Outpainting |
| Type | API |
| Date | 2026-03-30 |
| Author | shane |
| Min ComfyUI version | 0.16.0 |
| Usage | 52 |
| Nodes | 21 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #247 | video | animated_man_framing.mp4 |
| output | `SaveVideo` #270 | video | template_horizontal_vertical_extension.mp4 |

## Custom nodes required

- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)
- [comfyui_layerstyle](https://registry.comfy.org/nodes/comfyui_layerstyle)
- [masquerade-nodes-comfyui](https://registry.comfy.org/nodes/masquerade-nodes-comfyui)

## Subgraphs

- **Video Extend** (13 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LayerUtility: ColorImage V2` | 3 | comfyui_layerstyle |
| `PreviewImage` | 3 | comfy-core |
| `Paste By Mask` | 2 | masquerade-nodes-comfyui |
| `CreateVideo` | 1 | comfy-core |
| `Get Image Size` | 1 | masquerade-nodes-comfyui |
| `GetVideoComponents` | 1 | comfy-core |
| `ImageRemoveAlpha+` | 1 | comfyui_essentials |
| `ImageToMask` | 1 | comfy-core |
| `JWImageResizeByShorterSide` | 1 |  |
| `KlingOmniProEditVideoNode` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `Note` | 1 |  |
| `ResolutionSelector` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `Video Slice` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
Adjust the offsets to reframe the video vertically or horizontally before extension

This workflow is only designed for horizontal to vertical and vice versa. If you want to adjust the aspect ratio only slightly or to 1x1 square format, Kling Video Edit node is not recommended.
```

</details>

<details><summary>Change Fill Color</summary>

## Tips

- If your image doesn't have enough contrast to the empty area, change the background color here 👉

</details>
