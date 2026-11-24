# Depth Estimation: Depth Anything 3

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_depth_anything3_image_depth_estimation-1.webp" width="360" alt="Depth Estimation: Depth Anything 3 utility_depth_anything3_image_depth_estimation-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_depth_anything3_image_depth_estimation-2.webp" width="360" alt="Depth Estimation: Depth Anything 3 utility_depth_anything3_image_depth_estimation-2.webp">

> Upload 1 image. Generate a depth map using Depth Anything 3 and view a side-by-side comparison of the original and depth output. Ideal for 3D scene reconstruction, AR/VR asset preparation, and visual effects depth passes.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_depth_anything3_image_depth_estimation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_depth_anything3_image_depth_estimation.json)

## Details

| | |
|---|---|
| Name | `utility_depth_anything3_image_depth_estimation` |
| Category | Foundation › Image Tools |
| Media type | image |
| Models | Depth Anything v3 |
| Tags | ControlNet |
| Type | open source |
| Date | 2026-06-12 |
| Author | ComfyUI |
| Download size | 1.2 GB |
| Min ComfyUI version | 0.25.0 |
| Usage | 34 |
| Nodes | 8 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #85 | image | retro_futuristic_home.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `depth_anything_3_mono_large.safetensors` | `geometry_estimation` | [link](https://huggingface.co/Comfy-Org/Depth-Anything-3/resolve/main/geometry_estimation/depth_anything_3_mono_large.safetensors) |

## Subgraphs

- **Image Depth Estimation (Depth Anything 3)** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `DA3Inference` | 1 | comfy-core |
| `DA3Render` | 1 | comfy-core |
| `ImageCompare` | 1 | comfy-core |
| `LoadDA3Model` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model Link</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Link

- [Hugging Face:Comfy-Org/Depth-Anything-3](https://huggingface.co/Comfy-Org/Depth-Anything-3)
- [ModelScope:Comfy-Org/Depth-Anything-3](https://modelscope.cn/models/Comfy-Org/Depth-Anything-3)

**geometry_estimation**

- [depth_anything_3_small.safetensors](https://huggingface.co/Comfy-Org/Depth-Anything-3/resolve/main/geometry_estimation/depth_anything_3_small.safetensors) (130.9 MB)
- [depth_anything_3_base.safetensors](https://huggingface.co/Comfy-Org/Depth-Anything-3/resolve/main/geometry_estimation/depth_anything_3_base.safetensors) (516.4 MB)
- [depth_anything_3_mono_large.safetensors](https://huggingface.co/Comfy-Org/Depth-Anything-3/resolve/main/geometry_estimation/depth_anything_3_mono_large.safetensors) (1.24 GB)
- [depth_anything_3_metric_large.safetensors](https://huggingface.co/Comfy-Org/Depth-Anything-3/resolve/main/geometry_estimation/depth_anything_3_metric_large.safetensors) (1.24 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 geometry_estimation/
│       ├── depth_anything_3_small.safetensors
│       ├── depth_anything_3_base.safetensors
│       ├── depth_anything_3_mono_large.safetensors
│       └── depth_anything_3_metric_large.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>About: Depth Anything 3</summary>

## About Depth Anything 3

[Depth Anything 3 (DA3)](https://github.com/ByteDance-Seed/Depth-Anything-3) is a vision transformer from ByteDance Seed that recovers spatially consistent geometry from arbitrary visual inputs, with or without known camera poses. A single plain DINO encoder and unified depth-ray representation let one model family cover monocular depth, multi-view depth, camera pose estimation, and 3D reconstruction.

### What this workflow does

Upload one image and run **Image Depth Estimation (Depth Anything 3)** to produce a depth map. The result is shown in **Depth Preview**, with a side-by-side **ImageCompare** against the source image.

### Model variants

- **depth_anything_3_mono_large** (default): High-quality relative monocular depth with sky segmentation. Best starting point for single-image depth maps.
- **depth_anything_3_metric_large**: Metric depth in real-world scale (meters). Use `raw` normalization in Render to preserve scale.
- **depth_anything_3_base**: Any-view foundation model (0.12B). Adds confidence maps and supports multi-view mode.
- **depth_anything_3_small**: Fastest any-view model (0.08B). Lowest VRAM; supports confidence and multi-view.


### Learn more

- Paper: [arXiv:2511.10647](https://arxiv.org/abs/2511.10647)
- Original repo: [ByteDance-Seed/Depth-Anything-3](https://github.com/ByteDance-Seed/Depth-Anything-3)
- ComfyUI weights: [Comfy-Org/Depth-Anything-3](https://huggingface.co/Comfy-Org/Depth-Anything-3)

</details>
