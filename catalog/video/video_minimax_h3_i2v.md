# MiniMax H3: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_minimax_h3_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_minimax_h3_i2v-1.webp" width="360" alt="MiniMax H3: Image to Video video_minimax_h3_i2v-1.webp">

> Turn a starting image into a short, high-quality video clip with MiniMax H3, a unified multimodal model that generates visuals and synchronized audio in a single pass. The workflow takes 1 input image and produces 1 video output, with optional text or reference media to steer motion, style, or sound. Ideal for rapid concept visualization, character-driven animation tests, and creating shareable social media clips with built-in sound design.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_minimax_h3_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_minimax_h3_i2v.json)

## Details

| | |
|---|---|
| Name | `video_minimax_h3_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | MiniMax H3 |
| Tags | Image to Video, Int8, Video |
| Type | open source |
| Date | 2026-08-02 |
| Author | ComfyUI |
| Download size | 41.4 GB |
| Min ComfyUI version | 0.30.0 |
| Usage | 19766 |
| Nodes | 29 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #114 | image | transparent_rgb_gaming_mouse.png |
| output | `SaveVideo` #92 | video | video_minimax_h3_i2v.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `minimax_h3_fl2va_pruned_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) |
| `minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Minimax-h3-Turbo/resolve/main/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors) |
| `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) |
| `minimax_h3_audio_vae_fp32.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) |
| `minimax_h3_video_vae_int8_convrot.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) |

## Subgraphs

- **Image to Video (MiniMax H3)** (21 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `ComfySwitchNode` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `BasicGuider` | 1 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `ComfyMathExpression` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageScaleToTotalPixels` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `MiniMaxH3ImageToVideo` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `PrimitiveFloat` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `ResolutionSelector` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEDecodeAudio` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: MiniMax H3</summary>

## MiniMax H3

[MiniMax H3](https://www.minimax.io/blog/minimax-h3) is MiniMax's general-purpose, omni-modal generation model. It jointly understands text, image, video, and audio, and generates video with **native stereo audio**: voice, sound effects, and music are modeled jointly in a single forward pass, not layered on afterward. Output is up to 2K resolution, 24fps, and up to about 15 seconds.

## About this workflow

This template runs the **Image to Video** task (`MiniMaxH3ImageToVideo` node), which covers both:

- **t2va** (text-to-video), when no images are connected
- **fl2va** (first/last-frame image-to-video), when `first_frame` and/or `last_frame` are connected

**Key inputs**

- **first_frame / last_frame**: optional keyframes; the model generates the motion between them
- **prompt**: describe the shots, motion, and the accompanying audio (dialogue, SFX, music) in one block
- **width / height**: set via Resolution Selector. H3's native canvas is a 768px short edge, capped at 768x1344 pixels, rounded to a multiple of 32
- **duration (seconds)**: converted to a valid frame `length` by the Math Expression node, snapping up to the model's 17-frame-per-block (17k+5) grid at 24fps

</details>

<details><summary>Note: Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)

### Alternative Repos

- [ModelScope:Comfy-Org/MiniMax-H3](https://modelscope.cn/models/Comfy-Org/MiniMax-H3)

**Input Assets**
- [transparent_rgb_gaming_mouse.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/transparent_rgb_gaming_mouse.png) — required workflow input (`input/transparent_rgb_gaming_mouse.png`)

**vae**

- [minimax_h3_video_vae_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) (2.62 GB)
- [minimax_h3_audio_vae_fp32.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) (577.2 MB)

**diffusion_models**

- [minimax_h3_fl2va_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) (19.53 GB)

**text_encoders**

- [qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) (14.61 GB)

**loras**

- 8 steps:  [minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors](https://huggingface.co/lightx2v/Minimax-h3-Turbo/resolve/main/minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors) (1.82 GB)
-  4 steps: [minimax_h3_fl2v_turbo_4step_v1.0_768p_comfyui_bf16.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/loras/minimax_h3_fl2v_turbo_4step_v1.0_768p_comfyui_bf16.safetensors) (1.82 GB)

**embeddings**

- [10 style embeddings](https://huggingface.co/Comfy-Org/MiniMax-H3/tree/main/embeddings) (`minimaxh3_*.safetensors`), for example `minimaxh3_art_is_explosion`

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   ├── minimax_h3_video_vae_int8_convrot.safetensors
│   │   └── minimax_h3_audio_vae_fp32.safetensors
│   ├── 📂 diffusion_models/
│   │   └── minimax_h3_fl2va_pruned_int8_convrot.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
│   ├── 📂 loras/
│   │   └── minimax_h3_fl2v_turbo_8step_v1.0_comfyui_bf16.safetensors
│   └── 📂 embeddings/
│       └── minimaxh3_art_is_explosion.safetensors
```

## Using Prompt Embeddings

Prompt embeddings (supported since [ComfyUI#15697](https://github.com/Comfy-Org/ComfyUI/pull/15697)) add reusable style tokens to your prompt. Download one or more embeddings from the folder above into `ComfyUI/models/embeddings/`, then reference one in the prompt text with the `embedding:` prefix and the filename without its extension, for example:

`embedding:minimaxh3_art_is_explosion`

Using an embedding is optional and the template runs fine without one.

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: Size Settings Reference</summary>

| megapixels | Aspect | Output (multiple=32) |
|---|---|---|
| 0.2 | 16:9 | 608 x 352 |
| 0.3 | 16:9 | 736 x 416 |
| 0.4 | 16:9 | 864 x 480 |
| 0.5 | 16:9 | 960 x 544 |
| 0.6 | 16:9 | 1056 x 608 |
| 0.7 | 16:9 | 1152 x 640 |
| 0.8 | 16:9 | 1216 x 672 |
| 0.9 | 16:9 | 1280 x 736 |
| 0.98 | 16:9 | 1344 x 768 (official 768p) |

</details>
