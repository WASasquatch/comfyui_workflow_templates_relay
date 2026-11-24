# MiniMax H3: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_minimax_h3_t2i-1.webp" width="360" alt="MiniMax H3: Text to Image image_minimax_h3_t2i-1.webp">

> Generate a single still image from a text prompt with MiniMax H3, an omni-modal video model used here for its first-frame decode. No file inputs required: the graph samples an empty latent and decodes it through the H3 video VAE. Best suited to a single subject with a defined light source and a simple or blurred background.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_minimax_h3_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_minimax_h3_t2i.json)

## Details

| | |
|---|---|
| Name | `image_minimax_h3_t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | MiniMax H3 |
| Tags | Text to Image, Int8 |
| Type | open source |
| Date | 2026-10-27 |
| Author | ComfyUI |
| Download size | 39.0 GB |
| Min ComfyUI version | 0.32.0 |
| Usage | 1237 |
| Nodes | 19 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #48 | image | image_minimax_h3_t2i.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `minimax_h3_fl2va_pruned_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) |
| `minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/loras/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors) |
| `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) |
| `minimax_h3_video_vae_fp16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_fp16.safetensors) |

## Subgraphs

- **Text to Image (MiniMax H3)** (15 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `BasicGuider` | 1 |  |
| `BasicScheduler` | 1 |  |
| `CLIPLoader` | 1 |  |
| `CLIPTextEncode` | 1 |  |
| `ComfySwitchNode` | 1 |  |
| `EmptyLatentImage` | 1 |  |
| `KSamplerSelect` | 1 |  |
| `LoraLoaderModelOnly` | 1 |  |
| `LTXVSeparateAVLatent` | 1 |  |
| `ModelAttentionBackend` | 1 |  |
| `RandomNoise` | 1 |  |
| `ResolutionSelector` | 1 |  |
| `SamplerCustomAdvanced` | 1 |  |
| `SaveImage` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Steps</summary>

**Steps**

- `30` is the default for this checkpoint.
- Raise it to `50` for the most detail: H3 keeps improving with more steps.
- Lower step counts lose fine texture and skin detail first.

</details>

<details><summary>MarkdownNote</summary>

## Model Links

- [Hugging Face:Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)

### Alternative Repos

- [ModelScope:Comfy-Org/MiniMax-H3](https://modelscope.cn/models/Comfy-Org/MiniMax-H3)

**diffusion_models**

- [minimax_h3_fl2va_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) - 20.97 GB
- [minimax_h3_fl2va_pruned_bf16.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_bf16.safetensors) - 40.23 GB, full precision

**text_encoders**

- [qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) - 15.69 GB
- [qwen3vl_32b_minimax_h3_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_int8_convrot.safetensors) - 19.4 GB, drop-in swap

**vae**

- [minimax_h3_video_vae_fp16.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_fp16.safetensors) - 5.21 GB (the audio VAE is not needed for stills)

**loras**

- [minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/loras/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors) - 1.96 GB, the 8-step turbo this graph loads
- [minimax_h3_turbo_4step_ema_ckpt850.safetensors](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora/resolve/main/minimax_h3_turbo_4step_ema_ckpt850.safetensors) - 780 MB, optional 4-step community LoRA ([larryvrh/MiniMax-H3-Turbo-Lora](https://huggingface.co/larryvrh/MiniMax-H3-Turbo-Lora)); rename to `MiniMaxH3_fl2va_pruned_turbo_lora_larryvrh_4step_ema_ckpt850.safetensors`
- [minimax_h3_fl2v_turbo_4step_v1.0_768p_comfyui_bf16.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/loras/minimax_h3_fl2v_turbo_4step_v1.0_768p_comfyui_bf16.safetensors) - 1.96 GB, 4-step, tuned for 768p frames

**Disk footprint**: about **43.8 GB** with the files this graph loads (20.97 + 15.69 + 5.21 + 1.96).

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── minimax_h3_fl2va_pruned_int8_convrot.safetensors   20.97 GB
│   ├── 📂 text_encoders/
│   │   └── qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors       15.69 GB
│   ├── 📂 vae/
│   │   └── minimax_h3_video_vae_fp16.safetensors               5.21 GB
│   └── 📂 loras/
│       └── minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors  1.96 GB
```

Single-image decoding needs the ComfyUI build that ships PR #16881 (merged 2026-10-10).

## Report Issue

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
