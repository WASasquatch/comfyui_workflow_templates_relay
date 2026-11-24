# Wan2.1 ATI

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_ati-1.webp" width="360" alt="Wan2.1 ATI video_wan_ati-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_ati-2.webp" width="360" alt="Wan2.1 ATI video_wan_ati-2.webp">

> Trajectory-controlled Video Generation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_ati.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan_ati.json)
- [Tutorial](https://docs.comfy.org/tutorials/video/wan/wan-ati)

## Details

| | |
|---|---|
| Name | `video_wan_ati` |
| Category | Foundation › Video |
| Media type | image |
| Models | Wan2.1, Wan |
| Tags | Video, Motion Control |
| Type | open source |
| Date | 2025-05-21 |
| Author | ComfyUI |
| Download size | 23.7 GB |
| Min ComfyUI version | 0.3.46 |
| Usage | 9 |
| Nodes | 18 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #240 | image | video_wan_ati_input_image.jpg |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `clip_vision_h.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) |
| `Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPVisionEncode` | 1 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `ModelSamplingSD3` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `WanTrackToVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>VRAM Usage</summary>

4090D 24GB (VRAM usage 90%)
- size: 720*480
- 1st gen: 500s
- 2nd gen: 463s

</details>

<details><summary>How to create Trajectory JSON</summary>

Visit [Trajectory-Annotation-Tool](https://comfyui-wiki.github.io/Trajectory-Annotation-Tool/), upload an image and create trajectories.

</details>

<details><summary>Model Links</summary>

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

[Tutorial](https://docs.comfy.org/tutorials/video/wan/wan-ati)

**Diffusion Model**
- [Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors) (15.96 GB)

**VAE**
- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors?download=true) (242.1 MB)

**Text encoders**   Chose one of following model
- [umt5_xxl_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp16.safetensors?download=true) (10.59 GB)
- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true) (6.27 GB)

**clip_vision**
- [clip_vision_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) (1.18 GB)

File save location

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   └───Wan2_1-I2V-ATI-14B_fp8_e4m3fn.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors # or other version
│   ├───📂 clip_vision/
│   │   └─── clip_vision_h.safetensors
│   └───📂 vae/
│       └──  wan_2.1_vae.safetensors
```

</details>
