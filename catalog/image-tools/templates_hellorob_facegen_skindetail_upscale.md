# Skin Enhancer + Upscaler

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_hellorob_facegen_skindetail_upscale)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_hellorob_facegen_skindetail_upscale-1.webp" width="360" alt="Skin Enhancer + Upscaler templates_hellorob_facegen_skindetail_upscale-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_hellorob_facegen_skindetail_upscale-2.webp" width="360" alt="Skin Enhancer + Upscaler templates_hellorob_facegen_skindetail_upscale-2.webp">

> One click workflow to generate a character portrait, refine/add skin details, and upscale to 4k. All done in less than 60 seconds.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_hellorob_facegen_skindetail_upscale.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_hellorob_facegen_skindetail_upscale.json)

## Details

| | |
|---|---|
| Name | `templates_hellorob_facegen_skindetail_upscale` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | Z-Image-Turbo, SDXL |
| Tags | Image Upscale |
| Type | open source |
| Date | 2026-03-09 |
| Author | hellorob |
| Download size | 25.9 GB |
| Min ComfyUI version | 0.9.0 |
| Usage | 234 |
| Nodes | 66 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #17 | image | input_face-1.png |
| output | `SaveImage` #282 | image | templates_hellorob_facegen_skindetail_upscale-1.png |
| output | `SaveImage` #286 | image | templates_hellorob_facegen_skindetail_upscale-2.png |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [comfyui_essentials](https://registry.comfy.org/nodes/comfyui_essentials)
- [comfyui_face_parsing](https://registry.comfy.org/nodes/comfyui_face_parsing)
- [comfyui_ultimatesdupscale](https://registry.comfy.org/nodes/comfyui_ultimatesdupscale)
- [seedvr2_videoupscaler](https://registry.comfy.org/nodes/seedvr2_videoupscaler)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors` | `checkpoints` | [link](https://huggingface.co/RunDiffusion/Juggernaut-XL-v9/resolve/main/Juggernaut-XL_v9_RunDiffusionPhoto_v2.safetensors?download=true) |
| `z_image_turbo_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) |
| `sdxl-better_freckles.safetensors` | `loras` | [link](https://civitai.com/api/download/models/588715) |
| `sdxl-skin_realism_acne_skin_details_imperfections.safetensors` | `loras` | [link](https://civitai.com/api/download/models/340833) |
| `zimage-grainscape_ultrareal.safetensors` | `loras` | [link](https://civitai.com/api/download/models/2460872) |
| `qwen_3_4b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Image Upscale(SeedVR2)** (9 nodes)
- **New Subgraph** (40 nodes)
- **Text to Image (Z-Image-Turbo)** (10 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Reroute` | 12 |  |
| `CLIPTextEncode` | 3 | comfy-core |
| `ImageCompare` | 3 |  |
| `LoraLoaderModelOnly` | 3 | comfy-core |
| `MarkdownNote` | 3 |  |
| `GetImageSize` | 2 | comfy-core |
| `PreviewImage` | 2 | comfy-core |
| `PrimitiveFloat` | 2 | comfy-core |
| `SaveImage` | 2 | comfy-core |
| `BBoxDetect(FaceParsing)` | 1 | comfyui_face_parsing |
| `BBoxDetectorLoader(FaceParsing)` | 1 | comfyui_face_parsing |
| `BBoxListItemSelect(FaceParsing)` | 1 | comfyui_face_parsing |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `ComfySwitchNode` | 1 |  |
| `ConditioningZeroOut` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `FaceParse(FaceParsing)` | 1 | comfyui_face_parsing |
| `FaceParsingModelLoader(FaceParsing)` | 1 | comfyui_face_parsing |
| `FaceParsingProcessorLoader(FaceParsing)` | 1 | comfyui_face_parsing |
| `FaceParsingResultsParser(FaceParsing)` | 1 | comfyui_face_parsing |
| `GrowMaskWithBlur` | 1 | comfyui-kjnodes |
| `ImageCompositeMasked` | 1 | comfy-core |
| `ImageCropWithBBox(FaceParsing)` | 1 | comfyui_face_parsing |
| `ImageInsertWithBBox(FaceParsing)` | 1 | comfyui_face_parsing |
| `ImageResizeKJv2` | 1 | comfyui-kjnodes |
| `ImpactCompare` | 1 |  |
| `KSampler` | 1 | comfy-core |
| `LayerUtility: If` | 1 |  |
| `LoadImage` | 1 | comfy-core |
| `MaskPreview` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `Note` | 1 |  |
| `PrimitiveNode` | 1 |  |
| `SeedVR2LoadDiTModel` | 1 | seedvr2_videoupscaler |
| `SeedVR2LoadVAEModel` | 1 | seedvr2_videoupscaler |
| `SeedVR2VideoUpscaler` | 1 | seedvr2_videoupscaler |
| `SimpleMath+` | 1 | comfyui_essentials |
| `UltimateSDUpscale` | 1 | comfyui_ultimatesdupscale |
| `UNETLoader` | 1 | comfy-core |
| `UpscaleModelLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Add Skin Detail Explained</summary>

## Prompt
Describe features of the face you want to have, such as:
- man/woman, freckles, red blush on cheeks, long dark eyelashes, acne, mascara, without-makeup, facial hair, etc

## Denoise
- Higher denoise → more change to the face *(recommended 0.15–0.35)*

## Feature Toggles
`nose` `r_eye` `l_eye` `r_brow` `l_brow` `u_lip` `l_lip`
- Features toggled **on** (`true`) will change
- Features toggled **off** (`false`) will be retained

</details>

<details><summary>Image Switch Explained</summary>

Toggle Off = Z-image-turbo image
Toggle On = Load Image

</details>

<details><summary>Note</summary>

## About SeedVR2

You can watch a comprehensive tutorial from the author on [Youtube](https://www.youtube.com/watch?v=MBtWYXq_r60) or check out the [Github](https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler).

## Quick Notes
Hover over the node inputs for tooltip info from author

input_noise_scale softens higher frequency details (e.g. skin textures)

latent_noise_scale softens low frequency details. Best around 0.01-0.05 (but depends on upscale factor)

Nodes support alpha masks

</details>

<details><summary>Note</summary>

```text
Bypass (ctrl+B) the "LoraLoaderModelOnly" if you do not want to add freckles (also add/remove "freckles" from the prompt)
```

</details>
