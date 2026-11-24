# Flux.1 Dev OneReward

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_flux.1_fill_dev_OneReward)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux.1_fill_dev_OneReward-1.webp" width="360" alt="Flux.1 Dev OneReward image_flux.1_fill_dev_OneReward-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux.1_fill_dev_OneReward-2.webp" width="360" alt="Flux.1 Dev OneReward image_flux.1_fill_dev_OneReward-2.webp">

> Supports various tasks such as image inpainting, outpainting, and object removal by bytedance-research team

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_flux.1_fill_dev_OneReward.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_flux.1_fill_dev_OneReward.json)
- [Tutorial](https://docs.comfy.org/tutorials/flux/flux-1-fill-dev)

## Details

| | |
|---|---|
| Name | `image_flux.1_fill_dev_OneReward` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX.1, FLUX |
| Tags | Inpainting, Outpainting |
| Type | open source |
| Date | 2025-09-21 |
| Author | ComfyUI |
| Download size | 20.8 GB |
| Min ComfyUI version | 0.3.42 |
| Usage | 62 |
| Nodes | 30 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #17 | image | image_flux.1_fill_dev_OneReward_input_image.png |
| output | `SaveImage` #62 | image | image_flux.1_fill_dev_OneReward.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux.1-fill-dev-OneReward-transformer_fp8.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/OneReward_repackaged/resolve/main/split_files/diffusion_models/flux.1-fill-dev-OneReward-transformer_fp8.safetensors) |
| `removal_timestep_alpha-2-1740.safetensors` | `loras` | [link](https://huggingface.co/lrzjason/ObjectRemovalFluxFill/resolve/main/removal_timestep_alpha-2-1740.safetensors) |
| `clip_l.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true) |
| `t5xxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true) |
| `t5xxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **OneReward Image Inpainting** (12 nodes)
- **OneReward Image Outpainting** (12 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `ConditioningZeroOut` | 2 | comfy-core |
| `DifferentialDiffusion` | 2 | comfy-core |
| `DualCLIPLoader` | 2 | comfy-core |
| `FluxGuidance` | 2 | comfy-core |
| `InpaintModelConditioning` | 2 | comfy-core |
| `KSampler` | 2 | comfy-core |
| `PreviewImage` | 2 | comfy-core |
| `UNETLoader` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `ImagePadForOutpaint` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `SetLatentNoiseMask` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: How to draw mask</summary>

Right-click on the Load Image node, then click Open in `Maskeditor` to edit the mask.

</details>

<details><summary>Note: About OneReward and Model links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/OneReward_repackaged](https://huggingface.co/Comfy-Org/OneReward_repackaged)
- [Hugging Face:Comfy-Org/Lumina_Image_2.0_Repackaged](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/OneReward_repackaged](https://modelscope.cn/models/Comfy-Org/OneReward_repackaged)
- [ModelScope:Comfy-Org/Lumina_Image_2.0_Repackaged](https://modelscope.cn/models/Comfy-Org/Lumina_Image_2.0_Repackaged)

**text_encoders**

- [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true) (234.7 MB)
- [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true) (9.12 GB)
- [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) (9.12 GB)

**loras**

- [removal_timestep_alpha-2-1740.safetensors](https://huggingface.co/lrzjason/ObjectRemovalFluxFill/resolve/main/removal_timestep_alpha-2-1740.safetensors) (85.6 MB)

**diffusion_models**

- [flux.1-fill-dev-OneReward-transformer_fp8.safetensors](https://huggingface.co/Comfy-Org/OneReward_repackaged/resolve/main/split_files/diffusion_models/flux.1-fill-dev-OneReward-transformer_fp8.safetensors) (11.09 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      ├── clip_l.safetensors
│   │      ├── t5xxl_fp16.safetensors
│   │      └── t5xxl_fp16.safetensors
│   ├── 📂 loras/
│   │      └── removal_timestep_alpha-2-1740.safetensors
│   ├── 📂 diffusion_models/
│   │      └── flux.1-fill-dev-OneReward-transformer_fp8.safetensors
│   └── 📂 vae/
│          └── ae.safetensors
```

## Report issue

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: About object removal</summary>

By default, this group is an image inpainting workflow. 

You can select the  the 
**LoraLoaderModelOnly** node and use **Ctrl+B** to enable it, which will turn it into an object removal workflow.

</details>
