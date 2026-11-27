# Qwen Image 3.0 Pro: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_qwen3_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_qwen3_t2i-1.webp" width="360" alt="Qwen Image 3.0 Pro: Text to Image api_qwen3_t2i-1.webp">

> Generate detailed, production-ready images from text prompts using the Qwen Image 3.0 Pro model, supporting up to 4.5k tokens for complex layouts like posters, infographics, and storyboards. It renders crisp 10px text, realistic textures, and native support for 12 languages and over 100 art styles, with optional 1-3 reference images for fusion editing. Ideal for marketing materials, educational diagrams, and UI design mockups.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_qwen3_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_qwen3_t2i.json)

## Details

| | |
|---|---|
| Name | `api_qwen3_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | Qwen Image 3.0 Pro |
| Tags | API, Text to Image |
| Type | API |
| Date | 2026-08-06 |
| Author | ComfyUI |
| Min ComfyUI version | 0.32.0 |
| Usage | 52 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #2 | image | api_qwen3_t2i.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 1 |  |
| `QwenImageTextToImageApi` | 1 |  |
| `ResolutionSelector` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Megapixels can be up to 6.2, or remove the `Resolution Selector` for fully customize width and height.

</details>
