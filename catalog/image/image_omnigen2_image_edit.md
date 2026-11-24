# OmniGen2 Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_omnigen2_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_omnigen2_image_edit-1.webp" width="360" alt="OmniGen2 Image Edit image_omnigen2_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_omnigen2_image_edit-2.webp" width="360" alt="OmniGen2 Image Edit image_omnigen2_image_edit-2.webp">

> Edit images with natural language instructions using OmniGen2's advanced image editing capabilities and text rendering support.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_omnigen2_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_omnigen2_image_edit.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/omnigen/omnigen2)

## Details

| | |
|---|---|
| Name | `image_omnigen2_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | OmniGen |
| Tags | Image, Image Edit |
| Type | open source |
| Date | 2025-06-30 |
| Author | ComfyUI |
| Download size | 14.7 GB |
| Min ComfyUI version | 0.3.42 |
| Usage | 10 |
| Nodes | 27 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #16 | image | image_omnigen2_image_edit_input_image.png |
| output | `SaveImage` #9 | image | image_omnigen2_image_edit.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `omnigen2_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/omnigen2_fp16.safetensors) |
| `qwen_2.5_vl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_fp16.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ReferenceLatent` | 4 | comfy-core |
| `MarkdownNote` | 3 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `ImageScaleToTotalPixels` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `VAEEncode` | 2 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `DualCFGGuider` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model links</summary>

## Docs
[English](https://docs.comfy.org/tutorials/image/omnigen/omnigen2) | [中文](https://docs.comfy.org/zh-CN/tutorials/image/omnigen/omnigen2)

## Model links

- [Hugging Face:Comfy-Org/Omnigen2_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged)
- [ModelScope:Comfy-Org/Omnigen2_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Omnigen2_ComfyUI_repackaged)
- [Hugging Face:Comfy-Org/Lumina_Image_2.0_Repackaged](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged)
- [ModelScope:Comfy-Org/Lumina_Image_2.0_Repackaged](https://modelscope.cn/models/Comfy-Org/Lumina_Image_2.0_Repackaged)

**diffusion model**

- [omnigen2_fp16.safetensors](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/omnigen2_fp16.safetensors) (7.39 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/blob/main/split_files/vae/ae.safetensors)

**text encoder**

- [qwen_2.5_vl_fp16.safetensors](https://huggingface.co/Comfy-Org/Omnigen2_ComfyUI_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_fp16.safetensors) (6.99 GB)

File save location
```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── omnigen2_fp16.safetensors
│   ├── 📂 vae/
│   │   └── ae.safetensor
│   └── 📂 text_encoders/
│       └── qwen_2.5_vl_fp16.safetensors
```

</details>

<details><summary>Custom image size</summary>

To customize the image size, delete the **Get Image Size** node.

</details>

<details><summary>Enable the second input image</summary>

Use **Ctrl + B** to switch all nodes in Bypass mode to normal mode to enable the second image input.

</details>
