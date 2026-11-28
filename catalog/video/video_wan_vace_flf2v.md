# Wan2.1 VACE First-Last Frame

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_wan_vace_flf2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_vace_flf2v-1.webp" width="360" alt="Wan2.1 VACE First-Last Frame video_wan_vace_flf2v-1.webp">

> Generate smooth video transitions by defining start and end frames. Supports custom keyframe sequences.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_vace_flf2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan_vace_flf2v.json)
- [Tutorial](https://docs.comfy.org/tutorials/video/wan/vace)

## Details

| | |
|---|---|
| Name | `video_wan_vace_flf2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.1, Wan |
| Tags | FLF2V, Video |
| Type | open source |
| Date | 2025-05-21 |
| Author | ComfyUI |
| Download size | 53.8 GB |
| Min ComfyUI version | 0.16.4 |
| Usage | 14 |
| Nodes | 41 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #144 | image | video_wan_vace_flf2v_start_image.png |
| input | `LoadImage` #147 | image | video_wan_vace_flf2v_end_image.png |
| output | `SaveVideo` #69 | video | video_wan_vace_flf2v.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `wan2.1_vace_14B_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_vace_14B_fp16.safetensors) |
| `lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Subgraphs

- **Wan VACE FLF2V Image Batch** (10 nodes)
- **FLF2V (Wan2.1 VACE)** (27 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveInt` | 6 | comfy-core |
| `ComfyMathExpression` | 4 | comfy-core |
| `ComfySwitchNode` | 3 | comfy-core |
| `BatchImagesNode` | 2 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `MaskToImage` | 2 | comfy-core |
| `PrimitiveFloat` | 2 | comfy-core |
| `SolidMask` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `ImageToMask` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `ModelSamplingSD3` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `RepeatImageBatch` | 1 | comfy-core |
| `SaveVideo` | 1 | comfy-core |
| `TrimVideoLatent` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `WanVaceToVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

**vae**

- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) (242.1 MB)

**text_encoders**

- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors?download=true) (6.27 GB)

**loras**

- [lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) (703.8 MB)

**diffusion_models**

- [wan2.1_vace_14B_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_vace_14B_fp16.safetensors) (32.29 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 vae/
│   │   └── wan_2.1_vae.safetensors
│   ├── 📂 text_encoders/
│   │   └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
│   ├── 📂 loras/
│   │   └── lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
│   └── 📂 diffusion_models/
│       └── wan2.1_vace_14B_fp16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: Limited</summary>

This model support up to 720P, less than 5s

</details>
