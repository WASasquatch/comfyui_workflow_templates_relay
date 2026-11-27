# Hunyuan Video 1.5 Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_hunyuan_video_1.5_720p_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_hunyuan_video_1.5_720p_t2v-1.webp" width="360" alt="Hunyuan Video 1.5 Text to Video video_hunyuan_video_1.5_720p_t2v-1.webp">

> Generate high-quality 720p videos from text prompts with cinematic camera control, emotional expressions, and physics simulation. Supports multiple styles including realistic, anime, and 3D with text rendering.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_hunyuan_video_1.5_720p_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_hunyuan_video_1.5_720p_t2v.json)

## Details

| | |
|---|---|
| Name | `video_hunyuan_video_1.5_720p_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Hunyuan Video |
| Tags | Text to Video, Video |
| Type | open source |
| Date | 2025-11-21 |
| Author | ComfyUI |
| Download size | 42.3 GB |
| Min ComfyUI version | 0.3.71 |
| Usage | 17 |
| Nodes | 42 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #102 | video | video_hunyuan_video_1.5_720p_t2v.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `hunyuanvideo1.5_1080p_sr_distilled_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/diffusion_models/hunyuanvideo1.5_1080p_sr_distilled_fp16.safetensors) |
| `hunyuanvideo1.5_720p_t2v_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/diffusion_models/hunyuanvideo1.5_720p_t2v_fp16.safetensors) |
| `hunyuanvideo15_latent_upsampler_1080p.safetensors` | `latent_upscale_models` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/latent_upscale_models/hunyuanvideo15_latent_upsampler_1080p.safetensors) |
| `byt5_small_glyphxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/byt5_small_glyphxl_fp16.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `hunyuanvideo15_vae_fp16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/vae/hunyuanvideo15_vae_fp16.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Note` | 4 |  |
| `CFGGuider` | 3 | comfy-core |
| `SamplerCustomAdvanced` | 3 | comfy-core |
| `BasicScheduler` | 2 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `CreateVideo` | 2 | comfy-core |
| `EasyCache` | 2 | comfy-core |
| `KSamplerSelect` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `ModelSamplingSD3` | 2 | comfy-core |
| `RandomNoise` | 2 | comfy-core |
| `SaveVideo` | 2 | comfy-core |
| `UNETLoader` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VAEDecodeTiled` | 2 | comfy-core |
| `DisableNoise` | 1 | comfy-core |
| `DualCLIPLoader` | 1 | comfy-core |
| `EmptyHunyuanVideo15Latent` | 1 | comfy-core |
| `HunyuanVideo15LatentUpscaleWithModel` | 1 | comfy-core |
| `HunyuanVideo15SuperResolution` | 1 | comfy-core |
| `LatentUpscaleModelLoader` | 1 | comfy-core |
| `SplitSigmas` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Sampler settings</summary>

50 inference steps just take too long to get the final video, so by default we set the step to 20 steps. If you want a better quality, please try the original settings below

## Original setting from Hunyuan team
| Model              | cfg | embedded_cfg | shift | inference step |
|-----------------------|-----|-------------|-------|----------------|
| 480p_t2v              | 6   | None        | 5     | 50             |
| 480p_i2v              | 6   | None        | 5     | 50             |
| 720p_t2v              | 6   | None        | 9     | 50             |
| 720p_i2v              | 6   | None        | 7     | 50             |
| 480p_t2v_distilled    | 1   | None        | 5     | 50             |
| 480p_i2v_distilled    | 1   | None        | 5     | 50             |
| 720p_t2v_distilled    | 1   | None        | 9     | 50             |
| 720p_i2v_distilled    | 1   | None        | 7     | 50             |

</details>

<details><summary>Note</summary>

```text
If you don't have enough VRAM and encounter the OOM error, please try to set the `weight_dtype` to `fp8_e4n3fn`.
```

</details>

<details><summary>Model links</summary>

## Report issue

If you found any issues when running this workflow, [report template issue here](https://github.com/Comfy-Org/workflow_templates/issues)

## Model Links

- [Hugging Face:Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/HunyuanVideo_1.5_repackaged](https://modelscope.cn/models/Comfy-Org/HunyuanVideo_1.5_repackaged)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)
- [byt5_small_glyphxl_fp16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/byt5_small_glyphxl_fp16.safetensors) (418.3 MB)

**diffusion_models**

- [hunyuanvideo1.5_1080p_sr_distilled_fp16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/diffusion_models/hunyuanvideo1.5_1080p_sr_distilled_fp16.safetensors) (15.52 GB)
- [hunyuanvideo1.5_720p_t2v_fp16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/diffusion_models/hunyuanvideo1.5_720p_t2v_fp16.safetensors) (15.51 GB)

**vae**

- [hunyuanvideo15_vae_fp16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/vae/hunyuanvideo15_vae_fp16.safetensors) (2.35 GB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      ├── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   │      └── byt5_small_glyphxl_fp16.safetensors
│   ├── 📂 diffusion_models/
│   │      ├── hunyuanvideo1.5_1080p_sr_distilled_fp16.safetensors
│   │      └── hunyuanvideo1.5_720p_t2v_fp16.safetensors
│   └── 📂 vae/
│          └── hunyuanvideo15_vae_fp16.safetensors
```

</details>

<details><summary>Note</summary>

```text
EasyCache can speed up this workflow, but it will also sacrifice the video quality. If you need it, use Ctrl+B to enable.
```

</details>

<details><summary>Note</summary>

```text
Use the VAE Decode (Tiled) if it takes too long to get the final video.
```

</details>

<details><summary>Note</summary>

```text
Split at matching sigma to the noise scale
```

</details>
