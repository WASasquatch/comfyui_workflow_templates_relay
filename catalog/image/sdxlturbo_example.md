# SDXL Turbo

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/sdxlturbo_example-1.webp" width="360" alt="SDXL Turbo sdxlturbo_example-1.webp">

> Generate images in a single step using SDXL Turbo.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/sdxlturbo_example.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/sdxlturbo_example.json)
- [Tutorial](https://comfyanonymous.github.io/ComfyUI_examples/sdturbo/)

## Details

| | |
|---|---|
| Name | `sdxlturbo_example` |
| Category | Foundation › Image |
| Media type | image |
| Models | SDXL, Stability |
| Tags | Text to Image, Image |
| Type | open source |
| Date | 2025-03-01 |
| Author | ComfyUI |
| Download size | 6.5 GB |
| Min ComfyUI version | 0.0.1 |
| Usage | 35 |
| Nodes | 10 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `sd_xl_turbo_1.0_fp16.safetensors` | `checkpoints` | [link](https://huggingface.co/stabilityai/sdxl-turbo/resolve/main/sd_xl_turbo_1.0_fp16.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 |  |
| `CheckpointLoaderSimple` | 1 |  |
| `EmptyLatentImage` | 1 |  |
| `KSamplerSelect` | 1 |  |
| `MarkdownNote` | 1 |  |
| `SamplerCustom` | 1 |  |
| `SaveImage` | 1 |  |
| `SDTurboScheduler` | 1 |  |
| `VAEDecode` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

🛈 [Learn more about this workflow](https://comfyanonymous.github.io/ComfyUI_examples/sdturbo/)

</details>
