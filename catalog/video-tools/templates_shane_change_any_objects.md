# Change Any Objects

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_shane_change_any_objects)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_shane_change_any_objects-1.webp" width="360" alt="Change Any Objects templates_shane_change_any_objects-1.webp">

> Use simple prompt to mask out certain objects within a video, and replace the object using prompt, or optional reference image. Model used: SAM3 + WAN 2.1 VACE inpainting

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_shane_change_any_objects.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_shane_change_any_objects.json)

## Details

| | |
|---|---|
| Name | `templates_shane_change_any_objects` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | SAM3, Wan2.1 VACE |
| Tags | Inpainting, Video |
| Type | open source |
| Date | 2026-03-04 |
| Author | shane |
| Download size | 10.0 GB |
| Min ComfyUI version | 0.20.0 |
| Distributions | cloud |
| Usage | 42 |
| Nodes | 30 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `VHS_LoadVideo` #187 | video | woman_holding_the_pineapple.mp4 |
| input | `LoadImage` #204 | image | dragon_fruit.png |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui-sam3](https://registry.comfy.org/nodes/comfyui-sam3)
- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [ComfyUI-WanVideoWrapper](https://registry.comfy.org/nodes/ComfyUI-WanVideoWrapper)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)
- [RES4LYF](https://registry.comfy.org/nodes/RES4LYF)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `wan2.1_vace_14B_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/diffusion_models/wan2.1_vace_14B_fp16.safetensors) |
| `Wan21_CausVid_14B_T2V_lora_rank32_v2.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan21_CausVid_14B_T2V_lora_rank32_v2.safetensors?download=true) |
| `umt5-xxl-enc-bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/umt5-xxl-enc-bf16.safetensors?download=true) |
| `Wan2_1_VAE_bf16.safetensors` | `vae` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2_1_VAE_bf16.safetensors?download=true) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `INTConstant` | 3 | comfyui-kjnodes |
| `ImageCompositeMasked` | 2 |  |
| `MaskBlur+` | 2 |  |
| `VHS_VideoCombine` | 2 | comfyui-videohelpersuite |
| `GrowMaskWithBlur` | 1 |  |
| `ImageConstant` | 1 |  |
| `ImageResize+` | 1 | comfyui_essentials |
| `LoadImage` | 1 | comfy-core |
| `LoadSAM3Model` | 1 | comfyui-sam3 |
| `LoadWanVideoT5TextEncoder` | 1 | ComfyUI-WanVideoWrapper |
| `SAM3Propagate` | 1 | comfyui-sam3 |
| `SAM3VideoOutput` | 1 | comfyui-sam3 |
| `SAM3VideoSegmentation` | 1 | comfyui-sam3 |
| `TextBox1` | 1 | RES4LYF |
| `VHS_LoadVideo` | 1 | comfyui-videohelpersuite |
| `WanVideoDecode` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoExperimentalArgs` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoLoraSelect` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoModelLoader` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoSampler` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoSLG` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoTextEncode` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoTorchCompileSettings` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoVACEEncode` | 1 | ComfyUI-WanVideoWrapper |
| `WanVideoVAELoader` | 1 | ComfyUI-WanVideoWrapper |
