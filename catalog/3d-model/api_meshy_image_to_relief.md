# Meshy: Image to Relief

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_meshy_image_to_relief)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_image_to_relief-1.webp" width="360" alt="Meshy: Image to Relief api_meshy_image_to_relief-1.webp">

> Turn one photo into a bas-relief 3D model plus a 16-bit depth map for 3D printing, laser engraving and CNC carving. Relief height follows the image's brightness, so dark artwork on a light background reads as raised; carving mode, depth, plate, bend and mesh resolution describe the physical piece you are making.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_image_to_relief.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_meshy_image_to_relief.json)

## Details

| | |
|---|---|
| Name | `api_meshy_image_to_relief` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Meshy |
| Tags | 3D, API, Image to 3D |
| Type | API |
| Date | 2026-11-24 |
| Author | ComfyUI |
| Min ComfyUI version | 0.46.3 |
| Usage | 0 |
| Nodes | 6 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #1 | image | frost_furred_yeti.png |
| output | `SaveGLB` #4 | 3d | 3d/api_meshy_image_to_relief.glb |
| output | `SaveImageAdvanced` #5 | image | 3d/api_meshy_image_to_relief/depth.png |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 1 |  |
| `MarkdownNote` | 1 |  |
| `MeshyImageToReliefNode` | 1 |  |
| `PreviewImage` | 1 |  |
| `SaveGLB` | 1 |  |
| `SaveImageAdvanced` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Meshy: Image to Relief

**Turn one photo into a bas-relief model and a 16-bit depth map.** Relief height is read from the photo's brightness — dark artwork on a light background is raised — which is what makes this the tool for 3D printing, laser engraving and CNC carving instead of rebuilding an object in 3D.

**Input asset (demo):**
- [frost_furred_yeti.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/frost_furred_yeti.png) — 880 x 1168 front-facing artwork on a light ground; the subject is dark enough to read as raised (required workflow input).

### What each node does

| Node | Role |
|---|---|
| **Load Image** | The artwork the relief is cut from. Transparency is dropped before upload, so flatten a transparent logo onto white first. |
| **Meshy: Image to Relief** | The whole generation is this one API call: `relief_type`, `carving_mode`, `size_mm`, `base` and `bend` describe the physical piece, `mesh_resolution` sets the mesh density. It returns the relief as `GLB` (and `STL`, `OBJ`, `FBX`, `USDZ`, `3MF`) plus a 16-bit `depth_map` and a `preview` render — **only the outputs you connect are downloaded**.
With `preview` connected but no model output, Meshy still builds the GLB the preview is rendered from,
it is just not saved; with no model output and no preview, the task returns only the depth map. |
| **Save GLB** | Writes the relief mesh to `output/3d/`. |
| **Save Image (Advanced)** | Writes the depth map as a **16-bit PNG** — feed that straight into a laser or CNC job as the height map. |
| **Preview Image** | Shows the render Meshy returns for the finished relief. |

### Controls

| Control | What it does |
|---|---|
| `relief_type` → `carving_depth_mm` | `low` is the shallow cut used for laser engraving, CNC and plaques (3 mm default); `high` carves deeper for 3D printing (6 mm default). |
| `carving_mode` | `emboss` raises the nearer parts of the photo, `engrave` cuts them in. |
| `size_mm` | Length of the photo's longer side on the model, measured flat before any bend (20–250 mm). |
| `base` | `plate` adds a backing plate, `base_thickness_mm` sets its depth; `none` keeps only the relief and drops thin edges via `removal_threshold`. |
| `bend` | `off` keeps it flat; `convex` / `concave` wrap it around a cylinder, with `bend_axis` and `bend_angle`. |
| `mesh_resolution` | 512–2048. 1024 already gives a ~50 MB GLB; 2048 roughly doubles it, and a bend doubles it again. |
| `color_mapping` | Colours the mesh from the photo. STL and 3MF always stay white. |
| `seed` | Fixed; the seed only decides whether the node re-runs, it does not reproduce an earlier relief. |

---

### Limitations

- Billed per call; the sticker price is on the node.
- Height is driven by luminance: a busy background or a dark background flattens the relief, and large flat white areas stay flat.
- One artwork per call, front elevation only — this is not a way to model an object in the round (use Image to Model for that).
- Every connected model output is generated and downloaded, so connecting `STL` as well as `GLB` doubles the wait and the disk.

---

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare the input asset.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
