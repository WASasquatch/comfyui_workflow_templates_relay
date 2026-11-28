# SCAIL-2 Int8: Character Replacement

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_wan21_scail2_character_replacement_int8)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan21_scail2_character_replacement_int8-1.webp" width="360" alt="SCAIL-2 Int8: Character Replacement video_wan21_scail2_character_replacement_int8-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan21_scail2_character_replacement_int8-2.webp" width="360" alt="SCAIL-2 Int8: Character Replacement video_wan21_scail2_character_replacement_int8-2.webp">

> Animate a reference character using a driving video or replace characters entirely with SCAIL-2 Int8, which delivers higher quality than fp8 while running faster. The workflow accepts one reference image and one driving video, outputting an animated character sequence with replaced identity. Ideal for cross-identity character swaps, animal-driven animation, and multi-character scenes without intermediate pose representations.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan21_scail2_character_replacement_int8.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan21_scail2_character_replacement_int8.json)

## Details

| | |
|---|---|
| Name | `video_wan21_scail2_character_replacement_int8` |
| Category | Foundation › Video |
| Output | video |
| Models | SCAIL-2 |
| Tags | Character Replacement, Int8 |
| Type | open source |
| Date | 2026-07-13 |
| Author | ComfyUI |
| Download size | 26.7 GB |
| Min ComfyUI version | 0.25.0 |
| Usage | 436 |
| Nodes | 100 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #30 | image | asian_model_in_white_clothes.png |
| input | `LoadVideo` #155 | video | girl_eats_apple.mp4 |
| output | `SaveVideo` #271 | video | video_wan21_scail2_character_replacement_int8.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sam3.1_multiplex_fp16.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors) |
| `clip_vision_h.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) |
| `wan2.1_14B_SCAIL_2_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/SCAIL-2/resolve/main/diffusion_models/wan2.1_14B_SCAIL_2_int8_convrot.safetensors) |
| `lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) |
| `wan2.1_SCAIL_2_DPO_lora_bf16.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/SCAIL-2/resolve/main/loras/wan2.1_SCAIL_2_DPO_lora_bf16.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `Wan2_1_VAE_bf16.safetensors` | `vae` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2_1_VAE_bf16.safetensors) |

## Subgraphs

- **Character Replacement (SCAIL-2 Int8 Base)** (42 nodes)
- **Character Replacement (SCAIL-2 Int8 Extend)** (45 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveInt` | 10 | comfy-core |
| `CLIPTextEncode` | 8 | comfy-core |
| `ComfyMathExpression` | 7 | comfy-core |
| `ComfySwitchNode` | 6 | comfy-core |
| `ImageFromBatch` | 4 | comfy-core |
| `LoraLoaderModelOnly` | 4 | comfy-core |
| `PreviewImage` | 4 | comfy-core |
| `PrimitiveBoolean` | 4 | comfy-core |
| `PrimitiveFloat` | 4 | comfy-core |
| `SAM3_VideoTrack` | 4 | comfy-core |
| `GetImageSize` | 3 | comfy-core |
| `GetVideoComponents` | 3 | comfy-core |
| `BasicScheduler` | 2 | comfy-core |
| `CheckpointLoaderSimple` | 2 | comfy-core |
| `CLIPLoader` | 2 | comfy-core |
| `CLIPVisionEncode` | 2 | comfy-core |
| `CLIPVisionLoader` | 2 | comfy-core |
| `CreateVideo` | 2 | comfy-core |
| `KSamplerSelect` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `ModelSamplingSD3` | 2 | comfy-core |
| `ResizeImageMaskNode` | 2 | comfy-core |
| `SamplerCustom` | 2 | comfy-core |
| `SaveVideo` | 2 | comfy-core |
| `SCAIL2ColoredMask` | 2 | comfy-core |
| `UNETLoader` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `WanSCAILToVideo` | 2 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `ColorTransfer` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: About SCAIL-2</summary>

# SCAIL-2 Character Replacement

This workflow is using subgraph, please check [here](https://docs.comfy.org/interface/features/subgraph) for more details

## About SCAIL-2

[SCAIL-2](https://huggingface.co/zai-org/SCAIL-2) is an end-to-end character animation model that drives a reference character image with a driving video for character animation or in-video character replacement.


---

## Parameters

### Shared (Base & Extend)

| Input | Notes |
|---|---|
| `pose_video` | Driving video |
| `reference_image` | Character to use |
| `prompt` | Output video description — see **Prompt Writing** below |
| `replace_mode` | `true` = Replacement (default), `false` = Animation |
| `segment_index` | `1` first chunk; `2+` continue. Pose offset = `76 × (index − 1)` |
| `width` / `height` | e.g. 896×512 |
| `frame_count` | Default **81** (4n+1) |
| `previous_frame_count` | Overlap **5** |
| `pose_strength` / `pose_start` / `pose_end` | Pose conditioning |
| `turbo_mode` | Lightx2v fast preset |
| `distill_lora` / `dpo_lora` | Speed / quality LoRA strength |
| `sam3_video_object` | SAM3 text for driving video — see **SAM3** below |
| `sam3_image_object` | SAM3 text for reference image |

### Extend only

| Input | Notes |
|---|---|
| `previous_frames` | IMAGE from previous segment; only last `previous_frame_count` frames used |

---

## Two Modes (`replace_mode`)

| Value | Mode | Summary |
|---|---|---|
| `true` | **Replacement** | Swap tracked person in driving video with reference character. Driving mask bg: **white**. **This workflow default.** |
| `false` | **Animation** | Reference character performs driving motion. Driving mask bg: **black**. |

Set on **both** subgraphs. Animation still needs masks; rewrite `prompt` accordingly.

---

## SAM3 (two inputs)

Not the SCAIL-2 `prompt` — only for mask track/segment:

| Pin | Target | Output mask |
|---|---|---|
| `sam3_video_object` | Driving video | `pose_video_mask` |
| `sam3_image_object` | Reference image | `reference_image_mask` |

Open-vocabulary text (default `human`). Use the same word when subject matches; use different words if video/ref need different focus (e.g. crowded scene → be more specific).

Colored masks bind body regions between ref and driving. Main `prompt` controls final appearance.

---


## How This Workflow Works

1. Load `pose_video` + `reference_image`.
2. **Base** subgraph — segment 1 (`segment_index = 1`, no `previous_frames`).
3. **Extend** subgraph — segment 2+ (`previous_frames` from prior output, increment `segment_index`).
4. Preview / save; stitch segments if needed.


---

## Long Videos

`ceil(total_frames / 76)` segments — see **Estimate Segment Count** group.

| Segments | Action |
|---|---|
| 1 | Base only |
| 2+ | Base + Extend(s); duplicate Extend, chain `previous_frames`, increase `segment_index` |

**No auto loop:** `WanSCAILToVideo` cannot queue all segments automatically — run each segment manually.

---

Requires ComfyUI [PR#14373](https://github.com/Comfy-Org/ComfyUI/pull/14373)

</details>

<details><summary>Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/SCAIL-2](https://huggingface.co/Comfy-Org/SCAIL-2)
- [ModelScope:Comfy-Org/SCAIL-2](https://modelscope.cn/models/Comfy-Org/SCAIL-2)
- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [Hugging Face:Comfy-Org/sam3.1](https://huggingface.co/Comfy-Org/sam3.1)
- [ModelScope:Comfy-Org/sam3.1](https://modelscope.cn/models/Comfy-Org/sam3.1)

**loras**

- [lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) (703.8 MB)
- [wan2.1_SCAIL_2_DPO_lora_bf16.safetensors](https://huggingface.co/Comfy-Org/SCAIL-2/resolve/main/loras/wan2.1_SCAIL_2_DPO_lora_bf16.safetensors) (1.14 GB)

**vae**

- [Wan2_1_VAE_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2_1_VAE_bf16.safetensors) (242 MB)

**text_encoders**

- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) (6.27 GB)

**clip_vision**

- [clip_vision_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) (1.18 GB)

**diffusion_models**

- [wan2.1_14B_SCAIL_2_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/SCAIL-2/resolve/main/diffusion_models/wan2.1_14B_SCAIL_2_int8_convrot.safetensors) (15.51 GB)

**checkpoints**

- [sam3.1_multiplex_fp16.safetensors](https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors) (1.63 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 loras/
│   │   ├── lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
│   │   └── wan2.1_SCAIL_2_DPO_lora_bf16.safetensors
│   ├── 📂 vae/
│   │   └── Wan2_1_VAE_bf16.safetensors
│   ├── 📂 text_encoders/
│   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
│   ├── 📂 clip_vision/
│   │   └── clip_vision_h.safetensors
│   ├── 📂 diffusion_models/
│   │   └── wan2.1_14B_SCAIL_2_int8_convrot.safetensors
│   └── 📂 checkpoints/
│       └── sam3.1_multiplex_fp16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
