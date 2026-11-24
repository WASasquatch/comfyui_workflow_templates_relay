# Qwen-Image InstantX Union ControlNet

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_qwen_image_instantx_controlnet)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_instantx_controlnet-1.webp" width="360" alt="Qwen-Image InstantX Union ControlNet image_qwen_image_instantx_controlnet-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_instantx_controlnet-2.webp" width="360" alt="Qwen-Image InstantX Union ControlNet image_qwen_image_instantx_controlnet-2.webp">

> Generate images with Qwen-Image InstantX ControlNet, supporting canny, soft edge, depth, pose

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_image_instantx_controlnet.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_qwen_image_instantx_controlnet.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image)

## Details

| | |
|---|---|
| Name | `image_qwen_image_instantx_controlnet` |
| Category | Foundation › Image |
| Output | image |
| Models | Qwen-Image |
| Tags | Image, ControlNet |
| Type | open source |
| Date | 2025-08-23 |
| Author | ComfyUI |
| Download size | 32.9 GB |
| Min ComfyUI version | 0.3.49 |
| Usage | 21 |
| Nodes | 33 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #71 | image | image_qwen_image_instantx_controlnet_input_image.jpg |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `Qwen-Image-InstantX-ControlNet-Union.safetensors` | `controlnet` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-InstantX-ControlNets/resolve/main/split_files/controlnet/Qwen-Image-InstantX-ControlNet-Union.safetensors) |
| `lotus-depth-d-v1-1.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/lotus/resolve/main/lotus-depth-d-v1-1.safetensors) |
| `qwen_image_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) |
| `Qwen-Image-Lightning-4steps-V1.0.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-4steps-V1.0.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |
| `vae-ft-mse-840000-ema-pruned.safetensors` | `vae` | [link](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors) |

## Subgraphs

- **ControlNet (Qwen-Image InstantX Union)** (15 nodes)
- **Image to Depth Map (Lotus)** (12 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `Note` | 2 |  |
| `UNETLoader` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VAEEncode` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `BasicGuider` | 1 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `ControlNetApplyAdvanced` | 1 | comfy-core |
| `ControlNetLoader` | 1 | comfy-core |
| `DisableNoise` | 1 | comfy-core |
| `FluxKontextImageScale` | 1 | comfy-core |
| `ImageInvert` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `LotusConditioning` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `SetFirstSigma` | 1 | comfy-core |

## Notes embedded in the workflow

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

- [Qwen-Image-InstantX-ControlNet-Union.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-InstantX-ControlNets/resolve/main/split_files/controlnet/Qwen-Image-InstantX-ControlNet-Union.safetensors) (3.29 GB)

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
│   │   └── Qwen-Image-InstantX-ControlNet-Union.safetensors
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   └── 📂 text_encoders/
│       └── qwen_2.5_vl_7b_fp8_scaled.safetensors
```

</details>

<details><summary>Lotus Depth</summary>

## Model Links

- [Hugging Face:Comfy-Org/lotus](https://huggingface.co/Comfy-Org/lotus)

### Alternative Repos

- [ModelScope:Comfy-Org/lotus](https://modelscope.cn/models/Comfy-Org/lotus)

**Diffusion Model**

Download [lotus-depth-d-v1-1.safetensors](https://huggingface.co/Comfy-Org/lotus/resolve/main/lotus-depth-d-v1-1.safetensors) (1.62 GB) 
 and place it in **ComfyUI/models/diffusion_models**

**VAE Model**

Download  [vae-ft-mse-840000-ema-pruned.safetensors](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors) (319.1 MB)  and place it in **ComfyUI/models/vae** or you can use any SD1.5 VAE if you prefer.

```
ComfyUI/
├── models/
│   ├── diffusion_models/
│   │   └─── lotus-depth-d-v1-1.safetensors
│   └── vae/
│       └──  lvae-ft-mse-840000-ema-pruned.safetensors
```

</details>

<details><summary>Note</summary>

```text
Set cfg to 1.0 for a speed boost at the cost of consistency. Samplers like res_multistep work pretty well at cfg 1.0

The official number of steps is 50 but I think that's too much. Even just 10 steps seems to work.
```

</details>

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
