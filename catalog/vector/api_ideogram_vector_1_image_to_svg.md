# Ideogram Vector 1: Image to SVG

[← Vector](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_vector_1_image_to_svg-1.webp" width="360" alt="Ideogram Vector 1: Image to SVG api_ideogram_vector_1_image_to_svg-1.webp">

> Trace a bitmap into a fully editable SVG with Ideogram Vector 1 and save it as one vector file. Ideal for turning logos, flat illustration, patterns and line art into clean paths that stay crisp at any size, with a detail mode that either keeps large flat color blocks or finer color regions. Photographs also work, but convert into many small paths, so clean sources with large areas of flat color and transparent backgrounds vectorize best.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_ideogram_vector_1_image_to_svg.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_ideogram_vector_1_image_to_svg.json)

## Details

| | |
|---|---|
| Name | `api_ideogram_vector_1_image_to_svg` |
| Category | Foundation › Vector |
| Media type | image |
| Models | Ideogram |
| Tags | API, Vector |
| Type | API |
| Date | 2026-10-22 |
| Author | ComfyUI |
| Min ComfyUI version | 0.42.5 |
| Usage | 64 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #4 | image | kid_onknight_dragon.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `IdeogramVectorImageToSVGApi` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveSVGNode` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# Ideogram Vector 1: Image to SVG

Traces a bitmap into a fully editable **SVG** you can open in any vector editor. Best for logos, flat illustration, patterns and line art. Photographs work too, but a photo turns into thousands of tiny paths, so the file gets heavy and hard to edit by hand.

## Input Asset

- [kid_onknight_dragon.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/kid_onknight_dragon.png)

## Source image
- Start from a clean image with large areas of flat color and clear edges. The vectorizer follows what it sees, including grain, gradients and background clutter.
- Transparent areas keep their alpha, so a cut-out PNG stays cut out.

## Detail control
- `mode` = `simple` outlines fewer, larger color blocks, which gives a lighter and flatter SVG.
- `mode` = `default` keeps finer detail and more color blocks, so the result stays closer to the source.

## Output
The node emits an SVG rather than a raster image: connect it to **Save SVG** to write a `.svg` file to disk.

## Notes
- This is an API node: sign in and keep credits available ([API node overview](https://docs.comfy.org/tutorials/partner-nodes/overview)).

</details>
