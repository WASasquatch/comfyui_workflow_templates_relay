# Video Upscale: Wan 2.2 Creative

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_video_upscale)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_video_upscale-1.webp" width="360" alt="Video Upscale: Wan 2.2 Creative utility_video_upscale-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_video_upscale-2.webp" width="360" alt="Video Upscale: Wan 2.2 Creative utility_video_upscale-2.webp">

> Upload a video and upscale it to a higher resolution with Wan 2.2

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_video_upscale.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_video_upscale.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/video-upscale)

## Details

| | |
|---|---|
| Name | `utility_video_upscale` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | Wan2.2 |
| Tags | Video Upscale |
| Type | open source |
| Date | 2026-01-22 |
| Author | sirolim |
| Download size | 40.0 GB |
| Min ComfyUI version | 0.16.4 |
| Usage | 89 |
| Nodes | 33 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #727 | video | input_upscale.mp4 |
| output | `SaveVideo` #678 | video | utility_video_upscale.mp4 |

## Custom nodes required

- [ComfyUI-WanVideoWrapper](https://registry.comfy.org/nodes/ComfyUI-WanVideoWrapper)
- [comfyui-wanvideowrapper](https://registry.comfy.org/nodes/comfyui-wanvideowrapper)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors) |
| `umt5_xxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp16.safetensors) |

## Subgraphs

- **Utility Video Upscale** (14 nodes)
- **Video Stitch** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 4 |  |
| `GetVideoComponents` | 3 | comfy-core |
| `ComfyMathExpression` | 2 |  |
| `CreateVideo` | 2 | comfy-core |
| `GetImageSize` | 2 |  |
| `PrimitiveInt` | 2 |  |
| `SaveVideo` | 2 |  |
| `ImageFromBatch` | 1 | comfy-core |
| `ImageResize+` | 1 |  |
| `ImageStitch` | 1 | comfy-core |
| `LoadVideo` | 1 |  |
| `ResizeImageMaskNode` | 1 |  |
| `ResolutionSelector` | 1 |  |
| `WanVideoDecode` | 1 | comfyui-wanvideowrapper |
| `WanVideoEmptyEmbeds` | 1 | comfyui-wanvideowrapper |
| `WanVideoEncode` | 1 |  |
| `WanVideoLoraSelect` | 1 |  |
| `WanVideoModelLoader` | 1 |  |
| `WanVideoSampler` | 1 | comfyui-wanvideowrapper |
| `WanVideoSetLoRAs` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoTextEncodeCached` | 1 |  |
| `WanVideoTorchCompileSettings` | 1 | comfyui-wanvideowrapper |
| `WanVideoVAELoader` | 1 | comfyui-wanvideowrapper |

## Notes embedded in the workflow

<details><summary>Settings</summary>

| Category               | Subcategory          | Parameter Recommendations                     |
|------------------------|----------------------|----------------------------------------------|
| **Adjust Size**        | Width and height     | It must be divisible by 64 (e.g., 1088 instead of 1080). You can also try 4K (3840 x 2160), but it will take more time to get the output. |
| **Denoising Strength** | Creative Upscaling   | 0.20 – 0.30 (coarse)                         |
|                        | Detail Preserving    | 0.10 – 0.20 (fine)                           |
| **Steps**              | Quick Upscaling      | 4 – 12 Steps                                 |
|                        | Detailed Upscaling   | 12 – 30 Steps                                |

</details>

<details><summary>Trim Video</summary>

- Upscale duration can be up to 121 frames with Wan 2.2
- Upscale duration is constrained by available VRAM

</details>

<details><summary>Utility Video Upscale</summary>

Upscale videos to sharper, higher-resolution outputs with Wan2.2, with precise control over detail, denoise strength, and sizing parameters in **Utility Video Upscale**.

## How It Works
1. Upload a video
2. Choose the target size
3. Wan2.2 upscales and sharpens the frames
4. The workflow rebuilds and saves the final video

## Tips
- Use clean source videos with stable framing
- Can improve heavily compressed, blurry, or noisy footage
- Keep the target width and height divisible by 64
- Use lower denoise values for faithful upscaling and higher values for more creative detail
- Shorter clips are faster and easier to test before processing a full video

## Constraints
- 4K resolution requires a lot of VRAM

## That's it.

Low-resolution video to sharper upscaled output in ComfyUI with **Utility Video Upscale**.

</details>

<details><summary>Resolution</summary>

- Full HD ~ 2.1 megapixel
- 4K ~ 8.3 megapixel

</details>
