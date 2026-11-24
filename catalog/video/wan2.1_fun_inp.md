# Wan 2.1 Inpainting

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/wan2.1_fun_inp-1.webp" width="360" alt="Wan 2.1 Inpainting wan2.1_fun_inp-1.webp">

> Generate videos from start and end frames using Wan 2.1 inpainting.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/wan2.1_fun_inp.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/wan2.1_fun_inp.json)
- [Tutorial](https://docs.comfy.org/tutorials/video/wan/fun-inp)

## Details

| | |
|---|---|
| Name | `wan2.1_fun_inp` |
| Category | Foundation › Video |
| Media type | image |
| Models | Wan2.1, Wan |
| Tags | Inpainting, Video |
| Type | open source |
| Date | 2025-04-15 |
| Author | ComfyUI |
| Download size | 10.6 GB |
| Min ComfyUI version | 0.3.31 |
| Usage | 9 |
| Nodes | 19 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #52 | image | wan2.1_fun_inp_start_image.png |
| input | `LoadImage` #72 | image | wan2.1_fun_inp_end_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `clip_vision_h.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors?download=true) |
| `wan2.1_fun_inp_1.3B_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_fun_inp_1.3B_bf16.safetensors?download=true) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors?download=true) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `CFGZeroStar` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPVisionEncode` | 1 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingSD3` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `SkipLayerGuidanceDiT` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `UNetTemporalAttentionMultiply` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `WanFunInpaintToVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

### Learn more about this workflow

> [ComfyUI Wan2.1 Fun InP Video - docs.comfy](https://docs.comfy.org/tutorials/video/wan/fun-inp)

</details>
