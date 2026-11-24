# LTX-2.5: Text to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_5_t2v-1.webp" width="360" alt="LTX-2.5: Text to Video video_ltx2_5_t2v-1.webp">

> Generate cinematic video from a text prompt using LTX-2.5, a production-ready diffusion model that outputs a single video file with optional spatial upscaling for enhanced resolution. Ideal for film previsualization, commercial storyboards, and high-volume content creation pipelines.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_5_t2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_ltx2_5_t2v.json)

## Details

| | |
|---|---|
| Name | `video_ltx2_5_t2v` |
| Category | Foundation › Video |
| Media type | image |
| Models | LTX-2.5 |
| Tags | Video, Text to Video, Int8 |
| Type | open source |
| Date | 2026-08-11 |
| Author | ComfyUI |
| Download size | 49.5 GB |
| Min ComfyUI version | 0.32.0 |
| Usage | 1209 |
| Nodes | 48 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveVideo` #75 | video | video_ltx2_5_t2v.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors) |
| `ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors` | `latent_upscale_models` | [link](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors) |
| `gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors) |
| `gemma4_e2b_it_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/gemma-4/resolve/main/text_encoders/gemma4_e2b_it_int8_convrot.safetensors) |
| `ltx-2.5-audio-vae-bf16.safetensors` | `vae` | [link](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/vae/ltx-2.5-audio-vae-bf16.safetensors) |
| `ltx-2.5-video-vae-bf16.safetensors` | `vae` | [link](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/vae/ltx-2.5-video-vae-bf16.safetensors) |

## Subgraphs

- **Text to Video (LTX-2.5)** (42 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfyMathExpression` | 4 | comfy-core |
| `MarkdownNote` | 4 |  |
| `PrimitiveInt` | 4 | comfy-core |
| `CLIPLoader` | 2 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `KSamplerSelect` | 2 | comfy-core |
| `LTXVConcatAVLatent` | 2 | comfy-core |
| `LTXVDualCFGGuider` | 2 | comfy-core |
| `LTXVSeparateAVLatent` | 2 | comfy-core |
| `ManualSigmas` | 2 | comfy-core |
| `RandomNoise` | 2 | comfy-core |
| `SamplerCustomAdvanced` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `ComfySwitchNode` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `EmptyLTXVLatentVideo` | 1 | comfy-core |
| `LatentUpscaleModelLoader` | 1 | comfy-core |
| `LTXVAudioVAEDecode` | 1 | comfy-core |
| `LTXVConditioning` | 1 | comfy-core |
| `LTXVEmptyLatentAudio` | 1 | comfy-core |
| `LTXVLatentUpsampler` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |
| `ResolutionSelector` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `TextGenerateLTX2Prompt` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecodeTiled` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: About LTX-2.5</summary>

# LTX-2.5

LTX-2.5 is Lightricks' open video generation model : fast, local-first, and built for production. Run it locally, fine-tune it for your own use case, or integrate it into your pipeline.

**Key highlights:**

- **Pixel Diffusion** : keyframes-first generation that builds every scene on a grid of high-fidelity keyframes for industry-leading pixel quality
- **Diffusion Video Decoder** : sharper faces, legible text, fewer smears in fast motion
- **Native multishot** : one generation yields multiple connected shots holding character, environment, lighting, voice, and style across cuts
- **Custom Gemma 4 12B text encoder** : retains multiple subjects, actions, lighting, detail, and camera direction across complex prompts
- **Dedicated Prompt Enhancer** *(optional)* : a lightweight model that expands short prompts into rich cinematic instructions
- **Auto Duration** : predicts the right clip length from the described action before diffusion begins
- **Better distilled model** : carries far more quality, prompt adherence, and motion into a smaller, faster variant
- Carried over from LTX-2.3: native 4K, synchronized audio-video

Official model & files: https://huggingface.co/Lightricks/LTX-2.5
## What this workflow does

This **Text-to-Video** workflow generates a video directly from a text prompt. Write your prompt, optionally enable the Prompt Enhancer, and the model renders a clip with cinematic pixel quality and synchronized audio.

## Subgraph parameters

The **Text to Video (LTX-2.5)** node is a subgraph. Click the **Enter subgraph** button at the bottom of the node to open its internal graph, where you can inspect and fine-tune every step of the pipeline (conditioning, sampler, CFG guider, VAE decode, and more).

| Parameter | What it does |
|---|---|
| prompt | Text prompt describing the scene, action, lighting, camera, and style |
| prompt_enhance | *(Optional, off by default)* Toggle the built-in Prompt Enhancer, which expands short prompts into rich cinematic instructions. Requires the separate prompt enhancer model (~10 GB) below and adds ~1-2 min of generation time |
| duration | Clip length in seconds (Auto Duration can predict it from the action) |
| width / height | Output resolution in pixels (e.g. 1280×720) |
| seed | Random seed : set a fixed value to reproduce the same result |
| frame_rate | Frames per second |
| unet_name | Main model: LTX-2.5 distilled transformer (ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors) |
| video_vae | Video VAE used for decoding (ltx-2.5-video-vae-bf16.safetensors) |
| audio_vae | Audio VAE that produces synchronized audio (ltx-2.5-audio-vae-bf16.safetensors) |
| clip_name | Text encoder: custom Gemma 4 12B with projection (gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors) |
| upscale_model | Latent upscaler applied before decoding for higher-fidelity output |
| prompt_enhance_model | Model checkpoint used by the Prompt Enhancer |

## How to use

1. Download the models listed in **Note: Model Links** and place them in ComfyUI's `models/` folder (the prompt enhancer model is optional - skip it unless you enable **prompt_enhance**)
2. Write your prompt, optionally toggle **prompt_enhance** for short prompts
3. Set **duration** / **width** / **height** / **frame_rate** (defaults work well) and hit **Queue**
4. To dive deeper, click **Enter subgraph** at the bottom of the main node : every internal step (conditioning, sampler, CFG, VAE decode) can be edited there

</details>

<details><summary>Note: Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/gemma-4](https://huggingface.co/Comfy-Org/gemma-4)
- [ModelScope:Comfy-Org/gemma-4](https://modelscope.cn/models/Comfy-Org/gemma-4)

**text_encoders**

- [gemma4_e2b_it_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/gemma-4/resolve/main/text_encoders/gemma4_e2b_it_int8_convrot.safetensors) (4.84 GB) — *optional, only needed when **prompt_enhance** is enabled*
- [gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors)

**diffusion_models**

- [ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors)

**vae**

- [ltx-2.5-video-vae-bf16.safetensors](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/vae/ltx-2.5-video-vae-bf16.safetensors)
- [ltx-2.5-audio-vae-bf16.safetensors](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/vae/ltx-2.5-audio-vae-bf16.safetensors)

**latent_upscale_models**

- [ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   ├── gemma4_e2b_it_int8_convrot.safetensors
│   │   └── gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors
│   ├── 📂 diffusion_models/
│   │   └── ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors
│   ├── 📂 vae/
│   │   ├── ltx-2.5-video-vae-bf16.safetensors
│   │   └── ltx-2.5-audio-vae-bf16.safetensors
│   └── 📂 latent_upscale_models/
│       └── ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: Size Settings Reference</summary>

| megapixels | Aspect | Output (multiple=32) |
|---|---|---|
| 0.2 | 16:9 | 608 x 352 |
| 0.3 | 16:9 | 736 x 416 |
| 0.4 | 16:9 | 864 x 480 |
| 0.5 | 16:9 | 960 x 544 |
| 0.6 | 16:9 | 1056 x 608 |
| 0.7 | 16:9 | 1152 x 640 |
| 0.8 | 16:9 | 1216 x 672 |
| 0.9 | 16:9 | 1280 x 736 |
| 1.0 | 16:9 | 1376 x 768 |
| 1.2 | 16:9 | 1504 x 832 |
| 1.5 | 16:9 | 1664 x 928 |
| 1.8 | 16:9 | 1824 x 1024 |
| 2.0 | 16:9 | 1920 x 1088 |

</details>

<details><summary>Note: Model Links</summary>

Before you download all the models, please make sure you have granted access to [LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) first.

</details>
