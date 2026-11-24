# MiniMax H3: Multiframe Reference

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_minimax_h3_multiframe_reference-1.webp" width="360" alt="MiniMax H3: Multiframe Reference video_minimax_h3_multiframe_reference-1.webp">

> Generate video from multiple still images with MiniMax H3, anchoring up to four reference frames anywhere along the timeline to control motion and composition. Ideal for creating video continuations from existing clips, forcing narrative beats at specific moments, and producing footage with synchronized native audio for cinematic or social media content.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_minimax_h3_multiframe_reference.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_minimax_h3_multiframe_reference.json)

## Details

| | |
|---|---|
| Name | `video_minimax_h3_multiframe_reference` |
| Category | Foundation › Video |
| Media type | image |
| Models | MiniMax H3 |
| Tags | Reference to Video, Int8 |
| Type | open source |
| Date | 2026-09-04 |
| Author | ComfyUI |
| Download size | 41.4 GB |
| Min ComfyUI version | 0.35.0 |
| Usage | 170 |
| Nodes | 41 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #157 | image | h3_frame_ref_2.png |
| input | `LoadImage` #159 | image | h3_frame_ref_3.png |
| input | `LoadImage` #164 | image | h3_frame_ref_1.png |
| input | `LoadImage` #167 | image | h3_frame_ref_4.png |

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
| `ComfyMathExpression` | 4 | comfy-core |
| `LoadImage` | 4 |  |
| `MarkdownNote` | 4 |  |
| `PrimitiveFloat` | 4 | comfy-core |
| `MiniMaxH3AddGuide` | 3 |  |
| `ComfySwitchNode` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `BasicGuider` | 1 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `MiniMaxH3ReferenceToVideo` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
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

[MiniMax H3](https://www.minimax.io/blog/minimax-h3) is MiniMax's general-purpose, omni-modal generation model. It jointly understands text, image, video, and audio, and generates video with **native stereo audio**: voice, sound effects, and music are modeled jointly in a single forward pass, not layered on afterward. Output is up to 2K resolution, 24fps, and up to about 15 seconds.

## ComfyUI links
- [ComfyUI#15224](https://github.com/Comfy-Org/ComfyUI/pull/15224)
- [Add Guide for MiniMax H3](https://github.com/Comfy-Org/ComfyUI/pull/15439)
- [🤗 Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)

## About this workflow

This template runs the **reference-to-video (ref2va)** task using the **MiniMax H3 Reference to Video** node. It takes any mix of reference images, videos, and standalone audio, and weaves them into the generation to lock in a character's identity, a style, a motion, a camera move, or a voice.

On top of that, chained **Add Guide for MiniMax H3** nodes pin extra stills (or short clips, and optional audio) onto specific frames of the *output* timeline. The model can address guides anywhere on a continuous time axis, not only the first and last frame. That is the multi-frame / keyframe path in this graph.

**Key inputs**

- **ref_images / ref_videos / ref_video_audios / ref_audios** on **MiniMax H3 Reference to Video**: up to 9 reference images, 3 reference videos (each may carry its own paired soundtrack), and 3 standalone reference audio clips. These are semantic references. Name them in connection order as `<Picture 1>`, `<Video 1>`, `<Audio 1>`. They do not sit on a timeline by themselves.
- **prompt** (**Input Text (Prompt)**): reference the inputs by tag, in the exact order they were connected, then describe the target scene, motion, and audio. In this template, also name each later picture as a shot's first frame or keyframe, and cut to it at the matching timestamp in `detailed_description`.
- **ref_image_size**: `match` scales references down to the generation's resolution (faster); `max` keeps up to a 2048px short edge for stronger identity fidelity, at the cost of speed since reference tokens ride along every sampling step
- **width / height**: set via **Resolution Selector (Size)**
- **duration (seconds)** (**Float (Duration)**): converted to a valid frame `length` by the **Math Expression** node

**Multi-frame guides (Add Guide for MiniMax H3)**

Each **Add Guide for MiniMax H3** anchors a guide at `frame_idx` (negative values count from the end of the video):

- a still image
- a clip (image batches snap down to the model's valid clip lengths: 5, 22, 39... frames; batches shorter than 5 frames use only the first image)
- audio, starting at the same position
- any combination. Chain several nodes (`positive` in to `positive` out) for several guides

`frame_idx` is in frames at 24fps. This template sets it from **Frame Index (Second)** through **Math Expression** `round(a * 24)` (1.5s → frame 36). The index plus the guide length must stay inside the generated `length`.

This graph wires four pictures as follows:

- **Load Image** `h3_frame_ref_1.png` → first `ref_images` input on **MiniMax H3 Reference to Video**. This is `<Picture 1>`, the identity lock and the first frame of Shot 1. There is no Add Guide at 0s; the prompt tells the model the video starts from `<Picture 1>`.
- **Load Image** `h3_frame_ref_2.png` → first **Add Guide for MiniMax H3** at **1.5s** (Shot 2 keyframe)
- **Load Image** `h3_frame_ref_3.png` → second Add Guide at **3.0s** (Shot 3 keyframe)
- **Load Image** `h3_frame_ref_4.png` → third Add Guide at **5.0s** (Shot 4 first frame)

To add more keyframes, copy the same block: **Load Image** + **Frame Index (Second)** + **Math Expression** + **Add Guide for MiniMax H3**. Keep `positive` in series (last guide → **Basic Guider**). Reuse the same video VAE, audio VAE, and `LATENT` from **MiniMax H3 Reference to Video**. Leave `audio` empty unless you also want a soundtrack anchored at that time.

`<Picture N>` tags only bind to images actually connected on `ref_images`, in that order. Pictures 2-4 here are timeline anchors only. Also plug them into extra `ref_images` slots if you want the text encoder to see them as `<Picture 2>` / `<Picture 3>` / `<Picture 4>`.

Other useful patterns from the same node: feed the first 22 frames of an existing video plus its audio into one Add Guide at `frame_idx` 0 to continue both streams, or drop a still at a mid-clip frame (for example frame 60 of 124) to force the shot to hit that frame.

</details>

<details><summary>Note: Model Links</summary>

## Input Assets
- [h3_frame_ref_1.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/h3_frame_ref_1.png)
- [h3_frame_ref_2.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/h3_frame_ref_2.png)
- [h3_frame_ref_3.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/h3_frame_ref_3.png)
- [h3_frame_ref_4.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/h3_frame_ref_4.png)

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

<details><summary>Note: Video Settings</summary>

## Resolution Selector
Delete the **Resolution Selector** node if you want to customize video size manually
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

---

## Lightning LoRA

For fast video generation, but scarce video quality

---
## Duration

Up to 15s

</details>

<details><summary>Note</summary>

Follow the same pattern to add more video frame guidance

</details>
