# Z-Image-Turbo Fun Union ControlNet

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_z_image_turbo_fun_union_controlnet)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_z_image_turbo_fun_union_controlnet-1.webp" width="360" alt="Z-Image-Turbo Fun Union ControlNet image_z_image_turbo_fun_union_controlnet-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_z_image_turbo_fun_union_controlnet-2.webp" width="360" alt="Z-Image-Turbo Fun Union ControlNet image_z_image_turbo_fun_union_controlnet-2.webp">

> Multi-control ControlNet supporting Canny, HED, Depth, Pose, and MLSD for Z-Image-Turbo.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_z_image_turbo_fun_union_controlnet.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_z_image_turbo_fun_union_controlnet.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/z-image/z-image-turbo)

## Details

| | |
|---|---|
| Name | `image_z_image_turbo_fun_union_controlnet` |
| Category | Foundation › Image |
| Output | image |
| Models | Z-Image-Turbo |
| Tags | Image, ControlNet |
| Type | open source |
| Date | 2025-12-02 |
| Author | ComfyUI |
| Download size | 22.2 GB |
| Min ComfyUI version | 0.4.0 |
| Usage | 350 |
| Nodes | 19 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #58 | image | image_z_image_turbo_fun_union_controlnet_input_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `z_image_turbo_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) |
| `Z-Image-Turbo-Fun-Controlnet-Union.safetensors` | `model_patches` | [link](https://huggingface.co/alibaba-pai/Z-Image-Turbo-Fun-Controlnet-Union/resolve/main/Z-Image-Turbo-Fun-Controlnet-Union.safetensors) |
| `qwen_3_4b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Z-Image-Turbo Fun Control to Image** (12 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `Canny` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageScaleToMaxDimension` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `ModelPatchLoader` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `QwenImageDiffsynthControlnet` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Guide(for local user)</summary>

Guide: [subgraph](https://docs.comfy.org/interface/features/subgraph)

[alibaba-pai/Z-Image-Turbo-Fun-Controlnet-Union](https://huggingface.co/alibaba-pai/Z-Image-Turbo-Fun-Controlnet-Union) supports multiple control conditions—including Canny, HED, Depth, Pose and MLSD. This workflow only demonstrates the Canny one; replace the `Image preprocessing` with other preprocessors to try other control methods.

## Report issue

If you found any issues when running this workflow, [report template issue here](https://github.com/Comfy-Org/workflow_templates/issues)

## Model Links

- [Hugging Face:Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo)

### Alternative Repos

- [ModelScope:Comfy-Org/z_image_turbo](https://modelscope.cn/models/Comfy-Org/z_image_turbo)

**text_encoders**

- [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) (7.49 GB)

**diffusion_models**

- [z_image_turbo_bf16.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) (11.46 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

**model_patches**

- [Z-Image-Turbo-Fun-Controlnet-Union.safetensors](https://huggingface.co/alibaba-pai/Z-Image-Turbo-Fun-Controlnet-Union/resolve/main/Z-Image-Turbo-Fun-Controlnet-Union.safetensors) (2.89 GB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── qwen_3_4b.safetensors
│   ├── 📂 diffusion_models/
│   │      └── z_image_turbo_bf16.safetensors
│   ├── 📂 vae/
│   │      └── ae.safetensors
│   └── 📂 model_patches/
│          └── Z-Image-Turbo-Fun-Controlnet-Union.safetensors
```

</details>

<details><summary>MarkdownNote</summary>

If your input image is too large(like over 2500px), please select the node above, then use Ctrl-B to enable it.

</details>
