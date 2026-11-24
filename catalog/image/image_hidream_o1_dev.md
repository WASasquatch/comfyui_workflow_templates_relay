# HiDream O1 Dev

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_hidream_o1_dev-1.webp" width="360" alt="HiDream O1 Dev image_hidream_o1_dev-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_hidream_o1_dev-2.webp" width="360" alt="HiDream O1 Dev image_hidream_o1_dev-2.webp">

> Input a text prompt and optional reference images. Generate a high-resolution image (up to 2048x2048) with support for text-to-image, image editing, and subject-driven personalization.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_hidream_o1_dev.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_hidream_o1_dev.json)
- [Tutorial](https://docs.comfy.org/tutorials/image/hidream/hidream-o1)

## Details

| | |
|---|---|
| Name | `image_hidream_o1_dev` |
| Category | Foundation › Image |
| Media type | image |
| Models | HiDream |
| Tags | Image Edit, Text to Image |
| Type | open source |
| Date | 2026-05-14 |
| Author | ComfyUI |
| Download size | 15.9 GB |
| Min ComfyUI version | 0.21.1 |
| Usage | 24 |
| Nodes | 40 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #213 | image | noir_portrait.png |
| output | `SaveImage` #227 | image | image_hidream_o1_dev.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `hidream_o1_image_dev_fp8_scaled.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/HiDream-O1-Image/resolve/main/checkpoints/hidream_o1_image_dev_fp8_scaled.safetensors) |
| `gemma4_e4b_it_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/gemma-4/resolve/main/text_encoders/gemma4_e4b_it_fp8_scaled.safetensors) |

## Subgraphs

- **Prompt Enhancement** (12 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewAny` | 5 | comfy-core |
| `ComfySwitchNode` | 4 | comfy-core |
| `MarkdownNote` | 3 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `ComfyMathExpression` | 2 | comfy-core |
| `EmptyHiDreamO1LatentImage` | 2 | comfy-core |
| `PrimitiveBoolean` | 2 | comfy-core |
| `PrimitiveStringMultiline` | 2 | comfy-core |
| `RegexReplace` | 2 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `HiDreamO1ReferenceImages` | 1 | comfy-core |
| `ImageScaleToTotalPixels` | 1 | comfy-core |
| `JsonExtractString` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `ModelNoiseScale` | 1 | comfy-core |
| `SamplerCustom` | 1 | comfy-core |
| `SamplerLCM` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `StringConcatenate` | 1 | comfy-core |
| `StringReplace` | 1 | comfy-core |
| `TextGenerate` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: About Image Size</summary>

Select and Ctrl-B to enable the  `ImageScaleToTotalPixels` node, if your input image is too large

The O1 model is trained under the following resolutions:
| Width | Height | Category   |
|-------|--------|------------|
| 2048  | 2048   | Square     |
| 2304  | 1728   | Landscape  |
| 2304  | 1792   | Landscape  |
| 2496  | 1664   | Landscape  |
| 2560  | 1440   | Landscape  |
| 3104  | 1312   | Landscape  |
| 1728  | 2304   | Portrait   |
| 1792  | 2304   | Portrait   |
| 1664  | 2496   | Portrait   |
| 1440  | 2560   | Portrait   |
| 1312  | 3104   | Portrait   |

</details>

<details><summary>MarkdownNote</summary>

Related PR: [#13817](https://github.com/Comfy-Org/ComfyUI/pull/13817)

## Model Links

- [Hugging Face:Comfy-Org/HiDream-O1-Image](https://huggingface.co/Comfy-Org/HiDream-O1-Image)
- [ModelScope:Comfy-Org/HiDream-O1-Image](https://modelscope.cn/models/Comfy-Org/HiDream-O1-Image)
- [Hugging Face:Comfy-Org/gemma-4](https://huggingface.co/Comfy-Org/gemma-4)
- [ModelScope:Comfy-Org/gemma-4](https://modelscope.cn/models/Comfy-Org/gemma-4)

**checkpoints**

- [hidream_o1_image_dev_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/HiDream-O1-Image/resolve/main/checkpoints/hidream_o1_image_dev_fp8_scaled.safetensors) (7.51 GB)

**text_encoders**

- [gemma4_e4b_it_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/gemma-4/resolve/main/text_encoders/gemma4_e4b_it_fp8_scaled.safetensors) (8.44 GB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │   └── hidream_o1_image_dev_fp8_scaled.safetensors
│   └── 📂 text_encoders/
│       └── gemma4_e4b_it_fp8_scaled.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: Reference Images</summary>

The HiDream O1 supports up to 10 reference images. You can add more Load Image nodes, then link them to the HiDream-O1 Reference Images node.

</details>
