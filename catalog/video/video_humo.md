# HuMo Video Generation

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_humo-1.webp" width="360" alt="HuMo Video Generation video_humo-1.webp">

> Generate videos based on audio, image, and text, keeping the character's lip sync.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_humo.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_humo.json)

## Details

| | |
|---|---|
| Name | `video_humo` |
| Category | Foundation › Video |
| Media type | image |
| Models | HuMo |
| Tags | Video, Text to Video |
| Type | open source |
| Date | 2025-09-21 |
| Author | ComfyUI |
| Download size | 26.0 GB |
| Min ComfyUI version | 0.3.60 |
| Usage | 28 |
| Nodes | 20 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #49 | image | video_humo_reference_image.png |
| input | `LoadAudio` #58 | audio | video_humo_input_audio.wav |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `whisper_large_v3_fp16.safetensors` | `audio_encoders` | [link](https://huggingface.co/Comfy-Org/HuMo_ComfyUI/resolve/main/split_files/audio_encoders/whisper_large_v3_fp16.safetensors) |
| `humo_17B_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/HuMo_ComfyUI/resolve/main/split_files/diffusion_models/humo_17B_fp8_e4m3fn.safetensors) |
| `lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `AudioEncoderEncode` | 1 | comfy-core |
| `AudioEncoderLoader` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadAudio` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `ModelSamplingSD3` | 1 | comfy-core |
| `RecordAudio` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `WanHuMoImageToVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Model links</summary>

## Model links

- [Hugging Face:Comfy-Org/HuMo_ComfyUI](https://huggingface.co/Comfy-Org/HuMo_ComfyUI)
- [ModelScope:Comfy-Org/HuMo_ComfyUI](https://modelscope.cn/models/Comfy-Org/HuMo_ComfyUI)
- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [Hugging Face:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)
- [ModelScope:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)


**diffusion_models**

- [humo_17B_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/HuMo_ComfyUI/resolve/main/split_files/diffusion_models/humo_17B_fp8_e4m3fn.safetensors) (15.89 GB)

**loras**
- [lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) (703.8 MB)

**text_encoders**
- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) (6.27 GB)

**vae**
- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) (242.1 MB)

**audio_encoders**
- [whisper_large_v3_fp16.safetensors](https://huggingface.co/Comfy-Org/HuMo_ComfyUI/resolve/main/split_files/audio_encoders/whisper_large_v3_fp16.safetensors) (2.88 GB)


```
📂 ComfyUI/
├─ 📂 models/
│   ├─ 📂 diffusion_models/
│   │     └── humo_17B_fp8_e4m3fn.safetensors
│   ├─ 📂 text_encoders/
│   │     └── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   ├─ 📂 audio_encoders/
│   │     └── whisper_large_v3_fp16.safetensors 
│   └─ 📂 vae/
│            └──  wan_2.1_vae.safetensors
```

</details>

<details><summary>Note: About HuMo</summary>

HuMo is a human-centric video generation tool that creates controllable, high-quality human videos from multimodal inputs (text, images, audio), supporting text-image guided customization, text-audio driven audio-motion sync, and 480P(832x480)/720P(1280x720) resolutions.

</details>

<details><summary>Note: About HuMo</summary>

If you want to use your recorded audio, please connect the audio output to the nodes that were previously linked to the LoadAudio node.

</details>
