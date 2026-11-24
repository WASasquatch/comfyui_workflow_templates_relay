# Equirectangular HDR Skybox Generator

[← Brand & Design](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_text_prompt_to_360hdr.app)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_text_prompt_to_360hdr.app-1.webp" width="360" alt="Equirectangular HDR Skybox Generator templates_text_prompt_to_360hdr.app-1.webp">

> Prompt an environment and generate a equirectangular hdr image to use as skybox or lookdev in game development.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_text_prompt_to_360hdr.app.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_text_prompt_to_360hdr.app.json)

## Details

| | |
|---|---|
| Name | `templates_text_prompt_to_360hdr.app` |
| Category | Applied › Brand & Design |
| Output | image |
| Models | Qwen-Image, SeedVR2 |
| Tags | Game, LoRA, 3D |
| Type | open source |
| Date | 2026-03-06 |
| Author | shane |
| Download size | 29.6 GB |
| Min ComfyUI version | 0.28.0 |
| Usage | 37 |
| Nodes | 24 |

## Custom nodes required

- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)
- [seedvr2_videoupscaler](https://registry.comfy.org/nodes/seedvr2_videoupscaler)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_2512_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_2512_bf16.safetensors) |
| `qwen-360-diffusion-2512-int8-bf16-v2.safetensors` | `loras` | [link](https://huggingface.co/ProGamerGov/qwen-360-diffusion/resolve/main/qwen-360-diffusion-2512-int8-bf16-v2.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Image Upscale(SeedVR2)** (9 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `PrimitiveStringMultiline` | 2 |  |
| `SaveImage` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImpactCompare` | 1 |  |
| `KSampler` | 1 | comfy-core |
| `LayerUtility: If` | 1 |  |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PrimitiveFloat` | 1 | comfy-core |
| `SeedVR2LoadDiTModel` | 1 | seedvr2_videoupscaler |
| `SeedVR2LoadVAEModel` | 1 | seedvr2_videoupscaler |
| `SeedVR2VideoUpscaler` | 1 | seedvr2_videoupscaler |
| `SimpleMath+` | 1 | comfyui_essentials |
| `StringConcatenate` | 1 |  |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

## About SeedVR2

You can watch a comprehensive tutorial from the author on [Youtube](https://www.youtube.com/watch?v=MBtWYXq_r60) or check out the [Github](https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler).

## Quick Notes
Hover over the node inputs for tooltip info from author

input_noise_scale softens higher frequency details (e.g. skin textures)

latent_noise_scale softens low frequency details. Best around 0.01-0.05 (but depends on upscale factor)

Nodes support alpha masks

</details>
