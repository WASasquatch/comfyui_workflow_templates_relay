# Kandinsky 5.0 Video Lite Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_kandinsky5_t2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_kandinsky5_t2v-1.webp" width="360" alt="Kandinsky 5.0 Video Lite Text to Video video_kandinsky5_t2v-1.webp">

> A lightweight 2B model that generates videos from English and Russian prompts with high visual quality.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_kandinsky5_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_kandinsky5_t2v.json)

## Details

| | |
|---|---|
| Name | `video_kandinsky5_t2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Kandinsky |
| Tags | Text to Video, Video |
| Type | open source |
| Date | 2025-12-09 |
| Author | ComfyUI |
| Download size | 13.7 GB |
| Min ComfyUI version | 0.4.0 |
| Usage | 14 |
| Nodes | 13 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `kandinsky5lite_t2v_sft_5s.safetensors` | `diffusion_models` | [link](https://huggingface.co/kandinskylab/Kandinsky-5.0-T2V-Lite-sft-5s/resolve/main/model/kandinsky5lite_t2v_sft_5s.safetensors) |
| `clip_l.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `hunyuan_video_vae_bf16.safetensors` | `vae` | [link](https://huggingface.co/Kijai/HunyuanVideo_comfy/resolve/main/hunyuan_video_vae_bf16.safetensors) |

## Subgraphs

- **Kandinsky5 Text to Video** (10 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 |  |
| `MarkdownNote` | 2 |  |
| `CreateVideo` | 1 | comfy-core |
| `DualCLIPLoader` | 1 |  |
| `Kandinsky5ImageToVideo` | 1 |  |
| `KSampler` | 1 | comfy-core |
| `ModelSamplingSD3` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Video Size</summary>

768x512x121 for 5s or 768x512x241 for 10s, Width and Height should be divisible by 128 for 10s model. In case of image 2 video aspect ratio of result is close to start image ratio and area is close to 768*512

</details>

<details><summary>For Local User</summary>

## Model links

- [Hugging Face:Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged)

**ModelScope mirrors** (alternative repo location)

- [ModelScope:Comfy-Org/HunyuanVideo_1.5_repackaged](https://modelscope.cn/models/Comfy-Org/HunyuanVideo_1.5_repackaged)

You can find the step distilled model weight here: [kandinsky-50-video-lite](https://huggingface.co/collections/kandinskylab/kandinsky-50-video-lite)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)
- [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true) (234.7 MB)

**diffusion_models**

- [kandinsky5lite_t2v_sft_5s.safetensors](https://huggingface.co/kandinskylab/Kandinsky-5.0-T2V-Lite-sft-5s/resolve/main/model/kandinsky5lite_t2v_sft_5s.safetensors) (4.26 GB)

**vae**

- [hunyuan_video_vae_bf16.safetensors](https://huggingface.co/Kijai/HunyuanVideo_comfy/resolve/main/hunyuan_video_vae_bf16.safetensors) (470.1 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      ├── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   │      └── clip_l.safetensors
│   ├── 📂 diffusion_models/
│   │      └── kandinsky5lite_t2v_sft_5s.safetensors
│   └── 📂 vae/
│          └── hunyuan_video_vae_bf16.safetensors
```

## Report issue

If you found any issues when running this workflow, [report template issue here](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
