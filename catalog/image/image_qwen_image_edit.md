# Qwen Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_edit-1.webp" width="360" alt="Qwen Image Edit image_qwen_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_edit-2.webp" width="360" alt="Qwen Image Edit image_qwen_image_edit-2.webp">

> Edit images with precise bilingual text editing and dual semantic/appearance editing capabilities using Qwen-Image-Edit's 20B MMDiT model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_qwen_image_edit.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit)

## Details

| | |
|---|---|
| Name | `image_qwen_image_edit` |
| Category | Foundation › Image |
| Media type | image |
| Models | Qwen-Image-Edit |
| Tags | Image Edit |
| Type | open source |
| Date | 2025-08-18 |
| Author | ComfyUI |
| Download size | 29.6 GB |
| Min ComfyUI version | 0.4.0 |
| Usage | 34 |
| Nodes | 25 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #78 | image | image_qwen_image_edit_input_image.png |
| output | `SaveImage` #60 | image | image_qwen_image_edit.jpg |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_edit_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_fp8_e4m3fn.safetensors) |
| `Qwen-Image-Edit-Lightning-4steps-V1.0-bf16.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Edit-Lightning-4steps-V1.0-bf16.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Qwen-Image-Edit** (20 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 | comfy-core |
| `MarkdownNote` | 3 |  |
| `PrimitiveFloat` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `TextEncodeQwenImageEdit` | 2 | comfy-core |
| `CFGNorm` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `ImageScaleToTotalPixels` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>For Local User</summary>

[Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit)

## Model Links

- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)
- [Hugging Face:Comfy-Org/Qwen-Image-Edit_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI)

### Alternative Repos

- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)
- [ModelScope:Comfy-Org/Qwen-Image-Edit_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image-Edit_ComfyUI)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**loras**

- [Qwen-Image-Edit-Lightning-4steps-V1.0-bf16.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Edit-Lightning-4steps-V1.0-bf16.safetensors) (810.2 MB)

**diffusion_models**

- [qwen_image_edit_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_fp8_e4m3fn.safetensors) (19.03 GB)

**vae**

- [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   ├── 📂 loras/
│   │      └── Qwen-Image-Edit-Lightning-4steps-V1.0-bf16.safetensors
│   ├── 📂 diffusion_models/
│   │      └── qwen_image_edit_fp8_e4m3fn.safetensors
│   └── 📂 vae/
│          └── qwen_image_vae.safetensors
```

## Report issue

If you have any problems running this workflow, please report template-related issues via this link: [report the template issue here](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>MarkdownNote</summary>

This node is to avoid poor output results caused by excessively large input image sizes.

</details>

<details><summary>KSampler settings</summary>

You can test and find the best setting by yourself. The following table is for reference.

| Model            | Steps | CFG |
|---------------------|---------------|---------------|
| Offical             | 50               | 4.0               
| comfy             | 20                | 2.5               |
| fp8_e4m3fn + 4steps LoRA    | 4               | 1.0               |

</details>
