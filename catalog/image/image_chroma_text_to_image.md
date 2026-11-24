# Chroma: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_chroma_text_to_image)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_chroma_text_to_image-1.webp" width="360" alt="Chroma: Text to Image image_chroma_text_to_image-1.webp">

> Chroma - enhanced Flux model with improved image quality and better prompt understanding for stunning text-to-image generation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_chroma_text_to_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_chroma_text_to_image.json)

## Details

| | |
|---|---|
| Name | `image_chroma_text_to_image` |
| Category | Foundation › Image |
| Output | image |
| Models | Chroma, FLUX |
| Tags | Text to Image, Image |
| Type | open source |
| Date | 2025-06-04 |
| Author | ComfyUI |
| Download size | 21.7 GB |
| Min ComfyUI version | 0.3.31 |
| Usage | 89 |
| Nodes | 18 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #740 | image | image_chroma_text_to_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `Chroma1-HD-fp8mixed.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Chroma1-HD_repackaged/resolve/main/split_files/diffusion_models/Chroma1-HD-fp8mixed.safetensors) |
| `t5xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn_scaled.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `Note` | 2 |  |
| `BasicScheduler` | 1 | comfy-core |
| `CFGGuider` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `T5TokenizerOptions` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Optional Flow Shift</summary>

```text
Flow Shift node set to 1.0 represents intended shift by the creator of the Chroma model and will produce greater detail.
```

</details>

<details><summary>Optional Padding</summary>

```text
min_padding 1 is the official way. setting it to 0 works too.
```

</details>

<details><summary>MarkdownNote</summary>

Chroma final model has been released and is hosted [here](https://huggingface.co/lodestones/Chroma1-HD). You can visit [here](https://huggingface.co/lodestones/Chroma) to get previous versions for download. For other models, if you have used models related to Flux, then you probably don't need to download them again.

## diffusion_models

## Model Links

- [Hugging Face:Comfy-Org/Chroma1-HD_repackaged](https://huggingface.co/Comfy-Org/Chroma1-HD_repackaged)
- [Hugging Face:Comfy-Org/Lumina_Image_2.0_Repackaged](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Chroma1-HD_repackaged](https://modelscope.cn/models/Comfy-Org/Chroma1-HD_repackaged)
- [ModelScope:Comfy-Org/Lumina_Image_2.0_Repackaged](https://modelscope.cn/models/Comfy-Org/Lumina_Image_2.0_Repackaged)

[Chroma1-HD.safetensors](https://huggingface.co/lodestones/Chroma1-HD/resolve/main/Chroma1-HD.safetensors) (16.58 GB)

or fp8_scaled version for lower VRAM GPU

[Chroma1-HD-fp8mixed.safetensors](https://huggingface.co/Comfy-Org/Chroma1-HD_repackaged/resolve/main/split_files/diffusion_models/Chroma1-HD-fp8mixed.safetensors) (8.56 GB)

## text_encoders

[t5xxl_fp16](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) (9.12 GB)

or

[t5xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn_scaled.safetensors) (4.8 GB)

## vae

[ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

```
📂 ComfyUI/
├─ 📂 models/
│   ├─ 📂 diffusion_models/
│   │     ├── Chroma1-HD-fp8_scaled_rev2_learned_topp0.25_k16-2688_svd.safetensors
│   │     └── Chroma1-HD.safetensors
│   ├─ 📂 text_encoders/
│   │     ├── t5xxl_fp8_e4m3fn_scaled.safetensors
│   │     └── t5xxl_fp16.safetensors 
│   └─ 📂 vae/
│            └──  ae.safetensors
```

</details>
