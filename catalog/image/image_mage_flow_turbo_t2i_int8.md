# Mage-Flow Turbo: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_mage_flow_turbo_t2i_int8)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_mage_flow_turbo_t2i_int8-1.webp" width="360" alt="Mage-Flow Turbo: Text to Image image_mage_flow_turbo_t2i_int8-1.webp">

> Generate high-quality images from text prompts using the compact 4B-parameter Mage-Flow Turbo model, producing a single image output without any file inputs. This workflow supports native-resolution generation from 512 to 2048 pixels per side at any aspect ratio, including extreme 4:1 dimensions. Ideal for rapid concept visualization, creative asset generation, and low-latency image prototyping on modest hardware.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_mage_flow_turbo_t2i_int8.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_mage_flow_turbo_t2i_int8.json)

## Details

| | |
|---|---|
| Name | `image_mage_flow_turbo_t2i_int8` |
| Category | Foundation › Image |
| Output | image |
| Models | Mage-Flow |
| Tags | Text to Image, Int8, Turbo |
| Type | open source |
| Date | 2026-07-28 |
| Author | ComfyUI |
| Download size | 12.5 GB |
| Min ComfyUI version | 0.29.0 |
| Usage | 23 |
| Nodes | 10 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| output | `SaveImageAdvanced` #10 | image | Mage_flow_turbo.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `mage_flow_turbo_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/diffusion_models/mage_flow_turbo_int8_convrot.safetensors) |
| `qwen3vl_4b_bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/text_encoders/qwen3vl_4b_bf16.safetensors) |
| `mage_flow_vae_bf16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/vae/mage_flow_vae_bf16.safetensors) |

## Subgraphs

- **Text to Image (Mage-Flow Turbo)** (6 nodes)

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

<details><summary>Note: Mage-Flow-Turbo</summary>

# Mage-Flow-Turbo (Text-to-Image)

**Mage-Flow-Turbo** is the few-step distilled variant of Microsoft's 4B Mage-Flow text-to-image model. Distilled from the Base/RL checkpoints via decoupled-DMD + adversarial perceptual guidance, Turbo trades a small amount of quality for **~7× fewer denoising steps**.

**Good at:** fast prompt iteration, interactive previews, portraits, landscapes, still life, cinematic scenes, and surreal/editorial compositions.

## Links

- **Mage project:** https://github.com/microsoft/Mage
- **ComfyUI integration PR:** https://github.com/Comfy-Org/ComfyUI/pull/15026
- **Model repo:** https://huggingface.co/Comfy-Org/Mage-Flow

This workflow ships with **4 steps / CFG 1.0** pre-configured in the KSampler.

## Resolution limits

| Item | Value |
|------|-------|
| Output range | **512 – 2048** px per side |
| Alignment | Width & height must be a **multiple of 16** |
| Aspect ratio | Any; extreme **4:1** supported (e.g. `2048×512`) |

**Recommendations:** **1024** for everyday use; **1536–2048** when you need more detail. Avoid exceeding **2048**.

## Workflow parameters

| Parameter | Description |
|-----------|-------------|
| `prompt` | Text description (English recommended) |
| `negative_prompt` | Optional; what to avoid |
| `seed` | Fixed seed or randomize |
| `width` / `height` | Via **ResolutionSelector**; step 16 |
| `unet_name` | `mage_flow_turbo_int8_convrot` (default) or `mage_flow_turbo_bf16` |
| `clip_name` | `qwen3vl_4b_bf16.safetensors` (type: mage) |
| `vae_name` | `mage_flow_vae_bf16.safetensors` (shared with all Mage-Flow variants) |

</details>

<details><summary>Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Mage-Flow](https://huggingface.co/Comfy-Org/Mage-Flow)

### Alternative Repos

- [ModelScope:Comfy-Org/Mage-Flow](https://modelscope.cn/models/Comfy-Org/Mage-Flow)

**diffusion_models** (Mage-Flow-Turbo)

- [mage_flow_turbo_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/diffusion_models/mage_flow_turbo_int8_convrot.safetensors) (3.87 GB) (INT8, default in this workflow)
- [mage_flow_turbo_bf16.safetensors](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/diffusion_models/mage_flow_turbo_bf16.safetensors) (7.67 GB) (BF16, higher quality)

**text_encoders** (shared across all Mage-Flow variants)

- [qwen3vl_4b_bf16.safetensors](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/text_encoders/qwen3vl_4b_bf16.safetensors) (8.27 GB)

**vae** (shared across all Mage-Flow variants)

- [mage_flow_vae_bf16.safetensors](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/vae/mage_flow_vae_bf16.safetensors) (329.1 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   ├── mage_flow_turbo_int8_convrot.safetensors
│   │   └── mage_flow_turbo_bf16.safetensors
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
