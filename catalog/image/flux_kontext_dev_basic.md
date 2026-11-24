# Flux Kontext Dev Image Edit

[← Image](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=flux_kontext_dev_basic)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_kontext_dev_basic-1.webp" width="360" alt="Flux Kontext Dev Image Edit flux_kontext_dev_basic-1.webp"> <img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_kontext_dev_basic-2.webp" width="360" alt="Flux Kontext Dev Image Edit flux_kontext_dev_basic-2.webp">

> Smart image editing that keeps characters consistent, edits specific parts without affecting others, and preserves original styles.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/flux_kontext_dev_basic.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/flux_kontext_dev_basic.json)
- [Tutorial](https://docs.comfy.org/tutorials/flux/flux-1-kontext-dev)

## Details

| | |
|---|---|
| Name | `flux_kontext_dev_basic` |
| Category | Foundation › Image |
| Output | image |
| Models | FLUX.1 Kontext, FLUX |
| Tags | Image Edit |
| Type | open source |
| Date | 2025-06-26 |
| Author | ComfyUI |
| Download size | 16.4 GB |
| Min ComfyUI version | 0.3.42 |
| Usage | 156 |
| Nodes | 18 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #190 | image | flux_kontext_dev_basic_input_image.jpg |
| output | `SaveImage` #136 | image | flux_kontext_dev_basic.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `flux1-dev-kontext_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/flux1-kontext-dev_ComfyUI/resolve/main/split_files/diffusion_models/flux1-dev-kontext_fp8_scaled.safetensors) |
| `clip_l.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/clip_l.safetensors) |
| `t5xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn_scaled.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Image Edit (Flux.1 Kontext Dev)** (13 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `MarkdownNote` | 3 |  |
| `LoadImage` | 2 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `DualCLIPLoader` | 1 | comfy-core |
| `FluxGuidance` | 1 | comfy-core |
| `FluxKontextImageScale` | 1 | comfy-core |
| `ImageStitch` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `ReferenceLatent` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAEEncode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Model links</summary>

## Model Links

- [Hugging Face:Comfy-Org/flux1-kontext-dev_ComfyUI](https://huggingface.co/Comfy-Org/flux1-kontext-dev_ComfyUI)
- [Hugging Face:Comfy-Org/Lumina_Image_2.0_Repackaged](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged)

### Alternative Repos

- [ModelScope:Comfy-Org/flux1-kontext-dev_ComfyUI](https://modelscope.cn/models/Comfy-Org/flux1-kontext-dev_ComfyUI)
- [ModelScope:Comfy-Org/Lumina_Image_2.0_Repackaged](https://modelscope.cn/models/Comfy-Org/Lumina_Image_2.0_Repackaged)

[tutorial](https://docs.comfy.org/tutorials/flux/flux-1-kontext-dev)

**diffusion model**

- [flux1-dev-kontext_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/flux1-kontext-dev_ComfyUI/resolve/main/split_files/diffusion_models/flux1-dev-kontext_fp8_scaled.safetensors) (11.09 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/Lumina_Image_2.0_Repackaged/blob/main/split_files/vae/ae.safetensors)

**text encoder**

- [clip_l.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/blob/main/clip_l.safetensors)
- [t5xxl_fp16.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp16.safetensors) (9.12 GB) or [t5xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/comfyanonymous/flux_text_encoders/resolve/main/t5xxl_fp8_e4m3fn_scaled.safetensors) (4.8 GB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └── flux1-dev-kontext_fp8_scaled.safetensors
│   ├── 📂 vae/
│   │   └── ae.safetensor
│   └── 📂 text_encoders/
│       ├── clip_l.safetensors
│       └── t5xxl_fp16.safetensors 或者 t5xxl_fp8_e4m3fn_scaled.safetensors
```

</details>

<details><summary>Flux Kontext Prompt Techniques</summary>

## Flux Kontext Prompt Techniques

### 1. Basic Modifications
- Simple and direct: `"Change the car color to red"`
- Maintain style: `"Change to daytime while maintaining the same style of the painting"`

### 2. Style Transfer
**Principles:**
- Clearly name style: `"Transform to Bauhaus art style"`
- Describe characteristics: `"Transform to oil painting with visible brushstrokes, thick paint texture"`
- Preserve composition: `"Change to Bauhaus style while maintaining the original composition"`

### 3. Character Consistency
**Framework:**
- Specific description: `"The woman with short black hair"` instead of "she"
- Preserve features: `"while maintaining the same facial features, hairstyle, and expression"`
- Step-by-step modifications: Change background first, then actions

### 4. Text Editing
- Use quotes: `"Replace 'joy' with 'BFL'"`
- Maintain format: `"Replace text while maintaining the same font style"`

## Common Problem Solutions

### Character Changes Too Much
❌ Wrong: `"Transform the person into a Viking"`
✅ Correct: `"Change the clothes to be a viking warrior while preserving facial features"`

### Composition Position Changes
❌ Wrong: `"Put him on a beach"`
✅ Correct: `"Change the background to a beach while keeping the person in the exact same position, scale, and pose"`

### Style Application Inaccuracy
❌ Wrong: `"Make it a sketch"`
✅ Correct: `"Convert to pencil sketch with natural graphite lines, cross-hatching, and visible paper texture"`

## Core Principles

1. **Be Specific and Clear** - Use precise descriptions, avoid vague terms
2. **Step-by-step Editing** - Break complex modifications into multiple simple steps
3. **Explicit Preservation** - State what should remain unchanged
4. **Verb Selection** - Use "change", "replace" rather than "transform"

## Best Practice Templates

**Object Modification:**
`"Change [object] to [new state], keep [content to preserve] unchanged"`

**Style Transfer:**
`"Transform to [specific style], while maintaining [composition/character/other] unchanged"`

**Background Replacement:**
`"Change the background to [new background], keep the subject in the exact same position and pose"`

**Text Editing:**
`"Replace '[original text]' with '[new text]', maintain the same font style"`

> **Remember:** The more specific, the better. Kontext excels at understanding detailed instructions and maintaining consistency.

</details>

<details><summary>About multiple images reference</summary>

[English] In addition to using **Image Stitch** to combine two images at a time, you can also encode individual images, then concatenate multiple latent conditions using the **ReferenceLatent** node, thus achieving the purpose of referencing multiple images. You can use the **EmptySD3LatentImage** node on the right to connect to **KSamper** and customize the size of the **latent_image**.

</details>
