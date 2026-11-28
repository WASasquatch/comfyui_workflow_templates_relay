# Wan2.2 Animate, Character Animation and Replacement

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_wan2_2_14B_animate)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_animate-1.webp" width="360" alt="Wan2.2 Animate, Character Animation and Replacement video_wan2_2_14B_animate-1.webp">

> Unified character animation and replacement framework with precise motion and expression replication.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_animate.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan2_2_14B_animate.json)
- [Tutorial](https://docs.comfy.org/tutorials/video/wan/wan2-2-animate)

## Details

| | |
|---|---|
| Name | `video_wan2_2_14B_animate` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan, wan2.2 Animate |
| Tags | Video, Image to Video |
| Type | open source |
| Date | 2025-09-22 |
| Author | ComfyUI |
| Download size | 25.5 GB |
| Min ComfyUI version | 0.8.0 |
| Usage | 206 |
| Nodes | 57 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #10 | image | video_wan2_2_14B_animate_reference_image.png |
| input | `LoadVideo` #145 | video | video_wan2_2_14B_animate_original_video.mp4 |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [ComfyUI-segment-anything-2](https://registry.comfy.org/nodes/ComfyUI-segment-anything-2)
- [comfyui_controlnet_aux](https://registry.comfy.org/nodes/comfyui_controlnet_aux)

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
- **Video Extend(Subgraph)** (7 nodes)
- **Video Extend(Subgraph)** (7 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 6 |  |
| `CreateVideo` | 3 | comfy-core |
| `ImageFromBatch` | 3 | comfy-core |
| `KSampler` | 3 | comfy-core |
| `SaveVideo` | 3 | comfy-core |
| `TrimVideoLatent` | 3 | comfy-core |
| `VAEDecode` | 3 | comfy-core |
| `WanAnimateToVideo` | 3 | comfy-core |
| `BatchImagesNode` | 2 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `DWPreprocessor` | 2 | comfyui_controlnet_aux |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `BlockifyMask` | 1 | comfyui-kjnodes |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPVisionEncode` | 1 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `DownloadAndLoadSAM2Model` | 1 | ComfyUI-segment-anything-2 |
| `DrawMaskOnImage` | 1 | comfyui-kjnodes |
| `GetVideoComponents` | 1 | comfy-core |
| `GrowMask` | 1 | comfy-core |
| `ImageScale` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `MaskPreview` | 1 | comfy-core |
| `ModelSamplingSD3` | 1 | comfy-core |
| `Note` | 1 |  |
| `PixelPerfectResolution` | 1 | comfyui_controlnet_aux |
| `PointsEditor` | 1 | comfyui-kjnodes |
| `PreviewImage` | 1 | comfy-core |
| `Sam2Segmentation` | 1 | ComfyUI-segment-anything-2 |
| `UNETLoader` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
The Image Scale node is to prevent you from inputting an oversized video. A large size video will take a very long time to preprocess.

Please update this setting according to the video size you input
```

</details>

<details><summary>Note: Switch to Move mode</summary>

The model has two modes:
- Mix: character replace
- Move: Pose transfer

If you want to switch to **Move** mode, please disconnect **Background_video** and **Character_mask** output from the **WanAnimateToVideo** node.

Bypass will still pass the input video to the **WanAnimateToVideo** node, so please disconnect them.

</details>

<details><summary>Note: About Points Editor</summary>

## How to load image 

You can right-click on the canvas, then choose Load Image. Or you can run the workflow once, and it will automatically get the first frame of the input video.

## Add new green points

Green points are used to mark the area that you want to detect.
Press the Shift key, then use the left click to add new green points.

## Add new red points

Red points are used to mark the area you want to exclude.
Press the Shift key, then use the right click to add new red points.

## Clear all points

Click the **New canvas** to clear all points

</details>

<details><summary>Note: Extend video length</summary>

Copy this group then link the "Batch images" and the "video_frame_offset" to the next extend subgraph

</details>

<details><summary>Note: Make sure these custom nodes are installed.</summary>

In this template, we have used three custom nodes. For users who don't know how to install a custom node, please refer to [How to install custom node](https://docs.comfy.org/installation/install_custom_node).

## Custom nodes

- [comfyui_controlnet_aux](https://github.com/Fannovel16/comfyui_controlnet_aux)
- [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes/)
- [ComfyUI-segment-anything-2](https://github.com/kijai/ComfyUI-segment-anything-2)

</details>

<details><summary>Note: Model links</summary>

[Tutorial](https://docs.comfy.org/tutorials/video/wan/wan2-2-animate
) 

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)
- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)
- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

**diffusion_models**       
- [Wan2_2-Animate-14B_fp8_e4m3fn_scaled_KJ.safetensors](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/resolve/main/Wan22Animate/Wan2_2-Animate-14B_fp8_e4m3fn_scaled_KJ.safetensors) (17.14 GB)
- [wan2.2_animate_14B_bf16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_animate_14B_bf16.safetensors) (32.18 GB)

**loras**
- [lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) (703.8 MB)
- [WanAnimate_relight_lora_fp16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/LoRAs/Wan22_relight/WanAnimate_relight_lora_fp16.safetensors) (1.34 GB)

**clip_visions**
- [clip_vision_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) (1.18 GB)

**vae**
- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) (242.1 MB)

**text_encoders**   
- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) (6.27 GB)

```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   ├─── Wan2_2-Animate-14B_fp8_e4m3fn_scaled_KJ.safetensors
│   │   └─── wan2.2_animate_14B_bf16.safetensors
│   ├───📂 loras/
│   │   ├─── lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
│   │   └─── WanAnimate_relight_lora_fp16.safetensors
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   ├───📂 clip_visions/ 
│   │   └─── clip_vision_h.safetensors
│   └───📂 vae/
│       └── wan_2.1_vae.safetensors
```
# Report issue

If you have any problems while using this workflow, please report template-related issues via this link: [report the template issue here](https://github.com/Comfy-Org/workflow_templates/issues).

</details>

<details><summary>Note: about size</summary>

Due to the **WanAnimateToVideo** node input limit. The width and height must be multiples of 16.

By default, we set it to a smaller size. This is in case you don't have enough VRAM and input a large size, which may cause an out-of-memory issue.

</details>
