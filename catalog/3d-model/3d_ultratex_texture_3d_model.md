# UltraTex: Texture a 3D Model

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_ultratex_texture_3d_model-1.webp" width="360" alt="UltraTex: Texture a 3D Model 3d_ultratex_texture_3d_model-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_ultratex_texture_3d_model-2.webp" width="360" alt="UltraTex: Texture a 3D Model 3d_ultratex_texture_3d_model-2.webp">

> Texture an untextured mesh from a single reference image. UltraTex renders the mesh into six world-normal views, paints albedo and metallic/roughness with two UltraTex LoRA passes on FLUX.2 Klein 9B, then bakes the result onto the mesh UVs and exports a PBR GLB with its PNG maps.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_ultratex_texture_3d_model.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/3d_ultratex_texture_3d_model.json)

## Details

| | |
|---|---|
| Name | `3d_ultratex_texture_3d_model` |
| Category | Foundation › 3D Model |
| Media type | image |
| Models | UltraTex, FLUX.2 Klein |
| Tags | 3D, 3D Texturing |
| Type | open source |
| Date | 2026-11-22 |
| Author | ComfyUI |
| Download size | 12.3 GB |
| Min ComfyUI version | 0.46.0 |
| Usage | 0 |
| Nodes | 36 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #14 | image | sir_frog.png |
| input | `Load3DAdvanced` #234 | 3d | sir_frog.obj |
| output | `SaveGLB` #81 | 3d | 3d/ultratex_texture_3d_model.glb |
| output | `SaveImageAdvanced` #228 | image | 3d/ultratex_texture_3d_model_albedo.png |
| output | `SaveImageAdvanced` #230 | image | 3d/ultratex_texture_3d_model_roughness.png |
| output | `SaveImageAdvanced` #231 | image | 3d/ultratex_texture_3d_model_metallic.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `birefnet.safetensors` | `background_removal` | [link](https://huggingface.co/Comfy-Org/BiRefNet/resolve/main/background_removal/birefnet.safetensors) |
| `flux-2-klein-base-9b_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/UltraTex/resolve/main/diffusion_models/flux-2-klein-base-9b_int8_convrot.safetensors) |
| `flux-2-klein-9b_empty_prompt.safetensors` | `embeddings` | [link](https://huggingface.co/Comfy-Org/UltraTex/resolve/main/embeddings/flux-2-klein-9b_empty_prompt.safetensors) |
| `flux-2-klein-9b_distill_lora_avg_rank_345_bf16.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/UltraTex/resolve/main/loras/flux-2-klein-9b_distill_lora_avg_rank_345_bf16.safetensors) |
| `ultratex_flux2_klein_9b_albedo_lora_bf16.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/UltraTex/resolve/main/loras/ultratex_flux2_klein_9b_albedo_lora_bf16.safetensors) |
| `ultratex_flux2_klein_9b_metallic_roughness_lora_bf16.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/UltraTex/resolve/main/loras/ultratex_flux2_klein_9b_metallic_roughness_lora_bf16.safetensors) |
| `ultratex_flux2_vae_fp32.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/UltraTex/resolve/main/vae/ultratex_flux2_vae_fp32.safetensors) |

## Subgraphs

- **Control Settings** (2 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoraLoaderModelOnly` | 3 |  |
| `SaveImageAdvanced` | 3 |  |
| `BakeTextureFromViews` | 2 |  |
| `KSampler` | 2 |  |
| `MarkdownNote` | 2 |  |
| `MaskPreview` | 2 |  |
| `PrimitiveInt` | 2 |  |
| `VAEDecode` | 2 |  |
| `ApplyTextureToMesh` | 1 |  |
| `BlockSparseAttention` | 1 |  |
| `ConditioningLoader` | 1 |  |
| `CreateCameraOrbit` | 1 |  |
| `EmptyFlux2LatentImage` | 1 |  |
| `Get3DComponents` | 1 |  |
| `Load3DAdvanced` | 1 |  |
| `LoadBackgroundRemovalModel` | 1 |  |
| `LoadImage` | 1 |  |
| `PreviewImage` | 1 |  |
| `RemoveBackground` | 1 |  |
| `RenderMesh` | 1 |  |
| `ResizeAndPadImage` | 1 |  |
| `SaveGLB` | 1 |  |
| `SplitImageChannels` | 1 |  |
| `UltraTexConditioning` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Model Links</summary>

**Paper:** [UltraTex on arXiv](https://arxiv.org/abs/2609.23169) · [Code and project page](https://github.com/yiboz2001/UltraTex)

## Model Links

- [Hugging Face:Comfy-Org/UltraTex](https://huggingface.co/Comfy-Org/UltraTex)
- [Hugging Face:Comfy-Org/BiRefNet](https://huggingface.co/Comfy-Org/BiRefNet) (background removal of the reference image)
- License: [FLUX Non-Commercial License](https://huggingface.co/black-forest-labs/FLUX.2-klein-9B/blob/main/LICENSE.md)

UltraTex (SIGGRAPH Asia 2026) is a 2K multi-view texturing framework. This graph runs it on the FLUX.2 Klein base 9B backbone: the UltraTex LoRAs repaint that model into a texture generator, and the UltraTex VAE is the foreground-aware decoder that keeps the 2K views clean.

### Alternative Repos

- [ModelScope:Comfy-Org/UltraTex](https://modelscope.cn/models/Comfy-Org/UltraTex)
- [ModelScope:Comfy-Org/BiRefNet](https://modelscope.cn/models/Comfy-Org/BiRefNet)

**diffusion_models**

- [flux-2-klein-base-9b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/UltraTex/resolve/main/diffusion_models/flux-2-klein-base-9b_int8_convrot.safetensors) - 9.44 GB, the checkpoint this graph loads
- [flux-2-klein-base-9b_bf16.safetensors](https://huggingface.co/Comfy-Org/UltraTex/resolve/main/diffusion_models/flux-2-klein-base-9b_bf16.safetensors) - 18.16 GB, full precision

**loras**

- [flux-2-klein-9b_distill_lora_avg_rank_345_bf16.safetensors](https://huggingface.co/Comfy-Org/UltraTex/resolve/main/loras/flux-2-klein-9b_distill_lora_avg_rank_345_bf16.safetensors) - 1.96 GB, distillation LoRA, `LoraLoaderModelOnly` at strength 0.5
- [ultratex_flux2_klein_9b_albedo_lora_bf16.safetensors](https://huggingface.co/Comfy-Org/UltraTex/resolve/main/loras/ultratex_flux2_klein_9b_albedo_lora_bf16.safetensors) - 478 MB, albedo LoRA, strength 1.0, stacked on the distillation LoRA
- [ultratex_flux2_klein_9b_metallic_roughness_lora_bf16.safetensors](https://huggingface.co/Comfy-Org/UltraTex/resolve/main/loras/ultratex_flux2_klein_9b_metallic_roughness_lora_bf16.safetensors) - 478 MB, metallic/roughness LoRA, strength 1.0, applied to the base model without the distillation LoRA

**embeddings**

- [flux-2-klein-9b_empty_prompt.safetensors](https://huggingface.co/Comfy-Org/UltraTex/resolve/main/embeddings/flux-2-klein-9b_empty_prompt.safetensors) - 25 MB, pre-encoded empty prompt read by `Load Conditioning`; the graph loads no text encoder

**vae**

- [ultratex_flux2_vae_fp32.safetensors](https://huggingface.co/Comfy-Org/UltraTex/resolve/main/vae/ultratex_flux2_vae_fp32.safetensors) - 336 MB, the UltraTex VAE: encodes the normal views and the reference, and decodes the generated views

**background_removal**

- [birefnet.safetensors](https://huggingface.co/Comfy-Org/BiRefNet/resolve/main/background_removal/birefnet.safetensors) - 444 MB, masks the reference image

**Disk footprint**: the graph as shipped needs **13.16 GB**. Swapping the checkpoint to `bf16` brings it to **21.87 GB**.

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── flux-2-klein-base-9b_int8_convrot.safetensors                      9.44 GB
│   ├── 📂 loras/
│   │   ├── flux-2-klein-9b_distill_lora_avg_rank_345_bf16.safetensors         1.96 GB
│   │   ├── ultratex_flux2_klein_9b_albedo_lora_bf16.safetensors               478 MB
│   │   └── ultratex_flux2_klein_9b_metallic_roughness_lora_bf16.safetensors   478 MB
│   ├── 📂 embeddings/
│   │   └── flux-2-klein-9b_empty_prompt.safetensors                           25 MB
│   ├── 📂 vae/
│   │   └── ultratex_flux2_vae_fp32.safetensors                                336 MB
│   └── 📂 background_removal/
│       └── birefnet.safetensors                                               444 MB
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: UltraTex</summary>

## UltraTex

Texture an untextured mesh from one reference image. The mesh is rendered as six world-normal views, a FLUX.2 Klein 9B model wearing the UltraTex LoRAs turns those views plus the reference into 1024 × 1024 texture views, and the views are baked onto the mesh UVs: albedo in one pass, packed metallic/roughness in another. Output: a PBR GLB plus the PNG maps.

**Input Assets**
- [sir_frog.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/sir_frog.png): the reference, i.e. how the object should look
- [sir_frog.obj](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/sir_frog.obj): the mesh, opened in **Load 3D (Advanced)**

### Chain

`Load 3D (Advanced)` -> `Create Camera Orbit` -> `Render Mesh` (world normal, 6 views) -> `UltraTex Conditioning` -> `KSampler` albedo / `KSampler` metallic and roughness -> `Bake Texture From Views` -> `Apply Texture to Mesh` -> `Save 3D Model`. The reference side is `Load Image` -> `Resize And Pad Image` (1024, white) -> `Remove Background`.

### What to change

- **Load 3D (Advanced)**: your mesh and the camera the front view is taken from; the bake reuses that rig.
- **Load Image**: the reference seen from that camera's side. It lands on the front view, so keep one object in one orientation.
- `Rendered Mesh Resolution` (1024) sizes the renders and the latent; `Texture Resolution` (4096) sizes the baked maps.
- Albedo pass: 4 steps, seed 1, distillation LoRA 0.5 under albedo LoRA 1.0. Metallic/roughness pass: 8 steps, seed 4, no distillation LoRA.
- `fill_unseen` on grows colour into texels no view saw; off keeps the mesh's own texture there.
- `Create Camera Orbit` is pinned to four side views plus top and bottom: six views, which is the batch `EmptyFlux2LatentImage` is set to. Changing the rig means changing that batch size to match.

### Before you queue

- The mesh needs UVs already: bake and apply reuse them, there is no unwrap step.
- Seeds change surface detail only; the silhouette comes from the mesh.

</details>
