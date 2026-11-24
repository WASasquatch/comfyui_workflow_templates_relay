# Hunyuan Video Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/hunyuan_video_text_to_video-1.webp" width="360" alt="Hunyuan Video Text to Video hunyuan_video_text_to_video-1.webp">

> Generate videos from text prompts using Hunyuan model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/hunyuan_video_text_to_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/hunyuan_video_text_to_video.json)
- [Tutorial](https://comfyanonymous.github.io/ComfyUI_examples/hunyuan_video/)

## Details

| | |
|---|---|
| Name | `hunyuan_video_text_to_video` |
| Category | Foundation › Video |
| Media type | image |
| Models | Hunyuan Video, Tencent |
| Tags | Text to Video, Video |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 33.0 GB |
| Min ComfyUI version | 0.3.31 |
| Usage | 10 |
| Nodes | 19 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `hunyuan_video_t2v_720p_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/resolve/main/split_files/diffusion_models/hunyuan_video_t2v_720p_bf16.safetensors?download=true) |
| `clip_l.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true) |
| `llava_llama3_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/resolve/main/split_files/text_encoders/llava_llama3_fp8_scaled.safetensors?download=true) |
| `hunyuan_video_vae_bf16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_repackaged/resolve/main/split_files/vae/hunyuan_video_vae_bf16.safetensors?download=true) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Note` | 2 |  |
| `BasicGuider` | 1 |  |
| `BasicScheduler` | 1 |  |
| `CLIPTextEncode` | 1 |  |
| `CreateVideo` | 1 |  |
| `DualCLIPLoader` | 1 |  |
| `EmptyHunyuanLatentVideo` | 1 |  |
| `FluxGuidance` | 1 |  |
| `KSamplerSelect` | 1 |  |
| `MarkdownNote` | 1 |  |
| `ModelSamplingSD3` | 1 |  |
| `RandomNoise` | 1 |  |
| `SamplerCustomAdvanced` | 1 |  |
| `SaveVideo` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAEDecodeTiled` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
Select a fp8 weight_dtype if you are running out of  memory.
```

</details>

<details><summary>Note</summary>

```text
Use the tiled decode node by default because most people will need it.

Lower the tile_size and overlap if you run out of memory.
```

</details>

<details><summary>MarkdownNote</summary>

🛈 [Learn more about this workflow](https://comfyanonymous.github.io/ComfyUI_examples/hunyuan_video/)

</details>
