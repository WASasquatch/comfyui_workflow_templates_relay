# Realistic 2k Images - Quick Variations

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_rob_realistic_2k_images_quick_variations-1.webp" width="360" alt="Realistic 2k Images - Quick Variations template_rob_realistic_2k_images_quick_variations-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_rob_realistic_2k_images_quick_variations-2.webp" width="360" alt="Realistic 2k Images - Quick Variations template_rob_realistic_2k_images_quick_variations-2.webp">

> Upload an image that you want a variation of. The workflow captions the input image, generates with Grok Image, and upscales with Z-Image to add realistic textures.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_rob_realistic_2k_images_quick_variations.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_rob_realistic_2k_images_quick_variations.json)

## Details

| | |
|---|---|
| Name | `template_rob_realistic_2k_images_quick_variations` |
| Category | Foundation › Image |
| Media type | image |
| Models | Grok, Z-Image-Turbo |
| Tags | API, Image Upscale, Text to Image |
| Type | API |
| Date | 2026-03-08 |
| Author | hellorob |
| Download size | 19.3 GB |
| Min ComfyUI version | 0.16.1 |
| Usage | 27 |
| Nodes | 24 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #77 | image | rapper_on_cliff_with_moon.png |
| output | `SaveImage` #103 | image | template_rob_realistic_2k_images_quick_variations.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `z_image_turbo_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) |
| `qwen_3_4b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) |
| `RealESRGAN_x4plus.safetensors` | `upscale_models` | [link](https://huggingface.co/Comfy-Org/Real-ESRGAN_repackaged/resolve/main/RealESRGAN_x4plus.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Image Upscale(Z-image-Turbo)** (15 nodes)
- **New Subgraph** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `SaveImage` | 2 | comfy-core |
| `StringConcatenate` | 2 |  |
| `AILab_QwenVL` | 1 |  |
| `CLIPLoader` | 1 | comfy-core |
| `GrokImageNode` | 1 |  |
| `ImageCompare` | 1 | comfy-core |
| `ImageRemoveAlpha+` | 1 |  |
| `ImageScaleBy` | 1 | comfy-core |
| `ImageScaleToTotalPixels` | 1 | comfy-core |
| `ImageUpscaleWithModel` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `Note` | 1 |  |
| `PreviewAny` | 1 |  |
| `UNETLoader` | 1 | comfy-core |
| `UpscaleModelLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
res_2m - 
bong tangent
```

</details>
