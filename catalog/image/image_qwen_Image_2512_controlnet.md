# Qwen-Image 2512: Fun Union ControlNet

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_qwen_Image_2512_controlnet)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_Image_2512_controlnet-1.webp" width="360" alt="Qwen-Image 2512: Fun Union ControlNet image_qwen_Image_2512_controlnet-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_Image_2512_controlnet-2.webp" width="360" alt="Qwen-Image 2512: Fun Union ControlNet image_qwen_Image_2512_controlnet-2.webp">

> Upload an image and select a control type from Canny, HED, Depth, Pose, MLSD, Scribble, or Grayscale. Generate a new image guided by the chosen structural condition.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_qwen_Image_2512_controlnet.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_qwen_Image_2512_controlnet.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image-2512)

## Details

| | |
|---|---|
| Name | `image_qwen_Image_2512_controlnet` |
| Category | Foundation › Image |
| Output | image |
| Models | Qwen-Image 2512 |
| Tags | ControlNet, Image |
| Type | open source |
| Date | 2026-02-16 |
| Author | ComfyUI |
| Download size | 32.9 GB |
| Min ComfyUI version | 0.8.0 |
| Usage | 32 |
| Nodes | 29 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #121 | image | low_angle_shot.png |
| output | `SaveImage` #60 | image | image_qwen_Image_2512_controlnet.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `Qwen-Image-2512-Fun-Controlnet-Union-2602.safetensors` | `controlnet` | [link](https://huggingface.co/alibaba-pai/Qwen-Image-2512-Fun-Controlnet-Union/resolve/main/Qwen-Image-2512-Fun-Controlnet-Union-2602.safetensors) |
| `qwen_image_2512_fp8_e4m3fn.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors) |
| `Qwen-Image-Lightning-4steps-V1.0.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-4steps-V1.0.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **ControlNet (Qwen-Image 2512)** (21 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `PrimitiveFloat` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `Canny` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `ControlNetApplyAdvanced` | 1 | comfy-core |
| `ControlNetLoader` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `Reroute` | 1 |  |
| `ResizeImageMaskNode` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

You can replace this section with other image preprocessors, such as OpenPose, or depth preprocessors.

You might need [comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux)

</details>

<details><summary>Model links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)

### Alternative Repos

- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)

**controlnet**

- [Qwen-Image-2512-Fun-Controlnet-Union-2602.safetensors](https://huggingface.co/alibaba-pai/Qwen-Image-2512-Fun-Controlnet-Union/resolve/main/Qwen-Image-2512-Fun-Controlnet-Union-2602.safetensors) (3.27 GB)

**loras**

- [Qwen-Image-Lightning-4steps-V1.0.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Lightning-4steps-V1.0.safetensors) (1.58 GB)

**diffusion_models**

- [qwen_image_2512_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_2512_fp8_e4m3fn.safetensors) (19.03 GB)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**vae**

- [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 controlnet/
│   │   └── Qwen-Image-2512-Fun-Controlnet-Union-2602.safetensors
│   ├── 📂 loras/
│   │   └── Qwen-Image-Lightning-4steps-V1.0.safetensors
│   ├── 📂 diffusion_models/
│   │   └── qwen_image_2512_fp8_e4m3fn.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   └── 📂 vae/
│       └── qwen_image_vae.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
