# MoGe: Panorama to Mesh

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=3d_moge_panorama_to_mesh)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_moge_panorama_to_mesh-1.webp" width="360" alt="MoGe: Panorama to Mesh 3d_moge_panorama_to_mesh-1.webp">

> Upload an equirectangular 360° panorama image and generate a textured GLB mesh with vertex colors.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_moge_panorama_to_mesh.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/3d_moge_panorama_to_mesh.json)

## Details

| | |
|---|---|
| Name | `3d_moge_panorama_to_mesh` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | MoGe |
| Tags | 3D, Image to 3D |
| Type | open source |
| Date | 2026-05-19 |
| Author | ComfyUI |
| Download size | 614.4 MB |
| Min ComfyUI version | 0.22.0 |
| Usage | 19 |
| Nodes | 12 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #28 | image | lego_street_panorama.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `moge_2_vitl_normal_fp16.safetensors` | `geometry_estimation` | [link](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_2_vitl_normal_fp16.safetensors) |

## Subgraphs

- **Panorama to Mesh (Moge)** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `ComfyMathExpression` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadMoGeModel` | 1 | comfy-core |
| `MoGePanoramaInference` | 1 | comfy-core |
| `MoGePointMapToMesh` | 1 | comfy-core |
| `ResizeImageMaskNode` | 1 |  |
| `SaveGLB` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model Link</summary>

## MoGe — models & downloads

Research repo: [microsoft/MoGe](https://github.com/microsoft/MoGe) (CVPR'25, monocular geometry from a single image).

ComfyUI weights: [Comfy-Org/MoGe](https://huggingface.co/Comfy-Org/MoGe) → `models/geometry_estimation/`

### Which checkpoint to use

| File | Version | Use when |
|------|---------|----------|
| `moge_1_vitl_fp16` | **MoGe-1** | Point map + depth + mask; relative scale. Lighter baseline. |
| `moge_2_vitl_normal_fp16` | **MoGe-2** | **Recommended.** Metric-scale depth/points, sharper detail, **normal maps** (needed for normal previews & better mesh edges). |

MoGe-2 adds metric scale and normals in one forward pass; MoGe-1 does not predict normals (normals in previews may be derived from points).

## Input Asset

- [lego_street_panorama.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/lego_street_panorama.png)

## Model Link

- [Hugging Face:Comfy-Org/MoGe](https://huggingface.co/Comfy-Org/MoGe)
- [ModelScope:Comfy-Org/MoGe](https://modelscope.cn/models/Comfy-Org/MoGe)

**geometry_estimation**

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

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Workflow</summary>

## moge_panorama_to_mesh

**Equirectangular (360°) panorama → textured GLB**

`Load Image` → subgraph `source_panorama` → `Save GLB`

Uses **`MoGePanoramaInference`**: 12 perspective views → merge → mesh. Research: [microsoft/MoGe](https://github.com/microsoft/MoGe).

Single photo workflow: `3d_moge_perspective_to_mesh.json` (`MoGeInference` + depth/normal previews).

### Pipeline
1. Optional downscale if `auto_resize_input` and width > 2048
2. Split equirect into **12** crops (90° FOV)
3. MoGe on each crop (`panorama_split_resolution`, `inference_resolution`)
4. **CPU merge** — stitch distance maps into one equirect depth (`panorama_merge_resolution`)
5. `MoGePointMapToMesh` → GLB with vertex colors

Merge disables per-view metric scale; MoGe-2 normals are not stitched. A long **“panorama merge”** progress phase is expected.

### Input
- **Equirectangular** 360°×180°, usually **2:1** (e.g. 2048×1024)
- **One** image per run

### Subgraph ports
| Port | Meaning |
|------|--------|
| `source_panorama` | RGB equirect |
| `inference_resolution` | MoGe detail **0–9** (default 5) |
| `panorama_split_resolution` | Each crop side length — **GPU** (default 512) |
| `panorama_merge_resolution` | Merge grid **long edge** — **CPU** (default 1024; never above input size) |
| `inference_batch_size` | Views per forward, 12 total (default 4) |
| `mesh_frame_index` | **0** for one panorama |
| `mesh_decimation` | Vertex stride; **1** = full |
| `mesh_gap_threshold` | Cull faces at depth jumps; **0** = off |
| `mesh_texture` | Bake panorama into GLB |
| `moge_model` | Checkpoint — **Model Link** |
| `auto_resize_input` | Downscale when width > 2048 |

**Split vs merge:** split = per-view inference sharpness; merge = seam / global depth quality. Example: 4096×2048 + merge **1920** → solve ~1920×960, then upsample to input size for meshing.

### Tuning
| Goal | Try |
|------|-----|
| Faster | resolution 3–4, split 512, merge 768 |
| Quality | resolution 9, split 768+, merge 2048+, MoGe-2 |
| GPU OOM | batch 1–2, split 512 |
| Slow merge | lower `panorama_merge_resolution` |

### Output
`mesh` → **Save GLB** (default `3d/Moge`). Spherical glTF mesh — view from inside the sphere.

</details>
