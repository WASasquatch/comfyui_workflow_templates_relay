# Wan 2.1 ControlNet

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/wan2.1_fun_control-1.webp" width="360" alt="Wan 2.1 ControlNet wan2.1_fun_control-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/wan2.1_fun_control-2.webp" width="360" alt="Wan 2.1 ControlNet wan2.1_fun_control-2.webp">

> Generate videos guided by pose, depth, and edge controls using Wan 2.1 ControlNet.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/wan2.1_fun_control.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/wan2.1_fun_control.json)
- [Tutorial](https://docs.comfy.org/tutorials/video/wan/fun-control)

## Details

| | |
|---|---|
| Name | `wan2.1_fun_control` |
| Category | Foundation › Video |
| Media type | image |
| Models | Wan2.1, Wan |
| Tags | Video to Video, Video |
| Type | open source |
| Date | 2025-04-15 |
| Author | ComfyUI |
| Download size | 10.6 GB |
| Min ComfyUI version | 0.3.31 |
| Usage | 15 |
| Nodes | 22 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #52 | image | wan2.1_fun_control_start_frame.png |
| input | `LoadVideo` #80 | video | wan2.1_fun_control_control_video.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `clip_vision_h.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors?download=true) |
| `wan2.1_fun_control_1.3B_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_fun_control_1.3B_bf16.safetensors?download=true) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors?download=true) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `Canny` | 1 | comfy-core |
| `CFGZeroStar` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPVisionEncode` | 1 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `GetVideoComponents` | 1 |  |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadVideo` | 1 |  |
| `MarkdownNote` | 1 |  |
| `ModelSamplingSD3` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `SkipLayerGuidanceDiT` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `UNetTemporalAttentionMultiply` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `WanFunControlToVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

[Tutorial](https://docs.comfy.org/tutorials/video/wan/fun-control)

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

**text_encoders**

- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true) (6.27 GB)

**clip_vision**

- [clip_vision_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors?download=true) (1.18 GB)

**diffusion_models**

- [wan2.1_fun_control_1.3B_bf16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_fun_control_1.3B_bf16.safetensors?download=true) (2.91 GB)

**vae**

- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors?download=true) (242.1 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
│   ├── 📂 clip_vision/
│   │      └── clip_vision_h.safetensors
│   ├── 📂 diffusion_models/
│   │      └── wan2.1_fun_control_1.3B_bf16.safetensors
│   └── 📂 vae/
│          └── wan_2.1_vae.safetensors
```

</details>
