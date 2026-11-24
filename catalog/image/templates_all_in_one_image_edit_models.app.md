# 1 input and multiple editing model comparison

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_all_in_one_image_edit_models.app)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_all_in_one_image_edit_models.app-1.webp" width="360" alt="1 input and multiple editing model comparison templates_all_in_one_image_edit_models.app-1.webp">

> One click generations to test all the leading image editing models.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_all_in_one_image_edit_models.app.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_all_in_one_image_edit_models.app.json)

## Details

| | |
|---|---|
| Name | `templates_all_in_one_image_edit_models.app` |
| Category | Foundation › Image |
| Output | image |
| Models | Nano Banana 2, Grok, Qwen-Image-Edit |
| Tags | API, Style Transfer, Image Edit |
| Type | API |
| Date | 2026-03-09 |
| Author | hellorob |
| Download size | 132.9 GB |
| Min ComfyUI version | 0.33.3 |
| Distributions | cloud |
| Usage | 8 |
| Nodes | 82 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #183 | image | input-illustration_to_real-1.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux-2-klein-base-4b-fp8.safetensors` | `diffusion_models` | [link](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4b-fp8/resolve/main/flux-2-klein-base-4b-fp8.safetensors) |
| `flux-2-klein-base-9b-fp8.safetensors` | `diffusion_models` | [link](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-9b-fp8/resolve/main/flux-2-klein-base-9b-fp8.safetensors) |
| `flux2_dev_fp8mixed.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/diffusion_models/flux2_dev_fp8mixed.safetensors) |
| `qwen_image_edit_2511_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2511_bf16.safetensors) |
| `mistral_3_small_flux2_bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/text_encoders/mistral_3_small_flux2_bf16.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_3_4b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) |
| `qwen_3_8b_fp8mixed.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/flux2-klein-9B/resolve/main/split_files/text_encoders/qwen_3_8b_fp8mixed.safetensors) |
| `flux2-vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Image Edit (FLUX.2 Dev)** (16 nodes)
- **Image Edit (Qwen 2511)** (15 nodes)
- **Image Edit (FLUX.2 Klein 9B)** (15 nodes)
- **Image Edit (FLUX.2 Klein 9B)** (15 nodes)
- **Reference Conditioning** (3 nodes)
- **Reference Conditioning** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `SaveImage` | 9 | comfy-core |
| `CLIPTextEncode` | 5 | comfy-core |
| `ReferenceLatent` | 5 | comfy-core |
| `CLIPLoader` | 4 | comfy-core |
| `UNETLoader` | 4 | comfy-core |
| `VAEDecode` | 4 | comfy-core |
| `VAEEncode` | 4 | comfy-core |
| `VAELoader` | 4 | comfy-core |
| `EmptyFlux2LatentImage` | 3 | comfy-core |
| `Flux2Scheduler` | 3 | comfy-core |
| `GetImageSize` | 3 | comfy-core |
| `ImageScaleToTotalPixels` | 3 | comfy-core |
| `KSamplerSelect` | 3 | comfy-core |
| `RandomNoise` | 3 | comfy-core |
| `SamplerCustomAdvanced` | 3 | comfy-core |
| `CFGGuider` | 2 | comfy-core |
| `FluxKontextMultiReferenceLatentMethod` | 2 | comfy-core |
| `MarkdownNote` | 2 |  |
| `TextEncodeQwenImageEditPlus` | 2 | comfy-core |
| `BasicGuider` | 1 | comfy-core |
| `ByteDanceSeedreamNode` | 1 | comfy-core |
| `CFGNorm` | 1 | comfy-core |
| `FluxGuidance` | 1 | comfy-core |
| `FluxKontextImageScale` | 1 | comfy-core |
| `GeminiImage2Node` | 1 | comfy-core |
| `GeminiNanoBanana2` | 1 |  |
| `GrokImageEditNode` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `Note` | 1 |  |
| `OpenAIGPTImage1` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/flux2-dev](https://huggingface.co/Comfy-Org/flux2-dev)
- [Hugging Face:Comfy-Org/Qwen-Image-Edit_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI)
- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)
- [Hugging Face:Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo)
- [Hugging Face:Comfy-Org/HunyuanVideo_1.5_repackaged](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/flux2-dev](https://modelscope.cn/models/Comfy-Org/flux2-dev)
- [ModelScope:Comfy-Org/Qwen-Image-Edit_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image-Edit_ComfyUI)
- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)
- [ModelScope:Comfy-Org/z_image_turbo](https://modelscope.cn/models/Comfy-Org/z_image_turbo)
- [ModelScope:Comfy-Org/HunyuanVideo_1.5_repackaged](https://modelscope.cn/models/Comfy-Org/HunyuanVideo_1.5_repackaged)

**diffusion_models**

- [flux-2-klein-base-4b-fp8.safetensors](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4b-fp8/resolve/main/flux-2-klein-base-4b-fp8.safetensors) (3.81 GB)
- [flux2_dev_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/diffusion_models/flux2_dev_fp8mixed.safetensors) (33.02 GB)
- [qwen_image_edit_2511_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2511_bf16.safetensors) (38.05 GB)

**vae**

- [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) (320.6 MB)
- [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

**text_encoders**

- [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) (7.49 GB)
- [mistral_3_small_flux2_bf16.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/text_encoders/mistral_3_small_flux2_bf16.safetensors) (33.14 GB)
- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   ├── flux-2-klein-base-4b-fp8.safetensors
│   │   ├── flux2_dev_fp8mixed.safetensors
│   │   └── qwen_image_edit_2511_bf16.safetensors
│   ├── 📂 vae/
│   │   ├── flux2-vae.safetensors
│   │   └── qwen_image_vae.safetensors
│   └── 📂 text_encoders/
│       ├── qwen_3_4b.safetensors
│       ├── mistral_3_small_flux2_bf16.safetensors
│       └── qwen_2.5_vl_7b_fp8_scaled.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>KSampler settings</summary>

You can test and find the best setting by yourself. The following table is for reference.
|   | Qwen | Comfy | lightning LoRA |
|--------|---------|------------|---------------------------|
| Steps  | 40      | 20         | 4                         |
| CFG    | 4.0     | 4.0       | 1.0                       |

By default, we use 20 steps as we just don't want it to take too long. Try 40 if you want a better result, but it will take longer.

</details>

<details><summary>Note</summary>

```text
The "Edit Model Reference Method" nodes above are not needed if you use Comfy files, but may be needed if you use repackaged ones from other people.
```

</details>
