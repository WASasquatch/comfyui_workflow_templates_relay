# Pixal3D: Multi Views to 3D

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=3d_pixal3d_multi_views)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_pixal3d_multi_views-1.webp" width="360" alt="Pixal3D: Multi Views to 3D 3d_pixal3d_multi_views-1.webp">

> Upload your own separate view images, or use one mixed multi-view turnaround sheet. The workflow prepares front, back, left and right views, then reconstructs a textured 3D model with Pixal3D Multi-View.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_pixal3d_multi_views.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/3d_pixal3d_multi_views.json)

## Details

| | |
|---|---|
| Name | `3d_pixal3d_multi_views` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Pixal3D |
| Tags | 3D, Image to 3D, Int8 |
| Type | open source |
| Date | 2026-09-09 |
| Author | ComfyUI |
| Download size | 8.7 GB |
| Min ComfyUI version | 0.42.0 |
| Usage | 266 |
| Nodes | 68 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #364 | image | character_turnaround_4view_sheet.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `birefnet.safetensors` | `background_removal` | [link](https://huggingface.co/Comfy-Org/BiRefNet/resolve/main/background_removal/birefnet.safetensors) |
| `dino_v3_L_naf_fp32.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/clip_vision/dino_v3_L_naf_fp32.safetensors) |
| `pixal3d_multiview_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/diffusion_models/pixal3d_multiview_int8_convrot.safetensors) |
| `trellis_2_shape_vae_bf16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/vae/trellis_2_shape_vae_bf16.safetensors) |
| `trellis_2_texture_vae_bf16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/vae/trellis_2_texture_vae_bf16.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewImage` | 6 | comfy-core |
| `ImageCropToMask` | 4 | comfy-core |
| `ImageCropV2` | 4 |  |
| `KSampler` | 4 | comfy-core |
| `RemoveBackground` | 4 | comfy-core |
| `SaveImageAdvanced` | 4 |  |
| `MeshToFile3D` | 3 | comfy-core |
| `CFGOverride` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `MeshSmoothNormals` | 2 | comfy-core |
| `Preview3DAdvanced` | 2 | comfy-core |
| `RescaleCFG` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `ApplyTextureToMesh` | 1 | comfy-core |
| `BakeAmbientOcclusion` | 1 | comfy-core |
| `BakeNormalMapFromMesh` | 1 | comfy-core |
| `BakeTextureFromVoxel` | 1 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `DecimateMesh` | 1 | comfy-core |
| `EmptyTrellis2LatentStructure` | 1 | comfy-core |
| `GetMeshInfo` | 1 | comfy-core |
| `LoadBackgroundRemovalModel` | 1 | comfy-core |
| `LoadImage` | 1 |  |
| `ModelSamplingSD3` | 1 | comfy-core |
| `Note` | 1 |  |
| `PaintMesh` | 1 | comfy-core |
| `Pixal3DMultiViewConditioning` | 1 |  |
| `PrimitiveInt` | 1 | comfy-core |
| `RemeshMesh` | 1 | comfy-core |
| `RenderUVAtlas` | 1 | comfy-core |
| `Save3DAdvanced` | 1 |  |
| `Trellis2ShapeStage` | 1 | comfy-core |
| `Trellis2TextureStage` | 1 | comfy-core |
| `Trellis2UpsampleStage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `UnwrapMesh` | 1 | comfy-core |
| `VaeDecodeShapeTrellis` | 1 | comfy-core |
| `VaeDecodeStructureTrellis2` | 1 | comfy-core |
| `VaeDecodeTextureTrellis` | 1 | comfy-core |
| `VoxelToMesh` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: CFG</summary>

```text
CFG override and rescaleCFG are to match the original default pipeline behaviour
```

</details>

<details><summary>MarkdownNote</summary>

This workflow uses a turnaround sheet as input. You can use the `Character Turnaround Sheet Generator` [template](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/api_google_nano_banana_create_turnaround_sheet.json) in the template library to create a Character Turnaround Sheet Generator as input, or you can load your separated views image

</details>

<details><summary>MarkdownNote</summary>

## Input Asset

- [character_turnaround_4view_sheet.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/character_turnaround_4view_sheet.png)

## Model Links

- [Hugging Face:Comfy-Org/Pixal3D](https://huggingface.co/Comfy-Org/Pixal3D)
- [ModelScope:Comfy-Org/Pixal3D](https://modelscope.cn/models/Comfy-Org/Pixal3D)
- [Hugging Face:Comfy-Org/BiRefNet](https://huggingface.co/Comfy-Org/BiRefNet)
- [ModelScope:Comfy-Org/BiRefNet](https://modelscope.cn/models/Comfy-Org/BiRefNet)

**vae**

- [trellis_2_texture_vae_bf16.safetensors](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/vae/trellis_2_texture_vae_bf16.safetensors) (904.5 MB)
- [trellis_2_shape_vae_bf16.safetensors](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/vae/trellis_2_shape_vae_bf16.safetensors) (1.02 GB)

**clip_vision**

- [dino_v3_L_naf_fp32.safetensors](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/clip_vision/dino_v3_L_naf_fp32.safetensors) (1.13 GB)

**background_removal**

- [birefnet.safetensors](https://huggingface.co/Comfy-Org/BiRefNet/resolve/main/background_removal/birefnet.safetensors) (423.9 MB)

**diffusion_models**

- [pixal3d_multiview_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/diffusion_models/pixal3d_multiview_int8_convrot.safetensors) (5.2 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   ├── trellis_2_texture_vae_bf16.safetensors
│   │   └── trellis_2_shape_vae_bf16.safetensors
│   ├── 📂 clip_vision/
│   │   └── dino_v3_L_naf_fp32.safetensors
│   ├── 📂 background_removal/
│   │   └── birefnet.safetensors
│   └── 📂 diffusion_models/
│       └── pixal3d_multiview_int8_convrot.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
