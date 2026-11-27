# Wan Animate 2: Motion Transfer

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_wan_animate2)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_animate2-1.webp" width="360" alt="Wan Animate 2: Motion Transfer video_wan_animate2-1.webp">

> Animate a still character using a driving video with Wan Animate 2, transferring motion directly from video frames without any pose extraction or skeleton preprocessing. The output preserves the reference character's identity while generating a fresh background and camera movement from your text prompt. Ideal for motion transfer, action mimicry, and character animation replacement projects.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_animate2.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan_animate2.json)

## Details

| | |
|---|---|
| Name | `video_wan_animate2` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan Animate |
| Tags | Motion Control, Int8 |
| Type | open source |
| Date | 2026-08-07 |
| Author | ComfyUI |
| Download size | 23.9 GB |
| Min ComfyUI version | 0.36.0 |
| Usage | 1682 |
| Nodes | 67 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #189 | image | pink_hair_mech_arms_ref.png |
| input | `LoadVideo` #240 | video | street_dance_drive.mp4 |
| output | `SaveVideo` #292 | video | video_wan_animate2.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `clip_vision_h.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/clip_vision/clip_vision_h.safetensors) |
| `wan_animate_2_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/diffusion_models/wan_animate_2_int8_convrot.safetensors) |
| `lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/loras/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `Wan2_1_VAE_bf16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/vae/Wan2_1_VAE_bf16.safetensors) |

## Subgraphs

- **Video Stitch** (13 nodes)
- **Motion Transfer (Wan Animate 2)** (48 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfyMathExpression` | 7 |  |
| `ComfySwitchNode` | 6 |  |
| `GetImageSize` | 5 |  |
| `ImageFromBatch` | 5 |  |
| `GetVideoComponents` | 4 | comfy-core |
| `CLIPTextEncode` | 3 |  |
| `MarkdownNote` | 3 |  |
| `ResizeImageMaskNode` | 3 |  |
| `CLIPVisionEncode` | 2 |  |
| `CreateVideo` | 2 | comfy-core |
| `GetItemFromList` | 2 |  |
| `PrimitiveInt` | 2 |  |
| `SaveVideo` | 2 |  |
| `BasicScheduler` | 1 |  |
| `CLIPLoader` | 1 |  |
| `CLIPVisionLoader` | 1 |  |
| `ContextWindowsManual` | 1 |  |
| `CreateList` | 1 |  |
| `EndLoop` | 1 |  |
| `ImageStitch` | 1 | comfy-core |
| `KSamplerSelect` | 1 |  |
| `LoadImage` | 1 |  |
| `LoadVideo` | 1 |  |
| `LoraLoaderModelOnly` | 1 |  |
| `ModelSamplingSD3` | 1 |  |
| `RebatchImages` | 1 |  |
| `SamplerCustom` | 1 |  |
| `StartLoop` | 1 |  |
| `TrimVideoLatent` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |
| `WanAnimate2Cache` | 1 |  |
| `WanAnimate2ToVideo` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Wan Animate2</summary>

# Wan Animate 2 — Character Animation

## What is this model?
**Wan-Animate-2** (by Wan-Video / Alibaba) is an **end-to-end character animation model**:

> Reference image (who) + Driving video (what motion) → your character performing that motion

Key properties:
- **No pose/keypoint extraction** — unlike v1 (Wan 2.2 Animate), the raw driving video frames are used directly. No skeleton/pose preprocessing needed.
- **Identity preservation** — the output character matches the reference image.
- **Text-controlled background and camera** — the output background is generated from the prompt, fully decoupled from both the reference image and the driving video.

## How it works (brief)

    Reference image ──VAE──▶ ref latent ──┐
                                          ├──▶ DiT (14B) ──▶ frames ──▶ video
    Driving video  ──VAE──▶ pose latent ──┘   pose branch feeds K/V per frame
           ▲
    Text prompt ──▶ text conditioning (character + background)

Each generated frame attends to the reference frame (identity) plus the pose video frame (motion).

## How to use this workflow

1. **LoadImage** — your character image (background doesn't matter; the output background follows the prompt).
2. **LoadVideo** — the driving video (any resolution; keep the character framing similar to the reference image, e.g. full-body to full-body).
3. **Set the prompts** on the `Motion Transfer` subgraph:
   - `text_1` (main): `Character appearance description: ...` + `Background description: ...` — describe the LOOKS only, no motion words.
   - `text_2` (pose): describe the motion in the video, e.g. `a person dancing`.
4. **Queue it** — `SaveVideo` writes the result; the node on the right shows a side-by-side comparison with the driving video.

## Making longer videos (extending)

Each `Motion Transfer` subgraph generates **81 frames** (~3.4 s @ 24 fps). To extend beyond that, chain multiple subgraphs manually:

1. **Duplicate** the `Motion Transfer (Wan Animate 2)` subgraph — select it, press `Ctrl-C` then `Ctrl-Shift-V`.
2. **Wire the previous subgraph to the new one**:
   - previous `IMAGE` → new `continue_motion` (uses the last frame as a temporal anchor)
   - previous `video_frame_offset` → new `video_frame_offset` (continues reading the driving video where it left off)
3. **Concatenate the outputs** — connect the new subgraph's `IMAGE` to the `Batch Images` node (its inputs auto-grow with the `+` button).
4. Consecutive segments overlap by 1 frame by design (that frame keeps the motion continuous). If you see a 1-frame "hiccup" at the seam, drop the new segment's first frame (the `trim_image` output = how many frames to remove).

> How many subgraphs do you need? Roughly `driving video frames / 81` — the math node in the bottom-left computes this for you.

**Alternative (future):** the [Native loop support PR](https://github.com/Comfy-Org/ComfyUI/pull/13180) will allow looping/extension without manual duplication. It's still under review — until it lands, manual chaining above is the way. You can also try the community `ComfyUI-NativeLooping_testing` nodes for window-to-window seamless loops.

## Tips
- Framing mismatch (close-up vs full-body) is the #1 cause of bad results.
- Frames are taken 1:1 from the video (no fps resampling) — resample to ~16-24 fps if the motion looks too slow.
- Set `WanAnimate2Cache` device to **cpu** to avoid VRAM spikes.

</details>

<details><summary>Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Wan-Animate-2](https://huggingface.co/Comfy-Org/Wan-Animate-2)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan-Animate-2](https://modelscope.cn/models/Comfy-Org/Wan-Animate-2)

**Input Assets** (download these files and load them to the `load image` and `load video` nodes

- [pink_hair_mech_arms_ref.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/pink_hair_mech_arms_ref.png) — required workflow input (`input/pink_hair_mech_arms_ref.png`)
- [street_dance_drive.mp4](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/street_dance_drive.mp4) — required workflow input (`input/street_dance_drive.mp4`)

**diffusion_models**

- [wan_animate_2_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/diffusion_models/wan_animate_2_int8_convrot.safetensors) (15.51 GB)

**loras**

- [lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/loras/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) (703.8 MB)

**text_encoders**

- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) (6.27 GB)

**clip_vision**

- [clip_vision_h.safetensors](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/clip_vision/clip_vision_h.safetensors) (1.18 GB)

**vae**

- [Wan2_1_VAE_bf16.safetensors](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/vae/Wan2_1_VAE_bf16.safetensors) (242 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── wan_animate_2_int8_convrot.safetensors
│   ├── 📂 loras/
│   │   └── lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
│   ├── 📂 text_encoders/
│   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
│   ├── 📂 clip_vision/
│   │   └── clip_vision_h.safetensors
│   └── 📂 vae/
│       └── Wan2_1_VAE_bf16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Loop math (exact frame count)</summary>

# Start Loop math - why these numbers line up

`b` = `#635` (fragment_length)   |   `F` = `#537` (driving-video frame count)

Each continuation repeats the previous segment's **last** frame as its own first frame
(`CONTINUE_MOTION_FRAMES = 1` in `WanAnimate2ToVideo`), and `#604 ImageFromBatch`
trims that duplicate - so a segment of length `b` only adds `b - 1` frames.

    k continuations   =>   sum(lengths) = F + k      (k extra frames feed the k repeats)

Keeping segment 0 inside one context window (1 <= len0 <= b):

    #636    k    = floor((F - 2) / (b - 1))
    #639    len0 = 4 * ceil((F - (b-1)*k - 1) / 4) + 1      <- rounded up to a legal 4n+1
    #645    n    = k + 1                  (num_iterations)

`#639` rounds **up**, so the loop always generates at least F frames, and `#667`
(`ImageFromBatch`, length = F) trims the tail back to exactly F.

    Exact w/o trim?  =  (F % 4 == 1) and (b % 4 == 1)
      True  -> generated == F, `#668` bypasses the trim
      False -> generated  > F, `#668` applies the trim        (any F still works)

`b` should be a legal Wan length (81, 85, 89 ...) : `latent_T = ((len-1)//4)+1`.

Formula and requirements verified against ComfyUI `nodes_wan.py` + the Wan VAE kernel.

</details>
