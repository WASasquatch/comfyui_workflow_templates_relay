# Causal Forcing: Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_causal_forcing_i2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_causal_forcing_i2v-1.webp" width="360" alt="Causal Forcing: Image to Video video_causal_forcing_i2v-1.webp">

> Input a text prompt and select a model checkpoint. Generate a high-quality video using Causal Forcing or Causal Forcing++ with 1 to 4 inference steps.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_causal_forcing_i2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_causal_forcing_i2v.json)

## Details

| | |
|---|---|
| Name | `video_causal_forcing_i2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.1 |
| Tags | Image to Video |
| Type | open source |
| Date | 2026-03-31 |
| Author | ComfyUI |
| Download size | 11.8 GB |
| Min ComfyUI version | 0.21.0 |
| Usage | 68 |
| Nodes | 19 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #18 | image | girl_riding_a_wolf.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `causal_forcing-framewise.safetensors` | `diffusion_models` | [link](https://huggingface.co/TalmajM/causal_forcing_framewise_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/causal_forcing-framewise.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Subgraphs

- **Image to Video (Causal Forcing Framewise)** (15 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `ARVideoI2V` | 1 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `CFGGuider` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `ComfyMathExpression` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `PrimitiveFloat` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `SamplerARVideo` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

**diffusion_models**

- [causal_forcing-framewise.safetensors](https://huggingface.co/TalmajM/causal_forcing_framewise_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/causal_forcing-framewise.safetensors) (5.29 GB)

**vae**

- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) (242.1 MB)

**text_encoders**

- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) (6.27 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── causal_forcing-framewise.safetensors
│   ├── 📂 vae/
│   │   └── wan_2.1_vae.safetensors
│   └── 📂 text_encoders/
│       └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: Causal Forcing Framewise</summary>

## About Causal Forcing

[Causal Forcing](https://github.com/thu-ml/Causal-Forcing) is an open-source video generation method from Tsinghua University. It uses **Causal ODE** or **Causal Consistency Distillation** to distill autoregressive diffusion models into a few-step generator, enabling high-quality real-time interactive video generation.

Compared to earlier methods like Self Forcing, Causal Forcing delivers better visual quality and motion dynamics at the same training budget and inference speed.

**This workflow template is image-to-video (I2V) only** — it takes a starting image and animates it with a text prompt. It uses the **Causal Forcing Framewise 4-step** checkpoint with Wan 2.1 components.

## Duration Limit

**The maximum output length in this template is about 5 seconds.**

- Output is encoded at **16 fps** (`CreateVideo`)
- Frame count is computed as `min(duration × 16 + 1, 81)`
- The cap of **81 frames** corresponds to roughly **5 seconds** of video

Adjust the **duration** input on the subgraph (default: 5). Values above ~5 s will still be clamped to 81 frames.

## How to Use

1. **Load Image** — upload the first frame of your video
2. **Image to Video (Causal Forcing Framewise)** subgraph — set the main controls:
   - **first_frame** — connected from Load Image
   - **positive_prompt** — describe the motion and scene you want
   - **width / height** — output resolution (default 832 × 480)
   - **duration** — length in seconds (default 5, max ~5)
   - **noise_seed** — change to get different results
3. **Save Video** — output is saved under `video/CausalForcing_I2V`

The **negative prompt** is preset inside the subgraph and is not exposed as an input. Edit it inside the subgraph if you need to customize it.

## Sampling Settings (inside subgraph)

These are pre-tuned for the framewise 4-step checkpoint and generally should not be changed:

- **4 sampling steps** (`BasicScheduler`)
- **CFG = 1** (`CFGGuider`) — classifier-free guidance is disabled
- **SamplerARVideo** — autoregressive frame-by-frame generation

## Tips

- Write prompts that describe **motion and camera behavior**, not just the static image content
- Match your input image aspect ratio to **width / height** for best results
- For longer videos, see the upstream project's [long video generation](https://github.com/thu-ml/Causal-Forcing) extensions (Rolling Forcing, etc.)

</details>
