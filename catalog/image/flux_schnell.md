# Flux.1 Schnell FP8

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_schnell-1.webp" width="360" alt="Flux.1 Schnell FP8 flux_schnell-1.webp">

> Quickly generate images with Flux.1 Schnell fp8 quantized version. Ideal for low-end hardware, requires only 4 steps to generate images.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_schnell.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/flux_schnell.json)
- [Tutorial](https://docs.comfy.org/tutorials/flux/flux-1-text-to-image)

## Details

| | |
|---|---|
| Name | `flux_schnell` |
| Category | Foundation › Image |
| Media type | image |
| Models | FLUX.1, FLUX |
| Tags | Text to Image, Image |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 16.0 GB |
| Min ComfyUI version | 0.0.4 |
| Usage | 15 |
| Nodes | 9 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux1-schnell-fp8.safetensors` | `checkpoints` | [link](https://huggingface.co/Comfy-Org/flux1-schnell/resolve/main/flux1-schnell-fp8.safetensors?download=true) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 |  |
| `CheckpointLoaderSimple` | 1 |  |
| `EmptySD3LatentImage` | 1 |  |
| `KSampler` | 1 |  |
| `MarkdownNote` | 1 |  |
| `Note` | 1 |  |
| `SaveImage` | 1 |  |
| `VAEDecode` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
Note that Flux dev and schnell do not have any negative prompt so CFG should be set to 1.0. Setting CFG to 1.0 means the negative prompt is ignored.

The schnell model is a distilled model that can generate a good image with only 4 steps.
```

</details>

<details><summary>MarkdownNote</summary>

🛈 [Learn more about this workflow](https://comfyanonymous.github.io/ComfyUI_examples/flux/#flux-schnell-1)

</details>
