# Mage-Flow: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_mage_flow_t2i_int8)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_mage_flow_t2i_int8-1.webp" width="360" alt="Mage-Flow: Text to Image image_mage_flow_t2i_int8-1.webp">

> Generate high-resolution images from text prompts using Mage-Flow, a compact 4B-parameter diffusion model that outputs a single image at native resolutions from 512 to 2048 pixels per side. Ideal for rapid concept visualization, creative asset generation, and research in controlled image synthesis under limited compute budgets.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_mage_flow_t2i_int8.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_mage_flow_t2i_int8.json)

## Details

| | |
|---|---|
| Name | `image_mage_flow_t2i_int8` |
| Category | Foundation › Image |
| Output | image |
| Models | Mage-Flow |
| Tags | Text to Image, Int8 |
| Type | open source |
| Date | 2026-07-28 |
| Author | ComfyUI |
| Download size | 12.5 GB |
| Min ComfyUI version | 0.29.0 |
| Usage | 33 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImageAdvanced` #10 | image | Mage_flow.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `mage_flow_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/diffusion_models/mage_flow_int8_convrot.safetensors) |
| `qwen3vl_4b_bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/text_encoders/qwen3vl_4b_bf16.safetensors) |
| `mage_flow_vae_bf16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/vae/mage_flow_vae_bf16.safetensors) |

## Subgraphs

- **Text to Image (Mage-Flow)** (6 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `CLIPLoader` | 1 |  |
| `KSampler` | 1 |  |
| `ResolutionSelector` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
| `TextEncodeMageFlowEdit` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Mage-Flow</summary>

# Mage-Flow (Text-to-Image)

- **Mage project:** https://github.com/microsoft/Mage
- **ComfyUI integration PR:** https://github.com/Comfy-Org/ComfyUI/pull/15026

## Resolution limits

| Item | Value |
|------|-------|
| Output range | **512 – 2048** px per side (native-resolution training range) |
| Alignment | Width & height must be a **multiple of 16** (VAE downsamples 16×) |
| Aspect ratio | Any; extreme **4:1** supported (e.g. `2048×512`, `512×2048`) |

**Recommendations:** use **1024** longest side for everyday tests; **1536–2048** for higher quality. Avoid exceeding **2048**.

## Model variants

| Variant | Steps | CFG | Notes |
|---------|-------|-----|-------|
| Base | 30 | 5.0 | Stable baseline |
| RL | 20 | 5.0 | Better prompt following & aesthetics |
| Turbo | **4** | **1.0** | Fastest (~0.6 s/image at 1024² on A100) |

Swap the diffusion model checkpoint in the subgraph to match your variant. Turbo **must** use 4 steps and CFG 1.0.

## Workflow parameters

| Parameter | Description |
|-----------|-------------|
| `prompt` | Text description of the image (English recommended for best results) |
| `negative_prompt` | Optional; what to avoid (blur, artifacts, etc.) |
| `seed` | Fixed seed for reproducibility; randomize to explore |
| `width` / `height` | Output size via **ResolutionSelector**; step 16 |
| `unet_name` | Diffusion model (e.g. `mage_flow_int8_convrot` or `mage_flow_bf16`) |
| `clip_name` | `qwen3vl_4b_bf16.safetensors` (type: mage) |
| `vae_name` | `mage_flow_vae_bf16.safetensors` |

Default sampler in subgraph: **30 steps**, **CFG 5.0**, euler / simple.

</details>

<details><summary>Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Mage-Flow](https://huggingface.co/Comfy-Org/Mage-Flow)

### Alternative Repos

- [ModelScope:Comfy-Org/Mage-Flow](https://modelscope.cn/models/Comfy-Org/Mage-Flow)

**diffusion_models** (text-to-image — pick one)

- [mage_flow_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/diffusion_models/mage_flow_int8_convrot.safetensors) (3.87 GB) (INT8, lower VRAM)
- [mage_flow_bf16.safetensors](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/diffusion_models/mage_flow_bf16.safetensors) (7.67 GB) (BF16, higher quality)

**text_encoders**

- [qwen3vl_4b_bf16.safetensors](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/text_encoders/qwen3vl_4b_bf16.safetensors) (8.27 GB)

**vae**

- [mage_flow_vae_bf16.safetensors](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/vae/mage_flow_vae_bf16.safetensors) (329.1 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   ├── mage_flow_int8_convrot.safetensors
│   │   └── mage_flow_bf16.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen3vl_4b_bf16.safetensors
│   └── 📂 vae/
│       └── mage_flow_vae_bf16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
