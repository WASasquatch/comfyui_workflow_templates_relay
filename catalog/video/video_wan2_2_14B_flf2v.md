# Wan 2.2 14B First-Last Frame to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_wan2_2_14B_flf2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_flf2v-1.webp" width="360" alt="Wan 2.2 14B First-Last Frame to Video video_wan2_2_14B_flf2v-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_flf2v-2.webp" width="360" alt="Wan 2.2 14B First-Last Frame to Video video_wan2_2_14B_flf2v-2.webp">

> Generate smooth video transitions by defining start and end frames.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_flf2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan2_2_14B_flf2v.json)
- [Tutorial](https://docs.comfy.org/tutorials/video/wan/wan2_2)

## Details

| | |
|---|---|
| Name | `video_wan2_2_14B_flf2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.2, Wan |
| Tags | FLF2V, Video |
| Type | open source |
| Date | 2025-08-02 |
| Author | ComfyUI |
| Download size | 35.4 GB |
| Min ComfyUI version | 0.3.46 |
| Usage | 213 |
| Nodes | 40 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #62 | image | video_wan2_2_14B_flf2v_start_image.png |
| input | `LoadImage` #68 | image | video_wan2_2_14B_flf2v_end_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors) |
| `wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors) |
| `wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors) |
| `wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 4 | comfy-core |
| `KSamplerAdvanced` | 4 | comfy-core |
| `LoadImage` | 4 | comfy-core |
| `ModelSamplingSD3` | 4 | comfy-core |
| `UNETLoader` | 4 | comfy-core |
| `MarkdownNote` | 3 |  |
| `Note` | 3 |  |
| `CLIPLoader` | 2 | comfy-core |
| `CreateVideo` | 2 | comfy-core |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `SaveVideo` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `WanFirstLastFrameToVideo` | 2 | comfy-core |

## Notes embedded in the workflow

<details><summary>Video Size</summary>

```text
By default, we set the video to a smaller size for users with low VRAM. If you have enough VRAM, you can change the size
```

</details>

<details><summary>Note: About 4 Steps LoRA</summary>

```text
Using the Wan2.2 Lighting LoRA will result in the loss of video dynamics, but it will reduce the generation time. This template provides two workflows, and you can enable one as needed.
```

</details>

<details><summary>Note: Video Size</summary>

```text
By default, we set the video to a smaller size for users with low VRAM. If you have enough VRAM, you can change the size
```

</details>

<details><summary>MarkdownNote</summary>

1. Box-select then use Ctrl + B to enable
2. If you don't want to run both groups simultaneously, don't forget to use **Ctrl + B** to disable the **fp8_scaled + 4steps LoRA** group after enabling the **fp8_scaled** group, or try the [partial - execution](https://docs.comfy.org/interface/features/partial-execution) feature.

</details>

<details><summary>Note: Model Links</summary>

[Tutorial](https://docs.comfy.org/tutorials/video/wan/wan2_2)

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [Hugging Face:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [ModelScope:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)

**text_encoders**

- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) (6.27 GB)

**loras**

- [wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors) (1.14 GB)
- [wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors) (1.14 GB)

**diffusion_models**

- [wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors) (13.31 GB)
- [wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors) (13.31 GB)

**vae**

- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) (242.1 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
│   ├── 📂 loras/
│   │      ├── wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors
│   │      └── wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors
│   ├── 📂 diffusion_models/
│   │      ├── wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors
│   │      └── wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors
│   └── 📂 vae/
│          └── wan_2.1_vae.safetensors
```

## Report issue

If you encounter any issues when running this workflow, [report template issue here](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: VRAM Usage</summary>

## GPU:RTX4090D 24GB

| Model            | Size |VRAM Usage | 1st Generation | 2nd Generation |
|---------------------|-------|-----------|---------------|-----------------|
| fp8_scaled               |640*640| 84%               | ≈  536s              | ≈ 513s                   |
| fp8_scaled +  4steps LoRA  | 640*640  | 89%                | ≈ 108s               | ≈ 71s                   |

</details>
