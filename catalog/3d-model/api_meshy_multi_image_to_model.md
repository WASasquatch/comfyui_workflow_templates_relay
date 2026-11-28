# Meshy 6: Multi-Image to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_meshy_multi_image_to_model)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_multi_image_to_model-1.webp" width="360" alt="Meshy 6: Multi-Image to Model api_meshy_multi_image_to_model-1.webp">

> Create high-quality 3D models from multiple images using Meshy 6. More photos mean better detail capture, accurate proportions, and cleaner mesh structure.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_multi_image_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_meshy_multi_image_to_model.json)

## Details

| | |
|---|---|
| Name | `api_meshy_multi_image_to_model` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Meshy |
| Tags | 3D, API, Image to 3D |
| Type | API |
| Date | 2026-01-19 |
| Author | ComfyUI |
| Min ComfyUI version | 0.46.3 |
| Usage | 37 |
| Nodes | 15 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #8 | image | joker_front.jpg |
| input | `LoadImage` #12 | image | joker_back.jpg |
| input | `LoadImage` #13 | image | joker_side.jpg |
| output | `Save3DAdvanced` #22 | 3d | 3d/api_meshy_multi_image_to_model.glb |
| output | `SaveGLB` #23 | 3d | 3d/api_meshy_multi_image_to_model_from_fbx.glb |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 3 | comfy-core |
| `MarkdownNote` | 2 |  |
| `MeshyAnimateModelNode` | 1 | comfy-core |
| `MeshyMultiImageToModelNode` | 1 |  |
| `MeshyRefineNode` | 1 | comfy-core |
| `MeshyRigModelNode` | 1 | comfy-core |
| `MeshyTextureN1Node` | 1 |  |
| `MeshyTextureNode` | 1 | comfy-core |
| `Preview3DAdvanced` | 1 | comfy-core |
| `Save3DAdvanced` | 1 |  |
| `SaveGLB` | 1 | comfy-core |
| `SaveText` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note</summary>

## Saved text

`Save Text` writes the path of the generated model to a `.txt`, stamped with the date. Handy when you want to find the file again without digging through `output/`.

## Task id

The `meshy_task_id` output is what the Meshy toolset nodes take, so you can refine, re-texture or rig the same job later without rebuilding it.

## Output

Both save nodes write into `ComfyUI/output/3d/`. The preview node can also export the file straight from its viewport.

</details>

<details><summary>MarkdownNote</summary>

## Meshy 6: Multi-Image to 3D Model

**Three photos of the same subject in, one textured 3D model out.** Meshy 6 fuses a front, a side and a back view into a single mesh, so the surfaces the camera never sees are inferred from the other views instead of guessed from one image.

**Input assets (demo):**
- [joker_front.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/joker_front.jpg) — front view, the framing and scale reference (required workflow input).
- [joker_back.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/joker_back.jpg) — back view, gives the model its rear silhouette (required workflow input).
- [joker_side.jpg](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/joker_side.jpg) — side view, fixes depth and profile (required workflow input).

### What each node does

| Node | Role |
|---|---|
| **Load Image** ×3 | Front, back and side reference of the same subject. They feed `images.image0`, `image1` and `image2`; a fourth slot exists but stays empty here. |
| **Meshy: Multi-Image to Model** | Single API call: fuses the views into one mesh, runs a remesh to a game-ready triangle budget, generates UVs and returns three things — the model `GLB`, an `FBX`, and the `model_file` path of the result on disk. |
| **Preview 3D (Advanced)** | Shows the returned GLB in the viewport and can export it straight from the node. |
| **Save 3D (Advanced)** | Writes the GLB the node returned to the output folder. |
| **Save GLB** | Writes the FBX branch as GLB. Both save nodes exist to show the two formats; wire the one you need and remove the other. |
| **Save Text** | Writes the returned file path to a `.txt`, one line, stamped with the date (for example `meshy_model_path_20261125_203113_00001.txt`). |
| **Meshy Toolset** | Bypassed group of five follow-up calls, driven by the returned task id instead of the file: see below. |

### The Meshy toolset

The toolset is the same model's follow-up API chain. Every node in it takes a `meshy_task_id`, i.e. the id of an existing Meshy job — it re-uses the geometry instead of generating it again, so refining or re-texturing an old task costs one call rather than a fresh build.

- **Meshy: Refine** — adds PBR maps and a texture prompt to an existing task.
- **Meshy: Texture** — re-textures with a style prompt or a reference image.
- **Meshy: Texture N1** — N1 texturing, optionally keeping the original UVs.
- **Meshy: Rig Model** — turns the mesh into a rigged character, `height_meters` sets the scale.
- **Meshy: Animate** — animates a rigged task by `action_id`.

They ship **bypassed** (the whole group is `Ctrl+B`-ready): select the nodes you want and press `Ctrl+B` to enable them, then wire the `meshy_task_id` output of **Multi-Image to Model** (or an id saved earlier) into the node you enabled. Leave them off unless you need a second pass.

### Controls

| Control | What it does |
|---|---|
| `model` | `meshy-6` is the multi-image model; pick it unless you are deliberately comparing. |
| `should_remesh` → `topology`, `target_polycount` | Remesh on, `triangle` topology, 300000 triangles. Lower the budget for real-time use. |
| `symmetry_mode` | `auto` lets the model mirror symmetric parts; set `on`/`off` when the subject is (or is not) symmetric. |
| `should_texture` → `texture_resolution`, `pbr` | Texture generation and 2K maps; PBR is off by default. |
| `pose_mode` | `auto` reads the pose from the references. |
| `seed` | Fixed, so a re-run repeats the same request; the render itself is not bit-identical. |
| `ultra_mode` | Extra mesh detail for a higher credit cost. |

---

### Limitations

- Billed per run (the node shows the credit cost); follow-up toolset calls are billed separately.
- Three views of the *same* subject, taken from roughly front, side and back, give the best result; unrelated images are fused into one object.
- The returned files are already on disk, so both save nodes are optional — they exist to control the name and the folder.

---

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare the input assets.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
