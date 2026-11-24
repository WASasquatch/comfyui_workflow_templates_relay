# Ovis-Image Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_ovis_text_to_image)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_ovis_text_to_image-1.webp" width="360" alt="Ovis-Image Text to Image image_ovis_text_to_image-1.webp">

> Ovis-Image is a 7B text-to-image model specifically optimized for high-quality text rendering in generated images. Designed to operate efficiently under computational constraints, it excels at accurately generating images containing text content.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_ovis_text_to_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_ovis_text_to_image.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/ovis/ovis-image)

## Details

| | |
|---|---|
| Name | `image_ovis_text_to_image` |
| Category | Foundation › Image |
| Output | image |
| Models | Ovis-Image |
| Tags | Text to Image, Image |
| Type | open source |
| Date | 2025-12-02 |
| Author | ComfyUI |
| Download size | 18.8 GB |
| Min ComfyUI version | 0.4.0 |
| Usage | 8 |
| Nodes | 11 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ovis_image_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Ovis-Image/resolve/main/split_files/diffusion_models/ovis_image_bf16.safetensors) |
| `ovis_2.5.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Ovis-Image/resolve/main/split_files/text_encoders/ovis_2.5.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Text to Image (Ovis)** (9 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model links (for local user)</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Report issue

If you found any issues when running this workflow, [report template issue here](https://github.com/Comfy-Org/workflow_templates/issues)

## Model Links

- [Hugging Face:Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo)
- [Hugging Face:Comfy-Org/Ovis-Image](https://huggingface.co/Comfy-Org/Ovis-Image)

### Alternative Repos

- [ModelScope:Comfy-Org/z_image_turbo](https://modelscope.cn/models/Comfy-Org/z_image_turbo)
- [ModelScope:Comfy-Org/Ovis-Image](https://modelscope.cn/models/Comfy-Org/Ovis-Image)

**text_encoders**

- [ovis_2.5.safetensors](https://huggingface.co/Comfy-Org/Ovis-Image/resolve/main/split_files/text_encoders/ovis_2.5.safetensors) (4.79 GB)

**diffusion_models**

- [ovis_image_bf16.safetensors](https://huggingface.co/Comfy-Org/Ovis-Image/resolve/main/split_files/diffusion_models/ovis_image_bf16.safetensors) (13.73 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── ovis_2.5.safetensors
│   ├── 📂 diffusion_models/
│   │      └── ovis_image_bf16.safetensors
│   └── 📂 vae/
│          └── ae.safetensors
```

</details>
