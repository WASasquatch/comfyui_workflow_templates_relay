# Patina: Text to Material

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_patina_material_t2m-1.webp" width="360" alt="Patina: Text to Material api_patina_material_t2m-1.webp">

> Generate a complete, seamlessly tiling PBR material from a text prompt with Patina. One run returns a base texture plus basecolor, normal, roughness, metalness and height maps that line up pixel for pixel, so the whole set drops straight into a 3D material. Works best on structured surfaces such as wood, stone, metal, fabric and ceramic tile; connect an image, optionally with a mask, to repaint an existing surface instead of inventing one.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_patina_material_t2m.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_patina_material_t2m.json)

## Details

| | |
|---|---|
| Name | `api_patina_material_t2m` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Patina |
| Tags | 3D, API |
| Type | API |
| Date | 2026-10-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.43.1 |
| Usage | 18 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #23 | image | api_patina_material_t2m.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveImage` | 6 |  |
| `MarkdownNote` | 1 |  |
| `PatinaMaterialNode` | 1 |  |
| `SaveText` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# Patina Material

**Text -> complete, seamlessly tiling PBR material.** One prompt returns a base texture plus
basecolor / normal / roughness / metalness / height maps, all generated from the same latent so they line up
pixel for pixel. This is a partner (API) node: it runs on Comfy's servers, needs an account, nothing renders locally.

## Three ways to use it

| mode | wiring | behaviour |
|---|---|---|
| text -> material | only `prompt` | invents a tileable material from the description |
| image-to-image | `prompt` + `image` | keeps the photo's structure and redraws it toward the prompt; `strength` 0.01-1 sets how far it moves |
| inpaint | `prompt` + `image` + `mask` | white = regenerate, black = keep; a mask without an image raises an error |

## Outputs - wire in this slot order

`0 texture` · `1 basecolor` · `2 normal` · `3 roughness` · `4 metalness` · `5 height` · `6 expanded_prompt`

Every map can be switched off, but at least one has to stay on. Fewer maps = a cheaper, faster run.

## Tips that actually matter

- `image_size`: presets 1024², 512², 4:3, 3:4, 16:9, 9:16, or `custom` (512-2048, step 16).
- `num_inference_steps` tops out at 8 - there is nothing to gain above that.
- `tile_size` is in latent space: 128 is about 1024 px, 64 about 512 px. `tiling_mode` = both / horizontal / vertical.
- `prompt_expansion` is **off by default on purpose**: the LLM rewrite reframes the prompt as a photo and tends to
  wash out the metalness map. Turn it on only when you want more surface detail and do not need a metalness map.
- `upscale_factor` 2 or 4 upscales the **maps only** (SeedVR) - the base texture is never upscaled.
- Describe a surface, not a scene. Add "flat even lighting, no perspective" and name the pattern
  ("running bond", "herringbone", "warp and weft") - that is what makes the result tile.
- Structured materials work best: wood, stone, metal, fabric, ceramic tile, concrete, leather.
  Avoid free-form marble, flat gradients, and anything that depends on readable text - the texture generator will
  happily invent plausible-looking nonsense.

## This workflow

Brick example, all five maps on. Every save node writes to `patina/<yyyymmdd>-<hhmm>_<map>`, so the files of one run
sit next to each other in the output folder and runs from different days never mix.

</details>
