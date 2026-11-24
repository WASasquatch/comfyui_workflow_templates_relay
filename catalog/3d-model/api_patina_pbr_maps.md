# Patina: PBR Maps

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_patina_pbr_maps-1.webp" width="360" alt="Patina: PBR Maps api_patina_pbr_maps-1.webp">

> Turn one image into a set of PBR maps with Patina: basecolor, normal, roughness, metalness and height, all derived from exactly what the picture contains. No regeneration and no tiling - feed a flat, evenly lit surface photo or an existing basecolor map, pick the maps you need and drop them straight into a 3D material.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_patina_pbr_maps.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_patina_pbr_maps.json)

## Details

| | |
|---|---|
| Name | `api_patina_pbr_maps` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | Patina |
| Tags | API, 3D |
| Type | API |
| Date | 2026-10-28 |
| Author | ComfyUI |
| Min ComfyUI version | 0.43.1 |
| Usage | 0 |
| Nodes | 8 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #30 | image | patina_pbr_webbing_basecolor.png |
| output | `SaveImage` #23 | image | api_patina_pbr_maps.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveImage` | 5 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PatinaPBRMapsNode` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# Patina PBR Maps

**Photo or texture -> PBR maps.** Converts one image into basecolor / normal / roughness / metalness / height. Nothing
is regenerated: the maps are derived from exactly what the picture contains, so seams, perspective and lighting in the
source stay in the result. Partner (API) node: it runs on Comfy's servers, needs an account, nothing renders locally.

## Input Asset

- [patina_pbr_webbing_basecolor.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/patina_pbr_webbing_basecolor.png)

## How to use it

- Feed a flat, evenly lit surface photo, or an existing basecolor map - this example takes the green / white webbing
  basecolor produced by the Patina Material Extract template, so the chain reads extract -> PBR maps.
- Switch on only the maps you need. Every enabled map is billed, and three maps are usually enough for a game or a
  product material.
- **This node does not tile.** If the source is not seamless, the maps will not be either: use Patina Material
  (Extract) when the result has to repeat, and this node when you already have a tiling basecolor and want the rest of
  the set.
- Inputs up to 2048 px; larger images are scaled down automatically (`auto_downscale`, on by default).

## Outputs - wire in this slot order

`0 basecolor` . `1 normal` . `2 roughness` . `3 metalness` . `4 height`

## Tips that actually matter

- The maps come back at the **input resolution**, not at a fixed size.
- Metalness on non-metal surfaces comes back solid black - that is correct, not a failed download.
- Roughness tends to read darker (smoother) than the photo suggests; check it against the source before shipping.
- Strong directional light in the source is baked into the basecolor, which double-lights the material in 3D. Prefer
  flat, diffuse photos.

</details>
