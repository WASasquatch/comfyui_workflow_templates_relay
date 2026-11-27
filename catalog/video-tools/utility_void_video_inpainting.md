# Video Inpainting: VOID

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_void_video_inpainting)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_void_video_inpainting-1.webp" width="360" alt="Video Inpainting: VOID utility_void_video_inpainting-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_void_video_inpainting-2.webp" width="360" alt="Video Inpainting: VOID utility_void_video_inpainting-2.webp">

> Upload a video and mask the object you want to remove. Generate a clean video with the object and its physical interactions deleted.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_void_video_inpainting.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_void_video_inpainting.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/void-video-inpainting)

## Details

| | |
|---|---|
| Name | `utility_void_video_inpainting` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | VOID |
| Tags | Video Edit, Inpainting |
| Type | open source |
| Date | 2026-05-14 |
| Author | ComfyUI |
| Download size | 31.9 GB |
| Min ComfyUI version | 0.21.0 |
| Usage | 146 |
| Nodes | 44 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #4 | video | snowboarder.mp4 |
| output | `SaveVideo` #38 | video | utility_void_video_inpainting.mp4 |
| output | `SaveVideo` #48 | video | utility_void_video_inpainting.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sam3.1_multiplex_fp16.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors) |
| `void_pass1.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/void-model/resolve/main/diffusion_models/void_pass1.safetensors) |
| `void_pass2.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/void-model/resolve/main/diffusion_models/void_pass2.safetensors) |
| `raft_large_C_T_SKHT_V2-ff5fadd5.safetensors` | `optical_flow` | [link](https://huggingface.co/Comfy-Org/void-model/resolve/main/optical_flow/raft_large_C_T_SKHT_V2-ff5fadd5.safetensors) |
| `t5xxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) |
| `cogvideox_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/void-model/resolve/main/vae/cogvideox_vae.safetensors) |

## Subgraphs

- **Image Segmentation (SAM3)** (3 nodes)
- **Video Inpaint (VOID)** (37 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveInt` | 4 | comfy-core |
| `CLIPTextEncode` | 3 | comfy-core |
| `BasicScheduler` | 2 | comfy-core |
| `CFGGuider` | 2 | comfy-core |
| `ComfyMathExpression` | 2 | comfy-core |
| `CreateVideo` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `SamplerCustomAdvanced` | 2 | comfy-core |
| `SaveVideo` | 2 | comfy-core |
| `UNETLoader` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VOIDSampler` | 2 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `ComfySwitchNode` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `ImageFromBatch` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `MaskPreview` | 1 | comfy-core |
| `OpticalFlowLoader` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `SAM3_Detect` | 1 | comfy-core |
| `TrimAudioDuration` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `VOIDInpaintConditioning` | 1 | comfy-core |
| `VOIDWarpedNoise` | 1 | comfy-core |
| `VOIDWarpedNoiseSource` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Related PR: [#13403](https://github.com/Comfy-Org/ComfyUI/pull/13403)

## Model Links

- [Hugging Face:Comfy-Org/sam3.1](https://huggingface.co/Comfy-Org/sam3.1)
- [Hugging Face:Comfy-Org/void-model](https://huggingface.co/Comfy-Org/void-model)

### Alternative Repos

- [ModelScope:Comfy-Org/sam3.1](https://modelscope.cn/models/Comfy-Org/sam3.1)
- [ModelScope:Comfy-Org/void-model](https://modelscope.cn/models/Comfy-Org/void-model)

**checkpoints**

- [sam3.1_multiplex_fp16.safetensors](https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors) (1.63 GB)

**text_encoders**

- [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) (9.12 GB)

**vae**

- [cogvideox_vae.safetensors](https://huggingface.co/Comfy-Org/void-model/resolve/main/vae/cogvideox_vae.safetensors) (411.2 MB)

**optical_flow**

- [raft_large_C_T_SKHT_V2-ff5fadd5.safetensors](https://huggingface.co/Comfy-Org/void-model/resolve/main/optical_flow/raft_large_C_T_SKHT_V2-ff5fadd5.safetensors) (20.1 MB)

**diffusion_models**

- [void_pass2.safetensors](https://huggingface.co/Comfy-Org/void-model/resolve/main/diffusion_models/void_pass2.safetensors) (10.38 GB)
- [void_pass1.safetensors](https://huggingface.co/Comfy-Org/void-model/resolve/main/diffusion_models/void_pass1.safetensors) (10.38 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │   └── sam3.1_multiplex_fp16.safetensors
│   ├── 📂 text_encoders/
│   │   └── t5xxl_fp16.safetensors
│   ├── 📂 vae/
│   │   └── cogvideox_vae.safetensors
│   ├── 📂 optical_flow/
│   │   └── raft_large_C_T_SKHT_V2-ff5fadd5.safetensors
│   └── 📂 diffusion_models/
│       ├── void_pass2.safetensors
│       └── void_pass1.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: About VOID Model</summary>

Project: [Netflix/void-model](https://github.com/Netflix/void-model)

## What this stack is good at

Segmentation (**SAM3** from your text cue) defines **what** to erase; the **two-pass** video model **inpaints holes over time**. Strengths:

- **Object removal**, not single-frame patching: coherent motion and lighting across the clip.
- **Interaction-aware seams**: occluded pixels are filled as if the object (and often its immediate influence on nearby stuff) **was never there**, so shadows, overlaps, or simple causal cues can look **more plausible** than a naive erase.
- **Pass 2** refines temporal stability (fewer jitters/flashes) versus **Pass 1** alone — useful on longer cuts or textured backgrounds.

Limits: unclear masks, chaotic motion, or targets that dominate the frame still fail; prompting cannot fix fundamentally wrong segmentation.

## Inputs

- **Source video** — From ComfyUI `input` (`Load Video`).
- **Positive prompt (inpaint fill)** — The **filled** scene after removal (what remains / how it looks and moves).
- **Negative prompt** — Optional anti-artifact list; can be empty.
- **SAM3 object prompt** — Short label for **what** to mask out.

## Prompt writing

**Positive (inpaint)** — Describe the **result**, not “remove X”. Example: `empty kitchen counter, daylight, tiles visible`.

**SAM3 object** — Short referring phrase: `person in blue jacket`, `red cup on table`.

| Field | Role |
|--------|------|
| SAM3 | **What** is removed |
| Positive | **How** the hole is filled in time |

Use **Negative** only when you see repeating defects (watermark, blur, extra limbs, etc.).

</details>
