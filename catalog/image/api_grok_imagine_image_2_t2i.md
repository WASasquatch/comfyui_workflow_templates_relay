# Grok Imagine Image 2.0: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_image_2_t2i-1.webp" width="360" alt="Grok Imagine Image 2.0: Text to Image api_grok_imagine_image_2_t2i-1.webp">

> Generate images from text prompts using Grok Imagine Image 2.0, an Aurora-engine model that excels at crisp short-text rendering and 1K or 2K outputs across 14 aspect ratios. Enter one text prompt and receive one generated image, with low or medium quality options to control cost. Ideal for poster and cover design, product and brand visuals, and character-driven scenes where consistency matters.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_image_2_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_grok_imagine_image_2_t2i.json)

## Details

| | |
|---|---|
| Name | `api_grok_imagine_image_2_t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | Grok Imagine Image 2.0 |
| Tags | API, Text to Image |
| Type | API |
| Date | 2026-08-13 |
| Author | ComfyUI |
| Min ComfyUI version | 0.32.0 |
| Usage | 199 |
| Nodes | 2 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImageAdvanced` #2 | image | api_grok_imagine_image_2_t2i.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GrokImageNode` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
