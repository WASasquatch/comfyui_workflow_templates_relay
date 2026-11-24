# SD3.5 Large Depth

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/sd3.5_large_depth-1.webp" width="360" alt="SD3.5 Large Depth sd3.5_large_depth-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/sd3.5_large_depth-2.webp" width="360" alt="SD3.5 Large Depth sd3.5_large_depth-2.webp">

> Generate images guided by depth information using SD 3.5.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/sd3.5_large_depth.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/sd3.5_large_depth.json)
- [Tutorial](https://comfyanonymous.github.io/ComfyUI_examples/sd3/#sd35-controlnets)

## Details

| | |
|---|---|
| Name | `sd3.5_large_depth` |
| Category | Foundation › Image |
| Media type | image |
| Models | SD3.5, Stability |
| Tags | Image, ControlNet |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 22.0 GB |
| Min ComfyUI version | 0.3.42 |
| Usage | 29 |
| Nodes | 28 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #45 | image | sd3.5_large_depth_input_image.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sd3.5_large_fp8_scaled.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8/resolve/main/sd3.5_large_fp8_scaled.safetensors?download=true) |
| `sd3.5_large_controlnet_depth.safetensors` | `controlnet` | [link](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-controlnets_ComfyUI_repackaged/resolve/main/split_files/controlnet/sd3.5_large_controlnet_depth.safetensors) |
| `lotus-depth-d-v1-1.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/lotus/resolve/main/lotus-depth-d-v1-1.safetensors) |
| `vae-ft-mse-840000-ema-pruned.safetensors` | `vae` | [link](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors) |

## Subgraphs

- **Lotus Depth(Subgraph)** (12 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `VAEDecode` | 2 | comfy-core |
| `VAEEncode` | 2 | comfy-core |
| `BasicGuider` | 1 | comfy-core |
| `BasicScheduler` | 1 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `ControlNetApplyAdvanced` | 1 | comfy-core |
| `ControlNetLoader` | 1 | comfy-core |
| `DisableNoise` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `ImageInvert` | 1 | comfy-core |
| `ImageScaleToTotalPixels` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `KSamplerSelect` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LotusConditioning` | 1 | comfy-core |
| `PreviewImage` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `SetFirstSigma` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note: Image size</summary>

Connect this `LATENT` output to the KSampler, and then the output image will use the size you set in the `EmptySD3LatentImage` node.

</details>

<details><summary>Note: SD3.5 controlnet model links</summary>

## Model Links

- [Hugging Face:Comfy-Org/stable-diffusion-3.5-fp8](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8)
- [ModelScope:Comfy-Org/stable-diffusion-3.5-fp8](https://modelscope.cn/models/Comfy-Org/stable-diffusion-3.5-fp8)
- [Hugging Face:Comfy-Org/stable-diffusion-3.5-controlnets_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-controlnets_ComfyUI_repackaged)
- [ModelScope:Comfy-Org/stable-diffusion-3.5-controlnets_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/stable-diffusion-3.5-controlnets_ComfyUI_repackaged)

**checkpoints**
 - [sd3.5_large_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-fp8/resolve/main/sd3.5_large_fp8_scaled.safetensors) (13.91 GB)

**ControlNet**

- [sd3.5_large_controlnet_depth.safetensors](https://huggingface.co/Comfy-Org/stable-diffusion-3.5-controlnets_ComfyUI_repackaged/resolve/main/split_files/controlnet/sd3.5_large_controlnet_depth.safetensors) (8.06 GB)


```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 checkpoints/
│   │   └── sd3.5_large_fp8_scaled.safetensors
│   ├── 📂 controlnet/ 
│   │   └── sd3.5_large_controlnet_depth.safetensors
```

</details>

<details><summary>Note: Lotus Depth model links</summary>

## Model Links

- [Hugging Face:Comfy-Org/lotus](https://huggingface.co/Comfy-Org/lotus)
- [ModelScope:Comfy-Org/lotus](https://modelscope.cn/models/Comfy-Org/lotus)

**diffusion_models**

- [lotus-depth-d-v1-1.safetensors](https://huggingface.co/Comfy-Org/lotus/resolve/main/lotus-depth-d-v1-1.safetensors) (1.62 GB) 

**vae**

- [vae-ft-mse-840000-ema-pruned.safetensors](https://huggingface.co/stabilityai/sd-vae-ft-mse-original/resolve/main/vae-ft-mse-840000-ema-pruned.safetensors) (319.1 MB)  

You also use any SD1.5 VAE


```
ComfyUI/
├── models/
│   ├── diffusion_models/
│   │   └─── lotus-depth-d-v1-1.safetensors
│   └── vae/
│       └──  lvae-ft-mse-840000-ema-pruned.safetensors
```

</details>
