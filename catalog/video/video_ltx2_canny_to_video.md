# LTX-2 Canny to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_ltx2_canny_to_video)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_canny_to_video-1.webp" width="360" alt="LTX-2 Canny to Video video_ltx2_canny_to_video-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_canny_to_video-2.webp" width="360" alt="LTX-2 Canny to Video video_ltx2_canny_to_video-2.webp">

> Generate high-quality videos from edge detection (Canny) guidance with synchronized audio-video generation using LTX-2. Features precise edge control, structural consistency, and efficient performance.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_canny_to_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_ltx2_canny_to_video.json)

## Details

| | |
|---|---|
| Name | `video_ltx2_canny_to_video` |
| Category | Foundation › Video |
| Output | video |
| Models | LTX-2, Lightricks |
| Tags | ControlNet, Video |
| Type | open source |
| Date | 2026-01-06 |
| Author | ComfyUI |
| Download size | 35.4 GB |
| Min ComfyUI version | 0.22.0 |
| Usage | 14 |
| Nodes | 93 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #127 | video | squirrel_in_flower_garden.mp4 |
| input | `LoadImage` #160 | image | ltx_2_canny_1st_frame.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-2-19b-dev-fp8.safetensors` | `checkpoints` | [link](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-dev-fp8.safetensors) |
| `ltx-2-19b-distilled.safetensors` | `checkpoints` | [link](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-distilled.safetensors) |
| `ltx-2-spatial-upscaler-x2-1.0.safetensors` | `latent_upscale_models` | [link](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-spatial-upscaler-x2-1.0.safetensors) |
| `ltx-2-19b-distilled-lora-384.safetensors` | `loras` | [link](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-distilled-lora-384.safetensors) |
| `ltx-2-19b-ic-lora-canny-control.safetensors` | `loras` | [link](https://huggingface.co/Lightricks/LTX-2-19b-IC-LoRA-Canny-Control/resolve/main/ltx-2-19b-ic-lora-canny-control.safetensors) |
| `gemma_3_12B_it_fp4_mixed.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) |

## Subgraphs

- **Canny to Video (LTX 2.0)** (39 nodes)
- **Canny to Video (LTX 2.0 Distilled)** (37 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveInt` | 5 | comfy-core |
| `CFGGuider` | 4 | comfy-core |
| `KSamplerSelect` | 4 | comfy-core |
| `LTXVConcatAVLatent` | 4 | comfy-core |
| `LTXVImgToVideoInplace` | 4 | comfy-core |
| `LTXVSeparateAVLatent` | 4 | comfy-core |
| `RandomNoise` | 4 | comfy-core |
| `SamplerCustomAdvanced` | 4 | comfy-core |
| `CLIPTextEncode` | 3 | comfy-core |
| `LoraLoaderModelOnly` | 3 | comfy-core |
| `ManualSigmas` | 3 | comfy-core |
| `MarkdownNote` | 3 |  |
| `CheckpointLoaderSimple` | 2 | comfy-core |
| `CreateVideo` | 2 | comfy-core |
| `EmptyLTXVLatentVideo` | 2 | comfy-core |
| `GetImageSize` | 2 | comfy-core |
| `LatentUpscaleModelLoader` | 2 | comfy-core |
| `LTXAVTextEncoderLoader` | 2 | comfy-core |
| `LTXVAddGuide` | 2 | comfy-core |
| `LTXVAudioVAEDecode` | 2 | comfy-core |
| `LTXVAudioVAELoader` | 2 | comfy-core |
| `LTXVConditioning` | 2 | comfy-core |
| `LTXVCropGuides` | 2 | comfy-core |
| `LTXVEmptyLatentAudio` | 2 | comfy-core |
| `LTXVLatentUpsampler` | 2 | comfy-core |
| `PrimitiveFloat` | 2 | comfy-core |
| `Reroute` | 2 |  |
| `ResizeImageMaskNode` | 2 | comfy-core |
| `SaveVideo` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VAEDecodeTiled` | 2 | comfy-core |
| `Canny` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `ImageFromBatch` | 1 | comfy-core |
| `ImageScaleBy` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `LTXVScheduler` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>About Size</summary>

Width & height settings must be divisible by 64.
Frame count must be divisible by 8 + 1. 


Running with invalid parameters **will not cause errors**. Instead, the flow will silently choose the closest valid parameters. 

By default, we are using 720p resolution. You can try 1920*1088 if you have a powerful GPU.

</details>

<details><summary>MarkdownNote</summary>

- Huggingface: [Lightricks/LTX-2](https://huggingface.co/Lightricks/LTX-2)
- Github: [LTX-2](https://github.com/Lightricks/LTX-2)

## LTX-2 Prompting Tips

1. **Core Actions**: Describe events and actions as they occur over time  
2. **Visual Details**: Describe all visual details you want to appear in the video  
3. **Audio**: Describe sounds and dialogue needed for the scene

## Report LTX-2 Issues
To report any issues when running this workflow, [go to GitHub](https://github.com/Lightricks/ComfyUI-LTXVideo/issues)

## Model Links

- [Hugging Face:Comfy-Org/ltx-2](https://huggingface.co/Comfy-Org/ltx-2)

### Alternative Repos

- [ModelScope:Comfy-Org/ltx-2](https://modelscope.cn/models/Comfy-Org/ltx-2)

**checkpoints**

- [ltx-2-19b-dev.safetensors](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-dev.safetensors) (40.31 GB)
- [ltx-2-19b-dev-fp8.safetensors](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-dev-fp8.safetensors) (25.22 GB)
- [ltx-2-19b-distilled.safetensors](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-distilled.safetensors) (40.31 GB)
- [ltx-2-19b-distilled-fp8.safetensors](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-distilled-fp8.safetensors) (25.22 GB)

**text_encoders**

- [gemma_3_12B_it_fp4_mixed.safetensors](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) (8.8 GB)

**loras**

- [ltx-2-19b-distilled-lora-384.safetensors](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-distilled-lora-384.safetensors) (7.15 GB)
- [ltx-2-19b-ic-lora-canny-control.safetensors](https://huggingface.co/Lightricks/LTX-2-19b-IC-LoRA-Canny-Control/resolve/main/ltx-2-19b-ic-lora-canny-control.safetensors) (624.1 MB)

**latent_upscale_models**

- [ltx-2-spatial-upscaler-x2-1.0.safetensors](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-spatial-upscaler-x2-1.0.safetensors) (949.6 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │      ├── ltx-2-19b-dev.safetensors
│   │      ├── ltx-2-19b-dev-fp8.safetensors
│   │      ├── ltx-2-19b-distilled.safetensors
│   │      └── ltx-2-19b-distilled-fp8.safetensors
│   ├── 📂 text_encoders/
│   │      └── gemma_3_12B_it_fp4_mixed.safetensors
│   ├── 📂 loras/
│   │      ├── ltx-2-19b-distilled-lora-384.safetensors
│   │      └── ltx-2-19b-ic-lora-canny-control.safetensors
│   └── 📂 latent_upscale_models/
│          └── ltx-2-spatial-upscaler-x2-1.0.safetensors
```

## Report issue

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Frame Rate Note</summary>

Please make sure the frame rate value is the same in both boxes

</details>
