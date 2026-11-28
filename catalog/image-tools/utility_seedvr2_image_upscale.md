# Image Upscale: SeedVR2

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_seedvr2_image_upscale)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_seedvr2_image_upscale-1.webp" width="360" alt="Image Upscale: SeedVR2 utility_seedvr2_image_upscale-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_seedvr2_image_upscale-2.webp" width="360" alt="Image Upscale: SeedVR2 utility_seedvr2_image_upscale-2.webp">

> Upload an image to upscale it with SeedVR2 and generate a high-definition output.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_seedvr2_image_upscale.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_seedvr2_image_upscale.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/image-upscale)

## Details

| | |
|---|---|
| Name | `utility_seedvr2_image_upscale` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | SeedVR2 |
| Tags | Image Upscale |
| Type | open source |
| Date | 2026-02-06 |
| Author | ComfyUI |
| Download size | 16.5 GB |
| Min ComfyUI version | 0.28.0 |
| Usage | 988 |
| Nodes | 13 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #24 | image | vr_ad.png |
| output | `SaveImage` #45 | image | utility_seedvr2_image_upscale.png |

## Custom nodes required

- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)
- [seedvr2_videoupscaler](https://registry.comfy.org/nodes/seedvr2_videoupscaler)

## Subgraphs

- **Image Upscale(SeedVR2)** (9 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `GetImageSize` | 1 | comfy-core |
| `ImageCompare` | 1 |  |
| `ImpactCompare` | 1 |  |
| `LayerUtility: If` | 1 |  |
| `LoadImage` | 1 | comfy-core |
| `PrimitiveFloat` | 1 | comfy-core |
| `SaveImage` | 1 |  |
| `SeedVR2LoadDiTModel` | 1 | seedvr2_videoupscaler |
| `SeedVR2LoadVAEModel` | 1 | seedvr2_videoupscaler |
| `SeedVR2VideoUpscaler` | 1 | seedvr2_videoupscaler |
| `SimpleMath+` | 1 | comfyui_essentials |

## Notes embedded in the workflow

<details><summary>Note</summary>

Image Compare is now only available under Nodes 2.0. Open menu -> Nodes 2.0 to switch

</details>

<details><summary>Note</summary>

## About SeedVR2

You can watch a comprehensive tutorial from the author on [Youtube](https://www.youtube.com/watch?v=MBtWYXq_r60) or check out the [Github](https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler).

## Quick Notes
Hover over the node inputs for tooltip info from author

input_noise_scale softens higher frequency details (e.g. skin textures)

latent_noise_scale softens low frequency details. Best around 0.01-0.05 (but depends on upscale factor)

Nodes support alpha masks

</details>
