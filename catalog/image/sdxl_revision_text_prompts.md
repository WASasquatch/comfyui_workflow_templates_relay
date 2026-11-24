# SDXL Revision Text Prompts

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/sdxl_revision_text_prompts-1.webp" width="360" alt="SDXL Revision Text Prompts sdxl_revision_text_prompts-1.webp">

> Generate images by transferring concepts from reference images using SDXL Revision.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/sdxl_revision_text_prompts.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/sdxl_revision_text_prompts.json)
- [Tutorial](https://comfyanonymous.github.io/ComfyUI_examples/sdxl/#revision)

## Details

| | |
|---|---|
| Name | `sdxl_revision_text_prompts` |
| Category | Foundation › Image |
| Media type | image |
| Models | SDXL, Stability |
| Tags | Text to Image, Image |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 9.9 GB |
| Min ComfyUI version | 0.0.1 |
| Usage | 28 |
| Nodes | 15 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #34 | image | sdxl_revision_text_prompts_ref_image1.png |
| input | `LoadImage` #38 | image | sdxl_revision_text_prompts_ref_image2.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sd_xl_base_1.0.safetensors` | `checkpoints` | [link](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors?download=true) |
| `clip_vision_g.safetensors` | `clip_vision` | [link](https://huggingface.co/comfyanonymous/clip_vision_g/resolve/main/clip_vision_g.safetensors?download=true) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `CLIPVisionEncode` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `unCLIPConditioning` | 2 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `EmptyLatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

🛈 [Learn more about this workflow](https://comfyanonymous.github.io/ComfyUI_examples/sdxl/#revision)


## Model links

**checkpoints**

- [sd_xl_base_1.0.safetensors](https://huggingface.co/stabilityai/stable-diffusion-xl-base-1.0/resolve/main/sd_xl_base_1.0.safetensors) (6.46 GB)

**clip_vision**

- [clip_vision_g.safetensors](https://huggingface.co/comfyanonymous/clip_vision_g/resolve/main/clip_vision_g.safetensors) (3.44 GB)


Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │      └── sd_xl_base_1.0.safetensors
│   └── 📂 clip_vision/
│          └── clip_vision_g.safetensors
```

</details>
