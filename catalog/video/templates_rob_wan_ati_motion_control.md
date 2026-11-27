# Wan ATI Motion Control

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_rob_wan_ati_motion_control)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_rob_wan_ati_motion_control-1.webp" width="360" alt="Wan ATI Motion Control templates_rob_wan_ati_motion_control-1.webp">

> Upload an input image and use the Animate Path node to draw paths for a viral video effect.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_rob_wan_ati_motion_control.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_rob_wan_ati_motion_control.json)

## Details

| | |
|---|---|
| Name | `templates_rob_wan_ati_motion_control` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan ATI |
| Tags | Motion Control, Image to Video |
| Type | open source |
| Date | 2026-03-18 |
| Author | hellorob |
| Download size | 71.9 GB |
| Min ComfyUI version | 0.5.0 |
| Usage | 51 |
| Nodes | 33 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #460 | image | white_tiger.png |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [comfyui_fill-nodes](https://registry.comfy.org/nodes/comfyui_fill-nodes)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `clip_vision_h.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) |
| `Wan21-WanMove_fp8_scaled_e4m3fn_KJ.safetensors` | `diffusion_models` | [link](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/resolve/main/WanMove/Wan21-WanMove_fp8_scaled_e4m3fn_KJ.safetensors) |
| `lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Subgraphs

- **Image Resize and Prep** (4 nodes)
- **WanMoveTrackToVideo** (23 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 | comfy-core |
| `PrimitiveInt` | 3 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `PrimitiveFloat` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPVisionEncode` | 1 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `CreateVideo` | 1 | comfy-core |
| `FL_PathAnimator` | 1 | comfyui_fill-nodes |
| `GetImageSize` | 1 | comfy-core |
| `GetImageSizeAndCount` | 1 | comfyui-kjnodes |
| `ImageResizeKJv2` | 1 |  |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingSD3` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `PrimitiveNode` | 1 |  |
| `RepeatImageBatch` | 1 |  |
| `Reroute` | 1 |  |
| `SaveVideo` | 1 |  |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `WanMoveTracksFromCoords` | 1 | comfy-core |
| `WanMoveTrackToVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

[Watch this Tutorial](https://www.youtube.com/watch?v=AI9-1G7niXY&t=498s) for information on how to use the Animate Path node.

> **Note:** Video length value needs to be `16 × number of seconds + 1`

</details>
