# 1 image input Split Stack - Qwen Multiangle + Wan 2.2

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_rob_split_stack_qwen_multi_wan22)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_rob_split_stack_qwen_multi_wan22-1.webp" width="360" alt="1 image input Split Stack - Qwen Multiangle + Wan 2.2 template_rob_split_stack_qwen_multi_wan22-1.webp">

> Upload 1 input image and generate 5 alternate angles to be used as start frames with Wan2.2. Each video is stacked horizontally in a final 9x16 video.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_rob_split_stack_qwen_multi_wan22.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_rob_split_stack_qwen_multi_wan22.json)

## Details

| | |
|---|---|
| Name | `template_rob_split_stack_qwen_multi_wan22` |
| Category | Applied › Character & Fashion |
| Output | image |
| Models | Qwen-Image-Edit, Wan2.2 |
| Tags | Video, Image to Video |
| Type | open source |
| Date | 2026-03-18 |
| Author | hellorob |
| Download size | 20.0 GB |
| Min ComfyUI version | 0.8.0 |
| Usage | 37 |
| Nodes | 298 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #41 | image | projection_light_portrait.png |

## Custom nodes required

- [comfyui-frame-interpolation](https://registry.comfy.org/nodes/comfyui-frame-interpolation)
- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui-qwenmultiangle](https://registry.comfy.org/nodes/comfyui-qwenmultiangle)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)
- [masquerade-nodes-comfyui](https://registry.comfy.org/nodes/masquerade-nodes-comfyui)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_edit_2511_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2511_bf16.safetensors) |
| `wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors) |
| `wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors) |
| `Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning/resolve/main/Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors) |
| `qwen-image-edit-2511-multiple-angles-lora.safetensors` | `loras` | [link](https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA/resolve/main/qwen-image-edit-2511-multiple-angles-lora.safetensors) |
| `wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors) |
| `wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Subgraphs

- **Image to Video (Wan2.2)** (27 nodes)
- **Image to Video (Wan2.2)** (27 nodes)
- **Image to Video (Wan2.2)** (27 nodes)
- **Image to Video (Wan2.2)** (27 nodes)
- **Image to Video (Wan2.2)** (27 nodes)
- **Composite Stack 1** (3 nodes)
- **Composite Stack 2** (4 nodes)
- **Composite Stack 3** (4 nodes)
- **Composite Stack 4** (4 nodes)
- **Composite Stack 5** (4 nodes)
- **Image Edit(Qwen-Image 2511 with LoRA)** (24 nodes)
- **Image Edit(Qwen-Image 2511 with LoRA)** (24 nodes)
- **Image Edit(Qwen-Image 2511 with LoRA)** (24 nodes)
- **Image Edit(Qwen-Image 2511 with LoRA)** (24 nodes)
- **Image Edit(Qwen-Image 2511 with LoRA)** (24 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 40 | comfy-core |
| `PrimitiveInt` | 33 | comfy-core |
| `LoraLoaderModelOnly` | 20 | comfy-core |
| `PrimitiveFloat` | 20 | comfy-core |
| `UNETLoader` | 15 | comfy-core |
| `CLIPLoader` | 10 | comfy-core |
| `CLIPTextEncode` | 10 | comfy-core |
| `FluxKontextMultiReferenceLatentMethod` | 10 | comfy-core |
| `KSamplerAdvanced` | 10 | comfy-core |
| `ModelSamplingSD3` | 10 | comfy-core |
| `PrimitiveBoolean` | 10 | comfy-core |
| `TextEncodeQwenImageEditPlus` | 10 | comfy-core |
| `VAEDecode` | 10 | comfy-core |
| `VAELoader` | 10 | comfy-core |
| `CreateVideo` | 6 | comfy-core |
| `SaveVideo` | 6 | comfy-core |
| `CFGNorm` | 5 | comfy-core |
| `FluxKontextImageScale` | 5 | comfy-core |
| `GetVideoComponents` | 5 | comfy-core |
| `KSampler` | 5 | comfy-core |
| `ModelSamplingAuraFlow` | 5 | comfy-core |
| `Note` | 5 |  |
| `QwenMultiangleCameraNode` | 5 | comfyui-qwenmultiangle |
| `ResizeImageMaskNode` | 5 | comfy-core |
| `RIFE VFI` | 5 | comfyui-frame-interpolation |
| `SaveImage` | 5 | comfy-core |
| `VAEEncode` | 5 | comfy-core |
| `WanImageToVideo` | 5 | comfy-core |
| `ImageStitch` | 4 | comfy-core |
| `MarkdownNote` | 2 |  |
| `LoadImage` | 1 | comfy-core |
| `Reroute` | 1 |  |

## Notes embedded in the workflow

<details><summary>About Size</summary>

Width & height settings must be divisible by 32 + 1. 
Frame count must be divisible by 8 + 1. 


Running with invalid parameters **will not cause errors**. Instead, the flow will silently choose the closest valid parameters. 

By default, we are using 720p resolution. 

You can try 1920*1088 if you have a powerful GPU.

</details>

<details><summary>Model links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)
- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)
- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [Hugging Face:Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged)
- [Hugging Face:Comfy-Org/Qwen-Image-Edit_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)
- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)
- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [ModelScope:Comfy-Org/HunyuanVideo_1.5_repackaged](https://modelscope.cn/models/Comfy-Org/HunyuanVideo_1.5_repackaged)
- [ModelScope:Comfy-Org/Qwen-Image-Edit_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image-Edit_ComfyUI)

**loras**

- [wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors) (1.14 GB)
- [wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors) (1.14 GB)
- [Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning/resolve/main/Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors) (810.2 MB)
- [qwen-image-edit-2511-multiple-angles-lora.safetensors](https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA/resolve/main/qwen-image-edit-2511-multiple-angles-lora.safetensors) (281.5 MB)

**vae**

- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) (242.1 MB)
- [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

**text_encoders**

- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) (6.27 GB)
- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**diffusion_models**

- [wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors) (13.31 GB)
- [wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors) (13.31 GB)
- [qwen_image_edit_2511_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2511_bf16.safetensors) (38.05 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 loras/
│   │   ├── wan2.2_i2v_lightx2v_4steps_lora_v1_low_noise.safetensors
│   │   ├── wan2.2_i2v_lightx2v_4steps_lora_v1_high_noise.safetensors
│   │   ├── Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors
│   │   └── qwen-image-edit-2511-multiple-angles-lora.safetensors
│   ├── 📂 vae/
│   │   ├── wan_2.1_vae.safetensors
│   │   └── qwen_image_vae.safetensors
│   ├── 📂 text_encoders/
│   │   ├── umt5_xxl_fp8_e4m3fn_scaled.safetensors
│   │   └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   └── 📂 diffusion_models/
│       ├── wan2.2_i2v_low_noise_14B_fp8_scaled.safetensors
│       ├── wan2.2_i2v_high_noise_14B_fp8_scaled.safetensors
│       └── qwen_image_edit_2511_bf16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note</summary>

```text
The "Edit Model Reference Method" nodes above are not needed if you use Comfy files, but may be needed if you use repackaged ones from other people.
```

</details>

<details><summary>Note</summary>

```text
The "Edit Model Reference Method" nodes above are not needed if you use Comfy files, but may be needed if you use repackaged ones from other people.
```

</details>

<details><summary>Note</summary>

```text
The "Edit Model Reference Method" nodes above are not needed if you use Comfy files, but may be needed if you use repackaged ones from other people.
```

</details>

<details><summary>Note</summary>

```text
The "Edit Model Reference Method" nodes above are not needed if you use Comfy files, but may be needed if you use repackaged ones from other people.
```

</details>

<details><summary>Note</summary>

```text
The "Edit Model Reference Method" nodes above are not needed if you use Comfy files, but may be needed if you use repackaged ones from other people.
```

</details>
