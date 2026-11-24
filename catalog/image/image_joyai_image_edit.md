# JoyAI Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_joyai_image_edit-1.webp" width="360" alt="JoyAI Image Edit image_joyai_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_joyai_image_edit-2.webp" width="360" alt="JoyAI Image Edit image_joyai_image_edit-2.webp">

> Edit images by following natural language instructions with JoyAI-Image-Edit, which leverages multimodal understanding for precise, spatially aware modifications. This workflow takes one reference image and produces one edited image output plus a side-by-side comparison view. Ideal for instruction-guided retouching, region-specific object replacement, and complex scene adjustments requiring relational grounding.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_joyai_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_joyai_image_edit.json)

## Details

| | |
|---|---|
| Name | `image_joyai_image_edit` |
| Category | Foundation › Image |
| Media type | image |
| Models | JoyAI Image Edit |
| Tags | Image, Image Edit, Int8 |
| Type | open source |
| Date | 2026-07-20 |
| Author | ComfyUI |
| Download size | 24.9 GB |
| Min ComfyUI version | 0.29.0 |
| Usage | 56 |
| Nodes | 15 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #41 | image | perfume_bottle.png.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `joyai_image_edit_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/JoyAI-Image-Edit/resolve/main/diffusion_models/joyai_image_edit_int8_convrot.safetensors) |
| `qwen3vl_8b_joyimage_edit_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/JoyAI-Image-Edit/resolve/main/text_encoders/qwen3vl_8b_joyimage_edit_int8_convrot.safetensors) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/JoyAI-Image-Edit/resolve/main/vae/wan_2.1_vae.safetensors) |

## Subgraphs

- **Image Edit (Joy Image Edit)** (9 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `TextEncodeJoyImageEdit` | 2 |  |
| `CFGNorm` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 |  |
| `GetImageSize` | 1 |  |
| `ImageCompare` | 1 |  |
| `ImageScaleToTotalPixels` | 1 |  |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Model Links</summary>

**Input Assets**
- [perfume_bottle.png.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/perfume_bottle.png.png) — required workflow input (`input/perfume_bottle.png.png`)

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## JoyImage Edit

Instruction-guided image editing workflow with one reference image.

## Model Links

- Repository: [Comfy-Org/JoyAI-Image-Edit](https://huggingface.co/Comfy-Org/JoyAI-Image-Edit)

**ModelScope mirrors** (alternative repo location)

- [ModelScope:Comfy-Org/JoyAI-Image-Edit](https://modelscope.cn/models/Comfy-Org/JoyAI-Image-Edit)

- Original: [jdopensource/JoyAI-Image-Edit-Plus-ComfyUI](https://huggingface.co/jdopensource/JoyAI-Image-Edit-Plus-ComfyUI)

**diffusion_models**

- [joyai_image_edit_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/JoyAI-Image-Edit/resolve/main/diffusion_models/joyai_image_edit_int8_convrot.safetensors) (15.3 GB)

**text_encoders**

- [qwen3vl_8b_joyimage_edit_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/JoyAI-Image-Edit/resolve/main/text_encoders/qwen3vl_8b_joyimage_edit_int8_convrot.safetensors) (9.37 GB)

**vae**

- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/JoyAI-Image-Edit/resolve/main/vae/wan_2.1_vae.safetensors) (242.1 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── joyai_image_edit_int8_convrot.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen3vl_8b_joyimage_edit_int8_convrot.safetensors
│   └── 📂 vae/
│       └── wan_2.1_vae.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

## Defaults

- Output size: `1024 x 1024`
- Sampler: `euler / simple`
- CFG: `4.0`

</details>
