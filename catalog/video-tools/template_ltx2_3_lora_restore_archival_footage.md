# Restore Archival Footage - LTX 2.3 Dearchive LoRA

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_lora_restore_archival_footage-1.webp" width="360" alt="Restore Archival Footage - LTX 2.3 Dearchive LoRA template_ltx2_3_lora_restore_archival_footage-1.webp">

> Upload an input video or archival footage and restore it with 1 click.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_lora_restore_archival_footage.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_ltx2_3_lora_restore_archival_footage.json)

## Details

| | |
|---|---|
| Name | `template_ltx2_3_lora_restore_archival_footage` |
| Category | Foundation › Video Tools |
| Media type | image |
| Models | LTX-2.3 |
| Tags | Video Edit, LoRA |
| Type | open source |
| Date | 2026-05-21 |
| Author | hellorob |
| Download size | 66.6 GB |
| Min ComfyUI version | 0.16.4 |
| Usage | 23 |
| Nodes | 55 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadVideo` #5188 | video | input_dearchive.mp4 |

## Custom nodes required

- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [ComfyUI-LTXVideo](https://registry.comfy.org/nodes/ComfyUI-LTXVideo)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-2.3-22b-dev.safetensors` | `checkpoints` | [link](https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-22b-dev.safetensors) |
| `ltx-2.3-spatial-upscaler-x2-1.1.safetensors` | `latent_upscale_models` | [link](https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-spatial-upscaler-x2-1.1.safetensors) |
| `gemma_3_12B_it.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it.safetensors) |

## Subgraphs

- **Video Generation (LTX-2.3 Remove Subtitles)** (43 nodes)
- **Video Stitch** (8 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `GetVideoComponents` | 4 | comfy-core |
| `ComfyMathExpression` | 3 | comfy-core |
| `CFGGuider` | 2 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `CreateVideo` | 2 | comfy-core |
| `KSamplerSelect` | 2 | comfy-core |
| `LTXAddVideoICLoRAGuide` | 2 | ComfyUI-LTXVideo |
| `LTXVConcatAVLatent` | 2 | comfy-core |
| `LTXVCropGuides` | 2 | comfy-core |
| `LTXVSeparateAVLatent` | 2 | comfy-core |
| `LTXVSetAudioRefTokens` | 2 | ComfyUI-LTXVideo |
| `ManualSigmas` | 2 | comfy-core |
| `RandomNoise` | 2 | comfy-core |
| `ResizeImageMaskNode` | 2 | comfy-core |
| `SamplerCustomAdvanced` | 2 | comfy-core |
| `SaveVideo` | 2 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `EmptyLTXVLatentVideo` | 1 | comfy-core |
| `GetImageSize` | 1 |  |
| `GetImageSizeAndCount` | 1 | comfyui-kjnodes |
| `ImageResizeKJv2` | 1 |  |
| `ImageStitch` | 1 | comfy-core |
| `LatentUpscaleModelLoader` | 1 | comfy-core |
| `LoadVideo` | 1 | comfy-core |
| `LTXAVTextEncoderLoader` | 1 | comfy-core |
| `LTXFloatToInt` | 1 | ComfyUI-LTXVideo |
| `LTXICLoRALoaderModelOnly` | 1 | ComfyUI-LTXVideo |
| `LTXVAudioVAEDecode` | 1 | comfy-core |
| `LTXVAudioVAEEncode` | 1 | comfy-core |
| `LTXVAudioVAELoader` | 1 | comfy-core |
| `LTXVConditioning` | 1 | comfy-core |
| `LTXVEmptyLatentAudio` | 1 | comfy-core |
| `LTXVLatentUpsampler` | 1 | comfy-core |
| `LTXVTiledVAEDecode` | 1 | ComfyUI-LTXVideo |
| `MarkdownNote` | 1 |  |
| `Note` | 1 |  |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
Make sure to adjust the number of tiles and overlap to fit your hardware.
(fewer tiles will result in faster execution, but will require more memory)
```

</details>

<details><summary>MarkdownNote</summary>

The `latent_downscale_factor` output from the IC-LoRA Loader is intentionally ignored. The lipdub LoRA was trained with `reference_downscale_factor = 1` (full resolution), so no spatial downscaling of the reference is needed. For reference on handling other values, see `LTX-2.3_ICLoRA_Union_Control_Distilled.json`

</details>
