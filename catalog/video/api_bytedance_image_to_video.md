# Seedance 1.0 Pro: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_bytedance_image_to_video)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_image_to_video-1.webp" width="360" alt="Seedance 1.0 Pro: Image to Video api_bytedance_image_to_video-1.webp">

> Transform static images into dynamic videos using ByteDance's Seedance model. Analyzes image structure and generates natural motion with consistent visual style and coherent video sequences.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_bytedance_image_to_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_bytedance_image_to_video.json)

## Details

| | |
|---|---|
| Name | `api_bytedance_image_to_video` |
| Category | Foundation › Video |
| Output | video |
| Models | Seedance1.0 Pro, ByteDance |
| Tags | API, Image to Video, Video |
| Type | API |
| Date | 2025-10-06 |
| Author | ComfyUI |
| Min ComfyUI version | 0.3.58 |
| Usage | 642 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #12 | image | api_bytedance_image_to_video_input_image.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ByteDanceImageToVideoNode` | 1 |  |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 | comfy-core |

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
