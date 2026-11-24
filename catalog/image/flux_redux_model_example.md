# Flux.1 Redux Model

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_redux_model_example-1.webp" width="360" alt="Flux.1 Redux Model flux_redux_model_example-1.webp">

> Generate images by transferring style from reference images using Flux.1 Redux.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_redux_model_example.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/flux_redux_model_example.json)
- [Tutorial](https://docs.comfy.org/tutorials/flux/flux-1-controlnet)

## Details

| | |
|---|---|
| Name | `flux_redux_model_example` |
| Category | Foundation › Image |
| Media type | image |
| Models | FLUX.1, FLUX |
| Tags | ControlNet, Image |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 32.7 GB |
| Min ComfyUI version | 0.0.4 |
| Usage | 15 |
| Nodes | 29 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #40 | image | flux_redux_model_example_reference_image_1.png |
| input | `LoadImage` #47 | image | flux_redux_model_example_reference_image_2.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sigclip_vision_patch14_384.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/sigclip_vision_384/resolve/main/sigclip_vision_patch14_384.safetensors?download=true) |
| `flux1-dev.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev.safetensors) |
| `flux1-redux-dev.safetensors` | `style_models` | [link](https://huggingface.co/Comfy-Org/Flux1-Redux-Dev/resolve/main/flux1-redux-dev.safetensors) |
| `clip_l.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors) |
| `t5xxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `CLIPVisionEncode` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `Note` | 2 |  |
| `PrimitiveNode` | 2 |  |
| `StyleModelApply` | 2 | comfy-core |
| `BasicGuider` | 1 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `DualCLIPLoader` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `FluxGuidance` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `ModelSamplingFlux` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `StyleModelLoader` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

[Tutorial](https://comfyanonymous.github.io/ComfyUI_examples/flux/#redux)

## Model Links

- [Hugging Face:Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev)
- [Hugging Face:Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384)
- [Hugging Face:Comfy-Org/Flux1-Redux-Dev](https://huggingface.co/Comfy-Org/Flux1-Redux-Dev)
- [Hugging Face:Comfy-Org/Lumina_Image_2.0_Repackaged](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/flux1-dev](https://modelscope.cn/models/Comfy-Org/flux1-dev)
- [ModelScope:Comfy-Org/sigclip_vision_384](https://modelscope.cn/models/Comfy-Org/sigclip_vision_384)
- [ModelScope:Comfy-Org/Flux1-Redux-Dev](https://modelscope.cn/models/Comfy-Org/Flux1-Redux-Dev)
- [ModelScope:Comfy-Org/Lumina_Image_2.0_Repackaged](https://modelscope.cn/models/Comfy-Org/Lumina_Image_2.0_Repackaged)

**Diffusion model**

- [flux1-dev.safetensors](https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev.safetensors) (22.17 GB)

**Text encoder**

- [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors) (234.7 MB)
- [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) (9.12 GB) or [t5xxl_fp8_e4m3fn.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn.safetensors) (4.56 GB)

**CLIP Vision**

- [sigclip_vision_patch14_384.safetensors](https://huggingface.co/Comfy-Org/sigclip_vision_384/resolve/main/sigclip_vision_patch14_384.safetensors) (816.8 MB)

**Style model**

- [flux1-redux-dev.safetensors](https://huggingface.co/Comfy-Org/Flux1-Redux-Dev/resolve/main/flux1-redux-dev.safetensors) (123.1 MB)

**VAE**
- [ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

Tip: You can set the weight_dtype above to one of the fp8 types if you have memory issues.

**Models save location**

```
ComfyUI/
├── models/
│   ├── diffusion_models/
│   │   └─── flux1-dev.safetensors
│   ├── style_models/
│   │   └─── flux1-redux-dev.safetensors
│   ├── text_encoders/
│   │   ├── clip_l.safetensors
│   │   └─── t5xxl_fp16.safetensors or t5xxl_fp8_e4m3fn.safetensors
│   ├── clip_vision/
│   │   └── sigclip_vision_patch14_384.safetensors
│   └── vae/
│       └── ae.safetensors
```

</details>

<details><summary>Note</summary>

```text
The redux model lets you prompt with images. It can be used with any Flux1 dev or schnell model workflow.

You can chain multiple "Apply Style Model" nodes if you want to mix multiple images together.
```

</details>

<details><summary>Note</summary>

```text
The reference sampling implementation auto adjusts the shift value based on the resolution, if you don't want this you can just bypass (CTRL-B) this ModelSamplingFlux node.
```

</details>

<details><summary>Note: About Flux redux</summary>

## Flux Redux (by Black Forest Labs)

**Key Features**
- **No Prompt Required**: Extracts style features directly from input images to generate image variations, no text prompts needed.
- **Multi-Image Blending Support**: Blends styles of multiple input images for more creative possibilities.
- **Good Integration**: Seamlessly fits into complex workflows; enables image restyling via prompts.
- **Advanced Performance**: Excels in image variation generation, producing high-quality variations efficiently.

</details>

<details><summary>Note: About prompt</summary>

Even without a prompt, this model can still apply the image styles from the reference images.

</details>
