# Depth Map: Depth Anything 3

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_depth_anything3_video_depth_estimation-1.webp" width="360" alt="Depth Map: Depth Anything 3 utility_depth_anything3_video_depth_estimation-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_depth_anything3_video_depth_estimation-2.webp" width="360" alt="Depth Map: Depth Anything 3 utility_depth_anything3_video_depth_estimation-2.webp">

> Upload 1 image to generate a depth map for video depth estimation. Output a single depth-processed image ready for use in downstream workflows. Ideal for video generation tasks requiring depth control, 3D scene preprocessing, and animation depth mapping.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_depth_anything3_video_depth_estimation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_depth_anything3_video_depth_estimation.json)

## Details

| | |
|---|---|
| Name | `utility_depth_anything3_video_depth_estimation` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | Depth Anything v3 |
| Tags | ControlNet |
| Type | open source |
| Date | 2026-06-12 |
| Author | ComfyUI |
| Download size | 1.2 GB |
| Min ComfyUI version | 0.25.0 |
| Usage | 212 |
| Nodes | 11 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #87 | video | empty_room_assembly.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `depth_anything_3_mono_large.safetensors` | `geometry_estimation` | [link](https://huggingface.co/Comfy-Org/Depth-Anything-3/resolve/main/geometry_estimation/depth_anything_3_mono_large.safetensors) |

## Subgraphs

- **Video Depth Estimation (Depth Anything 3)** (5 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `CreateVideo` | 1 | comfy-core |
| `DA3Inference` | 1 | comfy-core |
| `DA3Render` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `LoadDA3Model` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `Video Slice` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model Link</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Depth-Anything-3](https://huggingface.co/Comfy-Org/Depth-Anything-3)

### Alternative Repos

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

<details><summary>About: Depth Anything 3 Video</summary>

## About Depth Anything 3

[Depth Anything 3 (DA3)](https://github.com/ByteDance-Seed/Depth-Anything-3) is a vision transformer from ByteDance Seed that recovers spatially consistent geometry from arbitrary visual inputs. In ComfyUI, it can estimate a depth map for every frame of a video.

### What this workflow does

Upload a video with **LoadVideo**, then run **Video Depth Estimation (Depth Anything 3)** to produce a per-frame depth sequence. Inside the subgraph:

1. **GetVideoComponents** splits the input video into a frame **image sequence**, **audio**, and **fps**.
2. **LoadDA3Model** loads the selected DA3 checkpoint.
3. **DA3Inference** runs mono depth estimation on each frame.
4. **DA3Render** converts geometry into a depth preview image per frame.

The subgraph also forwards the original **audio** and **fps** from the source video for downstream reuse.


### Model variants

- **depth_anything_3_mono_large** (default): High-quality relative monocular depth with sky segmentation. Best starting point for per-frame video depth.
- **depth_anything_3_metric_large**: Metric depth in real-world scale (meters). Use `raw` normalization in Render to preserve scale.
- **depth_anything_3_base**: Any-view foundation model (0.12B). Adds confidence maps; supports multi-view mode (not used in this per-frame video workflow).
- **depth_anything_3_small**: Fastest any-view model (0.08B). Lowest VRAM per frame.

### Learn more

- Paper: [arXiv:2511.10647](https://arxiv.org/abs/2511.10647)
- Original repo: [ByteDance-Seed/Depth-Anything-3](https://github.com/ByteDance-Seed/Depth-Anything-3)
- ComfyUI weights: [Comfy-Org/Depth-Anything-3](https://huggingface.co/Comfy-Org/Depth-Anything-3)

</details>
