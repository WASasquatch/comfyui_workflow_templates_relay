# Flux.1 Depth Lora

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=flux_depth_lora_example)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_depth_lora_example-1.webp" width="360" alt="Flux.1 Depth Lora flux_depth_lora_example-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_depth_lora_example-2.webp" width="360" alt="Flux.1 Depth Lora flux_depth_lora_example-2.webp">

> Generate images guided by depth information using Flux.1 LoRA.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_depth_lora_example.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/flux_depth_lora_example.json)
- [Tutorial](https://docs.comfy.org/tutorials/flux/flux-1-controlnet)

## Details

| | |
|---|---|
| Name | `flux_depth_lora_example` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX, FLUX.1 |
| Tags | ControlNet, Image |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 33.0 GB |
| Min ComfyUI version | 0.3.42 |
| Usage | 20 |
| Nodes | 28 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #17 | image | flux_depth_lora_example_input_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux1-dev-fp8.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors) |
| `lotus-depth-d-v1-1.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/lotus/resolve/main/lotus-depth-d-v1-1.safetensors) |
| `flux1-depth-dev-lora.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/split_files/loras/flux1-depth-dev-lora.safetensors) |
| `clip_l.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true) |
| `t5xxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) |
| `vae-ft-mse-840000-ema-pruned.safetensors` | `vae` | [link](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors) |

## Subgraphs

- **Lotus Depth(Subgraph)** (12 nodes)
- **Depth to Image(Flux.1 Dev)** (13 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `UNETLoader` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `BasicGuider` | 1 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `DisableNoise` | 1 | comfy-core |
| `DualCLIPLoader` | 1 | comfy-core |
| `FluxGuidance` | 1 | comfy-core |
| `ImageInvert` | 1 | comfy-core |
| `ImageScaleToTotalPixels` | 1 | comfy-core |
| `InstructPixToPixConditioning` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `LotusConditioning` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `SetFirstSigma` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Lotus Depth model links</summary>

## Model Links

- [Hugging Face:Comfy-Org/lotus](https://huggingface.co/Comfy-Org/lotus)

### Alternative Repos

- [ModelScope:Comfy-Org/lotus](https://modelscope.cn/models/Comfy-Org/lotus)

**Diffusion Model**

Download [lotus-depth-d-v1-1.safetensors](https://huggingface.co/Comfy-Org/lotus/resolve/main/lotus-depth-d-v1-1.safetensors) (1.62 GB) 
 and place it in **ComfyUI/models/diffusion_models**

**VAE Model**

Download  [vae-ft-mse-840000-ema-pruned.safetensors](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors) (319.1 MB)  and place it in **ComfyUI/models/vae** or you can use any SD1.5 VAE if you prefer.

```
ComfyUI/
├── models/
│   ├── diffusion_models/
│   │   └─── lotus-depth-d-v1-1.safetensors
│   └── vae/
│       └──  lvae-ft-mse-840000-ema-pruned.safetensors
```

</details>

<details><summary>Note: Model links</summary>

[Tutorial](https://docs.comfy.org/tutorials/flux/flux-1-controlnet)

## Model Links

- [Hugging Face:Comfy-Org/flux1-dev](https://huggingface.co/Comfy-Org/flux1-dev)
- [Hugging Face:Comfy-Org/Lumina_Image_2.0_Repackaged](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/flux1-dev](https://modelscope.cn/models/Comfy-Org/flux1-dev)
- [ModelScope:Comfy-Org/Lumina_Image_2.0_Repackaged](https://modelscope.cn/models/Comfy-Org/Lumina_Image_2.0_Repackaged)

**text_encoders**

- [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors?download=true) (9.12 GB)
- [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors?download=true) (234.7 MB)

**loras**

- [flux1-depth-dev-lora.safetensors](https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/split_files/loras/flux1-depth-dev-lora.safetensors) (1.16 GB)

**diffusion_models**

- [flux1-dev-fp8.safetensors](https://huggingface.co/Comfy-Org/flux1-dev/resolve/main/flux1-dev-fp8.safetensors) (16.06 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      ├── t5xxl_fp16.safetensors
│   │      └── clip_l.safetensors
│   ├── 📂 loras/
│   │      └── flux1-depth-dev-lora.safetensors
│   ├── 📂 diffusion_models/
│   │      └── flux1-dev-fp8.safetensors
│   └── 📂 vae/
│          └── ae.safetensors
```

</details>
