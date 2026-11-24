# Depth Estimation: Lotus

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_lotus_depth_v1_1)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_lotus_depth_v1_1-1.webp" width="360" alt="Depth Estimation: Lotus image_lotus_depth_v1_1-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_lotus_depth_v1_1-2.webp" width="360" alt="Depth Estimation: Lotus image_lotus_depth_v1_1-2.webp">

> Run Lotus Depth in ComfyUI for zero-shot, efficient monocular depth estimation with high detail retention.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_lotus_depth_v1_1.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_lotus_depth_v1_1.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/moge)

## Details

| | |
|---|---|
| Name | `image_lotus_depth_v1_1` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | SD1.5, Stability |
| Tags | Image, Text to Image |
| Type | open source |
| Date | 2025-05-21 |
| Author | ComfyUI |
| Download size | 1.9 GB |
| Min ComfyUI version | 0.3.42 |
| Usage | 10 |
| Nodes | 15 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #12 | image | image_lotus_depth_v1_1_input_image.png |
| output | `SaveImage` #9 | image | image_lotus_depth_v1_1.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `lotus-depth-d-v1-1.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/lotus/resolve/main/lotus-depth-d-v1-1.safetensors) |
| `vae-ft-mse-840000-ema-pruned.safetensors` | `vae` | [link](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors) |

## Subgraphs

- **Lotus depth** (12 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `BasicGuider` | 1 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `DisableNoise` | 1 | comfy-core |
| `ImageInvert` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LotusConditioning` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `SetFirstSigma` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>For Local User</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Report issue

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

## Model Links

- [Hugging Face:Comfy-Org/lotus](https://huggingface.co/Comfy-Org/lotus)

### Alternative Repos

- [ModelScope:Comfy-Org/lotus](https://modelscope.cn/models/Comfy-Org/lotus)

**diffusion_models**

- [lotus-depth-d-v1-1.safetensors](https://huggingface.co/Comfy-Org/lotus/resolve/main/lotus-depth-d-v1-1.safetensors) (1.62 GB)

**vae**

- [vae-ft-mse-840000-ema-pruned.safetensors](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors) (319.1 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │      └── lotus-depth-d-v1-1.safetensors
│   └── 📂 vae/
│          └── vae-ft-mse-840000-ema-pruned.safetensors
```

</details>
