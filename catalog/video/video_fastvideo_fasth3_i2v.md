# FastVideo FastH3: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_fastvideo_fasth3_i2v-1.webp" width="360" alt="FastVideo FastH3: Image to Video video_fastvideo_fasth3_i2v-1.webp">

> Generate video with synchronized native audio from a single still image using MiniMax H3 and the FastH3 8-step checkpoint. One image produces one video output with matching voice, sound effects, and music in a single pass. Ideal for animating portraits, bringing product shots to life, and quick social media clips.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_fastvideo_fasth3_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_fastvideo_fasth3_i2v.json)

## Details

| | |
|---|---|
| Name | `video_fastvideo_fasth3_i2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | MiniMax H3 |
| Tags | Image to Video, Int8 |
| Type | open source |
| Date | 2026-09-15 |
| Author | ComfyUI |
| Download size | 42.0 GB |
| Min ComfyUI version | 0.36.0 |
| Usage | 2284 |
| Nodes | 24 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #136 | image | red_line_barrier.png |
| output | `SaveVideo` #92 | video | video_fastvideo_fasth3_i2v.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `fastvideo_fasth3_8step_v2_pruned_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/FastVideo/FastVideo-FastH3-Comfy/resolve/main/diffusion_models/fastvideo_fasth3_8step_v2_pruned_int8_convrot.safetensors) |
| `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) |
| `minimax_h3_audio_vae_fp32.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) |
| `minimax_h3_video_vae_int8_convrot.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) |

## Subgraphs

- **First Last Frame to Video (FastVideo FastH3)** (18 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `VAELoader` | 2 | comfy-core |
| `BasicGuider` | 1 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `BlockSparseAttention` | 1 |  |
| `CLIPLoader` | 1 | comfy-core |
| `ComfyMathExpression` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageScaleToTotalPixels` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `LoadImage` | 1 |  |
| `MiniMaxH3ImageToVideo` | 1 | comfy-core |
| `MiniMaxH3SigmaShift` | 1 |  |
| `ModelAttentionBackend` | 1 |  |
| `PrimitiveFloat` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEDecodeAudio` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Fast Video FastH3</summary>

This template runs the **Image to Video** task (`MiniMaxH3ImageToVideo` node) with the [FastVideo FastH3 8-Step V2](https://huggingface.co/FastVideo/FastVideo-FastH3-8-Step-V2) checkpoint, a DMD2-distilled model that generates synchronized video and audio in **8 sampling steps** instead of the base model's full schedule. It covers both:

- **t2va** (text-to-video), when no images are connected
- **fl2va** (first/last-frame image-to-video), when `first_frame` and/or `last_frame` are connected

**Checkpoint repo**: [FastVideo/FastVideo-FastH3-Comfy](https://huggingface.co/FastVideo/FastVideo-FastH3-Comfy)

**Scope**: this distilled checkpoint supports t2va and fl2va only. Ref2VA (multi-reference conditioning) was not distilled; use the base MiniMax H3 model for reference-based tasks.

**Key inputs**

- **first_frame / last_frame**: optional keyframes; the model generates the motion between them
- **prompt**: describe the shots, motion, and the accompanying audio (dialogue, SFX, music) in one block
- **width / height**: set via Resolution Selector. H3's native canvas is a 768px short edge, capped at 768x1344 pixels, rounded to a multiple of 32
- **duration (seconds)**: converted to a valid frame `length` by the Math Expression node, snapping up to the model's 17-frame-per-block (17k+5) grid at 24fps

</details>

<details><summary>Note: Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Input Asset

- [red_line_barrier.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/red_line_barrier.png)

## Model Links

- [Hugging Face:Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)

### Alternative Repos

- [ModelScope:Comfy-Org/MiniMax-H3](https://modelscope.cn/models/Comfy-Org/MiniMax-H3)

**vae**

- [minimax_h3_video_vae_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) (2.62 GB)
- [minimax_h3_audio_vae_fp32.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) (577.2 MB)

**diffusion_models**

- [fastvideo_fasth3_8step_v2_pruned_int8_convrot.safetensors](https://huggingface.co/FastVideo/FastVideo-FastH3-Comfy/resolve/main/diffusion_models/fastvideo_fasth3_8step_v2_pruned_int8_convrot.safetensors) (20.61 GB)

**text_encoders**

- [qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) (14.61 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   ├── minimax_h3_video_vae_int8_convrot.safetensors
│   │   └── minimax_h3_audio_vae_fp32.safetensors
│   ├── 📂 diffusion_models/
│   │   └── fastvideo_fasth3_8step_v2_pruned_int8_convrot.safetensors
│   └── 📂 text_encoders/
│       └── qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
