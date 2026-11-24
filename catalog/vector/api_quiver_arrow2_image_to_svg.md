# Arrow2: Image to SVG

[← Vector](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_quiver_arrow2_image_to_svg-1.webp" width="360" alt="Arrow2: Image to SVG api_quiver_arrow2_image_to_svg-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_quiver_arrow2_image_to_svg-2.webp" width="360" alt="Arrow2: Image to SVG api_quiver_arrow2_image_to_svg-2.webp">

> Convert a raster image into a clean, editable SVG vector using Arrow 2, taking one image and returning one vector output. The model produces cleaner geometry and stronger composition with fewer control points. Ideal for vectorizing sketches, logos, and line art, or preparing scalable brand and product assets.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_quiver_arrow2_image_to_svg.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_quiver_arrow2_image_to_svg.json)

## Details

| | |
|---|---|
| Name | `api_quiver_arrow2_image_to_svg` |
| Category | Foundation › Vector |
| Media type | image |
| Models | Quiver |
| Tags | API, Vector |
| Type | API |
| Date | 2026-09-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.39.2 |
| Usage | 22 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #22 | image | retro_office_car_scene.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `QuiverImageToSVGNodeV2` | 1 |  |
| `SaveSVGNode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Input Asset

- [retro_office_car_scene.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/retro_office_car_scene.png)


## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
