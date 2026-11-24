# Depth Estimation: Marigold V2

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_marigold_v2_depth_estimation-1.webp" width="360" alt="Depth Estimation: Marigold V2 image_marigold_v2_depth_estimation-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_marigold_v2_depth_estimation-2.webp" width="360" alt="Depth Estimation: Marigold V2 image_marigold_v2_depth_estimation-2.webp">

> Estimate scene depth from an input image using Marigold V2, generating a depth map with brighter areas representing closer objects and darker areas representing farther objects.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_marigold_v2_depth_estimation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_marigold_v2_depth_estimation.json)

## Details

| | |
|---|---|
| Name | `image_marigold_v2_depth_estimation` |
| Category | Foundation › Image Tools |
| Media type | image |
| Models | Marigold v2 |
| Tags | Depth, Int8 |
| Type | open source |
| Date | 2026-09-14 |
| Author | ComfyUI |
| Download size | 20.9 GB |
| Min ComfyUI version | 0.36.0 |
| Usage | 52 |
| Nodes | 17 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #12 | image | ev_suv_gold_desert_pavilion.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_edit_2509_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/diffusion_models/qwen_image_edit_2509_int8_convrot.safetensors) |
| `marigold_v2_depth_conditioning.safetensors` | `embeddings` | [link](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/embeddings/marigold_v2_depth_conditioning.safetensors) |
| `marigold_v2_depth_log_stage2.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/loras/marigold_v2_depth_log_stage2.safetensors) |
| `marigold_v2_depth_log_stage2_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/vae/marigold_v2_depth_log_stage2_vae.safetensors) |

## Subgraphs

- **Image Depth Estimation (Marigold V2)** (13 nodes)

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

- [ev_suv_gold_desert_pavilion.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/ev_suv_gold_desert_pavilion.png)

## Model Links

- [Hugging Face:Comfy-Org/marigold-v2-0](https://huggingface.co/Comfy-Org/marigold-v2-0)
- [ModelScope:Comfy-Org/marigold-v2-0](https://modelscope.cn/models/Comfy-Org/marigold-v2-0)

**diffusion_models**

- [qwen_image_edit_2509_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/diffusion_models/qwen_image_edit_2509_int8_convrot.safetensors) (19.09 GB)

**loras**

- [marigold_v2_depth_log_stage2.safetensors](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/loras/marigold_v2_depth_log_stage2.safetensors) (1.59 GB)

**embeddings**

- [marigold_v2_depth_conditioning.safetensors](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/embeddings/marigold_v2_depth_conditioning.safetensors) (2.3 MB)

**vae**

- [marigold_v2_depth_log_stage2_vae.safetensors](https://huggingface.co/Comfy-Org/marigold-v2-0/resolve/main/vae/marigold_v2_depth_log_stage2_vae.safetensors) (242 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── qwen_image_edit_2509_int8_convrot.safetensors
│   ├── 📂 loras/
│   │   └── marigold_v2_depth_log_stage2.safetensors
│   ├── 📂 embeddings/
│   │   └── marigold_v2_depth_conditioning.safetensors
│   └── 📂 vae/
│       └── marigold_v2_depth_log_stage2_vae.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
