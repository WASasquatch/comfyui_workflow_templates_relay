# Video Upscale: SeedVR2 3B Int8

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_seedvr2_3b_int8_upscale_video-1.webp" width="360" alt="Video Upscale: SeedVR2 3B Int8 utility_seedvr2_3b_int8_upscale_video-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_seedvr2_3b_int8_upscale_video-2.webp" width="360" alt="Video Upscale: SeedVR2 3B Int8 utility_seedvr2_3b_int8_upscale_video-2.webp">

> Upscale and restore video footage using SeedVR2 3B Int8, a one-step diffusion model that enhances resolution while maintaining temporal consistency across frames. This workflow takes one degraded video as input and outputs a single high-resolution, restored video. Ideal for restoring old or degraded footage, upscaling low-resolution videos, and enhancing archival media.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_seedvr2_3b_int8_upscale_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_seedvr2_3b_int8_upscale_video.json)

## Details

| | |
|---|---|
| Name | `utility_seedvr2_3b_int8_upscale_video` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | SeedVR2 |
| Tags | Video Upscale, Int8 |
| Type | open source |
| Date | 2026-07-14 |
| Author | ComfyUI |
| Download size | 3.7 GB |
| Min ComfyUI version | 0.28.0 |
| Usage | 516 |
| Nodes | 22 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #73 | video | grainy_perfume_shot_crf32.mp4 |
| output | `SaveVideo` #76 | video | utility_seedvr2_3b_int8_upscale_video.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `seedvr2_3b_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/SeedVR2/resolve/main/diffusion_models/seedvr2_3b_int8_convrot.safetensors) |
| `seedvr2_ema_vae_fp16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/SeedVR2/resolve/main/vae/seedvr2_ema_vae_fp16.safetensors) |

## Subgraphs

- **Upscale Video (SeedVR2 3B Int8)** (18 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 | comfy-core |
| `MarkdownNote` | 2 |  |
| `CreateVideo` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 |  |
| `ResizeImageMaskNode` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `SeedVR2Conditioning` | 1 | comfy-core |
| `SeedVR2PostProcessing` | 1 | comfy-core |
| `SeedVR2Preprocess` | 1 | comfy-core |
| `SeedVR2TemporalChunk` | 1 | comfy-core |
| `SeedVR2TemporalMerge` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecodeTiled` | 1 | comfy-core |
| `VAEEncodeTiled` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `Video Slice` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/SeedVR2](https://huggingface.co/Comfy-Org/SeedVR2)

### Alternative Repos

- [ModelScope:Comfy-Org/SeedVR2](https://modelscope.cn/models/Comfy-Org/SeedVR2)

**vae**

- [seedvr2_ema_vae_fp16.safetensors](https://huggingface.co/Comfy-Org/SeedVR2/resolve/main/vae/seedvr2_ema_vae_fp16.safetensors) (478.1 MB)

**diffusion_models**

- [seedvr2_3b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/SeedVR2/resolve/main/diffusion_models/seedvr2_3b_int8_convrot.safetensors) (3.22 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   └── seedvr2_ema_vae_fp16.safetensors
│   └── 📂 diffusion_models/
│       └── seedvr2_3b_int8_convrot.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: SeedVR2</summary>

## SeedVR2

One-step video restoration / upscale (ICLR 2026). This workflow uses the **3B Int8** model for video upscaling.

- Project: [SeedVR2](https://iceclear.github.io/projects/seedvr2/)
- ComfyUI native support: [PR #14424](https://github.com/Comfy-Org/ComfyUI/pull/14424)

### Subgraph parameters

- **trim_video**: enable to cut a segment before upscaling
- **trim_start_time / duration**: trim start (seconds) and length
- **scale_multiplier**: upscale factor (default `2`)
- **seed / sampler / scheduler / denoise**: sampling controls; `denoise=1` means full restore
- **color_correction_method**: optional color match to original (default `none`)
- **unet_name / vae_name**: model files to load

### Tip: long videos

If the input is too long, turn on **trim_video**, upscale in shorter segments, then merge them. This helps avoid OOM / slowdowns on long clips.

</details>
