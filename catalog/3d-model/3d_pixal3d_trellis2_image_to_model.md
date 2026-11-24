# Pixal3D & TRELLIS.2: Image to Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=3d_pixal3d_trellis2_image_to_model)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_pixal3d_trellis2_image_to_model-1.webp" width="360" alt="Pixal3D & TRELLIS.2: Image to Model 3d_pixal3d_trellis2_image_to_model-1.webp">

> Upload a single image. Generate a high-fidelity 3D model with PBR textures using either Pixal3D or TRELLIS.2, toggled by a single switch. Both pipelines share the same DINOv3 encoder and shape/texture VAEs; Pixal3D adds MoGe camera estimation for pixel-aligned geometry. Includes background removal and a complete mesh post-processing pipeline: remesh, decimate, UV unwrap, and texture baking.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_pixal3d_trellis2_image_to_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/3d_pixal3d_trellis2_image_to_model.json)

## Details

| | |
|---|---|
| Name | `3d_pixal3d_trellis2_image_to_model` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Pixal3D, TRELLIS.2 |
| Tags | 3D, Image to 3D, Int8 |
| Type | open source |
| Date | 2026-08-25 |
| Author | ComfyUI |
| Download size | 14.3 GB |
| Min ComfyUI version | 0.42.0 |
| Usage | 818 |
| Nodes | 66 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #122 | image | viking_wolf_rune_axe.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `birefnet.safetensors` | `background_removal` | [link](https://huggingface.co/Comfy-Org/BiRefNet/resolve/main/background_removal/birefnet.safetensors) |
| `dino_v3_L_naf_fp32.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/clip_vision/dino_v3_L_naf_fp32.safetensors) |
| `pixal3d_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/diffusion_models/pixal3d_int8_convrot.safetensors) |
| `trellis_2_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/TRELLIS.2/resolve/main/diffusion_models/trellis_2_int8_convrot.safetensors) |
| `moge_2_vitl_normal_fp16.safetensors` | `geometry_estimation` | [link](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_2_vitl_normal_fp16.safetensors) |
| `trellis_2_shape_vae_bf16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/vae/trellis_2_shape_vae_bf16.safetensors) |
| `trellis_2_texture_vae_bf16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/vae/trellis_2_texture_vae_bf16.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewImage` | 7 | comfy-core |
| `ComfySwitchNode` | 4 | comfy-core |
| `KSampler` | 4 | comfy-core |
| `MeshToFile3D` | 3 | comfy-core |
| `CFGOverride` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `MeshSmoothNormals` | 2 | comfy-core |
| `Preview3DAdvanced` | 2 | comfy-core |
| `RescaleCFG` | 2 | comfy-core |
| `UNETLoader` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `ApplyTextureToMesh` | 1 | comfy-core |
| `BakeAmbientOcclusion` | 1 | comfy-core |
| `BakeNormalMapFromMesh` | 1 | comfy-core |
| `BakeTextureFromVoxel` | 1 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `DecimateMesh` | 1 | comfy-core |
| `EmptyTrellis2LatentStructure` | 1 | comfy-core |
| `GetMeshInfo` | 1 | comfy-core |
| `ImageCropToMask` | 1 | comfy-core |
| `LoadBackgroundRemovalModel` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadMoGeModel` | 1 | comfy-core |
| `MaskPreview` | 1 | comfy-core |
| `ModelSamplingSD3` | 1 | comfy-core |
| `MoGeGeometryToFOV` | 1 | comfy-core |
| `MoGeInference` | 1 | comfy-core |
| `Note` | 1 |  |
| `PaintMesh` | 1 | comfy-core |
| `Pixal3DConditioning` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `PrimitiveInt` | 1 | comfy-core |
| `RemeshMesh` | 1 | comfy-core |
| `RemoveBackground` | 1 | comfy-core |
| `RenderUVAtlas` | 1 | comfy-core |
| `Save3DAdvanced` | 1 | comfy-core |
| `Trellis2Conditioning` | 1 | comfy-core |
| `Trellis2ShapeStage` | 1 | comfy-core |
| `Trellis2TextureStage` | 1 | comfy-core |
| `Trellis2UpsampleStage` | 1 | comfy-core |
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

<details><summary>Note: Model Links and Input Asset</summary>

**Input Assets** 

- [viking_wolf_rune_axe.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/viking_wolf_rune_axe.png) — required workflow input (`input/viking_wolf_rune_axe.png`)

## Model Links

- [Hugging Face:Comfy-Org/Pixal3D](https://huggingface.co/Comfy-Org/Pixal3D)
- [Hugging Face:Comfy-Org/MoGe](https://huggingface.co/Comfy-Org/MoGe)
- [Hugging Face:Comfy-Org/BiRefNet](https://huggingface.co/Comfy-Org/BiRefNet)
- [Hugging Face:Comfy-Org/TRELLIS.2](https://huggingface.co/Comfy-Org/TRELLIS.2)

### Alternative Repos

- [ModelScope:Comfy-Org/Pixal3D](https://modelscope.cn/models/Comfy-Org/Pixal3D)
- [ModelScope:Comfy-Org/MoGe](https://modelscope.cn/models/Comfy-Org/MoGe)
- [ModelScope:Comfy-Org/BiRefNet](https://modelscope.cn/models/Comfy-Org/BiRefNet)
- [ModelScope:Comfy-Org/TRELLIS.2](https://modelscope.cn/models/Comfy-Org/TRELLIS.2)

**vae**

- [trellis_2_texture_vae_bf16.safetensors](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/vae/trellis_2_texture_vae_bf16.safetensors) (904.5 MB)
- [trellis_2_shape_vae_bf16.safetensors](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/vae/trellis_2_shape_vae_bf16.safetensors) (1.02 GB)

**clip_vision**

- [dino_v3_L_naf_fp32.safetensors](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/clip_vision/dino_v3_L_naf_fp32.safetensors) (1.13 GB)

**geometry_estimation**

- [moge_2_vitl_normal_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_2_vitl_normal_fp16.safetensors) (631.2 MB)

**background_removal**

- [birefnet.safetensors](https://huggingface.co/Comfy-Org/BiRefNet/resolve/main/background_removal/birefnet.safetensors) (423.9 MB)

**diffusion_models**

- [trellis_2_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/TRELLIS.2/resolve/main/diffusion_models/trellis_2_int8_convrot.safetensors) (4.89 GB)
- [pixal3d_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Pixal3D/resolve/main/diffusion_models/pixal3d_int8_convrot.safetensors) (5.2 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   ├── trellis_2_texture_vae_bf16.safetensors
│   │   └── trellis_2_shape_vae_bf16.safetensors
│   ├── 📂 clip_vision/
│   │   └── dino_v3_L_naf_fp32.safetensors
│   ├── 📂 geometry_estimation/
│   │   └── moge_2_vitl_normal_fp16.safetensors
│   ├── 📂 background_removal/
│   │   └── birefnet.safetensors
│   └── 📂 diffusion_models/
│       ├── trellis_2_int8_convrot.safetensors
│       └── pixal3d_int8_convrot.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>MarkdownNote</summary>

Set to `false` to use Pixal3D

Set to `true` to use Trellis.2

</details>
