# Patina: Material Extract

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_patina_material_extract-1.webp" width="360" alt="Patina: Material Extract api_patina_material_extract-1.webp">

> Pull a seamless, tiling PBR material out of a photo of a surface with Patina. The prompt says which surface to extract and which structure to keep, and the base texture comes back with basecolor, normal, roughness, metalness and height maps aligned pixel for pixel. Made for photos that already contain the material you want: brick walls, paving, plaster, fabric.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_patina_material_extract.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_patina_material_extract.json)

## Details

| | |
|---|---|
| Name | `api_patina_material_extract` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Patina |
| Tags | 3D, API |
| Type | API |
| Date | 2026-10-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.43.1 |
| Usage | 0 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #30 | image | patina_chair_webbing.png |
| output | `SaveImage` #23 | image | api_patina_material_extract.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveImage` | 6 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PatinaMaterialExtractNode` | 1 |  |
| `SaveText` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# Patina Material Extract

**Photo -> seamless, tiling PBR material, extracted.** Point it at a photo that already contains the material you want
and the prompt says which surface to pull out and what structure to keep. The base texture and the basecolor / normal /
roughness / metalness / height maps all come from the same latent, so they line up pixel for pixel. Partner (API) node:
it runs on Comfy's servers, needs an account, nothing renders locally.

## Input Asset

- [patina_chair_webbing.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/patina_chair_webbing.png)

## How to use it

- **Load Image** holds the photo. It does not have to be a flat crop: the node re-synthesises the layout, so a product
  shot works as long as the material itself repeats - here the green and white webbing on a folding chair.
- `prompt` names the surface to extract, not the scene: `chair webbing fabric` picks the woven straps and ignores the
  chair frame, the court and the paddle. Add the structure to keep ("keep the weave and the strap edges") when the
  pattern starts drifting.
- `strength` (advanced, 0.6 here) sets how far the extracted texture may drift from the photo.
- Works best on materials whose pattern repeats inside a few hundred pixels - webbing, brick, pavers, planks, plaster.
  Large one-off structures (a rock cliff, aerial terrain, a single object) come back as a repaint that will not tile.
- For text-only material generation use the Patina Material text-to-material template; to convert a photo into maps
  **without** making it tile, the Patina PBR Maps node is the direct path.

## Outputs - wire in this slot order

`0 texture` . `1 basecolor` . `2 normal` . `3 roughness` . `4 metalness` . `5 height` . `6 expanded_prompt`

Every map can be switched off, but at least one has to stay on. Fewer maps = a cheaper, faster run.

## Tips that actually matter

- Keep the photo bigger than the output size where you can - the model has more real detail to extract from.
- `num_inference_steps` tops out at 8; there is nothing to gain above that.
- `tile_size` is in latent space: 128 is about 1024 px, 64 about 512 px. `tiling_mode` = both / horizontal / vertical.
- `prompt_expansion` is **off by default on purpose**: the LLM rewrite reframes the prompt as a photo and tends to
  wash out the metalness map.
- `upscale_factor` 2 or 4 upscales the **maps only** (SeedVR) - the base texture is never upscaled.
- Dramatic lighting in the source carries into the basecolor: prefer flat, evenly lit photos.

</details>
