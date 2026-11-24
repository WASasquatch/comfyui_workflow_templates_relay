# Albedo Estimation: Marigold V2

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_marigold_v2_albedo_estimation-1.webp" width="360" alt="Albedo Estimation: Marigold V2 image_marigold_v2_albedo_estimation-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_marigold_v2_albedo_estimation-2.webp" width="360" alt="Albedo Estimation: Marigold V2 image_marigold_v2_albedo_estimation-2.webp">

> Estimate albedo from an input image using Marigold V2. The workflow separates surface color from lighting and shading, producing an albedo map useful for relighting, material analysis, and 3D asset creation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_marigold_v2_albedo_estimation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_marigold_v2_albedo_estimation.json)

## Details

| | |
|---|---|
| Name | `image_marigold_v2_albedo_estimation` |
| Category | Foundation › Image Tools |
| Media type | image |
| Models | Marigold v2 |
| Tags | Albedo Estimation, Int8 |
| Type | open source |
| Date | 2026-09-14 |
| Author | ComfyUI |
| Download size | 20.9 GB |
| Min ComfyUI version | 0.36.0 |
| Usage | 19 |
| Nodes | 17 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #12 | image | flower_with_texture.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_edit_2509_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/diffusion_models/qwen_image_edit_2509_int8_convrot.safetensors) |
| `marigold_v2_albedo_conditioning.safetensors` | `embeddings` | [link](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/embeddings/marigold_v2_albedo_conditioning.safetensors) |
| `marigold_v2_albedo.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/loras/marigold_v2_albedo.safetensors) |
| `marigold_v2_albedo_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/vae/marigold_v2_albedo_vae.safetensors) |

## Subgraphs

- **Image Albedo Estimation (Marigold V2)** (13 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BasicGuider` | 1 |  |
| `ConditioningLoader` | 1 |  |
| `DisableNoise` | 1 |  |
| `ImageCompare` | 1 |  |
| `KSamplerSelect` | 1 |  |
| `LoadImage` | 1 |  |
| `LoraLoaderModelOnly` | 1 |  |
| `ManualSigmas` | 1 |  |
| `MarigoldV2PostProcess` | 1 |  |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 |  |
| `SamplerCustomAdvanced` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAEEncode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Input Asset

- [flower_with_texture.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/flower_with_texture.png)

## Model Links

- [Hugging Face:Comfy-Org/marigold-v2-0](https://huggingface.co/Comfy-Org/marigold-v2-0)
- [ModelScope:Comfy-Org/marigold-v2-0](https://modelscope.cn/models/Comfy-Org/marigold-v2-0)

**diffusion_models**

- [qwen_image_edit_2509_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/diffusion_models/qwen_image_edit_2509_int8_convrot.safetensors) (19.09 GB)

**loras**

- [marigold_v2_albedo.safetensors](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/loras/marigold_v2_albedo.safetensors) (1.59 GB)

**embeddings**

- [marigold_v2_albedo_conditioning.safetensors](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/embeddings/marigold_v2_albedo_conditioning.safetensors) (2.5 MB)

**vae**

- [marigold_v2_albedo_vae.safetensors](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/vae/marigold_v2_albedo_vae.safetensors) (242 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── qwen_image_edit_2509_int8_convrot.safetensors
│   ├── 📂 loras/
│   │   └── marigold_v2_albedo.safetensors
│   ├── 📂 embeddings/
│   │   └── marigold_v2_albedo_conditioning.safetensors
│   └── 📂 vae/
│       └── marigold_v2_albedo_vae.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
