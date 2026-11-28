# Qwen-Image InstantX Inpainting ControlNet

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_qwen_image_instantx_inpainting_controlnet)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_instantx_inpainting_controlnet-1.webp" width="360" alt="Qwen-Image InstantX Inpainting ControlNet image_qwen_image_instantx_inpainting_controlnet-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_instantx_inpainting_controlnet-2.webp" width="360" alt="Qwen-Image InstantX Inpainting ControlNet image_qwen_image_instantx_inpainting_controlnet-2.webp">

> Professional inpainting and image editing with Qwen-Image InstantX ControlNet. Supports object replacement, text modification, background changes, and outpainting.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_instantx_inpainting_controlnet.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_qwen_image_instantx_inpainting_controlnet.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image)

## Details

| | |
|---|---|
| Name | `image_qwen_image_instantx_inpainting_controlnet` |
| Category | Foundation › Image |
| Output | image |
| Models | Qwen-Image |
| Tags | Image, ControlNet, Inpainting |
| Type | open source |
| Date | 2025-09-12 |
| Author | ComfyUI |
| Download size | 33.5 GB |
| Min ComfyUI version | 0.3.57 |
| Usage | 186 |
| Nodes | 58 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #71 | image | image_qwen_image_instantx_inpainting_controlnet_input_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `Qwen-Image-InstantX-ControlNet-Inpainting.safetensors` | `controlnet` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-InstantX-ControlNets/resolve/main/split_files/controlnet/Qwen-Image-InstantX-ControlNet-Inpainting.safetensors) |
| `qwen_image_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) |
| `Qwen-Image-Lightning-4steps-V1.0.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-4steps-V1.0.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Grow and Blur Mask** (4 nodes)
- **Scale image and mask(Subgraph)** (5 nodes)
- **Grow and Blur Mask** (4 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 5 |  |
| `CLIPTextEncode` | 4 | comfy-core |
| `SaveImage` | 4 | comfy-core |
| `ImageScaleToMaxDimension` | 3 | comfy-core |
| `ImageToMask` | 3 | comfy-core |
| `MaskToImage` | 3 | comfy-core |
| `CLIPLoader` | 2 | comfy-core |
| `ControlNetInpaintingAliMamaApply` | 2 | comfy-core |
| `ControlNetLoader` | 2 | comfy-core |
| `GrowMask` | 2 | comfy-core |
| `ImageBlur` | 2 | comfy-core |
| `ImageCompositeMasked` | 2 | comfy-core |
| `KSampler` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `MaskPreview` | 2 | comfy-core |
| `ModelSamplingAuraFlow` | 2 | comfy-core |
| `Note` | 2 |  |
| `UNETLoader` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VAEEncode` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `ImagePadForOutpaint` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `PrimitiveInt` | 1 | comfy-core |
| `SetLatentNoiseMask` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>About how to create mask</summary>

Right-click on the Load Image node, then click "Open in MaskEditor" to open it and paint the area you want to inpaint.

You can learn more about MaskEditor in the [MaskEditor Document](https://docs.comfy.org/interface/maskeditor)

</details>

<details><summary>Note</summary>

```text
Set cfg to 1.0 for a speed boost at the cost of consistency. Samplers like res_multistep work pretty well at cfg 1.0

The official number of steps is 50 but I think that's too much. Even just 10 steps seems to work.
```

</details>

<details><summary>About ImageCompositeMasked</summary>

Some users might want to keep the unmasked area unchanged, though with ImageCompositeMasked, we can paste the original pixels back.

</details>

<details><summary>About ImageScaleToMaxDimension</summary>

The input image shouldn't be too large (such as more than 3000). A too large input might cause bad results. You can enable the *ImageScaleToMaxDimension* node to download and scale the input image.

</details>

<details><summary>Model links</summary>

[Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image)

## Model Links

- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)
- [Hugging Face:Comfy-Org/Qwen-Image-InstantX-ControlNets](https://huggingface.co/Comfy-Org/Qwen-Image-InstantX-ControlNets)

### Alternative Repos

- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)
- [ModelScope:Comfy-Org/Qwen-Image-InstantX-ControlNets](https://modelscope.cn/models/Comfy-Org/Qwen-Image-InstantX-ControlNets)

You can find all the models on [Huggingface](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/tree/main) or [Modelscope](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI/files)

**Diffusion model**

- [qwen_image_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) (19.03 GB)

**ControlNet**

- [Qwen-Image-InstantX-ControlNet-Inpainting.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-InstantX-ControlNets/resolve/main/split_files/controlnet/Qwen-Image-InstantX-ControlNet-Inpainting.safetensors) (3.94 GB)

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
│   ├── 📂 controlnet/ 
│   │   └── Qwen-Image-InstantX-ControlNet-Inpainting.safetensors
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   └── 📂 text_encoders/
│       └── qwen_2.5_vl_7b_fp8_scaled.safetensors
```

</details>

<details><summary>Note</summary>

```text
Increase the shift if you get too many blurry/dark/bad images. Decrease if you want to try increasing detail.
```

</details>

<details><summary>Note: KSampler settings</summary>

You can test and find the best setting by yourself. The following table is for reference.
| Parameters   | Qwen Team | Comfy Original | with 4steps LoRA |
|--------|---------|------------|---------------------------|
| Steps  | 50      | 20         | 4                         |
| CFG    | 4.0     | 2.5        | 1.0                       |

</details>
