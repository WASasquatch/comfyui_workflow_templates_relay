# 1 Click Multiple Character Angles

[← Character & Fashion](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=templates-1_click_multiple_character_angles-v1.0)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-1_click_multiple_character_angles-v1.0-1.webp" width="360" alt="1 Click Multiple Character Angles templates-1_click_multiple_character_angles-v1.0-1.webp">

> Upload an image of your character and get multiple views of that image from different angles

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/templates-1_click_multiple_character_angles-v1.0.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/templates-1_click_multiple_character_angles-v1.0.json)

## Details

| | |
|---|---|
| Name | `templates-1_click_multiple_character_angles-v1.0` |
| Category | Applied › Character & Fashion |
| Output | image |
| Models | Qwen-Image-Edit |
| Tags | Image Edit |
| Type | open source |
| Date | 2025-12-08 |
| Author | hellorob |
| Download size | 29.1 GB |
| Min ComfyUI version | 0.5.0 |
| Usage | 292 |
| Nodes | 202 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #25 | image | character_input.png |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `qwen_image_edit_2511_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2511_bf16.safetensors) |
| `Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors` | `loras` | [link](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning/resolve/main/Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors) |
| `qwen-image-edit-2511-multiple-angles-lora.safetensors` | `loras` | [link](https://huggingface.co/fal/Qwen-Image-Edit-2511-Multiple-Angles-LoRA/resolve/main/qwen-image-edit-2511-multiple-angles-lora.safetensors) |
| `qwen_2.5_vl_7b_fp8_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/HunyuanVideo_1.5_repackaged/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) |
| `qwen_image_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) |

## Subgraphs

- **Image Edit (Qwen-Image 2511 with LoRA)** (24 nodes)
- **Image Edit (Qwen-Image 2511 with LoRA)** (24 nodes)
- **Image Edit (Qwen-Image 2511 with LoRA)** (24 nodes)
- **Image Edit (Qwen-Image 2511 with LoRA)** (24 nodes)
- **Image Edit (Qwen-Image 2511 with LoRA)** (24 nodes)
- **Image Edit (Qwen-Image 2511 with LoRA)** (24 nodes)
- **Image Edit (Qwen-Image 2511 with LoRA)** (24 nodes)
- **Image Edit (Qwen-Image 2511 with LoRA)** (24 nodes)
- **Qwen-Image 2511: Batch Angle Generation** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfySwitchNode` | 24 | comfy-core |
| `FluxKontextMultiReferenceLatentMethod` | 16 | comfy-core |
| `LoraLoaderModelOnly` | 16 | comfy-core |
| `PrimitiveFloat` | 16 | comfy-core |
| `PrimitiveInt` | 16 | comfy-core |
| `TextEncodeQwenImageEditPlus` | 16 | comfy-core |
| `CFGNorm` | 8 | comfy-core |
| `CLIPLoader` | 8 | comfy-core |
| `FluxKontextImageScale` | 8 | comfy-core |
| `KSampler` | 8 | comfy-core |
| `ModelSamplingAuraFlow` | 8 | comfy-core |
| `Note` | 8 |  |
| `PrimitiveBoolean` | 8 | comfy-core |
| `SaveImage` | 8 | comfy-core |
| `UNETLoader` | 8 | comfy-core |
| `VAEDecode` | 8 | comfy-core |
| `VAEEncode` | 8 | comfy-core |
| `VAELoader` | 8 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |

## Notes embedded in the workflow

<details><summary>For Local User</summary>

## Report issue

If you found any issues when running this workflow, [report template issue here](https://github.com/Comfy-Org/workflow_templates/issues)

## Model Links

- [Hugging Face:Comfy-Org/Qwen-Image_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI)
- [Hugging Face:Comfy-Org/Qwen-Image-Edit_ComfyUI](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI)

### Alternative Repos

- [ModelScope:Comfy-Org/Qwen-Image_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image_ComfyUI)
- [ModelScope:Comfy-Org/Qwen-Image-Edit_ComfyUI](https://modelscope.cn/models/Comfy-Org/Qwen-Image-Edit_ComfyUI)

**text_encoders**

- [qwen_2.5_vl_7b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/text_encoders/qwen_2.5_vl_7b_fp8_scaled.safetensors) (8.74 GB)

**loras**

- [Qwen-Edit-2509-Multiple-angles.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/loras/Qwen-Edit-2509-Multiple-angles.safetensors) (225.2 MB)
- [Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors](https://huggingface.co/lightx2v/Qwen-Image-Lightning/resolve/main/Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors) (810.2 MB)

**diffusion_models**

- [qwen_image_edit_2509_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-Edit_ComfyUI/resolve/main/split_files/diffusion_models/qwen_image_edit_2509_fp8_e4m3fn.safetensors) (19.03 GB)

**vae**

- [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/resolve/main/split_files/vae/qwen_image_vae.safetensors) (242 MB)

Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 text_encoders/
│   │      └── qwen_2.5_vl_7b_fp8_scaled.safetensors
│   ├── 📂 loras/
│   │      ├── Qwen-Edit-2509-Multiple-angles.safetensors
│   │      └── Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors
│   ├── 📂 diffusion_models/
│   │      └── qwen_image_edit_2509_fp8_e4m3fn.safetensors
│   └── 📂 vae/
│          └── qwen_image_vae.safetensors
```

</details>

<details><summary>Note</summary>

```text
The "Edit Model Reference Method" nodes above are not needed if you use Comfy files, but may be needed if you use repackaged ones from other people.
```

</details>

<details><summary>Note</summary>

```text
The "Edit Model Reference Method" nodes above are not needed if you use Comfy files, but may be needed if you use repackaged ones from other people.
```

</details>

<details><summary>Note</summary>

```text
The "Edit Model Reference Method" nodes above are not needed if you use Comfy files, but may be needed if you use repackaged ones from other people.
```

</details>

<details><summary>Note</summary>

```text
The "Edit Model Reference Method" nodes above are not needed if you use Comfy files, but may be needed if you use repackaged ones from other people.
```

</details>

<details><summary>Note</summary>

```text
The "Edit Model Reference Method" nodes above are not needed if you use Comfy files, but may be needed if you use repackaged ones from other people.
```

</details>

<details><summary>Note</summary>

```text
The "Edit Model Reference Method" nodes above are not needed if you use Comfy files, but may be needed if you use repackaged ones from other people.
```

</details>

<details><summary>Note</summary>

```text
The "Edit Model Reference Method" nodes above are not needed if you use Comfy files, but may be needed if you use repackaged ones from other people.
```

</details>

<details><summary>Note</summary>

```text
The "Edit Model Reference Method" nodes above are not needed if you use Comfy files, but may be needed if you use repackaged ones from other people.
```

</details>
