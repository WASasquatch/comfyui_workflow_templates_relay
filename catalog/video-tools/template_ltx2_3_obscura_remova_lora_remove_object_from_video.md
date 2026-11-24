# Remove Object from Video - LTX 2.3 Obscura Remova LoRA

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_ltx2_3_obscura_remova_lora_remove_object_from_video)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_obscura_remova_lora_remove_object_from_video-1.webp" width="360" alt="Remove Object from Video - LTX 2.3 Obscura Remova LoRA template_ltx2_3_obscura_remova_lora_remove_object_from_video-1.webp">

> Upload an input video and prompt for the object to get removed from the video's foreground.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_obscura_remova_lora_remove_object_from_video.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_ltx2_3_obscura_remova_lora_remove_object_from_video.json)

## Details

| | |
|---|---|
| Name | `template_ltx2_3_obscura_remova_lora_remove_object_from_video` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | LTX-2.3 |
| Tags | Video Edit, LoRA |
| Type | open source |
| Date | 2026-05-21 |
| Author | hellorob |
| Download size | 57.2 GB |
| Min ComfyUI version | 0.19.0 |
| Distributions | cloud |
| Usage | 84 |
| Nodes | 34 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #39 | video | input_playing_the_piano.mp4 |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [ComfyUI-LTXVideo](https://registry.comfy.org/nodes/ComfyUI-LTXVideo)
- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-2.3-22b-dev_transformer_only_bf16.safetensors` | `diffusion_models` | [link](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/main/diffusion_models/ltx-2.3-22b-dev_transformer_only_bf16.safetensors) |
| `ltx-2.3-22b-distilled-lora-384-1.1.safetensors` | `loras` | [link](https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-22b-distilled-lora-384-1.1.safetensors) |
| `ltx23-obscura_remova.safetensors` | `loras` | [link](https://civitai.com/api/download/models/2909707) |
| `gemma_3_12B_it_fp4_mixed.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it_fp4_mixed.safetensors) |
| `ltx-2.3_text_projection_bf16.safetensors` | `text_encoders` | [link](https://huggingface.co/Kijai/LTX2.3_comfy/resolve/main/text_encoders/ltx-2.3_text_projection_bf16.safetensors) |

## Subgraphs

- **Video Generation (LTX-2.3 Obscura Remova LoRA)** (30 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `CLIPTextEncode` | 2 | comfy-core |
| `CreateVideo` | 2 | comfy-core |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `SaveVideo` | 2 | comfy-core |
| `VAELoaderKJ` | 2 | comfyui-kjnodes |
| `ComfyMathExpression` | 1 | comfy-core |
| `ComfyNumberConvert` | 1 | comfy-core |
| `DualCLIPLoader` | 1 | comfy-core |
| `EmptyLTXVLatentVideo` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `GetVideoComponents` | 1 | comfy-core |
| `ImageFromBatch` | 1 | comfy-core |
| `ImageStitch` | 1 | comfy-core |
| `KSampler` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `LTXAddVideoICLoRAGuide` | 1 | ComfyUI-LTXVideo |
| `LTXVAudioVAEDecode` | 1 | comfy-core |
| `LTXVConcatAVLatent` | 1 | comfy-core |
| `LTXVConditioning` | 1 | comfy-core |
| `LTXVCropGuides` | 1 | comfy-core |
| `LTXVEmptyLatentAudio` | 1 | comfy-core |
| `LTXVSeparateAVLatent` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `PreviewAny` | 1 | comfy-core |
| `PrimitiveInt` | 1 | comfy-core |
| `ResizeImageMaskNode` | 1 | comfy-core |
| `UNETLoader` | 1 | comfy-core |
| `VAEDecode` | 1 | comfy-core |
| `VHS_GetImageCount` | 1 | comfyui-videohelpersuite |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

## LTX-2.3 Obscura Remova LoRA — Usage Guide

### Prompt Structure
> `Remove the {object} from the foreground.`

### Recommended Dimensions (width × height)

| Aspect | Resolution |
|---|---|
| Landscape (16:9) | 1920 × 1088 |
| Portrait (9:16) | 1088 × 1920 |
| Landscape (16:9) | 1280 × 704 |
| Portrait (9:16) | 704 × 1280 |

### LoRA Settings
- **`strength_model`**: `1.3` – `2.0`

### Stitch Direction
- **Landscape** ratios → `stitch_direction = down`
- **Portrait** ratios → `stitch_direction = right`

</details>
