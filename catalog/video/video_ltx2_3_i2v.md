# LTX-2.3: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_ltx2_3_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_i2v-1.webp" width="360" alt="LTX-2.3: Image to Video video_ltx2_3_i2v-1.webp">

> Upload an image to generate a video with improved motion consistency and fine details, including enhanced support for portrait formats and audio quality.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_ltx2_3_i2v.json)

## Details

| | |
|---|---|
| Name | `video_ltx2_3_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | LTX-2.3, Lightricks |
| Tags | Image to Video, Video |
| Type | open source |
| Date | 2026-03-05 |
| Author | ComfyUI |
| Download size | 44.0 GB |
| Min ComfyUI version | 0.21.0 |
| Usage | 14661 |
| Nodes | 53 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #269 | image | egyptian_queen.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-2.3-22b-dev-fp8.safetensors` | `checkpoints` | [link](https://huggingface.co/Lightricks/LTX-2.3-fp8/resolve/main/ltx-2.3-22b-dev-fp8.safetensors) |
| `ltx-2.3-spatial-upscaler-x2-1.1.safetensors` | `latent_upscale_models` | [link](https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-spatial-upscaler-x2-1.1.safetensors) |
| `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/loras/gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors) |
| `ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/ltx-2.3/resolve/main/split_files/loras/ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors) |
| `gemma_3_12B_it_fp4_mixed.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) |

## Subgraphs

- **Image to Video (LTX-2.3)** (50 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfyMathExpression` | 4 | comfy-core |
| `PrimitiveInt` | 4 | comfy-core |
| `CFGGuider` | 2 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `KSamplerSelect` | 2 | comfy-core |
| `LTXVConcatAVLatent` | 2 | comfy-core |
| `LTXVImgToVideoInplace` | 2 | comfy-core |
| `LTXVSeparateAVLatent` | 2 | comfy-core |
| `ManualSigmas` | 2 | comfy-core |
| `PrimitiveBoolean` | 2 | comfy-core |
| `RandomNoise` | 2 | comfy-core |
| `ResizeImageMaskNode` | 2 | comfy-core |
| `SamplerCustomAdvanced` | 2 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `ComfySwitchNode` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `EmptyLTXVLatentVideo` | 1 | comfy-core |
| `LatentUpscaleModelLoader` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoraLoader` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `LTXAVTextEncoderLoader` | 1 | comfy-core |
| `LTXVAudioVAEDecode` | 1 | comfy-core |
| `LTXVAudioVAELoader` | 1 | comfy-core |
| `LTXVConditioning` | 1 | comfy-core |
| `LTXVCropGuides` | 1 | comfy-core |
| `LTXVEmptyLatentAudio` | 1 | comfy-core |
| `LTXVLatentUpsampler` | 1 | comfy-core |
| `LTXVPreprocess` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `PreviewAny` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |
| `Reroute` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
| `TextGenerateLTX2Prompt` | 1 | comfy-core |
| `VAEDecodeTiled` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model Links</summary>

- Huggingface: [Lightricks/LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3/)
- Github: [LTX-2](https://github.com/Lightricks/LTX-2)

## LTX-2.3 Prompting Tips

1. **Core Actions**: Describe events and actions as they occur over time  
2. **Visual Details**: Describe all visual details you want to appear in the video  
3. **Audio**: Describe sounds and dialogue needed for the scene

## Report LTX-2.3 Issues
To report any issues when running this workflow, [go to GitHub](https://github.com/Lightricks/ComfyUI-LTXVideo/issues)

## Model Links (for Local Users)

- [Hugging Face:Comfy-Org/ltx-2.3](https://huggingface.co/Comfy-Org/ltx-2.3)
- [ModelScope:Comfy-Org/ltx-2.3](https://modelscope.cn/models/Comfy-Org/ltx-2.3)
- [Hugging Face:Comfy-Org/ltx-2](https://huggingface.co/Comfy-Org/ltx-2)
- [ModelScope:Comfy-Org/ltx-2](https://modelscope.cn/models/Comfy-Org/ltx-2)

**checkpoints**

- [ltx-2.3-22b-dev-fp8.safetensors](https://huggingface.co/Lightricks/LTX-2.3-fp8/resolve/main/ltx-2.3-22b-dev-fp8.safetensors) (27.14 GB)

**loras**

- [ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors](https://huggingface.co/Comfy-Org/ltx-2.3/resolve/main/split_files/loras/ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors) (2.55 GB)
- [gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/loras/gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors) (599.1 MB)

**latent_upscale_models**

- [ltx-2.3-spatial-upscaler-x2-1.1.safetensors](https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-spatial-upscaler-x2-1.1.safetensors) (949.6 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │   └── ltx-2.3-22b-dev-fp8.safetensors
│   ├── 📂 loras/
│   │   ├── ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors
│   │   └── gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors
│   └── 📂 latent_upscale_models/
│       └── ltx-2.3-spatial-upscaler-x2-1.1.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
