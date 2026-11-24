# Wan Dancer: Music to Dance

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_wan_dancer)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_dancer-1.webp" width="360" alt="Wan Dancer: Music to Dance video_wan_dancer-1.webp">

> Generate minute-scale coherent dance videos from music using a hierarchical Wan Dancer framework. Input a music file and reference image to produce high-resolution dance videos with global structure and temporal continuity.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan_dancer.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan_dancer.json)

## Details

| | |
|---|---|
| Name | `video_wan_dancer` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan |
| Tags | Audio to Video |
| Type | open source |
| Date | 2026-07-14 |
| Author | ComfyUI |
| Download size | 49.3 GB |
| Min ComfyUI version | 0.21.0 |
| Usage | 30 |
| Nodes | 75 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #547 | image | blue_dancer.png |
| input | `LoadAudio` #548 | audio | wan_dancer_reference_audio.mp3 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `clip_vision_h.safetensors` | `clip_vision` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) |
| `wan2.2_dancer_14b_global_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan-Dancer/resolve/main/diffusion_models/wan2.2_dancer_14b_global_fp8_scaled.safetensors) |
| `wan2.2_dancer_14b_local_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan-Dancer/resolve/main/diffusion_models/wan2.2_dancer_14b_local_fp8_scaled.safetensors) |
| `lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) |
| `umt5_xxl_fp16.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp16.safetensors) |
| `Wan2_1_VAE_bf16.safetensors` | `vae` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2_1_VAE_bf16.safetensors) |

## Subgraphs

- **Prompt Selector** (4 nodes)
- **Prompt Selector** (4 nodes)
- **Image to Video (Wan Dancer)** (63 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `PrimitiveInt` | 8 | comfy-core |
| `StringReplace` | 4 | comfy-core |
| `CLIPTextEncode` | 3 | comfy-core |
| `ComfyMathExpression` | 3 | comfy-core |
| `ComfySwitchNode` | 3 | comfy-core |
| `CustomCombo` | 3 | comfy-core |
| `MarkdownNote` | 3 |  |
| `BasicScheduler` | 2 | comfy-core |
| `CLIPVisionEncode` | 2 | comfy-core |
| `CreateVideo` | 2 | comfy-core |
| `KSamplerSelect` | 2 | comfy-core |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `PreviewAny` | 2 | comfy-core |
| `PrimitiveFloat` | 2 | comfy-core |
| `RegexExtract` | 2 | comfy-core |
| `SaveVideo` | 2 | comfy-core |
| `StringConcatenate` | 2 | comfy-core |
| `UNETLoader` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `WanDancerEncodeAudio` | 2 | comfy-core |
| `WanDancerVideo` | 2 | comfy-core |
| `CFGGuider` | 1 | comfy-core |
| `CLIPLoader` | 1 | comfy-core |
| `CLIPVisionLoader` | 1 | comfy-core |
| `ConditioningZeroOut` | 1 | comfy-core |
| `ImageFromBatch` | 1 | comfy-core |
| `LatentCutToBatch` | 1 | comfy-core |
| `LoadAudio` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |
| `ModelSamplingSD3` | 1 | comfy-core |
| `PrimitiveBoolean` | 1 | comfy-core |
| `PrimitiveStringMultiline` | 1 | comfy-core |
| `RandomNoise` | 1 | comfy-core |
| `RebatchImages` | 1 | comfy-core |
| `ResizeImageMaskNode` | 1 | comfy-core |
| `SamplerCustom` | 1 | comfy-core |
| `SamplerCustomAdvanced` | 1 | comfy-core |
| `SkipLayerGuidanceDiTSimple` | 1 | comfy-core |
| `TrimAudioDuration` | 1 | comfy-core |
| `VAELoader` | 1 | comfy-core |
| `WanDancerPadKeyframesList` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)

## Model Links

- [Hugging Face:Comfy-Org/Wan-Dancer](https://huggingface.co/Comfy-Org/Wan-Dancer)
- [ModelScope:Comfy-Org/Wan-Dancer](https://modelscope.cn/models/Comfy-Org/Wan-Dancer)
- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

**diffusion_models**

- [wan2.2_dancer_14b_global_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan-Dancer/resolve/main/diffusion_models/wan2.2_dancer_14b_global_fp8_scaled.safetensors) (17.08 GB)
- [wan2.2_dancer_14b_local_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan-Dancer/resolve/main/diffusion_models/wan2.2_dancer_14b_local_fp8_scaled.safetensors) (17.08 GB)

**loras**

- [lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) (703.8 MB)

**text_encoders**

- [umt5_xxl_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp16.safetensors) (10.59 GB)

**clip_vision**

- [clip_vision_h.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/clip_vision/clip_vision_h.safetensors) (1.18 GB)

**vae**

- [Wan2_1_VAE_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2_1_VAE_bf16.safetensors) (242 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   ├── wan2.2_dancer_14b_global_fp8_scaled.safetensors
│   │   └── wan2.2_dancer_14b_local_fp8_scaled.safetensors
│   ├── 📂 loras/
│   │   └── lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
│   ├── 📂 text_encoders/
│   │   └── umt5_xxl_fp16.safetensors
│   ├── 📂 clip_vision/
│   │   └── clip_vision_h.safetensors
│   └── 📂 vae/
│       └── Wan2_1_VAE_bf16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud updates follow stable releases, so some nightly-supported models may not be available yet.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>Note：⚠️</summary>

This model samples 149 frames at once, so it needs a large amount of VRAM. Before you run this workflow, please make sure you have a powerful GPU.

By default, this workflow sets the output duration to 5 seconds.

</details>

<details><summary>MarkdownNote</summary>

The original prompt is in Chinese. You can try to add more options here.

The base options here are the default options provided by the Wan team.

</details>
