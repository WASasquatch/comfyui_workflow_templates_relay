# Wan2.5: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_wan_image_to_video)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan_image_to_video-1.webp" width="360" alt="Wan2.5: Image to Video api_wan_image_to_video-1.webp">

> Transform images into videos with synchronized audio, enhanced motion, and superior quality.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_wan_image_to_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_wan_image_to_video.json)

## Details

| | |
|---|---|
| Name | `api_wan_image_to_video` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.5, Wan |
| Tags | Image to Video, Video, API |
| Type | API |
| Date | 2025-09-27 |
| Author | ComfyUI |
| Min ComfyUI version | 0.3.60 |
| Usage | 44 |
| Nodes | 7 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #3 | audio | audio_ace_step_1_m2m_editing_input_audio.mp3 |
| input | `LoadImage` #11 | image | api_wan_image_to_video_input_image.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `LoadAudio` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `RecordAudio` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `WanImageToVideoApi` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note： About audio input</summary>

Audio input is optional. It should be 3-30 seconds long and smaller than 15MB.

If you need the audio input, you need to link the audio output to the **Wan Text to Video** input.

For the Record Audio node, you can select it and then use **Ctrl - B** to enable it.

</details>

<details><summary>Note：About API Node</summary>

[About API Node](https://docs.comfy.org/tutorials/partner-nodes/overview) - [Pricing](https://docs.comfy.org/tutorials/partner-nodes/pricing)
 
To use the API, you must be in a secure network environment:

- Allows access from `127.0.0.1` or `localhost`.

- Use our API Node in website services starting with `https`

- Make sure you can normally connect to our API services (some regions may need a proxy).

- Make sure you are logged in in the settings and that your account still has enough credits to cover the consumption of API calls.

- On non-whitelisted sites or local area networks (LANs), please try to [log in using an API Key](https://docs.comfy.org/interface/user#logging-in-with-an-api-key).

</details>
