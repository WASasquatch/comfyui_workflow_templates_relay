# Image Restoration: SUPIR

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_image_upscale_supir)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_image_upscale_supir-1.webp" width="360" alt="Image Restoration: SUPIR utility_image_upscale_supir-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_image_upscale_supir-2.webp" width="360" alt="Image Restoration: SUPIR utility_image_upscale_supir-2.webp">

> Restore and enhance images using SUPIR's generative prior and text guidance. Accepts image and optional text prompts for intelligent restoration with high-quality results.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_image_upscale_supir.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_image_upscale_supir.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/image-upscale)

## Details

| | |
|---|---|
| Name | `utility_image_upscale_supir` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | SUPIR |
| Tags | Image Upscale |
| Type | open source |
| Date | 2026-04-20 |
| Author | ComfyUI |
| Download size | 17.8 GB |
| Min ComfyUI version | 0.20.0 |
| Distributions | local |
| Usage | 0 |
| Nodes | 25 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #92 | image | blurry_city_horses.png |
| output | `SaveImage` #97 | image | utility_image_upscale_supir.png |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `juggernautXL_v9Rdphoto2Lightning.safetensors` | `checkpoints` | [link](https://huggingface.co/AiWise/Juggernaut-XL-V9-GE-RDPhoto2-Lightning_4S/resolve/main/juggernautXL_v9Rdphoto2Lightning.safetensors) |
| `SUPIR-v0Q_fp16.safetensors` | `model_patches` | [link](https://huggingface.co/Kijai/SUPIR_pruned/resolve/main/SUPIR-v0Q_fp16.safetensors) |
| `qwen3.5_4b_bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Qwen3.5/resolve/main/text_encoders/qwen3.5_4b_bf16.safetensors) |

## Subgraphs

- **Image Upscale (SUPIR)** (21 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncodeSDXL` | 2 | comfy-core |
| `PrimitiveStringMultiline` | 2 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `BOOLConstant` | 1 | comfyui-kjnodes |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `ColorTransfer` | 1 | comfy-core |
| `ComfySwitchNode` | 1 | comfy-core |
| `EmptyLatentImage` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageCompare` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelPatchLoader` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `ResizeImageMaskNode` | 1 | comfy-core |
| `SamplerCustom` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `StringConcatenate` | 1 | comfy-core |
| `SUPIRApply` | 1 | comfy-core |
| `TextGenerate` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model Links</summary>

- Related PR: [#13250](https://github.com/Comfy-Org/ComfyUI/pull/13250)
- Original Repo: [Fanghua-Yu/SUPIR](https://github.com/Fanghua-Yu/SUPIR)

## Model Links

- [Hugging Face:Comfy-Org/Qwen3.5](https://huggingface.co/Comfy-Org/Qwen3.5)
- [ModelScope:Comfy-Org/Qwen3.5](https://modelscope.cn/models/Comfy-Org/Qwen3.5)

**checkpoints**

- [juggernautXL_v9Rdphoto2Lightning.safetensors](https://huggingface.co/AiWise/Juggernaut-XL-V9-GE-RDPhoto2-Lightning_4S/resolve/main/juggernautXL_v9Rdphoto2Lightning.safetensors) (6.62 GB)

**model_patches**

- [SUPIR-v0Q_fp16.safetensors](https://huggingface.co/Kijai/SUPIR_pruned/resolve/main/SUPIR-v0Q_fp16.safetensors) (2.48 GB)

**text_encoders**

- [qwen3.5_4b_bf16.safetensors](https://huggingface.co/Comfy-Org/Qwen3.5/resolve/main/text_encoders/qwen3.5_4b_bf16.safetensors) (8.68 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │   └── juggernautXL_v9Rdphoto2Lightning.safetensors
│   ├── 📂 model_patches/
│   │   └── SUPIR-v0Q_fp16.safetensors
│   └── 📂 text_encoders/
│       └── qwen3.5_4b_bf16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
