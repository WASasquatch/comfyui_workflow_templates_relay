# Depth Estimation: MoGe

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_moge_depth_estimation-1.webp" width="360" alt="Depth Estimation: MoGe utility_moge_depth_estimation-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_moge_depth_estimation-2.webp" width="360" alt="Depth Estimation: MoGe utility_moge_depth_estimation-2.webp">

> Upload a single RGB image and adjust inference resolution and batch size. Generate a colored depth preview and raw depth map,

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_moge_depth_estimation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_moge_depth_estimation.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/moge)

## Details

| | |
|---|---|
| Name | `utility_moge_depth_estimation` |
| Category | Foundation › Image Tools |
| Media type | image |
| Models | MoGe |
| Tags | ControlNet |
| Type | open source |
| Date | 2026-05-20 |
| Author | ComfyUI |
| Download size | 614.4 MB |
| Min ComfyUI version | 0.22.0 |
| Usage | 13 |
| Nodes | 17 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #9 | image | alien_world.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `moge_2_vitl_normal_fp16.safetensors` | `geometry_estimation` | [link](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_2_vitl_normal_fp16.safetensors) |

## Subgraphs

- **Depth Estimation (MoGe)** (11 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MoGeRender` | 3 | comfy-core |
| `ComfySwitchNode` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `PreviewImage` | 2 | comfy-core |
| `ComfyMathExpression` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageToMask` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadMoGeModel` | 1 | comfy-core |
| `MaskPreview` | 1 | comfy-core |
| `MoGeInference` | 1 | comfy-core |
| `ResizeImageMaskNode` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## moge_depth_estimation

**Single perspective photo -> depth previews + mask**

`Load Image` -> `Depth Estimation (MoGe)`

### Main flow
- Runs MoGe inference on one source image
- Renders both colored depth and raw depth previews
- Converts the rendered `mask` image into a real `MASK` output

### Inputs
| Control | Meaning |
|--------|--------|
| `source_image` | Input RGB image |
| `inference_resolution` | MoGe detail level `0-9`; higher is slower but keeps more detail |
| `inference_batch_size` | Passed to `MoGeInference` batch size; use `1` for a single still image |
| `moge_model` | Model checkpoint loaded by `LoadMoGeModel`; see `Model Link` |
| `auto_resize_input` | Enables pre-inference resize logic for large images |

### Auto-resize logic
When `auto_resize_input` is enabled, the subgraph checks image width first:
- width `> 2048`: resize by longer edge to `2048` before inference
- width `<= 2048`: keep the original image

When `auto_resize_input` is disabled, the original image always goes into inference.

### Outputs
- `depth_colored`: colorized depth preview from `MoGeRender`
- `depth`: raw depth preview from `MoGeRender`
- `MASK`: mask rendered by `MoGeRender` and converted through `ImageToMask`

### What `MASK` means
According to the official MoGe repo, `mask` is a **binary mask for valid pixels**.

In practice, it marks image regions where MoGe believes the geometry is defined and reliable enough to use for downstream geometry results. Regions with undefined geometry, such as sky or other ambiguous areas, are typically excluded.

This is **not** a foreground segmentation or object cutout mask. It is better understood as a **valid geometry mask**.

</details>

<details><summary>Model Link</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Input Asset

- [alien_world.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/alien_world.png)

## MoGe — models & downloads

- [ModelScope:Comfy-Org/MoGe](https://modelscope.cn/models/Comfy-Org/MoGe)

Research repo: [microsoft/MoGe](https://github.com/microsoft/MoGe) (CVPR'25, monocular geometry from a single image).

ComfyUI weights: [Comfy-Org/MoGe](https://huggingface.co/Comfy-Org/MoGe) → `models/geometry_estimation/`

### Which checkpoint to use

| File | Version | Use when |
|------|---------|----------|
| `moge_1_vitl_fp16` | **MoGe-1** | Point map + depth + mask; relative scale. Lighter baseline. |
| `moge_2_vitl_normal_fp16` | **MoGe-2** | **Recommended.** Metric-scale depth/points, sharper detail, **normal maps** (needed for normal previews & better mesh edges). |

MoGe-2 adds metric scale and normals in one forward pass; MoGe-1 does not predict normals (normals in previews may be derived from points).

### Downloads
- [moge_1_vitl_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_1_vitl_fp16.safetensors) (599.3 MB)
- [moge_2_vitl_normal_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_2_vitl_normal_fp16.safetensors) (631.2 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 geometry_estimation/
│       ├── moge_2_vitl_normal_fp16.safetensors
│       └── moge_1_vitl_fp16.safetensors
```

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

### Issues
Update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)), then install models.
- Runtime: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)

</details>
