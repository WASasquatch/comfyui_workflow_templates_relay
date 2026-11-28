# Hunyuan Video 1.5 Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_hunyuan_video_1.5_720p_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_hunyuan_video_1.5_720p_i2v-1.webp" width="360" alt="Hunyuan Video 1.5 Image to Video video_hunyuan_video_1.5_720p_i2v-1.webp">

> Animate still images into dynamic videos with precise motion and camera control. Maintains visual consistency while bringing photos and illustrations to life with smooth, natural movements.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_hunyuan_video_1.5_720p_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_hunyuan_video_1.5_720p_i2v.json)

## Details

| | |
|---|---|
| Name | `video_hunyuan_video_1.5_720p_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Hunyuan Video |
| Tags | Image to Video, Video |
| Type | open source |
| Date | 2025-11-21 |
| Author | ComfyUI |
| Download size | 42.3 GB |
| Min ComfyUI version | 0.3.71 |
| Usage | 60 |
| Nodes | 45 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #80 | image | video_hunyuan_video_1.5_720p_i2v_input_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sigclip_vision_patch14_384.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/sigclip_vision_384/resolve/main/sigclip_vision_patch14_384.safetensors) |
| `hunyuanvideo1.5_1080p_sr_distilled_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/diffusion_models/hunyuanvideo1.5_1080p_sr_distilled_fp16.safetensors) |
| `hunyuanvideo1.5_720p_i2v_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/diffusion_models/hunyuanvideo1.5_720p_i2v_fp16.safetensors) |
| `hunyuanvideo15_latent_upsampler_1080p.safetensors` | `latent_upscale_models` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/latent_upscale_models/hunyuanvideo15_latent_upsampler_1080p.safetensors) |
| `byt5_small_glyphxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/byt5_small_glyphxl_fp16.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `hunyuanvideo15_vae_fp16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/vae/hunyuanvideo15_vae_fp16.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CFGGuider` | 3 | comfy-core |
| `MarkdownNote` | 3 |  |
| `Note` | 3 |  |
| `SamplerCustomAdvanced` | 3 | comfy-core |
| `BasicScheduler` | 2 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `CreateVideo` | 2 | comfy-core |
| `EasyCache` | 2 | comfy-core |
| `KSamplerSelect` | 2 | comfy-core |
| `ModelSamplingSD3` | 2 | comfy-core |
| `RandomNoise` | 2 | comfy-core |
| `SaveVideo` | 2 | comfy-core |
| `UNETLoader` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VAEDecodeTiled` | 2 | comfy-core |
| `CLIPVisionEncode` | 1 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `DisableNoise` | 1 | comfy-core |
| `DualCLIPLoader` | 1 | comfy-core |
| `HunyuanVideo15ImageToVideo` | 1 | comfy-core |
| `HunyuanVideo15LatentUpscaleWithModel` | 1 | comfy-core |
| `HunyuanVideo15SuperResolution` | 1 | comfy-core |
| `LatentUpscaleModelLoader` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `SplitSigmas` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model links</summary>

## Report issue

If you found any issues when running this workflow, [report template issue here](https://github.com/Comfy-Org/workflow_templates/issues)

## Model Links

- [Hugging Face:Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged)
- [Hugging Face:Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384)

### Alternative Repos

- [ModelScope:Comfy-Org/HunyuanVideo_1.5_repackaged](https://modelscope.cn/models/Comfy-Org/HunyuanVideo_1.5_repackaged)
- [ModelScope:Comfy-Org/sigclip_vision_384](https://modelscope.cn/models/Comfy-Org/sigclip_vision_384)

[HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/tree/main/split_files)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)
- [byt5_small_glyphxl_fp16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/byt5_small_glyphxl_fp16.safetensors) (418.3 MB)

**clip_vision**

- [sigclip_vision_patch14_384.safetensors](https://huggingface.co/Comfy-Org/sigclip_vision_384/resolve/main/sigclip_vision_patch14_384.safetensors) (816.8 MB)

**diffusion_models**

- [hunyuanvideo1.5_720p_i2v_fp16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/diffusion_models/hunyuanvideo1.5_720p_i2v_fp16.safetensors) (15.51 GB)

**vae**

- [hunyuanvideo15_vae_fp16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/vae/hunyuanvideo15_vae_fp16.safetensors) (2.35 GB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      ├── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   │      └── byt5_small_glyphxl_fp16.safetensors
│   ├── 📂 clip_vision/
│   │      └── sigclip_vision_patch14_384.safetensors
│   ├── 📂 diffusion_models/
│   │      └── hunyuanvideo1.5_720p_i2v_fp16.safetensors
│   └── 📂 vae/
│          └── hunyuanvideo15_vae_fp16.safetensors
```

</details>

<details><summary>Note</summary>

```text
EasyCache can speed up this workflow, but it will also sacrifice the video quality. If you need it, use Ctrl+B to enable.
```

</details>

<details><summary>MarkdownNote</summary>

If you don't have enough VRAM and encounter the OOM error, please try to set the `weight_dtype` to `fp8_e4n3fn`.

</details>

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
Use the VAE Decode (Tiled) when it takes too long to get the final video.
```

</details>

<details><summary>Note</summary>

```text
Split at matching sigma to the noise scale
```

</details>
