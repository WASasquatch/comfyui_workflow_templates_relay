# Video Segmentation: SAM3

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_video_segment_sam3-1.webp" width="360" alt="Video Segmentation: SAM3 utility_video_segment_sam3-1.webp">

> Use the SAM3 model to segment the main subject or content from a video, isolating specific objects or regions. Input a video and receive a segmented mask output.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_video_segment_sam3.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_video_segment_sam3.json)
- [Tutorial](https://docs.comfy.org/tutorials/utility/video-segment-sam3)

## Details

| | |
|---|---|
| Name | `utility_video_segment_sam3` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | SAM3 |
| Tags | Element Segmentation |
| Type | open source |
| Date | 2026-04-27 |
| Author | ComfyUI |
| Download size | 1.6 GB |
| Min ComfyUI version | 0.20.0 |
| Usage | 105 |
| Nodes | 9 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #115 | video | drinking_unicorn.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sam3.1_multiplex_fp16.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors) |

## Subgraphs

- **Video Segment (SAM3)** (5 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `MaskPreview` | 1 | comfy-core |
| `Note` | 1 |  |
| `SAM3_Detect` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

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

<details><summary>Note: Prompt format</summary>

```text
Max tokens for this model is only 32, to separately prompt multiple subjects you can separate prompts with comma, and set the max amount of objects detected for each prompt with :N

For example above test prompt finds 2 cakes, one apron, 4 window panels
```

</details>
