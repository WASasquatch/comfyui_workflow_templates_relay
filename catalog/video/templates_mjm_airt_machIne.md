# AIrt MAchIne

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_mjm_airt_machIne-1.webp" width="360" alt="AIrt MAchIne templates_mjm_airt_machIne-1.webp">

> Upload any image to generate a unique, looping AI video. The workflow uses an LLM to create five prompts, produces images and video clips, and stitches them into a final seamless loop.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_mjm_airt_machIne.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_mjm_airt_machIne.json)

## Details

| | |
|---|---|
| Name | `templates_mjm_airt_machIne` |
| Category | Foundation › Video |
| Media type | image |
| Models | Wan2.2, Z-Image-Turbo |
| Tags | FLF2V, Text to Image |
| Type | open source |
| Date | 2026-03-03 |
| Author | Julien \| MJM |
| Download size | 56.0 GB |
| Min ComfyUI version | 0.8.0 |
| Usage | 10 |
| Nodes | 171 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #94 | image | AIrt_MAchIne_init.png |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors) |
| `wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors) |
| `z_image_turbo_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) |
| `wan2.2_i2v_A14b_high_noise_lora_rank64_lightx2v_4step_1022.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/resolve/main/wan2.2_i2v_A14b_high_noise_lora_rank64_lightx2v_4step_1022.safetensors) |
| `wan2.2_i2v_A14b_low_noise_lora_rank64_lightx2v_4step_1022.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Wan2.2-Distill-Loras/resolve/main/wan2.2_i2v_A14b_low_noise_lora_rank64_lightx2v_4step_1022.safetensors) |
| `qwen_3_4b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `4x-UltraSharp.safetensors` | `upscale_models` | [link](https://huggingface.co/Kim2091/UltraSharp/resolve/main/4x-UltraSharp.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Subgraphs

- **Z-Image** (12 nodes)
- **Z-Image** (12 nodes)
- **Z-Image** (12 nodes)
- **Z-Image** (12 nodes)
- **Z-Image** (12 nodes)
- **Optimized First-Last-Frame to Video with Wan 2.2** (10 nodes)
- **Optimized First-Last-Frame to Video with Wan 2.2** (10 nodes)
- **Optimized First-Last-Frame to Video with Wan 2.2** (10 nodes)
- **Optimized First-Last-Frame to Video with Wan 2.2** (10 nodes)
- **Optimized First-Last-Frame to Video with Wan 2.2** (10 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 15 | comfy-core |
| `VAEDecode` | 15 | comfy-core |
| `LoraLoaderModelOnly` | 12 | comfy-core |
| `PreviewAny` | 11 |  |
| `KSampler` | 10 | comfy-core |
| `KSamplerAdvanced` | 10 | comfy-core |
| `ModelSamplingSD3` | 10 | comfy-core |
| `AILab_QwenVL` | 6 |  |
| `ConditioningZeroOut` | 5 | comfy-core |
| `CreateVideo` | 5 | comfy-core |
| `EmptySD3LatentImage` | 5 | comfy-core |
| `ImageBatchMulti` | 5 |  |
| `ImageResizeKJv2` | 5 | comfyui-kjnodes |
| `ImageUpscaleWithModelBatched` | 5 |  |
| `ImpactStringSelector` | 5 |  |
| `ModelSamplingAuraFlow` | 5 | comfy-core |
| `PreviewImage` | 5 |  |
| `SaveImage` | 5 |  |
| `SaveVideo` | 5 |  |
| `VAEEncode` | 5 |  |
| `WanFirstLastFrameToVideo` | 5 | comfy-core |
| `UNETLoader` | 3 | comfy-core |
| `CLIPLoader` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `PrimitiveInt` | 2 |  |
| `VAELoader` | 2 | comfy-core |
| `BatchImagesNode` | 1 |  |
| `LoadImage` | 1 |  |
| `Note` | 1 |  |
| `PrimitiveFloat` | 1 |  |
| `UpscaleModelLoader` | 1 |  |
| `VHS_VideoCombine` | 1 |  |

## Notes embedded in the workflow

<details><summary>Model links for Z-Image Turbo</summary>

## Model links (when running locally)

- [Hugging Face:Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo)
- [ModelScope:Comfy-Org/z_image_turbo](https://modelscope.cn/models/Comfy-Org/z_image_turbo)

**text_encoders**

- [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) (7.49 GB)


**diffusion_models**

- [z_image_turbo_bf16.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) (11.46 GB)


**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)


**upscale_model**

- [4x-UltraSharp.pth](https://huggingface.co/lokCX/4x-Ultrasharp/blob/main/4x-UltraSharp.pth)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── qwen_3_4b.safetensors
│   ├── 📂 diffusion_models/
│   │      └── z_image_turbo_bf16.safetensors
│   └── 📂 vae/
│   │      └── ae.safetensors
│   └── 📂 upscale_models/
│          └── 4x-UltraSharp.pth
```

</details>

<details><summary>Read me!</summary>

```text
Load an image, hit run and be surprised by a new loop each time!

This is an hybrid workflow. It is using local video models and LLM API nodes.

You can use Z-Image LoRAs in the Z-Image Subgraphs.

You can bypass the save frames and save videos groups to only output the final combined video.

Enjoy,
Julien | MJM
```

</details>

<details><summary>Note: Model Links for Wan 2.2</summary>

## Model links (when running locally)

- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [Hugging Face:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)
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

</details>
