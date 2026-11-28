# Flux.1 Dev USO Reference Image Generation

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=flux1_dev_uso_reference_image_gen)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux1_dev_uso_reference_image_gen-1.webp" width="360" alt="Flux.1 Dev USO Reference Image Generation flux1_dev_uso_reference_image_gen-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux1_dev_uso_reference_image_gen-2.webp" width="360" alt="Flux.1 Dev USO Reference Image Generation flux1_dev_uso_reference_image_gen-2.webp">

> Use reference images to control both style and subject - keep your character's face while changing artistic style, or apply artistic styles to new scenes

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux1_dev_uso_reference_image_gen.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/flux1_dev_uso_reference_image_gen.json)
- [Tutorial](https://docs.comfy.org/tutorials/flux/flux-1-uso)

## Details

| | |
|---|---|
| Name | `flux1_dev_uso_reference_image_gen` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX, FLUX.1 |
| Tags | Image, Style Reference |
| Type | open source |
| Date | 2025-09-02 |
| Author | ComfyUI |
| Download size | 17.3 GB |
| Min ComfyUI version | 0.3.57 |
| Usage | 131 |
| Nodes | 42 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #47 | image | flux1_dev_uso_reference_image_gen_input_image.png |
| output | `SaveImage` #9 | image | flux1_dev_uso_reference_image_gen.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux1-dev-fp8.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors) |
| `sigclip_vision_patch14_384.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/sigclip_vision_384/resolve/main/sigclip_vision_patch14_384.safetensors) |
| `uso-flux1-dit-lora-v1.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/USO_1.0_Repackaged/resolve/main/split_files/loras/uso-flux1-dit-lora-v1.safetensors) |
| `uso-flux1-projector-v1.safetensors` | `model_patches` | [link](https://huggingface.co/Comfy-Org/USO_1.0_Repackaged/resolve/main/split_files/model_patches/uso-flux1-projector-v1.safetensors) |

## Subgraphs

- **USOStyleReference** (2 nodes)
- **USOStyleReference** (2 nodes)
- **USO Character Reference** (19 nodes)
- **USO Reference Conditioning** (3 nodes)
- **USOStyleReference(Subgraph)** (2 nodes)
- **USOStyleReference(Subgraph)** (2 nodes)
- **USO Style Reference** (11 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 5 | comfy-core |
| `CLIPVisionEncode` | 4 | comfy-core |
| `MarkdownNote` | 4 |  |
| `USOStyleReference` | 4 | comfy-core |
| `CheckpointLoaderSimple` | 2 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `CLIPVisionLoader` | 2 | comfy-core |
| `ConditioningZeroOut` | 2 | comfy-core |
| `KSampler` | 2 | comfy-core |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `ModelPatchLoader` | 2 | comfy-core |
| `SaveImage` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `EmptyLatentImage` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `FluxGuidance` | 1 | comfy-core |
| `FluxKontextMultiReferenceLatentMethod` | 1 | comfy-core |
| `ImageScaleToMaxDimension` | 1 | comfy-core |
| `ReferenceLatent` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>For Local User</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Report issue

Note: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

## Model Links

- [Hugging Face:Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev)
- [Hugging Face:Comfy-Org/sigclip_vision_384](https://huggingface.co/Comfy-Org/sigclip_vision_384)
- [Hugging Face:Comfy-Org/USO_1.0_Repackaged](https://huggingface.co/Comfy-Org/USO_1.0_Repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/flux1-dev](https://modelscope.cn/models/Comfy-Org/flux1-dev)
- [ModelScope:Comfy-Org/sigclip_vision_384](https://modelscope.cn/models/Comfy-Org/sigclip_vision_384)
- [ModelScope:Comfy-Org/USO_1.0_Repackaged](https://modelscope.cn/models/Comfy-Org/USO_1.0_Repackaged)

**checkpoints**

- [flux1-dev-fp8.safetensors](https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors) (16.06 GB)

**clip_vision**

- [sigclip_vision_patch14_384.safetensors](https://huggingface.co/Comfy-Org/sigclip_vision_384/resolve/main/sigclip_vision_patch14_384.safetensors) (816.8 MB)

**loras**

- [uso-flux1-dit-lora-v1.safetensors](https://huggingface.co/Comfy-Org/USO_1.0_Repackaged/resolve/main/split_files/loras/uso-flux1-dit-lora-v1.safetensors) (456 MB)

**model_patches**

- [uso-flux1-projector-v1.safetensors](https://huggingface.co/Comfy-Org/USO_1.0_Repackaged/resolve/main/split_files/model_patches/uso-flux1-projector-v1.safetensors) (20.5 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │      └── flux1-dev-fp8.safetensors
│   ├── 📂 clip_vision/
│   │      └── sigclip_vision_patch14_384.safetensors
│   ├── 📂 loras/
│   │      └── uso-flux1-dit-lora-v1.safetensors
│   └── 📂 model_patches/
│          └── uso-flux1-projector-v1.safetensors
```

</details>

<details><summary>About Style reference</summary>

The output image will reference the style from the images you uploaded. 

You can disable all reference image inputs and use this workflow as a subject-driven image generation workflow.

</details>

<details><summary>About ImageScaleToMaxDimension</summary>

Different largest_size values affect how much the character features from the reference image are retained in the final output image.

512px is the recommendation from the UXO team, as it preserves more character features.

However, tests also show that if you only use images of the character's head as input, the final output image often has issues like the character taking up too much space. Setting it to 1024px gives much better results.

So please use different size settings based on the characteristics of your input image to get the best output.

</details>

<details><summary>About EasyCache</summary>

The EasyCache node will maintain a `cumulative_change_rate`. When this value is lower than the `reuse_threshold`, it skips the current step and uses the cached result.

This node can reduce inference time, but it also sacrifices some quality and details. You can bypass it (Ctrl+B) if you don't need it.

</details>
