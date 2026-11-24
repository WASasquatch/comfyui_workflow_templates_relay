# ChronoEdit 14B: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_chrono_edit_14B)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_chrono_edit_14B-1.webp" width="360" alt="ChronoEdit 14B: Image Edit image_chrono_edit_14B-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_chrono_edit_14B-2.webp" width="360" alt="ChronoEdit 14B: Image Edit image_chrono_edit_14B-2.webp">

> Image editing powered by video models' dynamic understanding, creating physically plausible results while preserving character and style consistency.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_chrono_edit_14B.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_chrono_edit_14B.json)

## Details

| | |
|---|---|
| Name | `image_chrono_edit_14B` |
| Category | Foundation › Image |
| Output | image |
| Models | Wan2.1, ChronoEdit, Nvidia |
| Tags | Image Edit |
| Type | open source |
| Date | 2025-11-03 |
| Author | ComfyUI |
| Download size | 38.6 GB |
| Min ComfyUI version | 0.4.0 |
| Usage | 28 |
| Nodes | 25 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #52 | image | image_chrono_edit_input_image.png |
| output | `SaveImage` #60 | image | image_chrono_edit_14B.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `clip_vision_h.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) |
| `chrono_edit_14B_fp16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/chrono_edit_14B_fp16.safetensors) |
| `chronoedit_distill_lora.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/chronoedit_distill_lora.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Subgraphs

- **Chrono Image Edit** (22 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 |  |
| `CLIPTextEncode` | 2 | comfy-core |
| `PrimitiveFloat` | 2 |  |
| `PrimitiveInt` | 2 |  |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPVisionEncode` | 1 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `ImageFromBatch` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `ModelSamplingSD3` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 |  |
| `SaveImage` | 1 | comfy-core |
| `ScaleROPE` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `WanImageToVideo` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>For Local User</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [Hugging Face:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [ModelScope:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)

**text_encoders**

- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) (6.27 GB)

**clip_vision**

- [clip_vision_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) (1.18 GB)

**loras**

- [chronoedit_distill_lora.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/chronoedit_distill_lora.safetensors) (358.5 MB)

**diffusion_models**

- [chrono_edit_14B_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/chrono_edit_14B_fp16.safetensors) (30.54 GB)

**vae**

- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) (242.1 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── umt5_xxl_fp8_e4m3fn_scaled.safetensors
│   ├── 📂 clip_vision/
│   │      └── clip_vision_h.safetensors
│   ├── 📂 loras/
│   │      └── chronoedit_distill_lora.safetensors
│   ├── 📂 diffusion_models/
│   │      └── chrono_edit_14B_fp16.safetensors
│   └── 📂 vae/
│          └── wan_2.1_vae.safetensors
```
## About ChronoEdit

ChronoEdit-14B is finetuned from the pretrain model of Wan2.1-I2V-14B 720P

[ChronoEdit](https://research.nvidia.com/labs/toronto-ai/chronoedit/), a framework developed by teams from NVIDIA and the University of Toronto, reframes image editing as a two-frame video generation task. It leverages the temporal priors of pretrained video generative models and incorporates a temporal reasoning mechanism to achieve editing results with both visual fidelity and physical consistency. Additionally, it comes with the PBench-Edit benchmark for evaluating physical consistency, making it suitable for scenarios like world simulation that require strict adherence to physical laws.

## Report issue

- Cannot run / runtime errors: https://github.com/Comfy-Org/ComfyUI/issues
- UI / frontend issues: https://github.com/Comfy-Org/ComfyUI_frontend/issues
- Workflow mistakes, wrong params, can't download the models: https://github.com/Comfy-Org/workflow_templates/issues

</details>
