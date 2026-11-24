# Grok Imagine Image 2.0: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_grok_imagine_image_2_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_image_2_image_edit-1.webp" width="360" alt="Grok Imagine Image 2.0: Image Edit api_grok_imagine_image_2_image_edit-1.webp">

> Grok Imagine Image 2.0 performs precise image editing and text rendering using xAI's Aurora engine, letting you modify specific elements, swap backgrounds, or restyle scenes through natural language with crisp short-text output. It takes up to 3 reference images and generates at 1K or 2K resolution across 14 aspect ratios, with strong character consistency across scenes. Ideal for poster and cover design, product and brand visuals, or multi-scene character workflows.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_grok_imagine_image_2_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_grok_imagine_image_2_image_edit.json)

## Details

| | |
|---|---|
| Name | `api_grok_imagine_image_2_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | Grok Imagine Image 2.0 |
| Tags | API, Image Edit |
| Type | API |
| Date | 2026-08-13 |
| Author | ComfyUI |
| Min ComfyUI version | 0.32.0 |
| Usage | 648 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #11 | image | model_blue_outfit.png |
| input | `LoadImage` #13 | image | pink_lipstick.png |
| output | `SaveImage` #12 | image | api_grok_imagine_image_2_image_edit.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `GrokImageEditNodeV2` | 1 |  |
| `SaveImage` | 1 |  |
