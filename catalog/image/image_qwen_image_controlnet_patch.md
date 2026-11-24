# Qwen-Image ControlNet Model Patch

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_controlnet_patch-1.webp" width="360" alt="Qwen-Image ControlNet Model Patch image_qwen_image_controlnet_patch-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_controlnet_patch-2.webp" width="360" alt="Qwen-Image ControlNet Model Patch image_qwen_image_controlnet_patch-2.webp">

> Control image generation using Qwen-Image ControlNet models. Supports canny, depth, and inpainting controls through model patching.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_controlnet_patch.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_qwen_image_controlnet_patch.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image)

## Details

| | |
|---|---|
| Name | `image_qwen_image_controlnet_patch` |
| Category | Foundation › Image |
| Media type | image |
| Models | Qwen-Image |
| Tags | Text to Image, Image, ControlNet |
| Type | open source |
| Date | 2025-08-24 |
| Author | ComfyUI |
| Download size | 31.7 GB |
| Min ComfyUI version | 0.3.52 |
| Usage | 16 |
| Nodes | 20 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #71 | image | image_qwen_image_controlnet_patch_input_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) |
| `Qwen-Image-Lightning-4steps-V1.0.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-4steps-V1.0.safetensors) |
| `qwen_image_canny_diffsynth_controlnet.safetensors` | `model_patches` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/resolve/main/split_files/model_patches/qwen_image_canny_diffsynth_controlnet.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `Canny` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `ImageScaleToTotalPixels` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `ModelPatchLoader` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `Note` | 1 |  |
| `PreviewImage` | 1 | comfy-core |
| `QwenImageDiffsynthControlnet` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>KSampler settings</summary>

You can test and find the best setting by yourself. The following table is for reference.

| model            | steps | cfg |
|---------------------|---------------|---------------|
| fp8_e4m3fn             | 20                | 2.5               |
| fp8_e4m3fn + 4 Steps lightning LoRA    | 4               | 1.0               |

</details>

<details><summary>Note</summary>

```text
Increase the shift if you get too many blurry/dark/bad images. Decrease if you want to try increasing detail.
```

</details>

<details><summary>Model links</summary>

[Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image) 


## Model links

- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)
- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)
- [Hugging Face:Comfy-Org/Qwen-Image-DiffSynth-ControlNets](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets)
- [ModelScope:Comfy-Org/Qwen-Image-DiffSynth-ControlNets](https://modelscope.cn/models/Comfy-Org/Qwen-Image-DiffSynth-ControlNets)

You can find all the models on [Huggingface](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/tree/main) or [Modelscope](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI/files)

**Diffusion model**

- [qwen_image_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) (19.03 GB)

**Model patches**

- [qwen_image_canny_diffsynth_controlnet.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/resolve/main/split_files/model_patches/qwen_image_canny_diffsynth_controlnet.safetensors) (2.11 GB)
- [qwen_image_depth_diffsynth_controlnet.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/resolve/main/split_files/model_patches/qwen_image_depth_diffsynth_controlnet.safetensors) (2.11 GB)
- [qwen_image_inpaint_diffsynth_controlnet.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-DiffSynth-ControlNets/resolve/main/split_files/model_patches/qwen_image_inpaint_diffsynth_controlnet.safetensors) (2.11 GB)

**LoRA**

- [Qwen-Image-Lightning-4steps-V1.0.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-4steps-V1.0.safetensors) (1.58 GB)

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
│   │   └── Qwen-Image-Lightning-8steps-V1.0.safetensors
│   ├── 📂 model_patches/ # create one if you can't find it
│   │   ├── qwen_image_depth_diffsynth_controlnet.safetensors
│   │   ├── qwen_image_canny_diffsynth_controlnet.safetensors
│   │   └── qwen_image_inpaint_diffsynth_controlnet.safetensors
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   └── 📂 text_encoders/
│       └── qwen_2.5_vl_7b_fp8_scaled.safetensors
```

</details>
