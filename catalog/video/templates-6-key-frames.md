# Multi-Keyframe Video Stitching

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates-6-key-frames)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-6-key-frames-1.webp" width="360" alt="Multi-Keyframe Video Stitching templates-6-key-frames-1.webp">

> Creates a smooth video using 6 key frames.It auto fills in the motion between frames and stitches the segments together seamlessly.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-6-key-frames.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-6-key-frames.json)

## Details

| | |
|---|---|
| Name | `templates-6-key-frames` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.2 |
| Tags | FLF2V, Image to Video |
| Type | open source |
| Date | 2025-12-03 |
| Author | ComfyUI |
| Min ComfyUI version | 0.8.0 |
| Usage | 67 |
| Nodes | 90 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #62 | image | 6-key-frames-1.jpg |
| input | `LoadImage` #122 | image | 6-key-frames-2.png |
| input | `LoadImage` #124 | image | 6-key-frames-3.png |
| input | `LoadImage` #126 | image | 6-key-frames-4.png |
| input | `LoadImage` #128 | image | 6-key-frames-5.png |
| input | `LoadImage` #130 | image | 6-key-frames-6.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors) |
| `wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors) |
| `wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors) |
| `wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Subgraphs

- **Wan 2.2 FLF2V** (16 nodes)
- **Wan 2.2 FLF2V** (16 nodes)
- **Wan 2.2 FLF2V** (16 nodes)
- **Wan 2.2 FLF2V** (16 nodes)
- **Wan 2.2 FLF2V** (16 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 10 | comfy-core |
| `KSamplerAdvanced` | 10 | comfy-core |
| `LoraLoaderModelOnly` | 10 | comfy-core |
| `ModelSamplingSD3` | 10 | comfy-core |
| `UNETLoader` | 10 | comfy-core |
| `CreateVideo` | 6 | comfy-core |
| `LoadImage` | 6 | comfy-core |
| `CLIPLoader` | 5 | comfy-core |
| `Note` | 5 |  |
| `VAEDecode` | 5 | comfy-core |
| `VAELoader` | 5 | comfy-core |
| `WanFirstLastFrameToVideo` | 5 | comfy-core |
| `BatchImagesNode` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SaveVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [Hugging Face:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [ModelScope:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)

**text_encoders**

- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) (6.27 GB)

**diffusion_models**

- [wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors) (13.31 GB)
- [wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors) (13.31 GB)

**loras**

- [wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors) (1.14 GB)
- [wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors) (1.14 GB)

**vae**

- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) (242.1 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
│   ├── 📂 diffusion_models/
│   │   ├── wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors
│   │   └── wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors
│   ├── 📂 loras/
│   │   ├── wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors
│   │   └── wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors
│   └── 📂 vae/
│       └── wan_2.1_vae.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: Video Size</summary>

```text
By default, we set the video to a smaller size for users with low VRAM. If you have enough VRAM, you can change the size
```

</details>

<details><summary>Note: Video Size</summary>

```text
By default, we set the video to a smaller size for users with low VRAM. If you have enough VRAM, you can change the size
```

</details>

<details><summary>Note: Video Size</summary>

```text
By default, we set the video to a smaller size for users with low VRAM. If you have enough VRAM, you can change the size
```

</details>

<details><summary>Note: Video Size</summary>

```text
By default, we set the video to a smaller size for users with low VRAM. If you have enough VRAM, you can change the size
```

</details>

<details><summary>Note: Video Size</summary>

```text
By default, we set the video to a smaller size for users with low VRAM. If you have enough VRAM, you can change the size
```

</details>
