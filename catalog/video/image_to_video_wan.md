# Wan 2.1 Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_to_video_wan)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_to_video_wan-1.webp" width="360" alt="Wan 2.1 Image to Video image_to_video_wan-1.webp">

> Generate videos from images using Wan 2.1.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_to_video_wan.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_to_video_wan.json)
- [Tutorial](https://docs.comfy.org/tutorials/video/wan/wan-video)

## Details

| | |
|---|---|
| Name | `image_to_video_wan` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.1, Wan |
| Tags | Text to Video, Video |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 38.2 GB |
| Min ComfyUI version | 0.3.31 |
| Usage | 42 |
| Nodes | 15 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #52 | image | image_to_video_wan_start_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `clip_vision_h.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) |
| `wan2.1_i2v_480p_14B_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_i2v_480p_14B_fp16.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 |  |
| `CLIPLoader` | 1 |  |
| `CLIPVisionEncode` | 1 |  |
| `CLIPVisionLoader` | 1 |  |
| `CreateVideo` | 1 |  |
| `KSampler` | 1 |  |
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `ModelSamplingSD3` | 1 |  |
| `SaveVideo` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |
| `WanImageToVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

[Tutorial](https://docs.comfy.org/tutorials/video/wan/wan-video)

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

**text_encoders**

- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) (6.27 GB)

**clip_vision**

- [clip_vision_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) (1.18 GB)

**diffusion_models**

- [wan2.1_i2v_480p_14B_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_i2v_480p_14B_fp16.safetensors) (30.54 GB)

**vae**

- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) (242.1 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
│   ├── 📂 clip_vision/
│   │      └── clip_vision_h.safetensors
│   ├── 📂 diffusion_models/
│   │      └── wan2.1_i2v_480p_14B_fp16.safetensors
│   └── 📂 vae/
│          └── wan_2.1_vae.safetensors
```

</details>
