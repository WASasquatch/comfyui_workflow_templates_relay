# Wan2.5: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_wan_text_to_image)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan_text_to_image-1.webp" width="360" alt="Wan2.5: Text to Image api_wan_text_to_image-1.webp">

> Generate images with excellent prompt following and visual quality using Wan 2.5.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan_text_to_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_wan_text_to_image.json)

## Details

| | |
|---|---|
| Name | `api_wan_text_to_image` |
| Category | Foundation › Image |
| Output | image |
| Models | Wan2.5, Wan |
| Tags | Text to Image, Image, API |
| Type | API |
| Date | 2025-09-25 |
| Author | ComfyUI |
| Min ComfyUI version | 0.3.60 |
| Usage | 32 |
| Nodes | 3 |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `WanTextToImageApi` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note：About API Node</summary>

[About API Node](https://docs.comfy.org/tutorials/partner-nodes/overview) - [Pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing) | [API 节点](https://docs.comfy.org/zh-CN/tutorials/partner-nodes/overview) - [定价](https://docs.comfy.org/zh-CN/tutorials/partner-nodes/pricing)
 
To use the API, you must be in a secure network environment:

- Allows access from `127.0.0.1` or `localhost`.

- Use our API Node in website services starting with `https`

- Make sure you can normally connect to our API services (some regions may need a proxy).

- Make sure you are logged in in the settings and that your account still has enough credits to cover the consumption of API calls.

- On non-whitelisted sites or local area networks (LANs), please try to [log in using an API Key](https://docs.comfy.org/interface/user#logging-in-with-an-api-key).

</details>
