# Tripo 2.5: Multiview to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=api_tripo_multiview_to_model)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_multiview_to_model-1.webp" width="360" alt="Tripo 2.5: Multiview to Model api_tripo_multiview_to_model-1.webp">

> Build 3D models from multiple angles with Tripo's advanced scanner.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/api_tripo_multiview_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_tripo_multiview_to_model.json)

## Details

| | |
|---|---|
| Name | `api_tripo_multiview_to_model` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Tripo |
| Tags | Image to 3D, 3D, API |
| Type | API |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Min ComfyUI version | 0.46.1 |
| Usage | 14 |
| Nodes | 11 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #7 | image | api_tripo_multiview_to_model_front_image.jpg |
| input | `LoadImage` #8 | image | api_tripo_multiview_to_model_back_image.jpg |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 | comfy-core |
| `SaveGLB` | 2 | comfy-core |
| `MarkdownNote` | 1 |  |
| `TripoConversionNode` | 1 | comfy-core |
| `TripoMultiviewToModelNode` | 1 | comfy-core |
| `TripoRetargetNode` | 1 | comfy-core |
| `TripoRigNode` | 1 | comfy-core |
| `TripoSmartUVNode` | 1 |  |
| `TripoTextureNodeV2` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# Tripo 2.5: Multiview to Model

A front and a back photo become one textured mesh — GLB and FBX. Pinned to `v2.5-20250123`; the node
also lists v3.0 and v3.1, which ship as their own templates (`Tripo3.0:`, `Tripo H3.1: Multiview to Model`).

**Input assets (demo):**
- [Front view → `image`](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_tripo_multiview_to_model_front_image.jpg) — required
- [Back view → `image_back`](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/api_tripo_multiview_to_model_back_image.jpg) — second view, required here

One object per photo, same scale, plain background. `image_left` / `image_right` stay empty here; fill
them for profile-heavy designs. A front image on its own is refused: Tripo needs at least one more
angle (`image_left`, `image_back` or `image_right`), so for a single photo use an image-to-model
template instead.

## Toolset — bypassed, select and `ctrl + B`

| Node | What it does | When |
| --- | --- | --- |
| **Multiview to Model** | front + back → textured mesh | always |
| **Rig** | adds a skeleton, `auto` picks biped / quadruped / hexapod / octopod | the model has to move |
| **Retarget** | plays a preset animation on a rig (`preset:idle` here) | after Rig |
| **Convert** | re-exports GLTF / USDZ / FBX / OBJ / STL / 3MF, plus quad, face limit, pivot, pack UV | another container or a poly budget |
| **Smart UV** | re-unwraps UVs and bakes the textures onto the new layout (≤ 80k triangles) | hand-painted seams |
| **Texture v2** | regenerates the texture from a prompt or a style image | geometry fine, surface wrong |

Enabling a tool only turns it on — it still has to be connected: wire the upstream `model task_id` /
`rig task_id` into that tool's input, then wire the tool's output to the saver you want. Every step
reads the id from the node above it, and Smart UV and Texture v2 return a new id, so the next tool
has to point at the newest one.

Outputs: `3d/tripo_multiview_to_model` (GLB) and `3d/tripo_multiview_to_model_fbx`.

</details>
