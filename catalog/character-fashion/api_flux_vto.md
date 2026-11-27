# Virtual Try-On: Flux

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_flux_vto)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_flux_vto-1.webp" width="360" alt="Virtual Try-On: Flux api_flux_vto-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_flux_vto-2.webp" width="360" alt="Virtual Try-On: Flux api_flux_vto-2.webp">

> Upload a person photo and a garment image. Generate a virtual try-on result with the garment applied to the person while preserving face and pose.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_flux_vto.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_flux_vto.json)

## Details

| | |
|---|---|
| Name | `api_flux_vto` |
| Category | Applied › Character & Fashion |
| Output | image |
| Models | FLUX |
| Tags | API, Virtual Try-On |
| Type | API |
| Date | 2026-06-04 |
| Author | ComfyUI |
| Min ComfyUI version | 0.23.0 |
| Usage | 17 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | portrait_floral_headshot.png |
| input | `LoadImage` #5 | image | green_chiffon_short_dress.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `FluxVTONode` | 1 |  |
| `ImageCompare` | 1 |  |
| `ImageStitch` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Flux Virtual Try-On</summary>

## FLUX Virtual Try-On

Puts the clothing from your **garment** photo onto the **person** photo. Face and pose stay from the person image.

### Quick start

- **Load Image (top)** — **Person**: who will wear the clothes. Use a clear photo with the body/clothing area visible.
- **Load Image (bottom)** — **Garment**: the clothes to apply (product shot, flat lay, or one combined image).

Upload both, adjust **prompt** on **Flux Virtual Try-On** if needed, then **Queue Prompt**. Use **Compare Images** to check before/after; **Save Image** writes the result.

### Prompt

Describe the garment and how it should be worn — not the person or background.

Example:
`Dress the person in the reference garment. Match color, pattern, and fit. Keep face and pose unchanged.`

Optional: `upper body only`, `tucked in`, `preserve the logo on the chest`.

### Several garment images

Only one image goes into **garment**. Use **Stitch Images** to join separate pieces (e.g. jacket + pants) side by side or stacked, then connect that output to **garment**. Name each piece in the prompt.

</details>
