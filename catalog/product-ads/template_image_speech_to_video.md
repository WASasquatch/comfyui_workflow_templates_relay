# Generate UGC Video With Voice Clone

[← Product & Ads](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_image_speech_to_video)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_image_speech_to_video-1.webp" width="360" alt="Generate UGC Video With Voice Clone template_image_speech_to_video-1.webp">

> Upload an image to generate AI prompts and synthesize speech. Create a final video with accurate lip sync using ElevenLabs and LTX Video.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_image_speech_to_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_image_speech_to_video.json)

## Details

| | |
|---|---|
| Name | `template_image_speech_to_video` |
| Category | Applied › Product & Ads |
| Output | video |
| Models | ElevenLabs, LTX-2.3 |
| Tags | API, Lip Sync |
| Type | API |
| Date | 2026-04-06 |
| Author | sirolim |
| Download size | 45.6 GB |
| Min ComfyUI version | 0.35.2 |
| Usage | 16 |
| Nodes | 68 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #440 | image | template_image_speech_to_video_woman_holding_face_oil.png |
| input | `LoadAudio` #611 | audio | long_demo.mp3 |
| output | `SaveVideo` #479 | video | template_image_speech_to_video.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-2.3-22b-dev-fp8.safetensors` | `checkpoints` | [link](https://huggingface.co/Lightricks/LTX-2.3-fp8/resolve/main/ltx-2.3-22b-dev-fp8.safetensors) |
| `ltx-2.3-spatial-upscaler-x2-1.1.safetensors` | `latent_upscale_models` | [link](https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-spatial-upscaler-x2-1.1.safetensors) |
| `gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/loras/gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors) |
| `ltx-2.3-22b-distilled-lora-384.safetensors` | `loras` | [link](https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-22b-distilled-lora-384.safetensors) |
| `ltx-2.3-id-lora-talkvid-3k.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/ltx-2.3/resolve/main/split_files/loras/ltx-2.3-id-lora-talkvid-3k.safetensors) |
| `gemma_3_12B_it_fp4_mixed.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) |

## Subgraphs

- **Video Generation (LTX-2.3)** (52 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfyMathExpression` | 4 | comfy-core |
| `PreviewAny` | 4 | comfy-core |
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
| `RegexExtract` | 2 | comfy-core |
| `SamplerCustomAdvanced` | 2 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `ElevenLabsInstantVoiceClone` | 1 | comfy-core |
| `ElevenLabsTextToSpeech` | 1 | comfy-core |
| `ElevenLabsVoiceSelector` | 1 | comfy-core |
| `EmptyLTXVLatentVideo` | 1 | comfy-core |
| `GeminiNode` | 1 | comfy-core |
| `LatentUpscaleModelLoader` | 1 | comfy-core |
| `LoadAudio` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoraLoader` | 1 | comfy-core |
| `LTXAVTextEncoderLoader` | 1 | comfy-core |
| `LTXVAudioVAEDecode` | 1 | comfy-core |
| `LTXVAudioVAEEncode` | 1 | comfy-core |
| `LTXVAudioVAELoader` | 1 | comfy-core |
| `LTXVConditioning` | 1 | comfy-core |
| `LTXVCropGuides` | 1 | comfy-core |
| `LTXVLatentUpsampler` | 1 | comfy-core |
| `LTXVPreprocess` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `PrimitiveFloat` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |
| `Reroute` | 1 |  |
| `ResizeImageMaskNode` | 1 | comfy-core |
| `ResizeImagesByLongerEdge` | 1 | comfy-core |
| `SaveAudioMP3` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `SetLatentNoiseMask` | 1 | comfy-core |
| `SolidMask` | 1 | comfy-core |
| `TextGenerateLTX2Prompt` | 1 | comfy-core |
| `TrimAudioDuration` | 1 | comfy-core |
| `VAEDecodeTiled` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>🎙️Clone Voice</summary>

## Bring your own voice

1. Load audio
2. Connect **voice** output  to **Eleven Labs Text to Speech node**
3. Generate audio

</details>

<details><summary>Image → Speech → Video</summary>

Create UGC videos by uploading an image, clone a voice and generate a video with Eleven Labs v3 and LTX 2.3.

## How It Works

1. **Upload an image**
2. The system:
   -  Generates two prompts from your images:
      1.  A speech prompt with expression tags
      2. A scene description prompt
   - LTX 2.3 generates a video based on the image, audio and prompt

## Tips

- Works best if character in input image is "speaking"

That’s it.

Image → Speech → Video

</details>

<details><summary>Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/ltx-2](https://huggingface.co/Comfy-Org/ltx-2)
- [ModelScope:Comfy-Org/ltx-2](https://modelscope.cn/models/Comfy-Org/ltx-2)
- [Hugging Face:Comfy-Org/ltx-2.3](https://huggingface.co/Comfy-Org/ltx-2.3)
- [ModelScope:Comfy-Org/ltx-2.3](https://modelscope.cn/models/Comfy-Org/ltx-2.3)

**latent_upscale_models**

- [ltx-2.3-spatial-upscaler-x2-1.1.safetensors](https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-spatial-upscaler-x2-1.1.safetensors) (949.6 MB)

**checkpoints**

- [ltx-2.3-22b-dev-fp8.safetensors](https://huggingface.co/Lightricks/LTX-2.3-fp8/resolve/main/ltx-2.3-22b-dev-fp8.safetensors) (27.14 GB)

**text_encoders**

- [gemma_3_12B_it_fp4_mixed.safetensors](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) (8.8 GB)

**loras**

- [gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/loras/gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors) (599.1 MB)
- [ltx-2.3-22b-distilled-lora-384.safetensors](https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-22b-distilled-lora-384.safetensors) (7.08 GB)
- [ltx-2.3-id-lora-talkvid-3k.safetensors](https://huggingface.co/Comfy-Org/ltx-2.3/resolve/main/split_files/loras/ltx-2.3-id-lora-talkvid-3k.safetensors) (1.08 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 latent_upscale_models/
│   │   └── ltx-2.3-spatial-upscaler-x2-1.1.safetensors
│   ├── 📂 checkpoints/
│   │   └── ltx-2.3-22b-dev-fp8.safetensors
│   ├── 📂 text_encoders/
│   │   └── gemma_3_12B_it_fp4_mixed.safetensors
│   └── 📂 loras/
│       ├── gemma-3-12b-it-abliterated_lora_rank64_bf16.safetensors
│       ├── ltx-2.3-22b-distilled-lora-384.safetensors
│       └── ltx-2.3-id-lora-talkvid-3k.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
