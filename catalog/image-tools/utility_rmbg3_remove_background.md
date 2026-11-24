# Remove Background: RMBG 3.0

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_rmbg3_remove_background-1.webp" width="360" alt="Remove Background: RMBG 3.0 utility_rmbg3_remove_background-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_rmbg3_remove_background-2.webp" width="360" alt="Remove Background: RMBG 3.0 utility_rmbg3_remove_background-2.webp">

> RMBG 3.0 renders a soft grayscale alpha matte instead of a hard mask, so hair, glass, veils and liquid keep real transparency. A vision model writes the matting instruction from your image; add one sentence about the material to refine it.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_rmbg3_remove_background.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_rmbg3_remove_background.json)

## Details

| | |
|---|---|
| Name | `utility_rmbg3_remove_background` |
| Category | Foundation › Image Tools |
| Media type | image |
| Models | RMBG 3.0 |
| Tags | Remove Background |
| Type | open source |
| Date | 2026-11-21 |
| Author | ComfyUI |
| Download size | 12.7 GB |
| Min ComfyUI version | 0.46.0 |
| Usage | 0 |
| Nodes | 30 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #10 | image | withered_hydrangeas_still_life_vintage_lit.png |
| output | `SaveImage` #171 | image | utility_rmbg3_remove_background.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `rmbg3_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/briaai/RMBG-3.0-Comfy/resolve/main/diffusion_models/rmbg3_int8_convrot.safetensors) |
| `qwen3vl_4b_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/briaai/RMBG-3.0-Comfy/resolve/main/text_encoders/qwen3vl_4b_int8_convrot.safetensors) |
| `flux2-vae.safetensors` | `vae` | [link](https://huggingface.co/briaai/RMBG-3.0-Comfy/resolve/main/vae/flux2-vae.safetensors) |

## Subgraphs

- **Remove Background (RMBG 3.0)** (23 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveStringMultiline` | 3 |  |
| `CLIPLoader` | 2 |  |
| `ComfySwitchNode` | 2 |  |
| `JoinImageWithAlpha` | 2 |  |
| `MarkdownNote` | 2 |  |
| `SaveImage` | 2 |  |
| `AdjustBrightness` | 1 |  |
| `AdjustContrast` | 1 |  |
| `GrowMask` | 1 |  |
| `ImageCompare` | 1 |  |
| `ImageToMask` | 1 |  |
| `InvertMask` | 1 |  |
| `KSampler` | 1 |  |
| `LoadImage` | 1 |  |
| `MaskPreview` | 1 |  |
| `PreviewAny` | 1 |  |
| `StringFormat` | 1 |  |
| `TextEncodeFibo2` | 1 |  |
| `TextGenerateV2` | 1 |  |
| `ThresholdMask` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: RMBG 3.0</summary>

## Remove Background: RMBG 3.0

RMBG 3.0 renders a soft grayscale alpha matte instead of a hard mask, so hair, glass, veils and liquid keep real transparency.

### Outputs

- `foreground_image` — RGBA cutout at the source resolution
- `background_image` — the source with the subject removed
- `mask` — the raw matte

### How to use

- Drop a photo into `source_image`
- Keep `auto_prompt` ON: a vision model writes the matting instruction from the image
- Add `subject_note` (optional) to describe the material
- Keep `cfg` at **1.0**; raise it only for see-through subjects (see below)
- Subgraph guide: [docs.comfy.org › Subgraph](https://docs.comfy.org/interface/features/subgraph)

### Writing `subject_note`

- One short sentence about the material, not about the scene or lighting
- Name what stays solid: paper, metal, skin, petals, fabric
- Name what stays see-through: glass, liquid, veil, mesh, smoke
- Example: `Clear glass bottle, paper label, metal cap`

### Tuning

- Glass or veil comes back solid white → describe it in `subject_note`, then raise `cfg` to **1.5–2.0**
- Coloured glass often stays opaque → lower `alpha_brightness`, or paint that area by hand
- Faint grey noise in the background → lower `alpha_brightness`, or enable `hard_mask`
- `cfg` 1.0 is the official setting: RMBG 3.0 is distilled without classifier-free guidance, so a higher cfg trades source fidelity for transparency

</details>

<details><summary>Note: Model links</summary>

## Input Asset

- [withered_hydrangeas_still_life_vintage_lit.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/withered_hydrangeas_still_life_vintage_lit.png)

## Model Links

- [Hugging Face:briaai/RMBG-3.0-Comfy](https://huggingface.co/briaai/RMBG-3.0-Comfy)

**diffusion_models**

- [rmbg3_int8_convrot.safetensors](https://huggingface.co/briaai/RMBG-3.0-Comfy/resolve/main/diffusion_models/rmbg3_int8_convrot.safetensors) (7.83 GB)

**text_encoders**

- [qwen3vl_4b_int8_convrot.safetensors](https://huggingface.co/briaai/RMBG-3.0-Comfy/resolve/main/text_encoders/qwen3vl_4b_int8_convrot.safetensors) (4.52 GB)

**vae**

- [flux2-vae.safetensors](https://huggingface.co/briaai/RMBG-3.0-Comfy/resolve/main/vae/flux2-vae.safetensors) (320.6 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── rmbg3_int8_convrot.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen3vl_4b_int8_convrot.safetensors
│   └── 📂 vae/
│       └── flux2-vae.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
