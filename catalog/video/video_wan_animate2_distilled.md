# Wan Animate 2 Distilled: Motion Transfer

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_wan_animate2_distilled)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_animate2_distilled-1.webp" width="360" alt="Wan Animate 2 Distilled: Motion Transfer video_wan_animate2_distilled-1.webp">

> Animate a still character using a driving video with Wan Animate 2, transferring motion directly from video frames without any pose extraction or skeleton preprocessing. The output preserves the reference character's identity while generating a fresh background and camera movement from your text prompt. This distilled version delivers efficient, high-fidelity motion generation with strong identity preservation, ideal for motion transfer, action mimicry, and character animation replacement projects.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_animate2_distilled.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan_animate2_distilled.json)

## Details

| | |
|---|---|
| Name | `video_wan_animate2_distilled` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan Animate |
| Tags | Motion Control, Int8 |
| Type | open source |
| Date | 2026-08-07 |
| Author | ComfyUI |
| Download size | 23.2 GB |
| Min ComfyUI version | 0.31.0 |
| Usage | 113 |
| Nodes | 83 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #189 | image | ref_doll_realistic.png |
| input | `LoadVideo` #240 | video | drive_doll_street_dance.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `clip_vision_h.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/clip_vision/clip_vision_h.safetensors) |
| `wan_animate_2_distill_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/diffusion_models/wan_animate_2_distill_int8_convrot.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `Wan2_1_VAE_bf16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan-Animate-2/resolve/main/vae/Wan2_1_VAE_bf16.safetensors) |

## Subgraphs

- **Motion Transfer (Wan Animate 2 Distilled)** (27 nodes)
- **Video Stitch** (13 nodes)
- **Motion Transfer (Wan Animate 2 Distilled)** (27 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 6 | comfy-core |
| `GetImageSize` | 6 | comfy-core |
| `ImageFromBatch` | 6 | comfy-core |
| `GetVideoComponents` | 5 | comfy-core |
| `ResizeImageMaskNode` | 5 | comfy-core |
| `CLIPVisionEncode` | 4 | comfy-core |
| `ComfyMathExpression` | 4 | comfy-core |
| `ComfySwitchNode` | 4 | comfy-core |
| `MarkdownNote` | 4 |  |
| `BasicScheduler` | 2 | comfy-core |
| `CLIPLoader` | 2 | comfy-core |
| `CLIPVisionLoader` | 2 | comfy-core |
| `ContextWindowsManual` | 2 | comfy-core |
| `CreateVideo` | 2 | comfy-core |
| `KSamplerSelect` | 2 | comfy-core |
| `ModelSamplingSD3` | 2 | comfy-core |
| `PrimitiveBoolean` | 2 | comfy-core |
| `PrimitiveStringMultiline` | 2 | comfy-core |
| `SamplerCustom` | 2 | comfy-core |
| `SaveVideo` | 2 | comfy-core |
| `TrimVideoLatent` | 2 | comfy-core |
| `UNETLoader` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `WanAnimate2Cache` | 2 | comfy-core |
| `WanAnimate2ToVideo` | 2 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `ImageStitch` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

[Native loop support PR](https://github.com/Comfy-Org/ComfyUI/pull/13180) is still under review, so you have to manually copy and paste the `Motion Transfer (Wan Animate 2)` subgraph in order to make a longer video, the number here indicates how many subgraphs you need to match the pose reference video length.

</details>

<details><summary>Note: How to duplicate the subgraph (manually)</summary>

1. Select and press `Ctrl+B` to enable the bypassed subgraph above.
2. Update it first, and make sure the prompt and size match the first one, linking the `image` output to the `Batch Images` node
3. Select the `Motion Transfer (Wan Animate 2)` subgraph
4. Use `Ctrl+C` and `Ctrl+Shift+V` to duplicate the subgraph
5. Link `continue_motion` and `video_frame_offset` from the previous subgraph to the new subgraph.
6. Link the `image` output to the `Batch Images` node to extend the total output images

</details>

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
