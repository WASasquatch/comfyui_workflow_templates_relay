# Runway: Reference to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_runway_reference_to_image)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_runway_reference_to_image-1.webp" width="360" alt="Runway: Reference to Image api_runway_reference_to_image-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_runway_reference_to_image-2.webp" width="360" alt="Runway: Reference to Image api_runway_reference_to_image-2.webp">

> Generate new images based on reference styles and compositions with Runway's AI.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_runway_reference_to_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_runway_reference_to_image.json)

## Details

| | |
|---|---|
| Name | `api_runway_reference_to_image` |
| Category | Foundation › Image |
| Output | image |
| Models | Runway |
| Tags | Image, API, Style Reference |
| Type | API |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.3.37 |
| Usage | 15 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #5 | image | api_runway_reference_to_image_input_image.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `LoadImage` | 1 | comfy-core |
| `RunwayTextToImageNode` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

`Runway Text to Image` Node only support one image input.

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
