# Video to Seamless Loop Converter

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_sirolim_seamless_loop)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_sirolim_seamless_loop-1.webp" width="360" alt="Video to Seamless Loop Converter template_sirolim_seamless_loop-1.webp">

> Upload a video clip to generate a seamless, looping video output.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_sirolim_seamless_loop.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_sirolim_seamless_loop.json)

## Details

| | |
|---|---|
| Name | `template_sirolim_seamless_loop` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | Wan2.1 VACE |
| Tags | API, Video Edit |
| Type | API |
| Date | 2026-03-08 |
| Author | sirolim |
| Download size | 39.1 GB |
| Min ComfyUI version | 0.8.0 |
| Usage | 14 |
| Nodes | 39 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `VHS_LoadVideo` #158 | video | seamless_loop_input.mp4 |
| output | `SaveVideo` #251 | video | template_sirolim_seamless_loop.mp4 |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `wan2.1_vace_14B_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_vace_14B_fp16.safetensors) |
| `Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors?download=true) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Subgraphs

- **Wan Vace 2.1** (14 nodes)
- **Seanless Loop** (19 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ImageFromBatch` | 4 | comfy-core |
| `LayerUtility: ColorImage V2` | 3 |  |
| `ReverseImageBatch` | 3 | comfyui-kjnodes |
| `VHS_DuplicateImages` | 3 | comfyui-videohelpersuite |
| `BatchImagesNode` | 2 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `PrimitiveInt` | 2 |  |
| `VHS_VideoCombine` | 2 |  |
| `CLIPLoader` | 1 | comfy-core |
| `CreateVideo` | 1 |  |
| `ImageBatch` | 1 | comfy-core |
| `ImageResize+` | 1 | comfyui_essentials |
| `ImageToMask` | 1 |  |
| `KSampler` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 |  |
| `MarkdownNote` | 1 |  |
| `OpenAIChatNode` | 1 |  |
| `PreviewAny` | 1 |  |
| `SaveVideo` | 1 |  |
| `SimpleMath+` | 1 |  |
| `UNETLoader` | 1 |  |
| `UNetTemporalAttentionMultiply` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `VHS_LoadVideo` | 1 | comfyui-videohelpersuite |
| `WanVaceToVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Seamless Loop ♾️</summary>

Upload a **video** and turn it into a seamless loop.

## How It Works

1. **Upload a video**
2. Set your video length

3. The system:
   - Creates empty frames
   - Uses Wan 2.1 VACE to fill these empty Frames and generate a seamless loop

## Tips

- This technique works better when first and last frame have similar angles towards your subject.

That’s it.  
Video → Seamless Loop.

</details>
