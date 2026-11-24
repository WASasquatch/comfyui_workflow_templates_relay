# Inflation Lora Character Expansion Effect Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_ingi_infl8)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_ingi_infl8-1.webp" width="360" alt="Inflation Lora Character Expansion Effect Video templates_ingi_infl8-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_ingi_infl8-2.webp" width="360" alt="Inflation Lora Character Expansion Effect Video templates_ingi_infl8-2.webp">

> Upload a character image and input your prompt. Generate an animated video where the character expands with an inflation effect.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_ingi_infl8.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_ingi_infl8.json)

## Details

| | |
|---|---|
| Name | `templates_ingi_infl8` |
| Category | Foundation › Video |
| Output | video |
| Models | wan2.2 Animate |
| Tags | Video, Image to Video |
| Type | open source |
| Date | 2026-03-09 |
| Author | ingi |
| Download size | 47.3 GB |
| Min ComfyUI version | 0.16.4 |
| Usage | 8 |
| Nodes | 44 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `VHS_LoadVideo` #2 | video | woman_walking.mp4 |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [ComfyUI-segment-anything-2](https://registry.comfy.org/nodes/ComfyUI-segment-anything-2)
- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [ComfyUI-WanAnimatePreprocess](https://registry.comfy.org/nodes/ComfyUI-WanAnimatePreprocess)
- [ComfyUI-WanVideoWrapper](https://registry.comfy.org/nodes/ComfyUI-WanVideoWrapper)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `clip_vision_h.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors?download=true) |
| `qwen_image_edit_2511_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2511_bf16.safetensors) |
| `Qwen_Image_Edit_2511-SYSTMS_INFL8.safetensors` | `loras` | [link](https://huggingface.co/systms/SYSTMS-INFL8-LoRA-Qwen-Image-Edit-2511/resolve/main/SYSTMS_INFL8_LoRA_Qwen_Image_Edit_2511.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Image Edit (Qwen 2511)** (16 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `FluxKontextMultiReferenceLatentMethod` | 2 | comfy-core |
| `ImageResizeKJv2` | 2 | comfyui-kjnodes |
| `Note` | 2 |  |
| `TextEncodeQwenImageEditPlus` | 2 | comfy-core |
| `BlockifyMask` | 1 | comfyui-kjnodes |
| `CFGNorm` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `ComfyMathExpression` | 1 |  |
| `DownloadAndLoadSAM2Model` | 1 | ComfyUI-segment-anything-2 |
| `DrawMaskOnImage` | 1 | comfyui-kjnodes |
| `DrawViTPose` | 1 | ComfyUI-WanAnimatePreprocess |
| `FluxKontextImageScale` | 1 | comfy-core |
| `GetImageRangeFromBatch` | 1 | comfyui-kjnodes |
| `GrowMaskWithBlur` | 1 | comfyui-kjnodes |
| `KSampler` | 1 | comfy-core |
| `LoadWanVideoT5TextEncoder` | 1 | ComfyUI-WanVideoWrapper |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `OnnxDetectionModelLoader` | 1 | ComfyUI-WanAnimatePreprocess |
| `PoseAndFaceDetection` | 1 | ComfyUI-WanAnimatePreprocess |
| `Sam2Segmentation` | 1 | ComfyUI-segment-anything-2 |
| `SaveImage` | 1 |  |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `VHS_LoadVideo` | 1 | comfyui-videohelpersuite |
| `VHS_VideoCombine` | 1 | comfyui-videohelpersuite |
| `VHS_VideoInfo` | 1 | comfyui-videohelpersuite |
| `WanVideoAnimateEmbeds` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoClipVisionEncode` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoDecode` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoLoraSelectMulti` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoModelLoader` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoSamplerv2` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoSchedulerv2` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoTextEncode` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoVAELoader` | 1 | ComfyUI-WanVideoWrapper |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
Models:

https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_edit_2511_fp8mixed.safetensors

https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors

https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/vae/qwen_image_vae.safetensors

https://huggingface.co/Osrivers/Qwen-Image-Edit-2509-Lightning-8steps-V1.0-bf16.safetensors/blob/main/Qwen-Image-Edit-2509-Lightning-8steps-V1.0-bf16.safetensors

https://huggingface.co/systms/SYSTMS-INFL8-LoRA-Qwen-Image-Edit-2511/blob/main/SYSTMS_INFL8_LoRA_Qwen_Image_Edit_2511.safetensors

https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_animate_14B_bf16.safetensors

https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_animate_14B_relight_lora_bf16.safetensors

https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/blob/main/split_files/vae/wan_2.1_vae.safetensors

https://huggingface.co/drozbay/Wan2.2_A14B_lora_extract/blob/main/Wan22_A14B_T2V_lora_extract_r64.safetensors

https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_14B_T2V_cfg_step_distill_lora_adaptive_rank_quantile_0.15_bf16.safetensors
```

</details>

<details><summary>KSampler settings</summary>

You can test and find the best setting by yourself. The following table is for reference.
|   | Qwen | Comfy | lightning LoRA |
|--------|---------|------------|---------------------------|
| Steps  | 40      | 20         | 4                         |
| CFG    | 4.0     | 4.0       | 1.0                       |

By default, we use 20 steps as we just don't want it to take too long. Try 40 if you want a better result, but it will take longer.

</details>

<details><summary>Note</summary>

```text
The "Edit Model Reference Method" nodes above are not needed if you use Comfy files, but may be needed if you use repackaged ones from other people.
```

</details>
