# LTX-2.3 Style Transition

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_ltx2_3_style_transition)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_style_transition-1.webp" width="360" alt="LTX-2.3 Style Transition template_ltx2_3_style_transition-1.webp">

> Apply the ltx2.3-transition LoRA to create smooth style and scene transitions. This workflow uses a specialized model to blend visual elements.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_style_transition.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_ltx2_3_style_transition.json)

## Details

| | |
|---|---|
| Name | `template_ltx2_3_style_transition` |
| Category | Foundation › Video |
| Output | video |
| Models | LTX-2.3 |
| Tags | FLF2V, LoRA, Video |
| Type | open source |
| Date | 2026-03-30 |
| Author | shane |
| Download size | 36.7 GB |
| Min ComfyUI version | 0.16.4 |
| Usage | 24 |
| Nodes | 38 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #137 | image | ltx23_flf2v_last_frame.png |
| input | `LoadImage` #138 | image | ltx23_flf2v_first_frame.png |
| output | `SaveVideo` #68 | video | template_ltx2_3_style_transition.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-2.3-22b-distilled-fp8.safetensors` | `checkpoints` | [link](https://huggingface.co/Lightricks/LTX-2.3-fp8/resolve/main/ltx-2.3-22b-distilled-fp8.safetensors) |
| `ltx2.3-transition.safetensors` | `loras` | [link](https://huggingface.co/valiantcat/LTX-2.3-Transition-LORA/resolve/main/ltx2.3-transition.safetensors) |
| `gemma_3_12B_it_fp4_mixed.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) |

## Subgraphs

- **LTX-2.3 FLF2V w/ Lora** (33 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveInt` | 4 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `ComfyMathExpression` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `LTXVAddGuide` | 2 | comfy-core |
| `LTXVPreprocess` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `ResizeImageMaskNode` | 2 | comfy-core |
| `CFGGuider` | 1 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `EmptyLTXVLatentVideo` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `LTXAVTextEncoderLoader` | 1 | comfy-core |
| `LTXVAudioVAEDecode` | 1 | comfy-core |
| `LTXVAudioVAELoader` | 1 | comfy-core |
| `LTXVConcatAVLatent` | 1 | comfy-core |
| `LTXVConditioning` | 1 | comfy-core |
| `LTXVCropGuides` | 1 | comfy-core |
| `LTXVEmptyLatentAudio` | 1 | comfy-core |
| `LTXVSeparateAVLatent` | 1 | comfy-core |
| `ManualSigmas` | 1 | comfy-core |
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

**loras**

- [ltx2.3-transition.safetensors](https://huggingface.co/valiantcat/LTX-2.3-Transition-LORA/resolve/main/ltx2.3-transition.safetensors) (372.2 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │   └── ltx-2.3-22b-distilled-fp8.safetensors
│   ├── 📂 text_encoders/
│   │   └── gemma_3_12B_it_fp4_mixed.safetensors
│   └── 📂 loras/
│       └── ltx2.3-transition.safetensors
```

</details>

<details><summary>LoRA Tips</summary>

# Trigger Word
zhuanchang

If needed, place the trigger word near the end of the prompt so the base prompt still clearly describes:
- subject
- scene
- camera movement
- transformation behavior
- atmosphere

# Prompting Guide
For best results, prompts should usually contain:
1. Shot description
   Example: close-up, medium shot, wide shot, low-angle, tracking shot.
2. Subject and environment
   Describe the character, object, or scene as clearly as possible.
3. Motion or transformation process
   Explain what changes over time: identity, style, object form, scene layout, or camera trajectory.
4. Visual details
   Add texture, lighting, color, material, and spatial cues.
5. Ending trigger
   Add zhuanchang when you want the LoRA behavior to activate more strongly.

</details>
