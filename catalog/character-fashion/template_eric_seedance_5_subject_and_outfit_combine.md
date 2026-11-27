# Outfit Application for Character Portraits

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_eric_seedance_5_subject_and_outfit_combine)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_eric_seedance_5_subject_and_outfit_combine-1.webp" width="360" alt="Outfit Application for Character Portraits template_eric_seedance_5_subject_and_outfit_combine-1.webp">

> Upload your character portrait and outfit reference. Generate a new portrait with the specific outfit applied for consistent wardrobe control. Affordable alternative to Nano Banana Pro and Nano Banana 2.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_eric_seedance_5_subject_and_outfit_combine.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_eric_seedance_5_subject_and_outfit_combine.json)

## Details

| | |
|---|---|
| Name | `template_eric_seedance_5_subject_and_outfit_combine` |
| Category | Applied › Character & Fashion |
| Output | image |
| Models | Seedream 4.5 |
| Tags | API, Virtual Try-On |
| Type | API |
| Date | 2026-03-08 |
| Author | enigmatic_e |
| Min ComfyUI version | 0.34.0 |
| Usage | 25 |
| Nodes | 15 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #16 | image | subject_far.png |
| input | `LoadImage` #26 | image | clothing.png |
| input | `LoadImage` #226 | image | subject_close.png |
| output | `SaveImage` #11 | image | template_eric_seedance_5_subject_and_outfit_combine-2.png |
| output | `SaveImage` #258 | image | template_eric_seedance_5_subject_and_outfit_combine-1.png |

## Subgraphs

- **Batch Images** (4 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 3 | comfy-core |
| `ByteDanceSeedreamNodeV3` | 2 |  |
| `PrimitiveStringMultiline` | 2 | comfy-core |
| `RegexReplace` | 2 | comfy-core |
| `ResizeAndPadImage` | 2 | comfy-core |
| `SaveImage` | 2 | comfy-core |
| `BatchImagesNode` | 1 |  |
| `GetImageSize` | 1 | comfy-core |
