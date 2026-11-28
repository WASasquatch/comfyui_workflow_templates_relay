# Wan 2.1 Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=text_to_video_wan)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/text_to_video_wan-1.webp" width="360" alt="Wan 2.1 Text to Video text_to_video_wan-1.webp">

> Generate videos from text prompts using Wan 2.1.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/text_to_video_wan.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/text_to_video_wan.json)
- [Tutorial](https://docs.comfy.org/tutorials/video/wan/wan-video)

## Details

| | |
|---|---|
| Name | `text_to_video_wan` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.1, Wan |
| Tags | Text to Video, Video |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 9.2 GB |
| Min ComfyUI version | 0.3.31 |
| Usage | 51 |
| Nodes | 11 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `wan2.1_t2v_1.3B_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_t2v_1.3B_fp16.safetensors?download=true) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors?download=true) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 |  |
| `CLIPLoader` | 1 |  |
| `CreateVideo` | 1 |  |
| `EmptyHunyuanLatentVideo` | 1 |  |
| `KSampler` | 1 |  |
| `ModelSamplingSD3` | 1 |  |
| `SaveVideo` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |
