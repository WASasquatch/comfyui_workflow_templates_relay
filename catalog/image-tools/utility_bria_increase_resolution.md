# Image Upscale: Bria Increase Resolution

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_bria_increase_resolution)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_bria_increase_resolution-1.webp" width="360" alt="Image Upscale: Bria Increase Resolution utility_bria_increase_resolution-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_bria_increase_resolution-2.webp" width="360" alt="Image Upscale: Bria Increase Resolution utility_bria_increase_resolution-2.webp">

> Upscale any image to higher resolutions using Bria's dedicated resolution enhancement API, which preserves original content without adding new details or regenerating the image. The workflow accepts a single input image and produces one enhanced, higher-resolution output, supporting JPEG and PNG files in RGB, RGBA, or CMYK color modes up to a maximum area of 8192x8192 pixels. Built-in content moderation scans both the input image and generated output to ensure safe, policy-compliant processing. Ideal for preparing images for print, enlarging photos for digital display, or increasing resolution of assets for professional design work.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_bria_increase_resolution.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_bria_increase_resolution.json)

## Details

| | |
|---|---|
| Name | `utility_bria_increase_resolution` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | BRIA |
| Tags | API, Image Upscale |
| Type | API |
| Date | 2026-09-02 |
| Author | ComfyUI |
| Min ComfyUI version | 0.34.0 |
| Usage | 28 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2 | image | orange_suit_golden_pour.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BriaIncreaseResolution` | 1 |  |
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
