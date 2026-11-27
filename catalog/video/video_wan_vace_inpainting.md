# Wan2.1 VACE Inpainting

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_wan_vace_inpainting)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_vace_inpainting-1.webp" width="360" alt="Wan2.1 VACE Inpainting video_wan_vace_inpainting-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_vace_inpainting-2.webp" width="360" alt="Wan2.1 VACE Inpainting video_wan_vace_inpainting-2.webp">

> Edit specific regions in videos while preserving surrounding content. Great for object removal or replacement.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_vace_inpainting.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan_vace_inpainting.json)
- [Tutorial](https://docs.comfy.org/tutorials/video/wan/vace)

## Details

| | |
|---|---|
| Name | `video_wan_vace_inpainting` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.1, Wan |
| Tags | Inpainting, Video |
| Type | open source |
| Date | 2025-05-21 |
| Author | ComfyUI |
| Download size | 53.8 GB |
| Min ComfyUI version | 0.20.0 |
| Usage | 131 |
| Nodes | 43 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #162 | image | api_bfl_flux_1_kontext_multiple_images_input_dog.jpg |
| input | `LoadVideo` #209 | video | video_wan_vace_inpainting_input_video.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sam3.1_multiplex_fp16.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors) |
| `wan2.1_vace_14B_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_vace_14B_fp16.safetensors) |
| `Wan21_CausVid_14B_T2V_lora_rank32.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan21_CausVid_14B_T2V_lora_rank32.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Subgraphs

- **Image Segmentation (SAM3)** (3 nodes)
- **Video Inpainting (Wan2.1 VACE)** (36 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveInt` | 4 | comfy-core |
| `CLIPTextEncode` | 3 | comfy-core |
| `ComfySwitchNode` | 3 | comfy-core |
| `ComfyMathExpression` | 2 | comfy-core |
| `ImageFromBatch` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `PrimitiveFloat` | 2 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `GrowMask` | 1 | comfy-core |
| `ImageCompositeMasked` | 1 | comfy-core |
| `InvertMask` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `MaskPreview` | 1 | comfy-core |
| `MaskToImage` | 1 | comfy-core |
| `ModelSamplingSD3` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `ResizeImageMaskNode` | 1 | comfy-core |
| `SAM3_Detect` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `TrimVideoLatent` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `WanVaceToVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Workflow Usage</summary>

## Wan2.1 VACE — Video Inpainting Workflow

### What this model can do

**[Wan2.1-VACE-14B](https://huggingface.co/Wan-AI/Wan2.1-VACE-14B)** is an all-in-one video creation and editing model ([VACE project page](https://ali-vilab.github.io/VACE-Page/)). This workflow uses its **masked video-to-video (MV2V) / inpainting** capability:

- Edit regions inside a video defined by a **mask** (replace or regenerate masked areas)
- Optionally use a **reference image** for appearance or subject consistency
- Control output with a **text prompt** (what should appear in the edited region)

Related VACE modes (not all wired in this template): reference-to-video, swap/move/expand objects, video rerender, and more.

---

### Main graph

1. **Load Video** — input clip to edit  
2. **Load Image** *(optional)* — reference image  
3. **Video Inpainting (Wan2.1 VACE)** — open the subgraph for all controls  
4. **Save Video** — output

---

### Subgraph inputs (display order)

| Input | Purpose |
|-------|--------|
| **prompt** | VACE generation prompt — describes the desired result in the masked area |
| **width** / **height** | Output resolution (area). VACE-14B supports **480P** and **720P**; match your GPU and quality needs |
| **frame_counts** | **Total frames to generate** (latent length). See below |
| **seed** | Random seed for reproducibility |
| **wan_vace_model** | VACE diffusion checkpoint (e.g. `wan2.1_vace_14B_fp16`) |
| **clip_model** | Text encoder for VACE (e.g. `umt5_xxl_*`) |
| **vae_model** | Wan VAE (`wan_2.1_vae.safetensors`) |
| **enable_turbo_mode** | Faster sampling preset (Lightning LoRA path) |
| **lightning_lora** | LoRA used when turbo mode is on |
| **sam3_mask_object** | SAM3 text prompt — what to segment (e.g. `person`, `dog`). **Not** the VACE negative prompt |
| **mask_expand** | Pixels to grow the SAM3 mask (softer edges, fewer seams) |
| **sam3_model** | SAM3 checkpoint for mask creation |

Draw or refine masks inside the subgraph (*Create Video Mask* group). VACE negative prompt is fixed inside the subgraph.

---

### frame_counts (important)

VACE is trained and evaluated on **short clips** (~**81 frames** at 16 fps ≈ 5 s). It **does not** reliably handle very long videos in one pass.

- This workflow defaults **frame_counts = 81** as a safe total frame count.
- If your source video is longer, **do not** only raise `frame_counts` very high — quality, memory, and stability usually suffer.

**Recommended for long videos:** duplicate the **same subgraph** (or run the workflow in chunks), process **~81 frames per segment**, then concatenate segments in your editor or with a separate merge step. Keep prompts and seeds consistent across chunks if you need continuity.

</details>

<details><summary>Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/sam3.1](https://huggingface.co/Comfy-Org/sam3.1)
- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/sam3.1](https://modelscope.cn/models/Comfy-Org/sam3.1)
- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

**checkpoints**

- [sam3.1_multiplex_fp16.safetensors](https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors) (1.63 GB)

**loras**

- [Wan21_CausVid_14B_T2V_lora_rank32.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan21_CausVid_14B_T2V_lora_rank32.safetensors) (304.3 MB)

**text_encoders**

- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true) (6.27 GB)

**vae**

- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) (242.1 MB)

**diffusion_models**

- [wan2.1_vace_14B_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_vace_14B_fp16.safetensors) (32.29 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │   └── sam3.1_multiplex_fp16.safetensors
│   ├── 📂 loras/
│   │   └── Wan21_CausVid_14B_T2V_lora_rank32.safetensors
│   ├── 📂 text_encoders/
│   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
│   ├── 📂 vae/
│   │   └── wan_2.1_vae.safetensors
│   └── 📂 diffusion_models/
│       └── wan2.1_vace_14B_fp16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
