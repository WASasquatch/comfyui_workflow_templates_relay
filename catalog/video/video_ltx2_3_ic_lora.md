# LTX 2.3 IC-LoRA Union Control

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_ic_lora-1.webp" width="360" alt="LTX 2.3 IC-LoRA Union Control video_ltx2_3_ic_lora-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_ic_lora-2.webp" width="360" alt="LTX 2.3 IC-LoRA Union Control video_ltx2_3_ic_lora-2.webp">

> Generate LTX 2.3 videos with IC-LoRA using aligned control inputs like depth, pose, or edges.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_ic_lora.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_ltx2_3_ic_lora.json)

## Details

| | |
|---|---|
| Name | `video_ltx2_3_ic_lora` |
| Category | Foundation › Video |
| Media type | image |
| Models | LTX-2.3 |
| Tags | ControlNet, Video |
| Type | open source |
| Date | 2026-04-25 |
| Author | ComfyUI |
| Download size | 38.1 GB |
| Min ComfyUI version | 0.22.0 |
| Usage | 89 |
| Nodes | 48 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #199 | video | stone_ruins.mp4 |
| input | `LoadImage` #200 | image | the_forgotten_gate.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-2.3-22b-distilled-fp8.safetensors` | `checkpoints` | [link](https://huggingface.co/Lightricks/LTX-2.3-fp8/resolve/main/ltx-2.3-22b-distilled-fp8.safetensors) |
| `moge_2_vitl_normal_fp16.safetensors` | `geometry_estimation` | [link](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_2_vitl_normal_fp16.safetensors) |
| `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/loras/gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors) |
| `ltx-2.3-22b-ic-lora-union-control-ref0.5.safetensors` | `loras` | [link](https://huggingface.co/Lightricks/LTX-2.3-22b-IC-LoRA-Union-Control/resolve/main/ltx-2.3-22b-ic-lora-union-control-ref0.5.safetensors) |
| `gemma_3_12B_it_fp4_mixed.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) |

## Subgraphs

- **First-Last-Frame to Video (LTX-2.3)** (29 nodes)
- **Video Depth Estimation (MoGe)** (12 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 | comfy-core |
| `MoGeRender` | 3 | comfy-core |
| `PrimitiveInt` | 3 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `ComfyMathExpression` | 2 | comfy-core |
| `GetImageSize` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `EmptyLTXVLatentVideo` | 1 | comfy-core |
| `GetICLoRAParameters` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `ImageToMask` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadMoGeModel` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `LoraLoader` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `LTXAVTextEncoderLoader` | 1 | comfy-core |
| `LTXVAddGuide` | 1 | comfy-core |
| `LTXVAudioVAEDecode` | 1 | comfy-core |
| `LTXVAudioVAELoader` | 1 | comfy-core |
| `LTXVConcatAVLatent` | 1 | comfy-core |
| `LTXVConditioning` | 1 | comfy-core |
| `LTXVCropGuides` | 1 | comfy-core |
| `LTXVEmptyLatentAudio` | 1 | comfy-core |
| `LTXVImgToVideoInplace` | 1 | comfy-core |
| `LTXVSeparateAVLatent` | 1 | comfy-core |
| `MoGeInference` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `ResizeImageMaskNode` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
| `TextGenerateLTX2Prompt` | 1 | comfy-core |
| `VAEDecodeTiled` | 1 | comfy-core |
| `Video Slice` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model Links</summary>

- Huggingface: [Lightricks/LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3/)
- Github: [LTX-2](https://github.com/Lightricks/LTX-2)
- IC-LoRA model page: [Lightricks/LTX-2.3-22b-IC-LoRA-Union-Control](https://huggingface.co/Lightricks/LTX-2.3-22b-IC-LoRA-Union-Control)

## LTX-2.3 Prompting Tips

1. **Core Actions**: Describe events and actions as they occur over time  
2. **Visual Details**: Describe all visual details you want to appear in the video  
3. **Audio**: Describe sounds and dialogue needed for the scene

## Report LTX-2.3 Issues
To report any issues when running this workflow, [go to GitHub](https://github.com/Lightricks/ComfyUI-LTXVideo/issues)

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/ltx-2](https://huggingface.co/Comfy-Org/ltx-2)
- [ModelScope:Comfy-Org/ltx-2](https://modelscope.cn/models/Comfy-Org/ltx-2)
- [Hugging Face:Comfy-Org/MoGe](https://huggingface.co/Comfy-Org/MoGe)
- [ModelScope:Comfy-Org/MoGe](https://modelscope.cn/models/Comfy-Org/MoGe)

**checkpoints**

- [ltx-2.3-22b-distilled-fp8.safetensors](https://huggingface.co/Lightricks/LTX-2.3-fp8/resolve/main/ltx-2.3-22b-distilled-fp8.safetensors) (27.5 GB)

**text_encoders**

- [gemma_3_12B_it_fp4_mixed.safetensors](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) (8.8 GB)

**loras**

- [ltx-2.3-22b-ic-lora-union-control-ref0.5.safetensors](https://huggingface.co/Lightricks/LTX-2.3-22b-IC-LoRA-Union-Control/resolve/main/ltx-2.3-22b-ic-lora-union-control-ref0.5.safetensors) (624.1 MB)
- [gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/loras/gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors) (599.1 MB)

**geometry_estimation**

- [moge_2_vitl_normal_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_2_vitl_normal_fp16.safetensors) (631.2 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │   └── ltx-2.3-22b-distilled-fp8.safetensors
│   ├── 📂 text_encoders/
│   │   └── gemma_3_12B_it_fp4_mixed.safetensors
│   ├── 📂 loras/
│   │   ├── ltx-2.3-22b-ic-lora-union-control-ref0.5.safetensors
│   │   └── gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors
│   └── 📂 geometry_estimation/
│       └── moge_2_vitl_normal_fp16.safetensors
```

</details>

<details><summary>Note: IC-LoRA</summary>

## IC-LoRA

### What This Model Is
`ltx-2.3-22b-ic-lora-union-control-ref0.5.safetensors` is an In-Context LoRA trained on top of LTX-2.3. It adds aligned reference control on top of the base video model and is designed for control-style guidance such as Canny, Depth, and Pose. This model expects a reference downscale factor of `0.5`.

### What It Can Do
- Guide generation with aligned control frames while still following the text prompt.
- Preserve the structure and motion hinted by the control sequence.
- Work well for reference-driven video generation where timing matters.

### Inputs Used In This Workflow
- `first_frame`: sets the starting appearance and composition.
- `control_images`: the aligned control sequence used by IC-LoRA guidance.
- `prompt`: describes the subject, motion, and scene.
- `prompt_enhance`: rewrites or expands the prompt text before sampling.
- `ckpt_name`: selects the base LTX-2.3 checkpoint.
- `ic_lora`: selects the IC-LoRA weights.
- `lora_strength`: controls how strongly the IC-LoRA guide is followed.
- `fps`: controls output playback rate.

### Workflow Usage Notes
- In this workflow, `control_images` comes from the video preprocessing branch and is used as the IC-LoRA guide.
- This depth-guided setup is only one example. Users can swap in other preprocessors and other control types as long as they produce frame-aligned `control_images`.
- Different preprocessors emphasize different guidance signals, for example depth for structure, pose for body motion, or edge-based controls for contours.
- Keep `control_images` temporally aligned with the motion you want to generate.
- `lora_strength` higher: stronger guide following. Lower: more freedom from the guide.
- `prompt_enhance` changes the prompt text only. It does not change guide timing or frame count.
- All model download links are listed in the `Model Links` note.

### Length Control
- The generated video length is controlled by the video node branch, especially the `LoadVideo` / `Video Slice` path that provides the control sequence.
- To change the generated duration, change the source control video or the slice length in that video branch.
- Changing `ic_lora`, `lora_strength`, or `prompt_enhance` will not change the number of guided frames.

</details>
