# Image Upscale: Wan 2.2 Two-Stage

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_sirolim_image_controlled_upscale-1.webp" width="360" alt="Image Upscale: Wan 2.2 Two-Stage utility_sirolim_image_controlled_upscale-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_sirolim_image_controlled_upscale-2.webp" width="360" alt="Image Upscale: Wan 2.2 Two-Stage utility_sirolim_image_controlled_upscale-2.webp">

> Upload an image and set a resize factor. Generate an AI prompt from your image and upscale it in two controlled stages to enhance detail and fidelity.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_sirolim_image_controlled_upscale.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_sirolim_image_controlled_upscale.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/video-upscale)

## Details

| | |
|---|---|
| Name | `utility_sirolim_image_controlled_upscale` |
| Category | Foundation › Image Tools |
| Media type | image |
| Models | Wan2.2 |
| Tags | API, Image Upscale |
| Type | API |
| Date | 2026-03-12 |
| Author | sirolim |
| Download size | 20.0 GB |
| Min ComfyUI version | 0.35.2 |
| Usage | 19 |
| Nodes | 49 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #664 | image | playful_portrait.png |
| output | `SaveImage` #733 | image | utility_sirolim_image_controlled_upscale-1.png |
| output | `SaveImage` #670 | image | utility_sirolim_image_controlled_upscale-2.png |

## Custom nodes required

- [comfyui-wanvideowrapper](https://registry.comfy.org/nodes/comfyui-wanvideowrapper)
- [ComfyUI-WanVideoWrapper](https://registry.comfy.org/nodes/ComfyUI-WanVideoWrapper)

## Subgraphs

- **Image Controlled Upscale** (20 nodes)
- **Image Controlled Upscale** (20 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveInt` | 6 |  |
| `GetImageSize` | 4 |  |
| `SimpleMath+` | 4 |  |
| `WanVideoLoraSelect` | 4 |  |
| `MarkdownNote` | 3 |  |
| `ImageResize+` | 2 |  |
| `SaveImage` | 2 |  |
| `VHS_SelectImages` | 2 |  |
| `WanVideoDecode` | 2 | comfyui-wanvideowrapper |
| `WanVideoEmptyEmbeds` | 2 | comfyui-wanvideowrapper |
| `WanVideoEncode` | 2 |  |
| `WanVideoModelLoader` | 2 |  |
| `WanVideoSampler` | 2 | comfyui-wanvideowrapper |
| `WanVideoSetLoRAs` | 2 | ComfyUI-WanVideoWrapper |
| `WanVideoTextEncodeCached` | 2 |  |
| `WanVideoTorchCompileSettings` | 2 | comfyui-wanvideowrapper |
| `WanVideoVAELoader` | 2 | comfyui-wanvideowrapper |
| `GeminiNodeV3` | 1 |  |
| `ImageCompare` | 1 |  |
| `LoadImage` | 1 |  |
| `PreviewAny` | 1 |  |

## Notes embedded in the workflow

<details><summary>Steps</summary>

## Quick Upscaling:
- 25 Steps

## Detailed Upscaling:
- 50+ Steps

</details>

<details><summary>Image Controlled Upscale</summary>

This is a two-stage iterative image upscaler. It can help to increase fidelity especially in AI generated images.

## How It Works

1. **Upload an image**
2. Set your resize factor

3. The system:
   - Analyzes your image and generates a prompt
   - Upscales it in a first pass e.g. 4x with a higher denoise
   - Upscales it in a second pass e.g. 2x Refining with a finer denoise


## Tips

- When you need higher resemblance, lower the denoise
- When you need better textures, increase the denoise
- Try it for different image styles
- Experiment with steps and denoise
- This workflow is really useful when you need control over your upscale


That’s it.  
Image -> Controlled Upscale

</details>

<details><summary>Denoising Strength</summary>

## Creative Upscaling:
- 0.20 - 0.4 (coarse)

## Detail Preserving:
- 0.10 - 0.20 (fine)

</details>
