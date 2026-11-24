# FastH3 OmniRef: Reference to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_fasth3_ominiref_r2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_fasth3_ominiref_r2v-1.webp" width="360" alt="FastH3 OmniRef: Reference to Video video_fasth3_ominiref_r2v-1.webp">

> Generate synchronized video with matching audio from a text prompt plus a reference image using the FastH3 OmniRef eight-step distilled model, which renders both streams in just eight sampling steps. Takes 1 input image and produces 1 video output. Ideal for animating reference characters, creating talking avatars, and rapid social media video prototyping.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_fasth3_ominiref_r2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_fasth3_ominiref_r2v.json)

## Details

| | |
|---|---|
| Name | `video_fasth3_ominiref_r2v` |
| Category | Foundation › Video |
| Output | video |
| Models | MiniMax H3 |
| Tags | Reference to Video, Video |
| Type | open source |
| Date | 2026-10-20 |
| Author | ComfyUI |
| Download size | 40.0 GB |
| Min ComfyUI version | 0.43.0 |
| Usage | 1296 |
| Nodes | 25 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #137 | image | yellow_plane_ref.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `fasth3_omniref_8step_pruned_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/FastVideo/FastH3-OmniRef-Comfy/resolve/main/diffusion_models/fasth3_omniref_8step_pruned_int8_convrot.safetensors) |
| `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) |
| `minimax_h3_audio_vae_fp32.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) |
| `minimax_h3_video_vae_int8_convrot.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `VAELoader` | 2 | comfy-core |
| `BasicGuider` | 1 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `BlockSparseAttention` | 1 |  |
| `CLIPLoader` | 1 | comfy-core |
| `ComfyMathExpression` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MiniMaxH3ReferenceToVideo` | 1 | comfy-core |
| `MiniMaxH3SigmaShift` | 1 |  |
| `ModelAttentionBackend` | 1 |  |
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

<details><summary>Note: Fast Video FastH3</summary>

## FastVideo FastH3 OmniRef

[FastH3 OmniRef](https://huggingface.co/FastVideo/FastH3-OmniRef-Comfy) is FastVideo's reference-to-video checkpoint on top of MiniMax H3: the distilled student (step 3500) trained with trajectory-based PDD and a joint DMD loss, so it renders synchronized video and audio in **8 sampling steps**. VSA is trained on 128-token tiles; ComfyUI runs 64-token tiles and the difference is not visible, since the larger tile only speeds up the native kernel on datacenter GPUs.

## About this workflow

This template runs the **reference-to-video (ref2va)** task with the `MiniMaxH3ReferenceToVideo` node. Reference images are woven into the packed sequence, so a character, a product or a location can be reused across shots while the model still generates the performance and the audio.

**Key inputs**

- **ref_images**: up to 9 reference images; two are wired here (`<Picture 1>` identity, `<Picture 2>` location). Add more slots on the node if you need them.
- **ref_videos / ref_audios**: optional, up to 3 each. A reference video can carry its own soundtrack.
- **prompt**: address the inputs by tag in connection order (`<Picture 1>`, `<Picture 2>`, …), then describe the shot, the motion and one line of dialogue; the audio follows the description.
- **ref_image_size**: `match` downscales references to the output resolution (faster), `max` keeps up to a 2048px short edge for stronger identity fidelity at the cost of speed.
- **Duration → length**: the `Float (Duration)` value is converted to the 17k+5 frame grid the model expects (5 s = 124 frames at 24fps).

## Required settings

- **Model Sparse Attention** must stay on method `vsa` with `keep_percent` 10: FastH3 checkpoints are trained with VSA and must never run plain block-sparse attention. `sol-attn` and `sla` are not compatible.
- **Model Attention Backend** only picks the dense fallback used before `start_percent` and under `min_tokens`; `comfy kitchen attention` is the int8 kernel.
- **MiniMaxH3SigmaShift** 12 / 3 is this checkpoint's video / audio shift. The FastH3 V2 text-to-video recipe (video shift 10) is not an OmniRef recipe, so do not copy it here.

## Checkpoints

Two diffusion files are published for this model: the int8 convrot export used here (22.2 GB) and a bf16 export (44.2 GB). Load exactly one of them; the text encoders and VAEs are shared with the FastH3 V2 packaging. The NVFP4 AWQ option in the text encoder folder is a text encoder, not an NVFP4 export of this diffusion model.

## Scope

This checkpoint is distilled for reference-to-video. Plain text-to-video works but is not its strength; use **FastVideo FastH3: Text to Video** or **Image to Video** for those tasks.

</details>

<details><summary>Note: Model Links</summary>

## Input Asset

- [yellow_plane_ref.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/yellow_plane_ref.png)

## Model Links

- [Hugging Face:Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)
- [Hugging Face:FastVideo/FastH3-OmniRef-Comfy](https://huggingface.co/FastVideo/FastH3-OmniRef-Comfy)

### Alternative Repos

- [ModelScope:Comfy-Org/MiniMax-H3](https://modelscope.cn/models/Comfy-Org/MiniMax-H3)

**vae**

- [minimax_h3_video_vae_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) (2.62 GB)
- [minimax_h3_audio_vae_fp32.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) (577.2 MB)

**diffusion_models**

- [fasth3_omniref_8step_pruned_int8_convrot.safetensors](https://huggingface.co/FastVideo/FastH3-OmniRef-Comfy/resolve/main/diffusion_models/fasth3_omniref_8step_pruned_int8_convrot.safetensors)

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
│   │   └── fasth3_omniref_8step_pruned_int8_convrot.safetensors
│   └── 📂 text_encoders/
│       └── qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note</summary>

At full `1344x768` (around 1MP) and `362` frames (15s), VSA sparse attention is about 2x faster than the int8 attention backend; at shorter, smaller clips it offers little speedup. This template uses `120 frames` (about `5s`) just to avoid OOM on some low-VRAM GPUs.

</details>
