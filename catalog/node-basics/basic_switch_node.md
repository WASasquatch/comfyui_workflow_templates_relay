# Switch Node

[← Node Basics](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/basic_switch_node-1.webp" width="360" alt="Switch Node basic_switch_node-1.webp">

> Guide on how Switch Nodes work, simple Text Switch and LoRA Switch

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/basic_switch_node.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/basic_switch_node.json)

## Details

| | |
|---|---|
| Name | `basic_switch_node` |
| Category | Foundation › Node Basics |
| Media type | image |
| Models | Z-Image-Turbo |
| Tags | Node Basics |
| Type | open source |
| Date | 2026-03-30 |
| Author | ComfyUI |
| Download size | 19.3 GB |
| Min ComfyUI version | 0.4.0 |
| Usage | 14 |
| Nodes | 26 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `z_image_turbo_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) |
| `pixel_art_style_z_image_turbo.safetensors` | `loras` | [link](https://huggingface.co/tarn59/pixel_art_style_lora_z_image_turbo/resolve/main/pixel_art_style_z_image_turbo.safetensors) |
| `qwen_3_4b.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) |
| `ae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) |

## Subgraphs

- **Z-Image Turbo (Text to Image)** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 4 | comfy-core |
| `PrimitiveString` | 4 | comfy-core |
| `MarkdownNote` | 2 |  |
| `PreviewAny` | 2 | comfy-core |
| `PrimitiveStringMultiline` | 2 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPTextEncode` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `EmptySD3LatentImage` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |
| `ModelSamplingAuraFlow` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `SaveImage` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# ComfyUI Switch Node

Routes between two inputs via a boolean toggle. **OFF → `on_false`, ON → `on_true`.**

| Pin | Role |
|---|---|
| `on_false` | Output when switch is OFF |
| `on_true` | Output when switch is ON |
| `switch` | Boolean toggle |
| `output` | Selected value |

---

## Example 1 — String Switch

```
String("true")  → on_false ┐
                            Switch [OFF] → "true"
String("false") → on_true  ┘
```

The pin name describes *which state picks it*, not what the value is.

---

## Example 2 — LoRA Toggle

A single **LoRA Switch** boolean drives two switches in sync:

| LoRA Switch | Model | Prompt |
|---|---|---|
| OFF | Base model | `"a person smiling"` |
| ON | Base + LoRA | `"3d stylized style, a person smiling"` |

One toggle flips both the model and its trigger-word prompt together — clean A/B testing with no manual rewiring.

---

## Key Takeaways

- **Works with any type** — STRING, MODEL, CLIP, IMAGE, etc. ComfyUI infers it from the connection.
- **No mixing types** — both pins must carry the same data type or the workflow breaks.
- **One boolean, many switches** — wire a single toggle to multiple Switch nodes to keep everything in sync.
- Always include the **LoRA trigger word** in your `on_true` prompt or the LoRA effect will be weak.

</details>

<details><summary>Mdode Links</summary>

## Model Links

- [Hugging Face:Comfy-Org/z_image_turbo](https://huggingface.co/Comfy-Org/z_image_turbo)
- [ModelScope:Comfy-Org/z_image_turbo](https://modelscope.cn/models/Comfy-Org/z_image_turbo)

**loras**

- [pixel_art_style_z_image_turbo.safetensors](https://huggingface.co/tarn59/pixel_art_style_lora_z_image_turbo/resolve/main/pixel_art_style_z_image_turbo.safetensors) (162.2 MB)

**diffusion_models**

- [z_image_turbo_bf16.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) (11.46 GB)

**text_encoders**

- [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) (7.49 GB)

**vae**

- [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) (319.8 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 loras/
│   │   └── pixel_art_style_z_image_turbo.safetensors
│   ├── 📂 diffusion_models/
│   │   └── z_image_turbo_bf16.safetensors
│   ├── 📂 text_encoders/
│   │   └── qwen_3_4b.safetensors
│   └── 📂 vae/
│       └── ae.safetensors
```

</details>
