# Video Upscale: RelayVSR 2x

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_relayvsr_video_x2_upscale-1.webp" width="360" alt="Video Upscale: RelayVSR 2x utility_relayvsr_video_x2_upscale-1.webp">

> Upscale real footage 2x with RelayVSR: a large Wan-based model writes reference latents for sparse keyframes and a compact Flash decoder carries them across every frame, so a long clip is restored in one streaming pass at one sampling step. Output is exactly 2x the input at the source frame rate, with the audio track kept. Ideal as the finishing pass after a 480p-768p generation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_relayvsr_video_x2_upscale.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_relayvsr_video_x2_upscale.json)

## Details

| | |
|---|---|
| Name | `utility_relayvsr_video_x2_upscale` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | RelayVSR |
| Tags | Video Upscale, 2x, Restoration |
| Type | open source |
| Date | 2026-11-10 |
| Author | ComfyUI |
| Download size | 4.8 GB |
| Min ComfyUI version | 0.45.0 |
| Usage | 97 |
| Nodes | 13 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #1 | video | utility_relayvsr_video_x2_upscale_input.mp4 |
| output | `SaveVideo` #106 | video | utility_relayvsr_video_x2_upscale.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `relayvsr_x2_lightx2v_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/RelayVSR/resolve/main/diffusion_models/relayvsr_x2_lightx2v_int8_convrot.safetensors) |
| `relayvsr_flash_vae_x2_fp32.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/RelayVSR/resolve/main/vae/relayvsr_flash_vae_x2_fp32.safetensors) |

## Subgraphs

- **RelayVSR Video Upscaler** (7 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `CreateVideo` | 1 |  |
| `GetVideoComponents` | 1 |  |
| `KSampler` | 1 |  |
| `LoadVideo` | 1 |  |
| `RelayVSRConditioning` | 1 |  |
| `SaveVideo` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAELoader` | 1 |  |
| `Video Slice` | 1 |  |
| `VSRDecode` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Model links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Input Asset

- [utility_relayvsr_video_x2_upscale_input.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/utility_relayvsr_video_x2_upscale_input.mp4)

## Model Links

- [Hugging Face:Comfy-Org/RelayVSR](https://huggingface.co/Comfy-Org/RelayVSR)

### Alternative Repos

- [ModelScope:Comfy-Org/RelayVSR](https://modelscope.cn/models/Comfy-Org/RelayVSR)

**diffusion_models**

- [relayvsr_x2_lightx2v_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/RelayVSR/resolve/main/diffusion_models/relayvsr_x2_lightx2v_int8_convrot.safetensors) (4.81 GB)

**vae**

- [relayvsr_flash_vae_x2_fp32.safetensors](https://huggingface.co/Comfy-Org/RelayVSR/resolve/main/vae/relayvsr_flash_vae_x2_fp32.safetensors) (121.8 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── relayvsr_x2_lightx2v_int8_convrot.safetensors
│   └── 📂 vae/
│       └── relayvsr_flash_vae_x2_fp32.safetensors
```

## About this model

RelayVSR upscales real video in one step: a large Wan-based model paints reference latents for sparse keyframes and a light "Flash" decoder carries them across every frame, so a long clip is restored in a streaming pass. The 2x pair here was retrained by LightX2V for the step after H3 generation; native in ComfyUI since #17511.

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note</summary>

## How to use

**Load Video** → **RelayVSR Video Upscaler** (subgraph) → **Save Video**. Frame rate and audio pass through; only the picture is scaled, exactly 2x.

In the subgraph: `steps 1`, `cfg 1`, `euler` / `simple`, and a matching weight pair — `relayvsr_x2_lightx2v_int8_convrot` with `relayvsr_flash_vae_x2_fp32`. 

The factor comes from the checkpoint, not from a widget, and mixing x2 with x4 files fails. The big model writes a keyframe every 15 frames; `VSRDecode` expands them to every frame.

- For 4x, swap in `relayvsr_x4_int8_convrot` + `relayvsr_flash_vae_x4_fp32`. Nothing else changes.

</details>

<details><summary>MarkdownNote</summary>

If you get OOM while using this workflow, try to trim the input and split the whole process into several passes

</details>
