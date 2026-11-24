# Wan-Move Motion-Control Image to Video

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wanmove_480p-1.webp" width="360" alt="Wan-Move Motion-Control Image to Video video_wanmove_480p-1.webp">

> Generate videos from a single image using Wan-Move, with fine-grained point-level motion control via trajectory guidance.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wanmove_480p.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wanmove_480p.json)

## Details

| | |
|---|---|
| Name | `video_wanmove_480p` |
| Category | Foundation › Video |
| Media type | image |
| Models | Wan, Wan2.1 |
| Tags | Image to Video, Motion Control, Video |
| Type | open source |
| Date | 2025-12-15 |
| Author | ComfyUI |
| Download size | 23.7 GB |
| Min ComfyUI version | 0.5.0 |
| Usage | 8 |
| Nodes | 38 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #238 | image | snowboard_rush.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `clip_vision_h.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) |
| `Wan21-WanMove_fp8_scaled_e4m3fn_KJ.safetensors` | `diffusion_models` | [link](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/resolve/main/WanMove/Wan21-WanMove_fp8_scaled_e4m3fn_KJ.safetensors) |
| `lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Subgraphs

- **WanMoveTrackToVideo** (23 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 | comfy-core |
| `GenerateTracks` | 3 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `CreateVideo` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `PrimitiveFloat` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `SaveVideo` | 2 | comfy-core |
| `WanMoveConcatTrack` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPVisionEncode` | 1 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageScale` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `ModelSamplingSD3` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `Reroute` | 1 |  |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `WanMoveTracksFromCoords` | 1 | comfy-core |
| `WanMoveTrackToVideo` | 1 | comfy-core |
| `WanMoveVisualizeTracks` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

You can use [this editor](https://comfyui-wiki.github.io/wan_move_track_visualizer/) to generate tracks visually.

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

**text_encoders**

- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) (6.27 GB)

**clip_vision**

- [clip_vision_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) (1.18 GB)

**loras**

- [lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) (703.8 MB)

**diffusion_models**

- [Wan21-WanMove_fp8_scaled_e4m3fn_KJ.safetensors](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/resolve/main/WanMove/Wan21-WanMove_fp8_scaled_e4m3fn_KJ.safetensors) (15.28 GB)

**vae**

- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) (242.1 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
│   ├── 📂 clip_vision/
│   │      └── clip_vision_h.safetensors
│   ├── 📂 loras/
│   │      └── lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
│   ├── 📂 diffusion_models/
│   │      └── Wan21-WanMove_fp8_scaled_e4m3fn_KJ.safetensors
│   └── 📂 vae/
│          └── wan_2.1_vae.safetensors
```

## Report issue

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Online WanMOve Visual Track Editor</summary>

You can use [this editor](https://comfyui-wiki.github.io/wan_move_track_visualizer/) to generate tracks visually. Or, you can also install [/ComfyUI_Fill-Nodes](https://github.com/filliptm/ComfyUI_Fill-Nodes) and then use the *FL Path Animator* to create the track coordinates.

The WanMoveTracksFromCoords supports converting tracks from coords

</details>
