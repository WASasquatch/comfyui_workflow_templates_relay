# PixVerse: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pixverse_i2v-1.webp" width="360" alt="PixVerse: Image to Video api_pixverse_i2v-1.webp">

> Generate dynamic videos from static images with motion and effects using PixVerse.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_pixverse_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_pixverse_i2v.json)

## Details

| | |
|---|---|
| Name | `api_pixverse_i2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | PixVerse |
| Tags | Image to Video, Video, API |
| Type | API |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.3.32 |
| Usage | 6 |
| Nodes | 5 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #6 | image | api_runway_reference_to_image_input_image.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `PixverseImageToVideoNode` | 1 | comfy-core |
| `PixverseTemplateNode` | 1 |  |
| `SaveVideo` | 1 | comfy-core |

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
