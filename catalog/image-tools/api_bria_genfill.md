# Inpainting: Bria Generative Fill

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bria_genfill)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_genfill-1.webp" width="360" alt="Inpainting: Bria Generative Fill api_bria_genfill-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_genfill-2.webp" width="360" alt="Inpainting: Bria Generative Fill api_bria_genfill-2.webp">

> Use Bria's Generative Fill API to regenerate a specific region of an image while keeping everything outside the mask pixel-perfect unchanged. Paint a mask over the target area, write a detailed prompt for the replacement content, and compare the before/after side-by-side before exporting. Ideal for product photography corrections, object removal or replacement, and creative compositing where precise control over the edited region matters.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bria_genfill.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bria_genfill.json)

## Details

| | |
|---|---|
| Name | `api_bria_genfill` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | BRIA |
| Tags | API, Inpainting |
| Type | API |
| Date | 2026-08-16 |
| Author | ComfyUI |
| Min ComfyUI version | 0.33.0 |
| Usage | 25 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | retro_girl_cinnamon_bun.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BriaGenFill` | 1 |  |
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `Painter` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Bria GenFill</summary>

# Bria GenFill Template

Use this template to **regenerate a specific region of an image** with Bria's Generative Fill API. The masked area is fully regenerated from your prompt; everything outside the mask stays pixel-perfect unchanged.

## Input Assets

- [retro_girl_cinnamon_bun.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/retro_girl_cinnamon_bun.png)

## How to use

1. **Load an image**: Upload your image in `LoadImage`. The Painter canvas and compare view auto-update.
2. **Paint a mask**: Use the `Painter` node to brush over the region you want to regenerate. Blob-shaped, brush-drawn masks work best. Tip: paint slightly beyond the object's edge (hair, glass, fabric, contact points) so the model has room to blend.
3. **Write the prompt**: In `BriaGenFill`, describe what should be generated *inside the masked area*, as if art-directing a cropped micro-scene: name the object, its material and size, how it interacts with the surface, and ask for a contact shadow. Around 90-110 words works best. Keep `refine_prompt` enabled.
4. **Optional**: `negative_prompt` to avoid unwanted details. Use a fixed `seed` to iterate on the mask or wording, then randomize once the result looks right.
5. **Compare and save**: `ImageCompare` shows before/after, `SaveImageAdvanced` exports the result.

## Notes

- Masks trigger **generative replacement**, not pixel retouching: the masked area is "regenerate this region", not "touch up this region".
- The `Painter` node is only available under **Nodes 2.0**. The canvas auto-updates when you upload a new image. If you only see "Painter: Node 2.0 only": enable Nodes 2.0 via **Menu -> Nodes2.0**, or remove the Painter node and use the [Mask Editor](https://docs.comfy.org/interface/maskeditor) to create the mask.

</details>
