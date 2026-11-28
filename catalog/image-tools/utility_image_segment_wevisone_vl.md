# Image Segmentation: WeVisOne-VL

[← Image Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=utility_image_segment_wevisone_vl)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_image_segment_wevisone_vl-1.webp" width="360" alt="Image Segmentation: WeVisOne-VL utility_image_segment_wevisone_vl-1.webp">

> Segment whatever a text query names in an image with WeVisOne-VL: hand it a short phrase such as human and it returns per-instance alpha mattes, boxes and points, previews the matte over the picture and gives you foreground and background cutouts. Drop the matte into a background-removal, masking or compositing chain.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/utility_image_segment_wevisone_vl.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/utility_image_segment_wevisone_vl.json)

## Details

| | |
|---|---|
| Name | `utility_image_segment_wevisone_vl` |
| Category | Foundation › Image Tools |
| Output | image |
| Models | WeVisOne-VL |
| Tags | Element Segmentation, Remove Background |
| Type | open source |
| Date | 2026-11-14 |
| Author | ComfyUI |
| Download size | 2.7 GB |
| Min ComfyUI version | 0.45.0 |
| Usage | 158 |
| Nodes | 13 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #10 | image | utility_image_segment_wevisone_vl_input.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `wevisone_vl_2b_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/WeVisOne-VL/resolve/main/text_encoders/wevisone_vl_2b_int8_convrot.safetensors) |

## Subgraphs

- **WeVisOne-VL Segment** (5 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PreviewImage` | 3 |  |
| `JoinImageWithAlpha` | 2 |  |
| `MarkdownNote` | 2 |  |
| `CLIPLoader` | 1 |  |
| `DrawBBoxes` | 1 |  |
| `InvertMask` | 1 |  |
| `LoadImage` | 1 |  |
| `MaskPreview` | 1 |  |
| `WeVisOneDetect` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)


## How to use

**Load Image** → **WeVisOne-VL Segment** (subgraph) → previews. One pass returns alpha mattes, boxes, points and the raw answer; the graph previews the matte, the boxes drawn over the source, and the foreground and background cutouts on transparency, so the matte drops straight into a background-removal, masking or compositing chain.

- `query` — the graph ships `segmentation` with `human`. Put whatever you want cut out in there as a short noun phrase; a full sentence makes `segmentation` ramble.
- `task` — ten tasks, listed with what each returns in the model note next to this one.
- `individual_masks` — one matte per instance instead of the union of them.
- The `MASK` output wires straight into mask nodes (`Invert Mask`, `Grow Mask`, `Join Image with Alpha`, …), so the matte can drive any matting or compositing branch.

## About this model

WeVisOne-VL is a compact vision-language model that answers in shapes instead of prose: it locates what a text query names and returns boxes, points or per-instance alpha mattes in one pass. Native in ComfyUI since #17632.

## Tasks

`task` rewrites your query into the instruction the checkpoint was trained on:

- `segmentation` — alpha matte per instance plus its box (this graph).
- `detection` — boxes only, one label per line in the query.
- `referring` — boxes for a describing phrase ("the cup on the left"), not just a category.
- `point` — centre points as JSON instead of boxes.
- `count_box` — counts the instances and boxes each one.
- `count_point` — counts them and marks each with a point.
- `ocr` — boxes every word in the picture.
- `ocr_grounding` — finds the one string you put in the query and boxes it.
- `visual_prompt` — takes reference boxes on the optional `bboxes` input and finds similar objects; wire a Bounding Box source in first.
- `freeform` — sends the query as the whole prompt, for anything else this model can answer.

`individual_masks` splits the mattes per instance instead of one union per image; `max_length` caps the answer length.

</details>

<details><summary>Note: Models & tasks</summary>

## Input Assets

- [utility_image_segment_wevisone_vl_input.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/utility_image_segment_wevisone_vl_input.png)

## Models

- [Hugging Face:Comfy-Org/WeVisOne-VL](https://huggingface.co/Comfy-Org/WeVisOne-VL)

**ModelScope mirrors** (alternative repo location)

- [ModelScope:Comfy-Org/WeVisOne-VL](https://modelscope.cn/models/Comfy-Org/WeVisOne-VL)

**text_encoders**

- [wevisone_vl_2b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/WeVisOne-VL/resolve/main/text_encoders/wevisone_vl_2b_int8_convrot.safetensors) (2.69 GB) — loaded by this graph
- [wevisone_vl_2b_bf16.safetensors](https://huggingface.co/Comfy-Org/WeVisOne-VL/resolve/main/text_encoders/wevisone_vl_2b_bf16.safetensors) (4.58 GB)
- [wevisone_vl_4b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/WeVisOne-VL/resolve/main/text_encoders/wevisone_vl_4b_int8_convrot.safetensors) (4.93 GB)
- [wevisone_vl_4b_bf16.safetensors](https://huggingface.co/Comfy-Org/WeVisOne-VL/resolve/main/text_encoders/wevisone_vl_4b_bf16.safetensors) (9.03 GB)

Swap weights with `clip_name` in `CLIPLoader` (`stable_diffusion` type): the 4B pair is heavier and slower, the int8 files fit smaller GPUs.

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   └── 📂 text_encoders/
│       └── wevisone_vl_2b_int8_convrot.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
