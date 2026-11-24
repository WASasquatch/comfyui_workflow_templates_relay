# Prompt Multi Batch Generation

[← Node Basics](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates_purz_batch_generation)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_purz_batch_generation-1.webp" width="360" alt="Prompt Multi Batch Generation templates_purz_batch_generation-1.webp">

> Send multiple prompts simultaneously to generate independent outputs in a single queue. Connect to Blueprint or Partner Nodes for batch processing of any modality. Use for prompt variation comparisons and batch generation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates_purz_batch_generation.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates_purz_batch_generation.json)

## Details

| | |
|---|---|
| Name | `templates_purz_batch_generation` |
| Category | Foundation › Node Basics |
| Output | image |
| Models | Z-Image-Turbo |
| Tags | Batch Generation, Image |
| Type | open source |
| Date | 2026-03-21 |
| Author | ComfyUI |
| Download size | 19.3 GB |
| Min ComfyUI version | 0.11.0 |
| Usage | 20 |
| Nodes | 13 |

## Custom nodes required

- [comfyui_fill-nodes](https://registry.comfy.org/nodes/comfyui_fill-nodes)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `z_image_turbo_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) |
| `qwen_3_4b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Text to Image (Z-Image-Turbo)** (9 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `FL_PromptMulti` | 1 |  |
| `KSampler` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `SaveImage` | 1 |  |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# ⚡ FL Prompt Multi

Sends multiple prompts **at the same time** — each slot runs independently and 
generates its own output in a single queue entry.

---

## ⚠️ Each prompt slot = one run

Fill 6 slots, spend 6 runs. This adds up fast — especially with Partner Nodes 
where every run costs credits.

- Test with 2 slots before filling them all
- Blank or unused slots may still trigger a run
- Keep an eye on the queue panel so you can interrupt early

---

## Setup

1. Write each prompt on its own line — one prompt per line
2. Connect the output to a Blueprint or Partner Node to run generations of any modality
3. Queue — all prompts fire together

---

## Use this node for

✅ Prompt variation comparisons  
✅ Batch image generation  
❌ Single outputs — just use a regular prompt node  
❌ Active iteration/testing — you'll burn credits fast

---

_💡 Every line = one press of Queue. Fill with intention._

</details>

<details><summary>Model link</summary>

## Report workflow issue

If you found any issues when running this workflow, [report template issue here](https://github.com/Comfy-Org/workflow_templates/issues)

## Model Links

- [Hugging Face:Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo)

### Alternative Repos

- [ModelScope:Comfy-Org/z_image_turbo](https://modelscope.cn/models/Comfy-Org/z_image_turbo)

**text_encoders**

- [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) (7.49 GB)

**loras**

- [pixel_art_style_z_image_turbo.safetensors](https://huggingface.co/tarn59/pixel_art_style_lora_z_image_turbo/resolve/main/pixel_art_style_z_image_turbo.safetensors) (162.2 MB)

**diffusion_models**

- [z_image_turbo_bf16.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) (11.46 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── qwen_3_4b.safetensors
│   ├── 📂 loras/
│   │      └── pixel_art_style_z_image_turbo.safetensors
│   ├── 📂 diffusion_models/
│   │      └── z_image_turbo_bf16.safetensors
│   └── 📂 vae/
│          └── ae.safetensors
```

</details>
