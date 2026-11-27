# Image Segmentation: SAM3

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_image_segment_sam3)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_image_segment_sam3-1.webp" width="360" alt="Image Segmentation: SAM3 utility_image_segment_sam3-1.webp">

> Use the SAM3 model to segment the main subject or content from a photo or image, isolating specific objects or regions. Input an image and receive a segmented mask output.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_image_segment_sam3.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_image_segment_sam3.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/video-segment-sam3)

## Details

| | |
|---|---|
| Name | `utility_image_segment_sam3` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | SAM3 |
| Tags | Element Segmentation |
| Type | open source |
| Date | 2026-04-26 |
| Author | ComfyUI |
| Download size | 1.6 GB |
| Min ComfyUI version | 0.20.0 |
| Usage | 69 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #79 | image | neon_guitarist.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sam3.1_multiplex_fp16.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors) |

## Subgraphs

- **Image Segment (SAM3)** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `InvertMask` | 1 | comfy-core |
| `JoinImageWithAlpha` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MaskPreview` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `SAM3_Detect` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Input Asset

- [neon_guitarist.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/neon_guitarist.png)

## Model Links

- [Hugging Face:Comfy-Org/sam3.1](https://huggingface.co/Comfy-Org/sam3.1)

### Alternative Repos

- [ModelScope:Comfy-Org/sam3.1](https://modelscope.cn/models/Comfy-Org/sam3.1)

**checkpoints**

- [sam3.1_multiplex_fp16.safetensors](https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors) (1.63 GB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 checkpoints/
│       └── sam3.1_multiplex_fp16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: Prompt format</summary>

Max tokens for this model is only 32, to separately prompt multiple subjects you can separate prompts with comma, and set the max amount of objects detected for each prompt with :N

For example above test prompt finds 2 cakes, one apron, 4 window panels

```
eye:2, window panels:4
```

</details>
