# Noise Injected VideoGen

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_mjm_Injected-1.webp" width="360" alt="Noise Injected VideoGen templates_mjm_Injected-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_mjm_Injected-2.webp" width="360" alt="Noise Injected VideoGen templates_mjm_Injected-2.webp">

> Upload a starting image and a mask video to define the injection area. Generate a dynamic video by injecting noise patterns from a dedicated noise video, with AI auto-generated prompts.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_mjm_Injected.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_mjm_Injected.json)

## Details

| | |
|---|---|
| Name | `templates_mjm_Injected` |
| Category | Foundation › Video |
| Media type | image |
| Models | SD1.5 |
| Tags | Video, Image to Video |
| Type | open source |
| Date | 2026-03-02 |
| Author | Julien \| MJM |
| Download size | 10.0 GB |
| Min ComfyUI version | 0.3.42 |
| Usage | 1 |
| Nodes | 32 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #8 | image | Init.png |
| input | `VHS_LoadVideo` #126 | video | Noise_injection.mp4 |
| input | `VHS_LoadVideo` #137 | video | Mask.mp4 |
| output | `SaveVideo` #209 | video | templates_mjm_Injected.mp4 |

## Custom nodes required

- [comfyui-animatediff-evolved](https://registry.comfy.org/nodes/comfyui-animatediff-evolved)
- [comfyui-frame-interpolation](https://registry.comfy.org/nodes/comfyui-frame-interpolation)
- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)
- [QwenVL](https://registry.comfy.org/nodes/QwenVL)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `realismByStableYogi_v4LCM.safetensors` | `checkpoints` | [link](https://civitai.com/api/download/models/353362?type=Model&format=SafeTensor&size=full&fp=fp16) |

## Subgraphs

- **AD with Image Injection** (11 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ImageScale` | 3 |  |
| `CLIPTextEncode` | 2 |  |
| `FILM VFI` | 2 |  |
| `INTConstant` | 2 |  |
| `VHS_LoadVideo` | 2 |  |
| `VHS_VideoCombine` | 2 |  |
| `ADE_AnimateDiffLoaderWithContext` | 1 |  |
| `ADE_AnimateDiffSamplingSettings` | 1 |  |
| `ADE_LoopedUniformContextOptions` | 1 |  |
| `ADE_MultivalDynamic` | 1 |  |
| `ADE_NoisedImageInjection` | 1 |  |
| `AILab_QwenVL` | 1 |  |
| `CheckpointLoaderSimple` | 1 |  |
| `CreateVideo` | 1 |  |
| `GetImageSizeAndCount` | 1 |  |
| `ImageBlur` | 1 |  |
| `ImageToMask` | 1 |  |
| `KSampler` | 1 |  |
| `LoadImage` | 1 |  |
| `PreviewAny` | 1 |  |
| `PrimitiveInt` | 1 |  |
| `RepeatLatentBatch` | 1 |  |
| `SaveVideo` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAEEncode` | 1 |  |
