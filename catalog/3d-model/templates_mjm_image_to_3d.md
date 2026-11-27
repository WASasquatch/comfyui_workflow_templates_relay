# Generate 3D Model From Single Image

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_mjm_image_to_3d)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_mjm_image_to_3d-1.webp" width="360" alt="Generate 3D Model From Single Image templates_mjm_image_to_3d-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_mjm_image_to_3d-2.webp" width="360" alt="Generate 3D Model From Single Image templates_mjm_image_to_3d-2.webp">

> Input a single image to automatically generate three orthographic views. Use these multiviews with Meshy to create a textured 3D model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_mjm_image_to_3d.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_mjm_image_to_3d.json)

## Details

| | |
|---|---|
| Name | `templates_mjm_image_to_3d` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Meshy, Nano Banana 2 |
| Tags | API, 3D, Image to 3D |
| Type | API |
| Date | 2026-03-19 |
| Author | Julien \| MJM |
| Min ComfyUI version | 0.36.0 |
| Usage | 32 |
| Nodes | 12 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | templates_mjm_image_to_3d.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GeminiImage2Node` | 3 | comfy-core |
| `SaveImage` | 3 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `Preview3DAdvanced` | 1 | comfy-core |
| `SaveGLB` | 1 | comfy-core |
| `TripoImageToModelNodeV2` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Image To 3D - How it works!</summary>

Turn a **single image** into a 3D model.

## How It Works

1. **Upload an image**
2. **Start the workflow and it will generate the required side and rear shots to create a 3D model from your input**

Enjoy!

</details>
