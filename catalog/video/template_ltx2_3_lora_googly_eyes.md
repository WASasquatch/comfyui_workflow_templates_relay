# Googly Eyes

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=template_ltx2_3_lora_googly_eyes)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_lora_googly_eyes-1.webp" width="360" alt="Googly Eyes template_ltx2_3_lora_googly_eyes-1.webp">

> LTX 2.3 LoRA that makes anyone in the input video have Googly Eyes. This workflow utilizes the Googlyeyes LTX 2.3 LoRA by TheBurgstall

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/template_ltx2_3_lora_googly_eyes.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/template_ltx2_3_lora_googly_eyes.json)

## Details

| | |
|---|---|
| Name | `template_ltx2_3_lora_googly_eyes` |
| Category | Foundation › Video |
| Output | video |
| Models | LTX-2.3 |
| Tags | Video Edit, LoRA |
| Type | open source |
| Date | 2026-05-21 |
| Author | PurzBeats |
| Download size | 57.2 GB |
| Min ComfyUI version | 0.16.4 |
| Usage | 18 |
| Nodes | 48 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `VHS_LoadVideo` #5060 | video | iclora_input_resized_purz.mp4 |

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
| `ltx-2.3-googlyeyes.safetensors` | `loras` | [link](https://huggingface.co/TheBurgstall/ltx-2.3-googlyeyes-lora/resolve/main/googlyeyes-ltx-2.3-rank32-step03000.safetensors) |
| `gemma_3_12B_it.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/ltx-2/resolve/main/split_files/text_encoders/gemma_3_12B_it.safetensors) |

## Subgraphs

- **LTX 2.3 - Googly Eyes** (43 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `VHS_VideoCombine` | 4 | comfyui-videohelpersuite |
| `ComfyMathExpression` | 3 |  |
| `ResizeImageMaskNode` | 3 | comfy-core |
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
| `ImageResizeKJv2` | 1 |  |
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

# Googly Eyes LoRA
### Controls
**`skip_first_frames`** — trims frames from the start of your clip before processing begins.
**`frame_count`** — sets how many frames to convert after the skip.
**Example:** 600-frame anime clip → set `skip_first_frames: 60`, `frame_count: 480` = 480 frames converted to realism starting at frame 60 ✅

---

## Output Resolution
Set `target_resolution_w` and `target_resolution_h` to your desired pixel dimensions.

| Format | W | H |
|---|---|---|
| Vertical (TikTok/Reels) | 1080 | 1920 |
| Square | 1080 | 1080 |
| Landscape | 1920 | 1080 |

Hit **▷ Run** when ready.

> **Prompt is optional** — but describing the real-world style, lighting, or setting you want can help guide the realism output (e.g. *"cinematic, natural lighting, photorealistic skin"*).

</details>
