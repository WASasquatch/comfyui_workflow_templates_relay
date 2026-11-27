# Wan 2.2 14B Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_wan2_2_14B_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_t2v-1.webp" width="360" alt="Wan 2.2 14B Text to Video video_wan2_2_14B_t2v-1.webp">

> Generate high-quality videos from text prompts with cinematic aesthetic control and dynamic motion generation using Wan 2.2.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan2_2_14B_t2v.json)
- [Tutorial](https://docs.comfy.org/tutorials/video/wan/wan2_2)

## Details

| | |
|---|---|
| Name | `video_wan2_2_14B_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.2, Wan |
| Tags | Text to Video, Video |
| Type | open source |
| Date | 2025-07-29 |
| Author | ComfyUI |
| Download size | 35.4 GB |
| Min ComfyUI version | 0.16.4 |
| Usage | 322 |
| Nodes | 33 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors) |
| `wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors) |
| `wan2.2_t2v_lightx2v_4steps_lora_v1.1_high_noise.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_t2v_lightx2v_4steps_lora_v1.1_high_noise.safetensors) |
| `wan2.2_t2v_lightx2v_4steps_lora_v1.1_low_noise.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_t2v_lightx2v_4steps_lora_v1.1_low_noise.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Subgraphs

- **Text to Video(Wan2.2)** (30 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 5 | comfy-core |
| `PrimitiveFloat` | 4 | comfy-core |
| `PrimitiveInt` | 4 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `KSamplerAdvanced` | 2 | comfy-core |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `ModelSamplingSD3` | 2 | comfy-core |
| `UNETLoader` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `ComfyMathExpression` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `EmptyHunyuanLatentVideo` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model Links</summary>

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)
- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)
- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

[Tutorial](https://docs.comfy.org/tutorials/video/wan/wan2_2
) | [教程](https://docs.comfy.org/zh-CN/tutorials/video/wan/wan2_2
)

**Diffusion Model**       
- [wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors) (13.31 GB)
- [wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors) (13.31 GB)

**LoRA**

- [wan2.2_t2v_lightx2v_4steps_lora_v1.1_high_noise.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_t2v_lightx2v_4steps_lora_v1.1_high_noise.safetensors) (1.14 GB)
- [wan2.2_t2v_lightx2v_4steps_lora_v1.1_low_noise.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_t2v_lightx2v_4steps_lora_v1.1_low_noise.safetensors) (1.14 GB)

**VAE**
- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) (242.1 MB)

**Text Encoder**   
- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) (6.27 GB)

File save location

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   ├─── wan2.2_t2v_low_noise_14B_fp8_scaled.safetensors
│   │   └─── wan2.2_t2v_high_noise_14B_fp8_scaled.safetensors
│   ├───📂 loras/
│   │   ├───wan2.2_t2v_lightx2v_4steps_lora_v1.1_low_noise.safetensors
│   │   └───wan2.2_t2v_lightx2v_4steps_lora_v1.1_high_noise.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   └───📂 vae/
│       └── wan_2.1_vae.safetensors
```

</details>

<details><summary>VRAM Usage</summary>

## GPU:RTX4090D 24GB

| Model            | Size |VRAM Usage | 1st Generation | 2nd Generation |
|---------------------|-------|-----------|---------------|-----------------|
| fp8_scaled               |640*640| 84%               | ≈  536s              | ≈ 513s                   |
| fp8_scaled +  4steps LoRA  | 640*640  | 89%                | ≈ 108s               | ≈ 71s                   |

</details>
