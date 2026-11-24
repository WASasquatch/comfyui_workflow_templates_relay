# MOSS-Image: Color & Depth Control

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_moss_image_color_depth_control)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_moss_image_color_depth_control-1.webp" width="360" alt="MOSS-Image: Color & Depth Control image_moss_image_color_depth_control-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_moss_image_color_depth_control-2.webp" width="360" alt="MOSS-Image: Color & Depth Control image_moss_image_color_depth_control-2.webp">

> Re-pose and re-style a reference photo with MOSS-Image: the graph estimates the reference's geometry with MoGe 3, then generates a new image that keeps the pose, framing and silhouette while the prompt decides the character, wardrobe, setting and light. A color/depth control adapter LoRA makes the model follow the estimated map, and the color map socket is there for region-painted layouts.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_moss_image_color_depth_control.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_moss_image_color_depth_control.json)

## Details

| | |
|---|---|
| Name | `image_moss_image_color_depth_control` |
| Category | Foundation › Image |
| Output | image |
| Models | MOSS-Image |
| Tags | Depth, Image |
| Type | open source |
| Date | 2026-10-26 |
| Author | ComfyUI |
| Download size | 17.0 GB |
| Min ComfyUI version | 0.43.0 |
| Usage | 125 |
| Nodes | 27 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #55 | image | fashion_portrait_red_canyon.png |
| output | `SaveImage` #85 | image | image_moss_image_color_depth_control.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `moss_image_sft_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/diffusion_models/moss_image_sft_int8_convrot.safetensors) |
| `moge_3_vitg_fp16.safetensors` | `geometry_estimation` | [link](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_3_vitg_fp16.safetensors) |
| `moss_image_color_depth_control.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/loras/moss_image_color_depth_control.safetensors) |
| `qwen3.5_9b_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/text_encoders/qwen3.5_9b_int8_convrot.safetensors) |
| `flux2-vae_small.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/vae/flux2-vae_small.safetensors) |

## Subgraphs

- **Geometry Estimation (MoGe 3)** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 |  |
| `MarkdownNote` | 2 |  |
| `BasicScheduler` | 1 |  |
| `CLIPLoader` | 1 |  |
| `EmptyLatentImage` | 1 |  |
| `GetImageSize` | 1 |  |
| `ImageCompare` | 1 |  |
| `ImageScaleToTotalPixels` | 1 |  |
| `LoadImage` | 1 |  |
| `LoadMoGeModel` | 1 |  |
| `LoraLoaderModelOnly` | 1 |  |
| `ModelSamplingAuraFlow` | 1 |  |
| `MoGeInference` | 1 |  |
| `MoGeRender` | 1 |  |
| `MOSSImageControl` | 1 |  |
| `Painter` | 1 |  |
| `PreviewImage` | 1 |  |
| `SamplerCustom` | 1 |  |
| `SamplerER_SDE` | 1 |  |
| `SaveImage` | 1 |  |
| `SkipLayerGuidanceDiTSimple` | 1 |  |
| `TemporalScoreRescaling` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: About</summary>

## MOSS-Image: Color & Depth Control from a Photo

**Input Assets**
- [fashion_portrait_red_canyon.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/fashion_portrait_red_canyon.png) — required workflow input (`input/fashion_portrait_red_canyon.png`)

Drop in a photo and the graph estimates its geometry, then generates a new image that keeps the same pose and framing. No map to prepare by hand.

**How it works**

1. **Load Image** (node 55) - the character reference. It is scaled to 1.0 MP, 16 px aligned (node 77), and drives the output size through **Get Image Size** (node 61) -> **Empty Latent** (node 54).
2. **Geometry Estimation (MoGe 3)** subgraph - `Load MoGe Model` (`moge_3_vitg_fp16`) -> `Run MoGe Inference` -> `Render MoGe Geometry`. Its output is the `depth_map` of **MOSS-Image Color/Depth Control** (node 53).
3. **Positive Prompt** (node 5) describes the character and the scene. Geometry comes from the render, everything else - identity, wardrobe, material, light, style - comes from the text.
4. **MOSS-Image Color/Depth Control** (node 53) injects the map into the image tokens; the LoRA loaded just before it (`moss_image_color_depth_control.safetensors`, strength 1.0) is what makes the model read it. Without the LoRA the node is a no-op.
5. **Save / Compare**: `VAE Decode` -> preview, plus **Compare Images** (node 80) holding the generated frame next to the rendered map.

**Settings**

`strength` 1.0 is the trained strength; `start_percent` / `end_percent` pick the part of the run that is controlled (0 to 0.6 here: the layout is fixed, the last steps render freely). Sampling follows the MOSS-Image control test graph: 25 steps, CFG 3, `er_sde` / `simple`, shift 5, skip layer guidance on layer 24, temporal score rescaling 0.95.

**Useful knobs**

- `Render MoGe Geometry` in the subgraph is set to `mask`: only the silhouette is used. Switch it to `depth` (`normalization = min_max`) when you want the face profile, shoulders and background falloff to be controlled too - the pose gets tighter, the prompt has less room.
- `end_percent` 1.0 pins geometry to the last step; 0.5 frees the surface and lighting. For a mask-derived map 0.6 is a good middle.
- The reference has **pointed elf ears**, and the geometry keeps them. Either keep that in the prompt (`pointed elf ears`) or hide them (`ears covered by hair`).
- **Painter** (node 81) is in the graph for painting a map by hand: white near / black far for depth, one flat colour per region for colour. Connect its `IMAGE` to `depth_map` or `color_map` to override the estimate.
- `color_map` is optional and currently unconnected. One flat colour per region, colours only act as region IDs, black means "unspecified"; it must match the output size (1024 x 1024 here).

</details>

<details><summary>Note: Model Links</summary>

## Model Links

- [Hugging Face:Comfy-Org/MOSS-Image](https://huggingface.co/Comfy-Org/MOSS-Image)
- [Hugging Face:Comfy-Org/MoGe](https://huggingface.co/Comfy-Org/MoGe) (geometry estimation)
- Upstream control adapter: darask0/MOSS-Image-color-depth-control (Hugging Face repo is gated — sign in to view)

**ModelScope mirrors** (alternative repo location)

- [ModelScope:Comfy-Org/MOSS-Image](https://modelscope.cn/models/Comfy-Org/MOSS-Image)
- [ModelScope:Comfy-Org/MoGe](https://modelscope.cn/models/Comfy-Org/MoGe)

**diffusion_models**

- [moss_image_sft_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/diffusion_models/moss_image_sft_int8_convrot.safetensors) - 5.41 GB, the checkpoint this graph loads
- [moss_image_sft_bf16.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/diffusion_models/moss_image_sft_bf16.safetensors) - 10.16 GB, higher precision, slower
- [moss_image_base_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/diffusion_models/moss_image_base_int8_convrot.safetensors) - 5.41 GB, the base checkpoint runs in the same graph

**text_encoders**

- [qwen3.5_9b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/text_encoders/qwen3.5_9b_int8_convrot.safetensors) - 9.75 GB, the encoder this graph loads
- [qwen3.5_9b_w4a8_gptq.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors) - 7.34 GB, drop-in swap, saves 2.4 GB
- [qwen3.5_9b_bf16.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/text_encoders/qwen3.5_9b_bf16.safetensors) - 19.31 GB, full precision

**vae**

- [flux2-vae_small.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/vae/flux2-vae_small.safetensors) - 249 MB, the one this graph loads
- [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/vae/flux2-vae.safetensors) - 336 MB, full size, pixel-level differences only

**loras**

- [moss_image_color_depth_control.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/loras/moss_image_color_depth_control.safetensors) - 313 MB, `LoraLoaderModelOnly` at strength 1.0

**geometry_estimation**

- [moge_3_vitg_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_3_vitg_fp16.safetensors) - 2.50 GB, the depth estimator used by the subgraph
- [moge_3_vitl_fp16.safetensors](https://huggingface.co/Comfy-Org/MoGe/resolve/main/geometry_estimation/moge_3_vitl_fp16.safetensors) - 741 MB, the lighter ViT-L variant

**Disk footprint**: the graph as shipped needs **18.23 GB** (18,226,010,396 bytes) (5.41 + 9.75 + 0.25 + 0.31 + 2.50). Swapping the text encoder to `w4a8_gptq` brings it to **15.82 GB**; a bf16 checkpoint and encoder instead push it past 32 GB.

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── moss_image_sft_int8_convrot.safetensors     5.41 GB
│   ├── 📂 text_encoders/
│   │   └── qwen3.5_9b_int8_convrot.safetensors         9.75 GB
│   ├── 📂 vae/
│   │   └── flux2-vae_small.safetensors                 249 MB
│   ├── 📂 loras/
│   │   └── moss_image_color_depth_control.safetensors  313 MB
│   └── 📂 geometry_estimation/
│       └── moge_3_vitg_fp16.safetensors                2.50 GB
```

Core support (`MOSSImageControl`, MoGe nodes) ships from ComfyUI **0.43.0**.

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
