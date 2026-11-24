# Luma Photon: Style Reference

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_luma_photon_style_ref)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_luma_photon_style_ref-1.webp" width="360" alt="Luma Photon: Style Reference api_luma_photon_style_ref-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_luma_photon_style_ref-2.webp" width="360" alt="Luma Photon: Style Reference api_luma_photon_style_ref-2.webp">

> Generate images by blending style references with precise control using Luma Photon.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_luma_photon_style_ref.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_luma_photon_style_ref.json)

## Details

| | |
|---|---|
| Name | `api_luma_photon_style_ref` |
| Category | Foundation › Image |
| Output | image |
| Models | Luma |
| Tags | API, Image, Text to Image |
| Type | API |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.8.0 |
| Usage | 9 |
| Nodes | 17 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #26 | image | api_luma_photon_i2i_ref_image_1.png |
| input | `LoadImage` #52 | image | api_luma_photon_i2i_ref_image_2.png |
| output | `SaveImage` #32 | image | api_luma_photon_style_ref.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 7 | comfy-core |
| `LumaReferenceNode` | 4 | comfy-core |
| `MarkdownNote` | 3 |  |
| `BatchImagesNode` | 1 |  |
| `LumaImageNode` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>About API Node</summary>

[About API Node](https://docs.comfy.org/tutorials/partner-nodes/overview) 

To use the API, you must be in a secure network environment:

- Allows access from `127.0.0.1` or `localhost`.

- Use our API Node in website services starting with `https`

- Make sure you can normally connect to our API services (some regions may need a proxy).

- Make sure you are logged in in the settings and that your account still has enough credits to cover the consumption of API calls.

- On non-whitelisted sites or local area networks (LANs), please try to [log in using an API Key](https://docs.comfy.org/interface/user#logging-in-with-an-api-key).

</details>

<details><summary>How to enable input images</summary>

You can right - click on the corresponding node group to set the "mode" to "always" to enable the corresponding image output.

</details>

<details><summary>About Luma Image to Image</summary>

[Tutorial](https://docs.comfy.org/tutorials/partner-nodes/luma/luma-text-to-image) 

1 - "image_luma_ref" and "character_image" support a maximum of 4 reference image inputs.

2 - The larger the "style_image_weight", the more obvious the style.

3 - You can right - click on the corresponding node group to set the "mode" to "always" to enable the corresponding image output.

4 - "Batch Images" requires both inputs to exist simultaneously. By mixing "load image" and "Batch Images", combinations with different numbers of input images can be achieved.

</details>
