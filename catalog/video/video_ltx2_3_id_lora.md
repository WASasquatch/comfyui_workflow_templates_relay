# LTX-2.3: ID LoRA

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_ltx2_3_id_lora)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_id_lora-1.webp" width="360" alt="LTX-2.3: ID LoRA video_ltx2_3_id_lora-1.webp">

> Generate personalized videos with synchronized audio from a text prompt, reference image, and short audio clip. Use ID-LoRA to adapt a person's appearance and voice in a single generative model.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_3_id_lora.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_ltx2_3_id_lora.json)

## Details

| | |
|---|---|
| Name | `video_ltx2_3_id_lora` |
| Category | Foundation › Video |
| Output | video |
| Models | LTX-2.3 |
| Tags | Lip Sync, Video, Voice Cloning |
| Type | open source |
| Date | 2026-03-27 |
| Author | ComfyUI |
| Download size | 40.5 GB |
| Min ComfyUI version | 0.19.0 |
| Usage | 136 |
| Nodes | 54 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #269 | image | vintage_thinker.png |
| input | `LoadAudio` #276 | audio | ltx23_reference_audio.mp3 |
| output | `SaveVideo` #341 | video | video_ltx2_3_id_lora.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-2.3-22b-dev-fp8.safetensors` | `checkpoints` | [link](https://huggingface.co/Lightricks/LTX-2.3-fp8/resolve/main/ltx-2.3-22b-dev-fp8.safetensors) |
| `ltx-2.3-spatial-upscaler-x2-1.1.safetensors` | `latent_upscale_models` | [link](https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-spatial-upscaler-x2-1.1.safetensors) |
| `ltx-2.3-id-lora-talkvid-3k.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/ltx-2.3/resolve/main/split_files/loras/ltx-2.3-id-lora-talkvid-3k.safetensors) |
| `ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/ltx-2.3/resolve/main/split_files/loras/ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors) |
| `gemma_3_12B_it_fp4_mixed.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) |

## Subgraphs

- **Video Generation (LTX-2.3 ID LoRA)** (47 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfyMathExpression` | 4 | comfy-core |
| `MarkdownNote` | 3 |  |
| `PrimitiveInt` | 3 | comfy-core |
| `CFGGuider` | 2 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `KSamplerSelect` | 2 | comfy-core |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `LTXVConcatAVLatent` | 2 | comfy-core |
| `LTXVImgToVideoInplace` | 2 | comfy-core |
| `LTXVSeparateAVLatent` | 2 | comfy-core |
| `ManualSigmas` | 2 | comfy-core |
| `RandomNoise` | 2 | comfy-core |
| `ResizeImageMaskNode` | 2 | comfy-core |
| `SamplerCustomAdvanced` | 2 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `EmptyLTXVLatentVideo` | 1 | comfy-core |
| `LatentUpscaleModelLoader` | 1 | comfy-core |
| `LoadAudio` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LTXAVTextEncoderLoader` | 1 | comfy-core |
| `LTXVAudioVAEDecode` | 1 | comfy-core |
| `LTXVAudioVAELoader` | 1 | comfy-core |
| `LTXVConditioning` | 1 | comfy-core |
| `LTXVCropGuides` | 1 | comfy-core |
| `LTXVEmptyLatentAudio` | 1 | comfy-core |
| `LTXVLatentUpsampler` | 1 | comfy-core |
| `LTXVPreprocess` | 1 | comfy-core |
| `LTXVReferenceAudio` | 1 | comfy-core |
| `PrimitiveFloat` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |
| `RecordAudio` | 1 | comfy-core |
| `Reroute` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
| `SolidMask` | 1 | comfy-core |
| `VAEDecodeTiled` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model Links</summary>

- Huggingface: [Lightricks/LTX-2.3](https://huggingface.co/Lightricks/LTX-2.3/)
- Github: [LTX-2](https://github.com/Lightricks/LTX-2)
- [ID LoRA](https://github.com/ID-LoRA/ID-LoRA/tree/main)
## Report LTX-2.3 Issues
To report any issues when running this workflow, [go to GitHub](https://github.com/Lightricks/ComfyUI-LTXVideo/issues)

## Model Links

- [Hugging Face:Comfy-Org/ltx-2.3](https://huggingface.co/Comfy-Org/ltx-2.3)
- [ModelScope:Comfy-Org/ltx-2.3](https://modelscope.cn/models/Comfy-Org/ltx-2.3)
- [Hugging Face:Comfy-Org/ltx-2](https://huggingface.co/Comfy-Org/ltx-2)
- [ModelScope:Comfy-Org/ltx-2](https://modelscope.cn/models/Comfy-Org/ltx-2)

**checkpoints**

- [ltx-2.3-22b-dev-fp8.safetensors](https://huggingface.co/Lightricks/LTX-2.3-fp8/resolve/main/ltx-2.3-22b-dev-fp8.safetensors) (27.14 GB)

**loras**

- [ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors](https://huggingface.co/Comfy-Org/ltx-2.3/resolve/main/split_files/loras/ltx_2.3_22b_distilled_1.1_lora_dynamic_fro09_avg_rank_111_bf16.safetensors) (2.55 GB)
- [ltx-2.3-id-lora-talkvid-3k.safetensors](https://huggingface.co/Comfy-Org/ltx-2.3/resolve/main/split_files/loras/ltx-2.3-id-lora-talkvid-3k.safetensors) (1.08 GB)

**text_encoders**

- [gemma_3_12B_it_fp4_mixed.safetensors](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) (8.8 GB)

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
│   │   └── ltx-2.3-id-lora-talkvid-3k.safetensors
│   ├── 📂 text_encoders/
│   │   └── gemma_3_12B_it_fp4_mixed.safetensors
│   └── 📂 latent_upscale_models/
│       └── ltx-2.3-spatial-upscaler-x2-1.1.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>ID LoRA Prompt Format</summary>

ID-LoRA uses a structured prompt with three tagged sections:

```
[VISUAL]: <scene and appearance description>
[SPEECH]: <exact words the person should say>
[SOUNDS]: <speaker vocal style + ambient/environmental sounds>
```

| Section | What to write | Example |
|---------|--------------|---------|
| `[VISUAL]` | Shot type, subject appearance, clothing, setting, lighting, actions | *A medium shot of a woman with short black hair wearing a white blouse, standing in a modern kitchen with warm lighting and speaking calmly.* |
| `[SPEECH]` | The literal words to be spoken | *Hello everyone, welcome to our channel.* |
| `[SOUNDS]` | Speaker vocal qualities (volume, tone, distance from mic) and background sounds | *The speaker has a calm, conversational tone at moderate volume, close to the microphone. Soft birds chirping in the background.* |

**Full example:**

```
[VISUAL]: A medium shot features a young man with curly brown hair and light blue eyes, sitting on a beige couch. He is wearing a light blue shirt and a red patterned tie. His mouth is slightly open as he speaks. In the background, there is a blurry room with warm lighting.
[SPEECH]: We are proud to introduce ID-LoRA.
[SOUNDS]: The speaker has a moderate volume and a conversational tone, sounding engaged and natural. They are close to the microphone. Light, instrumental background music plays softly, creating a calm atmosphere.
```

**Tips:**
- Be descriptive in `[VISUAL]` — shot type, colors, clothing, and background details all help, mention that the person is speaking to avoid voice-overs.
- `[SPEECH]` should contain the exact transcript, not a summary.
- `[SOUNDS]` controls both the speaking style (tone, volume, mic proximity) and ambient sounds (music, nature, room noise). Describing these steers the audio generation.

</details>

<details><summary>Use your own voice.</summary>

Record your own voice and use it as the reference audio.

</details>
