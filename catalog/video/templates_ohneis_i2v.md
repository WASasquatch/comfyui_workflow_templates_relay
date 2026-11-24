# Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_ohneis_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_ohneis_i2v-1.webp" width="360" alt="Image to Video templates_ohneis_i2v-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_ohneis_i2v-2.webp" width="360" alt="Image to Video templates_ohneis_i2v-2.webp">

> It shows how to go from a simple prompt to a Wes Anderson-style image using a cinematic image model, then enhance it with Nano Banana to improve textures and details, and finally turn it into a video using the current best video model, Kling 3.0.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_ohneis_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_ohneis_i2v.json)

## Details

| | |
|---|---|
| Name | `templates_ohneis_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Kling 2.6, Nano Banana Pro, Z-Image-Turbo |
| Tags | API, Image to Video, Text to Image, Video |
| Type | API |
| Date | 2026-03-19 |
| Author | ohneis652 |
| Download size | 19.3 GB |
| Min ComfyUI version | 0.5.0 |
| Usage | 6 |
| Nodes | 14 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `z_image_turbo_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) |
| `qwen_3_4b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Text to Image (Z-Image-Turbo)** (9 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveImage` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `GeminiImage2Node` | 1 | comfy-core |
| `KlingImageToVideoWithAudio` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
