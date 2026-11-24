# LTX-2: Audio to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx_2_audio_to_video-1.webp" width="360" alt="LTX-2: Audio to Video video_ltx_2_audio_to_video-1.webp">

> Upload an audio file and a starting image frame. Generate a video synchronized to the audio using the LTX-2 model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx_2_audio_to_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_ltx_2_audio_to_video.json)

## Details

| | |
|---|---|
| Name | `video_ltx_2_audio_to_video` |
| Category | Foundation › Video |
| Media type | image |
| Models | LTX-2 |
| Tags | Audio to Video, Video |
| Type | open source |
| Date | 2026-02-16 |
| Author | ComfyUI |
| Download size | 50.1 GB |
| Min ComfyUI version | 0.8.0 |
| Usage | 66 |
| Nodes | 117 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #444 | image | ltx2-a2v-input.png |
| input | `LoadAudio` #565 | audio | ltx2-a2v-input.mp3 |
| output | `SaveVideo` #984 | video | video_ltx_2_audio_to_video.mp4 |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-2-19b-distilled_transformer_only_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Kijai/LTXV2_comfy/resolve/main/diffusion_models/ltx-2-19b-distilled_transformer_only_bf16.safetensors) |
| `gemma_3_12B_it_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors) |
| `ltx-2-19b-embeddings_connector_distill_bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Kijai/LTXV2_comfy/resolve/main/text_encoders/ltx-2-19b-embeddings_connector_distill_bf16.safetensors) |

## Subgraphs

- **Audio to Video(LTX-2.0)** (39 nodes)
- **Video Extrndion** (16 nodes)
- **Video Extrndion** (16 nodes)
- **Video Extrndion** (16 nodes)
- **Basic Sampling** (12 nodes)
- **Video Extrndion** (16 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Reroute` | 8 |  |
| `CFGGuider` | 5 | comfy-core |
| `KSamplerSelect` | 5 | comfy-core |
| `LTXVAudioVAEEncode` | 5 | comfy-core |
| `LTXVConcatAVLatent` | 5 | comfy-core |
| `LTXVScheduler` | 5 | comfy-core |
| `LTXVSeparateAVLatent` | 5 | comfy-core |
| `RandomNoise` | 5 | comfy-core |
| `SamplerCustomAdvanced` | 5 | comfy-core |
| `TrimAudioDuration` | 5 | comfy-core |
| `VAEDecodeTiled` | 5 | comfy-core |
| `GetImageRangeFromBatch` | 4 | comfyui-kjnodes |
| `ImageBatchExtendWithOverlap` | 4 | comfyui-kjnodes |
| `LTXVAddGuideMulti` | 4 | comfyui-kjnodes |
| `LTXVAudioVideoMask` | 4 | comfyui-kjnodes |
| `LTXVCropGuides` | 4 | comfy-core |
| `MarkdownNote` | 4 |  |
| `VAEEncode` | 4 | comfy-core |
| `VHS_VideoCombine` | 4 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `CreateVideo` | 2 |  |
| `SaveVideo` | 2 |  |
| `VAELoaderKJ` | 2 | comfyui-kjnodes |
| `AudioCrop` | 1 |  |
| `AudioSeparation` | 1 |  |
| `ConditioningZeroOut` | 1 | comfy-core |
| `DualCLIPLoader` | 1 | comfy-core |
| `EmptyLTXVLatentVideo` | 1 | comfy-core |
| `FloatConstant` | 1 | comfyui-kjnodes |
| `ImageResizeKJv2` | 1 | comfyui-kjnodes |
| `LoadAudio` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LTX2_NAG` | 1 | comfyui-kjnodes |
| `LTX2SamplingPreviewOverride` | 1 | comfyui-kjnodes |
| `LTXVChunkFeedForward` | 1 | comfyui-kjnodes |
| `LTXVConditioning` | 1 | comfy-core |
| `LTXVImgToVideoInplaceKJ` | 1 | comfyui-kjnodes |
| `LTXVPreprocess` | 1 | comfy-core |
| `PrimitiveFloat` | 1 |  |
| `SetLatentNoiseMask` | 1 | comfy-core |
| `SolidMask` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# LTX-2 Audio to Video Workflow Guide

> ⚠️ **Experimental Workflow** — This is a highly experimental workflow. Results are not guaranteed and may vary significantly between runs.

## Overview

This workflow uses **audio files to generate video from a single image**. Rather than text-to-video or image-to-video in the traditional sense, you're providing an audio track that drives the video generation process.

## Resolution Requirements

- **Maximum Resolution:** 1600×900 — exceeding this limit will produce black videos
- **If your output is black:** Stop your run immediately and reduce the resolution
- **Aspect Ratio:** Your target resolution determines the aspect ratio of the final video, so choose dimensions that match your intended output format

## Audio Requirements

- **Minimum Length:** Your input audio must be at least **48 seconds long**
- **Trimming:** Use the **Audio Crop** node to select which portion of your audio to use
- **Selection Format:** Crop times are displayed in `m:ss` format (e.g., `0:00` to `0:48`)
- **Important:** Ensure your selection is at least 48 seconds long, or the workflow will not have enough audio to complete the full generation
- **Vocal Processing:** The workflow automatically separates vocals from the audio/music, then recombines them for the final output—this allows the video generation to react correctly to vocals

## What to Expect

- **Output Duration:** Up to 48 seconds of footage generated through sequential extension runs
- **Progressive Previews:** The workflow sends preview outputs along the way, allowing you to monitor quality and stop early if the generation starts to degrade
- **Variable Results:** Due to the experimental nature, some runs will produce better results than others

## Prompting Tips

Prompting is extremely powerful in this workflow—and requires careful attention.

### Stay on Subject

If you want the video to remain focused on your subject, **explicitly mention the subject in your prompt**. Without reinforcement, the model may drift away from the original image content.

**Example:**  
If your source image is a woman playing piano, include "woman playing piano" in your prompt throughout.

### Avoid Scene Changes

Describing a different scene in your prompt will often cause the video to **immediately jump to that new scene**, which can break continuity. Be intentional—if you want smooth, coherent footage, keep your prompt consistent with the source image.

## Workflow Tips

1. **Start with a clear, well-composed source image** — The quality of your input image significantly affects output quality
2. **Watch the previews** — If you notice the video falling apart (distortion, subject loss, incoherence), stop the workflow rather than waiting for the full 48 seconds
3. **Iterate on prompts** — Small prompt changes can produce dramatically different results
4. **Expect experimentation** — This workflow rewards trial and error; don't expect perfection on the first attempt

## Summary

| Aspect | Details |
|--------|---------|
| Modality | Audio → Video (from single image) |
| Max Duration | 48 seconds |
| Generation Method | Extension runs with previews |
| Stability | Experimental |

---

*Remember: This is cutting-edge functionality. Embrace the experimentation and enjoy the creative possibilities!*

</details>

<details><summary>MarkdownNote</summary>

- **If your output is black:** Stop your run immediately and reduce the resolution

</details>

<details><summary>Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/ltx-2](https://huggingface.co/Comfy-Org/ltx-2)
- [ModelScope:Comfy-Org/ltx-2](https://modelscope.cn/models/Comfy-Org/ltx-2)

**diffusion_models**

- [ltx-2-19b-distilled_transformer_only_bf16.safetensors](https://huggingface.co/Kijai/LTXV2_comfy/resolve/main/diffusion_models/ltx-2-19b-distilled_transformer_only_bf16.safetensors) (35.17 GB)

**vae**

- [LTX2_audio_vae_bf16.safetensors](https://huggingface.co/Kijai/LTXV2_comfy/resolve/main/VAE/LTX2_audio_vae_bf16.safetensors) (207.7 MB)

- [LTX2_video_vae_bf16.safetensors](https://huggingface.co/Kijai/LTXV2_comfy/resolve/main/VAE/LTX2_video_vae_bf16.safetensors) (2.28 GB)

**text_encoders**

- [gemma_3_12B_it_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp8_scaled.safetensors) (12.3 GB)
- [ltx-2-19b-embeddings_connector_distill_bf16.safetensors](https://huggingface.co/Kijai/LTXV2_comfy/resolve/main/text_encoders/ltx-2-19b-embeddings_connector_distill_bf16.safetensors) (2.67 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── ltx-2-19b-distilled_transformer_only_bf16.safetensors
│   └── 📂 text_encoders/
│       ├── gemma_3_12B_it_fp8_scaled.safetensors
│       └── ltx-2-19b-embeddings_connector_distill_bf16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Enable Video Preview</summary>

Select and use Ctrl-B to enable/disable video output preivew

</details>
