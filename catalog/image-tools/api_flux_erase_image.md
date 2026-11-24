# Object Removal: Flux

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_flux_erase_image)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_flux_erase_image-1.webp" width="360" alt="Object Removal: Flux api_flux_erase_image-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_flux_erase_image-2.webp" width="360" alt="Object Removal: Flux api_flux_erase_image-2.webp">

> Upload an image and paint a mask over the object to remove. The workflow erases the masked area and reconstructs the background.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_flux_erase_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_flux_erase_image.json)

## Details

| | |
|---|---|
| Name | `api_flux_erase_image` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | FLUX |
| Tags | API, Inpainting |
| Type | API |
| Date | 2026-06-04 |
| Author | ComfyUI |
| Min ComfyUI version | 0.23.0 |
| Usage | 36 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #10 | image | city_street_young_man.png |
| output | `SaveImage` #3 | image | api_flux_erase_image.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `FluxEraseNode` | 1 |  |
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Flux Erase Image</summary>

## FLUX Erase Image (BFL API)

Removes whatever you mask and reconstructs the background behind it. No prompt is required — only an image and a binary mask.

---

### Quick start in this graph

1. **Load Image** — Click the widget, upload your photo (min **256×256**). The same node outputs **IMAGE** and **MASK**.
2. **Paint the mask** — On **Load Image**, open the mask editor (right‑click the node → [mask editor](https://docs.comfy.org/interface/maskeditor)). Paint over everything you want removed (people, text, cables, logos, shadows you want gone).
   - Alternative: use a separate black/white mask via **Load Image (as Mask)**, then wire that into **Flux Erase Image**.
   - Convention matches the API: **white = erase**, **black = keep**. Mask is auto-resized to match the image.
3. **Flux Erase Image** — `dilate_pixels` (default **10**, range **0–25**) expands the mask slightly so edges, hair, and soft boundaries are fully covered. Increase to **15–20** for fuzzy edges; lower if you are erasing near important detail.
4. **Queue Prompt** 
5. **Save Image** 
---

### Mask tips

- Cover the **whole** object plus any shadow/reflection you want removed; a tight mask often leaves a halo — raise `dilate_pixels`.
- Best quality is near **~1 MP** and aspect ratios between **1:2** and **2:1** (per BFL guidance); very unusual sizes may look worse.

</details>
