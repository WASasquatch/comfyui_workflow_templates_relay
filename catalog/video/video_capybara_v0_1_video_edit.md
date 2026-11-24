# Capybara: Video Edit

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_capybara_v0_1_video_edit-1.webp" width="360" alt="Capybara: Video Edit video_capybara_v0_1_video_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_capybara_v0_1_video_edit-2.webp" width="360" alt="Capybara: Video Edit video_capybara_v0_1_video_edit-2.webp">

> Upload an image or video and a text instruction to perform generation or editing tasks. Generate a new or edited image or video based on the provided instruction.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_capybara_v0_1_video_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_capybara_v0_1_video_edit.json)

## Details

| | |
|---|---|
| Name | `video_capybara_v0_1_video_edit` |
| Category | Foundation › Video |
| Media type | image |
| Models | Capybara |
| Tags | Video Edit |
| Type | open source |
| Date | 2026-02-23 |
| Author | ComfyUI |
| Download size | 34.5 GB |
| Min ComfyUI version | 0.8.0 |
| Usage | 16 |
| Nodes | 26 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #127 | video | horse_running.mp4 |
| output | `SaveVideo` #114 | video | video_capybara_v0_1_video_edit.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sigclip_vision_patch14_384.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/sigclip_vision_384/resolve/main/sigclip_vision_patch14_384.safetensors) |
| `capybara_v0.1.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/diffusion_models/capybara_v0.1.safetensors) |
| `byt5_small_glyphxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/byt5_small_glyphxl_fp16.safetensors) |
| `qwen_2.5_vl_7b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanImage_2.1_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b.safetensors) |
| `hunyuanvideo15_vae_fp16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/vae/hunyuanvideo15_vae_fp16.safetensors) |

## Subgraphs

- **Text to Image (Capybara v0.1)** (21 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `CFGGuider` | 1 | comfy-core |
| `CLIPVisionEncode` | 1 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `DualCLIPLoader` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `HunyuanVideo15ImageToVideo` | 1 | comfy-core |
| `ImageFromBatch` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `ModelSamplingSD3` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `ResizeImageMaskNode` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model Lnks</summary>

- Subgraph Guide: [subgraph](https://docs.comfy.org/interface/features/subgraph) 
- [xgen-universe/Capybara](https://huggingface.co/xgen-universe/Capybara)

## Model Links

- [Hugging Face:Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged)
- [Hugging Face:Comfy-Org/HunyuanImage_2.1_ComfyUI](https://huggingface.co/Comfy-Org/HunyuanImage_2.1_ComfyUI)

### Alternative Repos

- [ModelScope:Comfy-Org/HunyuanVideo_1.5_repackaged](https://modelscope.cn/models/Comfy-Org/HunyuanVideo_1.5_repackaged)
- [ModelScope:Comfy-Org/HunyuanImage_2.1_ComfyUI](https://modelscope.cn/models/Comfy-Org/HunyuanImage_2.1_ComfyUI)

**diffusion_models**

- [capybara_v0.1.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/diffusion_models/capybara_v0.1.safetensors) (15.51 GB)

**text_encoders**

- [qwen_2.5_vl_7b.safetensors](https://huggingface.co/Comfy-Org/HunyuanImage_2.1_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b.safetensors) (15.45 GB)
- [byt5_small_glyphxl_fp16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/byt5_small_glyphxl_fp16.safetensors) (418.3 MB)

**vae**

- [hunyuanvideo15_vae_fp16.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/vae/hunyuanvideo15_vae_fp16.safetensors) (2.35 GB)

**clip_vision**

- [sigclip_vision_patch14_384.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/clip_vision/sigclip_vision_patch14_384.safetensors) (816.8 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── capybara_v0.1.safetensors
│   ├── 📂 text_encoders/
│   │   ├── qwen_2.5_vl_7b.safetensors
│   │   └── byt5_small_glyphxl_fp16.safetensors
│   ├── 📂 vae/
│   │   └── hunyuanvideo15_vae_fp16.safetensors
│   └── 📂 clip_vision/
│       └── sigclip_vision_patch14_384.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Size and Ratio Setting</summary>

## Capybara Resolution Configuration

| Resolution Group | Aspect Ratio | Height (H) | Width (W) | Total Pixels |
|-----------------|--------------|------------|-----------|--------------|
| **480p** | 16:9 | 480 | 848 | ~407k |
| | 4:3 | 544 | 720 | ~392k |
| | 1:1 | 640 | 640 | ~410k |
| | 3:4 | 720 | 544 | ~392k |
| | 9:16 | 848 | 480 | ~407k |
| **720p** | 16:9 | 720 | 1280 | ~922k |
| | 4:3 | 832 | 1104 | ~919k |
| | 1:1 | 960 | 960 | ~922k |
| | 3:4 | 1104 | 832 | ~919k |
| | 9:16 | 1280 | 720 | ~922k |
| **1024** | 16:9 | 768 | 1360 | ~1,044k |
| | 4:3 | 880 | 1184 | ~1,042k |
| | 1:1 | 1024 | 1024 | ~1,049k |
| | 3:4 | 1184 | 880 | ~1,042k |
| | 9:16 | 1360 | 768 | ~1,044k |
| **1080p** | 16:9 | 1088 | 1920 | ~2,089k |
| | 4:3 | 1248 | 1664 | ~2,077k |
| | 1:1 | 1440 | 1440 | ~2,074k |
| | 3:4 | 1664 | 1248 | ~2,077k |
| | 9:16 | 1920 | 1088 | ~2,089k |

</details>

<details><summary>Sampler Setting</summary>

| Parameter | Inference Script (Default) | ComfyUI (Default) |
 |-----------|---------------------------|-------------------|
 | **Steps** | 50 | 20 |
 | **CFG** | 4.0 | 6.0 |
> 💡 **Tip:** For better quality results, consider using **50 steps** instead of the default 20  steps in ComfyUI. 

Video length: 121/24 = 5s

</details>
