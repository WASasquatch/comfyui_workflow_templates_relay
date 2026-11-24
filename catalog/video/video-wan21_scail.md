# Wan2.1 SCAIL

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video-wan21_scail)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video-wan21_scail-1.webp" width="360" alt="Wan2.1 SCAIL video-wan21_scail-1.webp">

> One-Touch SCAIL Pose Control based on the composition of the Reference Image

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video-wan21_scail.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video-wan21_scail.json)

## Details

| | |
|---|---|
| Name | `video-wan21_scail` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.1 SCAIL |
| Tags | Motion Control, Video |
| Type | open source |
| Date | 2026-01-19 |
| Author | ComfyUI |
| Download size | 19.0 GB |
| Min ComfyUI version | 0.16.0 |
| Usage | 92 |
| Nodes | 39 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #390 | image | pirates_dancing.png |
| input | `LoadVideo` #408 | video | wan21_scail-input.mp4 |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui-scail-pose](https://registry.comfy.org/nodes/comfyui-scail-pose)
- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [ComfyUI-WanAnimatePreprocess](https://registry.comfy.org/nodes/ComfyUI-WanAnimatePreprocess)
- [ComfyUI-WanVideoWrapper](https://registry.comfy.org/nodes/ComfyUI-WanVideoWrapper)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `clip_vision_h.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) |

## Subgraphs

- **Wan 2.1 SCAIL** (35 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 4 |  |
| `CreateVideo` | 2 |  |
| `ImageResizeKJv2` | 2 | comfyui-kjnodes |
| `PoseDetectionVitPoseToDWPose` | 2 | comfyui-scail-pose |
| `SaveVideo` | 2 |  |
| `SimpleMath+` | 2 |  |
| `CLIPVisionLoader` | 1 | comfy-core |
| `GetVideoComponents` | 1 |  |
| `ImageFromBatch` | 1 |  |
| `LoadImage` | 1 | comfy-core |
| `LoadNLFModel` | 1 |  |
| `LoadVideo` | 1 |  |
| `NLFPredict` | 1 | ComfyUI-WanVideoWrapper |
| `Note` | 1 |  |
| `OnnxDetectionModelLoader` | 1 | ComfyUI-WanAnimatePreprocess |
| `RenderNLFPoses` | 1 | comfyui-scail-pose |
| `WanVideoAddSCAILPoseEmbeds` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoAddSCAILReferenceEmbeds` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoClipVisionEncode` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoContextOptions` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoDecode` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoEmptyEmbeds` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoLoraSelect` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoModelLoader` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoSamplerExtraArgs` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoSamplerv2` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoSchedulerv2` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoSetLoRAs` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoTextEncodeCached` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoTorchCompileSettings` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoVAELoader` | 1 | ComfyUI-WanVideoWrapper |

## Notes embedded in the workflow

<details><summary>Wan 2.1 SCAIL</summary>

WAN 2.1 SCAIL transfers motion and pose information from an input video onto a reference image while preserving the reference image’s original composition. It works by rescaling pose data from the source footage to match the proportions and framing of the reference image.

This makes it ideal for animating still images using real motion, without distorting the original layout.

## Inputs

| Input | Type | Description |
|------|------|-------------|
| reference_image | Image | The still image whose composition, framing, and visual identity you want to preserve |
| input_video | Image / Video | Source footage used to extract pose and motion data |
| num_frames | Integer | Number of frames to generate; typically matched to or derived from the input video length |

## Parameters

| Parameter | Description |
|---------|-------------|
| cfg | Controls how strongly the model follows the prompt versus the motion data. Lower values prioritize motion accuracy; higher values emphasize prompt adherence, leave it at 1.0 to begin |
| width | Output width in pixels. Must be divisible by 16 |
| height | Output height in pixels. Must be divisible by 16 |
| prompt | Text description guiding appearance, style, or action refinement |
| seed | Random seed for generation consistency. Keeping this fixed helps with repeatable results |

## Resolution Recommendations

| Use Case | Resolution | Notes |
|--------|------------|-------|
| Initial testing (landscape) | 832 × 480 | Fast iteration, easier to debug motion |
| Initial testing (portrait) | 480 × 832 | Fast iteration for vertical content |
| Final renders | Increase gradually | Scale up only after motion and framing look correct |

**Important:**  
- Both width and height must be divisible by **16**  
- Start at lower resolutions to validate motion transfer before increasing quality

</details>

<details><summary>Markdown Note: Pose input info</summary>

## IMPORTANT

The model uses downsampled poses, pose resolution needs to be **half** if the generation resolution. 

That is automatically calculated here and the pose is rendered to the target resolution directly.

dw_poses are optional and are used to draw face/hands as well as aligning the pose to the reference image.

You can disable the drawing and the alignment is still done if dw_poses are connected, to disable alignment disconnect them.

</details>

<details><summary>Note: Supported resolutions</summary>

```text
Dimensions should be divisible by 32
```

</details>

<details><summary>Preprocessor links</summary>

Nodes:

[https://github.com/kijai/ComfyUI-WanAnimatePreprocess](https://github.com/kijai/ComfyUI-WanAnimatePreprocess)

[https://github.com/kijai/ComfyUI-SCAIL-pose](https://github.com/kijai/ComfyUI-SCAIL-pose)

Models: /models/detection/

YOLO:

[https://huggingface.co/Wan-AI/Wan2.2-Animate-14B/blob/main/process_checkpoint/det/yolov10m.onnx](https://huggingface.co/Wan-AI/Wan2.2-Animate-14B/blob/main/process_checkpoint/det/yolov10m.onnx)

ViTPose

Large:

[https://huggingface.co/JunkyByte/easy_ViTPose/blob/main/onnx/wholebody/vitpose-l-wholebody.onnx](https://huggingface.co/JunkyByte/easy_ViTPose/blob/main/onnx/wholebody/vitpose-l-wholebody.onnx)

Huge (needs both files):

[https://huggingface.co/Kijai/vitpose_comfy/blob/main/onnx/vitpose_h_wholebody_model.onnx](https://huggingface.co/Kijai/vitpose_comfy/blob/main/onnx/vitpose_h_wholebody_model.onnx)

[https://huggingface.co/Kijai/vitpose_comfy/blob/main/onnx/vitpose_h_wholebody_data.bin](https://huggingface.co/Kijai/vitpose_comfy/blob/main/onnx/vitpose_h_wholebody_data.bin)

</details>

<details><summary>Model links</summary>

bf16: /models/diffusion_models/

[https://huggingface.co/Kijai/WanVideo_comfy/blob/main/SCAIL/Wan21-14B-SCAIL-preview_comfy_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/SCAIL/Wan21-14B-SCAIL-preview_comfy_bf16.safetensors)

fp8_scaled: /models/diffusion_models/

[https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/SCAIL/Wan21-14B-SCAIL-preview_fp8_e4m3fn_scaled_KJ.safetensors](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/blob/main/SCAIL/Wan21-14B-SCAIL-preview_fp8_e4m3fn_scaled_KJ.safetensors)

distill lora (should use I2V one): /models/loras/

[https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors)


Text encoder: /models/text_encoders/

[https://huggingface.co/Kijai/WanVideo_comfy/blob/main/umt5-xxl-enc-bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/umt5-xxl-enc-bf16.safetensors)

VAE: /models/vae/

[https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_VAE_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/blob/main/Wan2_1_VAE_bf16.safetensors)

</details>
