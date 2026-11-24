# LTX-2.5 DFR: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_ltx2_5_dfr_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_5_dfr_i2v-1.webp" width="360" alt="LTX-2.5 DFR: Image to Video video_ltx2_5_dfr_i2v-1.webp">

> Generate a short video with sound from a single image using LTX-2.5's DFR (Diffusion Fidelity Rendering) path: a half-resolution pass that carries generated detailing keyframes, a spatial x2 detailing pass with the pixel-spatial IC-LoRA, and an optional temporal x2 pass. Suited to cinematic shots, character beats and talking-image clips that need motion and synchronized audio.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_ltx2_5_dfr_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_ltx2_5_dfr_i2v.json)

## Details

| | |
|---|---|
| Name | `video_ltx2_5_dfr_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | LTX-2.5 |
| Tags | Image to Video, Int8, Video |
| Type | open source |
| Date | 2026-09-19 |
| Author | ComfyUI |
| Download size | 57.2 GB |
| Min ComfyUI version | 0.37.2 |
| Usage | 202 |
| Nodes | 94 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #2004 | image | office_garden_169_outpaint.png |
| output | `SaveVideo` #4852 | video | video_ltx2_5_dfr_i2v.mp4 |

## Custom nodes required

- [ComfyUI-LTXVideo](https://registry.comfy.org/nodes/ComfyUI-LTXVideo)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors) |
| `ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors` | `latent_upscale_models` | [link](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors) |
| `ltx-2.5-latent-temporal-upscaler-x2-bf16-1.0.safetensors` | `latent_upscale_models` | [link](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/latent_upscale_models/ltx-2.5-latent-temporal-upscaler-x2-bf16-1.0.safetensors) |
| `ltx-2.5-22b-ic-lora-pixel-spatial-upscaler-x2-1.0.safetensors` | `loras` | [link](https://huggingface.co/Lightricks/LTX-2.5-22b-IC-LoRA-Pixel-Spatial-Upscaler/resolve/main/ltx-2.5-22b-ic-lora-pixel-spatial-upscaler-x2-1.0.safetensors) |
| `gemma4-12b-with-proj-ltx-2.5-bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/text_encoders/gemma4-12b-with-proj-ltx-2.5-bf16.safetensors) |
| `gemma4_e2b_it_bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/gemma-4/resolve/main/text_encoders/gemma4_e2b_it_bf16.safetensors) |
| `ltx-2.5-audio-vae-bf16.safetensors` | `vae` | [link](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/vae/ltx-2.5-audio-vae-bf16.safetensors) |
| `ltx-2.5-video-vae-bf16.safetensors` | `vae` | [link](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/vae/ltx-2.5-video-vae-bf16.safetensors) |

## Subgraphs

- **Image to Video (LTX-2.5 DFR)** (88 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 6 |  |
| `ComfySwitchNode` | 5 | comfy-core |
| `ComfyMathExpression` | 4 | comfy-core |
| `PrimitiveBoolean` | 4 | comfy-core |
| `CFGGuider` | 3 | comfy-core |
| `KSamplerSelect` | 3 | comfy-core |
| `LTXVAddGeneratedKeyframes` | 3 | ComfyUI-LTXVideo |
| `LTXVConcatAVLatent` | 3 | comfy-core |
| `LTXVImgToVideoInplace` | 3 | comfy-core |
| `LTXVLatentUpsampler` | 3 | comfy-core |
| `LTXVSeparateAVLatent` | 3 | comfy-core |
| `LTXVSeparateGeneratedKeyframes` | 3 | ComfyUI-LTXVideo |
| `ManualSigmas` | 3 | comfy-core |
| `RandomNoise` | 3 | comfy-core |
| `SamplerCustomAdvanced` | 3 | comfy-core |
| `CLIPLoader` | 2 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `LatentUpscaleModelLoader` | 2 | comfy-core |
| `LTXVConditioning` | 2 | comfy-core |
| `LTXVCropGuides` | 2 | comfy-core |
| `PrimitiveFloat` | 2 |  |
| `PrimitiveStringMultiline` | 2 | comfy-core |
| `ResizeImageMaskNode` | 2 |  |
| `TextGenerateLTX2Prompt` | 2 | comfy-core |
| `VAEDecode` | 2 |  |
| `VAELoader` | 2 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `EmptyLTXVLatentVideo` | 1 | comfy-core |
| `GetImageSize` | 1 |  |
| `LatentCutToBatch` | 1 |  |
| `LoadImage` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 |  |
| `LTXVAddLatentGuide` | 1 | ComfyUI-LTXVideo |
| `LTXVAudioVAEDecode` | 1 | comfy-core |
| `LTXVEmptyLatentAudio` | 1 | comfy-core |
| `LTXVFreezeLatent` | 1 | ComfyUI-LTXVideo |
| `LTXVGeneratedKeyframesToGuides` | 1 | ComfyUI-LTXVideo |
| `LTXVPreprocess` | 1 | comfy-core |
| `Note` | 1 |  |
| `PreviewAny` | 1 |  |
| `PreviewImage` | 1 |  |
| `ResolutionSelector` | 1 |  |
| `SaveVideo` | 1 | comfy-core |
| `SeedNode` | 1 |  |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecodeTiled` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Input Asset

- [office_garden_169_outpaint.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/office_garden_169_outpaint.png)

## Model Links

- [Hugging Face:Comfy-Org/gemma-4](https://huggingface.co/Comfy-Org/gemma-4)
- [ModelScope:Comfy-Org/gemma-4](https://modelscope.cn/models/Comfy-Org/gemma-4)
- [Hugging Face:Lightricks/LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5)
- [Hugging Face:Lightricks/LTX-2.5-22b-IC-LoRA-Pixel-Spatial-Upscaler](https://huggingface.co/Lightricks/LTX-2.5-22b-IC-LoRA-Pixel-Spatial-Upscaler)

**text_encoders**

- [gemma4_e2b_it_bf16.safetensors](https://huggingface.co/Comfy-Org/gemma-4/resolve/main/text_encoders/gemma4_e2b_it_bf16.safetensors) (9.57 GB)
- [gemma4-12b-with-proj-ltx-2.5-bf16.safetensors](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/text_encoders/gemma4-12b-with-proj-ltx-2.5-bf16.safetensors)

**latent_upscale_models**

- [ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors)
- [ltx-2.5-latent-temporal-upscaler-x2-bf16-1.0.safetensors](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/latent_upscale_models/ltx-2.5-latent-temporal-upscaler-x2-bf16-1.0.safetensors)

**vae**

- [ltx-2.5-audio-vae-bf16.safetensors](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/vae/ltx-2.5-audio-vae-bf16.safetensors)
- [ltx-2.5-video-vae-bf16.safetensors](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/vae/ltx-2.5-video-vae-bf16.safetensors)

**diffusion_models**

- [ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors)

**loras**

- [ltx-2.5-22b-ic-lora-pixel-spatial-upscaler-x2-1.0.safetensors](https://huggingface.co/Lightricks/LTX-2.5-22b-IC-LoRA-Pixel-Spatial-Upscaler/resolve/main/ltx-2.5-22b-ic-lora-pixel-spatial-upscaler-x2-1.0.safetensors)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │   ├── gemma4_e2b_it_bf16.safetensors
│   │   └── gemma4-12b-with-proj-ltx-2.5-bf16.safetensors
│   ├── 📂 latent_upscale_models/
│   │   ├── ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors
│   │   └── ltx-2.5-latent-temporal-upscaler-x2-bf16-1.0.safetensors
│   ├── 📂 vae/
│   │   ├── ltx-2.5-audio-vae-bf16.safetensors
│   │   └── ltx-2.5-video-vae-bf16.safetensors
│   ├── 📂 diffusion_models/
│   │   └── ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors
│   └── 📂 loras/
│       └── ltx-2.5-22b-ic-lora-pixel-spatial-upscaler-x2-1.0.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: LTX-2.5 DFR i2v (manual)</summary>

**DFR = Diffusion Fidelity Rendering** - LTX's production-quality path: a distilled transformer plus a
detailing IC-LoRA, with extra generated keyframes and spatial (optionally temporal) detailing passes.

## What the subgraph `Image to Video (LTX-2.5 DFR)` can do

- **Image to video** from one start frame, or **text to video** with the `Switch to T2V` toggle.
- **Video with audio in a single pass** - ambience and speech; put spoken lines in quotes in the prompt.
- **Detailing keyframes** - one per second of video, denoised together with the video and then reused as
  guides in the later passes; this is where the DFR quality comes from.
- **Spatial x2 detailing** - the half-res stage-1 latent is re-injected as an IC-LoRA reference and re-sampled
  at double resolution with the pixel-spatial detailing IC-LoRA.
- **Temporal x2** - 121 -> 241 frames, 24 -> 48 fps at the same duration (can be switched off).
- **Controls** - aspect ratio and megapixel budget, fps, duration, seed, prompt, prompt enhancement, and
  tiled VAE decoding for low VRAM.

## Inputs

| Where | Control | Meaning |
|---|---|---|
| Top level | `Start image (I2V)` | first frame; ignored while `Switch to T2V` is on |
| Top level | `Output size (aspect / megapixels)` | target aspect and pixel budget, multiples of 32; stage 1 runs at half of it |
| Top level | `SeedNode` | seed; `fixed` keeps runs reproducible |
| Inside | `Prompt (positive)` / `Prompt (negative)` | text conditioning; the negative prompt is used as written |
| Inside | `Float (fps)` / `Float (Duration)` | 24 fps / 5 s by default, i.e. 121 frames |
| Inside | `Switch to T2V` | run text-to-video without using the start image |
| Inside | `Enable Prompt Enhancer` | rewrite and extend the prompt with the small gemma4 encoder first |
| Inside | `Run 3rd stage - Temporal Upscale` | off skips the temporal pass: faster, 24 fps / 121 frames |
| Inside | `Enable Tiled Decode` | tiled VAE decode - lower VRAM, slightly softer detail |

## The three stages

1. **Generate** - half resolution, **8 steps**; video, keyframe slots and audio are denoised together.
2. **Spatial x2** - latent spatial upsample, then **3 steps** with the detailing IC-LoRA; the half-res latent
   serves as the reference (`LTXVAddLatentGuide`).
3. **Temporal x2** - **4 steps** on a 241-frame / 48 fps canvas; the stage-2 keyframes return as guides at
   strength 0.95. Audio is used for cross-attention only and then dropped, so the shipped audio is still the
   stage-1 one. The step-by-step notes inside each stage group explain the mechanics.

Samplers are **euler** with **cfg 1.0** and fixed **`ManualSigmas`** schedules. The model is distilled, so the
step counts and sigmas are part of the recipe - changing them changes the look.

## Output

`Save video (mp4 + audio)` writes the mp4 (48 fps with the temporal stage, 24 fps without) and
`Preview frame` shows the final frame. Prompt-enhancer output, when enabled, is visible on
`Preview as Text (Final Prompt)`.

## Notes

- Repeating high-frequency textures and smooth gradients can "boil" or band during camera moves. A/B runs at
  the same prompt and seed - tiled decode and temporal upscale toggled separately and together - came out at
  the same level in all four variants, so this belongs to the model and the pipeline rather than to a node
  setting. Widescreen framing and gentle camera moves are the most stable, and bf16 weights are cleaner than
  int8.

Model links, folder layout and update/report links: see the note beside this one.

</details>

<details><summary>Preprocess</summary>

## Preprocess

**Video dimensions**

adjust video width and video height to determine the output dimensions.

**Image conditioning**

Adjust img_strength and img_compression to change the strength of the input image in case you provided one. Default img_strength is **1.0**.

**Detailing keyframes**

Empty generated keyframes at **1 KF per second** (skip frame 0, keep the last frame unless an image keyframe is already there). For the default 121 frames @ 24 fps that is `24,48,72,96,120`. `LTXVAddGeneratedKeyframes` places about one keyframe every 24 pixel frames after image conditions are written in place, so it will not add a keyframe on top of first/last-frame I2V. Keyframes go on the **video** latent only, then audio is concatenated.

</details>

<details><summary>Generate - stage 1</summary>

**Sample (8 steps)**

Half-res, distilled transformer. Empty detailing keyframes are denoised with the video. You can change the noise seed, the guider cfg (used for both video and audio) and select the sampler.

</details>

<details><summary>Note</summary>

```text
Do explore various samplers and cfg values (although we advise them to be kept close to 1)
```

</details>

<details><summary>Generate - stage 2</summary>

**Spatial upscale > detailing IC-LoRA > sample (3 steps)**

**Reserve** the half-res video, spatially x2-upsample video and detailing keyframes separately, then warm-start the detailing keyframes in the same positions.
The reserved half-res latent is injected with `LTXVAddLatentGuide` as an IC-LoRA reference (`VideoConditionByReferenceLatent`): dilated onto a sparse grid with RoPE expanded by the spatial ratio (x2), not pinned as a same-size frozen video. Stage 2 uses the distilled model **plus** the pixel-spatial detailing IC-LoRA, distilled Euler. Audio continues from stage 1 for cross-attn; decode keeps stage-2 audio after the temporal pass.

</details>

<details><summary>Generate - stage 3</summary>

**Temporal upscale > sample (4 steps)**

Temporal x2 the peeled stage-2 video (`241` frames @ `48` fps for the default clip). Conditioning fps is restamped to that temporal fps so RoPE is in playback time. I2V is re-applied on the x2 canvas (start-frame stays 0). Detailing keyframes from stage 2 are pinned as guides at the same moments on the x2 timeline (auto-scaled recorded indices, e.g. `48,96,144,192,240`) with strength **0.95**. Additional detailing keyframes fill the remaining 24-frame slots (e.g. `24,72,120,168,216`) from the nearest upsampled video frames. Sampler is **euler** and cfg is **1.0** on this subgraph.

**Audio used for cross-attn only.** Stage-2 audio is frozen (`noise_mask=0`) and concatenated after the extra keyframes, so the transformer can audio-cross-attend. Frame count is x2 but **duration is the same** (`(N-1)/fps`), so the audio latent is not stretched. After sampling, audio is split off and discarded; decode still uses the original stage-2 audio.

Toggle **Run Temporal Upscale (3rd stage)** in Inputs. Off skips this pass (lazy if/else inside this subgraph) and decode uses stage-2 video at the original fps.

</details>
