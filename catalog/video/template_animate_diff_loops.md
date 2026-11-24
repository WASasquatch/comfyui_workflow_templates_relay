# Animate Diff High Res Loops

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_animate_diff_loops-1.webp" width="360" alt="Animate Diff High Res Loops template_animate_diff_loops-1.webp">

> upload one image to get a seamless loop animation

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_animate_diff_loops.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_animate_diff_loops.json)

## Details

| | |
|---|---|
| Name | `template_animate_diff_loops` |
| Category | Foundation › Video |
| Media type | image |
| Models | IP Adapter |
| Tags | Image to Video |
| Type | open source |
| Date | 2026-03-30 |
| Author | ComfyUI |
| Download size | 4.0 GB |
| Min ComfyUI version | 0.3.42 |
| Distributions | local |
| Usage | 7 |
| Nodes | 36 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #145 | image | path_of_the_cube.png |

## Custom nodes required

- [comfyui-animatediff-evolved](https://registry.comfy.org/nodes/comfyui-animatediff-evolved)
- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [comfyui_fill-nodes](https://registry.comfy.org/nodes/comfyui_fill-nodes)
- [comfyui_ipadapter_plus](https://registry.comfy.org/nodes/comfyui_ipadapter_plus)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `realismByStableYogi_v4LCM.safetensors` | `checkpoints` | [link](https://civitai.com/api/download/models/353362?type=Model&format=SafeTensor&size=full&fp=fp16) |
| `CLIP-ViT-H-14-laion2B-s32B-b79K.safetensors` | `clip_vision` | [link](https://huggingface.co/h94/IP-Adapter/resolve/main/models/image_encoder/model.safetensors) |

## Subgraphs

- **New Subgraph** (10 nodes)
- **New Subgraph** (8 nodes)
- **New Subgraph** (8 nodes)
- **New Subgraph** (6 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 3 |  |
| `VAEDecode` | 3 |  |
| `VHS_VideoCombine` | 3 |  |
| `ADE_AnimateDiffSamplingSettings` | 2 |  |
| `ADE_AnimateDiffUniformContextOptions` | 2 |  |
| `ADE_ApplyAnimateDiffModel` | 2 |  |
| `ADE_UseEvolvedSampling` | 2 |  |
| `FreeU_V2` | 2 |  |
| `KSampler` | 2 |  |
| `ADE_AnimateDiffLoRALoader` | 1 |  |
| `ADE_LoadAnimateDiffModel` | 1 |  |
| `ADE_MultivalDynamic` | 1 |  |
| `AILab_QwenVL` | 1 |  |
| `CheckpointLoaderSimple` | 1 |  |
| `CLIPVisionLoader` | 1 |  |
| `EmptyLatentImage` | 1 |  |
| `FL_KsamplerPlus` | 1 |  |
| `FL_UpscaleModel` | 1 |  |
| `IPAdapterModelLoader` | 1 |  |
| `IPAdapterMS` | 1 |  |
| `LatentUpscaleBy` | 1 |  |
| `LoadImage` | 1 |  |
| `PrepImageForClipVision` | 1 |  |
| `Upscale Model Loader` | 1 |  |
