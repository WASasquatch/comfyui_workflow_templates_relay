# Qwen Image 2512

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_qwen_Image_2512)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_Image_2512-1.webp" width="360" alt="Qwen Image 2512 image_qwen_Image_2512-1.webp">

> Text-to-image model with enhanced human realism, finer natural details for landscapes and animal fur, and improved text rendering with accurate layout and multimodal composition.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_Image_2512.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_qwen_Image_2512.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image-2512)

## Details

| | |
|---|---|
| Name | `image_qwen_Image_2512` |
| Category | Foundation › Image |
| Output | image |
| Models | Qwen, Qwen-Image |
| Tags | Image, Text to Image |
| Type | open source |
| Date | 2025-12-31 |
| Author | ComfyUI |
| Download size | 29.6 GB |
| Min ComfyUI version | 0.4.0 |
| Usage | 258 |
| Nodes | 21 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #60 | image | image_qwen_Image_2512.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_2512_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors) |
| `Qwen-Image-2512-Lightning-4steps-V1.0-fp32.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Qwen-Image-2512-Lightning/resolve/main/Qwen-Image-2512-Lightning-4steps-V1.0-fp32.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Text to Image (Qwen-Image 2512)** (18 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `PrimitiveFloat` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)

### Alternative Repos

- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)

**diffusion_models**

- [qwen_image_2512_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors) (19.03 GB)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**vae**

- [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

**loras**

- [Qwen-Image-2512-Lightning-4steps-V1.0-fp32.safetensors](https://huggingface.co/lightx2v/Qwen-Image-2512-Lightning/resolve/main/Qwen-Image-2512-Lightning-4steps-V1.0-fp32.safetensors) (1.58 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── qwen_image_2512_fp8_e4m3fn.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   └── 📂 loras/
│       └── Qwen-Image-2512-Lightning-4steps-V1.0-fp32.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Aspect Ratios</summary>

- 1:1 : 1328x1328
- 16:9 : 1664x928
- 9:16 : 928x1664
- 4:3 : 1472x1104
- 3:4 : 1104x1472
- 3:2 : 1584x1056
- 2:3 : 1056x1584

</details>
