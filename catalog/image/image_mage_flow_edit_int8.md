# Mage-Flow-Edit: Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_mage_flow_edit_int8)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_mage_flow_edit_int8-1.webp" width="360" alt="Mage-Flow-Edit: Image Edit image_mage_flow_edit_int8-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_mage_flow_edit_int8-2.webp" width="360" alt="Mage-Flow-Edit: Image Edit image_mage_flow_edit_int8-2.webp">

> Edit images by following natural language instructions with Mage-Flow-Edit, an instruction-based model that handles background replacement, style changes, localized edits, and restoration using up to three reference images. The workflow takes one input image and produces one edited output plus a side-by-side comparison view. Ideal for creative photo retouching, product image styling, and restoring old or damaged photos.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_mage_flow_edit_int8.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_mage_flow_edit_int8.json)

## Details

| | |
|---|---|
| Name | `image_mage_flow_edit_int8` |
| Category | Foundation › Image |
| Output | image |
| Models | Mage-Flow |
| Tags | Image Edit, Int8 |
| Type | open source |
| Date | 2026-07-27 |
| Author | ComfyUI |
| Download size | 12.5 GB |
| Min ComfyUI version | 0.29.0 |
| Usage | 30 |
| Nodes | 19 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #7 | image | calm_amid_ruin.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `mage_flow_edit_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/diffusion_models/mage_flow_edit_int8_convrot.safetensors) |
| `qwen3vl_4b_bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/text_encoders/qwen3vl_4b_bf16.safetensors) |
| `mage_flow_vae_bf16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/vae/mage_flow_vae_bf16.safetensors) |

## Subgraphs

- **Image Edit (Mage-Flow-Edit)** (15 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 |  |
| `MarkdownNote` | 2 |  |
| `PrimitiveBoolean` | 2 |  |
| `PrimitiveInt` | 2 |  |
| `CLIPLoader` | 1 |  |
| `GetImageSize` | 1 |  |
| `ImageScaleToTotalPixels` | 1 |  |
| `KSampler` | 1 |  |
| `LoadImage` | 1 |  |
| `SaveImageAdvanced` | 1 |  |
| `TextEncodeMageFlowEdit` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: Mage-Flow-Edit</summary>

# Mage-Flow-Edit

**Mage-Flow-Edit** is Microsoft's 4B instruction-based image editing model (Mage-VAE + Native-Resolution DiT + Qwen3-VL). It supports background replacement, style/lighting changes, localized content edits, restoration, and multi-reference editing (1–3 refs recommended).

## Links

- **Mage project:** https://github.com/microsoft/Mage
- **ComfyUI integration PR:** https://github.com/Comfy-Org/ComfyUI/pull/15026

## Resolution limits

| Item | Value |
|------|-------|
| Output range | **512 – 2048** px per side (native-resolution training range) |
| Alignment | Width & height must be a **multiple of 16** (VAE downsamples 16×) |
| Aspect ratio | Any; extreme **4:1** supported (e.g. `2048×512`) |
| Reference input | No hard pixel cap; resized to the target output size |
| VL conditioning | Reference long edge capped at **384px** internally |

**Recommendations:** use **1024** longest side for everyday tests; **1536–2048** for higher quality. Avoid exceeding **2048** — quality and stability drop outside the training distribution.

## Workflow parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `prompt` | — | Edit instruction (English recommended). State what to keep, then what to change. |
| `seed` | randomize | Fixed seed for reproducibility |
| `steps` | 30 | Denoising steps (Base/RL: 30; Turbo: 4) |
| `cfg` | 5.0 | Guidance scale (Turbo: 1.0) |
| `resize_input_image` | true | Pre-scale the reference image before editing |
| `target_megapixels` | 1.0 | Target area in megapixels when resizing (~1.0 ≈ 1024×1024) |
| `match_input_size` | true | Output size follows the (resized) reference; if false, use `width` / `height` |
| `width` / `height` | 1024 | Manual output size (only when `match_input_size` = false); step 16 |

### Size logic

1. `resize_input_image = true` → scale input to `target_megapixels` first
2. `match_input_size = true` → output matches processed reference dimensions
3. `match_input_size = false` → output uses manual `width` × `height`

## Models (BF16)

- `mage_flow_edit_bf16.safetensors` — edit DiT
- `qwen3vl_4b_bf16.safetensors` — Qwen3-VL encoder (type: mage)
- `mage_flow_vae_bf16.safetensors` — Mage-VAE

</details>

<details><summary>Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Mage-Flow](https://huggingface.co/Comfy-Org/Mage-Flow)

### Alternative Repos

- [ModelScope:Comfy-Org/Mage-Flow](https://modelscope.cn/models/Comfy-Org/Mage-Flow)

**diffusion_models**

- [mage_flow_edit_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/diffusion_models/mage_flow_edit_int8_convrot.safetensors) (3.87 GB)
- [mage_flow_edit_bf16.safetensors](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/diffusion_models/mage_flow_edit_bf16.safetensors) (7.67 GB) (other model weights)

**text_encoders**

- [qwen3vl_4b_bf16.safetensors](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/text_encoders/qwen3vl_4b_bf16.safetensors) (8.27 GB)

**vae**

- [mage_flow_vae_bf16.safetensors](https://huggingface.co/Comfy-Org/Mage-Flow/resolve/main/vae/mage_flow_vae_bf16.safetensors) (329.1 MB)

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   ├── mage_flow_edit_bf16.safetensors
│   │   └── mage_flow_edit_int8_convrot.safetensors
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
