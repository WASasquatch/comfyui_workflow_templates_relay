# LTX2.3 LoRA: Video Outpainting

[← Video Tools](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_ltx2_3_lora_video_outpainting)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_lora_video_outpainting-1.webp" width="360" alt="LTX2.3 LoRA: Video Outpainting template_ltx2_3_lora_video_outpainting-1.webp">

> Video Outpainting using the LTX 2.3 Video Outpainting IC LoRA. Expand your video in any direction!

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_lora_video_outpainting.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_ltx2_3_lora_video_outpainting.json)

## Details

| | |
|---|---|
| Name | `template_ltx2_3_lora_video_outpainting` |
| Category | Foundation › Video Tools |
| Output | video |
| Models | LTX-2.3 |
| Tags | Outpainting, LoRA |
| Type | open source |
| Date | 2026-05-21 |
| Author | PurzBeats |
| Download size | 58.2 GB |
| Min ComfyUI version | 0.16.4 |
| Distributions | cloud |
| Usage | 89 |
| Nodes | 46 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `VHS_LoadVideo` #5060 | video | ltx2.3_video_outpainting_input.mp4 |

## Custom nodes required

- [ComfyMath](https://registry.comfy.org/nodes/ComfyMath)
- [comfyui-kjnodes](https://registry.comfy.org/nodes/comfyui-kjnodes)
- [ComfyUI-LTXVideo](https://registry.comfy.org/nodes/ComfyUI-LTXVideo)
- [comfyui-videohelpersuite](https://registry.comfy.org/nodes/comfyui-videohelpersuite)

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `ltx-2.3-22b-dev-fp8.safetensors` | `checkpoints` | [link](https://huggingface.co/Lightricks/LTX-2.3-fp8/resolve/main/ltx-2.3-22b-dev-fp8.safetensors) |
| `ltx-2.3-22b-distilled-lora-384.safetensors` | `loras` | [link](https://huggingface.co/Lightricks/LTX-2.3/resolve/main/ltx-2.3-22b-distilled-lora-384.safetensors) |
| `ltx-2.3-22b-ic-lora-outpaint.safetensors` | `loras` | [link](https://huggingface.co/oumoumad/LTX-2.3-22b-IC-LoRA-Outpaint/resolve/main/ltx-2.3-22b-ic-lora-outpaint.safetensors) |
| `gemma_3_12B_it.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it.safetensors) |

## Subgraphs

- **LTX 2.3 - Video Outpainting** (42 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `ComfyMathExpression` | 3 |  |
| `ResizeImageMaskNode` | 3 | comfy-core |
| `VHS_VideoCombine` | 3 | comfyui-videohelpersuite |
| `CLIPTextEncode` | 2 | comfy-core |
| `Float32ColorCorrect` | 2 |  |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `PrimitiveInt` | 2 |  |
| `CFGGuider` | 1 | comfy-core |
| `CheckpointLoaderSimple` | 1 | comfy-core |
| `CM_FloatToInt` | 1 | ComfyMath |
| `EmptyLTXVLatentVideo` | 1 | comfy-core |
| `GetImageSize` | 1 | comfy-core |
| `ImageConcanate` | 1 | comfyui-kjnodes |
| `ImagePadKJ` | 1 | comfyui-kjnodes |
| `KSamplerSelect` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `LTXAddVideoICLoRAGuide` | 1 | ComfyUI-LTXVideo |
| `LTXAVTextEncoderLoader` | 1 | comfy-core |
| `LTXVAudioVAEDecode` | 1 | comfy-core |
| `LTXVAudioVAELoader` | 1 | comfy-core |
| `LTXVConcatAVLatent` | 1 | comfy-core |
| `LTXVConditioning` | 1 | comfy-core |
| `LTXVCropGuides` | 1 | comfy-core |
| `LTXVEmptyLatentAudio` | 1 | comfy-core |
| `LTXVImgToVideoConditionOnly` | 1 | ComfyUI-LTXVideo |
| `LTXVPreprocess` | 1 | comfy-core |
| `LTXVSeparateAVLatent` | 1 | comfy-core |
| `ManualSigmas` | 1 | comfy-core |
| `MarkdownNote` | 1 |  |
| `PrimitiveBoolean` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `VAEDecode` | 1 |  |
| `VAEDecodeTiled` | 1 | comfy-core |
| `VHS_LoadVideo` | 1 | comfyui-videohelpersuite |
| `VHS_VideoInfo` | 1 | comfyui-videohelpersuite |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

# LTX 2.3 Video Outpainting

## Controls

**`skip_first_frames`** — trims frames from the start of your clip.
**`frame_count`** — sets how many frames to process after the skip.

**Example:** 600-frame clip → set `skip_first_frames: 60`, `frame_count: 480` = 480 frames starting at frame 60 ✅

---

## Aspect Ratio

Set `target_aspect_w` and `target_aspect_h` to your desired output ratio.

| Format | W | H |
|---|---|---|
| Vertical (TikTok/Reels) | 9 | 16 |
| Square | 1 | 1 |
| Landscape | 16 | 9 |

Hit **▷ Run** when ready.

| Prompt is optional.

</details>
