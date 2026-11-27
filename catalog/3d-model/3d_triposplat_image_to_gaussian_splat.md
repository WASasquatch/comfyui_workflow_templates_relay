# TripoSplat: Image to Gaussian Splat

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=3d_triposplat_image_to_gaussian_splat)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_triposplat_image_to_gaussian_splat-1.webp" width="360" alt="TripoSplat: Image to Gaussian Splat 3d_triposplat_image_to_gaussian_splat-1.webp">

> Upload a single 2D image. Generate a high-quality 3D Gaussian splat representation with controllable density and budget for rendering.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_triposplat_image_to_gaussian_splat.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/3d_triposplat_image_to_gaussian_splat.json)

## Details

| | |
|---|---|
| Name | `3d_triposplat_image_to_gaussian_splat` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | TripoSplat |
| Tags | 3D, Image to 3D |
| Type | open source |
| Date | 2026-06-02 |
| Author | ComfyUI |
| Download size | 3.7 GB |
| Min ComfyUI version | 0.23.0 |
| Usage | 125 |
| Nodes | 28 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #99 | image | white-hotel-on-rocky-island.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `birefnet.safetensors` | `background_removal` | [link](https://huggingface.co/Comfy-Org/BiRefNet/resolve/main/background_removal/birefnet.safetensors) |
| `dino_v3_vit_h.safetensors` | `clip_vision` | [link](https://huggingface.co/VAST-AI/TripoSplat/resolve/main/clip_vision/dino_v3_vit_h.safetensors) |
| `triposplat_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/VAST-AI/TripoSplat/resolve/main/diffusion_models/triposplat_fp16.safetensors) |
| `flux2-vae.safetensors` | `vae` | [link](https://huggingface.co/VAST-AI/TripoSplat/resolve/main/vae/flux2-vae.safetensors) |
| `triposplat_vae_decoder_fp16.safetensors` | `vae` | [link](https://huggingface.co/VAST-AI/TripoSplat/resolve/main/vae/triposplat_vae_decoder_fp16.safetensors) |

## Subgraphs

- **Remove Background (BiRefNet)** (4 nodes)
- **Image to Gaussian Splat (TripoSplat)** (14 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 2 | comfy-core |
| `InvertMask` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `SaveGLB` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `CreateCameraInfo` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `JoinImageWithAlpha` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadBackgroundRemovalModel` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `RemoveBackground` | 1 | comfy-core |
| `RenderSplat` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `SplatToFile3D` | 1 | comfy-core |
| `SplatToMesh` | 1 | comfy-core |
| `TripoSplatConditioning` | 1 | comfy-core |
| `TripoSplatPreprocessImage` | 1 | comfy-core |
| `TripoSplatSamplingPreview` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecodeTripoSplat` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Model Link</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

**Paper:** [TripoSplat on arXiv](https://arxiv.org/abs/2605.16355)

## Model Links

- [Hugging Face:Comfy-Org/BiRefNet](https://huggingface.co/Comfy-Org/BiRefNet)
- [ModelScope:Comfy-Org/BiRefNet](https://modelscope.cn/models/Comfy-Org/BiRefNet)

Model: [VAST-AI/TripoSplat](https://huggingface.co/VAST-AI/TripoSplat)

**background_removal**

- [birefnet.safetensors](https://huggingface.co/Comfy-Org/BiRefNet/resolve/main/background_removal/birefnet.safetensors) (423.9 MB)

**diffusion_models**

- [triposplat_fp16.safetensors](https://huggingface.co/VAST-AI/TripoSplat/resolve/main/diffusion_models/triposplat_fp16.safetensors) (706.8 MB)

**clip_vision**

- [dino_v3_vit_h.safetensors](https://huggingface.co/VAST-AI/TripoSplat/resolve/main/clip_vision/dino_v3_vit_h.safetensors) (1.57 GB)

**vae**

- [triposplat_vae_decoder_fp16.safetensors](https://huggingface.co/VAST-AI/TripoSplat/resolve/main/vae/triposplat_vae_decoder_fp16.safetensors) (549.5 MB)
- [flux2-vae.safetensors](https://huggingface.co/VAST-AI/TripoSplat/resolve/main/vae/flux2-vae.safetensors) (320.6 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 background_removal/
│   │   └── birefnet.safetensors
│   ├── 📂 diffusion_models/
│   │   └── triposplat_fp16.safetensors
│   ├── 📂 clip_vision/
│   │   └── dino_v3_vit_h.safetensors
│   └── 📂 vae/
│       ├── triposplat_vae_decoder_fp16.safetensors
│       └── flux2-vae.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: TripoSplat</summary>

## TripoSplat

Single 2D image → 3D Gaussian splat. Preview, export, or drop into game / AR / VR pipelines. Best on stylized objects.

- Github: [VAST-AI-Research/TripoSplat](https://github.com/VAST-AI-Research/TripoSplat)
- Paper: [arXiv:2605.16355](https://arxiv.org/abs/2605.16355)
- Model: [VAST-AI/TripoSplat](https://huggingface.co/VAST-AI/TripoSplat)
## Quick Start

1. Load image in **LoadImage**
2. Tune **Image to Gaussian Splat (TripoSplat)** subgraph
3. Queue — **Create Video** with an orbit preview and export an SPZ file
4. To export a GLB file select the bypassed nodes, press **Ctrl+B** to enable, then re-run

## Subgraph Settings

| Setting | Effect |
|---------|--------|
| `remove_background` | BiRefNet removes background before generation. Off if image is already clean/transparent. |
| `sampling_num_gaussians` (decode) | Final output count (rounded to ×32). **262144** = octree density. Higher oversamples existing points — denser, not more detail; costs more VRAM/time. |
| `seed` | Change for different variations. |
| Model selectors | Keep unless using custom checkpoints. |

## Output Branches

| Branch | Status | Output |
|--------|--------|--------|
| **Create Video** | active | Orbit preview video |
| **Create 3D Model (SPZ)** | active | 3D Gaussian splat (.spz) |
| **Create 3D Model (GLB)** | bypassed | Mesh export (.glb, experimental) — select nodes → **Ctrl+B** to enable |

</details>
