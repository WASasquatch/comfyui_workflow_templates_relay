# SVD Text to Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=txt_to_image_to_video)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/txt_to_image_to_video-1.webp" width="360" alt="SVD Text to Image to Video txt_to_image_to_video-1.webp">

> Generate videos by first creating images from text prompts.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/txt_to_image_to_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/txt_to_image_to_video.json)
- [Tutorial](https://comfyanonymous.github.io/ComfyUI_examples/video/#image-to-video)

## Details

| | |
|---|---|
| Name | `txt_to_image_to_video` |
| Category | Foundation › Video |
| Output | video |
| Models | SVD, Stability |
| Tags | Text to Video, Video |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 15.4 GB |
| Min ComfyUI version | 0.3.31 |
| Usage | 17 |
| Nodes | 15 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sd_xl_base_1.0.safetensors` | `checkpoints` | [link](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors?download=true) |
| `svd_xt.safetensors` | `checkpoints` | [link](https://huggingface.co/stabilityai/stable-video-diffusion-img2vid-xt/resolve/main/svd_xt.safetensors?download=true) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 |  |
| `KSampler` | 2 |  |
| `VAEDecode` | 2 |  |
| `CheckpointLoaderSimple` | 1 |  |
| `CreateVideo` | 1 |  |
| `EmptyLatentImage` | 1 |  |
| `ImageOnlyCheckpointLoader` | 1 |  |
| `MarkdownNote` | 1 |  |
| `PreviewImage` | 1 |  |
| `SaveVideo` | 1 |  |
| `SVD_img2vid_Conditioning` | 1 |  |
| `VideoLinearCFGGuidance` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

🛈 [Learn more about this workflow](https://comfyanonymous.github.io/ComfyUI_examples/video/#image-to-video)

</details>
