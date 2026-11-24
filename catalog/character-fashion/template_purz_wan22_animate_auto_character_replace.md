# Wan2.2 Animate: Automatic Character Replacement

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_purz_wan22_animate_auto_character_replace-1.webp" width="360" alt="Wan2.2 Animate: Automatic Character Replacement template_purz_wan22_animate_auto_character_replace-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_purz_wan22_animate_auto_character_replace-2.webp" width="360" alt="Wan2.2 Animate: Automatic Character Replacement template_purz_wan22_animate_auto_character_replace-2.webp">

> Upload a video and a character image. Automatically replace the character in the video using the Wan2.2 Animate model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_purz_wan22_animate_auto_character_replace.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_purz_wan22_animate_auto_character_replace.json)

## Details

| | |
|---|---|
| Name | `template_purz_wan22_animate_auto_character_replace` |
| Category | Applied › Character & Fashion |
| Media type | image |
| Models | wan2.2 Animate |
| Tags | Video, Character Replacement, Video Edit |
| Type | open source |
| Date | 2026-03-08 |
| Author | PurzBeats |
| Download size | 26.8 GB |
| Min ComfyUI version | 0.3.60 |
| Usage | 352 |
| Nodes | 44 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #10 | image | old_man_dancing.jpg |
| input | `VHS_LoadVideo` #301 | video | wan22-animate-auto-character_replace-input.mp4 |
| output | `SaveVideo` #19 | video | wan22-animate-auto-character_replace-output.mp4 |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [ComfyUI-segment-anything-2](https://registry.comfy.org/nodes/ComfyUI-segment-anything-2)
- [ComfyUI-WanAnimatePreprocess](https://registry.comfy.org/nodes/ComfyUI-WanAnimatePreprocess)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `clip_vision_h.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) |
| `Wan2_2-Animate-14B_fp8_e4m3fn_scaled_KJ.safetensors` | `diffusion_models` | [link](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/resolve/main/Wan22Animate/Wan2_2-Animate-14B_fp8_e4m3fn_scaled_KJ.safetensors) |
| `lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) |
| `WanAnimate_relight_lora_fp16.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/LoRAs/Wan22_relight/WanAnimate_relight_lora_fp16.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Subgraphs

- **Video Sampling and output(Subgraph)** (6 nodes)
- **Wan 2.2 Animate - Character Replace** (32 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CreateVideo` | 4 | comfy-core |
| `SaveVideo` | 4 | comfy-core |
| `PrimitiveInt` | 3 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `ImageScale` | 2 | comfy-core |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `Reroute` | 2 |  |
| `BlockifyMask` | 1 | comfyui-kjnodes |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPVisionEncode` | 1 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `DownloadAndLoadSAM2Model` | 1 | ComfyUI-segment-anything-2 |
| `DrawMaskOnImage` | 1 | comfyui-kjnodes |
| `DrawViTPose` | 1 | ComfyUI-WanAnimatePreprocess |
| `GetImageSize` | 1 |  |
| `GrowMaskWithBlur` | 1 | comfyui-kjnodes |
| `ImageFromBatch` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingSD3` | 1 | comfy-core |
| `Note` | 1 |  |
| `OnnxDetectionModelLoader` | 1 | ComfyUI-WanAnimatePreprocess |
| `PoseAndFaceDetection` | 1 | ComfyUI-WanAnimatePreprocess |
| `Sam2Segmentation` | 1 | ComfyUI-segment-anything-2 |
| `TrimVideoLatent` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `VHS_LoadVideo` | 1 |  |
| `VHS_VideoInfo` | 1 |  |
| `WanAnimateToVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>🎬 Wan 2.2 Animate – Automated Character Replace Workflow</summary>

This workflow takes an input video + reference image and generates an animated result using **Wan 2.2 Animate (Character Replace)**.

> ⚠️ Works best when the **reference image is a person**.  
Human subjects (clear face + body) produce the most stable and convincing results.

## 1️⃣ Set Target Resolution (Top Left)

Use the **Width** and **Height** nodes (top left) to define output resolution.

**Recommended:**
- ✅ Stay around **720p** (e.g. 720x720 or 832x480)
- ⚠️ 1080p may error depending on VRAM
- Higher resolutions = higher instability

> Both the input video and reference image are **center-cropped** to match the target resolution.

## 2️⃣ Control Frame Count

In the **Input Video** node, use:

`frame_load_cap`

to control how many frames are processed.

**Recommended range:**
- 🎯 **77–150 frames**

Lower = faster + less likely to crash
Higher = heavier VRAM usage

## 3️⃣ Wan 2.2 Animate Node

- Connect `input_video`
- Connect `reference_image`
- Set FPS (30 is typical)
- Add your prompt describing motion or behavior

Example:

the person is dancing

## 4️⃣ Export

The **Save Video** node outputs the final animation.

## ⚙️ Stability Guidelines

- Stick to ~720p
- Keep frames under ~150
- 1080p may fail without significant VRAM
- Everything is **center-cropped**
- Best results with **clear human reference images**

Resolution → Frame Cap → Prompt → Render.

</details>

<details><summary>Note: SAM2 detection</summary>

```text
You can use either the detected bbox or the kay_frame_body_points to positive coordinates, if one fails to creater proper mask, try the other
```

</details>
