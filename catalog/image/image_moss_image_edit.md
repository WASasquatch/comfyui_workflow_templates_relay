# MOSS-Image: Image Edit LoRA

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_moss_image_edit)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_moss_image_edit-1.webp" width="360" alt="MOSS-Image: Image Edit LoRA image_moss_image_edit-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_moss_image_edit-2.webp" width="360" alt="MOSS-Image: Image Edit LoRA image_moss_image_edit-2.webp">

> Edit a photo with a short instruction using MOSS-Image and its edit LoRA: the instruction and the source image are encoded together, so the sampler redraws the same frame and only the described change is applied. Colour, material, outfit and background swaps keep the face, hair, pose and framing intact, and a Compare Images node shows the source next to the result.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_moss_image_edit.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_moss_image_edit.json)

## Details

| | |
|---|---|
| Name | `image_moss_image_edit` |
| Category | Foundation › Image |
| Output | image |
| Models | MOSS-Image |
| Tags | Image Edit |
| Type | open source |
| Date | 2026-10-26 |
| Author | ComfyUI |
| Download size | 12.4 GB |
| Min ComfyUI version | 0.43.0 |
| Usage | 1804 |
| Nodes | 17 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #8 | image | two_women_berets_floral_jackets.png |
| output | `SaveImage` #9 | image | image_moss_image_edit.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `moss_image_sft_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/diffusion_models/moss_image_sft_int8_convrot.safetensors) |
| `moss_image_edit_lora_rank_64_bf16.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/loras/moss_image_edit_lora_rank_64_bf16.safetensors) |
| `qwen3.5_9b_w4a8_gptq.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors) |
| `flux2-vae_small.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/vae/flux2-vae_small.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 2 |  |
| `TextEncodeMOSSImageEdit` | 2 |  |
| `CLIPLoader` | 1 |  |
| `EmptyFlux2LatentImage` | 1 |  |
| `GetImageSize` | 1 |  |
| `ImageCompare` | 1 |  |
| `ImageScaleToTotalPixels` | 1 |  |
| `KSampler` | 1 |  |
| `LoadImage` | 1 |  |
| `LoraLoaderModelOnly` | 1 |  |
| `SaveImage` | 1 |  |
| `SkipLayerGuidanceDiTSimple` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## MOSS-Image: Image Edit

Edit one photo with a short instruction. An edit LoRA runs on top of the MOSS-Image SFT checkpoint, and the instruction is encoded together with the source image as a reference, so the sampler redraws the same frame with only the described change applied.

### How to use

1. **Load Image** (node 8): the photo to edit. It is scaled to 1.0 MP and aligned to 16 px (node 29), and **Get Image Size** feeds that size to **Empty Flux2 Latent Image**, so the output keeps the source aspect ratio.
2. **Text Encode MOSS-Image Edit - positive** (node 39): describe only the change. The phrasing the LoRA was trained on works best: `Change only the X to Y. Keep the character, face, hair, pose, background and composition unchanged.`
3. **Text Encode MOSS-Image Edit - negative** (node 36): the model's recommended negative line. It sees the same reference image, so it describes what to avoid, not what to remove from the scene.
4. **KSampler** (node 37): 30 steps, cfg 4.0, `euler`, `normal`, denoise 1: the values the LoRA author ships.
5. Queue. **Save Image** writes `image_moss_image_edit_*.png`, and **Compare Images** (node 20) shows the source next to the result.

### edit_format must match the LoRA

`edit_format` selects the layout the LoRA was trained with. Both encode nodes must use the same value.

| value | trained with |
|-------|--------------|
| `Moss-Image-Edit` | `moss_image_edit_lora_rank_64_bf16.safetensors`, the LoRA this workflow loads |
| `ai-toolkit` | ai-toolkit's MOSS-Image Edit Training |
| `ai-toolkit (kv_cache off)` | the same with `kv_cache` off: the references also attend to the image being generated, so they are recomputed every step |

Picking the wrong layout still returns an image, but a worse one: identity, framing and fine detail drift away from the source.

### Resolution

References enter the diffusion model at exactly the size they arrive with, so the source is scaled once by **Image Scale To Total Pixels** (node 29, 1.0 MP, 16 px step) and both the reference and the generated frame use that size. Lowering it to about 0.26 MP (a 512 px long edge) makes the run cheaper but looser: the model starts re-framing the subject instead of editing the frame it was given.

### Sampling

- **Skip Layer Guidance** (node 32) stays on, single layer `22`, 0 to 1.0 of the schedule: what the LoRA author ships.
- CFG 4.0 means the negative branch matters. If you see a necklace or earrings appear out of nowhere while editing the top, the cfg is too low for this LoRA; keep it at 4.0.

### More than one reference

The encode nodes autogrow `images.image_0`, `images.image_1`, ... Connect up to four photos (a garment, a face, a prop) and say in the prompt what each one is for. Extra slots appear only when you connect them; a disconnected slot costs nothing.

</details>

<details><summary>MarkdownNote</summary>

## Model Links

- [Hugging Face:Comfy-Org/MOSS-Image](https://huggingface.co/Comfy-Org/MOSS-Image) (checkpoints, text encoder, VAE, edit LoRA)
- [Hugging Face:chinoll/Moss-Image-Edit](https://huggingface.co/chinoll/Moss-Image-Edit) (upstream edit LoRA, same bytes as the rehosted file)

**ModelScope mirrors** (alternative repo location)

- [ModelScope:Comfy-Org/MOSS-Image](https://modelscope.cn/models/Comfy-Org/MOSS-Image)

**diffusion_models**

- [moss_image_sft_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/diffusion_models/moss_image_sft_int8_convrot.safetensors)
- [moss_image_sft_bf16.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/diffusion_models/moss_image_sft_bf16.safetensors) (higher precision, slower)

**loras**

- [moss_image_edit_lora_rank_64_bf16.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/loras/moss_image_edit_lora_rank_64_bf16.safetensors) (rank 64, bf16, 297 MB)

**text_encoders**

- [qwen3.5_9b_w4a8_gptq.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/text_encoders/qwen3.5_9b_w4a8_gptq.safetensors)
- [qwen3.5_9b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/text_encoders/qwen3.5_9b_int8_convrot.safetensors) (larger, slightly higher precision)

**vae**

- [flux2-vae_small.safetensors](https://huggingface.co/Comfy-Org/MOSS-Image/resolve/main/vae/flux2-vae_small.safetensors)

The edit LoRA runs on either MOSS-Image checkpoint: set `unet_model` to `moss_image_base_*` to try it on the base model. The Core support (`Text Encode MOSS-Image Edit`) ships from ComfyUI 0.43.0.

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── moss_image_sft_int8_convrot.safetensors
│   ├── 📂 loras/
│   │   └── moss_image_edit_lora_rank_64_bf16.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen3.5_9b_w4a8_gptq.safetensors
│   └── 📂 vae/
│       └── flux2-vae_small.safetensors
```

## Input Asset

`Load Image` points at `two_women_berets_floral_jackets.png`, two women in berets and floral jackets, which is what the shipped thumbnail was made from. Any image works: the graph scales it to 1.0 MP and keeps its aspect ratio, so portrait, square and landscape sources all come out at their own shape. Swap in your own file, or paint/connect extra references on the encode nodes.

</details>
