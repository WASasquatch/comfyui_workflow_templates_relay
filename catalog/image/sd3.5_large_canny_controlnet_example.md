# SD3.5 Large Canny ControlNet

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=sd3.5_large_canny_controlnet_example)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/sd3.5_large_canny_controlnet_example-1.webp" width="360" alt="SD3.5 Large Canny ControlNet sd3.5_large_canny_controlnet_example-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/sd3.5_large_canny_controlnet_example-2.webp" width="360" alt="SD3.5 Large Canny ControlNet sd3.5_large_canny_controlnet_example-2.webp">

> Generate images guided by edge detection using SD 3.5 Canny ControlNet.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/sd3.5_large_canny_controlnet_example.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/sd3.5_large_canny_controlnet_example.json)
- [Tutorial](https://comfyanonymous.github.io/ComfyUI_examples/sd3/#sd35-controlnets)

## Details

| | |
|---|---|
| Name | `sd3.5_large_canny_controlnet_example` |
| Category | Foundation › Image |
| Output | image |
| Models | SD3.5, Stability |
| Tags | Image, ControlNet |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 22.0 GB |
| Min ComfyUI version | 0.3.5 |
| Usage | 14 |
| Nodes | 14 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #45 | image | sd3.5_large_canny_controlnet_example_input_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sd3.5_large_fp8_scaled.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8/resolve/main/sd3.5_large_fp8_scaled.safetensors) |
| `sd3.5_large_controlnet_canny.safetensors` | `controlnet` | [link](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-controlnets_ComfyUI_repackaged/resolve/main/split_files/controlnet/sd3.5_large_controlnet_canny.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `Canny` | 1 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `ControlNetApplyAdvanced` | 1 | comfy-core |
| `ControlNetLoader` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `ImageScale` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `PreviewImage` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Model links</summary>

## Model Links

- [Hugging Face:Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8)
- [Hugging Face:Comfy-Org/stable-diffusion-3.5-controlnets_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-controlnets_ComfyUI_repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/stable-diffusion-3.5-fp8](https://modelscope.cn/models/Comfy-Org/stable-diffusion-3.5-fp8)
- [ModelScope:Comfy-Org/stable-diffusion-3.5-controlnets_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/stable-diffusion-3.5-controlnets_ComfyUI_repackaged)

**checkpoints**

- [sd3.5_large_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8/resolve/main/sd3.5_large_fp8_scaled.safetensors) (13.91 GB)

**controlnet**

- [sd3.5_large_controlnet_canny.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-controlnets_ComfyUI_repackaged/resolve/main/split_files/controlnet/sd3.5_large_controlnet_canny.safetensors) (8.06 GB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │      └── sd3.5_large_fp8_scaled.safetensors
│   └── 📂 controlnet/
│          └── sd3.5_large_controlnet_canny.safetensors
```

</details>
