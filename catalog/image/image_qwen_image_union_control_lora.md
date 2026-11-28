# Qwen-Image Union Control

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_qwen_image_union_control_lora)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_union_control_lora-1.webp" width="360" alt="Qwen-Image Union Control image_qwen_image_union_control_lora-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_union_control_lora-2.webp" width="360" alt="Qwen-Image Union Control image_qwen_image_union_control_lora-2.webp">

> Generate images with precise structural control using Qwen-Image's unified ControlNet LoRA. Supports multiple control types including canny, depth, lineart, softedge, normal, and openpose for diverse creative applications.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_union_control_lora.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_qwen_image_union_control_lora.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image)

## Details

| | |
|---|---|
| Name | `image_qwen_image_union_control_lora` |
| Category | Foundation › Image |
| Output | image |
| Models | Qwen-Image |
| Tags | Text to Image, Image, ControlNet |
| Type | open source |
| Date | 2025-08-23 |
| Author | ComfyUI |
| Download size | 30.5 GB |
| Min ComfyUI version | 0.4.0 |
| Usage | 18 |
| Nodes | 29 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #73 | image | image_qwen_image_union_control_lora_input_image.png |
| output | `SaveImage` #60 | image | image_qwen_image_union_control_lora.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) |
| `Qwen-Image-Lightning-4steps-V1.0.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-4steps-V1.0.safetensors) |
| `qwen_image_union_diffsynth_lora.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/resolve/main/split_files/loras/qwen_image_union_diffsynth_lora.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **ControlNet (Qwen-Image DiffSynth)** (22 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 | comfy-core |
| `MarkdownNote` | 3 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `PrimitiveFloat` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `ReferenceLatent` | 2 | comfy-core |
| `Canny` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `ImageScaleToTotalPixels` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model links</summary>

[Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image) 

[DiffSynth-Studio/Qwen-Image-In-Context-Control-Union](https://www.modelscope.cn/models/DiffSynth-Studio/Qwen-Image-In-Context-Control-Union) supports: canny, depth, lineart, softedge, normal, and openpose. 

## Model Links

- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)
- [Hugging Face:Comfy-Org/Qwen-Image-DiffSynth-ControlNets](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets)

### Alternative Repos

- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)
- [ModelScope:Comfy-Org/Qwen-Image-DiffSynth-ControlNets](https://modelscope.cn/models/Comfy-Org/Qwen-Image-DiffSynth-ControlNets)

You can find all the models on [Huggingface](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/tree/main) or [Modelscope](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI/files)

**Diffusion model**

- [qwen_image_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) (19.03 GB)

**LoRA**

- [Qwen-Image-Lightning-8steps-V1.0.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-8steps-V1.0.safetensors) (1.58 GB)
- [qwen_image_union_diffsynth_lora.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/resolve/main/split_files/loras/qwen_image_union_diffsynth_lora.safetensors) (900.2 MB)

**Text encoder**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**VAE**

- [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   ├── qwen_image_fp8_e4m3fn.safetensors
│   │   └── qwen_image_distill_full_fp8_e4m3fn.safetensors
│   ├── 📂 loras/
│   │   ├── qwen_image_union_diffsynth_lora.safetensors
│   │   └── Qwen-Image-Lightning-8steps-V1.0.safetensors
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   └── 📂 text_encoders/
│       └── qwen_2.5_vl_7b_fp8_scaled.safetensors
```

</details>

<details><summary>About Scale Image to Total Pixels</summary>

This node is to avoid poor output results caused by excessively large input image sizes. You can remove it or use **ctrl + B** to bypass it if you don't need it.

</details>

<details><summary>Steps</summary>

Try 50 steps, if you want to try the inference steps from Qwen-Image to get better output

</details>
