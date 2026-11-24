# Recraft: Color Control Image Generation

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_recraft_image_gen_with_color_control)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_image_gen_with_color_control-1.webp" width="360" alt="Recraft: Color Control Image Generation api_recraft_image_gen_with_color_control-1.webp">

> Generate images with custom color palettes and brand-specific visuals using Recraft.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_recraft_image_gen_with_color_control.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_recraft_image_gen_with_color_control.json)

## Details

| | |
|---|---|
| Name | `api_recraft_image_gen_with_color_control` |
| Category | Foundation › Image |
| Output | image |
| Models | Recraft |
| Tags | Text to Image, Image, API |
| Type | API |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.3.34 |
| Usage | 15 |
| Nodes | 13 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `RecraftColorRGB` | 3 | comfy-core |
| `MarkdownNote` | 2 |  |
| `RecraftControls` | 1 | comfy-core |
| `RecraftStyleV3DigitalIllustration` | 1 | comfy-core |
| `RecraftStyleV3LogoRaster` | 1 | comfy-core |
| `RecraftStyleV3RealisticImage` | 1 | comfy-core |
| `RecraftTextToImageNode` | 1 | comfy-core |
| `RecraftVectorizeImageNode` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `SaveSVGNode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>About Recraft Text to Image</summary>

[Tutorial](https://docs.comfy.org/tutorials/partner-nodes/recraft/recraft-text-to-image)

1 - Different "Recraft Styles" can quickly set different output styles.

2 - "seed" is only used to determine whether a node should be re - run, but the actual result has nothing to do with the seed.

</details>

<details><summary>About API Node</summary>

[About API Node](https://docs.comfy.org/tutorials/partner-nodes/overview) 

To use the API, you must be in a secure network environment:

- Allows access from `127.0.0.1` or `localhost`.

- Use our API Node in website services starting with `https`

- Make sure you can normally connect to our API services (some regions may need a proxy).

- Make sure you are logged in in the settings and that your account still has enough credits to cover the consumption of API calls.

- On non-whitelisted sites or local area networks (LANs), please try to [log in using an API Key](https://docs.comfy.org/interface/user#logging-in-with-an-api-key).

</details>
