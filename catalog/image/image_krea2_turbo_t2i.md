# Krea-2: Text to Image

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=image_krea2_turbo_t2i)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_krea2_turbo_t2i-1.webp" width="360" alt="Krea-2: Text to Image image_krea2_turbo_t2i-1.webp">

> Generate images from text prompts using Krea 2, a foundation model built for aesthetic quality and creative control. It focuses on rendering expressive and artistic styles. Ideal for concept art exploration, visual brainstorming, and creating stylized imagery for design projects.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/image_krea2_turbo_t2i.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/image_krea2_turbo_t2i.json)

## Details

| | |
|---|---|
| Name | `image_krea2_turbo_t2i` |
| Category | Foundation › Image |
| Output | image |
| Models | Krea 2 |
| Tags | Text to Image |
| Type | open source |
| Date | 2026-06-24 |
| Author | ComfyUI |
| Download size | 17.8 GB |
| Min ComfyUI version | 0.44.0 |
| Usage | 8677 |
| Nodes | 25 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `krea2_turbo_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/diffusion_models/krea2_turbo_fp8_scaled.safetensors) |
| `krea2_darkbrush.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/loras/krea2_darkbrush.safetensors) |
| `qwen3vl_4b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/text_encoders/qwen3vl_4b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Text to Image (Krea-2 Turbo)** (20 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 3 | comfy-core |
| `MarkdownNote` | 3 |  |
| `PrimitiveBoolean` | 2 | comfy-core |
| `PrimitiveStringMultiline` | 2 | comfy-core |
| `StringConcatenate` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `EmptyLatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `PreviewAny` | 1 | comfy-core |
| `ResolutionSelector` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `TextGenerateV2` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>LoRA Trigger Words and Settings</summary>

## Model Links

- [Hugging Face:Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2)
- [ModelScope:Comfy-Org/Krea-2](https://modelscope.cn/models/Comfy-Org/Krea-2)

Download the style LoRAs used in this workflow from [Comfy-Org/Krea-2/loras](https://huggingface.co/Comfy-Org/Krea-2/tree/main/loras). Place the `.safetensors` files in `ComfyUI/models/loras/`.

| LoRA                   | Trigger Words                        | Recommended Strength |
|------------------------|--------------------------------------|-------|
| `krea2_darkbrush`      | `monochrome ink wash style`          | `1.0` |
| `krea2_dotmatrix`      | `monochrome stippling style`         | `1.0` |
| `krea2_kidsdrawing`    | `naive expressive sketch style`      | `1.0` |
| `krea2_neondrip`       | `textured abstract style`            | `1.0` |
| `krea2_rainywindow`    | `rainy window style`                 | `1.0` |
| `krea2_retroanime`     | `purple retro anime style`           | `1.0` |
| `krea2_softwatercolor` | `art deco watercolor style`          | `1.0` |
| `krea2_sunsetblur`     | `ethereal motion blur style`         | `1.0` |
| `krea2_vintagetarot`   | `vintage tarot style`                | `1.0` |

</details>

<details><summary>Model Links</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [ModelScope:Comfy-Org/Krea-2](https://modelscope.cn/models/Comfy-Org/Krea-2)

For BF16 and NVFP4 variants, see [Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2)

**diffusion_models**

- [krea2_turbo_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/diffusion_models/krea2_turbo_fp8_scaled.safetensors) (12.24 GB)

**text_encoders**

- [qwen3vl_4b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/text_encoders/qwen3vl_4b_fp8_scaled.safetensors) (4.88 GB)

**vae**

- [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/vae/qwen_image_vae.safetensors) (242 MB)

**loras**

- [krea2_darkbrush.safetensors](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/loras/krea2_darkbrush.safetensors) (447.6 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── krea2_turbo_fp8_scaled.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen3vl_4b_fp8_scaled.safetensors
│   ├── 📂 vae/
│   │   └── qwen_image_vae.safetensors
│   └── 📂 loras/
│       └── krea2_darkbrush.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note: Krea-2</summary>

Guide: [krea-2](https://docs.comfy.org/tutorials/image/krea/krea-2)

This workflow generates images with **Krea-2 Turbo**, a fast distilled text-to-image model. The workflow is organized into a few parts: each handles a different step so you can generate quickly without digging through every node.

## Text to Image (Krea-2 Turbo) Subgraph

- [Hugging Face:Comfy-Org/Krea-2](https://huggingface.co/Comfy-Org/Krea-2)
- [ModelScope:Comfy-Org/Krea-2](https://modelscope.cn/models/Comfy-Org/Krea-2)

Double-click this node to open the full pipeline. Inside, the canvas is grouped into several areas:

**Models**: Loads the diffusion model, text encoder, VAE, and optional style LoRA (`LoraLoaderModelOnly`).

**Prompt**: Enter your image description in **Text String (User Prompt)**.

**Prompt Enhancement**: Expands your prompt before generation. Enabled by default (`prompt_enhance`). You can turn it off to use your prompt as-is, or replace the built-in module with **OpenAI** or **Gemini** API nodes.

**Feature Switch**: Quick toggles on the left side of the subgraph:
- `prompt_enhance`: enable or disable prompt expansion
- `enable_lora?`: enable or disable the style LoRA

**Image Generation**: Handles latent sizing, sampling (8 steps), and VAE decode to produce the final image.

When using a LoRA, set `enable_lora?` to true, select the matching file in **LoraLoaderModelOnly**, and adjust `lora_strength` as needed.

## LoRA & Trigger Word (CustomCombo)

On the main canvas, the **CustomCombo** node is where you choose which style LoRA you are using (e.g. `krea2_coolblue`, `krea2_darkbrush`). The workflow uses your selection to automatically append the correct **trigger word** to your prompt.

- Download LoRA files from [Comfy-Org/Krea-2/loras](https://huggingface.co/Comfy-Org/Krea-2/tree/main/loras) and place them in `ComfyUI/models/loras/`
- Select the LoRA name that matches the file loaded inside the subgraph
- The trigger word is applied for you: no need to type it manually
- For trigger words and recommended strength values, see the **LoRA Trigger Words and Settings** note beside this workflow

</details>
