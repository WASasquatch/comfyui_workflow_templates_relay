# Squish Anything with LTX-2 I2V and LoRA

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_ltx2_i2v_lora)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_i2v_lora-1.webp" width="360" alt="Squish Anything with LTX-2 I2V and LoRA video_ltx2_i2v_lora-1.webp">

> Upload any image to apply the Squish It LoRA effect. Generate a squished animation using the LTX-2 I2V model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_i2v_lora.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_ltx2_i2v_lora.json)

## Details

| | |
|---|---|
| Name | `video_ltx2_i2v_lora` |
| Category | Foundation › Video |
| Output | video |
| Models | LTX-2 |
| Tags | Image to Video |
| Type | open source |
| Date | 2026-02-09 |
| Author | ComfyUI |
| Download size | 96.7 GB |
| Min ComfyUI version | 0.8.0 |
| Usage | 11 |
| Nodes | 48 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #98 | image | puppy_with_blue_bandana.png |
| output | `SaveVideo` #75 | video | video_ltx2_i2v_lora.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-2-19b-dev.safetensors` | `checkpoints` | [link](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-dev.safetensors) |
| `ltx-2-spatial-upscaler-x2-1.0.safetensors` | `latent_upscale_models` | [link](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-spatial-upscaler-x2-1.0.safetensors) |
| `ltx-2-19b-distilled-lora-384.safetensors` | `loras` | [link](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-distilled-lora-384.safetensors) |
| `ltx2-squish.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/loras/ltx2-squish.safetensors) |
| `gemma_3_12B_it.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it.safetensors) |

## Subgraphs

- **Text to Video (LTX 2.0)** (44 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoraLoaderModelOnly` | 4 | comfy-core |
| `MarkdownNote` | 4 |  |
| `CFGGuider` | 2 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `KSamplerSelect` | 2 | comfy-core |
| `LTXVConcatAVLatent` | 2 | comfy-core |
| `LTXVSeparateAVLatent` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `RandomNoise` | 2 | comfy-core |
| `SamplerCustomAdvanced` | 2 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `EmptyImage` | 1 | comfy-core |
| `EmptyLTXVLatentVideo` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageScaleBy` | 1 | comfy-core |
| `ImageScaleToMaxDimension` | 1 | comfy-core |
| `LatentUpscaleModelLoader` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LTXAVTextEncoderLoader` | 1 | comfy-core |
| `LTXVAudioVAEDecode` | 1 | comfy-core |
| `LTXVAudioVAELoader` | 1 | comfy-core |
| `LTXVConditioning` | 1 | comfy-core |
| `LTXVCropGuides` | 1 | comfy-core |
| `LTXVEmptyLatentAudio` | 1 | comfy-core |
| `LTXVImgToVideoInplace` | 1 | comfy-core |
| `LTXVLatentUpsampler` | 1 | comfy-core |
| `LTXVPreprocess` | 1 | comfy-core |
| `LTXVScheduler` | 1 | comfy-core |
| `ManualSigmas` | 1 | comfy-core |
| `PrimitiveFloat` | 1 | comfy-core |
| `Reroute` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
| `VAEDecodeTiled` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>About Size</summary>

Width & height settings must be divisible by 64.
Frame count must be divisible by 8 + 1. 


Running with invalid parameters **will not cause errors**. Instead, the flow will silently choose the closest valid parameters. 

By default, we are using 720p resolution. You can try 1920*1088 if you have a powerful GPU.

</details>

<details><summary>Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

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

**loras**

- [ltx-2-19b-distilled-lora-384.safetensors](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-19b-distilled-lora-384.safetensors) (7.15 GB)
- [ltx2-squish.safetensors](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/loras/ltx2-squish.safetensors) (408.3 MB)

**latent_upscale_models**

- [ltx-2-spatial-upscaler-x2-1.0.safetensors](https://huggingface.co/Lightricks/LTX-2/resolve/main/ltx-2-spatial-upscaler-x2-1.0.safetensors) (949.6 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │   └── ltx-2-19b-dev.safetensors
│   ├── 📂 loras/
│   │   ├── ltx-2-19b-distilled-lora-384.safetensors
│   │   └── ltx2-squish.safetensors
│   └── 📂 latent_upscale_models/
│       └── ltx-2-spatial-upscaler-x2-1.0.safetensors
```

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
