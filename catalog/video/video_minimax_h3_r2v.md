# MiniMax H3: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_minimax_h3_r2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_minimax_h3_r2v-1.webp" width="360" alt="MiniMax H3: Reference to Video video_minimax_h3_r2v-1.webp">

> Generate a new video by feeding MiniMax H3 a reference image, up to nine images, three videos, and three audio clips alongside a text prompt, letting the model match character identity, motion, camera, voice, or style from those sources while producing native stereo audio in a single pass. Output is a single MP4 video at up to 2K resolution and 24fps for roughly 15 seconds. Ideal for character-consistent animation, style-transfer video generation, and audio-synced content creation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_minimax_h3_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_minimax_h3_r2v.json)

## Details

| | |
|---|---|
| Name | `video_minimax_h3_r2v` |
| Category | Foundation › Video |
| Output | video |
| Models | MiniMax H3 |
| Tags | Reference to Video, Int8, Video |
| Type | open source |
| Date | 2026-08-02 |
| Author | ComfyUI |
| Download size | 41.4 GB |
| Min ComfyUI version | 0.30.0 |
| Usage | 5759 |
| Nodes | 29 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #137 | image | red_superboy_on_city_roof.png |
| input | `LoadImage` #139 | image | mecha_dragon_lightning.png |
| output | `SaveVideo` #92 | video | video_minimax_h3_r2v.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) |
| `minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/loras/minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors) |
| `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) |
| `minimax_h3_audio_vae_fp32.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) |
| `minimax_h3_video_vae_int8_convrot.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `ComfySwitchNode` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `BasicGuider` | 1 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `ComfyMathExpression` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `MiniMaxH3ReferenceToVideo` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `PrimitiveFloat` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |
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

**Input Assets**
- [red_superboy_on_city_roof.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/red_superboy_on_city_roof.png) — required workflow input (`input/red_superboy_on_city_roof.png`)
- [mecha_dragon_lightning.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/mecha_dragon_lightning.png) — required workflow input (`input/mecha_dragon_lightning.png`)

[MiniMax H3](https://www.minimax.io/blog/minimax-h3) is MiniMax's general-purpose, omni-modal generation model. It jointly understands text, image, video, and audio, and generates video with **native stereo audio**: voice, sound effects, and music are modeled jointly in a single forward pass, not layered on afterward. Output is up to 2K resolution, 24fps, and up to about 15 seconds.

## ComfyUI links
- [ComfyUI#15224](https://github.com/Comfy-Org/ComfyUI/pull/15224)
- [🤗 Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)

## About this workflow

This template runs the **reference-to-video (ref2va)** task using the `MiniMaxH3ReferenceToVideo` node. It takes any mix of reference images, videos, and standalone audio, and weaves them into the generation to lock in a character's identity, a style, a motion, a camera move, or a voice.

**Key inputs**

- **ref_images / ref_videos / ref_video_audios / ref_audios**: up to 9 reference images, 3 reference videos (each may carry its own paired soundtrack), and 3 standalone reference audio clips
- **prompt**: reference the inputs by tag, in the exact order they were connected, for example `<Picture 1>`, `<Video 1>`, `<Audio 1>`, then describe the target scene, motion, and audio
- **ref_image_size**: `match` scales references down to the generation's resolution (faster); `max` keeps up to a 2048px short edge for stronger identity fidelity, at the cost of speed since reference tokens ride along every sampling step
- **width / height**: set via Resolution Selector.
- **duration (seconds)**: converted to a valid frame `length` by the Math Expression node

**Sampling and decode**

- Sampler: `res_multistep`. `beta` or `normal` scheduler tends to outperform `simple` for reference-heavy prompts like this one
- The sampler's joint audio+video `LATENT` output feeds directly into both `VAEDecode` (video, `minimax_h3_video_vae_int8_convrot`) and `VAEDecodeAudio` (audio, `minimax_h3_audio_vae_fp32`); each decode node automatically pulls its own half out of the packed latent. `CreateVideo` then muxes the two into a single MP4 with synced sound
- The diffusion model here is `minimax_h3_ref2va_pruned_int8_convrot.safetensors`, a different set of weights from the `fl2va` model used by the t2v/i2v templates

Ref2va's output is very sensitive to prompt wording; matching the reference tags precisely and being explicit about which reference drives which part of the shot tends to work best.

</details>

<details><summary>Note: Model Links</summary>

## Model Links

- [Hugging Face:Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)

### Alternative Repos

- [ModelScope:Comfy-Org/MiniMax-H3](https://modelscope.cn/models/Comfy-Org/MiniMax-H3)

**vae**

- [minimax_h3_video_vae_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) (2.62 GB)
- [minimax_h3_audio_vae_fp32.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) (577.2 MB)

**diffusion_models**

- [minimax_h3_ref2va_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) (19.53 GB)

**text_encoders**

- [qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) (14.61 GB)

**loras**

- 4 steps: [minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/loras/minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors) (1.82 GB)

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
│   │   └── minimax_h3_ref2va_pruned_int8_convrot.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
│   ├── 📂 loras/
│   │   └── minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors
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
