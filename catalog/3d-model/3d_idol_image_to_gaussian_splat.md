# Idol: Image to Gaussian Splat

[← 3D Model](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=3d_idol_image_to_gaussian_splat)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_idol_image_to_gaussian_splat-1.webp" width="360" alt="Idol: Image to Gaussian Splat 3d_idol_image_to_gaussian_splat-1.webp">

> Turn a single image into a 3D Gaussian splat with Idol, Comfy-Org's fine-tune of TripoSplat: BiRefNet removes the backdrop, DINOv3 and the Flux2 VAE encode the view, and one pass decodes a 262k-point splat. Exports a .spz splat, an orbit preview and an experimental .glb mesh. Best on stylized characters and props.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/3d_idol_image_to_gaussian_splat.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/3d_idol_image_to_gaussian_splat.json)

## Details

| | |
|---|---|
| Name | `3d_idol_image_to_gaussian_splat` |
| Category | Foundation › 3D Model |
| Output | 3d |
| Models | Idol, TripoSplat |
| Tags | 3D, Image to 3D |
| Type | open source |
| Date | 2026-11-03 |
| Author | ComfyUI |
| Download size | 3.5 GB |
| Min ComfyUI version | 0.23.0 |
| Usage | 210 |
| Nodes | 28 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #99 | image | polar_bear_bass_player.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `birefnet.safetensors` | `background_removal` | [link](https://huggingface.co/Comfy-Org/BiRefNet/resolve/main/background_removal/birefnet.safetensors) |
| `dino_v3_vit_h_bf16.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Idol/resolve/main/clip_vision/dino_v3_vit_h_bf16.safetensors) |
| `idol_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Idol/resolve/main/diffusion_models/idol_fp16.safetensors) |
| `flux2-vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Idol/resolve/main/vae/flux2-vae.safetensors) |
| `idol_decoder_fp16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Idol/resolve/main/vae/idol_decoder_fp16.safetensors) |

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

<details><summary>Note: Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

**Paper:** [TripoSplat on arXiv](https://arxiv.org/abs/2605.16355)

## Model Links

- [Hugging Face:Comfy-Org/Idol](https://huggingface.co/Comfy-Org/Idol)
- [Hugging Face:speridlabs/idol](https://huggingface.co/speridlabs/idol)
- [Hugging Face:Comfy-Org/BiRefNet](https://huggingface.co/Comfy-Org/BiRefNet)

### Alternative Repos

- [ModelScope:Comfy-Org/Idol](https://modelscope.cn/models/Comfy-Org/Idol)
- [ModelScope:Comfy-Org/BiRefNet](https://modelscope.cn/models/Comfy-Org/BiRefNet)

Idol is a fine-tuned TripoSplat released by Comfy-Org; it runs on the same TripoSplat nodes, so only the checkpoints below change.

**background_removal**

- [birefnet.safetensors](https://huggingface.co/Comfy-Org/BiRefNet/resolve/main/background_removal/birefnet.safetensors) (423.9 MB)

**diffusion_models**

- [idol_fp16.safetensors](https://huggingface.co/Comfy-Org/Idol/resolve/main/diffusion_models/idol_fp16.safetensors) (706.8 MB)

**clip_vision**

- [dino_v3_vit_h_bf16.safetensors](https://huggingface.co/Comfy-Org/Idol/resolve/main/clip_vision/dino_v3_vit_h_bf16.safetensors) (1.57 GB)

**vae**

- [idol_decoder_fp16.safetensors](https://huggingface.co/Comfy-Org/Idol/resolve/main/vae/idol_decoder_fp16.safetensors) (549.5 MB)
- [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/Idol/resolve/main/vae/flux2-vae.safetensors) (320.6 MB)

**Total**: 3.52 GB

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 background_removal/
│   │   └── birefnet.safetensors
│   ├── 📂 diffusion_models/
│   │   └── idol_fp16.safetensors
│   ├── 📂 clip_vision/
│   │   └── dino_v3_vit_h_bf16.safetensors
│   └── 📂 vae/
│       ├── idol_decoder_fp16.safetensors
│       └── flux2-vae.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: Idol</summary>

## Idol

Single 2D image → 3D Gaussian splat. Idol is Comfy-Org's fine-tune of TripoSplat: same nodes, sharper read on stylized characters and props. Preview, export, or drop into game / AR / VR pipelines.

- Model: [Comfy-Org/Idol](https://huggingface.co/Comfy-Org/Idol)
- Original: [speridlabs/idol](https://huggingface.co/speridlabs/idol)
- Base: [VAST-AI-Research/TripoSplat](https://github.com/VAST-AI-Research/TripoSplat) · [arXiv:2605.16355](https://arxiv.org/abs/2605.16355)

## Quick Start

1. Load a single subject on a clean background in **LoadImage**
2. Tune **Image to Gaussian Splat** subgraph (background removal, gaussians, seed)
3. Queue — all three branches are active: orbit video, `.spz` splat, and `.glb` mesh

## Subgraph Settings

| Setting | Effect |
|---------|--------|
| `auto_remove_background` | BiRefNet cuts the backdrop before generation. Turn off if the image already has alpha. |
| `num_gaussians` | Final point count (rounded to ×32). **262144** matches the octree density; higher oversamples existing points — denser, not more detailed, and costs VRAM/time. |
| `seed` | Fixed at 46 in this example — change it for variations. |
| Model selectors | Idol checkpoints (`idol_fp16`, `idol_decoder_fp16`, `dino_v3_vit_h_bf16`). Swap in the stock TripoSplat files to compare. |
| `enable_preview` | Shows the sampling preview while the splat decodes. |

## Output Branches

| Branch | Status | Output |
|--------|--------|--------|
| **Create Video** | active | Orbit preview (1024², 75 frames, 25 fps) |
| **Create 3D Model (SPZ)** | active | 3D Gaussian splat (`.spz`, 262144 points) |
| **Create 3D Model (GLB)** | active | Mesh export (`.glb`, SplatToMesh at res 384 — heavy, several million triangles) |

## Known Limits

One view in, one view out: the front reads well, the sides and back are inferred — thin or high-frequency parts (strings, rails, fur strands) thin out or pick up colour from the removed backdrop.

</details>
