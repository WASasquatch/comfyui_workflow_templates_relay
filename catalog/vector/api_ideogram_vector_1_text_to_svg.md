# Ideogram Vector 1: Text to SVG

[← Vector](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_ideogram_vector_1_text_to_svg)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_vector_1_text_to_svg-1.webp" width="360" alt="Ideogram Vector 1: Text to SVG api_ideogram_vector_1_text_to_svg-1.webp">

> Generate a fully editable SVG from a text prompt with Ideogram Vector 1, optionally guided by up to five reference images, and save it as one vector file. Ideal for logos, posters, flat illustration, patterns and line art that stays crisp at any size and opens directly in a vector editor.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_vector_1_text_to_svg.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_ideogram_vector_1_text_to_svg.json)

## Details

| | |
|---|---|
| Name | `api_ideogram_vector_1_text_to_svg` |
| Category | Foundation › Vector |
| Output | image |
| Models | Ideogram |
| Tags | API, Vector |
| Type | API |
| Date | 2026-10-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.42.5 |
| Usage | 16 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #8 | image | academic-svg.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `IdeogramVectorGenerateApi` | 1 |  |
| `LoadImage` | 1 |  |
| `SaveSVGNode` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# Ideogram Vector 1: Text to SVG

Turns a text prompt into a fully editable **SVG** you can open in any vector editor. Best for logos, posters, flat illustration, patterns and line art.

## Input Asset

- [academic-svg.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/academic-svg.png)

## Prompt tips
- Describe shapes, palette and composition rather than camera settings.
- Put lettering in quotes, e.g. `'COSTIERA AMALFITANA'`.
- `aspect_ratio` on `auto` derives the canvas from the prompt, or from image 1.

## Optional style reference
Connect up to 5 images to the `ref_image_1` ... `ref_image_5` inputs, then call them in the prompt as `@Image1`, `@Image2`, ... Image 1 is the main source.

## Notes
- The seed is fixed so the same prompt reproduces the same SVG. Set `control_after_generate` to `randomize` for variations.
- This is an API node: sign in and keep credits available ([API node overview](https://docs.comfy.org/tutorials/partner-nodes/overview)).

</details>

<details><summary>MarkdownNote</summary>

Plug a reference image into the Ideogram Vector Generate SVG node. Then you can use it for the style reference.

</details>
