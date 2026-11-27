# MiniMax-H3-Image: Character Swap

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_minimax_h3_image_character_swap)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_minimax_h3_image_character_swap-1.webp" width="360" alt="MiniMax-H3-Image: Character Swap image_minimax_h3_image_character_swap-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_minimax_h3_image_character_swap-2.webp" width="360" alt="MiniMax-H3-Image: Character Swap image_minimax_h3_image_character_swap-2.webp">

> Swap the person in a photo for a character from a reference image. The adapter reads the picture as <Picture 1> and the character as <Picture 2>, keeps the pose, framing and lighting of the shot, and carries over the reference character's face, costume and materials. Built on MiniMax-H3-Image with the h3_image_character_swap_v1 LoRA at strength 1.0.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_minimax_h3_image_character_swap.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_minimax_h3_image_character_swap.json)

## Details

| | |
|---|---|
| Name | `image_minimax_h3_image_character_swap` |
| Category | Applied › Character & Fashion |
| Output | image |
| Models | MiniMax H3 Image |
| Tags | Character Replacement, Image, Image Edit |
| Type | open source |
| Date | 2026-11-10 |
| Author | ComfyUI |
| Download size | 62.1 GB |
| Min ComfyUI version | 0.45.0 |
| Usage | 618 |
| Nodes | 18 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #45 | image | h3_char_swap_source.png |
| input | `LoadImage` #64 | image | h3_char_swap_reference.png |
| output | `SaveImage` #9 | image | image_minimax_h3_image_character_swap.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `minimax_h3_image_pruned_int8_convrot.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/diffusion_models/minimax_h3_image_pruned_int8_convrot.safetensors) |
| `h3_image_character_swap_v1.safetensors` | `loras` | [link](https://huggingface.co/akatz-ai/MiniMax-H3-Image-Character-Swap-LoRA/resolve/main/h3_image_character_swap_v1.safetensors) |
| `qwen3vl_32b_minimax_h3_int8_convrot.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_int8_convrot.safetensors) |
| `minimax_h3_image_vae_fp16.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/vae/minimax_h3_image_vae_fp16.safetensors) |

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `LoadImage` | 2 |  |
| `MarkdownNote` | 2 |  |
| `ResizeImageMaskNode` | 2 |  |
| `CLIPLoader` | 1 |  |
| `ConditioningZeroOut` | 1 |  |
| `GetImageSize` | 1 |  |
| `ImageCompare` | 1 |  |
| `KSampler` | 1 |  |
| `LoadLoraModel` | 1 |  |
| `MiniMaxH3ImageConditioning` | 1 |  |
| `PrimitiveStringMultiline` | 1 |  |
| `SaveImage` | 1 |  |
| `UNETLoader` | 1 |  |
| `VAEDecode` | 1 |  |
| `VAELoader` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note: size and reference images</summary>

Two pictures go in: **Load Image (Source Image)** is the picture to edit and reads as `<Picture 1>`; **Load Image (Reference Character)** is the character to carry over and reads as `<Picture 2>`.

The source is resized to **1 MP** (`scale total pixels`) and then to a multiple of 32, and that size becomes the canvas and the output size, 864 × 1152 with the example images. 1 MP is what the adapter's author tested and recommends. This workflow also holds up at 16 MP (`scale total pixels` = 16), at more VRAM and more time. The reference picture is scaled internally, so its own resolution only needs to be reasonable.

**No prompt enhancer**: the adapter was trained on short editing instructions, so write the instruction yourself and keep the `<Picture n>` references. The author's own prompt, shortened:

> Swap only the red-haired woman in the dark high-collared jacket in the close foreground in `<Picture 1>` with the character from `<Picture 2>`. Keep the original scene, framing, other people, and the target’s placement and action.

For more references, add `Load Image` nodes, connect them to the conditioning node and name them `<Picture 3>`, `<Picture 4>`, ...

</details>

<details><summary>Model Links</summary>

## Input Assets

- [h3_char_swap_source.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/h3_char_swap_source.png)
- [h3_char_swap_reference.png](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/refs/heads/main/input/h3_char_swap_reference.png)

## Model Links

- [Hugging Face:Comfy-Org/MiniMax-H3-Image](https://huggingface.co/Comfy-Org/MiniMax-H3-Image)
- [Hugging Face:Comfy-Org/MiniMax-H3](https://huggingface.co/Comfy-Org/MiniMax-H3)

### Alternative Repos

- [ModelScope:Comfy-Org/MiniMax-H3-Image](https://modelscope.cn/models/Comfy-Org/MiniMax-H3-Image)
- [ModelScope:Comfy-Org/MiniMax-H3](https://modelscope.cn/models/Comfy-Org/MiniMax-H3)

**diffusion_models**

- [minimax_h3_image_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/diffusion_models/minimax_h3_image_pruned_int8_convrot.safetensors) (21 GB)

**text_encoders**

- [qwen3vl_32b_minimax_h3_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_int8_convrot.safetensors) (25.28 GB)

**vae**

- [minimax_h3_image_vae_fp16.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3-Image/resolve/main/vae/minimax_h3_image_vae_fp16.safetensors) (1.17 GB)

**loras**

- [h3_image_character_swap_v1.safetensors](https://huggingface.co/akatz-ai/MiniMax-H3-Image-Character-Swap-LoRA/resolve/main/h3_image_character_swap_v1.safetensors) (155 MB)

## Adapter

The character-swap adapter is published in its original repo, [akatz-ai/MiniMax-H3-Image-Character-Swap-LoRA](https://huggingface.co/akatz-ai/MiniMax-H3-Image-Character-Swap-LoRA) (Akatz). It is a rank-16 LoRA trained with AI Toolkit on 140 paired edits and evaluated on the INT8 ConvRot checkpoint above; that repo holds the still-image examples, their prompts and the adapter license. Adapter use follows the MiniMax H3 Image Community License Agreement.

## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── minimax_h3_image_pruned_int8_convrot.safetensors
│   ├── 📂 loras/
│   │   └── h3_image_character_swap_v1.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen3vl_32b_minimax_h3_int8_convrot.safetensors
│   └── 📂 vae/
│       └── minimax_h3_image_vae_fp16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>
