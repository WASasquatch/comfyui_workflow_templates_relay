# Vidu Q1: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_image_to_video-1.webp" width="360" alt="Vidu Q1: Image to Video api_vidu_image_to_video-1.webp">

> Transform static images into dynamic 1080p videos with precise motion control and customizable movement amplitude using Vidu.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_vidu_image_to_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_vidu_image_to_video.json)

## Details

| | |
|---|---|
| Name | `api_vidu_image_to_video` |
| Category | Foundation › Video |
| Media type | image |
| Models | Vidu Q1, Vidu |
| Tags | Image to Video, Video, API |
| Type | API |
| Date | 2025-08-23 |
| Author | ComfyUI |
| Min ComfyUI version | 0.3.51 |
| Usage | 14 |
| Nodes | 4 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #22 | image | api_vidu_image_to_video_input_image.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
| `ViduImageToVideoNode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: About API Node</summary>

[About API Node](https://docs.comfy.org/tutorials/partner-nodes/overview)

To use the API, you must be in a secure network environment:

- Allows access from `127.0.0.1` or `localhost`.

- Use our API Node in website services starting with `https`

- Make sure you can normally connect to our API services (some regions may need a proxy).

- Make sure you are logged in in the settings and that your account still has enough credits to cover the consumption of API calls.

- On non-whitelisted sites or local area networks (LANs), please try to [log in using an API Key](https://docs.comfy.org/interface/user#logging-in-with-an-api-key).

</details>
