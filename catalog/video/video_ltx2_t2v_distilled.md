# LTX-2 Text to Video (Distilled)

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_t2v_distilled-1.webp" width="360" alt="LTX-2 Text to Video (Distilled) video_ltx2_t2v_distilled-1.webp">

> Generate high-quality videos from text prompts with synchronized audio-video generation using LTX-2 distilled model. Optimized for faster generation while maintaining quality. Features expressive lip sync, dynamic motion generation, and improved speed.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_t2v_distilled.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_ltx2_t2v_distilled.json)

## Details

| | |
|---|---|
| Name | `video_ltx2_t2v_distilled` |
| Category | Foundation › Video |
| Media type | image |
| Models | LTX-2, Lightricks |
| Tags | Text to Video, Video |
| Type | open source |
| Date | 2026-01-06 |
| Author | ComfyUI |
| Download size | 35.4 GB |
| Min ComfyUI version | 0.8.0 |
| Usage | 41 |
| Nodes | 39 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-2-19b-distilled.safetensors` | `checkpoints` | [link](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-distilled.safetensors) |
| `ltx-2-spatial-upscaler-x2-1.0.safetensors` | `latent_upscale_models` | [link](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-spatial-upscaler-x2-1.0.safetensors) |
| `ltx-2-19b-lora-camera-control-dolly-left.safetensors` | `loras` | [link](https://huggingface.co/Lightricks/LTX-2-19b-LoRA-Camera-Control-Dolly-Left/resolve/main/ltx-2-19b-lora-camera-control-dolly-left.safetensors) |
| `gemma_3_12B_it_fp4_mixed.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) |

## Subgraphs

- **Text to Video (LTX 2 Distilled)** (36 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 4 |  |
| `CFGGuider` | 2 | comfy-core |
| `KSamplerSelect` | 2 | comfy-core |
| `LTXVConcatAVLatent` | 2 | comfy-core |
| `LTXVSeparateAVLatent` | 2 | comfy-core |
| `ManualSigmas` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `RandomNoise` | 2 | comfy-core |
| `SamplerCustomAdvanced` | 2 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `EmptyImage` | 1 | comfy-core |
| `EmptyLTXVLatentVideo` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageScaleBy` | 1 | comfy-core |
| `LatentUpscaleModelLoader` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `LTXAVTextEncoderLoader` | 1 | comfy-core |
| `LTXVAudioVAEDecode` | 1 | comfy-core |
| `LTXVAudioVAELoader` | 1 | comfy-core |
| `LTXVConditioning` | 1 | comfy-core |
| `LTXVEmptyLatentAudio` | 1 | comfy-core |
| `LTXVLatentUpsampler` | 1 | comfy-core |
| `PrimitiveFloat` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `VAEDecodeTiled` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model Links</summary>

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

- [ltx-2-19b-distilled.safetensors](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-distilled.safetensors) (40.31 GB)
- [ltx-2-19b-distilled-fp8.safetensors](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-distilled-fp8.safetensors) (25.22 GB)

**text_encoders**

- [gemma_3_12B_it_fp4_mixed.safetensors](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) (8.8 GB)

**loras**

- [ltx-2-19b-distilled-lora-384.safetensors](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-distilled-lora-384.safetensors) (7.15 GB)
- [ltx-2-19b-lora-camera-control-dolly-left.safetensors](https://huggingface.co/Lightricks/LTX-2-19b-LoRA-Camera-Control-Dolly-Left/resolve/main/ltx-2-19b-lora-camera-control-dolly-left.safetensors) (312.1 MB)

**latent_upscale_models**

- [ltx-2-spatial-upscaler-x2-1.0.safetensors](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-spatial-upscaler-x2-1.0.safetensors) (949.6 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │      ├── ltx-2-19b-distilled.safetensors
│   │      └── ltx-2-19b-distilled-fp8.safetensors
│   ├── 📂 text_encoders/
│   │      └── gemma_3_12B_it_fp4_mixed.safetensors
│   ├── 📂 loras/
│   │      ├── ltx-2-19b-distilled-lora-384.safetensors
│   │      └── ltx-2-19b-lora-camera-control-dolly-left.safetensors
│   └── 📂 latent_upscale_models/
│          └── ltx-2-spatial-upscaler-x2-1.0.safetensors
```

## Report other issues

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>About Size</summary>

Width & height settings must be divisible by 64.
Frame count must be divisible by 8 + 1. 


Running with invalid parameters **will not cause errors**. Instead, the flow will silently choose the closest valid parameters. 

By default, we are using 720p resolution. You can try 1920*1088 if you have a powerful GPU.

</details>

<details><summary>Frame Rate Note</summary>

Please make sure the frame rate value is the same in both boxes

</details>

<details><summary>LoRA</summary>

# Using LoRAs
**Ctrl + B to enable**

For the camera LoRA we recommend setting strength = 1

You can use LTX [Ready to use camera LoRAs](https://huggingface.co/collections/Lightricks/ltx-2)




Use a second LoRa only when the details are important in the LoRa. 

## Training
We have made available a full trainer to help you to train your own LoRA. You can [find it here](https://github.com/Lightricks/LTX-2).

</details>
