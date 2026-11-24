# Patina: Image to Material

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_patina_material_i2m-1.webp" width="360" alt="Patina: Image to Material api_patina_material_i2m-1.webp">

> Turn a photo of a surface into a seamless, tiling PBR material with Patina. The source image sets the pattern and Patina redraws it as a tileable material, returning basecolor, normal, roughness, metalness and height maps that line up pixel for pixel. Built for brick, stone, wood, plaster, fabric and ceramic tile; a mask can restrict the redraw to part of the image.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_patina_material_i2m.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_patina_material_i2m.json)

## Details

| | |
|---|---|
| Name | `api_patina_material_i2m` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Patina |
| Tags | API, 3D |
| Type | API |
| Date | 2026-10-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.43.1 |
| Usage | 31 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #30 | image | patina_brick_wall.jpg |
| output | `SaveImage` #23 | image | api_patina_material_i2m.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveImage` | 6 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PatinaMaterialNode` | 1 |  |
| `SaveText` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# Patina Material

**Photo -> complete, seamlessly tiling PBR material.** The source image sets the pattern; Patina redraws it as a
tiling material and returns basecolor / normal / roughness / metalness / height maps from the same latent, so the whole
set lines up pixel for pixel. Partner (API) node: it runs on Comfy's servers, needs an account, nothing renders locally.

## Input Asset

- [patina_brick_wall.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/patina_brick_wall.jpg)

## How to use it

- **Load Image** holds the surface photo. Anything with a regular structure works: brick, stone, wood, plaster, fabric, tile.
- `prompt` describes the material you want back, not the scene. Name the pattern and the finish, and add
  "flat even lighting, no perspective" - that is what makes the result tile.
- `strength` (advanced, 0.6 here) sets how far it moves away from the photo: low keeps the original texture, high
  rewrites more of it.
- The optional **mask** input inpaints a region (white = regenerate, black = keep). A mask without an image raises an error.
- Want a texture from text alone, with no source photo? Use the Patina Material text-to-material template instead.
  Want the maps of a photo without making it tile? The Patina PBR Maps node is the direct converter.

## Outputs - wire in this slot order

`0 texture` . `1 basecolor` . `2 normal` . `3 roughness` . `4 metalness` . `5 height` . `6 expanded_prompt`

Every map can be switched off, but at least one has to stay on. Fewer maps = a cheaper, faster run.

## Tips that actually matter

- `image_size`: presets 1024², 512², 4:3, 3:4, 16:9, 9:16, or `custom` (512-2048, step 16).
- `num_inference_steps` tops out at 8 - there is nothing to gain above that.
- `tile_size` is in latent space: 128 is about 1024 px, 64 about 512 px. `tiling_mode` = both / horizontal / vertical.
- `prompt_expansion` is **off by default on purpose**: the LLM rewrite reframes the prompt as a photo and tends to wash
  out the metalness map.
- `upscale_factor` 2 or 4 upscales the **maps only** (SeedVR) - the base texture is never upscaled.
- Structured materials work best. Free-form marble, flat gradients and anything relying on readable text come back as
  plausible-looking nonsense.

## This workflow

Brick wall photo, basecolor and normal maps on. Every save node writes to `patina/<yyyymmdd>-<hhmm>_<map>`, so one run's
files sit next to each other in the output folder and runs from different days never mix.

</details>
