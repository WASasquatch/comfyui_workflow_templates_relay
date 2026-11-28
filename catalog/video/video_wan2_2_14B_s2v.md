# Wan2.2-S2V Audio-Driven Video Generation

[← Video](README.md) · [All categories](../README.md) · [All templates](../all.md) · [Open in browser](https://wasasquatch.github.io/comfyui_workflow_templates_relay/#t=video_wan2_2_14B_s2v)

<img src="https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_s2v-1.webp" width="360" alt="Wan2.2-S2V Audio-Driven Video Generation video_wan2_2_14B_s2v-1.webp">

> Transform static images and audio into dynamic videos with perfect synchronization and minute-level generation.

## Get the workflow

- **[Download JSON](https://raw.githubusercontent.com/Comfy-Org/workflow_templates/main/templates/video_wan2_2_14B_s2v.json)** — save it, then drag it onto the ComfyUI canvas (or *Workflow → Open*).
- [View on GitHub](https://github.com/Comfy-Org/workflow_templates/blob/main/templates/video_wan2_2_14B_s2v.json)
- [Tutorial](https://docs.comfy.org/tutorials/video/wan/wan2-2-s2v)

## Details

| | |
|---|---|
| Name | `video_wan2_2_14B_s2v` |
| Category | Foundation › Video |
| Output | video |
| Models | Wan2.2, Wan |
| Tags | Video, Audio to Video |
| Type | open source |
| Date | 2025-08-02 |
| Author | ComfyUI |
| Download size | 23.5 GB |
| Min ComfyUI version | 0.3.55 |
| Usage | 99 |
| Nodes | 74 |

## Inputs & outputs

| Direction | Node | Media | File |
|---|---|---|---|
| input | `LoadImage` #52 | image | video_wan2_2_14B_s2v_reference_image.jpg |
| input | `LoadAudio` #58 | audio | video_wan2_2_14B_s2v_input_audio.MP3 |

## Model files

| File | Folder (`ComfyUI/models/…`) | Download |
|---|---|---|
| `wav2vec2_large_english_fp16.safetensors` | `audio_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/audio_encoders/wav2vec2_large_english_fp16.safetensors) |
| `wan2.2_s2v_14B_fp8_scaled.safetensors` | `diffusion_models` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_s2v_14B_fp8_scaled.safetensors) |
| `wan2.2_t2v_lightx2v_4steps_lora_v1.1_high_noise.safetensors` | `loras` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/loras/wan2.2_t2v_lightx2v_4steps_lora_v1.1_high_noise.safetensors) |
| `umt5_xxl_fp8_e4m3fn_scaled.safetensors` | `text_encoders` | [link](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) |
| `wan_2.1_vae.safetensors` | `vae` | [link](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) |

## Subgraphs

- **Video S2V Extend** (3 nodes)
- **Video S2V Extend** (3 nodes)
- **Video S2V Extend** (3 nodes)
- **Video S2V Extend** (3 nodes)
- **Video S2V Extend** (3 nodes)
- **Video S2V Extend** (3 nodes)

## Nodes used

| Node | Count | Pack |
|---|---|---|
| `KSampler` | 8 | comfy-core |
| `LatentConcat` | 8 | comfy-core |
| `MarkdownNote` | 7 |  |
| `PrimitiveInt` | 6 | comfy-core |
| `WanSoundImageToVideoExtend` | 6 | comfy-core |
| `CLIPTextEncode` | 4 | comfy-core |
| `Note` | 4 |  |
| `AudioEncoderEncode` | 2 | comfy-core |
| `AudioEncoderLoader` | 2 | comfy-core |
| `CLIPLoader` | 2 | comfy-core |
| `CreateVideo` | 2 | comfy-core |
| `ImageFromBatch` | 2 | comfy-core |
| `LatentCut` | 2 | comfy-core |
| `LoadAudio` | 2 | comfy-core |
| `LoadImage` | 2 | comfy-core |
| `ModelSamplingSD3` | 2 | comfy-core |
| `PrimitiveFloat` | 2 | comfy-core |
| `SaveVideo` | 2 | comfy-core |
| `UNETLoader` | 2 | comfy-core |
| `VAEDecode` | 2 | comfy-core |
| `VAELoader` | 2 | comfy-core |
| `WanSoundImageToVideo` | 2 | comfy-core |
| `LoraLoaderModelOnly` | 1 | comfy-core |

## Notes embedded in the workflow

<details><summary>Note</summary>

```text
Stupid hack to fix the first frame being overbaked by the VAE, double the first frame and remove it after decoding.
```

</details>

<details><summary>Batch sizes</summary>

## Batch sizes
Batch sizes depend on how many Video S2V Extend subgraphs you have added to the workflow.

Each Video S2V Extend subgraph will add 77 frames to the final output.

Example:

If you added 1 Video S2V Extend subgraph, you should set the batch size to 2.

We added 2 Video S2V Extend subgraphs, so the batch size value is 3.

## Chunk length

77 is the default length from the WAN2.2S2V official code. This model needs at least 73 frames. If you set the value too high, it might cause an out-of-memory issue.

So you can just leave 77 as it is.

</details>

<details><summary>! Important</summary>

```text
If you need longer video output, just select one subgraph below, then use Ctrl+C and Ctrl+Shift+V to copy and paste the Video S2V Extend subgraph. Each of them will extend the other frames you set to the chunk length; by default, it's 77 frames.
```

</details>

<details><summary>Note</summary>

```text
Stupid hack to fix the first frame being overbaked by the VAE, double the first frame and remove it after decoding.
```

</details>

<details><summary>Batch sizes</summary>

## Batch sizes
Batch sizes depend on how many Video S2V Extend subgraphs you have added to the workflow.

Each Video S2V Extend subgraph will add 77 frames to the final output.

Example:

If you added 1 Video S2V Extend subgraph, you should set the batch size to 2.

We added 2 Video S2V Extend subgraphs, so the batch size value is 3.

## Chunk length

77 is the default length from the WAN2.2S2V official code. This model needs at least 73 frames. If you set the value too high, it might cause an out-of-memory issue.

So you can just leave 77 as it is.

</details>

<details><summary>Sampler settings</summary>

| model            | Steps | cfg |
|---------------------|---------------|---------------|
| With 4 steps lightning LoRA            | 4                | 1.0               |
| Without 4 Steps lightning LoRA    | 20               | 6.0               |

</details>

<details><summary>Sampler settings</summary>

| model            | Steps | cfg |
|---------------------|---------------|---------------|
| With 4 steps lightning LoRA            | 4                | 1.0               |
| Without 4 Steps lightning LoRA    | 20               | 6.0               |

</details>

<details><summary>MarkdownNote</summary>

This is the 20-step workflow. We put it here in case some users don't know how to modify the workflow that with Wan2.2 lightning LoRA. If you want to enable it, box-select the workflow and then use Ctrl+B to enable it.

</details>

<details><summary>About lightning LoRA</summary>

```text
Tested all wan2.2 lightning LoRAs; all worked, but many keys didn't match. However, because it reduces generation time a lot, we added this lightning model. If you find the output quality is too bad, you can try the 20 steps workflow without lightning LoRA.
```

</details>

<details><summary>About fp8_scaled and bf16</summary>

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)
- [ModelScope:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)

You can find both models [Here](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/tree/main/split_files/diffusion_models)

- [wan2.2_s2v_14B_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_s2v_14B_fp8_scaled.safetensors) (15.27 GB)
- [wan2.2_s2v_14B_bf16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_s2v_14B_bf16.safetensors) (30.35 GB)

This template is using wan2.2_s2v_14B_fp8_scaled.safetensors, which requires less VRAM. But you can try wan2.2_s2v_14B_bf16.safetensors to reduce degradation.

</details>

<details><summary>Model Links</summary>

## Model Links

- [Hugging Face:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)
- [ModelScope:Comfy-Org/Wan_2.2_ComfyUI_Repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.2_ComfyUI_Repackaged)
- [Hugging Face:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged)
- [ModelScope:Comfy-Org/Wan_2.1_ComfyUI_repackaged](https://modelscope.cn/models/Comfy-Org/Wan_2.1_ComfyUI_repackaged)

[Tutorial](https://docs.comfy.org/tutorials/video/wan/wan2-2-s2v
) 

**diffusion_models**       
- [wan2.2_s2v_14B_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_s2v_14B_fp8_scaled.safetensors) (15.27 GB)
- [wan2.2_s2v_14B_bf16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/diffusion_models/wan2.2_s2v_14B_bf16.safetensors) (30.35 GB)

**audio_encoders**
- [wav2vec2_large_english_fp16.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/audio_encoders/wav2vec2_large_english_fp16.safetensors) (601.8 MB)

**vae**
- [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.2_ComfyUI_Repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) (242.1 MB)

**text_encoders**   
- [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) (6.27 GB)


```
ComfyUI/
├───📂 models/
│   ├───📂 diffusion_models/
│   │   ├─── wan2.2_s2v_14B_fp8_scaled.safetensors
│   │   └─── wan2.2_s2v_14B_bf16.safetensors #  The bf16 model will cause less degradation
│   ├───📂 text_encoders/
│   │   └─── umt5_xxl_fp8_e4m3fn_scaled.safetensors 
│   ├───📂 audio_encoders/ # Create one if you can't find this folder
│   │   └─── wav2vec2_large_english_fp16.safetensors 
│   └───📂 vae/
│       └── wan_2.1_vae.safetensors
```

</details>
