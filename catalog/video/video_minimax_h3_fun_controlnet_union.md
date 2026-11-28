# MiniMax H3 Fun ControlNet Union

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_minimax_h3_fun_controlnet_union)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_minimax_h3_fun_controlnet_union-1.webp" width="360" alt="MiniMax H3 Fun ControlNet Union video_minimax_h3_fun_controlnet_union-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_minimax_h3_fun_controlnet_union-2.webp" width="360" alt="MiniMax H3 Fun ControlNet Union video_minimax_h3_fun_controlnet_union-2.webp">

> Generate videos from a pose reference video using MiniMax-H3 with a ControlNet-Union checkpoint, preserving the input's motion and structure while applying your prompt. Ideal for character animation, motion transfer, and choreography visualization projects. This workflow is for pose control only

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_minimax_h3_fun_controlnet_union.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_minimax_h3_fun_controlnet_union.json)

## Details

| | |
|---|---|
| Name | `video_minimax_h3_fun_controlnet_union` |
| Category | Foundation › Video |
| Output | video |
| Models | MiniMax H3 |
| Tags | ControlNet, Int8 |
| Type | open source |
| Date | 2026-09-07 |
| Author | ComfyUI |
| Download size | 45.4 GB |
| Min ComfyUI version | 0.35.0 |
| Usage | 68 |
| Nodes | 45 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #174 | video | dancer_field_pose.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sdpose_wholebody_fp16.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/SDPose/resolve/main/checkpoints/sdpose_wholebody_fp16.safetensors) |
| `minimax_h3_ref2va_pruned_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) |
| `rt_detr_v4-x-hgnet_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/SDPose/resolve/main/diffusion_models/rt_detr_v4-x-hgnet_fp16.safetensors) |
| `minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/loras/minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors) |
| `minimax_h3_fun_controlnet_union_pruned_int8_convrot.safetensors` | `model_patches` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/model_patches/minimax_h3_fun_controlnet_union_pruned_int8_convrot.safetensors) |
| `qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) |
| `minimax_h3_audio_vae_fp32.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) |
| `minimax_h3_video_vae_int8_convrot.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) |

## Subgraphs

- **SDPose Video Pose Extractor [Multi‑Person]** (7 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 6 |  |
| `ComfySwitchNode` | 2 | comfy-core |
| `GetVideoComponents` | 2 | comfy-core |
| `PrimitiveBoolean` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `UNETLoader` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `BasicGuider` | 1 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `ComfyMathExpression` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `GetImageSize` | 1 |  |
| `KSamplerSelect` | 1 | comfy-core |
| `LoadVideo` | 1 |  |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `MiniMaxH3FunControlNetApply` | 1 |  |
| `MiniMaxH3ReferenceToVideo` | 1 | comfy-core |
| `ModelPatchLoader` | 1 |  |
| `PreviewImage` | 1 |  |
| `PrimitiveFloat` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `ResizeImageMaskNode` | 1 | comfy-core |
| `ResolutionSelector` | 1 | comfy-core |
| `RTDETR_detect` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveVideo` | 1 |  |
| `SDPoseDrawKeypoints` | 1 | comfy-core |
| `SDPoseKeypointExtractor` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEDecodeAudio` | 1 | comfy-core |
| `Video Slice` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: MiniMax H3 Fun ControlNet</summary>

## MiniMax H3 Fun ControlNet-Union

[MiniMax-H3-Fun-Controlnet-Union](https://huggingface.co/alibaba-pai/MiniMax-H3-Fun-Controlnet-Union) is a single ControlNet-Union branch trained with VideoX-Fun. One checkpoint conditions MiniMax H3 on **Canny, Depth, HED, MLSD, or Pose** control video, and also runs **video inpainting**. Load it on top of a MiniMax H3 transformer (`fl2va` or `ref2va`).

Packaged weights: [🤗 Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3) (`minimax_h3_fun_controlnet_union_pruned_int8_convrot.safetensors`).

## ComfyUI links
- [ComfyUI#15224](https://github.com/Comfy-Org/ComfyUI/pull/15224) (MiniMax H3)
- [ComfyUI#15975](https://github.com/Comfy-Org/ComfyUI/pull/15975) (Fun ControlNet as model patch)
- [🤗 alibaba-pai/MiniMax-H3-Fun-Controlnet-Union](https://huggingface.co/alibaba-pai/MiniMax-H3-Fun-Controlnet-Union)
- [🤗 Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)

## About this workflow

This graph is a **Pose control** example only. The Union checkpoint can take Canny / Depth / HED / MLSD or an inpaint mask as well, but those paths are not wired here.

**What this graph does**

1. **Load Video (Control Video)** reads `dancer_field_pose.mp4`. Optional **Video Slice** trims the clip.
2. **SDPose Video Pose Extractor [Multi-Person]** detects people and draws whole-body skeletons (body, hands, face, feet). That skeleton sequence is the control video, not the raw RGB footage.
3. **Preview Image** shows the pose frames, then feeds them into **Apply MiniMax H3 Fun ControlNet** as `control_video`.
4. **MiniMax H3 Reference to Video** builds text conditioning and the joint audio+video latent. In this demo the `ref_*` slots are empty, so the run is text-to-video locked to the pose. You can still attach reference images, videos, or audio if you want identity or voice lock on top of the control.
5. Sampling and decode stay the same as other H3 templates: joint latent → video VAE + audio VAE → muxed MP4.

**Apply MiniMax H3 Fun ControlNet**

- **model_patch**: Fun ControlNet-Union from **ModelPatchLoader**
- **vae**: MiniMax H3 **video** VAE (used to encode the control frames)
- **control_video**: preprocessed frames. This template uses SDPose skeletons
- **mask** / **source_video**: leave empty here. `mask` (1 = regenerate) plus optional `source_video` is the inpaint path
- **strength**: how hard the control skip is added (same role as `control_context_scale` on the original model). `1.0` is strongest and is what this graph uses. Values below `1.0` loosen the pose. `0` turns the branch off
- **start_percent** / **end_percent**: which part of sampling the control is active (`0` → `1` here)

**Length and size**

- Frames snap to the video VAE grid `17n + 5` at 24fps. This template uses **5s → 124 frames**. Cap is about 15 seconds
- A control clip longer than `length` is taken from the start. A shorter clip holds its last frame
- To match the control video length, use the bypassed group and wire `batch_size` into **MiniMax H3 Reference to Video** `length`

**Prompt**

[Guide here](https://huggingface.co/MiniMaxAI/MiniMax-H3/blob/main/docs/VIDEO_PROMPT_WRITING_GUIDE_ref_en.md)

**Using the other Union modes**

Keep **Apply MiniMax H3 Fun ControlNet** and swap only the preprocessor that writes `control_video`:

- **Canny**: Detect Edges
- **Depth**: Depth Anything 3 or MoGe
- **Pose**: this graph (SDPose), or SAM3D Body
- **HED / MLSD**: no built-in preprocessor; use a community pack if you need them
- **Inpaint**: connect `mask` and optional `source_video`. `control_video` can stay empty or add extra structure

See the **Preparing the control video** note for official preprocessor tutorials.

</details>

<details><summary>Note: Model Links</summary>

## Input Asset

- [dancer_field_pose.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/dancer_field_pose.mp4)

## Model Links

- [Hugging Face:Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)
- [Hugging Face:Comfy-Org/SDPose](https://huggingface.co/Comfy-Org/SDPose)

### Alternative Repos

- [ModelScope:Comfy-Org/MiniMax-H3](https://modelscope.cn/models/Comfy-Org/MiniMax-H3)
- [ModelScope:Comfy-Org/SDPose](https://modelscope.cn/models/Comfy-Org/SDPose)

**vae**

- [minimax_h3_video_vae_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) (2.62 GB)
- [minimax_h3_audio_vae_fp32.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) (577.2 MB)

**diffusion_models**

- [minimax_h3_ref2va_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) (19.53 GB)
- [rt_detr_v4-x-hgnet_fp16.safetensors](https://huggingface.co/Comfy-Org/SDPose/resolve/main/diffusion_models/rt_detr_v4-x-hgnet_fp16.safetensors) (118.2 MB)

**text_encoders**

- [qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors) (14.61 GB)

**loras**

- [minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/loras/minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors) (1.82 GB)

**model_patches**

- [minimax_h3_fun_controlnet_union_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/model_patches/minimax_h3_fun_controlnet_union_pruned_int8_convrot.safetensors) (2.14 GB)

**checkpoints**

- [sdpose_wholebody_fp16.safetensors](https://huggingface.co/Comfy-Org/SDPose/resolve/main/checkpoints/sdpose_wholebody_fp16.safetensors) (1.79 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   ├── minimax_h3_video_vae_int8_convrot.safetensors
│   │   └── minimax_h3_audio_vae_fp32.safetensors
│   ├── 📂 diffusion_models/
│   │   ├── minimax_h3_ref2va_pruned_int8_convrot.safetensors
│   │   └── rt_detr_v4-x-hgnet_fp16.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen3vl_32b_minimax_h3_nvfp4_awq.safetensors
│   ├── 📂 loras/
│   │   └── minimax_h3_ref2v_turbo_4step_v0.1_comfyui_bf16.safetensors
│   ├── 📂 model_patches/
│   │   └── minimax_h3_fun_controlnet_union_pruned_int8_convrot.safetensors
│   └── 📂 checkpoints/
│       └── sdpose_wholebody_fp16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: Video Settings</summary>

## Resolution Selector
Delete the **Resolution Selector** node if you want to customize video size manually
| megapixels | Aspect | Output (multiple=32) |
|---|---|---|
| 0.2 | 16:9 | 608 x 352 |
| 0.3 | 16:9 | 736 x 416 |
| 0.4 | 16:9 | 864 x 480 |
| 0.5 | 16:9 | 960 x 544 |
| 0.6 | 16:9 | 1056 x 608 |
| 0.7 | 16:9 | 1152 x 640 |
| 0.8 | 16:9 | 1216 x 672 |
| 0.9 | 16:9 | 1280 x 736 |
| 0.98 | 16:9 | 1344 x 768 (official 768p) |

---

## Lightning LoRA

For fast video generation, but scarce video quality

---
## Duration

Up to 15s

</details>

<details><summary>MarkdownNote</summary>

Fun ControlNet: one checkpoint adds Canny / Depth / HED / MLSD / Pose control video plus inpainting to MiniMax H3.

Video length: 5-15s (frames snap to the 17n+5 grid at 24fps, e.g. 124 = 5s). Control videos longer than the target are trimmed to the first frames; shorter ones hold their last frame.

Works with both fl2va and ref2va model files. Keep guidance_scale = 1.0. Raise strength above 1 only if the control drifts.

</details>

<details><summary>Note: Use Video length</summary>

If you want the final video to match the control video length, you can use the group above and link the `batch_size` output to the `MiniMax H3 Reference to Video` node's length input

</details>

<details><summary>Note: Preparing the control video</summary>

## Preparing the control video with built-in preprocessing

The Fun ControlNet follows the control video you feed it, so the quality of that video's edges, depth or pose decides the quality of the control. ComfyUI ships with built-in preprocessing nodes, and each control type has an official tutorial:

- **Edges (Canny)**: [Detect Edges (Canny) node](https://docs.comfy.org/built-in-nodes/Canny)
- **Depth**: [Depth Anything 3 tutorial](https://docs.comfy.org/tutorials/utility/depth-anything-3) / [MoGe nodes](https://docs.comfy.org/built-in-nodes/MoGeInference)
- **Pose**: [SAM3D Body tutorial](https://docs.comfy.org/tutorials/utility/sam3d-body) / [SDPose Keypoint Extractor](https://docs.comfy.org/built-in-nodes/SDPoseKeypointExtractor)
- **All preprocessors overview**: [ComfyUI preprocessor workflows](https://docs.comfy.org/tutorials/utility/preprocessors)

**Mask / segmentation (for inpainting mode)**:
- [SAM3 video segmentation tutorial](https://docs.comfy.org/tutorials/utility/video-segment-sam3)

Note: HED and MLSD have no built-in preprocessing nodes. Canny, Depth and Pose cover most use cases; install a community pack if you need the others.

</details>
