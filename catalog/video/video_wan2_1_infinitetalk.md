# InfiniteTalk: Audio-Driven Full-Body Video Dubbing

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_wan2_1_infinitetalk)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_1_infinitetalk-1.webp" width="360" alt="InfiniteTalk: Audio-Driven Full-Body Video Dubbing video_wan2_1_infinitetalk-1.webp">

> Upload a source Image and target audio. Generate a full-body dubbed video with synchronized motion while preserving the original identity, background, and camera movement.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_1_infinitetalk.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan2_1_infinitetalk.json)

## Details

| | |
|---|---|
| Name | `video_wan2_1_infinitetalk` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.1 InfiniteTalk |
| Tags | Audio to Video, Lip Sync, Video |
| Type | open source |
| Date | 2026-01-26 |
| Author | ComfyUI |
| Download size | 27.6 GB |
| Min ComfyUI version | 0.17.0 |
| Usage | 77 |
| Nodes | 50 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadAudio` #24 | audio | audio_speaker1_woman.mp3 |
| input | `LoadImage` #32 | image | two_character_talking.png |
| input | `LoadAudio` #90 | audio | audio_speaker2_man.mp3 |
| output | `SaveVideo` #141 | video | video_wan2_1_infinitetalk.mp4 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `wav2vec2-chinese-base_fp16.safetensors` | `audio_encoders` | [link](https://huggingface.co/Kijai/wav2vec2_safetensors/resolve/main/wav2vec2-chinese-base_fp16.safetensors) |
| `Wan2_1-I2V-14B-480p_fp8_e4m3fn_scaled_KJ.safetensors` | `diffusion_models` | [link](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/resolve/main/I2V/Wan2_1-I2V-14B-480p_fp8_e4m3fn_scaled_KJ.safetensors) |
| `lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors` | `loras` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) |
| `wan2.1_infiniteTalk_multi_fp16.safetensors` | `model_patches` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/model_patches/wan2.1_infiniteTalk_multi_fp16.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `Wan2_1_VAE_bf16.safetensors` | `vae` | [link](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2_1_VAE_bf16.safetensors) |

## Subgraphs

- **InfiniteTalk (Base Generation)** (17 nodes)
- **InfiniteTalk (Base Generation)** (17 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `AudioEncoderEncode` | 4 | comfy-core |
| `MarkdownNote` | 3 |  |
| `AudioEncoderLoader` | 2 | comfy-core |
| `BasicScheduler` | 2 | comfy-core |
| `CFGGuider` | 2 | comfy-core |
| `CLIPLoader` | 2 | comfy-core |
| `CLIPTextEncode` | 2 | comfy-core |
| `ConditioningZeroOut` | 2 | comfy-core |
| `CreateVideo` | 2 | comfy-core |
| `KSamplerSelect` | 2 | comfy-core |
| `LoadAudio` | 2 | comfy-core |
| `LoraLoaderModelOnly` | 2 | comfy-core |
| `ModelPatchLoader` | 2 | comfy-core |
| `Painter` | 2 | comfy-core |
| `PrimitiveInt` | 2 | comfy-core |
| `RandomNoise` | 2 | comfy-core |
| `SamplerCustomAdvanced` | 2 | comfy-core |
| `SaveVideo` | 2 | comfy-core |
| `UNETLoader` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `WanInfiniteTalkToVideo` | 2 | comfy-core |
| `AudioConcat` | 1 | comfy-core |
| `BatchImagesNode` | 1 | comfy-core |
| `LoadImage` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>MarkdownNote</summary>

Each **Video Extend** group will extend 81/25=3.24s

So, if you want the output video to match the length of the input audio. For example, if your input audio is 9 seconds in total.

1. You need to manually box-select this Video Extend group. 
2. Press Ctrl-C, then Ctrl-Shift-V, to duplicate a new extend module.
3. Then linking the Previous `InfiniteTalk (Base Generation)`'s IMAGE output to the new **WanInfiniteTalkToVideo** node's `previous_frames`
4. Linking the Batch Images node's IMAGE output to the new Batch Images node's image1

</details>

<details><summary>MarkdownNote</summary>

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

**diffusion_models**

- [Wan2_1-I2V-14B-480p_fp8_e4m3fn_scaled_KJ.safetensors](https://huggingface.co/Kijai/WanVideo_comfy_fp8_scaled/resolve/main/I2V/Wan2_1-I2V-14B-480p_fp8_e4m3fn_scaled_KJ.safetensors) (15.5 GB)

**text_encoders**

- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) (6.27 GB)

**model_patches**

- [wan2.1_infiniteTalk_single_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/model_patches/wan2.1_infiniteTalk_single_fp16.safetensors) (4.77 GB)
- [wan2.1_infiniteTalk_multi_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/model_patches/wan2.1_infiniteTalk_multi_fp16.safetensors) (4.77 GB)

**audio_encoders**

- [wav2vec2-chinese-base_fp16.safetensors](https://huggingface.co/Kijai/wav2vec2_safetensors/resolve/main/wav2vec2-chinese-base_fp16.safetensors) (181.3 MB)

**vae**

- [Wan2_1_VAE_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2_1_VAE_bf16.safetensors) (242 MB)

**loras**

- [lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Lightx2v/lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors) (703.8 MB)


## Model Storage Location

```
📂 ComfyUI/
├── 📂 models/
│   ├── 📂 diffusion_models/
│   │   └─── Wan2_1-I2V-14B-480p_fp8_e4m3fn_scaled_KJ.safetensors
│   ├── 📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors
│   ├── 📂 model_patches/
│   │   ├─── wan2.1_infiniteTalk_single_fp16.safetensors
│   │   └─── wan2.1_infiniteTalk_multi_fp16.safetensors
│   ├── 📂 audio_encoders/
│   │   └─── wav2vec2-chinese-base_fp16.safetensors
│   ├── 📂 vae/
│   │   └─── Wan2_1_VAE_bf16.safetensors
│   ├── 📂 loras/
│   │   └─── lightx2v_I2V_14B_480p_cfg_step_distill_rank64_bf16.safetensors
```

## Report Issue

Note: Please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.

- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)
- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)
- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)

</details>

<details><summary>⚠️ IMPORTANT</summary>

- Upload the start frame, then right - click on the Load Image node and choose **[Open in MaskEditor](https://docs.comfy.org/interface/maskeditor)**.
- Use the brush to draw the mask for Character 1.
- For Character 2, you need to do the same thing: upload the first frame and draw a mask.

</details>
