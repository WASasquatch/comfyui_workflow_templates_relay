# Meshy 6: Text to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_meshy_text_to_model)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_text_to_model-1.webp" width="360" alt="Meshy 6: Text to Model api_meshy_text_to_model-1.webp">

> Generate high-quality 3D models from text prompts using Meshy 6. Create characters with refined geometry, mechanical objects with sharp edges, or game-ready low-poly assets.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_meshy_text_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_meshy_text_to_model.json)

## Details

| | |
|---|---|
| Name | `api_meshy_text_to_model` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Meshy |
| Tags | 3D, Text to 3D, API |
| Type | API |
| Date | 2026-01-19 |
| Author | ComfyUI |
| Min ComfyUI version | 0.46.3 |
| Usage | 20 |
| Nodes | 11 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveGLB` #7 | 3d | 3d/api_meshy_text_to_model.glb |
| output | `SaveGLB` #8 | 3d | 3d/api_meshy_text_to_model_from_fbx.glb |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `SaveGLB` | 2 | comfy-core |
| `MeshyAnimateModelNode` | 1 | comfy-core |
| `MeshyRefineNode` | 1 | comfy-core |
| `MeshyRigModelNode` | 1 | comfy-core |
| `MeshyTextToModelNode` | 1 |  |
| `MeshyTextureN1Node` | 1 |  |
| `MeshyTextureNode` | 1 | comfy-core |
| `SaveText` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## Meshy 6: Text to 3D Model

**One prompt in, one textured 3D model out.** Meshy 6 builds the mesh from the description alone — no reference image — then rebuilds the mesh to a game-ready triangle budget and generates UVs and textures in the same call.

### What each node does

| Node | Role |
|---|---|
| **Meshy: Text to Model** | The whole generation is this one API call: `prompt` and `style` in, a rebuilt and textured model out. It returns the `GLB`, the same model as `FBX`, and `model_file`, the path of the result on disk. |
| **Save GLB** (upper) | Writes the `GLB` branch to `output/3d/`. |
| **Save GLB** (lower) | Writes the `FBX` branch, converted to GLB, under its own name so the two files never overwrite each other. |
| **Save Text** | Writes `model_file` to a `.txt`, stamped with the date — a cheap way to find the output again later. |
| **Meshy Toolset** | Bypassed group of five follow-up calls driven by `meshy_task_id`: refine, texture, texture N1, rig, animate. |

### The Meshy toolset

The toolset is the follow-up API chain for a job that already exists. Every node in it takes a `meshy_task_id` and re-uses that job's geometry, so a second pass costs one call instead of a fresh generation.

- **Meshy: Refine** — adds PBR maps and a texture prompt to an existing task.
- **Meshy: Texture** — re-textures with a style prompt or a reference image.
- **Meshy: Texture N1** — N1 texturing, optionally keeping the original UVs.
- **Meshy: Rig Model** — turns the mesh into a rigged character; `height_meters` sets the scale.
- **Meshy: Animate** — animates a rigged task by `action_id`.

They ship **bypassed**. Select the nodes you want at the bottom of the canvas and press `Ctrl+B` to enable them, then wire the `meshy_task_id` output of **Text to Model** into the node you enabled.

### Controls

| Control | What it does |
|---|---|
| `prompt` | What to build. The demo asks for a Death Knight; describe one object, its materials and its pose. |
| `model` | `meshy-6` in this graph; `meshy-7` sits in the same list if you want the newer geometry. |
| `style` | `realistic` keeps the read of a real object; the stylised options push the shape language instead. |
| `should_remesh` → `topology`, `target_polycount` | Remesh on, `triangle` topology, 300000 triangles. Lower the budget for real-time use. |
| `symmetry_mode` | `auto` mirrors parts that look symmetric; force `on`/`off` for asymmetric characters. |
| `pose_mode` | Empty means natural pose. A t-pose in the prompt is the usual trick when the model will be rigged. |
| `seed` | Fixed, so a re-run repeats the request; the result itself is not bit-identical. |
| `ultra_mode` → `ultra_resolution` | Extra detail at a higher credit cost, `2k` maps. |

---

### Limitations

- Billed per run (the node shows the credit cost); toolset follow-ups are billed separately.
- The prompt is the only input — the model cannot see a reference image, so describe silhouette and materials rather than relying on a look you know.
- One object per run: asking for a scene usually fuses the parts into a single mesh.
- The saved files are copies; the API already returned them, so the save nodes are there to control name and folder.

---

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)).

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note</summary>

## Saved text

`Save Text` writes the path of the generated model to a `.txt`, stamped with the date. Handy when you want to find the file again without digging through `output/`.

## Task id

The `meshy_task_id` output is what the Meshy toolset nodes take, so you can refine, re-texture or rig the same job later without rebuilding it.

## Output

Both save nodes write into `ComfyUI/output/3d/` — one for the GLB branch, one for the FBX branch.

</details>
