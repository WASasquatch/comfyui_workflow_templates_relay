# LTX-2.3: FLF2V

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_ltx2_3_flf2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_flf2v-1.webp" width="360" alt="LTX-2.3: FLF2V video_ltx2_3_flf2v-1.webp">

> Upload a starting image to generate a video sequence. The workflow creates a short video with consistent style and motion, beginning with your provided frame.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_flf2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_ltx2_3_flf2v.json)

## Details

| | |
|---|---|
| Name | `video_ltx2_3_flf2v` |
| Category | Foundation › Video |
| Output | video |
| Models | LTX-2.3 |
| Tags | FLF2V, Video |
| Type | open source |
| Date | 2026-03-16 |
| Author | ComfyUI |
| Download size | 36.3 GB |
| Min ComfyUI version | 0.16.4 |
| Usage | 158 |
| Nodes | 36 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #31 | image | high_view_classic_car.png |
| input | `LoadImage` #39 | image | low_view_classic_car.png |
| output | `SaveVideo` #68 | video | video_ltx2_3_flf2v.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-2.3-22b-distilled-fp8.safetensors` | `checkpoints` | [link](https://huggingface.co/Lightricks/LTX-2.3-fp8/resolve/main/ltx-2.3-22b-distilled-fp8.safetensors) |
| `gemma_3_12B_it_fp4_mixed.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) |

## Subgraphs

- **First-Last-Frame to Video (LTX-2.3)** (32 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveInt` | 4 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `ComfyMathExpression` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `LTXVAddGuide` | 2 | comfy-core |
| `LTXVPreprocess` | 2 | comfy-core |
| `ResizeImageMaskNode` | 2 | comfy-core |
| `CFGGuider` | 1 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `EmptyLTXVLatentVideo` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `LTXAVTextEncoderLoader` | 1 | comfy-core |
| `LTXVAudioVAEDecode` | 1 | comfy-core |
| `LTXVAudioVAELoader` | 1 | comfy-core |
| `LTXVConcatAVLatent` | 1 | comfy-core |
| `LTXVConditioning` | 1 | comfy-core |
| `LTXVCropGuides` | 1 | comfy-core |
| `LTXVEmptyLatentAudio` | 1 | comfy-core |
| `LTXVSeparateAVLatent` | 1 | comfy-core |
| `ManualSigmas` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `RandomNoise` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SamplerEulerAncestral` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `VAEDecodeTiled` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model Links</summary>

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

- [ltx-2.3-22b-distilled-fp8.safetensors](https://huggingface.co/Lightricks/LTX-2.3-fp8/resolve/main/ltx-2.3-22b-distilled-fp8.safetensors) (27.5 GB)

**text_encoders**

- [gemma_3_12B_it_fp4_mixed.safetensors](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) (8.8 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │   └── ltx-2.3-22b-distilled-fp8.safetensors
│   └── 📂 text_encoders/
│       └── gemma_3_12B_it_fp4_mixed.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
