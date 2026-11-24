# Chroma1 Radiance Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_chroma1_radiance_text_to_image)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_chroma1_radiance_text_to_image-1.webp" width="360" alt="Chroma1 Radiance Text to Image image_chroma1_radiance_text_to_image-1.webp">

> Chroma1-Radiance works directly with image pixels instead of compressed latents, delivering higher quality images with reduced artifacts and distortion.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_chroma1_radiance_text_to_image.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_chroma1_radiance_text_to_image.json)

## Details

| | |
|---|---|
| Name | `image_chroma1_radiance_text_to_image` |
| Category | Foundation › Image |
| Output | image |
| Models | Chroma |
| Tags | Image, Text to Image |
| Type | open source |
| Date | 2025-09-18 |
| Author | ComfyUI |
| Download size | 22.5 GB |
| Min ComfyUI version | 0.3.60 |
| Usage | 31 |
| Nodes | 21 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImage` #740 | image | image_chroma1_radiance_text_to_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `chroma-radiance-x0.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Chroma1-Radiance_Repackaged/resolve/main/split_files/diffusion_models/chroma-radiance-x0.safetensors) |
| `t5xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn_scaled.safetensors) |

## Subgraphs

- **Chroma1 Radiance Text to Image** (19 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Note` | 4 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `BetaSamplingScheduler` | 1 | comfy-core |
| `CFGGuider` | 1 | comfy-core |
| `ChromaRadianceOptions` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `EmptyChromaRadianceLatentImage` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `T5TokenizerOptions` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>For Local User</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model links

- [Hugging Face:Comfy-Org/Chroma1-Radiance_Repackaged](https://huggingface.co/Comfy-Org/Chroma1-Radiance_Repackaged)
- [ModelScope:Comfy-Org/Chroma1-Radiance_Repackaged](https://modelscope.cn/models/Comfy-Org/Chroma1-Radiance_Repackaged)

**text_encoders**

- [t5xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn_scaled.safetensors) (4.8 GB)

**diffusion_models**

- [chroma-radiance-x0.safetensors](https://huggingface.co/Comfy-Org/Chroma1-Radiance_Repackaged/resolve/main/split_files/diffusion_models/chroma-radiance-x0.safetensors) (17.71 GB)


Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── t5xxl_fp8_e4m3fn_scaled.safetensors
│   └── 📂 diffusion_models/
│          └── chroma-radiance-x0.safetensors
```

## Report issue

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Optional Padding</summary>

```text
min_padding 1 is the official way. setting it to 0 works too.
```

</details>

<details><summary>ChromaRadianceOptions</summary>

```text
You can put nerf_tile_size as large as possible until you run out of GPU memory if you want increased speed. Hover over to see tooltip.
```

</details>

<details><summary>Note</summary>

```text
This Chroma1 Radiance image generation is in pixel space. No additional VAE is needed.
```

</details>

<details><summary>Optional Flow Shift</summary>

```text
Flow Shift node set to 1.0 represents intended shift by the creator of the Chroma model and will produce greater detail.  The Flow Shift can be raised up to 3.0 in order to help with complex compositions.
```

</details>
