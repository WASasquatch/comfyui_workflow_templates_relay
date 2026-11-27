# MoGe: Perspective Geometry Estimation

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=3d_moge_perspective_to_mesh)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_moge_perspective_to_mesh-1.webp" width="360" alt="MoGe: Perspective Geometry Estimation 3d_moge_perspective_to_mesh-1.webp">

> Upload an image to estimate its perspective geometry. Generate a 3D depth map and surface normals from the input.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_moge_perspective_to_mesh.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/3d_moge_perspective_to_mesh.json)

## Details

| | |
|---|---|
| Name | `3d_moge_perspective_to_mesh` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | MoGe |
| Tags | 3D, Image to 3D |
| Type | open source |
| Date | 2026-05-15 |
| Author | ComfyUI |
| Download size | 614.4 MB |
| Min ComfyUI version | 0.22.0 |
| Usage | 55 |
| Nodes | 16 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #9 | image | modern_living_room.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `moge_2_vitl_normal_fp16.safetensors` | `geometry_estimation` | [link](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_2_vitl_normal_fp16.safetensors) |

## Subgraphs

- **Geometry Estimation (MoGe)** (10 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `MoGeRender` | 2 | comfy-core |
| `PreviewImage` | 2 | comfy-core |
| `ComfyMathExpression` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageScaleToMaxDimension` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadMoGeModel` | 1 | comfy-core |
| `MoGeInference` | 1 | comfy-core |
| `MoGePointMapToMesh` | 1 | comfy-core |
| `SaveGLB` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## moge_image_to_mesh

**Input Assets**
- [modern_living_room.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/modern_living_room.png) — required workflow input (`input/modern_living_room.png`)

**Single perspective photo -> textured GLB**

`Load Image` -> `Geometry Estimation (MoGe)` -> `Save GLB`

### Main flow
- Runs MoGe inference on one source image
- Converts the inferred geometry into a mesh
- Exposes OpenGL and DirectX normal previews

### Inputs
| Control | Meaning |
|--------|--------|
| `source_image` | Input RGB image |
| `inference_resolution` | MoGe detail level `0-9`; higher is slower but keeps more detail |
| `inference_batch_size` | Passed to `MoGeInference` batch size; use `1` for a single still image |
| `mesh_frame_index` | Batch/frame index used when converting geometry to mesh; use `0` for one image |
| `mesh_decimation` | Mesh decimation step; `1` keeps the densest mesh |
| `mesh_gap_threshold` | Removes faces across large depth discontinuities; `0` disables the filter |
| `mesh_texture` | Bakes source image colors into the exported GLB |
| `moge_model` | Model checkpoint loaded by `LoadMoGeModel`; see `Model Link` |
| `auto_resize_input` | Enables pre-inference resize logic for large images |

### Auto-resize logic
When `auto_resize_input` is enabled, the subgraph checks image width first:
- width `> 2048`: resize by longer edge to `2048` before inference
- width `<= 2048`: keep the original image

When `auto_resize_input` is disabled, the original image always goes into inference.

### Outputs
- `mesh`: mesh output for `Save GLB`
- `normal_opengl`: preview rendered through `MoGeRender`
- `normal_directx`: preview rendered through `MoGeRender`

</details>

<details><summary>Model Link</summary>

## MoGe — models & downloads

**ModelScope mirrors** (alternative repo location)

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
