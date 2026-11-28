# Flux.1 [Pro]: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bfl_flux_pro_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux_pro_t2i-1.webp" width="360" alt="Flux.1 [Pro]: Text to Image api_bfl_flux_pro_t2i-1.webp">

> Generate images with excellent prompt following and visual quality using FLUX.1 Pro.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bfl_flux_pro_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bfl_flux_pro_t2i.json)
- [Tutorial](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-1-1-pro-ultra-image)

## Details

| | |
|---|---|
| Name | `api_bfl_flux_pro_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX, FLUX.1 |
| Tags | API, Image, Image Edit |
| Type | API |
| Date | 2025-05-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.3.32 |
| Usage | 13 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #14 | image | example.png |
| output | `SaveImage` #12 | image | api_bfl_flux_pro_t2i.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `FluxProUltraImageNode` | 1 |  |
| `LoadImage` | 1 |  |
| `SaveImage` | 1 |  |

## Notes embedded in the workflow

<details><summary>Flux 1.1 [pro] Ultra Image</summary>

[Tutorial](https://docs.comfy.org/tutorials/partner-nodes/black-forest-labs/flux-1-1-pro-ultra-image) 

### `image_prompt` is optional.
When `image_prompt` is input, the larger the value of `image_prompt_strength`, the closer the output result is to the input image.

### `raw` determines whether it is Ultra mode or raw format.
- **Ultra mode**: Specifically designed for high-resolution requirements, it can accurately restore the prompt and maintain the generation speed.
- **Raw mode**: Focuses on natural realism, optimizes details such as human skin color, light and shadow, and natural landscapes, making the results more realistic and less AI - like.

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

<details><summary>How to enable image_prompt</summary>

Right-click on the Load image node, set the mode to **always** to enable **image_prompt**

</details>
