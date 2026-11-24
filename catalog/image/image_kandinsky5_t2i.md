# Kandinsky 5.0 Image Lite: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_kandinsky5_t2i-1.webp" width="360" alt="Kandinsky 5.0 Image Lite: Text to Image image_kandinsky5_t2i-1.webp">

> A lightweight 2B model that generates images from English and Russian prompts with high visual quality.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_kandinsky5_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_kandinsky5_t2i.json)

## Details

| | |
|---|---|
| Name | `image_kandinsky5_t2i` |
| Category | Foundation › Image |
| Media type | image |
| Models | Kandinsky |
| Tags | Image, Text to Image |
| Type | open source |
| Date | 2026-02-03 |
| Author | ComfyUI |
| Download size | 20.2 GB |
| Min ComfyUI version | 0.4.0 |
| Usage | 20 |
| Nodes | 11 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #16 | image | kandinsky5-t2i.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `kandinsky5lite_t2i.safetensors` | `diffusion_models` | [link](https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite/resolve/main/model/kandinsky5lite_t2i.safetensors) |
| `clip_l.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Text to Image( Kandinsky5 )** (9 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `DualCLIPLoader` | 1 | comfy-core |
| `EmptyLatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingSD3` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>For Local User</summary>

## Model Links

- [Hugging Face:Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged)
- [Hugging Face:Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo)

### Alternative Repos

- [ModelScope:Comfy-Org/HunyuanVideo_1.5_repackaged](https://modelscope.cn/models/Comfy-Org/HunyuanVideo_1.5_repackaged)
- [ModelScope:Comfy-Org/z_image_turbo](https://modelscope.cn/models/Comfy-Org/z_image_turbo)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)
- [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true) (234.7 MB)

**diffusion_models**

- [kandinsky5lite_t2i.safetensors](https://huggingface.co/kandinskylab/Kandinsky-5.0-T2I-Lite/resolve/main/model/kandinsky5lite_t2i.safetensors) (11.22 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) (319.8 MB) 

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      ├── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   │      └── clip_l.safetensors
│   ├── 📂 diffusion_models/
│   │      └── kandinsky5lite_t2i.safetensors
│   └── 📂 vae/
│          └── ae.safetensors
```

## Report issue

If you found any issues when running this workflow, [report template issue here](https://github.com/Comfy-Org/workflow_templates/issues) or at [Kandinsky5 repo](https://github.com/kandinskylab/kandinsky-5/issues)

</details>
